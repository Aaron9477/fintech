# -*- coding: utf-8 -*-
# --------------------------------
# @Time      : 2023年7月27日
# @Author    : WSS
# @File      : main_first_累计净值填充
# @Project   : 银行理财代销图鉴
# @Function  ：使用【py_all_net_value_0704】生成【all_nv_data_new】依赖表
# --------------------------------

import numpy as np
import pandas as pd
from tqdm import tqdm

def function(b):
    if np.isnan(b) == False:
        return b

def result_check(df):
    
    result = df.copy()
    del_5 = []
    result['RateOfReturn'] = result['AccumulatedUnitNV_new'].dropna().pct_change()
    '''判断末尾是否有异常值并删除'''
    if tail_null == 1:
        rate_mean = (abs(result['RateOfReturn'])).mean()
        drop_index_0 = result[(result['AccumulatedUnitNV'].isnull()) & ((abs(result['RateOfReturn']) > 8*rate_mean) | (abs(result['RateOfReturn']) > 0.045)) & (abs(result['RateOfReturn']) > 0.015)].index
        for i in drop_index_0:
            if i>= last_not_null_index:
                del_5 = result.index[result.index.get_loc(i):]
                result = result.iloc[:result.index.get_loc(i)]
                break    
    
    '''通过收益率判断其他位置是否有异常值并删除'''
    rate_mean = (abs(result['RateOfReturn'])).mean()
    drop_index_0 = result[(result['AccumulatedUnitNV'].isnull()) & (abs(result['RateOfReturn']) > 8*rate_mean) & (abs(result['RateOfReturn']) > 0.015)].index
    drop_index_1 = result[(result['AccumulatedUnitNV'].isnull() == False) & (abs(result['RateOfReturn']) > 0.1)].index
    drop_index = []
    for i in drop_index_0:
        if abs(result.iloc[result.index.get_loc(i) + 1, -1]) > 8*rate_mean and result.iloc[result.index.get_loc(i) + 1, -1] * result.iloc[result.index.get_loc(i), -1] < 0:
            drop_index.append(i)
    for j in drop_index_1[:-1]:
        if abs(result.iloc[result.index.get_loc(j) + 1, -1]) > 0.1 and result.iloc[result.index.get_loc(j) + 1, -1] * result.iloc[result.index.get_loc(j), -1] < 0:
            drop_index.append(j)
    result.drop(drop_index, axis = 0,inplace = True)
    
    result['RateOfReturn'] = result['AccumulatedUnitNV_new'].pct_change()
    
    #print('根据收益率判断末尾有异常值共删除'+str(len(del_5))+'行：')
    #print(del_5)
    #print('根据收益率判断其他位置有异常值共删除'+str(len(drop_index))+'行：')
    #print(drop_index)
    
    return result

def nav_fill(code):
    
    '''读取数据并删除单位净值和累计净值均为空的行'''
    global df
    df_test = df[df['FinProCode'] == code]
    nan_nav_index = df_test[df_test['UnitNV'].isnull()&df_test['AccumulatedUnitNV'].isnull()].index
    df_test = df_test.drop(nan_nav_index)
    dividend = []
    global tail_null
    tail_null = 0
    del_2 = []
    
    '''删除末尾所有的 单位净值为1且累计净值为空 和 单位净值为和累计净值均为1 的行'''
    n = 0
    for index,row in df_test.iloc[::-1].iterrows():
        if row['UnitNV'] == 1 and (np.isnan(row['AccumulatedUnitNV']) or row['AccumulatedUnitNV'] == 1):
            n = n+1
            print(code, index, '末尾删除')
        else:
            break
    if n != 0:
        del_2 = df_test.index[-n:]
        df_test = df_test[:-n]
        
    '''删除中间单位净值为1累计净值为空且下一行单位净值仍为1的行'''
    unitnv1_index = df_test[df_test['UnitNV'] == 1 & df_test['AccumulatedUnitNV'].isnull()].index
    unitnv1_index_del = []
    for i in unitnv1_index:
        if df_test.iloc[df_test.index.get_loc(i) + 1, -2] == 1:
            unitnv1_index_del.append(i)
    df_test = df_test.drop(unitnv1_index_del)
    
    '''删除所有累计净值和单位净值之差有问题的行'''
    difference = (df_test['AccumulatedUnitNV'] - df_test['UnitNV']).dropna()
    diff_index_0 = difference[difference.diff(1)<-5e-4].index
    diff_index = []
    for i in diff_index_0:
        if i == df_test.index[-1]:
            j = df_test.index.get_loc(i)
            df_test.iloc[j,-1] = df_test.iloc[j-1,-1]+df_test.iloc[j,2]-df_test.iloc[j-1,2]
        elif difference.diff(1).iloc[difference.index.get_loc(i) + 1] > 5e-4:
            diff_index.append(i)
        elif abs(difference.diff(2).loc[i]) < 1e-4:
            diff_index.append(difference.index[difference.index.get_loc(i) - 1])
        elif abs(difference.diff(3).loc[i]) < 1e-4:
            diff_index.append(difference.index[difference.index.get_loc(i) - 1])
            diff_index.append(difference.index[difference.index.get_loc(i) - 2])
    df_test.drop(diff_index, inplace = True)
    
    '''若所有行都被删除'''
    if len(df_test) == 0:
        df_test['AccumulatedUnitNV_new'] = np.nan
        df_test['RateOfReturn'] = np.nan
        return df_test
    
    '''有累计净值就用累计净值'''
    df_test['AccumulatedUnitNV_new'] = df_test.apply(lambda x : function(x['AccumulatedUnitNV']),axis = 1)
    
    index_notnull = df_test[df_test['AccumulatedUnitNV_new'].isnull() == False].index
    num_notnull = []
    for j in index_notnull:
        num = df_test.index.get_loc(j)
        num_notnull.append(num)
    
    '''检验累计净值是否全为空值，若是则全用单位净值'''
    if df_test['AccumulatedUnitNV_new'].isnull().all() == True:
        df_test['AccumulatedUnitNV_new'] = df_test['UnitNV'].dropna()
        return result_check(df_test)
        
    '''检验开头是否有缺失值并填充'''
    if df_test.index[0] == index_notnull[0]:
        pass
    else:
        for i in range(num_notnull[0]-1,-1,-1):
            df_test.iloc[i,-1] = df_test.iloc[i+1,-1]+df_test.iloc[i,2]-df_test.iloc[i+1,2]
            
    '''检验结尾是否有缺失值并填充'''
    if df_test.index[-1] == index_notnull[-1]:
        pass
    else:
        global last_not_null_index
        tail_null = 1
        last_not_null_index = df_test.index[num_notnull[-1]+1]
        for i in range(num_notnull[-1]+1,len(df_test)):
            df_test.iloc[i,-1] = df_test.iloc[i-1,-1]+df_test.iloc[i,2]-df_test.iloc[i-1,2]
            
    '''检验中间是否有缺失值并填充'''
    index_notnull = df_test[df_test['AccumulatedUnitNV_new'].isnull() == False].index
    num_notnull = []
    for j in index_notnull:
        num = df_test.index.get_loc(j)
        num_notnull.append(num)
    if len(df_test) == len(num_notnull):
        pass
    else:
        nan_interval = []
        for i in range(len(num_notnull)-1):
            if num_notnull[i+1] - num_notnull[i] == 1:
                pass
            else:
                T = (num_notnull[i],num_notnull[i+1])
                nan_interval.append(T)
        for i in range(len(nan_interval)):
            num1 = nan_interval[i][0]
            num2 = nan_interval[i][1]
            diff1 = df_test.iloc[num1,3]-df_test.iloc[num1,2]
            diff2 = df_test.iloc[num2,3]-df_test.iloc[num2,2]
            
            '''判断是否有分红'''
            if diff2 - diff1 > 0.0002:
                rate_of_return = df_test.iloc[num1:num2+1,2].pct_change()
                timedelta = df_test.iloc[num1:num2+1,0] - df_test.iloc[num1:num2+1,0].shift(1)
                index_dividend = (rate_of_return/(timedelta.map(lambda x:x.days))).idxmin()
                dividend.append(index_dividend)
                num_dividend = df_test.index.get_loc(index_dividend)
                for i in range(num2-1,num_dividend-1,-1):
                    df_test.iloc[i,-1] = df_test.iloc[i+1,-1]+df_test.iloc[i,2]-df_test.iloc[i+1,2]
                for i in range(num1+1,num_dividend):
                    df_test.iloc[i,-1] = df_test.iloc[i-1,-1]+df_test.iloc[i,2]-df_test.iloc[i-1,2]
            #若无分红直接填充
            else:
                for i in range(num1+1,num2):
                    df_test.iloc[i,-1] = df_test.iloc[i-1,-1]+df_test.iloc[i,2]-df_test.iloc[i-1,2]
    
    #print('单位净值和累计净值均为空共'+str(len(nan_nav_index))+'行：')
    #print(list(nan_nav_index))
    #print('删除末尾所有的单位净值为1，且累计净值为空或为1共'+str(n)+'行：')
    #print(list(del_2))
    #print('删除中间单位净值为1累计净值为空且下一行单位净值仍为1共'+str(len(unitnv1_index_del))+'行：')
    #print(unitnv1_index_del)
    #print('由于累计净值和单位净值的差有问题删除'+str(len(diff_index))+'行：')
    #print(diff_index)
    #print('分红'+str(len(dividend))+'次，分红时的index为：')
    #print(dividend)
    
    return result_check(df_test)

#修改文件路径
df = pd.read_csv('./raw_datas/py_all_net_value_0704.csv')
path_outputdir = './raw_datas'

df['EndDate'] = pd.to_datetime(df['EndDate'])
df = df[['EndDate','FinProCode','UnitNV','AccumulatedUnitNV']] 

result=pd.DataFrame(columns=df.columns)
code_list=df['FinProCode'].drop_duplicates()  
for i in tqdm(code_list,desc="数据填充进度："):
    # print(i)
    result_=nav_fill(i)
    result=pd.concat([result,result_])
result.to_csv(path_outputdir+r'\all_nv_data_new.csv')
