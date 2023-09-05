# -*- coding: utf-8 -*-
# --------------------------------
# @Time      : 2023年7月25日
# @Author    : WSS
# @File      : daixiao_comp_gonggao_analysis
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_公告分析_代销机构】依赖表
# --------------------------------
#需要用到的库
import pandas as pd
import numpy as np
import empyrical as emp

from preprocess import exclude_mother_child_relation, preprocess
from sectorize import sectorize



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
    

def daixiao_comp_gonggao_analysis(start_date,df1,df2,df7,result_type='single'):
    '''
    function:生成【底层数据_公告分析_代销机构】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df7:dataframe，银行理财产品产品的周度净值数据。
    return:
        - 底层数据_公告分析_代销机构:【底层数据_公告分析_代销机构】依赖表，用于更新理财图鉴。
    注释：result_type='daixiao_sector'
    '''
    print(" *生成【底层数据_公告分析_代销机构】依赖表...")
    df1_temp = preprocess(df1,start_date,False)
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
    #合并基础数据和产品收益风险数据
    df1_temp['BenchmarkMin']=df1_temp['BenchmarkMin']/100
    df1_temp=df1_temp[['CompanyName','理财公司简称','FinProCode','InvestmentType','BenchmarkMin','AssetValue','RiskLevel','risk_score','RegistrationCode','ParentCompName','comp_type']]
    #计算一年的收益率
    df8=df7.copy()
    df7['interval_ret_annual']=df8.apply(lambda x : func8(x),axis=1)
    df5_temp = pd.merge(df1_temp,df7['interval_ret_annual'],how='left',on='FinProCode')
    
    df3_temp = pd.merge(df5_temp,df2,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
    df3_temp = sectorize(df3_temp,type = result_type)
    df3_temp = df3_temp.drop_duplicates(subset=['代销机构','FinProCode'])
    for m in ['否','是']:
        if m=='是':
            df3_temp = pd.merge(df5_temp,df2,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
            df3_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系
            df3_temp = sectorize(df3_temp,type = result_type)
            df3_temp = df3_temp.drop_duplicates(subset=['代销机构','FinProCode'])
        #计算低于基准产品比例
        group_=df3_temp.groupby(['代销机构','InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].dropna().mean()).rename('BenchMin_ave').to_frame()
        # group_.rename(columns={'BenchmarkMin':'BenchMin_ave'}, inplace = True)
        group_.replace(0,np.NaN,inplace=True)
        df3_temp=pd.merge(df3_temp,group_,left_on=['代销机构','InvestmentType'],right_index=True)
        #使用组内均值填充BenchmarkMin和AssetValue缺失值
        底层数据_公告分析_代销机构=df3_temp.groupby(['代销机构','InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].dropna().mean()).rename('BenchMin_ave').to_frame()
        #计算低于基准产品比例
        def low_bench_ratio(x):
            try:
                x = x.drop_duplicates(subset='RegistrationCode')
                x = x.dropna(subset=['BenchmarkMin','interval_ret_annual'])
                num = len(x)
                lower = len(x[x['interval_ret_annual']<x['BenchmarkMin']])
                return lower / num
            except:
                return np.NaN
        底层数据_公告分析_代销机构['低于基准比例']=df3_temp.groupby(['理财公司简称','InvestmentType'])[['BenchmarkMin','interval_ret_annual','RegistrationCode']].apply(low_bench_ratio)
        #复制index
        底层数据_公告分析_代销机构['type_']=底层数据_公告分析_代销机构.index.get_level_values('InvestmentType')
        底层数据_公告分析_代销机构['代销机构']=底层数据_公告分析_代销机构.index.get_level_values('代销机构')
        #计算业绩基准排名
        底层数据_公告分析_代销机构[['rank','rank_sum']]=np.NaN
        for j in ['混合类','现金管理类','权益类','商品及金融衍生品类','固定收益类']:
            for i in 底层数据_公告分析_代销机构.loc[底层数据_公告分析_代销机构['type_']==j].index:
                底层数据_公告分析_代销机构.loc[i,'rank']=底层数据_公告分析_代销机构.loc[底层数据_公告分析_代销机构['type_']==j]['BenchMin_ave'].rank(method='min',ascending=False)[i]
                底层数据_公告分析_代销机构.loc[i,'rank_sum']=底层数据_公告分析_代销机构.loc[底层数据_公告分析_代销机构['type_']==j]['BenchMin_ave'].count()
        #计算市场平均基准比例
        底层数据_公告分析_代销机构=pd.merge(底层数据_公告分析_代销机构,df3_temp.groupby(['InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].dropna().mean()).rename('BenchmarkMin').to_frame(),left_on='type_',right_index=True)
        #计算加权风险等级
        df3_temp['risk_score']=pd.to_numeric(df3_temp['risk_score'])
        底层数据_公告分析_代销机构['weight_risk']=df3_temp.groupby(['代销机构','InvestmentType']).apply(lambda x: np_average(x['risk_score'], weights=x['AssetValue']))
        #计算市场平均风险等级
        risk_market=pd.DataFrame(df3_temp.groupby(['InvestmentType']).apply(lambda x: np_average(x['risk_score'], weights=x['AssetValue'])),columns=['risk_score_ave'])
        底层数据_公告分析_代销机构=pd.merge(底层数据_公告分析_代销机构,risk_market,on='InvestmentType')
        if m=='是':
            底层数据_公告分析_代销机构['是否剔除母子关系']='是'
            底层数据_公告分析_代销机构_是=底层数据_公告分析_代销机构.copy()
        if m=='否':
            底层数据_公告分析_代销机构['是否剔除母子关系']='否'
            底层数据_公告分析_代销机构_否=底层数据_公告分析_代销机构.copy()
            
    底层数据_公告分析_代销机构=pd.concat([底层数据_公告分析_代销机构_否,底层数据_公告分析_代销机构_是]) 
    底层数据_公告分析_代销机构=底层数据_公告分析_代销机构.reindex(columns=['代销机构', 'type_','BenchMin_ave','低于基准比例',  'rank',
           'rank_sum', 'BenchmarkMin', 'weight_risk', 'risk_score_ave','是否剔除母子关系'])
    底层数据_公告分析_代销机构.replace('固定收益类','固定收益类（非现金）', inplace = True)
    底层数据_公告分析_代销机构.replace('商品及金融衍生品类','商品及衍生品类', inplace = True)
    底层数据_公告分析_代销机构.set_index('代销机构',inplace=True)
    底层数据_公告分析_代销机构.loc[:,['BenchMin_ave','低于基准比例','rank']] = 底层数据_公告分析_代销机构.loc[:,['BenchMin_ave','低于基准比例','rank']].fillna('-')
    return 底层数据_公告分析_代销机构
