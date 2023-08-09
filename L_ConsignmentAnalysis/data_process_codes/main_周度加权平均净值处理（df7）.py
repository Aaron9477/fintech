# -*- coding: utf-8 -*-
# --------------------------------
# @Time      : 2023年7月31日
# @Author    : WSS
# @File      : main_周度加权平均净值处理
# @Project   : 银行理财代销图鉴
# @Function  ：使用【py_all_net_value_0704】和【all_nv_data_new】生成【周度净值_均值处理_未筛选存续期】依赖表
# --------------------------------


#需要用到的库
import pandas as pd
import datetime as dt
from tqdm import tqdm
import numpy as np
import warnings
from WeeklyYield_to_nv import WeeklyYield_to_nv
from fillna_within_n import func_horizontal_fillna, func_vertical_fillna

from preprocess import preprocess
warnings.filterwarnings('default')
from typing import Union
import datetime

# ## 现金管理数据-直接处理
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

##################################主程序#################################
#全局变量设置
path_基本数据 = r'..\raw_datas\基础数据.xlsx'
path_代销数据 = r'..\raw_datas\代销数据0526.xlsx'
path_代销机构数据 = r'..\raw_datas\wind_bank_info_230628.csv'
path_outputdir = r'..\raw_datas\数据更新'
path_现金管理类数据 = r'..\raw_datas\py_all_net_value_0704.csv'
path_周度日期 = r'..\raw_datas\周度日期20220101-20230630.xlsx'
path_new = r'..\raw_datas\all_nv_data_new.csv'
path_outputdir = r'..\raw_datas'

#read
df1 = pd.read_excel(path_基本数据,index_col=0).infer_objects()
df1['理财公司简称'] = df1.apply(lambda x:x[0].split('有限')[0],axis=1)
df2 = pd.read_excel(path_代销数据)
df_date = pd.read_excel(path_周度日期,header=None)
df8 = pd.read_csv(path_代销机构数据,encoding='utf-8').drop_duplicates(subset='comp_simple_name', keep='first', inplace=False)
df9 = pd.read_csv(path_现金管理类数据,encoding='utf-8')
df9['EndDate'] = df9['EndDate'].astype('datetime64')
df10 = pd.read_csv(path_new,encoding='utf-8')
df10['EndDate'] = df10['EndDate'].astype('datetime64')

#常规数据时间区间
start_date = dt.datetime(2023,5,1)#需要更新的数据起始时间
end_date = dt.datetime(2023,5,31)#需要更新的数据结束时间（一般为最新时间）
#时序数据时间区间
start_date_ts = dt.datetime(2022,5,31)#需要更新的数据起始时间
end_date_ts = dt.datetime(2023,5,31)#需要更新的数据结束时间（一般为最新时间）

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
#现金管理类_七日年化


# #### 填补缺失值-现金管理
#填补现金管理类数据缺失值
现金管理_填补缺失=现金管理类_七日年化.groupby('FinProCode').apply(func_vertical_fillna,null_n=8)
周度日期_list=list(df_date[0])
现金管理_矩阵=现金管理_填补缺失.set_index(['FinProCode','EndDate']).unstack()['LatestWeeklyYield']
现金管理_周度矩阵=现金管理_矩阵[周度日期_list]
#将现金管理类收益率数据转化为净值数据
现金管理_净值矩阵=现金管理_周度矩阵.apply(WeeklyYield_to_nv,axis=1)
#现金管理_净值矩阵


# ### 基础净值数据处理
日度数据_矩阵=df10.set_index(['FinProCode','EndDate']).unstack()['AccumulatedUnitNV_new']

#填补缺失值（已加进度条）
print('----------数据缺失值填补开始----------')
tqdm.pandas(desc='apply')
日度数据_填补缺失=日度数据_矩阵.progress_apply(func_horizontal_fillna,axis=1)
print('----------数据缺失值填补完毕----------')
#### 与现金管理数据合并
现金管理_净值矩阵.replace(0,np.NaN,inplace=True)
现金管理_净值矩阵=现金管理_净值矩阵.dropna(how='all')
现金管理_净值矩阵_list=list(现金管理_净值矩阵.index)
周度数据_填补缺失=日度数据_填补缺失[周度日期_list]
#将现金管理净值数据和非现金管理部分数据合并
现金管理_净值矩阵_交集=list(set(现金管理_净值矩阵.index)&set(周度数据_填补缺失.index))
周度数据_合并=周度数据_填补缺失.drop(index=现金管理_净值矩阵_交集)
周度净值数据_处理=pd.concat([周度数据_合并,现金管理_净值矩阵])
周度净值数据_处理=周度净值数据_处理.dropna(how='all')
#周度净值数据_处理

# ### 计算产品加权平均值
#计算加权平均净值
def np_average (values):
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
            result=pd.DataFrame(index=[0],columns=values.columns)
            for i in col:
                if ((weight_ave[i]).notna()*weight_ave['weight']).sum()==0:
                    result.loc[0,i]=np.NaN
                else:
                    result.loc[0,i]=(weight_ave[i] * weight_ave['weight']).sum() / ((weight_ave[i]).notna()*weight_ave['weight']).sum()
            #print(result.shape)
            return result

周度净值数据_合并=pd.merge(周度净值数据_处理,df1[['FinProCode','RegistrationCode','AssetValue']],on='FinProCode')
#计算净值的加权平均值（已加进度条）
print('----------加权平均净值计算开始----------')
tqdm.pandas(desc='apply')
周度净值_均值_=周度净值数据_合并.groupby(['RegistrationCode']).progress_apply(np_average)
print('----------加权平均净值计算完毕----------')
周度净值_均值=周度净值_均值_.drop(['FinProCode','AssetValue','count'], axis = 1)
#周度净值_均值
df1_temp_ = preprocess(df1,start_date,False)
周度净值_均值处理_未筛选存续期 = pd.merge(周度净值_均值,df1_temp_[['RegistrationCode','FinProCode']],on='RegistrationCode')
周度净值_均值处理_未筛选存续期['RegistrationCode']=周度净值_均值处理_未筛选存续期['FinProCode']
周度净值_均值处理_未筛选存续期.drop('FinProCode',axis=1,inplace=True)
周度净值_均值处理_未筛选存续期.rename(columns={"RegistrationCode": "FinProCode"},inplace=True)
#周度净值_均值处理_未筛选存续期
周度净值_均值处理_未筛选存续期.to_excel(path_outputdir+r'\周度净值_均值处理_未筛选存续期.xlsx',index=False)



