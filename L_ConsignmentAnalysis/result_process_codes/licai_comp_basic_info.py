# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月20日16:11:33
# @Author    : Noah Zhan
# @File      : licai_comp_basic_info
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_理财公司基本信息】依赖表
# --------------------------------

import dateutil
import pandas as pd
from data_process_codes.preprocess import preprocess

def licai_comp_basic_info(start_date,end_date,df1):
    '''
    function:生成【底层数据_理财公司基本信息】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表。
    return:
        - 底层数据_理财公司基本信息:【底层数据_理财公司基本信息】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_理财公司基本信息】依赖表, ",start_date,"到",end_date,"...")
    底层数据_理财公司基本信息 = pd.DataFrame()
    date = end_date
    i = 1
    while date >= start_date:
        print(" -Processing date ",date)
        month_begin_date = date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
        df1_temp = preprocess(df1,month_begin_date)#这组表只需要用到基础数据，即df1
    #     df1_temp = df1.copy()
    #     df2_temp = df2[(df2['代销开始日']<start_date)&(df2['代销结束日']>month_begin_date)]

        #根据变量名称和column名字基本能看明白在算什么东西
        底层数据_理财公司基本信息_temp = pd.DataFrame(columns = ['日期','理财公司','所属分类','产品数量','成立日期','理财产品存续总规模','规模排名'])
        产品数量 = df1_temp.groupby('理财公司简称')['RegistrationCode'].agg(lambda x: len(x.unique()))#x.unique是为了去重
        底层数据_理财公司基本信息_temp['产品数量'] = 产品数量
        底层数据_理财公司基本信息_temp['理财公司'] = 产品数量.index
        底层数据_理财公司基本信息_temp.index = 产品数量.index
        底层数据_理财公司基本信息_temp['日期'] = date
        底层数据_理财公司基本信息_temp['所属分类'] = df1_temp.groupby('理财公司简称')[['report_date','ParentCompType']].apply(lambda x:x.sort_values(by='report_date',ascending = False)['ParentCompType'].iloc[0])
        底层数据_理财公司基本信息_temp['成立日期'] = df1_temp.groupby('理财公司简称')[['report_date','EstablishmentDate']].apply(lambda x:x.sort_values(by='report_date',ascending = False)['EstablishmentDate'].iloc[0])#最新报告数据中的值
        底层数据_理财公司基本信息_temp['理财产品存续总规模'] = df1_temp.groupby('理财公司简称')['AssetValue'].agg('sum')#这里有一点疑问，这个数据可能有问题，因为前面剔除了子产品，只保留母产品，这个产品存续总规模是不是不对
        #底层数据_理财公司基本信息_temp['理财产品存续总规模'] = df1.groupby('理财公司简称')['AssetValue'].agg('sum')
        底层数据_理财公司基本信息_temp['规模排名'] = 底层数据_理财公司基本信息_temp['理财产品存续总规模'].rank(method='min',ascending=False)
        底层数据_理财公司基本信息 = pd.concat([底层数据_理财公司基本信息,底层数据_理财公司基本信息_temp],axis=0)#合并不同时期的数据
        date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
        i= i+1
    return 底层数据_理财公司基本信息
# 底层数据_理财公司基本信息.to_excel(path_outputdir+r'\底层数据_理财公司基本信息.xlsx')#保存数据
# 底层数据_理财公司基本信息