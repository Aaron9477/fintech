# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月20日17:25:29
# @Author    : Noah Zhan
# @File      : hezuoproduct_num
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_合作产品】依赖表
# --------------------------------
import dateutil
import pandas as pd
from data_process_codes.preprocess import exclude_mother_child_relation, preprocess
from sectorize import sectorize


def hezuoproduct_num(start_date,end_date,df1,df2,if_sector = False):
    '''
    function:生成【底层数据_合作产品】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - if_sector:是否计算板块数据。
    return:
        - 理财公司_top10:生成【底层数据_合作产品】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_合作产品】依赖表, ",start_date,"到",end_date,"...")
    def df_val_to_rank(df,axis):
        result = df.copy()
        if(axis==0):#按行排序
            for i in range(0,len(result.index)):
                result.iloc[i,:] = list(df.iloc[i,:].rank(method='first',ascending=False))
        elif(axis==1):#按列排序
            for i in range(0,len(result.columns)):
                result.iloc[:,i] = list(df.iloc[:,i].rank(method='first',ascending=False))
        return result

    date = end_date
    i = 1
    底层数据_合作产品 = pd.DataFrame()
    while date >= start_date:
        print(" -Processing date ",date)
        month_begin_date = date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
        df1_temp = preprocess(df1,month_begin_date)
        df2_temp = df2[(df2['代销开始日']<date)&(df2['代销结束日']>month_begin_date)]
        df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
        df3_temp['代销机构_copy'] = df3_temp['代销机构'].copy()
        df3_temp['发行机构_copy'] = df3_temp['发行机构'].copy()
        df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系
        if if_sector:
            df3_temp_licai_sector = sectorize(df3_temp,type='licai_sector')
            df4_temp_licai_sector = sectorize(df4_temp,type='licai_sector')
            df3_temp_daixiao_sector = sectorize(df3_temp,type='daixiao_sector')
            df4_temp_daixiao_sector = sectorize(df4_temp,type='daixiao_sector')
        else:
            df3_temp_licai_sector = df3_temp
            df4_temp_licai_sector = df4_temp
            df3_temp_daixiao_sector = df3_temp
            df4_temp_daixiao_sector = df4_temp

        def func1(x):#需要用到agg处的函数
            return len(x.drop_duplicates())
        
        #根据变量名称和column名字基本能看明白在算什么东西
        #先计算不剔除母子关系的情况（用数据df3_tempxxx）
        合作产品数矩阵_理财公司 = df3_temp_licai_sector.groupby('发行机构').apply(lambda x : (x.groupby(['发行机构_copy','代销机构'])['产品登记编码'].agg(func1).unstack()).mean()).unstack()
        合作产品数矩阵_代销机构 = df3_temp_daixiao_sector.groupby('代销机构').apply(lambda x : (x.groupby(['代销机构_copy','发行机构'])['产品登记编码'].agg(func1).unstack()).mean()).unstack()

        合作产品数矩阵 = pd.concat([合作产品数矩阵_代销机构,合作产品数矩阵_理财公司],axis=0)
        合作产品数矩阵_排名 = df_val_to_rank(合作产品数矩阵,axis=0)
        底层数据_合作产品_temp1 = pd.DataFrame(index=合作产品数矩阵.index,columns=range(0,20))
        底层数据_合作产品_temp1.columns=['top1_company','top1_num','top2_company','top2_num','top3_company','top3_num','top4_company','top4_num','top5_company','top5_num',
                    'top6_company','top6_num','top7_company','top7_num','top8_company','top8_num','top9_company','top9_num','top10_company','top10_num']
        for ind in 底层数据_合作产品_temp1.index:
            companies = list(合作产品数矩阵_排名.loc[ind].sort_values(ascending=True).index[0:10])
            nums = list(合作产品数矩阵.loc[ind,companies])
            for i in range(1,min(11,len(companies)+1)):
                底层数据_合作产品_temp1.loc[ind,'top'+str(i)+'_company'] = companies[i-1]
                底层数据_合作产品_temp1.loc[ind,'top'+str(i)+'_num'] = nums[i-1]
        底层数据_合作产品_temp1['是否剔除母子关系'] = '否'
        底层数据_合作产品_temp1['日期'] = date

        #计算剔除母子关系的情况（用数据df_tempxxx）
        合作产品数矩阵_理财公司 = df4_temp_licai_sector.groupby('发行机构').apply(lambda x : (x.groupby(['发行机构_copy','代销机构'])['产品登记编码'].agg(func1).unstack()).mean()).unstack()
        合作产品数矩阵_代销机构 = df4_temp_daixiao_sector.groupby('代销机构').apply(lambda x : (x.groupby(['代销机构_copy','发行机构'])['产品登记编码'].agg(func1).unstack()).mean()).unstack()

        合作产品数矩阵 = pd.concat([合作产品数矩阵_代销机构,合作产品数矩阵_理财公司],axis=0)
        合作产品数矩阵_排名 = df_val_to_rank(合作产品数矩阵,axis=0)
        底层数据_合作产品_temp2 = pd.DataFrame(index=合作产品数矩阵.index,columns=range(0,20))
        底层数据_合作产品_temp2.columns=['top1_company','top1_num','top2_company','top2_num','top3_company','top3_num','top4_company','top4_num','top5_company','top5_num',
                    'top6_company','top6_num','top7_company','top7_num','top8_company','top8_num','top9_company','top9_num','top10_company','top10_num']
        for ind in 底层数据_合作产品_temp2.index:
            companies = list(合作产品数矩阵_排名.loc[ind].sort_values(ascending=True).index[0:10])
            nums = list(合作产品数矩阵.loc[ind,companies])
            for i in range(1,min(11,len(companies)+1)):
                底层数据_合作产品_temp2.loc[ind,'top'+str(i)+'_company'] = companies[i-1]
                底层数据_合作产品_temp2.loc[ind,'top'+str(i)+'_num'] = nums[i-1]
        底层数据_合作产品_temp2['是否剔除母子关系'] = '是'
        底层数据_合作产品_temp2['日期'] = date
        底层数据_合作产品 = pd.concat([底层数据_合作产品,底层数据_合作产品_temp1,底层数据_合作产品_temp2],axis=0)
        date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
        i= i+1
    return 底层数据_合作产品
