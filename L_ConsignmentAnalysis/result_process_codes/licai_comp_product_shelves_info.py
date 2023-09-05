# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月20日17:52:01
# @Author    : Noah Zhan
# @File      : licai_comp_product_shelves_info
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_代销产品货架_理财公司】依赖表
# --------------------------------
import dateutil
import numpy as np
import pandas as pd
from data_process_codes.preprocess import exclude_mother_child_relation, preprocess
import warnings
import empyrical as emp
import sys


sys.path.append('../data_process_codes')
from sectorize import sectorize
from data_process_codes.sort_by_frequency_return_top_n_join_with_sign import sort_by_frequency_return_top_n_join_with_sign
from data_process_codes.weighted_avg import weighted_avg_2


def licai_comp_product_shelves_info(start_date,end_date,df1,df2,df7,result_type='single'):
    '''
    function:生成【底层数据_代销产品货架_理财公司】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df7:dataframe，银行理财产品产品的周度收益率数据;
        - result_type:str,数据生成的报表类型，取值有'single'(代表单个公司数据)，'licai_sector'(理财公司分版块),'daixiao_sector'(代销公司分版块)，'sector'(理财公司和代销机构都分版块)。
    return:
        - 底层数据_代销产品货架_理财公司:【底层数据_代销产品货架_理财公司】依赖表，用于更新理财图鉴。
    '''
    warnings.filterwarnings("ignore")
    print(" *生成【底层数据_代销产品概况_理财公司】依赖表, ",start_date,"到",end_date,"...")

    def func11(x):
        #计算达标率
        try:
            return list(x.drop_duplicates(subset='RegistrationCode').dropna()['年化收益'] > (x.drop_duplicates(subset='RegistrationCode').dropna()['BenchmarkMin'] * 0.01)).count(True)/len(x.drop_duplicates(subset='RegistrationCode').dropna())
        except:
            return np.nan
    底层数据_代销产品货架_理财公司 = pd.DataFrame()
    date = end_date
    i = 1
    while date >= start_date:
        print(" -Processing date ",date)
        month_begin_date = date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
        df1_temp = preprocess(df1,month_begin_date)
        df2_temp = df2[(df2['代销开始日']<date)&(df2['代销结束日']>month_begin_date)]
        df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
        df3_temp = df3_temp.drop(df3_temp [(df3_temp['MinInvestTimeType']=='数据缺失')|(df3_temp['MinInvestTimeType']=='其他')].index)#处理数据缺失的情况
        df3_temp = df3_temp.dropna(subset=['MinInvestTimeType'])
        df7_temp = df7.loc[:,df7.columns<date]
        年化收益 = df7_temp.apply(lambda x:emp.annual_return((x/x.shift(1)-1).dropna(),annualization=52),axis=1).rename('年化收益').reset_index()
        df3_temp = pd.merge(df3_temp,年化收益,how='left',on='FinProCode')
        df3_temp.replace('其他半开型','封闭式',inplace = True)
        df3_temp['发行机构_copy'] = df3_temp['发行机构'].copy()
        df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系

        #根据result_type做数据修改
        df3_temp = sectorize(df3_temp,type=result_type)
        df4_temp = sectorize(df4_temp,type=result_type)
        
        def func1(x):#需要用到agg处的函数
            return len(x.drop_duplicates())
        
        #根据变量名称和column名字基本能看明白在算什么东西
        #先计算不剔除母子关系的情况（用数据df3_temp）
        #grouby时缺少的聚合依据变量则是将之视为整体聚合，然后赋值为全部
        temp1_1 = pd.concat([df3_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','InvestmentType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3,4]).agg('mean'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset=['RegistrationCode'])['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_1['是否剔除母子关系'] = '否'
        
        temp1_2 = pd.concat([df3_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','InvestmentType'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset=['RegistrationCode'])['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_2['是否剔除母子关系'] = '否'
        temp1_2['open_type'] = '全部'
        
        temp1_3 = pd.concat([df3_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_3['是否剔除母子关系'] = '否'
        temp1_3['InvestmentType'] = '全部'
        
        temp1_4 = pd.concat([df3_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','InvestmentType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df3_temp.groupby(['发行机构','InvestmentType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp.groupby(['发行机构','InvestmentType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp.groupby(['发行机构','InvestmentType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp.groupby(['发行机构','InvestmentType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_4['是否剔除母子关系'] = '否'
        temp1_4['MinInvestTimeType'] = '全部'
        
        temp1_5 = pd.concat([df3_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType'])['产品登记编码'].apply(func1)).groupby(level=[0,2]).agg('mean'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp.groupby(['发行机构','MinInvestTimeType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp.groupby(['发行机构','MinInvestTimeType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_5['是否剔除母子关系'] = '否'
        temp1_5['open_type'] = '全部'
        temp1_5['InvestmentType'] = '全部'
        
        temp1_6 = pd.concat([df3_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','InvestmentType'])['产品登记编码'].apply(func1)).groupby(level=[0,2]).agg('mean'),
                            df3_temp.groupby(['发行机构','InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp.groupby(['发行机构','InvestmentType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp.groupby(['发行机构','InvestmentType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp.groupby(['发行机构','InvestmentType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_6['是否剔除母子关系'] = '否'
        temp1_6['open_type'] = '全部'
        temp1_6['MinInvestTimeType'] = '全部'
        
        temp1_7 = pd.concat([df3_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2]).agg('mean'),
                            df3_temp.groupby(['发行机构','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp.groupby(['发行机构','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp.groupby(['发行机构','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp.groupby(['发行机构','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_7['是否剔除母子关系'] = '否'
        temp1_7['InvestmentType'] = '全部'
        temp1_7['MinInvestTimeType'] = '全部'
        
        temp1_8 = pd.concat([df3_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy'])['产品登记编码'].apply(func1)).groupby(level=[0]).agg('mean'),
                            df3_temp.groupby(['发行机构'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp.groupby(['发行机构'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp.groupby(['发行机构'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp.groupby(['发行机构'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_8['是否剔除母子关系'] = '否'
        temp1_8['InvestmentType'] = '全部'
        temp1_8['MinInvestTimeType'] = '全部'
        temp1_8['open_type'] = '全部'
        
        df3_temp_for9 = df3_temp.copy()
        df3_temp_for9.replace(['封闭长期','封闭中期','封闭短期'],'全部封闭型',inplace=True)
        df3_temp_for9.replace(['开放长期','开放中长期','开放中期','开放短中期','开放短期'],'全部开放型',inplace=True)
        temp1_9 = pd.concat([df3_temp_for9.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','InvestmentType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3,4]).agg('mean'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp1_9['是否剔除母子关系'] = '否'
        
        temp1_10 = pd.concat([df3_temp_for9.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','InvestmentType'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')]
                            ,axis=1).reset_index()
        temp1_10['open_type'] = '全部'
        temp1_10['是否剔除母子关系'] = '否'
        
        temp1_11 = pd.concat([df3_temp_for9.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')]
                            ,axis=1).reset_index()
        temp1_11['InvestmentType'] = '全部'
        temp1_11['是否剔除母子关系'] = '否'
        
        temp1_12 = pd.concat([df3_temp_for9.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType'])['产品登记编码'].apply(func1)).groupby(level=[0,2]).agg('mean'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df3_temp_for9.groupby(['发行机构','MinInvestTimeType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')]
                            ,axis=1).reset_index()
        temp1_12['InvestmentType'] = '全部'
        temp1_12['open_type'] = '全部'
        temp1_12['是否剔除母子关系'] = '否'
        
        #计算剔除母子关系的情况（用数据df4_temp）计算几乎同上，除了是否剔除母子关系为“是”
        temp2_1 = pd.concat([df4_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','InvestmentType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3,4]).agg('mean'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset=['RegistrationCode'])['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_1['是否剔除母子关系'] = '是'
        
        temp2_2 = pd.concat([df4_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','InvestmentType'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset=['RegistrationCode'])['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_2['是否剔除母子关系'] = '是'
        temp2_2['open_type'] = '全部'
        
        temp2_3 = pd.concat([df4_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_3['是否剔除母子关系'] = '是'
        temp2_3['InvestmentType'] = '全部'
        
        temp2_4 = pd.concat([df4_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','InvestmentType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df4_temp.groupby(['发行机构','InvestmentType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp.groupby(['发行机构','InvestmentType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp.groupby(['发行机构','InvestmentType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp.groupby(['发行机构','InvestmentType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_4['是否剔除母子关系'] = '是'
        temp2_4['MinInvestTimeType'] = '全部'
        
        temp2_5 = pd.concat([df4_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType'])['产品登记编码'].apply(func1)).groupby(level=[0,2]).agg('mean'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp.groupby(['发行机构','MinInvestTimeType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp.groupby(['发行机构','MinInvestTimeType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_5['是否剔除母子关系'] = '是'
        temp2_5['open_type'] = '全部'
        temp2_5['InvestmentType'] = '全部'
        
        temp2_6 = pd.concat([df4_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','InvestmentType'])['产品登记编码'].apply(func1)).groupby(level=[0,2]).agg('mean'),
                            df4_temp.groupby(['发行机构','InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp.groupby(['发行机构','InvestmentType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp.groupby(['发行机构','InvestmentType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp.groupby(['发行机构','InvestmentType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_6['是否剔除母子关系'] = '是'
        temp2_6['open_type'] = '全部'
        temp2_6['MinInvestTimeType'] = '全部'
        
        temp2_7 = pd.concat([df4_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2]).agg('mean'),
                            df4_temp.groupby(['发行机构','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp.groupby(['发行机构','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp.groupby(['发行机构','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp.groupby(['发行机构','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_7['是否剔除母子关系'] = '是'
        temp2_7['InvestmentType'] = '全部'
        temp2_7['MinInvestTimeType'] = '全部'
        
        temp2_8 = pd.concat([df4_temp.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy'])['产品登记编码'].apply(func1)).groupby(level=[0]).agg('mean'),
                            df4_temp.groupby(['发行机构'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp.groupby(['发行机构'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp.groupby(['发行机构'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp.groupby(['发行机构'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_8['是否剔除母子关系'] = '是'
        temp2_8['InvestmentType'] = '全部'
        temp2_8['MinInvestTimeType'] = '全部'
        temp2_8['open_type'] = '全部'
        
        df4_temp_for9 = df4_temp.copy()
        df4_temp_for9.replace(['封闭长期','封闭中期','封闭短期'],'全部封闭型',inplace=True)
        df4_temp_for9.replace(['开放长期','开放中长期','开放中期','开放短中期','开放短期'],'全部开放型',inplace=True)
        temp2_9 = pd.concat([df4_temp_for9.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','InvestmentType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3,4]).agg('mean'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')],
                            axis=1).reset_index()
        temp2_9['是否剔除母子关系'] = '是'
        
        temp2_10 = pd.concat([df4_temp_for9.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','InvestmentType'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','InvestmentType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')]
                            ,axis=1).reset_index()
        temp2_10['open_type'] = '全部'
        temp2_10['是否剔除母子关系'] = '是'
        
        temp2_11 = pd.concat([df4_temp_for9.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType','open_type'])['产品登记编码'].apply(func1)).groupby(level=[0,2,3]).agg('mean'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','open_type'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','open_type'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','open_type'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType','open_type'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')]
                            ,axis=1).reset_index()
        temp2_11['InvestmentType'] = '全部'
        temp2_11['是否剔除母子关系'] = '是'
        
        temp2_12 = pd.concat([df4_temp_for9.groupby('发行机构').apply(lambda x:x.groupby(['发行机构_copy','MinInvestTimeType'])['产品登记编码'].apply(func1)).groupby(level=[0,2]).agg('mean'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType'])[['BenchmarkMin','RegistrationCode']].apply(lambda x:x.drop_duplicates(subset='RegistrationCode')['BenchmarkMin'].mean()).rename('BenchmarkMin'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType'])['代销机构'].apply(sort_by_frequency_return_top_n_join_with_sign,ascending=False,n=2,sign=','),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType'])[['RegistrationCode','年化收益','AssetValue']].apply(weighted_avg_2).rename('加权平均年化收益'),
                            df4_temp_for9.groupby(['发行机构','MinInvestTimeType'])[['RegistrationCode','年化收益','BenchmarkMin']].apply(func11).rename('达标率')]
                            ,axis=1).reset_index()
        temp2_12['InvestmentType'] = '全部'
        temp2_12['open_type'] = '全部'
        temp2_12['是否剔除母子关系'] = '是'

        #合并数据
        底层数据_代销合作产品数矩阵_temp = pd.concat([temp1_1,temp1_2,temp1_3,temp1_4,temp1_5,temp1_6,temp1_7,temp1_8,temp1_9,temp1_10,temp1_11,temp1_12,
                                        temp2_1,temp2_2,temp2_3,temp2_4,temp2_5,temp2_6,temp2_7,temp2_8,temp2_9,temp2_10,temp2_11,temp2_12],axis=0)
        底层数据_代销合作产品数矩阵_temp['日期'] = date
        底层数据_代销产品货架_理财公司 = pd.concat([底层数据_代销产品货架_理财公司,底层数据_代销合作产品数矩阵_temp],axis=0,ignore_index=True)#合并不同时期的数据
        date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
        i= i+1

        
        #一些值的替换处理
    底层数据_代销产品货架_理财公司=底层数据_代销产品货架_理财公司[-底层数据_代销产品货架_理财公司.MinInvestTimeType.isin(['数据缺失','其他'])]
    底层数据_代销产品货架_理财公司.replace('定开型(申赎不同期)','定开型',inplace = True)
    底层数据_代销产品货架_理财公司.replace('定开型(申赎同期)','定开型',inplace = True)
    底层数据_代销产品货架_理财公司.replace('固定收益类','固收非现金', inplace = True)
    底层数据_代销产品货架_理财公司.replace('封闭短期','封闭短期（一年内）', inplace = True)
    底层数据_代销产品货架_理财公司.replace('封闭中期','封闭中期（一年到三年）', inplace = True)
    底层数据_代销产品货架_理财公司.replace('封闭长期','封闭长期（三年以上）', inplace = True)
    底层数据_代销产品货架_理财公司.replace('开放短期','开放短期（一个月内）', inplace = True)
    底层数据_代销产品货架_理财公司.replace('开放短中期','开放短中期（一月到三月）', inplace = True)
    底层数据_代销产品货架_理财公司.replace('开放中期','开放中期（三月到半年）', inplace = True)
    底层数据_代销产品货架_理财公司.replace('开放中长期','开放中长期（半年到一年）', inplace = True)
    底层数据_代销产品货架_理财公司.replace('开放长期','开放长期（一年以上）', inplace = True)
    底层数据_代销产品货架_理财公司.rename(columns={'BenchmarkMin':'业绩基准', '产品登记编码':'产品数量'}, inplace = True)
    底层数据_代销产品货架_理财公司['达标率'] = 底层数据_代销产品货架_理财公司['达标率'].fillna('-')
    底层数据_代销产品货架_理财公司['业绩基准'] = 底层数据_代销产品货架_理财公司['业绩基准'].fillna('-')
    # 底层数据_代销产品货架_理财公司.drop_duplicates().to_excel(path_outputdir+r'\底层数据_代销产品货架_理财公司.xlsx')
    # 底层数据_代销产品货架_理财公司
    warnings.filterwarnings("default")
    return 底层数据_代销产品货架_理财公司