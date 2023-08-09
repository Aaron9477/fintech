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
warnings.filterwarnings('default')
from typing import Union

#全局变量设置
path_基本数据 = r'C:\Users\12617\Desktop\代销图鉴0612(进度至收益风险分析）\基础数据.xlsx'
path_代销数据 = r'C:\Users\12617\Desktop\代销图鉴0612(进度至收益风险分析）\代销数据0526.xlsx'
path_代销机构数据 = r'C:\Users\12617\Desktop\代销图鉴0612(进度至收益风险分析）\wind_bank_info_230628.csv'
path_现金管理类基础数据 = r'C:\Users\12617\Desktop\py_all_net_value_0704.csv'
path_outputdir = r'C:\Users\12617\Desktop\代销图鉴0612(进度至收益风险分析）\数据更新'

#普通数据时间区间
start_date = dt.datetime(2023,5,1)#需要更新的数据起始时间
end_date = dt.datetime(2023,5,31)#需要更新的数据结束时间（一般为最新时间）

#导入数据
df1 = pd.read_excel(path_基本数据,index_col=0).infer_objects()
df1['理财公司简称'] = df1.apply(lambda x:x[0].split('有限')[0],axis=1)
df2 = pd.read_excel(path_代销数据)
df8 = pd.read_csv(path_代销机构数据,encoding='utf-8').drop_duplicates(subset='comp_simple_name', keep='first', inplace=False)
df9 = pd.read_csv(path_现金管理类基础数据,encoding='utf-8')
df9['EndDate'] = df9['EndDate'].astype('datetime64')

#会用到的依赖函数
def preprocess(input_df, statistics_date,product_exist=True):
    # 筛选存续期产品
    if product_exist:
        input_df = get_product_exist(input_df, statistics_date)
    input_df_copy = input_df.copy()

    def temp_func(x):
        if(x['ProductType']=='母产品'): return 1
        elif(x['ProductType']=='产品'): return 2
        elif(x['ProductType']=='子产品'): return 3
        else: return np.NaN
    input_df['tag'] = input_df.apply(temp_func,axis = 1)
    input_df['index'] = input_df.index
    input_df = input_df.dropna(subset=['tag'])
    target_index = list(input_df.groupby('RegistrationCode')[['tag','index']].apply(lambda x:x.sort_values(by='tag',ascending=True)['index'].iloc[0]))
    output_df = input_df_copy.loc[target_index,:]
    return output_df

# 筛选存续期产品
def get_product_exist(input, statistics_date):
    input_df = input.copy()
    input_df = input_df[(((input_df['MaturityDate'].isnull()) | (input_df['MaturityDate'] > statistics_date)))
                        & (input_df['product_establish_date'] < statistics_date)]
    return input_df

#剔除母子关系的数据
def exclude_mother_child_relation(input_df):
    return input_df[~(input_df['ParentCompName']==input_df['代销机构'])]

#填补缺失值
def func10(x,null_n=8):
    row=x.shape[0]
    i=0
    while i<row:
        if pd.isnull(x.iloc[i,-1]):
            k=1
            if i+k < row:
                while pd.isnull(x.iloc[i+k,-1]):
                    k=k+1
                    if i+k >= row:
                        break
            #print(k)
            if k<=null_n:
                x.iloc[i:i+k,-1]=x.iloc[i-1,-1]
                i=i+k
            else:
                i=i+k
        else:
            i=i+1
    return x    

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
#处理现金管理类产品的净值数据
import datetime
def get_processed_nv_data(net_value_df_all,lc_code,begin_date,end_date,is_cash=False):
    # net_value_df_all = reader.get_code_net_value_from_local(begin_date=begin_date, end_date=end_date)
    # groupd = net_value_df_all.groupby('FinProCode')
    net_value_df = net_value_df_all[net_value_df_all['FinProCode'] == lc_code].copy()
    net_value_df = net_value_df.reset_index(drop=True)
    data = GetProcessedNavData(net_value_df=net_value_df, licai_code=lc_code, begin_date=begin_date,
                               end_date=end_date, is_cash=is_cash)
    # 防止现金管理类识别错误，导致7日年化的数据却采用了净值计算
    nav_column = data.columns[2]
    if is_cash:
        if nav_column in ['LatestWeeklyYield']:
            return data
        else:
            return None
    else:
        if nav_column in ['AccumulatedUnitNV','UnitNV']:
            return data
        else:
            return None
        
def GetProcessedNavData(net_value_df: pd.DataFrame,
                        licai_code: str,
                        begin_date: Union[str,None] = None,
                        end_date: Union[str,None] = None,
                        is_cash: object = False,
                        spec_column: object = None) -> Union[pd.DataFrame, None]:
    """
    获取单个产品的净值，自动获取净值字段，如果是现金管理产品，根据7日年化收益率、万分收益和净值 自动转化为7日年化收益率
    :param net_value_df:
    :param is_cash: True 代表现金管理产品，False 代表非现金产品
    :param spec_column: 特殊指定相应字段，针对特殊个例情况
    :param licai_code:
    :param begin_date:
    :param end_date:
    :return: df
    """

    if net_value_df.empty:
        return None
    # 特殊处理：
    if spec_column is not None:
        return net_value_df[['FinProCode', 'EndDate', spec_column]]
    else:
        # 正常处理
        if begin_date is None:
            begin_date = datetime.datetime.strftime(net_value_df['EndDate'].iloc[0],'%Y%m%d')
        if end_date is None:
            end_date = datetime.datetime.strftime(net_value_df['EndDate'].iloc[-1],'%Y%m%d')

        net_value_df['UnitNVRestored'] = np.nan
        period = (datetime.datetime.strptime(end_date, '%Y%m%d') - datetime.datetime.strptime(begin_date,'%Y%m%d')).days
        not_null_count = net_value_df[
            ['DailyProfit', 'LatestWeeklyYield', 'UnitNV', 'AccumulatedUnitNV', 'UnitNVRestored']].apply(
            lambda x: len(x.dropna()) / len(x))
        if not is_cash:
            # 非现金产品，在复权净值、单位净值和累计净值中挑选
            if not_null_count['UnitNVRestored'] > 0:
                return net_value_df[['FinProCode', 'EndDate', 'UnitNVRestored']]

            if not_null_count['AccumulatedUnitNV'] == 0:  # 判断累计净值数据是否为空
                if not_null_count['UnitNV'] == 0:
                    return None
                else:
                    return net_value_df[['FinProCode', 'EndDate', 'UnitNV']]
            else:
                if not_null_count['UnitNV'] == 0:
                    return net_value_df[['FinProCode', 'EndDate', 'AccumulatedUnitNV']]
                else:
                    # 判断两个数据是否有差异数据
                    tmp = net_value_df[['UnitNV', 'AccumulatedUnitNV']].dropna(subset=['UnitNV', 'AccumulatedUnitNV'])
                    if tmp.empty:
                        return None
                    else:
                        tmp_diff_logic = tmp.apply(lambda x: 1 if x.UnitNV != x.AccumulatedUnitNV else 0, axis=1).sum()
                        if tmp_diff_logic == 0:  # 单位净值和累计净值数据一致
                            # 打分选择字段
                            not_null_count = not_null_count[['UnitNV', 'AccumulatedUnitNV']].copy()
                            period_nav_not_null_period = pd.Series()
                            try:
                                period_nav_not_null_period['UnitNV'] = (net_value_df.dropna(subset=['UnitNV'])[
                                                                            'EndDate'].iloc[-1] -
                                                                        net_value_df.dropna(subset=['UnitNV'])[
                                                                            'EndDate'].iloc[0]).days / period
                            except IndexError:
                                period_nav_not_null_period['UnitNV'] = 0
                            try:
                                period_nav_not_null_period['AccumulatedUnitNV'] = (net_value_df.dropna(
                                    subset=['AccumulatedUnitNV'])['EndDate'].iloc[-1] - net_value_df.dropna(
                                    subset=['AccumulatedUnitNV'])[
                                                                                       'EndDate'].iloc[
                                                                                       0]).days / period + 0.0001
                            except IndexError:
                                period_nav_not_null_period['AccumulatedUnitNV'] = 0
                            score = period_nav_not_null_period * 0.6 + not_null_count * 0.4
                            score = score.sort_values()
                            chosed_nav_col = score.idxmax()
                            return net_value_df[['FinProCode', 'EndDate', chosed_nav_col]]
                        else:
                            return net_value_df[['FinProCode', 'EndDate', 'AccumulatedUnitNV']]
        else:
            # 现金管理产品，在7日年化、万分收益和净值中挑选
            # 万分收益和7日年化打分判断
            not_null_count_cash = not_null_count[['DailyProfit', 'LatestWeeklyYield']].copy()
            period_cash_not_null_period = pd.Series()
            try:
                period_cash_not_null_period['DailyProfit'] = (net_value_df.dropna(subset=['DailyProfit'])[
                                                                  'EndDate'].iloc[-1] -
                                                              net_value_df.dropna(subset=['DailyProfit'])[
                                                                  'EndDate'].iloc[0]).days / period
            except IndexError:
                period_cash_not_null_period['DailyProfit'] = 0
            try:
                period_cash_not_null_period['LatestWeeklyYield'] = (net_value_df.dropna(subset=['LatestWeeklyYield'])[
                                                                        'EndDate'].iloc[-1] -
                                                                    net_value_df.dropna(subset=['LatestWeeklyYield'])[
                                                                        'EndDate'].iloc[0]).days / period + 0.0001
            except IndexError:
                period_cash_not_null_period['LatestWeeklyYield'] = 0
            score = period_cash_not_null_period * 0.6 + not_null_count_cash * 0.4
            score = score.sort_values()
            if score.max() >= 0.1:
                # 选择7日年化或者万份收益
                chosed_cash__col = score.idxmax()
                if chosed_cash__col == 'LatestWeeklyYield':
                    return net_value_df[['FinProCode', 'EndDate', 'LatestWeeklyYield']].copy()
                elif chosed_cash__col == 'DailyProfit':
                    net_value_df = net_value_df[['FinProCode', 'EndDate', 'DailyProfit']].copy()
                    net_value_df['LatestWeeklyYield'] = net_value_df['DailyProfit'].rolling(7).apply(
                        lambda x: np.power(x.apply(lambda i: (1 + i / 10000)).prod(), 365 / 7) - 1)
                    return net_value_df[['FinProCode', 'EndDate', 'LatestWeeklyYield']].copy()

                else:
                    raise ValueError('impossible error......')
            else:
                # 如果得分都很低的话，就采用净值来判断
                nav_df = GetProcessedNavData(net_value_df=net_value_df,licai_code=licai_code, begin_date=begin_date, end_date=end_date,
                                             is_cash=False)
                if nav_df is None:
                    return None
                else:
                    nav_df.columns = ['FinProCode', 'EndDate', 'net_value']
                    # 判断小数位数
                    digital_num = len(str(nav_df['net_value'].dropna().iloc[0]).split('.')[1]) + 1
                    if digital_num >= 6:
                        nav_df['ret'] = nav_df['net_value'].pct_change()
                        nav_df['LatestWeeklyYield'] = nav_df['ret'].rolling(7).apply(lambda x: (x.mean() * 365))
                        return nav_df[['FinProCode', 'EndDate', 'LatestWeeklyYield']]

                    else:
                        raise ValueError('现金管理类产品，净值数据精度不足，不能转化为7日年化收益......')
                        
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
现金管理类_七日年化=现金管理类_七日年化.groupby('FinProCode').apply(func10)
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