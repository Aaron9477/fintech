# -*- coding: utf-8 -*-
# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月25日
# @Author    : WSS
# @File      : main_xianjinguanli_df9result
# @Project   : 银行理财代销图鉴
# @Function  ：生成【现金管理类_七日年化】依赖表
# --------------------------------

#需要用到的库
import pandas as pd
import datetime as dt
from tqdm import tqdm
import numpy as np
import warnings

from fillna_within_n import func_vertical_fillna
from get_processed_nv_datas import get_processed_nv_data
from preprocess import preprocess
warnings.filterwarnings('default')
from typing import Union

#全局变量设置
path_基本数据 = './raw_datas/基础数据.xlsx'
path_代销数据 = './raw_datas/代销数据0526.xlsx'
path_代销机构数据 = './raw_datas/wind_bank_info_230628.csv'
path_现金管理类基础数据 = './raw_datas/py_all_net_value_0704.csv'
path_outputdir = './raw_datas'

#普通数据时间区间
start_date = dt.datetime(2023,5,1)#需要更新的数据起始时间
end_date = dt.datetime(2023,5,31)#需要更新的数据结束时间（一般为最新时间）

#导入数据
df1 = pd.read_excel(path_基本数据,index_col=0).infer_objects()
df1['理财公司简称'] = df1.apply(lambda x:x[0].split('有限')[0],axis=1)
df2 = pd.read_excel(path_代销数据)
df8 = pd.read_csv(path_代销机构数据,encoding='utf-8').drop_duplicates(subset='comp_simple_name', keep='first', inplace=False)
df9 = pd.read_csv(path_现金管理类基础数据,encoding='utf-8')
df9['EndDate'] = df9['EndDate'].astype('datetime64[ns]')

#会用到的依赖函数
def np_average_juzhen (values):
    if values.shape[0]==1:
        #print(values.shape)
        return values
    else:
        if (values['AssetValue'].notna().sum()==0)|((values['AssetValue']).sum()<0.0000001):
            weight_ave=pd.DataFrame()
            weight_ave=values.iloc[:,:-1]
            weight_ave['count']=values.iloc[:,:-1].count(axis=1)
            #print(weight_ave)
            result=weight_ave.sort_values(by='count',axis=0,ascending=False).iloc[:1,:]
            #print(result.shape)
            #print(weight_ave.sort_values(by='count',axis=0,ascending=False).index[0])
            return result
        else:
            weight_ave=pd.DataFrame()
            weight_ave=values.iloc[:,:-1]
            col=weight_ave.columns
            weight_ave['weight']=values['AssetValue'].copy()
            #weight_ave=weight_ave.dropna()
            result=pd.DataFrame(index=[0],columns=values.columns)
            for i in col:
                if ((weight_ave[i]).notna()*weight_ave['weight']).sum()==0:
                    result.loc[0,i]=np.NaN
                else:
                    result.loc[0,i]=(weight_ave[i] * weight_ave['weight']).sum() / ((weight_ave[i]).notna()*weight_ave['weight']).sum()
            #print(result.shape)
            return result

warnings.filterwarnings("ignore")
                        
现金管理类_七日年化 = pd.DataFrame()
lc_codes = df1[df1['InvestmentType']=='现金管理类']['FinProCode']
missing_lc_codes = []
for lc_code in tqdm(lc_codes):
    try:
        if 现金管理类_七日年化.empty:
            现金管理类_七日年化 = get_processed_nv_data(df9,lc_code,begin_date=None,end_date=None,is_cash=True)
        else:
            现金管理类_七日年化 = pd.concat([现金管理类_七日年化,get_processed_nv_data(df9,lc_code,begin_date='20210101',end_date='20230629',is_cash=True)],axis=0)
    except ValueError:
        missing_lc_codes.append(lc_code)
        #print(lc_code,"现金管理类产品，净值数据精度不足，不能转化为7日年化收益......")
    except AttributeError:
        continue
print('以下现金管理类产品，净值数据精度不足，不能转化为7日年化收益',missing_lc_codes)
warnings.filterwarnings("default")

#填补缺失值，默认n=8
现金管理类_七日年化=现金管理类_七日年化.groupby('FinProCode').apply(func_vertical_fillna)
现金管理类_七日年化_矩阵=现金管理类_七日年化.set_index(['FinProCode','EndDate']).unstack()['LatestWeeklyYield']
现金管理类_七日年化_矩阵_reg=pd.merge(现金管理类_七日年化_矩阵,df1[['RegistrationCode','FinProCode','AssetValue']],how='left',on='FinProCode')
#对同一注册编号的多个产品 根据assetvalue 进行加权平均
现金管理类_七日年化_矩阵_regave=现金管理类_七日年化_矩阵_reg.groupby('RegistrationCode').apply(np_average_juzhen)
df1_temp_未筛选=preprocess(df1,start_date,False)
df1_temp_未筛选 = df1_temp_未筛选[df1_temp_未筛选['InvestmentType']=='现金管理类']
现金管理类_七日年化_矩阵_regave.drop(['FinProCode','AssetValue','count'],axis = 1,inplace = True)
现金管理类_七日年化_矩阵_ave=pd.merge(现金管理类_七日年化_矩阵_regave,df1_temp_未筛选[['RegistrationCode','FinProCode']],how='inner',on=['RegistrationCode'])
现金管理类_七日年化_矩阵_ave.set_index('FinProCode',inplace = True)
现金管理类_七日年化_矩阵_ave.drop('RegistrationCode',axis = 1,inplace = True)

#将矩阵化的数据调整为竖列排布形式
现金管理类_七日年化_均值处理=现金管理类_七日年化_矩阵_ave.stack().reset_index()
现金管理类_七日年化_均值处理.columns=['FinProCode','EndDate','LatestWeeklyYield']
现金管理类_七日年化=现金管理类_七日年化_均值处理

#数据结果
现金管理类_七日年化.to_excel(path_outputdir+r'\现金管理类_七日年化.xlsx')