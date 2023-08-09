# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月21日10:10:04
# @Author    : Noah Zhan
# @File      : daixiao_comp_product_recommendation
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_产品甄选_代销机构】依赖表
# --------------------------------


import dateutil
import empyrical as emp
import numpy as np
import pandas as pd
import sys

from data_process_codes.merge2cols_ues_col2_if_col1_empty import \
    merge2cols_ues_col2_if_col1_empty
from data_process_codes.preprocess import (exclude_mother_child_relation,
                                           preprocess)
from data_process_codes.WeeklyYield_to_rangereturn import WeeklyYield_to_rangereturn
from sectorize import sectorize
def daixiao_comp_product_recommendation(start_date,end_date,df1,df2,df7,df9,result_type='single'):
    '''
    function:生成【底层数据_产品甄选_代销机构】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df7:dataframe，银行产品产品的周度收益率数据;
        - df9:dataframe，银行理财现金管理类产品产品的日度收益率数据;
        - result_type:str,数据生成的报表类型，取值有'single'(代表单个公司数据)，'licai_sector'(理财公司分版块),'daixiao_sector'(代销公司分版块)，'sector'(理财公司和代销机构都分版块)。
    return:
        - 底层数据_产品甄选_代销机构_近一年:【底层数据_产品甄选_理财公司】依赖表之一，用于更新理财图鉴。
        - 底层数据_产品甄选_代销机构_近半年:【底层数据_产品甄选_理财公司】依赖表之一，用于更新理财图鉴。
        - 底层数据_产品甄选_代销机构_近三月:【底层数据_产品甄选_理财公司】依赖表之一，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_产品甄选_代销机构】依赖表, ",start_date,"到",end_date,"...")
    底层数据_产品甄选_代销机构_近一年 = pd.DataFrame()
    底层数据_产品甄选_代销机构_近半年 = pd.DataFrame()
    底层数据_产品甄选_代销机构_近三月 = pd.DataFrame()
    #将df9中有的数据在df7中去重
    df7 = df7[~df7.index.isin(list(set(df9['FinProCode'])))]
    现金管理类_七日年化 = df9.copy()
    产品净值_字段计算 = pd.DataFrame(index = list(df7.index)+list(现金管理类_七日年化['FinProCode'].unique()))
    产品净值_字段计算['近三月收益'] = pd.concat([df7.apply(lambda x :x[-1]/x[-13]-1,axis=1),
                                    现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn,13)],axis=0)
    产品净值_字段计算['近半年收益'] =pd.concat([df7.apply(lambda x :x[-1]/x[-27]-1,axis=1)
                                ,现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn,26)],axis=0)
    产品净值_字段计算['近一年收益'] =pd.concat([df7.apply(lambda x :x[-1]/x[-53]-1,axis=1)
                                ,现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn,52)],axis=0)
    产品净值_字段计算['最大回撤'] = df7.apply(lambda x : emp.max_drawdown((x[-53:]/x.shift(1)[-53:]-1).dropna()),axis=1)
    产品净值_字段计算['夏普比率'] = df7.apply(lambda x : emp.sharpe_ratio((x[-53:]/x.shift(1)[-53:]-1).dropna(), risk_free=0, annualization=52),axis=1)

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
        
    def func6(x,timerange):
        temp = x.drop_duplicates("RegistrationCode").sort_values(by=timerange+'收益',ascending=False)[:10]
        temp['司内排名'] = list(range(1,len(temp)+1))
        return temp
    def func9(x):
        if(x[0]=='每日开放型'):
            return 1
        else: return x[1]
    for timerange in ['近一年','近半年','近三月']:
        底层数据_产品甄选_代销机构 = pd.DataFrame()
        date = end_date
        i = 1
        while date >= start_date:
            print(" -Processing date ",date)
            #按照时间结点对数据进行处理
            month_begin_date = date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
            df1_temp = preprocess(df1,month_begin_date)
            df1_temp['manage_fee'] = df1_temp[['manage_fee_y','manage_fee_x']].apply(merge2cols_ues_col2_if_col1_empty,axis=1)#新生成一列管理费，综合使用之前的两列数据
            df1_temp['二级分类'] = df1_temp[['固收增强分类_补充子产品','product_type_son']].apply(merge2cols_ues_col2_if_col1_empty,axis=1)#新生成一列二级分类，综合使用之前的两列数据
            df2_temp = df2[(df2['代销开始日']<date)&(df2['代销结束日']>month_begin_date)]
            df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
            df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系
            
            #根据result_type做数据修改
            df3_temp = sectorize(df3_temp,type=result_type)
            df4_temp = sectorize(df4_temp,type=result_type)
            
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
            #计算收益排名
            df5_temp = pd.merge(df5_temp,
                                df5_temp.dropna(subset=timerange+'收益')
                                .drop_duplicates('产品登记编码')
                                .groupby(['InvestmentType','open_type','持有期限'])
                                .apply(lambda x:pd.concat([x['产品登记编码'],(x[timerange+'收益']
                                                                        .rank(method='min',ascending=False))
                                                                        .astype(str)+"/"+str(len(x))],
                                                            axis=1,
                                                            ignore_index=True)
                                                    .rename(columns={0:'RegistrationCode',1:'收益排名'})),
                                on='RegistrationCode')
            df6_temp = pd.merge(df6_temp,
                                df6_temp.dropna(subset=timerange+'收益')
                                .drop_duplicates('产品登记编码')
                                .groupby(['InvestmentType','open_type','持有期限'])
                                .apply(lambda x:pd.concat([x['产品登记编码'],(x[timerange+'收益']
                                                                        .rank(method='min',ascending=False))
                                                                        .astype(str)+"/"+str(len(x))],
                                                            axis=1,
                                                            ignore_index=True)
                                                    .rename(columns={0:'RegistrationCode',1:'收益排名'})),
                                on='RegistrationCode')
            #先计算不剔除母子关系的情况（df5_temp）
            field_care = ['RegistrationCode','FinProCode','product_name','理财公司简称',
                          '代销机构','InvestmentType','open_type','持有期限',
                          '二级分类','AssetValue','BenchmarkMin','RiskLevel',
                          'manage_fee','夏普比率','最大回撤',timerange+'收益','收益排名']
            底层数据_产品甄选_代销机构_temp1 = df5_temp[field_care].groupby(['代销机构','InvestmentType','open_type','持有期限'])
            底层数据_产品甄选_代销机构_temp11 = df5_temp[field_care].groupby(['代销机构','InvestmentType','持有期限'])
            底层数据_产品甄选_代销机构_temp12 = df5_temp[field_care].groupby(['代销机构','InvestmentType','open_type'])
            底层数据_产品甄选_代销机构_temp13 = df5_temp[field_care].groupby(['代销机构','InvestmentType'])
            #甄选每家的前10名
            底层数据_产品甄选_代销机构_temp1 = 底层数据_产品甄选_代销机构_temp1.apply(func6, timerange)
            底层数据_产品甄选_代销机构_temp11 = 底层数据_产品甄选_代销机构_temp11.apply(func6, timerange)
            底层数据_产品甄选_代销机构_temp11['open_type'] = '全部'
            底层数据_产品甄选_代销机构_temp12 = 底层数据_产品甄选_代销机构_temp12.apply(func6, timerange)
            底层数据_产品甄选_代销机构_temp12['持有期限'] = '全部'
            底层数据_产品甄选_代销机构_temp13 = 底层数据_产品甄选_代销机构_temp13.apply(func6, timerange)
            底层数据_产品甄选_代销机构_temp13['open_type'] = '全部'
            底层数据_产品甄选_代销机构_temp13['持有期限'] = '全部'
            #被代销数量
            底层数据_产品甄选_代销机构_temp1 = pd.merge(底层数据_产品甄选_代销机构_temp1,
                                            df5_temp.groupby('FinProCode')[['产品登记编码','代销机构']]
                                            .apply(lambda x: len(x.drop_duplicates()))
                                            .rename('被代销数量')
                                            .reset_index(),
                                            on='FinProCode')
            底层数据_产品甄选_代销机构_temp11 = pd.merge(底层数据_产品甄选_代销机构_temp11,
                                             df5_temp.groupby('FinProCode')[['产品登记编码','代销机构']]
                                             .apply(lambda x: len(x.drop_duplicates()))
                                             .rename('被代销数量')
                                             .reset_index(),
                                             on='FinProCode')
            底层数据_产品甄选_代销机构_temp12 = pd.merge(底层数据_产品甄选_代销机构_temp12,
                                             df5_temp.groupby('FinProCode')[['产品登记编码','代销机构']]
                                             .apply(lambda x: len(x.drop_duplicates()))
                                             .rename('被代销数量')
                                             .reset_index(),
                                             on='FinProCode')
            底层数据_产品甄选_代销机构_temp13 = pd.merge(底层数据_产品甄选_代销机构_temp13,
                                             df5_temp.groupby('FinProCode')[['产品登记编码','代销机构']]
                                             .apply(lambda x: len(x.drop_duplicates()))
                                             .rename('被代销数量')
                                             .reset_index(),
                                             on='FinProCode')
            底层数据_产品甄选_代销机构_temp1 = pd.concat([底层数据_产品甄选_代销机构_temp1,底层数据_产品甄选_代销机构_temp11,底层数据_产品甄选_代销机构_temp12,底层数据_产品甄选_代销机构_temp13],axis=0)
            底层数据_产品甄选_代销机构_temp1['日期'] = date
            底层数据_产品甄选_代销机构_temp1['是否剔除母子关系'] = '否'

            #计算剔除母子关系的情况（df6_temp）
            field_care = ['RegistrationCode','FinProCode','product_name','理财公司简称',
                          '代销机构','InvestmentType','open_type','持有期限',
                          '二级分类','AssetValue','BenchmarkMin','RiskLevel',
                          'manage_fee','夏普比率','最大回撤',timerange+'收益','收益排名']
            底层数据_产品甄选_代销机构_temp2 = df6_temp[field_care].groupby(['代销机构','InvestmentType','open_type','持有期限'])
            底层数据_产品甄选_代销机构_temp21 = df6_temp[field_care].groupby(['代销机构','InvestmentType','持有期限'])
            底层数据_产品甄选_代销机构_temp22 = df6_temp[field_care].groupby(['代销机构','InvestmentType','open_type'])
            底层数据_产品甄选_代销机构_temp23 = df6_temp[field_care].groupby(['代销机构','InvestmentType'])
            #甄选每家的前五名
            底层数据_产品甄选_代销机构_temp2 = 底层数据_产品甄选_代销机构_temp2.apply(func6, timerange)
            底层数据_产品甄选_代销机构_temp21 = 底层数据_产品甄选_代销机构_temp21.apply(func6, timerange)
            底层数据_产品甄选_代销机构_temp21['open_type'] = '全部'
            底层数据_产品甄选_代销机构_temp22 = 底层数据_产品甄选_代销机构_temp22.apply(func6, timerange)
            底层数据_产品甄选_代销机构_temp22['持有期限'] = '全部'
            底层数据_产品甄选_代销机构_temp23 = 底层数据_产品甄选_代销机构_temp23.apply(func6, timerange)
            底层数据_产品甄选_代销机构_temp23['open_type']= '全部'
            底层数据_产品甄选_代销机构_temp23['持有期限'] = '全部'

            #被代销数量
            底层数据_产品甄选_代销机构_temp2 = pd.merge(底层数据_产品甄选_代销机构_temp2,
                                            df6_temp.groupby('FinProCode')[['产品登记编码','代销机构']]
                                            .apply(lambda x: len(x.drop_duplicates()))
                                            .rename('被代销数量')
                                            .reset_index(),
                                            on='FinProCode')
            底层数据_产品甄选_代销机构_temp21 = pd.merge(底层数据_产品甄选_代销机构_temp21,
                                             df6_temp.groupby('FinProCode')[['产品登记编码','代销机构']]
                                             .apply(lambda x: len(x.drop_duplicates()))
                                             .rename('被代销数量')
                                             .reset_index(),
                                             on='FinProCode')
            底层数据_产品甄选_代销机构_temp22 = pd.merge(底层数据_产品甄选_代销机构_temp22,
                                             df6_temp.groupby('FinProCode')[['产品登记编码','代销机构']]
                                             .apply(lambda x: len(x.drop_duplicates()))
                                             .rename('被代销数量')
                                             .reset_index(),
                                             on='FinProCode')
            底层数据_产品甄选_代销机构_temp23 = pd.merge(底层数据_产品甄选_代销机构_temp23,
                                             df6_temp.groupby('FinProCode')[['产品登记编码','代销机构']]
                                             .apply(lambda x: len(x.drop_duplicates()))
                                             .rename('被代销数量')
                                             .reset_index(),
                                             on='FinProCode')
            底层数据_产品甄选_代销机构_temp2 = pd.concat([底层数据_产品甄选_代销机构_temp2,
                                              底层数据_产品甄选_代销机构_temp21,
                                              底层数据_产品甄选_代销机构_temp22,
                                              底层数据_产品甄选_代销机构_temp23],
                                              axis=0)
            底层数据_产品甄选_代销机构_temp2['日期'] = date
            底层数据_产品甄选_代销机构_temp2['是否剔除母子关系'] = '是'
            


            #合并数据
            底层数据_产品甄选_代销机构 = pd.concat([底层数据_产品甄选_代销机构,底层数据_产品甄选_代销机构_temp1,底层数据_产品甄选_代销机构_temp2],axis=0,ignore_index=True)

            date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
            i= i+1
        底层数据_产品甄选_代销机构 = 底层数据_产品甄选_代销机构.fillna("-")
        # 底层数据_产品甄选_代销机构.to_excel(path_outputdir+r'\底层数据_产品甄选_代销机构_'+timerange+'.xlsx')
        if(timerange=='近一年'):
            底层数据_产品甄选_代销机构_近一年 = 底层数据_产品甄选_代销机构.copy()
        elif(timerange=='近半年'):
            底层数据_产品甄选_代销机构_近半年 = 底层数据_产品甄选_代销机构.copy()
        else:
            底层数据_产品甄选_代销机构_近三月 = 底层数据_产品甄选_代销机构.copy()
    return 底层数据_产品甄选_代销机构_近一年,底层数据_产品甄选_代销机构_近半年,底层数据_产品甄选_代销机构_近三月
