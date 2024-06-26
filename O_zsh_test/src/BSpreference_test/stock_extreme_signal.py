# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.signal
import datetime

# %matplotlib inline
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
plt.rcParams['axes.unicode_minus'] = False


def get_sign(point, arrmin, arrmax):
    if point in arrmin:
        return -1
    else:
        return 1


def get_min(arr):
    try:
        return min(arr)
    except:
        return 10 ** 10


def get_max(arr):
    try:
        return max(arr)
    except:
        return -10 ** 10


def get_extre(array, order=10):
    # step1：将股票价格序列进行随机化，避免同一区间内出现两个相同的最大值
    array = array + np.random.rand(len(array)) * 0.001
    # step2：滚动计算order区间内的极值点标识
    extres_max = scipy.signal.argrelextrema(array, np.greater, axis=0, order=order, mode='clip')[0]
    extres_min = scipy.signal.argrelextrema(array, np.less, axis=0, order=order, mode='clip')[0]
    # step3：进行不符合条件的极值点清理
    # extre_now赋初始值为最左侧的极值点
    extre_now = min(min(np.append(extres_min, 10 ** 10)), min(np.append(extres_max, 10 ** 10)))
    # while循环，使用extre_now变量作为指针，在已有的极值点位处从左到右观察，如出现不符合要求的情况，则删除对应的极值点，并将extre_now归为原始值
    while extre_now < max(max(np.append(extres_min, 0)), max(np.append(extres_max, 0))):
        extre_past = extre_now
        # rolling为extre_now右侧的极值点，将extre_now滚动到下一个极值点
        extres_max_rolling = extres_max[extres_max > extre_past]
        extres_min_rolling = extres_min[extres_min > extre_past]
        extre_now = min(min(np.append(extres_min_rolling, 10 ** 10)), min(np.append(extres_max_rolling, 10 ** 10)))
        # sign为extre_past、extre_now在极值点的归属，-1为极小值，1为极大值
        extre_past_sign = get_sign(extre_past, extres_min, extres_max)
        extre_now_sign = get_sign(extre_now, extres_min, extres_max)
        # 开始分情况讨论，需要删去的极值点情况
        # 情况1：extre_past、extre_now均为极小值，则删去对应股价较高的极值点
        if extre_past_sign + extre_now_sign < 0:
            if array[extre_past] <= array[extre_now]:
                extres_min = np.delete(extres_min, np.where(extres_min == extre_now))
            elif array[extre_past] > array[extre_now]:
                extres_min = np.delete(extres_min, np.where(extres_min == extre_past))
            extre_now = min(min(np.append(extres_min, 10 ** 10)), min(np.append(extres_max, 10 ** 10)))
        # 情况2：extre_past、extre_now均为极大值，则删去对应股价较低的极值点
        elif extre_past_sign + extre_now_sign > 0:
            if array[extre_past] < array[extre_now]:
                extres_max = np.delete(extres_max, np.where(extres_max == extre_past))
            elif array[extre_past] >= array[extre_now]:
                extres_max = np.delete(extres_max, np.where(extres_max == extre_now))
            extre_now = min(min(np.append(extres_min, 10 ** 10)), min(np.append(extres_max, 10 ** 10)))
        # 情况1、2均为出发时：进入后续情况判定
        else:
            # 触发以下条件时，删除extre_past、extre_now极值点对
            # （1）extre_past至extre_now区间的最小值小于extre_past、extre_now的极低值点，即反向区间
            # （2）extre_past至extre_now区间的最大值大于extre_past、extre_now的极高值点，即反向区间
            # （3）extre_past和extre_now对应的股价相同
            if (array[extre_past:extre_now].min() < min(array[extre_past], array[extre_now])
                    or array[extre_past:extre_now].max() > max(array[extre_past], array[extre_now])
                    or abs(array[extre_past] - array[extre_now]) < 0.1):
                extres_max = np.delete(extres_max, np.where(extres_max == extre_past))
                extres_min = np.delete(extres_min, np.where(extres_min == extre_past))
                extres_max = np.delete(extres_max, np.where(extres_max == extre_now))
                extres_min = np.delete(extres_min, np.where(extres_min == extre_now))
                extre_now = min(get_min(extres_min), get_min(extres_max))
        # while循环至最后一个极值点后，判断结束
    # 左端点值的处理，如果第一个极值点不是最左点，若第一个极值点为极小值，若最左点大于第一个极值点，则将最左点设为极大值点，反之，则删除第一个极值点，将最左点
    # 设为极小值点（即将极小值点移动到最左点）；其他情况类似
    if min(min(np.append(extres_min, 10 ** 10)), min(np.append(extres_max, 10 ** 10))) > 0:
        if get_min(extres_min) < get_min(extres_max):
            if array[extres_min[0]] < array[0] - 0.001:
                extres_max = np.insert(extres_max, 0, 0)
            else:
                extres_min = np.delete(extres_min, 0)
                extres_min = np.insert(extres_min, 0, 0)
        elif get_min(extres_min) > get_min(extres_max):
            if array[extres_max[0]] > array[0] + 0.001:
                extres_min = np.insert(extres_min, 0, 0)
            else:
                extres_max = np.delete(extres_max, 0)
                extres_max = np.insert(extres_max, 0, 0)
    max_point = len(array) - 1
    if max(max(np.append(extres_min, -10 ** 10)), max(np.append(extres_max, -10 ** 10))) < max_point:
        if get_max(extres_min) < get_max(extres_max):
            if array[extres_max[-1]] > array[-1] + 0.001:
                extres_min = np.insert(extres_min, -1, max_point) if len(extres_min) > 0 else np.insert(extres_min, 0,
                                                                                                        max_point)
            else:
                extres_max = np.delete(extres_max, -1)
                extres_max = np.insert(extres_max, -1, max_point) if len(extres_max) > 0 else np.insert(extres_max, 0,
                                                                                                        max_point)
        elif get_max(extres_min) > get_max(extres_max):
            if array[extres_min[-1]] < array[-1] - 0.001:
                extres_max = np.insert(extres_max, -1, max_point) if len(extres_max) > 0 else np.insert(extres_max, 0,
                                                                                                        max_point)
            else:
                extres_min = np.delete(extres_min, -1)
                extres_min = np.insert(extres_min, -1, max_point) if len(extres_min) > 0 else np.insert(extres_min, 0,
                                                                                                        max_point)
    return (extres_min, extres_max)


def get_stock_extreme_info(order, stock_position_port, stock_data_all):
    stocks = list(set(stock_position_port['windcode']))
    result_list = []

    for stock in stocks:
        stock_data = stock_data_all[stock_data_all['windcode'] == stock]

        # 如果财汇股票行情表里没有该证券代码的信息，说明不是股票跳过当前循环
        if len(stock_data.index) == 0:
            continue

        # 提取股票价格数据，并按日期排序，去除NaN值
        stock_price = pd.DataFrame({
            'backdate': stock_data['backdate'],
            'close': stock_data['S_DQ_ADJCLOSE']
        })
        stock_price = stock_price.sort_values(by='backdate').dropna()

        # 确定order天之前的日期
        order_date = (datetime.datetime.now() - datetime.timedelta(days=order))

        # 只选取当前时间-order天之前的数据
        recent_stock_price = stock_price[stock_price['backdate'] < order_date]

        extres_min_indices, extres_max_indices = get_extre(recent_stock_price['close'].values, order)
        extres_min_date = recent_stock_price.iloc[extres_min_indices]['backdate'].values
        extres_max_date = recent_stock_price.iloc[extres_max_indices]['backdate'].values

        # 格式化日期并添加到结果列表
        for date in [extres_min_date, extres_max_date]:
            for single_date in date:
                result_list.append({
                    'stock_code': stock,
                    'trade_date': single_date,
                    'stock_adjclose':
                        recent_stock_price.loc[recent_stock_price['backdate'] == single_date, 'close'].values[0],
                    'extreme_type': -1 if date is extres_min_date else 1
                })

    result_df = pd.DataFrame(result_list)

    # 返回最终的DataFrame
    return result_df


if __name__ == '__main__':
    all_stock_turn_volume = pd.read_csv('../石化投资组合股票交易数据_240603_部分测试数据.csv')
    all_stock_price = pd.read_csv('../财汇股票行情数据_240603.csv')

    all_stock_turn_volume = all_stock_turn_volume[['PORTFOLIOID', 'STOCK_CODE', 'CJSL', 'BCRQ']]

    all_stock_turn_volume.rename(columns={'STOCK_CODE': 'windcode', 'CJSL': 'trade', 'BCRQ': 'backdate'}, inplace=True)
    all_stock_price.rename(columns={'SYMBOL': 'windcode', 'TCLOSE': 'S_DQ_ADJCLOSE', 'TRADEDATE': 'backdate'},
                           inplace=True)

    all_stock_turn_volume['backdate'] = pd.to_datetime(all_stock_turn_volume['backdate'].astype(str), format='%Y%m%d')
    all_stock_price['backdate'] = pd.to_datetime(all_stock_price['backdate'].astype(str), format='%Y%m%d')

    # 取all_stock_price时间在20150101之后的数据
    all_stock_price = all_stock_price[all_stock_price['backdate'] > '20150101']

    stock_extreme_info = get_stock_extreme_info(30, all_stock_turn_volume, all_stock_price)

    stock_extreme_info.to_csv('财汇股票行情数据_240603_极值数据V2.csv', index=False)
