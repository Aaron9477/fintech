# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月20日16:11:33
# @Author    : Noah Zhan
# @File      : daixiao_comp_basic_info
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_理财公司基本信息】依赖表
# --------------------------------

import dateutil
import pandas as pd
from data_process_codes.preprocess import preprocess

def daixiao_comp_basic_info(start_date,end_date,df2,df8):
    '''
    function:生成【底层数据_理财公司基本信息】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df2:dataframe，银行理财产品的代销表;
        - df8:dataframe，代销机构数据。
    return:
        - 底层数据_理财公司基本信息:【底层数据_理财公司基本信息】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_理财公司基本信息】依赖表, ",start_date,"到",end_date,"...")
    底层数据_代销机构基本信息 = pd.DataFrame()
    date = end_date
    i = 1
    while date >= start_date:
        print(" -Processing date ",date)
        month_begin_date = date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
        df2_temp = df2[(df2['代销开始日']<date)&(df2['代销结束日']>month_begin_date)]
        df8_temp = df8.copy()
        df8_temp['comp_name'] = df8_temp['comp_name'].str.replace('股份有限公司','',regex=True)
        df8_temp['comp_name'] = df8_temp['comp_name'].str.replace('有限公司','',regex=True)
        df8_temp['comp_name'] = df8_temp['comp_name'].str.replace('有限责任公司','',regex=True)
        df8_temp['comp_name'] = df8_temp['comp_name'].apply(lambda x:x.split("(")[0])
        
        
        #     底层数据_代销机构基本信息_temp = pd.DataFrame(columns = ['日期','机构名称','机构简称','代销产品数量','所属分类','成立日期','资产总规模','所在地区'])
        代销产品数量 = df2_temp.groupby('代销机构')['产品登记编码'].agg(lambda x: len(x.unique())).rename('代销产品数量').sort_values().reset_index()#x.unique是为了去重
        底层数据_代销机构基本信息_temp = pd.merge(df8_temp,代销产品数量,how='right',left_on='comp_simple_name',right_on='代销机构')
        df8_temp.index = df8_temp['comp_name']
        底层数据_代销机构基本信息_temp.index = 底层数据_代销机构基本信息_temp['代销机构']
        底层数据_代销机构基本信息_temp[['comp_name','comp_simple_name','comp_type','found_date','regcapital','province']] = df8_temp[['comp_name','comp_simple_name','comp_type','found_date','regcapital','province']]
        底层数据_代销机构基本信息_temp['代销产品数量排名'] = 底层数据_代销机构基本信息_temp['代销产品数量'].rank(method='min',ascending=False).round(0).apply(lambda x: str(int(x))+"/"+str(len(底层数据_代销机构基本信息_temp)))
        底层数据_代销机构基本信息_temp['规模排名'] = 底层数据_代销机构基本信息_temp['regcapital'].rank(method='min',ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销机构基本信息_temp)))
        底层数据_代销机构基本信息_temp['日期'] = date
        
        底层数据_代销机构基本信息 = pd.concat([底层数据_代销机构基本信息,底层数据_代销机构基本信息_temp],axis=0)#合并不同时期的数据
        date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
        i= i+1
    return 底层数据_代销机构基本信息
    
# 底层数据_代销机构基本信息.loc[:,'comp_type':].to_excel(path_outputdir+r'\底层数据_代销机构基本信息.xlsx')
# 底层数据_代销机构基本信息