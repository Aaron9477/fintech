# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年8月1日14:40:54
# @Author    : Noah Zhan
# @File      : fillna_within_n
# @Project   : 银行理财代销图鉴
# @Function  ：对数据进行中间值的缺失值填充，即当缺失值前后都有有效数据时才填充。
# --------------------------------
import pandas as pd

def fillna_within_n(x,null_n=8,axis_fill=0):
    '''
    function:传入一列或一行数据，对数据中中间有缺失的数据进行有条件填充，即连续缺失小于等于8个记录的，使用上一个有效值进行填充。
    params:
        - x:pd.DataFrame/pd.Serise,需要填充的原始数据；
        - null_n:int/float,最大允许的连续缺失数量；
        - axis_fill:数据的填充方向，axis_fill=0为航向填充，1为竖向填充。
    return:
        - 修改后的数据表。 
    '''
    if axis_fill == 0:
        return func_horizontal_fillna(x,null_n=null_n)
    elif axis_fill == 1:
        return func_vertical_fillna(x,null_n=null_n)
    else:
        raise ValueError('axis='+str(axis_fill)+" is not allowed, use 0 for horizontal fillna, 1 for vertical fillna.")



def func_horizontal_fillna(x,null_n=8):
    #填补缺失值，对矩阵按照横向方向填补，默认n为8
    col=len(x)
    i=1
    while i<col:
        if pd.isnull(x.iloc[i]):
            k=1
            if i+k < col:
                while pd.isnull(x.iloc[i+k]):
                    k=k+1
                    if i+k >= col:
                        break
            if k<=null_n:
                x.iloc[i:i+k]=x.iloc[i-1]
                i=i+k
            else:
                i=i+k
        else:
            i=i+1
    return x

def func_vertical_fillna(x,null_n=8):
    #填补缺失值，对矩阵按照竖向方向填补，默认n为8
    row=x.shape[0]
    i=0
    while i<row:
        if pd.isnull(x.iloc[i,-1]):
            k=1
            if i+k < row:
                while pd.isnull(x.iloc[i+k,-1]):
                    k=k+1
                    if i+k >= row:
                        break
            if k<=null_n:
                x.iloc[i:i+k,-1]=x.iloc[i-1,-1]
                i=i+k
            else:
                i=i+k
        else:
            i=i+1
    return x