# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月21日13:20:25
# @Author    : Noah Zhan
# @File      : weighted_avg
# @Project   : 银行理财代销图鉴
# @Function  ：weighted_avg- 传入序列值和序列值的权重，先去缺失行，再求加权均值。
#              weighted_avg2- 
# --------------------------------

from math import ceil, floor
import re
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
        x1=x.drop_duplicates(subset='RegistrationCode').dropna()
        return np.average(x1['年化收益'].values,weights=x1['AssetValue'].values)
    except:
        return np.nan
    
def hash_string(s: str,p:np.float64,round=True) ->np.float64 :
    """_summary_

    Parameters
    ----------
    s : str
        _description_
    p : np.float64
        _description_

    Returns
    -------
    np.float64
        _description_
    """    
    code_gbk=np.array([int(char.encode("gbk").hex(),16) for char in s])
    powarray=np.power(p,np.arange(start=len(code_gbk),stop=0,step=-1)-1)
    hash_value=np.sum(code_gbk*powarray)
    return hash_value

def test_hash(s:str,p,round=True):
    l=re.split(r"\d{1,2}",s)
    return [hash_string(l[0]+str(i)+l[1],p,round)  for i in range(1,11) ]   
