# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月21日13:20:25
# @Author    : Noah Zhan
# @File      : weighted_avg
# @Project   : 银行理财代销图鉴
# @Function  ：weighted_avg- 传入序列值和序列值的权重，先去缺失行，再求加权均值。
#              weighted_avg2- 
# --------------------------------

import numpy as np
import pandas as pd


def weighted_avg(x,weight):
    '''
    function:传入序列值和序列值的权重，先去缺失行，再求加权均值。
    params:
        - x:pd.Series/pd.DataFrame,需要求均值的序列；
        - weight:pd.Series/pd.DataFrame,权重序列.
    return:
        - np.nan/sum(x.iloc[ind])*(7/365)*0.01
    '''
    temp = pd.concat([x,weight],axis=1).dropna()
    if sum(temp.iloc[:,1])<=0:
        return
    else:
        return np.average(temp.iloc[:,0],weights=temp.iloc[:,1])
    
def weighted_avg_2(x):
    '''
    function:传入带有RegistrationCode、年化收益、AssetValue三个字段的dataframe，先去重再去缺失行，再求加权均值。
    params:
        - x:pd.Series/pd.DataFrame,带有RegistrationCode、年化收益、AssetValue三个字段的dataframe；
    return:-
    '''
    try:
        return np.average(x.drop_duplicates(subset='RegistrationCode').dropna()['年化收益'].values,weights=x.drop_duplicates(subset='RegistrationCode').dropna()['AssetValue'].values)
    except:
        return np.nan