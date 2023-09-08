import dateutil
import empyrical as emp
import numpy as np
import pandas as pd

from sympy import comp

from data_process_codes.merge2cols_ues_col2_if_col1_empty import \
    merge2cols_ues_col2_if_col1_empty
from data_process_codes.preprocess import (exclude_mother_child_relation,
                                           preprocess)
from data_process_codes.WeeklyYield_to_rangereturn import WeeklyYield_to_rangereturn
from sectorize import sectorize


def caculate_return_by_sector(end_date,df1,df2,df7,df9):
    df7 = df7[~df7.index.isin(list(set(df9['FinProCode'])))]
    def func5(x):#将字段【MinInvestDay】转为相应的期限分类
        if(x['open_type']=='封闭型'):
            if(x['MinInvestDay']<=365):return "一年内"
            elif(x['MinInvestDay']>365 and x['MinInvestDay']<=365*3):return "一年到三年"
            elif(x['MinInvestDay']>365*3):return "三年以上"
        else:
            if(x['MinInvestDay']<=30):return "一个月内"
            elif(x['MinInvestDay']>30 and x['MinInvestDay']<=30*3):return "一月到三月"
            elif(x['MinInvestDay']>30*3 and x['MinInvestDay']<=30*6):return "三月到半年"
            elif(x['MinInvestDay']>30*6 and x['MinInvestDay']<=30*12):return "半年到一年"
            elif(x['MinInvestDay']>30*12):return "一年以上"
    def func9(x):
        if(x[0]=='每日开放型'):
            return 1
        else: return x[1]
    def func11(x):
    #计算达标率
        try:
            unique_data = x.drop_duplicates(subset='RegistrationCode').dropna()
            condition_met = unique_data['年化收益'] > (unique_data['BenchmarkMin'] * 0.01)
            ratio = condition_met.sum() / len(unique_data)
            return ratio
        except:
            return np.nan
    df1_temp = preprocess(df1,end_date)
    df1_temp['manage_fee'] = df1_temp[['manage_fee_y','manage_fee_x']].apply(merge2cols_ues_col2_if_col1_empty,axis=1)#新生成一列管理费，综合使用之前的两列数据
    df1_temp['二级分类'] = df1_temp[['固收增强分类_补充子产品','product_type_son']].apply(merge2cols_ues_col2_if_col1_empty,axis=1)#新生成一列二级分类，综合使用之前的两列数据
    df2_temp = df2[(df2['代销开始日']<end_date)&(df2['代销结束日']>end_date)]
    df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
    df3_temp=df3_temp[df3_temp['MinInvestTimeType']!='数据缺失']
    df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系


    现金管理类_七日年化 = df9.copy()
    现金管理类_七日年化 = 现金管理类_七日年化[现金管理类_七日年化['EndDate']<=end_date]
    产品净值_字段计算 = pd.DataFrame(index = list(df7.index)+list(现金管理类_七日年化['FinProCode'].unique()))
    产品净值_字段计算['近四周收益'] = pd.concat([df7.apply(lambda x :x[-1]/x[-5]-1,axis=1),
                                    现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn,4)],axis=0)
    产品净值_字段计算['近半年收益'] =pd.concat([df7.apply(lambda x :x[-1]/x[-27]-1,axis=1)
                                ,现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn,26)],axis=0)
    df3_temp = sectorize(df3_temp,type='sector')
    df4_temp = sectorize(df4_temp,type='sector')
    
    df5_temp = pd.merge(df3_temp,产品净值_字段计算,how='left',left_on = 'FinProCode',right_index=True)#合并基础数据、代销数据和净值数据计算的三个字段（不剔除母子关系）
    df6_temp = pd.merge(df4_temp,产品净值_字段计算,how='left',left_on = 'FinProCode',right_index=True)#合并基础数据、代销数据和净值数据计算的三个字段（剔除母子关系）
    #将“open_type”=“每日开放型”的，“MinInvestDay”补充为1，然后将“MinInvestDay”为-1或者为空的过滤掉
    df5_temp['MinInvestDay'] = df5_temp[['open_type','MinInvestDay']].apply(func9,axis=1).replace('-1',np.nan)
    df6_temp['MinInvestDay'] = df6_temp[['open_type','MinInvestDay']].apply(func9,axis=1).replace('-1',np.nan)
    df5_temp.dropna(subset = 'MinInvestDay',inplace = True)
    df6_temp.dropna(subset = 'MinInvestDay',inplace = True)
    #将open_type字段中【封闭式】和【其他半开型】均改为【封闭型】，将【定开型(申赎同期)】和【定开型(申赎不同期)】均改成【定开型】。
    df5_temp['open_type'] = df5_temp['open_type'].replace({"封闭式":"封闭型","其他半开型":"封闭型","定开型(申赎同期)":"定开型","定开型(申赎不同期)":"定开型"})
    df6_temp['open_type'] = df6_temp['open_type'].replace({"封闭式":"封闭型","其他半开型":"封闭型","定开型(申赎同期)":"定开型","定开型(申赎不同期)":"定开型"})
    #MinInvestDay生成持有期限
    df5_temp['持有期限'] = df5_temp.apply(func5,axis=1)
    df6_temp['持有期限'] = df6_temp.apply(func5,axis=1)

    df5_temp=df5_temp.dropna(subset=['近四周收益','近半年收益','AssetValue'])
    df6_temp=df6_temp.dropna(subset=['近四周收益','近半年收益','AssetValue'])
    
    df5_temp['Bench_4week']=(1+df5_temp['BenchmarkMin']*0.01)**(1/12)-1
    df5_temp['Bench_half_year']=(1+df5_temp['BenchmarkMin']*0.01)**(1/2)-1
    df5_temp['outperform_4week']=df5_temp['近四周收益']>df5_temp['Bench_4week']
    df5_temp['outperform_half_year']=df5_temp['近半年收益']>df5_temp['Bench_half_year']
    
    
    df6_temp['Bench_4week']=(1+df5_temp['BenchmarkMin']*0.01)**(1/12)-1
    df6_temp['Bench_half_year']=(1+df5_temp['BenchmarkMin']*0.01)**(1/2)-1
    df6_temp['outperform_4week']=df6_temp['近四周收益']>df6_temp['Bench_4week']
    df6_temp['outperform_half_year']=df6_temp['近半年收益']>df6_temp['Bench_half_year']

    #分组计算并合并

    outperformance_pct_n=df5_temp.groupby(['理财公司简称','InvestmentType','MinInvestTimeType'])[['outperform_4week','outperform_half_year']].mean()
                                 
    outperformance_pct_y=df6_temp.groupby(['理财公司简称','InvestmentType','MinInvestTimeType'])[['outperform_4week','outperform_half_year']].mean()


    sector_return_n=df5_temp.groupby(['理财公司简称','InvestmentType','MinInvestTimeType']).apply(lambda x:np.average(x[['近四周收益','近半年收益']],weights=x['AssetValue'],axis=0))
    sector_return_n=pd.concat([sector_return_n.str[0],sector_return_n.str[1]],axis=1,keys=['近四周收益','近半年收益'])
    sector_return_n=pd.concat([sector_return_n,outperformance_pct_n],axis=1)
    

    sector_return_y=df6_temp.groupby(['理财公司简称','InvestmentType','MinInvestTimeType']).apply(lambda x:np.average(x[['近四周收益','近半年收益']],weights=x['AssetValue'],axis=0))
    sector_return_y=pd.concat([sector_return_y.str[0],sector_return_y.str[1]],axis=1,keys=['近四周收益','近半年收益'])
    sector_return_y=pd.concat([sector_return_y,outperformance_pct_y],axis=1)

    

    sector_return=pd.concat([sector_return_n,sector_return_y],keys=['否','是'],names=['是否剔除'])
    sector_return=sector_return.unstack()
    idx=pd.IndexSlice
    sector_return=sector_return.loc[idx['是',:],:]
    sector_return=sector_return.droplevel('是否剔除')
    sector_return.rename(columns={'定开型(申赎不同期)':'定开型'},inplace = True)
    sector_return.rename(columns={'定开型(申赎同期)':'定开型'},inplace = True)
    sector_return.rename(columns={'固定收益类':'固收非现金'}, inplace = True)
    sector_return.rename(columns={'封闭短期':'封闭短期（一年内）'}, inplace = True)
    sector_return.rename(columns={'封闭中期':'封闭中期（一年到三年）'}, inplace = True)
    sector_return.rename(columns={'封闭长期':'封闭长期（三年以上）'}, inplace = True)
    sector_return.rename(columns={'开放短期':'开放短期（一个月内）'}, inplace = True)
    sector_return.rename(columns={'开放短中期':'开放短中期（一月到三月）'}, inplace = True)
    sector_return.rename(columns={'开放中期':'开放中期（三月到半年）'}, inplace = True)
    sector_return.rename(columns={'开放中长期':'开放中长期（半年到一年）'}, inplace = True)
    sector_return.rename(columns={'开放长期':'开放长期（一年以上）'}, inplace = True)

    ordered_columns=['封闭短期（一年内）','封闭中期（一年到三年）','封闭长期（三年以上）','开放短期（一个月内）','开放短中期（一月到三月）','开放中期（三月到半年）','开放中长期（半年到一年）','开放长期（一年以上）']


    #把合并数据拆开
    sector_return_4w=sector_return.loc[:,sector_return.columns.isin(['近四周收益'],level=0)]
    sector_return_4w=sector_return_4w.droplevel(0,axis=1)
    sector_return_4w=sector_return_4w.loc[:,ordered_columns]
    
    outperformance_4w=sector_return.loc[:,sector_return.columns.isin(['outperform_4week'],level=0)]
    outperformance_4w=outperformance_4w.droplevel(0,axis=1)
    outperformance_4w=outperformance_4w.loc[:,ordered_columns]


    sector_return_half_year=sector_return.loc[:,sector_return.columns.isin(['近半年收益'],level=0)]
    sector_return_half_year=sector_return_half_year.droplevel(0,axis=1)
    sector_return_half_year=sector_return_half_year.loc[:,ordered_columns]


    outperformance_half_year=sector_return.loc[:,sector_return.columns.isin(['outperform_half_year'],level=0)]
    outperformance_half_year=outperformance_half_year.droplevel(0,axis=1)
    outperformance_half_year=outperformance_half_year.loc[:,ordered_columns]

    with pd.ExcelWriter(r"类型表现.xlsx") as writer:
        sector_return_4w.to_excel(writer,'4周收益')    
        sector_return_half_year.to_excel(writer,'半年收益')  
        outperformance_4w.to_excel(writer,'4周达标率')
        outperformance_half_year.to_excel(writer,'半年达标率')

    return 