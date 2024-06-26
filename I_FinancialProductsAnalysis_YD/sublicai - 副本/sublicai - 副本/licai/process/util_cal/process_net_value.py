# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/11 11:02 
# @Author    : Wangyd5 
# @File      : process_net_value
# @Project   : licai
# @Function  ：处理普益的理财净值
# --------------------------------

import numpy as np
import pandas as pd
from database.read.read_py_base import PyReader
import traceback

reader = PyReader()

def function(b):
    # print(type(b))
    if np.isnan(b) == False:
        return b


'''结果输出为dataframe'''
def result_dataframe(series, df):

    FinProCode = df.loc[list(series.dropna().index), 'FinProCode'].values
    date = df.loc[list(series.dropna().index), 'trade_dt'].values
    UnitNV = df.loc[list(series.dropna().index), 'UnitNV'].values
    AccumulatedUnitNV = df.loc[list(series.dropna().index), 'AccumulatedUnitNV'].values

    result = pd.DataFrame({'FinProCode':FinProCode,
                           'trade_dt':date,
                            'UnitNV': UnitNV,
                           'AccumulatedUnitNV': AccumulatedUnitNV,
                           'net_value': series.dropna().values,
                           'RateOfReturn': series.dropna().pct_change().values})

    return result




def result_check(dataframe, tail_null, last_not_null_index):
    result = dataframe.copy()
    del_5 = []
    del_6 = []
    result['RateOfReturn'] = result['net_value'].dropna().pct_change()

    '''判断开头是否有异常值并删除'''
    first_notnull = (result['AccumulatedUnitNV'].isna() == False).argmax()
    if result['RateOfReturn'].iloc[first_notnull] < 0 and result['RateOfReturn'].iloc[
                                                          first_notnull + 1:].mean() > 0.002 and len(result) > 3:
        del_6 = result.index[:first_notnull]
        result = result.iloc[first_notnull:]

    '''判断末尾是否有异常值并删除'''
    if tail_null == 1:
        rate_mean = (abs(result['RateOfReturn'])).mean()
        drop_index_0 = result[(result['AccumulatedUnitNV'].isnull()) & (
                    (abs(result['RateOfReturn']) > 8 * rate_mean) | (abs(result['RateOfReturn']) > 0.045)) & (
                                          abs(result['RateOfReturn']) > 0.015)].index
        for i in drop_index_0:
            if i >= last_not_null_index:
                del_5 = result.index[result.index.get_loc(i):]
                result = result.iloc[:result.index.get_loc(i)]
                break

    '''通过收益率判断其他位置是否有异常值并删除'''
    rate_mean = (abs(result['RateOfReturn'])).mean()
    drop_index_0 = result[(result['AccumulatedUnitNV'].isnull()) & (abs(result['RateOfReturn']) > 8 * rate_mean) & (
                abs(result['RateOfReturn']) > 0.015)].index
    drop_index_1 = result[(result['AccumulatedUnitNV'].isnull() == False) & (abs(result['RateOfReturn']) > 0.1)].index
    drop_index = []
    for i in drop_index_0:
        if abs(result.iloc[result.index.get_loc(i) + 1, -1]) > 8 * rate_mean and result.iloc[
            result.index.get_loc(i) + 1, -1] * result.iloc[result.index.get_loc(i), -1] < 0:
            drop_index.append(i)
    for j in drop_index_1[:-1]:
        if abs(result.iloc[result.index.get_loc(j) + 1, -1]) > 0.1 and result.iloc[result.index.get_loc(j) + 1, -1] * \
                result.iloc[result.index.get_loc(j), -1] < 0:
            drop_index.append(j)
    result.drop(drop_index, axis=0, inplace=True)

    result['RateOfReturn'] = result['net_value'].pct_change()

    # print('根据收益率判断开头有异常值共删除'+str(len(del_6))+'行：')
    # print(del_6)
    # print('根据收益率判断末尾有异常值共删除'+str(len(del_5))+'行：')
    # print(del_5)
    # print('根据收益率判断其他位置有异常值共删除'+str(len(drop_index))+'行：')
    # print(drop_index)

    return result[['FinProCode','trade_dt', 'net_value']].dropna(subset=['net_value']).sort_values('trade_dt')


def nav_fill(df):
    # dividend = [] #储存分红日期, 用于输出
    tail_null = 0  # 用作result_check的参数，为1表明末尾有缺失值，用于检验结果
    last_first_null_index = 0  # 用作result_check的参数，为末尾第一个缺失累计净值的index，用于检验结果

    '''读取数据并删除单位净值和累计净值均为空的行'''
    df_test = df[['trade_dt','FinProCode', 'UnitNV', 'AccumulatedUnitNV','yield_7_days_annual', 'earning_per_ten_thousand']]
    nan_nav_index = df_test[
        df_test['UnitNV'].isnull() & df_test['AccumulatedUnitNV'].isnull()].index  # 单位净值和累计净值均为空的行的index
    df_test = df_test.drop(nan_nav_index)

    '''删除末尾所有的 单位净值为1且累计净值为空 和 单位净值和累计净值均为1 的行'''
    # del_unitnv1 = [] #储存删除的 "末尾所有的 单位净值为1且累计净值为空 和 单位净值和累计净值均为1 的行" 的index, 用于输出
    n = 0
    for index, row in df_test.iloc[::-1].iterrows():
        if row['UnitNV'] == 1 and (np.isnan(row['AccumulatedUnitNV']) or row['AccumulatedUnitNV'] == 1):
            n = n + 1
        else:
            break
    if n != 0:
        # del_unitnv1 = df_test.index[-n:] #将符合条件的index存入del_unitnv1，用于输出
        df_test = df_test[:-n]

    '''删除中间单位净值为1累计净值为空且下一行单位净值仍为1的行'''
    # 找到所有单位净值为1累计净值为空的行index，这里不会取到最后一行，因为上一步已经删掉了末尾单位净值为1累计净值为空的行
    unitnv1_index = df_test[df_test['UnitNV'] == 1 & df_test['AccumulatedUnitNV'].isnull()].index
    unitnv1_index_del = []  # 储存所有单位净值为1累计净值为空且下一行单位净值仍为1的行，用于删除和输出
    for i in unitnv1_index:
        # 如果下一行单位净值为1
        if df_test.iloc[df_test.index.get_loc(i) + 1]['UnitNV'] == 1:
            unitnv1_index_del.append(i)
    df_test = df_test.drop(unitnv1_index_del)

    '''删除所有累计净值和单位净值之差有问题的行'''
    difference = (df_test['AccumulatedUnitNV'] - df_test['UnitNV']).dropna()
    diff_index_0 = difference[difference.diff(1) < -5e-4].index  # 找到累计净值和单位净值之差减小的行index
    diff_index = []  # 储存所有因为累计净值和单位净值之差有问题而被删除的行，用于删除和输出
    for i in diff_index_0:
        if i == df_test.index[-1]:
            j = df_test.index.get_loc(i)
            df_test.iloc[j, -1] = df_test.iloc[j - 1, -1] + df_test.iloc[j, 2] - df_test.iloc[j - 1, 2]
        elif difference.diff(1).iloc[difference.index.get_loc(i) + 1] > 5e-4:
            diff_index.append(i)
        elif abs(difference.diff(2).loc[i]) < 1e-4:
            diff_index.append(difference.index[difference.index.get_loc(i) - 1])
        elif abs(difference.diff(3).loc[i]) < 1e-4:
            diff_index.append(difference.index[difference.index.get_loc(i) - 1])
            diff_index.append(difference.index[difference.index.get_loc(i) - 2])
    df_test.drop(diff_index, inplace=True)

    '''若所有行都被删除'''
    if len(df_test) == 0:
        df_test['net_value'] = np.nan
        df_test['RateOfReturn'] = np.nan
        return df_test

    '''有累计净值就用累计净值'''
    df_test.index = range(len(df_test))  # 修改index为连续的整数
    df_test['net_value'] = df_test['AccumulatedUnitNV']

    '''检验累计净值是否全为空值，若是则全用单位净值'''
    if df_test['net_value'].isnull().all() == True:
        df_test['net_value'] = df_test['UnitNV']
        tail_null = 1  # 这种情况累计净值全部缺失，因此末尾也有缺失值
        last_first_null_index = df_test.index[0]  # 累计净值从第一个开始连续缺失到最后一个，因此末尾处首个累计净值缺失的index为第一行index
        return result_check(df_test, tail_null, last_first_null_index)

    index_notnull = df_test[df_test['net_value'].isnull() == False].index  # 累计净值非空的index

    '''检验开头是否有缺失值并填充'''
    # 如果累计净值非空的首个index即为dataframe的首个index，说明开头处没有缺失值
    if df_test.index[0] == index_notnull[0]:
        pass
    else:
        # 开头处的缺失值从后往前倒序填充
        for i in df_test[:df_test.index.get_loc(index_notnull[0])].index[::-1]:
            # 当期累计净值 = 下一期累计净值 - 下一期单位净值 + 当期单位净值 = 分红 + 当期单位净值
            df_test.loc[i, 'net_value'] = df_test.loc[i + 1, 'net_value'] - df_test.loc[
                i + 1, 'UnitNV'] + df_test.loc[i, 'UnitNV']

    '''检验结尾是否有缺失值并填充'''
    # 如果累计净值非空的最后一个index即为dataframe的最后一个index，说明结尾处没有缺失值
    if df_test.index[-1] == index_notnull[-1]:
        pass
    else:
        # 结尾处的缺失值从前往后正序填充
        tail_null = 1
        last_null_index = df_test[df_test.index.get_loc(index_notnull[-1]) + 1:].index  # 结尾处累计净值缺失的index
        last_first_null_index = last_null_index[0]  # 结尾处累计净值缺失的首个index
        for i in last_null_index:
            # 当期累计净值 = 上一期累计净值 - 上一期单位净值 + 当期单位净值 = 分红 + 当期单位净值
            df_test.loc[i, 'net_value'] = df_test.loc[i - 1, 'net_value'] - df_test.loc[
                i - 1, 'UnitNV'] + df_test.loc[i, 'UnitNV']

    '''检验中间是否有缺失值并填充'''
    index_notnull = df_test[
        df_test['net_value'].isnull() == False].index  # 开头结尾填充完毕后再找一次累计净值非空的index，用于判断中间是否有缺失值
    # 若dataframe的长度和累计净值非空的index长度相等说明中间没有缺失值
    if len(df_test) == len(index_notnull):
        pass
    else:
        # 中间的缺失值一段一段填充
        nan_interval = []
        for i in range(len(index_notnull) - 1):
            if index_notnull[i + 1] - index_notnull[i] == 1:  # 若连续两个index的累计净值均不缺失，则这两个index中间没有需要填充的累计净值，跳过
                pass
            else:
                T = (index_notnull[i], index_notnull[i + 1])  # 每段缺失值两端累计净值不缺失的index构成的元组
                nan_interval.append(T)

        # 依次填充每段缺失值
        for i in range(len(nan_interval)):
            index1 = nan_interval[i][0]
            index2 = nan_interval[i][1]
            diff1 = df_test.loc[index1, 'AccumulatedUnitNV'] - df_test.loc[index1, 'UnitNV']
            diff2 = df_test.loc[index2, 'AccumulatedUnitNV'] - df_test.loc[index2, 'UnitNV']

            # 如果有分红
            if diff2 - diff1 > 0.0002:
                rate_of_return = df_test.loc[index1:index2, 'UnitNV'].pct_change()
                timedelta = df_test.loc[index1:index2, 'trade_dt'] - df_test.loc[index1:index2, 'trade_dt'].shift(1)
                # 单位净值日平均变化最小的一天判定为分红日
                index_dividend = (rate_of_return / (timedelta.map(lambda x: x.days))).idxmin()
                # dividend.append(df_test.loc[index_dividend, 'trade_dt'])
                # 分红日及之后，从后向前填充
                for i in range(index2 - 1, index_dividend - 1, -1):
                    # 当期累计净值 = 下一期累计净值 - 下一期单位净值 + 当期单位净值 = 分红 + 当期单位净值
                    df_test.loc[i, 'net_value'] = df_test.loc[i + 1, 'net_value'] - df_test.loc[
                        i + 1, 'UnitNV'] + df_test.loc[i, 'UnitNV']
                # 分红日前，从前向后填充
                for i in range(index1 + 1, index_dividend):
                    # 当期累计净值 = 上一期累计净值 - 上一期单位净值 + 当期单位净值 = 分红 + 当期单位净值
                    df_test.loc[i, 'net_value'] = df_test.loc[i - 1, 'net_value'] - df_test.loc[
                        i - 1, 'UnitNV'] + df_test.loc[i, 'UnitNV']
            else:
                # 若无分红，从前向后填充
                for i in df_test.loc[index1 + 1:index2 - 1].index:
                    # 当期累计净值 = 上一期累计净值 - 上一期单位净值 + 当期单位净值 = 分红 + 当期单位净值
                    df_test.loc[i, 'net_value'] = df_test.loc[i - 1, 'net_value'] - df_test.loc[
                        i - 1, 'UnitNV'] + df_test.loc[i, 'UnitNV']

    # print('单位净值和累计净值均为空共'+str(len(nan_nav_index))+'行：')
    # print(list(nan_nav_index))
    # print('删除末尾所有的单位净值为1，且累计净值为空或为1共'+str(n)+'行：')
    # print(list(del_2))
    # print('删除中间单位净值为1累计净值为空且下一行单位净值仍为1共'+str(len(unitnv1_index_del))+'行：')
    # print(unitnv1_index_del)
    # print('由于累计净值和单位净值的差有问题删除'+str(len(diff_index))+'行：')
    # print(diff_index)
    # print('分红'+str(len(dividend))+'次，分红时的日期为：')
    # print(dividend)

    return result_check(df_test, tail_null, last_first_null_index)


def product_type(x):
    if x == '母产品':
        return 1.5
    else:
        return 1


# 有份额数据后的值可能要再改
def representative(RegistrationCode,info, latest_date_weight=3, share_weight=1, timespan_weight=2):
    # 获取净值信息
    cp_id_list = info[info['RegistrationCode'] == RegistrationCode]['FinProCode'].tolist()
    nav_df = reader.get_net_value(cp_id=cp_id_list)
    if len(nav_df.dropna(subset=['UnitNV','AccumulatedUnitNV'])) == 0:
        return pd.Series([], name=cp_id_list[0])

    latest_date = nav_df['trade_dt'].max()
    product_df = pd.DataFrame(columns=['LatestDate', 'ProductType', 'Shares', 'TimeSpan', 'Score'])
    nav_dict = {}
    for code in cp_id_list:
        tmp_df = nav_df[nav_df['FinProCode'] == code].copy()
        try:
            result = nav_fill(tmp_df)
        except:
            print(traceback.format_exc())
            continue

        nav_dict[code] = result
        if len(result) > 0:
            last_date = result['trade_dt'].iloc[-1]
            first_date = result['trade_dt'].iloc[0]
            product_df.loc[code, 'LatestDate'] = last_date
            product_df.loc[code, 'ProductType'] = info[info['FinProCode'] == code]['ProductType'].values[0]
            product_df.loc[code, 'Shares'] = np.nan
            product_df.loc[code, 'TimeSpan'] = (last_date - first_date).days + 1
    product_df.fillna(0, inplace=True)

    shares_sum = product_df['Shares'].sum()
    if shares_sum == 0:
        shares_sum = 1
    date_score = (latest_date - product_df['LatestDate']).apply(lambda x: x.days)
    product_df['Score'] = - latest_date_weight * date_score + \
                          share_weight * product_df['ProductType'].apply(lambda x: product_type(x)) * product_df[
                              'Shares'] / shares_sum + \
                          timespan_weight * (product_df['TimeSpan'] + date_score)

    product_df = product_df[product_df['Score'] == product_df['Score'].max()]
    if len(product_df) > 0:
        represent_finprocode = product_df.index[0]
    else:
        represent_finprocode = cp_id_list[0]
    represent_result = nav_dict[represent_finprocode]
    return pd.Series(represent_result['net_value'].values, index=represent_result['trade_dt'].values,
                     name=represent_finprocode)


if __name__ == '__main__':
    from database.read.read_py_base import PyReader
    reader = PyReader()
    # cp_id = 1304354
    # net_value = reader.get_net_value(cp_id=cp_id)
    # df_new = nav_fill(net_value)

    # 测试代表性产品代码
    from tools.tools import Timer
    info = reader.get_bank_wealth_product()
    reg_code_list = list(info['RegistrationCode'].unique())
    # reg_code_list = ['Z7002120000004']
    problem_list = []
    with Timer(True):
        for i,reg_code in enumerate(reg_code_list):
            try:
                reg_code = 'Z7002120000004'
                print(i,reg_code,round(i/len(reg_code_list)*100,4))
                rep = representative(RegistrationCode=reg_code, info=info)
            except Exception as e:
                print(traceback.format_exc())
                problem_list.append(reg_code)

    # with open(r'D:\institution\sublicai\licai\a.txt','w') as f:
    #     f.writelines(problem_list)

