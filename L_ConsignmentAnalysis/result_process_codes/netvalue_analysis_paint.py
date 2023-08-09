# -*- coding: utf-8 -*-
# --------------------------------
# @Time      : 2023年7月25日
# @Author    : WSS
# @File      : netvalue_analysis_paint
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_净值走势】依赖表
# --------------------------------
#需要用到的库
import pandas as pd
import numpy as np

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
        
#删除数据过少行数
def drop_line(x,n=10):
    y=x.dropna().copy()
    if y.count()<n:
        x[:]=np.NaN
        return x
    else :
        return x
    
def netvalue_analysis_paint(start_date,df1,df2,df7,result_type1='single',result_type2='single'):
    '''
    function:生成【底层数据_净值走势】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df7:dataframe，银行理财产品产品的周度净值数据。
    return:
        - 底层数据_净值走势:【底层数据_净值走势】依赖表，用于更新理财图鉴(绘图)。
    注释：result_type1='licai_sector',result_type2='daixiao_sector'
    '''
    #将基金净值数据初始日期标准化为1
    print(" *生成【底层数据_净值走势】依赖表...")
    df7_stand=df7.dropna(how='all').copy()
    #df7_stand.drop('Unnamed: 0',axis=1,inplace=True)
    def func_stand(x): #所有净值数据均除以期初数据
        if np.isnan(x[0]):
            return x.dropna()[:]/x.dropna()[0]
        else:
            return x[:]/x[0]
    df7_stand=df7_stand.apply(lambda x :func_stand(x),axis=1)
    
    
    df1_temp=preprocess(df1,start_date,False)
    df1_merge=pd.merge(df1_temp[['理财公司简称','FinProCode','InvestmentType','AssetValue']],df7_stand,left_on=['FinProCode'],right_on=['FinProCode'])
    
    #市场均值
    list_columns=list(df7.columns)+['InvestmentType','AssetValue']
    底层数据_净值走势_市场均值=df1_merge[list_columns].groupby(['InvestmentType']).apply(np_average_juzhen).droplevel(None)
    底层数据_净值走势_市场均值=底层数据_净值走势_市场均值.reindex(index=['固定收益类', '混合类', '权益类','商品及金融衍生品类'])
    底层数据_净值走势_市场均值.drop('AssetValue',axis=1,inplace=True)
    底层数据_净值走势_市场均值=底层数据_净值走势_市场均值.apply(drop_line,axis=1)#删除数据过少行数，默认数据量少于10删除
    底层数据_净值走势_市场均值=底层数据_净值走势_市场均值.dropna(how='all')
    底层数据_净值走势_市场均值['InvestmentType']=底层数据_净值走势_市场均值.index
    底层数据_净值走势_市场均值['理财公司简称']='市场平均'
    底层数据_净值走势_市场均值=底层数据_净值走势_市场均值.set_index(['理财公司简称','InvestmentType'])
    
    df3_temp=pd.merge(df1_temp,df2,left_on='FinProCode',right_on='普益代码')
    df4_temp=exclude_mother_child_relation(df3_temp)
    df4_temp_list = df4_temp['FinProCode'].unique()
    
    df1_temp = sectorize(df1_temp,type = result_type1)
    df1_merge=pd.merge(df1_temp[['理财公司简称','FinProCode','InvestmentType','AssetValue']],df7_stand,left_on=['FinProCode'],right_on=['FinProCode'])
    
    df3_temp = sectorize(df3_temp,type = result_type2)
    df4_temp = sectorize(df4_temp,type = result_type2)
    df3_temp = df3_temp.drop_duplicates(subset=['代销机构','FinProCode'])
    df4_temp = df4_temp.drop_duplicates(subset=['代销机构','FinProCode'])
    df8_merge = pd.merge(df7_stand,df3_temp[['代销机构','FinProCode','InvestmentType','AssetValue']],on='FinProCode')


    for m in ['否','是']:
        #理财子公司
        if m=='是':
            df1_merge=df1_merge[df1_merge['FinProCode'].isin(df4_temp_list)]
            #print(222)
        底层数据_净值走势_理财公司=df1_merge.groupby(['理财公司简称','InvestmentType']).apply(np_average_juzhen).droplevel(None)
        底层数据_净值走势_理财公司=底层数据_净值走势_理财公司.drop(['FinProCode', 'AssetValue'], axis=1)
    
        #代销机构
        if m=='是':
            df8_merge=pd.merge(df7_stand,df4_temp[['代销机构','FinProCode','InvestmentType', 'AssetValue']],on='FinProCode')
            #print(111)
        底层数据_净值走势_代销机构=df8_merge.groupby(['代销机构','InvestmentType']).apply(np_average_juzhen).droplevel(None)
        底层数据_净值走势_代销机构=底层数据_净值走势_代销机构.drop(['FinProCode', 'AssetValue'], axis=1)
        
        #合并
        底层数据_净值走势=pd.concat([底层数据_净值走势_理财公司,底层数据_净值走势_代销机构]) 
        
        if m=='是':
            底层数据_净值走势.insert(0,'是否剔除母子关系','是')
            底层数据_净值走势=底层数据_净值走势.swaplevel()
            #list(底层数据_净值走势.index.names)
            底层数据_净值走势.sort_index(inplace=True)
            底层数据_净值走势=底层数据_净值走势.swaplevel()
            底层数据_净值走势_是=底层数据_净值走势.copy()
            #print(1)
        if m=='否':
            底层数据_净值走势.insert(0,'是否剔除母子关系','否')
            底层数据_净值走势=底层数据_净值走势.swaplevel()
            底层数据_净值走势.sort_index(inplace=True)
            底层数据_净值走势=底层数据_净值走势.swaplevel()
            底层数据_净值走势_否=底层数据_净值走势.copy()
            #print(2)
        
    底层数据_净值走势=pd.concat([底层数据_净值走势_否,底层数据_净值走势_是]) 
    底层数据_净值走势=底层数据_净值走势.apply(drop_line,axis=1)#删除数据过少行数，默认数据量少于10删除
    底层数据_净值走势=底层数据_净值走势.dropna(how='all')
    底层数据_净值走势=pd.concat([底层数据_净值走势,底层数据_净值走势_市场均值]) 
    return 底层数据_净值走势.T

