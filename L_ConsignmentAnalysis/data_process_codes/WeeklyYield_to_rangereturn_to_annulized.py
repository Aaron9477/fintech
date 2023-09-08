# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月21日10:35:52
# @Author    : Noah Zhan
# @File      : WeeklyYield_to_rangereturn_to_annulized
# @Project   : 银行理财代销图鉴
# @Function  ：根据将七日年化序列数据计算以最新期为截止时间的区间年化收益
# --------------------------------
import pandas as pd

def WeeklyYield_to_rangereturn_to_annulized(x,length = 13,frequency = 1):
    '''
    function:根据将七日年化序列数据计算以最新期为截止时间的区间年化收益
    params:
        - x:pd.Series/pd.Dataframe，现金管理类产品的七日年化序列数据;
        - length:int,区间的长度，例如=13/52为，计算三个月/一年的区间收益
        - frequency:int,原始数据的频率，=1/7，则原始数据为日度/周度。
    return:
        - np.nan/sum(x.iloc[ind])*(7/365)*0.01
    '''
    if(frequency not in [1,7]):
        raise ValueError('数据频率只能指定为日度（frequency=1）或周度（frequency=7）。')
    if isinstance(x,pd.Series):
        temp = x.copy()
        x=pd.DataFrame()
        x['LatestWeeklyYield'] = temp.to_frame()
        x['EndDate'] = temp.index

    if(x.sort_index(ascending=True).iloc[-1].empty):#最近一期是为空
        return
    x = x.sort_index(ascending=True)['LatestWeeklyYield'].fillna(method='ffill')
    ind = []
    for i in range(0,length):
        ind.append(int(-1-i*( 7 / frequency)))
    try:
        x.iloc[ind[-1]]
    except:
        return
    return sum(x.iloc[ind])*(7/365)*0.01/length*52