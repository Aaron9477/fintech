# -*- coding: utf-8 -*-
# --------------------------------
# @Time      : 2023年7月25日
# @Author    : WSS
# @File      : licai_comp_gonggao_analysis
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_公告分析_理财公司】依赖表
# --------------------------------
#需要用到的库
import pandas as pd
import numpy as np
import empyrical as emp

from preprocess import exclude_mother_child_relation, preprocess
from sectorize import sectorize
        
def func8(x):#计算近一年收益率，不满一年的使用已有数据年化
    x=x.iloc[-52:]
    if x.notna().sum()==0:
        return np.nan
    else:
        if(not np.isnan(x.iloc[-1]))&(not np.isnan(x.iloc[0])):
            return x.iloc[-1]/x.iloc[0]-1
        else:
            if (not np.isnan(x.iloc[-1])):
                x=x.fillna(method='ffill')
                return emp.annual_return((x/x.shift(1)-1).dropna(),annualization=52)
            else:
                k=-1
                for i in range(-1,-52,-1):
                    if (not np.isnan(x.iloc[i])):
                        k=i
                        break
                x=x.iloc[:k+1].fillna(method='ffill')
                return emp.annual_return((x/x.shift(1)-1).dropna(),annualization=52)

def np_average (values, weights): 
    weight_ave=pd.DataFrame()
    weight_ave['value']=values
    weight_ave['weight']=weights
    weight_ave=weight_ave.dropna()
    if sum (weight_ave['weight'])<0.0000001:
        return np.NaN
    else:
        if (weight_ave['value'].notna() *weight_ave['weight']).sum()==0:
            return np.NaN
        else:
            return (weight_ave['value'] * weight_ave['weight']).sum() / (weight_ave['value'].notna() *weight_ave['weight']).sum()
    

def licai_comp_gonggao_analysis(start_date,df1,df2,df7,result_type='single'):
    '''
    function:生成【底层数据_公告分析_理财公司】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df7:dataframe，银行理财产品产品的周度净值数据。
    return:
        - 底层数据_公告分析_理财公司:【底层数据_公告分析_理财公司】依赖表，用于更新理财图鉴。
    注释：result_type='licai_sector'
    '''
    print(" *生成【底层数据_公告分析_理财公司】依赖表...")
    df1_temp = preprocess(df1,start_date,False)
    #df2_temp = df2[(df2['代销开始日']<end_date)&(df2['代销结束日']>start_date)]
    df3_temp = pd.merge(df1_temp,df2,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
    df4_temp = exclude_mother_child_relation(df3_temp)
    df1_temp_list=df4_temp['FinProCode'].drop_duplicates()#剔除母子公司之间建立的代销关系
    
    df1_temp = sectorize(df1_temp,type = result_type)
    #将风险评级赋分
    df1_temp['risk_score']=''
    def risk_score(x):
        if x=='低':
            return 1
        elif x=='中低':
            return 2
        elif x=='中':
            return 3
        elif x=='中高':
            return 4
        elif x=='高':
            return 5
        else:
            return np.NaN
    df1_temp['risk_score']=df1_temp['RiskLevel'].apply(risk_score)
    #BenchmarkMin数据为%形式
    df1_temp['BenchmarkMin']=df1_temp['BenchmarkMin']/100
    df1_temp=df1_temp[['CompanyName','理财公司简称','FinProCode','InvestmentType','BenchmarkMin','AssetValue','RiskLevel','risk_score','RegistrationCode','ParentCompName']]
    #计算近一年的年化收益率
    df8=df7.copy()
    df7['interval_ret_annual']=df8.apply(lambda x : func8(x),axis=1)
    df5_temp = pd.merge(df1_temp,df7['interval_ret_annual'],how='left',on='FinProCode')
    #计算业绩基准均值
    group_=df5_temp.groupby(['理财公司简称','InvestmentType'])[['BenchmarkMin']].mean()
    group_.rename(columns={'BenchmarkMin':'BenchMin_ave'}, inplace = True)
    group_.replace(0,np.NaN,inplace=True)
    df5_temp=pd.merge(df5_temp,group_,left_on=['理财公司简称','InvestmentType'],right_index=True)

    for m in ['否','是']:
        if m=='是':
            df5_temp=df5_temp[df5_temp['FinProCode'].isin(df1_temp_list)]
        底层数据_公告分析_理财公司=df5_temp.groupby(['理财公司简称','InvestmentType'])[['BenchmarkMin']].mean()
        底层数据_公告分析_理财公司.rename(columns={'BenchmarkMin':'BenchMin_ave'}, inplace = True)
        #计算低于基准产品比例
        df5_temp['low_ret'] = df5_temp['interval_ret_annual'] < df5_temp['BenchMin_ave']
        底层数据_公告分析_理财公司['count']=df5_temp.groupby(['理财公司简称','InvestmentType'])['low_ret'].count()
        底层数据_公告分析_理财公司['count_low']=df5_temp.groupby(['理财公司简称','InvestmentType'])['low_ret'].sum()
        底层数据_公告分析_理财公司['低于基准比例']=底层数据_公告分析_理财公司['count_low']/底层数据_公告分析_理财公司['count']
        底层数据_公告分析_理财公司=底层数据_公告分析_理财公司.drop(['count','count_low'], axis=1)
        def low_rate(x):
            if np.isnan(x[0]):
                return np.NaN
            else:
                return x[1]
        底层数据_公告分析_理财公司['低于基准比例']=底层数据_公告分析_理财公司[['BenchMin_ave','低于基准比例']].apply(low_rate,axis=1)
        
        #复制index
        底层数据_公告分析_理财公司['type_']=底层数据_公告分析_理财公司.index.get_level_values('InvestmentType')
        底层数据_公告分析_理财公司['company']=底层数据_公告分析_理财公司.index.get_level_values('理财公司简称')
        #计算业绩基准排名
        底层数据_公告分析_理财公司[['rank','rank_sum']]=np.NaN
        for j in ['混合类','现金管理类','权益类','商品及金融衍生品类','固定收益类']:
            for i in 底层数据_公告分析_理财公司.loc[底层数据_公告分析_理财公司['type_']==j].index:
                底层数据_公告分析_理财公司.loc[i,'rank']=底层数据_公告分析_理财公司.loc[底层数据_公告分析_理财公司['type_']==j]['BenchMin_ave'].rank(method='min',ascending=False)[i]
                底层数据_公告分析_理财公司.loc[i,'rank_sum']=底层数据_公告分析_理财公司.loc[底层数据_公告分析_理财公司['type_']==j]['BenchMin_ave'].count()
        #计算市场平均基准比例
        底层数据_公告分析_理财公司=pd.merge(底层数据_公告分析_理财公司,df5_temp.groupby(['InvestmentType'])['BenchmarkMin'].mean(),left_on='type_',right_index=True)
        #计算加权风险等级
        df5_temp['risk_score']=pd.to_numeric(df5_temp['risk_score'])
        底层数据_公告分析_理财公司['weight_risk']=df5_temp.groupby(['理财公司简称','InvestmentType']).apply(lambda x: np_average(x['risk_score'], weights=x['AssetValue']))
        #计算市场平均风险等级
        risk_market=pd.DataFrame(df5_temp.groupby(['InvestmentType']).apply(lambda x: np_average(x['risk_score'], weights=x['AssetValue'])),columns=['risk_score_ave'])
        底层数据_公告分析_理财公司=pd.merge(底层数据_公告分析_理财公司,risk_market,on='InvestmentType')
        if m=='是':
            底层数据_公告分析_理财公司['是否剔除母子关系']='是'
            底层数据_公告分析_理财公司_是=底层数据_公告分析_理财公司.copy()
        if m=='否':
            底层数据_公告分析_理财公司['是否剔除母子关系']='否'
            底层数据_公告分析_理财公司_否=底层数据_公告分析_理财公司.copy()
    
    底层数据_公告分析_理财公司=pd.concat([底层数据_公告分析_理财公司_否,底层数据_公告分析_理财公司_是]) 
    底层数据_公告分析_理财公司=底层数据_公告分析_理财公司.reindex(columns=['company','type_', 'BenchMin_ave', '低于基准比例',  'rank', 'rank_sum',
           'BenchmarkMin', 'weight_risk', 'risk_score_ave', '是否剔除母子关系'])
    底层数据_公告分析_理财公司.replace('固定收益类','固定收益类（非现金）', inplace = True)
    底层数据_公告分析_理财公司.replace('商品及金融衍生品类','商品及衍生品类', inplace = True)
    底层数据_公告分析_理财公司.set_index('company',inplace=True)
    
    return 底层数据_公告分析_理财公司

