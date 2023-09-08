# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月25日10:24:48
# @Author    : Noah Zhan
# @File      : sectorize
# @Project   : 银行理财代销图鉴
# @Function  sectorize- 对数据进行替换处理（例如将代销机构名替换为银行类型）,以计算板块数据。
# --------------------------------
import pandas as pd

def sectorize(data,type = 'single',append=False):
    '''
    function:传入基础数据和代销数据合并后的表，根据type将对应的公司名称字段内容改为公司类型字段内容，以方便计算板块数据。
    params:
        - data:pd.DataFrame,需要更改的数据表。
        - type:str,取值有'signle'（不改变）,'daixiao_sector'（仅改变代销机构的字段）,'licai_sector'（仅改变理财公司的字段）,'sector'（代销机构和理财公司的字段均做修改）.
    return:
        - df修改后的数据表。 
    '''
    df = data.copy()
    if(type=='single'): return df
    elif(type=='licai_sector'):
        for felid in [i for i in ['理财公司简称','发行机构'] if i in df.columns]:
            df[felid] = df['ParentCompType']
    elif(type=='daixiao_sector'):
        for felid in [i for i in ['代销机构'] if i in df.columns]:
            df[felid] = df['comp_type']
    elif(type=="sector"):
        for felid in [i for i in ['代销机构'] if i in df.columns]:
            df[felid] = df['comp_type']
        for felid in [i for i in ['理财公司简称','发行机构'] if i in df.columns]:
            df[felid] = df['ParentCompType']
    if append:
        df=pd.concat([data,df])
    return df
