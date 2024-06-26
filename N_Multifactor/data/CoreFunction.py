# -*- coding: utf-8 -*-
"""
Created on Mar18 2022
@author: lihbjs
"""
# %% 导入包和参数设置
import os
import sys
import re
import math
import pandas as pd
import numpy as np
from WindPy import w
import empyrical as em
import quantstats as qs
import matplotlib.pyplot as plt
import time
import warnings
from datetime import datetime
from tqdm import tqdm  # 循环进度条函数
from SupportFunction import *  # 加载自定义支持函数
import seaborn as sns
from itertools import product
import swifter
import cvxpy as cp

# os.getcwd()  # 获取当前工作目录
# os.chdir("C:/Users/Hao Li/Desktop/")  # 改变当前工作目录

# 设置报错
warnings.filterwarnings('ignore')

# 设置数据输出格式
pd.set_option('display.max_rows', 100)
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行

# 设置命令行输出时的列对齐功能
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 设置绘图显示
# plt.style.use('seaborn')
# plt.style.use('whitegrid')
plt.rcParams['font.sans-serif'] = ['Simhei']
plt.rcParams['axes.unicode_minus'] = False
# 设置默认路径
root = os.path.abspath(".")[:1]
path_fund = r"{}:\Wind数据库\DB_Fund.db".format(root)
path_stock = r"{}:\Wind数据库\DB_Stock.db".format(root)
path_index = r"{}:\Wind数据库\DB_Index.db".format(root)

# 获取交易日历，定期链接Wind数据源刷新一下日历
# w.start()
# tradeday_list = pd.DatetimeIndex(w.tdays("2005-01-05", "2025-01-01", "").Times)  # 其他模块调用时会生成tradeday_list对象
# temp = pd.DataFrame(tradeday_list)
# temp.columns = ['Trade_day']
# temp.to_excel('tradeday_list.xlsx', index=False)
tradeday_list = pd.DatetimeIndex(
    pd.read_excel(r'{}:\工作同步目录\2 公募基金评价\B 公募基金分析框架\Python代码\自定义函数\tradeday_list.xlsx'.format(root)).Trade_day)


# %% # 日期向前平移函数，用于计算向前追溯业绩
# 如果Tradeday=True，则返回最近交易日
# TODO 目前的1m只是月份数-1，比如20230228向前一个月就是20230128，并不是自然月末，需要增加一个shift_length选项是自然月末（仅针对月末统计）
def fstartday(end_date, shift_length="", tradeday=True, tradeday_list=tradeday_list, tradeday_shift='after'):
    end_date = pd.to_datetime(end_date)
    if shift_length == '':
        start_date = end_date
    elif shift_length == '1d' or shift_length == '1D':
        start_date = end_date + pd.DateOffset(days=-1)
    elif shift_length == '1w' or shift_length == '1W':
        start_date = end_date + pd.DateOffset(weeks=-1)
    elif shift_length == '1m' or shift_length == '1M':
        start_date = end_date + pd.DateOffset(months=-1)
    elif shift_length == '3m' or shift_length == '3M':
        start_date = end_date + pd.DateOffset(months=-3)
    elif shift_length == '6m' or shift_length == '6M':
        start_date = end_date + pd.DateOffset(months=-6)
    elif shift_length == '1y' or shift_length == '1Y':
        start_date = end_date + pd.DateOffset(years=-1)
    elif shift_length == '2y' or shift_length == '2Y':
        start_date = end_date + pd.DateOffset(years=-2)
    elif shift_length == '3y' or shift_length == '3Y':
        start_date = end_date + pd.DateOffset(years=-3)
    elif shift_length == '5y' or shift_length == '5Y':
        start_date = end_date + pd.DateOffset(years=-5)

    if tradeday == True:  # 强制要求区间起点首日为交易日
        if pd.DatetimeIndex([start_date]).isin(tradeday_list)[0] == True:  # 如果是交易日，则取当天
            start_date1 = start_date
        elif pd.DatetimeIndex([start_date]).isin(tradeday_list)[0] == False:
            if (tradeday_shift == 'before'):  # 如果区间起点不是交易日，向前找最近交易日
                start_date1 = tradeday_list.asof(start_date)
            elif (tradeday_shift == 'after'):  # 向后找最近交易日
                start_date1 = tradeday_list[tradeday_list.get_loc(tradeday_list.asof(start_date)) + 1]
        return start_date1
    else:
        return start_date


# %% 代码示例
'''
fstartday('20220417',shift_length='',tradeday=True,tradeday_shift='before') # 向前找到最近一个交易日
fstartday('20220417',shift_length='6m',tradeday=True,tradeday_shift='after') # 向前找到6个月前的最近一个交易日
fstartday('20220417', shift_length='6m', tradeday=True, tradeday_shift='before') # 向前找到6个月前的最近一个交易日
'''


# %% # 日期向后平移函数，用于计算回测收益
# 如果Tradeday=True，则返回最近交易日
def fendday(start_date, shift_length="", tradeday=True, tradeday_list=tradeday_list, tradeday_shift='after'):
    start_date = pd.to_datetime(start_date)
    if shift_length == '':
        end_date = start_date
    elif shift_length == '1d' or shift_length == '1D':
        end_date = start_date + pd.DateOffset(days=1)
    elif shift_length == '1w' or shift_length == '1W':
        end_date = start_date + pd.DateOffset(weeks=1)
    elif shift_length == '1m' or shift_length == '1M':
        end_date = start_date + pd.DateOffset(months=1)
    elif shift_length == '3m' or shift_length == '3M':
        end_date = start_date + pd.DateOffset(months=3)
    elif shift_length == '6m' or shift_length == '6M':
        end_date = start_date + pd.DateOffset(months=6)
    elif shift_length == '1y' or shift_length == '1Y':
        end_date = start_date + pd.DateOffset(years=1)
    elif shift_length == '2y' or shift_length == '2Y':
        end_date = start_date + pd.DateOffset(years=2)
    elif shift_length == '3y' or shift_length == '3Y':
        end_date = start_date + pd.DateOffset(years=3)
    elif shift_length == '5y' or shift_length == '5Y':
        end_date = start_date + pd.DateOffset(years=5)

    if tradeday == True:  # 强制要求区间起点首日为交易日
        if pd.DatetimeIndex([end_date]).isin(tradeday_list)[0] == True:  # 如果是交易日，则取当天
            end_date1 = end_date
        elif pd.DatetimeIndex([end_date]).isin(tradeday_list)[0] == False:
            if (tradeday_shift == 'before'):  # 如果区间起点不是交易日，向前找最近交易日
                end_date1 = tradeday_list.asof(end_date)
            elif (tradeday_shift == 'after'):  # 向后找最近交易日
                end_date1 = tradeday_list[tradeday_list.get_loc(tradeday_list.asof(end_date)) + 1]
        return end_date1
    else:
        return end_date


# %% 代码示例
'''
fendday('20220417',shift_length='',tradeday=True,tradeday_shift='after') # 向后找到最近一个交易日
fendday('20220417',shift_length='6m',tradeday=True,tradeday_shift='after') # 向后找到6个月前的最近一个交易日
fendday('20220417', shift_length='6m', tradeday=True, tradeday_shift='before') # 向后找到6个月前的最近一个交易日
'''


# %% 获取A股交易日序列
def gen_td_series(start_date="", end_date="", freq="D", tradeday_list=tradeday_list, opt_type='str'):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    if freq == "D":  # 生成日频截止日Index，直接从tradeday_list读取,仅保留A股交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        report_date = report_date[report_date.isin(tradeday_list.strftime('%Y%m%d'))]
    elif freq == "W-END" or freq == "WE":  # 取每周最后交易日，如果当周没有交易日，则为NaT
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='W')])[
            'Trade_day'].last()  # 取每周最后交易日
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
    elif freq == "W-START" or freq == "WS":  # 取每周第一交易日，如果当周没有交易日，则为NaT
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='W')])[
            'Trade_day'].first()  # 取每周最后交易日
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
    elif freq == "M-END" or freq == "ME":  # 取每月最后交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='M')])['Trade_day'].last()
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
    elif freq == "M-START" or freq == "MS":  # 取每月第一个交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='M')])['Trade_day'].first()
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
    elif freq == "Q-END" or freq == "QE":  # 取每季度最后交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='Q')])['Trade_day'].last()
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
    elif freq == "Q-START" or freq == "QS":  # 取每季度第一个交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='Q')])['Trade_day'].first()
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
    elif freq == "H-END" or freq == "HE":  # 取每半年最后交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='Q')])['Trade_day'].last()
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
        report_date = report_date[report_date.map(lambda x: x.endswith("6", 5, 6) or x.endswith("12", 4, 6))]
    elif freq == "H-START" or freq == "HS":  # 取每半年第一个交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='Q')])['Trade_day'].first()
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
        report_date = report_date[report_date.map(lambda x: x.endswith("1", 5, 6) or x.endswith("7", 5, 6))]
    elif freq == "Y-END" or freq == "YE":  # 取每年最后交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='Y')])['Trade_day'].last()
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
    elif freq == "Y-START" or freq == "YS":  # 取每年第一个交易日
        report_date = pd.date_range(start_date, end_date).strftime('%Y%m%d')
        tdf = pd.DataFrame(tradeday_list).groupby([pd.Grouper(key='Trade_day', freq='Y')])['Trade_day'].first()
        tdf.dropna(inplace=True)
        report_date = report_date[report_date.isin(pd.DatetimeIndex(tdf).strftime('%Y%m%d'))]
    else:
        print("频率参数指定错误！")
    if opt_type == 'DatetimeIndex':
        report_date = pd.DatetimeIndex(report_date)
    elif opt_type == 'str':
        pass
    return report_date


# %% 代码示例
# gen_td_series(start_date="20190101",end_date="20221231",freq="QE",tradeday_list=tradeday_list,opt_type='str')


# %% # 业绩指标复合函数make_index()
# 输入业绩基准指数代码，权重，起止日期，是否再平衡，再平衡周期，数据来源（默认WindAPI）
# 再平衡函数目前仅支持定期再平衡

def make_index(asset_code=[], asset_weight=[], asset_type=[], start_date="", end_date="", rebalance="",
               tradeday_list=tradeday_list, datamode="WindAPI", database_path=[path_stock, path_index, path_fund],
               **kwargs):
    # TODO 考虑加入DF数据源，考虑加入阈值触发条件
    if round(sum(asset_weight), 3) != 1.0:
        print("初始权重和不为1！")
        return
    asset_series = pd.DataFrame()  # 先提取出业绩基准组成序列

    if datamode == "WindAPI":
        if w.isconnected() == False:  # 判断WindPy是否已经登录成功
            w.start()
        for atype, acode, aweight in zip(asset_type, asset_code, asset_weight):
            if atype == 'Fund':
                sub_series = w.wsd(acode, "NAV_adj", start_date, end_date, usedf=True)[1]
                print(f'基金读取{acode},权重{aweight}')
            elif atype == 'Index':
                sub_series = w.wsd(acode, "Close", start_date, end_date, usedf=True)[1]
                print(f'指数读取{acode},权重{aweight}')
            else:
                print('资产类别代码有误！')
                return
            if sub_series.isnull().values.any() == True:
                print(f"{acode}净值缺失，请检查指数成立日是否晚于起始日！")
                return
            sub_series.columns = [acode]
            asset_series = pd.concat([asset_series, sub_series], axis=1)
            asset_series = qs.utils.rebase(asset_series, 1)
            asset_series.set_index(pd.DatetimeIndex(asset_series.index), inplace=True)
    elif datamode == "DB":
        # 分离出基金代码、指数代码和股票代码
        fund_list = pd.Series(asset_code)[pd.Series(asset_type) == "Fund"].tolist()
        index_list = pd.Series(asset_code)[pd.Series(asset_type) == "Index"].tolist()
        stock_list = pd.Series(asset_code)[pd.Series(asset_type) == "Stock"].tolist()

        fund_list = "" if fund_list == [] else fund_list
        index_list = "" if index_list == [] else index_list
        stock_list = "" if stock_list == [] else stock_list

        asset_series = fetch_asset_series(stock_code=stock_list, index_code=index_list, fund_code=fund_list,
                                          start_date=start_date, end_date=end_date, data_mode=datamode,
                                          database_path=database_path, tradeday_list=tradeday_list,
                                          censor_rebase=True, to_wide=True)  # 在提取asset_series时会自动剔除起始NA值
        if asset_series.isnull().values.any() == True:
            print("DB模式提取出的资产价格序列存在缺失值！")

    asset_series.dropna(inplace=True)

    # 共享部分
    # 再生成权重矩阵，根据再平衡参数调节
    if rebalance != "":
        rebal_date0 = asset_series.resample(rebalance).last().index
        a1 = pd.DataFrame(rebal_date0)
        a1.columns = ['date']
        a2 = pd.DataFrame(tradeday_list)
        a2.columns = ['trade_date']
        rebal_date = pd.merge_asof(a1, a2, left_on='date', right_on='trade_date',
                                   direction='backward').trade_date  # 向前找到最近的交易日
        rebal_date = pd.DatetimeIndex(rebal_date)  # 获取再平衡交易日
        # 组合构建首日和尾日也定义为再平衡交易日，同时通过取并集，避免日期重叠问题
        # 组合没有再平衡，首尾两日也是再平衡日，保证再平衡日序列有首尾，程序可正常运转
        rebal_date = asset_series.index[0:1].union(rebal_date).union(asset_series.index[-1:])
    elif rebalance == "":
        rebal_date = asset_series.index[0:1].union(asset_series.index[-1:])

    # 遍历 rebal_date,找到再平衡区间的起点和终点
    index_final = pd.DataFrame()
    index_slice_base = 1
    for i in range(len(rebal_date) - 1):
        asset_series_slice = qs.utils.rebase(asset_series.loc[rebal_date[i]:rebal_date[i + 1]], 1)  # 区间内资产净值片段切片并归一
        index_slice = (asset_series_slice * asset_weight).sum(1)
        index_slice = qs.utils.rebase(index_slice, index_slice_base)
        index_slice_base = index_slice.tail(1)[0]
        index_final = pd.concat([index_final, index_slice])

        index_final.drop_duplicates(inplace=True)  # 去重

    # 给Index命名
    index_name = str()
    for acode, aweight in zip(asset_code, asset_weight):
        sub_name = w.wsd(acode, "sec_name", end_date, end_date, "").Data[0][0]
        sub_part = str(aweight) + "*" + sub_name + "+"
        index_name = index_name + sub_part
    if rebalance != "":
        index_name = [index_name[:-1]][0] + f"(平衡周期{rebalance})"
    elif rebalance == "":
        index_name = [index_name[:-1]][0] + "(无再平衡)"

    index_final.columns = [index_name]
    index_all = dict()  # 返回字典，包含指数序列，调仓日期和底层原始资产净值
    index_all['index'] = index_final
    index_all['rebal_date'] = rebal_date
    index_all['asset_series'] = asset_series

    return index_all


# %% 代码示例
'''
a=make_index(asset_code = ['005827.OF', 'H11009.CSI'],asset_weight = [0.5, 0.5],asset_type = ['Fund', 'Index'],
           start_date = fstartday('20190101',tradeday_shift='before'),end_date = '20211231',rebalance='6m')
b=make_index(asset_code = ['005827.OF', 'H11009.CSI'],asset_weight = [0.5, 0.5],asset_type = ['Fund', 'Index'],
           start_date = fstartday('20190101',tradeday_shift='before'),end_date = '20211231',rebalance='')
c=make_index(asset_code = ['000300.SH', 'H11009.CSI','IXIC.GI'],asset_weight = [0.3, 0.5,0.2],asset_type = ['Index']*3,
           start_date = fstartday('20190101',tradeday_shift='before'),end_date = '20211231',rebalance='3m')
d=make_index(asset_code = ['000300.SH', 'H11009.CSI'],asset_weight = [0.5, 0.5],asset_type = ['Index']*2,
           start_date = fstartday('20190101',tradeday_shift='before'),end_date = '20211231',rebalance='3m')
pd.concat([a['index'],b['index'],c["index"],d["index"]],axis=1).plot()
# 绘制调仓点,Index日期筛选有问题，需转化为series再unique处理
plt.scatter(a['rebal_date'], a['index'].loc[a['rebal_date'],].iloc[:,0].unique(), c='r', s=15, marker="^",zorder=2)
plt.scatter(b['rebal_date'], b['index'].loc[b['rebal_date'],].iloc[:,0].unique(), c='r', s=15, marker="^",zorder=2)
plt.scatter(c['rebal_date'], c['index'].loc[c['rebal_date'],].iloc[:,0].unique(), c='r', s=15, marker="^",zorder=2)
plt.scatter(d['rebal_date'], d['index'].loc[d['rebal_date'],].iloc[:,0].unique(), c='r', s=15, marker="^",zorder=2)
plt.show()

e = make_index(asset_code=['161005.OF', 'H11009.CSI', '600519.SH'], asset_weight=[0.25, 0.5, 0.25],
               asset_type=['Fund', 'Index', 'Stock'], start_date=fstartday('20190101', tradeday_shift='before'),
               end_date='20211231', rebalance='6m', datamode="DB")
e['index'].plot()
plt.show()
f = make_index(asset_code=['600519.SH'], asset_weight=[1],
               asset_type=['Stock'], start_date=fstartday('20190101', tradeday_shift='before'),
               end_date='20211231', rebalance='', datamode="DB")
f['index'].plot()
plt.show()
'''

# %% 提取基金/指数净值函数
# 当data_mode=DF 的时候，dataframe接受的数据框格式是长数据格式！！
# type_list支持Fund和Index两种

def fetch_nav(asset_list, type_list="", start_date="", end_date="", data_mode='DF', dataframe="",
              database_path=[path_stock, path_index, path_fund],tradeday_list=tradeday_list,
              check_na=True, censor_rebase=True, to_long=False):
    # 现将日期转化为标准格式
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    if type_list == "":
        type_list = ['Fund'] * len(asset_list)  # 如果不指定资产类型，默认都是Fund

    asset_series = pd.DataFrame()
    if data_mode == 'WindAPI':
        if w.isconnected() == False:  # 判断WindPy是否已经登录成功
            w.start()
        for acode, atype in zip(asset_list, type_list):
            if atype == 'Fund':
                sub_series = w.wsd(acode, "NAV_adj", start_date, end_date, usedf=True)[1]
                # print(f'基金读取{acode}')
            elif atype == 'Index':
                sub_series = w.wsd(acode, "Close", start_date, end_date, usedf=True)[1]
                # print(f'指数读取{acode}')
            else:
                print('资产类别代码有误！')
                # return
            sub_series.columns = [acode]
            asset_series = pd.concat([asset_series, sub_series], axis=1)

    elif data_mode == "DF":  # 需要指数和基金的净值拼接成一个大的DF
        for acode in asset_list:
            sub_series0 = dataframe[dataframe.F_INFO_WINDCODE == acode]
            sub_series = sub_series0.copy()
            sub_series.set_index(sub_series.TRADE_DT, inplace=True)
            sub_series.drop(['F_INFO_WINDCODE', 'TRADE_DT'], axis=1, inplace=True)
            sub_series.fillna(method='ffill', inplace=True)  # 缺失值用前值填充
            sub_series.columns = [acode]
            asset_series = pd.concat([asset_series, sub_series], axis=1)

    elif data_mode == 'DB':
        # 分离出基金代码和指数代码,暂时不支持股票资产
        fund_list = pd.Series(asset_list)[pd.Series(type_list) == "Fund"].tolist()
        index_list = pd.Series(asset_list)[pd.Series(type_list) == "Index"].tolist()
        if fund_list == []:
            fund_series = None
        else:
            fund_series=fetch_asset_series(stock_code='',index_code='', fund_code=fund_list,
                                           start_date=start_date,end_date=end_date, data_mode=data_mode,
                                           database_path=database_path,tradeday_list=tradeday_list,to_wide=False)
            fund_series=fund_series[['S_INFO_WINDCODE','TRADE_DT','S_DQ_ADJCLOSE']]
            fund_series.columns=['F_INFO_WINDCODE','TRADE_DT','F_NAV_ADJUSTED']

        if index_list == []:
            index_series = None
        else:
            index_series=fetch_asset_series(stock_code='',index_code=index_list, fund_code='',
                                           start_date=start_date,end_date=end_date, data_mode=data_mode,
                                           database_path=database_path,tradeday_list=tradeday_list,to_wide=False)
            index_series=index_series[['S_INFO_WINDCODE','TRADE_DT','S_DQ_ADJCLOSE']]
            index_series.columns=['F_INFO_WINDCODE','TRADE_DT','F_NAV_ADJUSTED']

        asset_series0 = pd.concat([fund_series, index_series])
        asset_series0.drop_duplicates(inplace=True)  # 删除重复记录
        asset_series = asset_series0.pivot(index='TRADE_DT', columns='F_INFO_WINDCODE', values='F_NAV_ADJUSTED')  # 数据透视
        asset_series = asset_series[asset_list]  # 对列重新排序,暂时处理不好OF与SZ混用的问题
        # 做数据透视表时候列顺序会打乱，需要按照asset_list的顺序重排
        asset_series.fillna(method='ffill', inplace=True)  # 缺失值用前值填充

    # 共享代码
    asset_series.set_index(pd.DatetimeIndex(asset_series.index), inplace=True)  # 统一将净值列表的索引改为DatetimeIndex
    asset_series = asset_series[asset_series.index.isin(tradeday_list)]  # 如果为DT数据源，可能有非交易日记录，筛选仅保留交易日记录
    asset_series = asset_series[start_date:end_date]  # 在开始结束日期内选择净值(为了下一步区间净值检查）

    if check_na == True:
        _na_test = asset_series.isnull().any(axis=0)  # 批量检查回测区间内是否有资产净值缺失
        if any(_na_test) == True:
            _na_list = _na_test[_na_test > 0].index.tolist()
            print(f"{_na_list}净值缺失，请检查基金成立日是否晚于指标计算起始日,或者资产类型列表是否正确！")
            return
    # new_col = list(map(lambda x: x.replace(".SH", '.OF').replace(".SZ", '.OF'), asset_series.columns.tolist()))  # 对于数据库中以.SH .SZ结尾的基金，将列名称改回.OF
    # asset_series.columns = new_col
    if censor_rebase == True:
        asset_series = qs.utils.rebase(asset_series, 1)  # 统一取最晚成立的基金成立日为首日，并将全部净值调整成初值为1，

    if to_long == True:
        asset_series['TRADE_DT'] = asset_series.index
        asset_series = pd.melt(asset_series, id_vars=['TRADE_DT'], var_name='F_INFO_WINDCODE',
                               value_name='F_NAV_ADJUSTED')
    return asset_series


# %% 代码示例
'''
# WindAPI取数模式
asset_nav = fetch_nav(asset_list=['360001.OF', '519714.OF', '000300.OF'], type_list="",
                      start_date="20190101", end_date="20211231", data_mode='WindAPI', database_path="", dataframe="",
                      tradeday_list=tradeday_list)
asset_nav.pct_change().corr()  # 计算相关性矩阵
sns.heatmap(asset_nav.pct_change().corr(), annot=True, vmax=1, square=True, cmap='Blues')
plt.show()
# DF取数模式
# 提前把需要用到的净值数据批量导出
record_path = "Import Adj History_普通股票.xlsx"
adj_table = pd.read_excel(record_path)
fund_list = adj_table['FundID'].unique().tolist()
fund_list_str = str(fund_list)[1:-1].replace(".OF", "").replace(".SH", "").replace(".SZ", "")
query = f"select F_INFO_WINDCODE, TRADE_DT,F_NAV_ADJUSTED from '中国共同基金净值' " \
        f"where substr(F_INFO_WINDCODE, 0, 7) in ({fund_list_str}) " \
        f"and F_INFO_WINDCODE not like '%!%' " \
        f"order by TRADE_DT"
fund_nav_table = Obtain_DBData(query, path_fund)
fund_nav_table.drop_duplicates(inplace=True)  # 删除重复记录，是长数据格式
asset_nav = fetch_nav(asset_list=['360001.OF', '519714.OF', '001054.OF'], type_list="",
                      start_date="20190101", end_date="20211231", data_mode='DF',
                      dataframe=fund_nav_table, tradeday_list=tradeday_list)
asset_nav = fetch_nav(asset_list=['360001.OF', '519714.OF', '001054.OF'], type_list="",
                      start_date="20190101", end_date="20211231", data_mode='DF',
                      dataframe=fund_nav_table, tradeday_list=tradeday_list,to_long=True)

# DB取数模式
asset_nav = fetch_nav(asset_list=['360001.OF', '519714.OF', '001054.OF'], type_list="",
                      start_date="20190101", end_date="20211231", data_mode='DB',
                      tradeday_list=tradeday_list)
asset_nav = fetch_nav(asset_list=['005911.OF', '519714.OF', '000300.SH'], type_list=['Fund']*2+['Index'],
                      start_date="20050101", end_date="20211231", data_mode='DB',
                      tradeday_list=tradeday_list,check_na=False,censor_rebase=True)
'''


# %% 获取资产价格序列函数 是fetch_nav的拓展版（目前只有Database和WindAPI两种取数模式）
# Note: 由于是从数据库里直接取数（Wind API = Alldays），因此可能包含非交易日数据（如季报日），此外注意AH交易日不同步问题
# 当to_wide=True时，由于交易日不匹配导致的空值会用前一交易日收盘价替代

def fetch_asset_series(stock_code="", index_code="", fund_code="", start_date="", end_date="", data_mode='DB',
                       database_path=[path_stock, path_index, path_fund], keep_td=True, tradeday_list=tradeday_list,
                       to_wide=False, show_wide="close", censor_rebase=False):
    """
    :param show_wide: close/pct_chg
    """
    start_date = pd.to_datetime(start_date).strftime('%Y%m%d')
    end_date = pd.to_datetime(end_date).strftime('%Y%m%d')

    if data_mode == 'WindAPI':
        if w.isconnected() == False:  # 判断WindPy是否已经登录成功
            w.start()
        """
          获取股票和指数数据
        """
        # Stock和Index合并提取，统称为asset
        if stock_code != "" and index_code != "":
            stk_idx_code = stock_code + index_code
        elif stock_code == "":
            stk_idx_code = index_code
        elif index_code == "":
            stk_idx_code = stock_code

        if stk_idx_code != "":
            stk_idx_code_str = str(list(stk_idx_code)).replace("'", "").replace(' ', '')[1:-1]
            # 因为A股，港股和美股交易时间不同，Wind提取的是日历日数据
            close_df = w.wsd(stk_idx_code_str, "close", start_date, end_date, "Days=Alldays;PriceAdj=B", usedf=True)[1]
            close_df['TRADE_DT'] = close_df.index
            chg_df = w.wsd(stk_idx_code_str, "pct_chg", start_date, end_date, "Days=Alldays;PriceAdj=B", usedf=True)[1]
            chg_df['TRADE_DT'] = chg_df.index
            close_df_long = pd.melt(close_df, id_vars=['TRADE_DT'], var_name='S_INFO_WINDCODE',
                                    value_name='S_DQ_ADJCLOSE')
            chg_df_long = pd.melt(chg_df, id_vars=['TRADE_DT'], var_name='S_INFO_WINDCODE', value_name='S_DQ_PCTCHANGE')
            stk_idx_series = pd.merge(close_df_long, chg_df_long, how='inner', on=["TRADE_DT", 'S_INFO_WINDCODE'])
            stk_idx_series['S_DQ_PCTCHANGE'] = stk_idx_series['S_DQ_PCTCHANGE'] / 100
            stk_idx_series.dropna(subset=['S_DQ_ADJCLOSE', 'S_DQ_PCTCHANGE'], how='any', inplace=True)
        elif stk_idx_code == "":
            stk_idx_series = None
        """
          获取基金数据
        """
        if fund_code != "":
            fund_code_str = str(list(fund_code)).replace("'", "").replace(' ', '')[1:-1]
            nav_adj_df = w.wsd(fund_code_str, "NAV_adj", start_date, end_date, "Days=Alldays", usedf=True)[1]
            nav_adj_df['TRADE_DT'] = nav_adj_df.index
            nav_adj_df.columns = fund_code + ['TRADE_DT']
            adj_return_df = w.wsd(fund_code_str, "NAV_adj_return1", start_date, end_date, "Days=Alldays", usedf=True)[1]
            adj_return_df['TRADE_DT'] = adj_return_df.index
            adj_return_df.columns = fund_code + ['TRADE_DT']
            # 只有一只基金的时候列名会有变化，要单独处理
            nav_adj_df_long = pd.melt(nav_adj_df, id_vars=['TRADE_DT'], var_name='S_INFO_WINDCODE',
                                      value_name='S_DQ_ADJCLOSE')
            adj_return_df_long = pd.melt(adj_return_df, id_vars=['TRADE_DT'], var_name='S_INFO_WINDCODE',
                                         value_name='S_DQ_PCTCHANGE')
            fund_series = pd.merge(nav_adj_df_long, adj_return_df_long, how='inner', on=["TRADE_DT", 'S_INFO_WINDCODE'])
            fund_series['S_DQ_PCTCHANGE'] = fund_series['S_DQ_PCTCHANGE'] / 100
            fund_series.dropna(subset=['S_DQ_ADJCLOSE', 'S_DQ_PCTCHANGE'], how='any', inplace=True)
        elif fund_code == "":
            fund_series = None
        asset_series = pd.concat([stk_idx_series, fund_series])

        asset_series = asset_series.loc[:, ["S_INFO_WINDCODE", 'TRADE_DT', 'S_DQ_ADJCLOSE', 'S_DQ_PCTCHANGE']]

    if data_mode == 'DB':
        """
        获取股票数据
        """
        if stock_code != "":
            # 先查询A股
            stock_code = [code.upper() for code in stock_code]
            stock_list_str = str(stock_code)[1:-1]
            query = f"select S_INFO_WINDCODE, TRADE_DT,S_DQ_ADJCLOSE,S_DQ_PCTCHANGE from '中国A股日行情' " \
                    f"where upper(S_INFO_WINDCODE) in ({stock_list_str})  and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"order by S_INFO_WINDCODE, TRADE_DT"
            stock_series_A = Obtain_DBData(query, database_path[0])
            stock_series_A['S_DQ_PCTCHANGE'] = stock_series_A['S_DQ_PCTCHANGE'] / 100
            # 再查询港股
            # 港股日行情收益率表有pct_change字段，要leftjoin匹配，不用在python中自己算，但是查询会很慢
            stock_code_left = set(stock_code).difference(set(stock_series_A["S_INFO_WINDCODE"]))
            stock_list_left_str = str(list(stock_code_left))[1:-1]
            query = f"select a.S_INFO_WINDCODE, a.TRADE_DT,a.S_DQ_ADJCLOSE,b.PCT_CHANGE_D as S_DQ_PCTCHANGE " \
                    f"from '香港股票日行情' as a " \
                    f"left join '香港股票日行情收益率' as b " \
                    f"on a.S_INFO_WINDCODE=b.S_INFO_WINDCODE and a.TRADE_DT=b.TRADE_DT " \
                    f"where upper(a.S_INFO_WINDCODE) in ({stock_list_left_str}) " \
                    f"and a.TRADE_DT >= {start_date} and a.TRADE_DT <= {end_date} " \
                    f"order by a.S_INFO_WINDCODE, a.TRADE_DT"

            stock_series_H = Obtain_DBData(query, database_path[0])
            stock_series_H['S_DQ_PCTCHANGE'] = stock_series_H['S_DQ_PCTCHANGE'] / 100

            # 判定是否还有未匹配资产
            stock_code_left2 = set(stock_code).difference(
                set(stock_series_H["S_INFO_WINDCODE"]).union(set(stock_series_A["S_INFO_WINDCODE"])))
            if stock_code_left2 == set():
                print('股票数据查询完毕')
            else:
                print(f"{stock_code_left2}没有查询到股票价格数据！")

            stock_series = pd.concat([stock_series_A, stock_series_H])
            # stock_series["ASSET_TYPE"] = "Stock"
        elif stock_code == "":
            stock_series = None
        """
        获取指数数据
        """
        if index_code != "":
            # 先查询债券指数
            index_code = [code.upper() for code in index_code]
            index_list_str = str(index_code)[1:-1]

            query = f"select upper(S_INFO_WINDCODE), TRADE_DT,S_DQ_CLOSE,S_DQ_PCTCHANGE from '中国债券指数日行情' " \
                    f"where upper(S_INFO_WINDCODE) in ({index_list_str})  and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"order by S_INFO_WINDCODE, TRADE_DT"
            index_series_B = Obtain_DBData(query, database_path[1])
            index_series_B['S_DQ_PCTCHANGE'] = index_series_B['S_DQ_PCTCHANGE'] / 100
            index_series_B.rename(columns={'upper(S_INFO_WINDCODE)': 'S_INFO_WINDCODE', "S_DQ_CLOSE": "S_DQ_ADJCLOSE"},
                                  inplace=True)

            # 再查询A股指数（因为A股指数日行情数据库有部分债券指数数据，但已经停更，因此先查询债券数据）
            index_code_left1 = set(index_code).difference(set(index_series_B["S_INFO_WINDCODE"]))
            index_list_left_str1 = str(list(index_code_left1))[1:-1]

            query = f"select upper(S_INFO_WINDCODE), TRADE_DT,S_DQ_CLOSE,S_DQ_PCTCHANGE from '中国A股指数日行情' " \
                    f"where upper(S_INFO_WINDCODE) in ({index_list_left_str1})  and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"order by S_INFO_WINDCODE, TRADE_DT"
            index_series_A = Obtain_DBData(query, database_path[1])
            index_series_A['S_DQ_PCTCHANGE'] = index_series_A['S_DQ_PCTCHANGE'] / 100
            index_series_A.rename(columns={'upper(S_INFO_WINDCODE)': 'S_INFO_WINDCODE', "S_DQ_CLOSE": "S_DQ_ADJCLOSE"},
                                  inplace=True)

            # 再查询Wind
            index_code_left2 = set(index_code_left1).difference(set(index_series_A["S_INFO_WINDCODE"]))
            index_list_left_str2 = str(list(index_code_left2))[1:-1]

            query = f"select upper(S_INFO_WINDCODE), TRADE_DT,S_DQ_CLOSE,S_DQ_PCTCHANGE from '中国A股Wind行业指数日行情' " \
                    f"where upper(S_INFO_WINDCODE) in ({index_list_left_str2})  and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"order by S_INFO_WINDCODE, TRADE_DT"
            index_series_Wind = Obtain_DBData(query, database_path[1])
            index_series_Wind['S_DQ_PCTCHANGE'] = index_series_Wind['S_DQ_PCTCHANGE'] / 100
            index_series_Wind.rename(
                columns={'upper(S_INFO_WINDCODE)': 'S_INFO_WINDCODE', "S_DQ_CLOSE": "S_DQ_ADJCLOSE"},
                inplace=True)

            # 再查询申万（申万库缺少S_DQ_PCTCHANGE，要自己算）
            index_code_left3 = set(index_code_left2).difference(set(index_series_Wind["S_INFO_WINDCODE"]))
            index_list_left_str3 = str(list(index_code_left3))[1:-1]

            query = f"select upper(S_INFO_WINDCODE), TRADE_DT,S_DQ_CLOSE from '申万指数日行情' " \
                    f"where upper(S_INFO_WINDCODE) in ({index_list_left_str3})  and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"order by S_INFO_WINDCODE, TRADE_DT"

            index_series_SW = Obtain_DBData(query, database_path[1])
            index_series_SW.rename(columns={'upper(S_INFO_WINDCODE)': 'S_INFO_WINDCODE', "S_DQ_CLOSE": "S_DQ_ADJCLOSE"},
                                   inplace=True)
            index_series_SW['S_DQ_PCTCHANGE'] = index_series_SW.groupby('S_INFO_WINDCODE').S_DQ_ADJCLOSE.pct_change()

            # 再查询中信
            index_code_left4 = set(index_code_left3).difference(set(index_series_SW["S_INFO_WINDCODE"]))
            index_list_left_str4 = str(list(index_code_left4))[1:-1]

            query = f"select upper(S_INFO_WINDCODE), TRADE_DT,S_DQ_CLOSE,S_DQ_PCTCHANGE from '中信指数日行情' " \
                    f"where upper(S_INFO_WINDCODE) in ({index_list_left_str4})  and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"order by S_INFO_WINDCODE, TRADE_DT"
            index_series_CI = Obtain_DBData(query, database_path[1])
            index_series_CI['S_DQ_PCTCHANGE'] = index_series_CI['S_DQ_PCTCHANGE'] / 100
            index_series_CI.rename(columns={'upper(S_INFO_WINDCODE)': 'S_INFO_WINDCODE', "S_DQ_CLOSE": "S_DQ_ADJCLOSE"},
                                   inplace=True)

            # 再查询基金指数（也没有pct_change字段，要自己算）
            index_code_left5 = set(index_code_left4).difference(set(index_series_CI["S_INFO_WINDCODE"]))
            index_list_left_str5 = str(list(index_code_left5))[1:-1]

            query = f"select upper(S_INFO_WINDCODE), TRADE_DT,S_DQ_CLOSE from '中国共同基金指数行情' " \
                    f"where upper(S_INFO_WINDCODE) in ({index_list_left_str5})  and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"order by S_INFO_WINDCODE, TRADE_DT"

            index_series_F = Obtain_DBData(query, database_path[1])
            index_series_F.rename(columns={'upper(S_INFO_WINDCODE)': 'S_INFO_WINDCODE', "S_DQ_CLOSE": "S_DQ_ADJCLOSE"},
                                  inplace=True)
            index_series_F['S_DQ_PCTCHANGE'] = index_series_F.groupby('S_INFO_WINDCODE').S_DQ_ADJCLOSE.pct_change()

            # 再查询港股指数
            index_code_left6 = set(index_code_left5).difference(set(index_series_F["S_INFO_WINDCODE"]))
            index_list_left_str6 = str(list(index_code_left6))[1:-1]

            query = f"select upper(S_INFO_WINDCODE), TRADE_DT,S_DQ_CLOSE,S_DQ_PCTCHANGE from '香港股票指数日行情' " \
                    f"where upper(S_INFO_WINDCODE) in ({index_list_left_str6})  and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"order by S_INFO_WINDCODE, TRADE_DT"
            index_series_H = Obtain_DBData(query, database_path[1])
            index_series_H['S_DQ_PCTCHANGE'] = index_series_H['S_DQ_PCTCHANGE'] / 100
            index_series_H.rename(columns={'upper(S_INFO_WINDCODE)': 'S_INFO_WINDCODE', "S_DQ_CLOSE": "S_DQ_ADJCLOSE"},
                                  inplace=True)

            # 判定是否还有未匹配资产
            index_code_left7 = set(index_code_left6).difference(set(index_series_H["S_INFO_WINDCODE"]))

            if index_code_left7 == set():
                print('指数数据查询完毕')
            else:
                print(f"{index_code_left7}没有查询到指数价格数据！")

            index_series = pd.concat(
                [index_series_A, index_series_H, index_series_Wind, index_series_SW, index_series_CI, index_series_B,
                 index_series_F])
            # index_series["ASSET_TYPE"] = "Index"
        elif index_code == "":
            index_series = None

        """
        获取基金数据(输入的可能是场外代码，输出的可能有场内代码)
        """
        if fund_code != "":
            fund_code = [code.upper() for code in fund_code]
            fund_list_str = str(fund_code)[1:-1].replace(".OF", "").replace(".SH", "").replace(".SZ", "")
            query = f"select F_INFO_WINDCODE, TRADE_DT,F_NAV_ADJUSTED from '中国共同基金净值' " \
                    f"where substr(F_INFO_WINDCODE, 0, 7) in ({fund_list_str}) and TRADE_DT >= {start_date} and TRADE_DT <= {end_date} " \
                    f"and F_INFO_WINDCODE not like '%!%' " \
                    f"order by F_INFO_WINDCODE, TRADE_DT"
            fund_series = Obtain_DBData(query, database_path[2])
            fund_series.rename(columns={'F_INFO_WINDCODE': 'S_INFO_WINDCODE', "F_NAV_ADJUSTED": "S_DQ_ADJCLOSE"},
                               inplace=True)
            fund_series['S_DQ_PCTCHANGE'] = fund_series.groupby('S_INFO_WINDCODE').S_DQ_ADJCLOSE.pct_change()
            # fund_series["ASSET_TYPE"] = "Fund"

            # 判定是否还有未匹配资产
            fund_code_left = set([code.replace(".OF", "").replace(".SH", "").replace(".SZ", "") for code in fund_code]). \
                difference(set(
                [code.replace(".OF", "").replace(".SH", "").replace(".SZ", "") for code in
                 fund_series["S_INFO_WINDCODE"]]))

            if fund_code_left == set():
                print('基金数据查询完毕')
            else:
                print(f"{fund_code_left}没有查询到基金价格数据！")
        elif fund_code == "":
            fund_series = None

        asset_series = pd.concat([stock_series, index_series, fund_series])
        asset_series.reset_index(drop=True, inplace=True)
        # # 日期格式统一转化成Datetime
        # asset_series.TRADE_DT = pd.DatetimeIndex(asset_series.TRADE_DT)
        # 最后一步，asset_series要剔除重复记录，特别是通过DB模式提取的数据
        asset_series.drop_duplicates(inplace=True)

    # 日期格式统一转化成Datetime
    asset_series.TRADE_DT = pd.DatetimeIndex(asset_series.TRADE_DT)
    # 是否只保留tradeday记录
    if keep_td == True:
        asset_series = asset_series[asset_series['TRADE_DT'].apply(lambda x: x in tradeday_list)]

    if to_wide == True:
        if show_wide == 'close':
            asset_series = asset_series.pivot(index='TRADE_DT', columns='S_INFO_WINDCODE',
                                              values='S_DQ_ADJCLOSE').fillna(
                method='ffill')  # 向下填充空值，若下一交易日没有行情，则沿用上一日行情
            if censor_rebase == True:
                asset_series = qs.utils.rebase(asset_series, 1)  # 统一取最晚成立的基金成立日为首日，并将全部净值调整成初值为1，
        elif show_wide == 'pct_chg':
            asset_series = asset_series.pivot(index='TRADE_DT', columns='S_INFO_WINDCODE',
                                              values='S_DQ_PCTCHANGE')  # pct_chg不能做填充操作
        # asset_series列按照股票、指数、基金的列顺序进行排序
        if data_mode == "WindAPI":
            stk_idx_code_i = stk_idx_series[
                'S_INFO_WINDCODE'].drop_duplicates().tolist() if stk_idx_series is not None else ['']
            fund_code_i = fund_series['S_INFO_WINDCODE'].drop_duplicates().tolist() if fund_series is not None else ['']
            asset_code_list = stk_idx_code_i + fund_code_i

        elif data_mode == "DB":
            stock_code_i = stock_series['S_INFO_WINDCODE'].drop_duplicates().tolist() if stock_series is not None else [
                '']
            index_code_i = index_series['S_INFO_WINDCODE'].drop_duplicates().tolist() if index_series is not None else [
                '']
            fund_code_i = fund_series['S_INFO_WINDCODE'].drop_duplicates().tolist() if fund_series is not None else ['']

            asset_code_list = stock_code_i + index_code_i + fund_code_i

            while '' in asset_code_list:
                asset_code_list.remove('')

        columns_cat = pd.Series(asset_series.columns.astype('category'))  # 将返回的指数按照股票、指数和基金的顺序返回
        columns_cat.cat.set_categories(asset_code_list, inplace=True)
        columns_cat.sort_values(inplace=True)
        asset_series = asset_series[columns_cat]

    return asset_series


# %% 代码示例

# asset_df1 = fetch_asset_series(stock_code=["600519.SH", "000009.SZ", "3690.HK", "0001.HK", "830799.BJ"],
#                                index_code=["000300.SH", "CBA00101.CS", "h01001.CSI", '882105.WI', '801085.SI',
#                                            "CI005322.WI", "885007.WI", "HSI.HI"], fund_code=['161005.OF', '110022.OF'],
#                                start_date="20170101", end_date="20220320", data_mode='DB',
#                                database_path=[path_stock, path_index, path_fund], tradeday_list=tradeday_list,
#                                censor_rebase=True, to_wide=True, show_wide='pct_chg')


# (asset_df1["3690.HK"]+1).cumprod()
# xx=pd.Series([np.nan,1.1,1.2,np.nan,1.3,np.nan])
# xx.cumprod().fillna(method='ffill')
# asset_df1 = fetch_asset_series(stock_code=["600519.SH", "000009.SZ", "3690.HK", "0001.HK", "830799.BJ"],
#                                index_code=["000300.SH", "CBA00101.CS", "h01001.CSI", '882105.WI', '801085.SI',
#                                            "CI005322.WI", "885007.WI", "HSI.HI"], fund_code=['161005.OF'],
#                                start_date="20170101", end_date="20220320", data_mode='DB',
#                                database_path=[path_stock, path_index, path_fund],tradeday_list=tradeday_list,
#                                check_na=True, censor_rebase=True, to_wide=True)
# qs.utils.rebase(asset_df1, base=1).plot()
# plt.show()

# # 通过WindAPI查询 - 速度快、耗流量
# asset_df2 = fetch_asset_series(stock_code=["600519.SH", "000009.SZ", "3690.HK", "0001.HK", "830799.BJ"],
#                                index_code=["000300.SH", "CBA00101.CS", "h01001.CSI", '882105.WI', '801085.SI',
#                                            "CI005322.WI", "885007.WI", "HSI.HI"], fund_code=["014671.OF", '161005.OF'],
#                                start_date="20170101",
#                                end_date="20220320", data_mode='WindAPI', tradeday_list=tradeday_list,
#                                check_na=True, censor_rebase=True, to_wide=True)
#
# qs.utils.rebase(asset_df2,base=1).plot()
# plt.show()
#  # 基金数据，记录数有差异。差异在于基金成立日那天的净值数据库计入，API没计入
# asset_df3 = fetch_asset_series(stock_code='',
#                                index_code="", fund_code=["014671.OF", '161005.OF'],
#                                start_date="20170101",
#                                end_date="20220320", data_mode='DB',
#                                database_path=[path_stock, path_index, path_fund], dataframe="",
#                                tradeday_list=tradeday_list,
#                                check_na=True, censor_rebase=True, to_wide=False)
#
# asset_df4 = fetch_asset_series(stock_code="",
#                                index_code="", fund_code=["014671.OF", '161005.OF'],
#                                start_date="20170101",
#                                end_date="20220320", data_mode='WindAPI', tradeday_list=tradeday_list,
#                                check_na=True, censor_rebase=True, to_wide=False)
# writer=pd.ExcelWriter("asset_df.xlsx")
# asset_df3.to_excel(writer,sheet_name='df3')
# asset_df4.to_excel(writer,sheet_name='df4')
# writer.save()
# writer.close()
#
# asset_df5 = fetch_asset_series(stock_code="",
#                                index_code="", fund_code=["014671.OF", '161005.OF'],
#                                start_date="20170101",
#                                end_date="20220320", data_mode='WindAPI', tradeday_list=tradeday_list,
#                                check_na=True, censor_rebase=True, to_wide=True)

# # 股票数据，记录数一致。OK
# asset_df6 = fetch_asset_series(stock_code=["600519.SH", "000009.SZ", "3690.HK", "0001.HK"],
#                                index_code="", fund_code="",
#                                start_date="20170101",
#                                end_date="20220320", data_mode='DB',
#                                database_path=[path_stock, path_index, path_fund],
#                                tradeday_list=tradeday_list,
#                                censor_rebase=False, to_wide=False)
#
# asset_df7 = fetch_asset_series(stock_code=["600519.SH", "000009.SZ", "3690.HK", "0001.HK"],
#                                index_code="", fund_code="",
#                                start_date="20170101",
#                                end_date="20220320", data_mode='WindAPI', tradeday_list=tradeday_list,
#                                censor_rebase=False, to_wide=False)

# 指数数据，记录数一致，OK
# asset_df6 = fetch_asset_series(stock_code="",
#                                index_code=["000300.SH", "CBA00101.CS", "h01001.CSI", '882105.WI', '801085.SI',
#                                            "CI005322.WI", "885007.WI", "HSI.HI"], fund_code="",
#                                start_date="20170101",
#                                end_date="20220320", data_mode='DB',
#                                database_path=[path_stock, path_index, path_fund],
#                                tradeday_list=tradeday_list,
#                                censor_rebase=True, to_wide=False)
#
# asset_df7 = fetch_asset_series(stock_code="",
#                                index_code=["000300.SH", "CBA00101.CS", "h01001.CSI", '882105.WI', '801085.SI',
#                                            "CI005322.WI", "885007.WI", "HSI.HI"], fund_code="",
#                                start_date="20170101",
#                                end_date="20220320", data_mode='WindAPI', tradeday_list=tradeday_list,
#                                censor_rebase=True, to_wide=False)

# writer = pd.ExcelWriter("asset_df.xlsx")
# asset_df6.to_excel(writer, sheet_name='df6')
# asset_df7.to_excel(writer, sheet_name='df7')
# writer.save()
# writer.close()


# %% 单期调仓FOF组合函数
# 调仓日start_date当天无收益，次日开始计算收益，end_date当天有收益
# 共有DF、DB和WindAPI三种取数方式，推荐用DF方式，把全部净值提前取好再跑一次回测
# TODO 增加基金的交易费用、包括申购费用和赎回费用
def fof_run(fund_list, type_list="", ini_weight_list="", ini_fund="", start_nav="", start_date="", end_date="",
            tradeday_list=tradeday_list, data_mode="WindAPI", database_path=[path_stock, path_index, path_fund],
            dataframe=""):
    # 初始化输出容器
    fof = dict()
    # 初始参数数据类型转化
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    if round(sum(ini_weight_list), 3) != 1.0:
        print(f"调仓日{start_date}初始权重和不为1！")
        return

    if start_date not in list(tradeday_list):
        print(f"调仓日{start_date}起始日期不是交易日！")
        return
    # 提取净值，fetch_nav目前支持Fund和Index两类资产，暂时不支持股票，不过股票资产也不迫切
    fund_nav_table = fetch_nav(asset_list=fund_list, type_list=type_list, start_date=start_date, end_date=end_date,
                               data_mode=data_mode, database_path=database_path, dataframe=dataframe,
                               tradeday_list=tradeday_list)

    ini_fund_list = pd.Series(ini_weight_list,
                              index=fund_list) * ini_fund  # ini_fund_list里面的fund指的是初始本金，不是基金的意思，索引是基金代码

    fund_daily_return = fund_nav_table.pct_change()  # 基金日度涨幅
    fund_cum_return = em.cum_returns(fund_daily_return)
    fund_cum_returnvalue = fund_cum_return * ini_fund_list
    fund_cum_returnvalue['Total'] = fund_cum_returnvalue.apply(lambda x: x.sum(), axis=1)
    fof_cum_return = fund_cum_returnvalue.Total / ini_fund  # 返回FOF的区间内累计回报
    fof_nav = (1 + fof_cum_return) * start_nav  # 返回FOF的累计净值序列

    fof['nav'] = fof_nav
    fof['first_nav'] = fof_nav[0]
    fof['last_nav'] = fof_nav[-1]
    fof["first_day"] = fof_nav.index[0].strftime("%Y-%m-%d")
    fof["last_day"] = fof_nav.index[-1].strftime("%Y-%m-%d")
    fof['first_cash'] = ini_fund
    fof['last_cash'] = ini_fund * fof_nav[-1] / fof_nav[0]
    fof['sub_fund_return'] = fund_cum_return.tail(1).T
    fof['sub_fund_return'].columns = ['Return']
    return fof


# %% 代码示例
'''
fof1 = fof_run(fund_list=["510500.OF", "161005.OF", "000300.SH"], type_list=['Fund', 'Fund', 'Index'],
               ini_weight_list=[0.5, 0.3, 0.2],ini_fund=10000,start_nav=1.0,start_date="20190102", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list)

fof2 = fof_run(fund_list=["000991.OF", "005233.OF", "006567.OF"],ini_weight_list=[0.3, 0.4, 0.3],
               ini_fund=10000,start_nav=1.0,start_date="20190102",end_date="20211231",
               data_mode="DB",tradeday_list=tradeday_list,database_path=path_fund)
fof1['nav'].plot()
fof2['nav'].plot()
plt.legend(['fof1', 'fof2'])
plt.show()
fof3 = fof_run(fund_list=["003327.OF", "004200.OF", "519782.OF", "003949.OF", '270048.OF', '000084.OF'],
               ini_weight_list=[0.16, 0.16, 0.16, 0.16, 0.16, 0.2],
               ini_fund=10000, start_nav=1.0, start_date="20171229", end_date="20220516",
               data_mode="WindAPI", tradeday_list=tradeday_list, database_path=path_fund)
fof3['nav'].plot()
plt.show()

'''


# %% 多期调仓FOF组合函数
# 要素：调仓表，回测截止日
def batch_fof_run(adj_table, end_date, ini_fund=10000, start_nav=1.0, tradeday_list=tradeday_list, data_mode="",
                  database_path=[path_stock, path_index, path_fund], dataframe="", bm_code="", bm_weight="", bm_type="",
                  excess_or_relative="excess",plot=True, tqdm_disable=False, **kwargs):
    adj_table0 = adj_table.copy()  # 复制一份，避免影响原数据
    adj_table0['Adj_Date'] = pd.to_datetime(adj_table0['Adj_Date'], format='%Y%m%d')
    # adj_table0.set_index("Adj_Date", inplace=True)
    adj_table0.set_index(pd.DatetimeIndex(adj_table0['Adj_Date']), inplace=True)
    # 生成调仓终止日期列，最后一个调仓日终止日期==end_date
    start_date_list = adj_table0.index.unique()
    adj_n = len(start_date_list)
    start_date_position = pd.Series([tradeday_list.get_loc(start_date_list[i]) for i in range(adj_n)])
    end_date_position = start_date_position - 1
    end_date_list0 = tradeday_list[end_date_position.to_list()[1:]]  # 通过向前错一位，返回调仓区间终点，同时删掉第一个值
    end_date_list = end_date_list0.append(
        pd.DatetimeIndex([pd.to_datetime(end_date)]))  # 把调仓终止日Append到最后一个位置，生成完整的调仓终点日列表

    fof_record = dict()
    fof_nav = pd.DataFrame()
    for i in tqdm(range(adj_n), disable=tqdm_disable):
        fund_list = adj_table0.loc[
            start_date_list[i], ["FundID"]].values.flatten().tolist()  # 如果提取出来的只有一个元素，是无法to_list的
        type_list = adj_table0.loc[start_date_list[i], ["Type"]].values.flatten().tolist()
        ini_weight_list = adj_table0.loc[start_date_list[i], ["Weight"]].values.flatten().tolist()
        fof = fof_run(fund_list=fund_list, type_list=type_list, ini_weight_list=ini_weight_list, ini_fund=ini_fund,
                      start_nav=start_nav, start_date=start_date_list[i], end_date=end_date_list[i],
                      tradeday_list=tradeday_list, data_mode=data_mode, database_path=database_path,
                      dataframe=dataframe)
        start_nav = fof['last_nav']
        ini_fund = fof['last_cash']
        # fof_record[f'fof_{i}'] = fof #暂不输出明细
        fof_nav = pd.concat([fof_nav, fof['nav']])

    fof_nav.columns = ['FOF']  # 列重命名

    if bm_code != "":
        bm_nav = \
            make_index(asset_code=bm_code, asset_weight=bm_weight, asset_type=bm_type, start_date=start_date_list[0],
                       end_date=end_date, rebalance=kwargs['rebanlance'])['index']
    else:
        bm_nav = pd.DataFrame([1] * len(fof_nav))
        bm_nav.index = fof_nav.index

    combined = pd.concat([fof_nav - 1, bm_nav - 1], axis=1)  # 列1：FOF净值 列2：基准净值

    if excess_or_relative == 'excess':
        combined['超额'] = combined.iloc[:, 0] - combined.iloc[:, 1]
    elif excess_or_relative == 'relative':
        combined['相对强弱'] = (1 + combined.iloc[:, 0]) / (1 + combined.iloc[:, 1])
    else:
        print("超额计算方式指定有误！")
        return

    if plot == True and bm_code != "":
        if excess_or_relative == 'excess':
            combined.iloc[:, 0:2].plot(zorder=1)  # 绘制净值曲线
            plt.fill_between(combined.iloc[:, -1].index, combined.iloc[:, -1], color="skyblue", alpha=0.5)  # 绘制相对强弱/超额
            plt.legend(['FOF组合', bm_nav.columns[0], '超额'], loc='best')  # 显示图例
            plt.scatter(start_date_list, fof_nav[fof_nav.index.isin(start_date_list)] - 1, c='r', s=10, marker="^",
                        zorder=2)  # 绘制调仓点
        elif excess_or_relative == 'relative':
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax1.plot(combined.index, combined.iloc[:, 0], label='FOF组合')
            ax1.plot(combined.index, combined.iloc[:, 1], label=combined.iloc[:, 1].name)
            plt.scatter(start_date_list, fof_nav[fof_nav.index.isin(start_date_list)] - 1, c='r', s=10, marker="^",
                        zorder=2)  # 绘制调仓点
            ax2 = ax1.twinx()
            ax2.grid(False)
            ax2.fill_between(combined.iloc[:, -1].index, combined.iloc[:, -1], color="skyblue",
                             alpha=0.5, label='相对强弱(右轴)')  # 绘制相对强弱/超额
            ax2.set_ylim(bottom=min(combined.iloc[:, -1]))
            ax1line, ax1label = ax1.get_legend_handles_labels()
            ax2line, ax2label = ax2.get_legend_handles_labels()
            plt.legend(ax1line + ax2line, ax1label + ax2label, loc='upper left')  # 显示图例
        plt.show()
        print("净值曲线图绘制完成")
    elif plot == True and bm_code == "":
        (fof_nav - 1).plot(zorder=1)
        plt.scatter(start_date_list, fof_nav[fof_nav.index.isin(start_date_list)] - 1, c='r', s=10, marker="^",
                    zorder=2)  # 绘制调仓点
        plt.show()
        print("净值曲线图绘制完成")
    else:
        pass
        # print("未绘制净值曲线图")

    fof_record['fof_nav'] = fof_nav  # 储存FOF净值
    fof_record['bm_nav'] = bm_nav  # 储存基准净值
    # 储存日度权重
    return fof_record


# %% 代码示例
'''
##运行fof函数
# 普通股票组合
adj_table1 = pd.read_excel("Import Adj History_普通股票.xlsx")
fof_collect1 = batch_fof_run(adj_table=adj_table1, end_date='20220225', ini_fund=10000, start_nav=1.0,
                             tradeday_list=tradeday_list, data_mode="WindAPI", plot=True,
                             bm_code=["885000.WI"], bm_weight=[1],bm_type=['Index'],rebanlance="")
# 偏股混合组合 - DF模式运行效率最快
adj_table2 = pd.read_excel("Import Adj History_偏股混合.xlsx")
fund_list = adj_table2['FundID'].unique().tolist()
fund_list_str = str(fund_list)[1:-1].replace(".OF", "").replace(".SH", "").replace(".SZ", "")
query = f"select F_INFO_WINDCODE, TRADE_DT,F_NAV_ADJUSTED from '中国共同基金净值' " \
        f"where substr(F_INFO_WINDCODE, 0, 7) in ({fund_list_str}) " \
        f"and F_INFO_WINDCODE not like '%!%' " \
        f"order by TRADE_DT"
fund_nav_table2 = Obtain_DBData(query, path_fund)
fund_nav_table2.drop_duplicates(inplace=True)  # 删除重复记录
fof_collect2 = batch_fof_run(adj_table=adj_table2, end_date='20220225', ini_fund=10000, start_nav=1.0,
                             tradeday_list=tradeday_list, data_mode="DF", dataframe=fund_nav_table2, plot=True,
                             bm_code=["885001.WI"],bm_weight=[1], bm_type=['Index'],rebanlance="", excess_or_relative="relative",
                             tqdm_disable=True)
# fof_collect1['fof_nav'].loc['2022-4-12',:]/fof_collect1['fof_nav'].loc['2021-12-31',:]-1
# 灵活配置组合 - DB模式运行效率最慢
adj_table3 = pd.read_excel("Import Adj History_灵活配置.xlsx")
fof_collect3 = batch_fof_run(adj_table=adj_table3, end_date='20220225', ini_fund=10000, start_nav=1.0,
                             tradeday_list=tradeday_list, data_mode="DB", database_path=path_fund, plot=True,
                             bm_code=["885061.WI"],bm_weight=[1], bm_type=['Index'],rebanlance="")
# 复合基准
fof_collect4 = batch_fof_run(adj_table=adj_table2, end_date='20220225', ini_fund=10000, start_nav=1.0,
                             tradeday_list=tradeday_list, data_mode="DF", dataframe=fund_nav_table2, plot=True,
                             bm_code={"000300.SH", "H11001.CSI"},bm_weight=[0.8,0.2],bm_type=["Index"]*2,rebanlance='3m')
fof_collect5 = batch_fof_run(adj_table=adj_table2, end_date='20220225', ini_fund=10000, start_nav=1.0,
                             tradeday_list=tradeday_list, data_mode="DF", dataframe=fund_nav_table2, plot=True,
                             bm_code="",bm_weight="",bm_type="",rebanlance="")
fof_collect6 = batch_fof_run(adj_table=adj_table2, end_date='20220225', ini_fund=10000, start_nav=1.0,
                             tradeday_list=tradeday_list, data_mode="DF", dataframe=fund_nav_table2, plot=False,
                             bm_code={"000300.SH", "H11001.CSI"},bm_weight=[0.8,0.2],bm_type=["Index"]*2,rebanlance="")
'''

# %% #绩效分析主函数(目前只支持DF和DB模式)
# 输出类别，序列就是DataFrame,单一数值就是Series
'''目前支持指标
1 "Cumulative Return Series":  # 累积回报序列
2 "Cumulative Return":  # 区间累积回报
3 "Annual Return":  # 区间年化回报
4 "Cumulative Return Table":  # 阶段涨幅表
5 "Annual Volativity":  # 区间年化波动
6 "Sharpe Ratio":  # 夏普比率
7 "Draw Down Series":  # 动态最大回撤序列
8 "Max Draw Down":  # 区间最大回撤
9 "Draw Down Detail":  # 最大回撤明细表，返回DataFrame
10 "Average Draw Down":  # 区间平均回撤
11 "Calmar Ratio":  # Calmar比率
12 "Downside Risk":  # 下行风险
13 "Sortino Ratio":  # Sortino比率
14 "Beta":  # Beta
15 "Alpha":  # Alpha
16 "Up Capture":  # Up Capture
17 "Down Capture":  # Down Capture
18 "Up-Down Capture":  # Up-Down Capture：Computes the ratio of up_capture to down_capture.
19 "Cumulative Excess Return Series_type1":  # 超额回报序列算法1，先算日度超额，再复利累积
20 "Cumulative Excess Return Series_type2":  # 超额回报序列算法2，先再复利累积，再作差算超额 - 常用但误用
21 "Cumulative Excess Return_type1":  # 区间超额回报算法1
22 "Cumulative Excess Return_type2":  # 区间超额回报算法2
23 "Annual Excess Return_type1":  # 区间年化超额回报算法1
24 "Annual Excess Return_type2":  # 区间年化超额回报算法2
25 "Excess Return Detail":  # 超额回报表
26 "Tracking Error":  # 年化跟踪误差
27 "Information Ratio":  # 信息比率Information Ratio
28 "Win Rate":  # 超额胜率 day/eow/eom/eoq/eoy
29 "Win Rate Table":  # 正收益概率/胜率Table day/eow/eom/eoq/eoy
30 "Rolling Return Detail": # 滚动回报明细
31 "Rolling Return Table": # 滚动回报分布
32 TODO 最高单期回报
33 TODO 最低单期回报
34 TODO 上涨/下跌期数
35 TODO 平均单期回报
36 TODO Burke Ratio
37 连续持有盈利概率
28 创新高次数
'''


# TODO 不断完善指标体系

# 虽然FundID支持列表导入，但目前只能跑单只基金
def cal_perf_index(Fund_ID="", index="", start_date="", end_date="", data_mode="DF", dataframe="", fund_series="",
                   bm_series="", tradeday_list=tradeday_list, **kwargs):
    if data_mode in ['DF', 'WindAPI']:
        f_nav = fetch_nav(asset_list=[Fund_ID], start_date=start_date, end_date=end_date, data_mode=data_mode,
                          dataframe=dataframe, tradeday_list=tradeday_list)
    elif data_mode in ['Series']:
        f_nav = fund_series

    f_daily_return = f_nav.pct_change()

    if len(bm_series) > 0:
        bm_series = pd.DataFrame(bm_series)
        bm_series.index = pd.DatetimeIndex(bm_series.index)  # 统一将业绩基准列表的索引改为DatetimeIndex
        bm_series = bm_series[bm_series.index.isin(f_nav.index)]  # bm_series的日期与f_nav保持一致
        if len(bm_series) == len(f_nav):  # 判断业绩基准长度与基金净值长度是否匹配
            b_daily_return = pd.DataFrame(bm_series.pct_change().iloc[:, 0])
            b_daily_return.index = pd.DatetimeIndex(b_daily_return.index)
        else:
            print("业绩基准与净值长度不匹配！")

    elif len(bm_series) == 0:  # 如果基准为空则赋值为0
        b_daily_return = pd.DataFrame([0] * len(f_nav))
        b_daily_return.index = pd.DatetimeIndex(f_daily_return.index)
        bm_series = b_daily_return.copy()

    # 开始计算指标
    if index == "Cumulative Return Series":  # 累积回报序列
        f_cum_return_series = em.cum_returns(f_daily_return)
        f_cum_return_series.columns = [Fund_ID]
        return f_cum_return_series

    elif index == "Cumulative Return":  # 区间累积回报
        f_cum_return = pd.Series(float(f_nav.tail(1).values / f_nav.head(1).values) - 1)
        f_cum_return.index = [Fund_ID]
        return f_cum_return

    elif index == "Annual Return":  # 区间年化回报
        # annualization用来更改年化交易日期取值，默认250，要保证计算正确，首行必须保留第一个日期，并储存为NA值
        f_ann_return = pd.Series(em.annual_return(f_daily_return, annualization=kwargs['annualization']))
        f_ann_return.index = [Fund_ID]
        return f_ann_return

    elif index == "Cumulative Return Table":  # 阶段涨幅表
        # 近一周、近一月、近三月、近半年、近一年、近两年、近三年、近五年、成立来、今年来、分年度、分季度
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        f_cum_return_table = dict()
        # 日期范围
        f_cum_return_table['date range'] = [start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')]
        # 区间回报
        f_latest_nav = f_nav.tail(1).values[0][0]
        b_latest_nav = bm_series.tail(1).values[0][0]
        period_return = pd.DataFrame()
        for periodlen in ['1w', '1m', '3m', '6m', '1y', '2y', '3y', '5y']:
            start_date0 = fstartday(end_date, shift_length=periodlen, tradeday=True, tradeday_shift='after',
                                    tradeday_list=tradeday_list)
            if start_date0 >= start_date:  # 如果业绩区间起点晚于净值起点，可以计算相关指标
                f_return0 = f_latest_nav / f_nav.loc[start_date0].values[0] - 1
                if bm_series.loc[start_date0].values[0] != 0:  # 此时判断是否配置了业绩基准，否则为0
                    b_return0 = b_latest_nav / bm_series.loc[start_date0].values[0] - 1
                else:
                    b_return0 = 0
                f_excess0 = f_return0 - b_return0
                temp = pd.DataFrame([f_return0, b_return0, f_excess0]).T
                temp.columns = ['Fund', 'Benchmark', 'Excess']
                temp.index = [periodlen]
                period_return = pd.concat([period_return, temp])
            else:
                pass
        f_cum_return_table['period_return'] = period_return
        # 年度回报
        f_yearly_return = qs.utils.aggregate_returns(f_daily_return.dropna(), period='eoy', compounded=True)
        b_yearly_return = qs.utils.aggregate_returns(b_daily_return.dropna(), period='eoy', compounded=True)
        f_yearly_excess = f_yearly_return.iloc[:, 0] - b_yearly_return.iloc[:, 0]
        temp = pd.concat([f_yearly_return, b_yearly_return, f_yearly_excess], axis=1)
        temp.columns = ['Fund', 'Benchmark', 'Excess']
        f_cum_return_table['yearly_return'] = temp
        # 季度回报
        f_quarter_return = qs.utils.aggregate_returns(f_daily_return.dropna(), period='eoq', compounded=True)
        b_quarter_return = qs.utils.aggregate_returns(b_daily_return.dropna(), period='eoq', compounded=True)
        f_quarter_excess = f_quarter_return.iloc[:, 0] - b_quarter_return.iloc[:, 0]
        temp = pd.concat([f_quarter_return, b_quarter_return, f_quarter_excess], axis=1)
        temp.columns = ['Fund', 'Benchmark', 'Excess']
        f_cum_return_table['quarter_return'] = temp
        # 月度回报
        f_month_return = qs.utils.aggregate_returns(f_daily_return.dropna(), period='eom', compounded=True)
        b_month_return = qs.utils.aggregate_returns(b_daily_return.dropna(), period='eom', compounded=True)
        f_month_excess = f_month_return.iloc[:, 0] - b_month_return.iloc[:, 0]
        temp = pd.concat([f_month_return, b_month_return, f_month_excess], axis=1)
        temp.columns = ['Fund', 'Benchmark', 'Excess']
        f_cum_return_table['month_return'] = temp
        return f_cum_return_table

    elif index == "Annual Volativity":  # 区间年化波动
        f_ann_volativity = pd.Series(em.annual_volatility(f_daily_return, annualization=kwargs['annualization']))
        f_ann_volativity.index = [Fund_ID]
        return f_ann_volativity

    elif index == "Sharpe Ratio":  # 夏普比率
        f_ann_sharpe = (em.annual_return(f_daily_return, annualization=kwargs['annualization']) - kwargs['risk_free']) / \
                       em.annual_volatility(f_daily_return, annualization=kwargs['annualization'])
        f_ann_sharpe = pd.Series(f_ann_sharpe)
        f_ann_sharpe.index = [Fund_ID]
        return f_ann_sharpe

    elif index == "Draw Down Series":  # 动态最大回撤序列
        f_dynamic_dd_series = pd.DataFrame(qs.stats.to_drawdown_series(f_daily_return))
        f_dynamic_dd_series.columns = [Fund_ID]
        return f_dynamic_dd_series

    elif index == "Max Draw Down":  # 区间最大回撤
        f_max_DD = pd.Series(em.max_drawdown(f_daily_return))
        f_max_DD.index = [Fund_ID]
        return f_max_DD

    elif index == "Draw Down Detail":  # 最大回撤明细表，返回DataFrame
        f_DD_detail = qs.stats.drawdown_details(f_daily_return)
        return f_DD_detail

    elif index == "Average Draw Down":  # 区间平均回撤
        f_dynamic_dd_series = pd.DataFrame(qs.stats.to_drawdown_series(f_daily_return))
        f_avg_DD = f_dynamic_dd_series.mean()
        f_avg_DD.index = [Fund_ID]
        return f_avg_DD

    elif index == "Calmar Ratio":  # Calmar比率
        # 不支持直接输入DataFrame，需要iloc转换成序列
        f_calmar_ratio = pd.Series(em.calmar_ratio(f_daily_return.iloc[:, 0], annualization=kwargs['annualization']))
        # f_calmar_ratio = pd.Series(em.calmar_ratio(f_daily_return, annualization=kwargs['annualization']))
        f_calmar_ratio.index = [Fund_ID]
        return f_calmar_ratio

    elif index == "Downside Risk":  # 下行风险
        f_downside_risk = pd.Series(em.downside_risk(f_daily_return, required_return=kwargs['required_return'],
                                                     annualization=kwargs['annualization']))
        f_downside_risk.index = [Fund_ID]
        return f_downside_risk

    elif index == "Sortino Ratio":  # Sortino比率
        f_sortino_ratio = ((em.annual_return(f_daily_return, annualization=kwargs['annualization']) - kwargs[
            'required_return']) / em.downside_risk(f_daily_return, annualization=kwargs['annualization']))
        f_sortino_ratio = pd.Series(f_sortino_ratio)
        f_sortino_ratio.index = [Fund_ID]
        return f_sortino_ratio

    elif index == "Beta":  # Beta
        f_beta = pd.Series(em.beta(f_daily_return, b_daily_return, risk_free=kwargs['risk_free']))
        f_beta.index = [Fund_ID]
        return f_beta

    elif index == "Alpha":  # Alpha
        f_alpha = pd.Series(em.alpha(f_daily_return, b_daily_return, risk_free=kwargs['risk_free'],
                                     annualization=kwargs['annualization']))
        f_alpha.index = [Fund_ID]
        return f_alpha

    elif index == "Up Capture":  # Up Capture
        f_up_capture = pd.Series(em.up_capture(f_daily_return.iloc[:, 0], b_daily_return.iloc[:, 0]))
        f_up_capture.index = [Fund_ID]
        return f_up_capture

    elif index == "Down Capture":  # Down Capture
        f_down_capture = pd.Series(em.down_capture(f_daily_return.iloc[:, 0], b_daily_return.iloc[:, 0]))
        f_down_capture.index = [Fund_ID]
        return f_down_capture

    elif index == "Up-Down Capture":  # Up-Down Capture：Computes the ratio of up_capture to down_capture.
        f_updown_capture = pd.Series(em.up_down_capture(f_daily_return.iloc[:, 0], b_daily_return.iloc[:, 0]))
        f_updown_capture.index = [Fund_ID]
        return f_updown_capture

    elif index == "Cumulative Excess Return Series_type1":  # 超额回报序列算法1，先算日度超额，再复利累积
        f_cum_exreturn_series1 = em.cum_returns(f_daily_return.iloc[:, 0] - b_daily_return.iloc[:, 0])
        f_cum_exreturn_series1.columns = [Fund_ID]
        return f_cum_exreturn_series1

    elif index == "Cumulative Excess Return Series_type2":  # 超额回报序列算法2，先再复利累积，再作差算超额
        f_cum_exreturn_series2 = em.cum_returns(f_daily_return.iloc[:, 0]) - em.cum_returns(b_daily_return.iloc[:, 0])
        f_cum_exreturn_series2.columns = [Fund_ID]
        return f_cum_exreturn_series2

    elif index == "Cumulative Excess Return_type1":  # 区间超额回报算法1
        f_cum_exreturn_series1 = em.cum_returns(f_daily_return.iloc[:, 0] - b_daily_return.iloc[:, 0])
        f_cum_exreturn1 = pd.Series(
            float(f_cum_exreturn_series1.tail(1).values - f_cum_exreturn_series1.head(1).values))
        f_cum_exreturn1.index = [Fund_ID]
        return f_cum_exreturn1

    elif index == "Cumulative Excess Return_type2":  # 区间超额回报算法2
        f_cum_exreturn_series2 = em.cum_returns(f_daily_return.iloc[:, 0]) - em.cum_returns(b_daily_return.iloc[:, 0])
        f_cum_exreturn2 = pd.Series(
            float(f_cum_exreturn_series2.tail(1).values - f_cum_exreturn_series2.head(1).values))
        f_cum_exreturn2.index = [Fund_ID]
        return f_cum_exreturn2

    elif index == "Annual Excess Return_type1":  # 区间年化超额回报算法1
        # annualization用来更改年化交易日期取值，默认250，要保证计算正确，首行必须保留第一个日期，并储存为NA值
        f_ann_exreturn1 = pd.Series(
            em.annual_return(f_daily_return.iloc[:, 0] - b_daily_return.iloc[:, 0],
                             annualization=kwargs['annualization']))
        f_ann_exreturn1.index = [Fund_ID]
        return f_ann_exreturn1

    elif index == "Annual Excess Return_type2":  # 区间年化超额回报算法2
        # annualization用来更改年化交易日期取值，默认250，要保证计算正确，首行必须保留第一个日期，并储存为NA值
        f_ann_exreturn2 = pd.Series(
            em.annual_return(f_daily_return.iloc[:, 0], annualization=kwargs['annualization']) -
            em.annual_return(b_daily_return.iloc[:, 0], annualization=kwargs['annualization']))
        f_ann_exreturn2.index = [Fund_ID]
        return f_ann_exreturn2

    elif index == "Excess Return Detail":  # 超额回报表
        Fund_Return = qs.utils.aggregate_returns(f_daily_return.iloc[:, 0].dropna(), period=kwargs['period'],
                                                 compounded=True)
        Benchmark_Return = qs.utils.aggregate_returns(b_daily_return.iloc[:, 0].dropna(), period=kwargs['period'],
                                                      compounded=True)
        f_excess_detail = pd.concat([Fund_Return, Benchmark_Return, Fund_Return - Benchmark_Return], axis=1)
        f_excess_detail.columns = ['Fund', 'Benchmark', 'Excess']
        return f_excess_detail

    elif index == "Tracking Error":  # 年化跟踪误差
        f_tracking_err = pd.Series(
            em.annual_volatility(f_daily_return.iloc[:, 0] - b_daily_return.iloc[:, 0],
                                 annualization=kwargs['annualization']))
        f_tracking_err.index = [Fund_ID]
        return f_tracking_err

    elif index == "Information Ratio":  # 信息比率Information Ratio
        f_ann_exreturn2 = pd.Series(em.annual_return(f_daily_return.iloc[:, 0], annualization=kwargs['annualization']) -
                                    em.annual_return(b_daily_return.iloc[:, 0], annualization=kwargs['annualization']))
        f_tracking_err = pd.Series(
            em.annual_volatility(f_daily_return.iloc[:, 0] - b_daily_return.iloc[:, 0],
                                 annualization=kwargs['annualization']))
        f_info_ratio = f_ann_exreturn2 / f_tracking_err
        f_info_ratio.index = [Fund_ID]
        return f_info_ratio

    elif index == "Win Rate":  # 超额胜率 day/eow/eom/eoq/eoy
        Fund_Return = qs.utils.aggregate_returns(f_daily_return.iloc[:, 0].dropna(), period=kwargs['period'],
                                                 compounded=True)
        Benchmark_Return = qs.utils.aggregate_returns(b_daily_return.iloc[:, 0].dropna(), period=kwargs['period'],
                                                      compounded=True)
        f_excess_detail = pd.concat([Fund_Return, Benchmark_Return, Fund_Return - Benchmark_Return], axis=1)
        f_excess_detail.columns = ['Fund', 'Benchmark', 'Excess']
        f_win_rate = pd.Series(qs.stats.win_rate(f_excess_detail)[-1])
        f_win_rate.index = [Fund_ID]
        return f_win_rate

    elif index == "Win Rate Table":  # 正收益概率/胜率Table day/eow/eom/eoq/eoy
        Fund_Return = qs.utils.aggregate_returns(f_daily_return.iloc[:, 0].dropna(), period=kwargs['period'],
                                                 compounded=True)
        Benchmark_Return = qs.utils.aggregate_returns(b_daily_return.iloc[:, 0].dropna(), period=kwargs['period'],
                                                      compounded=True)
        f_excess_detail = pd.concat([Fund_Return, Benchmark_Return, Fund_Return - Benchmark_Return], axis=1)
        f_excess_detail.columns = ['Fund', 'Benchmark', 'Excess']
        f_win_rate_table = qs.stats.win_rate(f_excess_detail)
        return f_win_rate_table

    elif index == "Rolling Cumulative Return Detail":  # 滚动回报明细
        window_param = {"1m": 30, "3m": 90, "6m": 180, "9m": 270, "1y": 365, '2y': 730, '3y': 1095, '5y': 1825,
                        '10y': 3650}
        daterange = pd.date_range(start=f_daily_return.index[0],
                                  end=f_daily_return.index[-1])  # 先把f_daily_return填充到自然日度，再rolling
        f_daily_return365 = pd.DataFrame(daterange.map(f_daily_return.iloc[:, 0])).fillna(0)  # 用0填充Nan值
        f_daily_return365.set_index(daterange, inplace=True)
        window_days = window_param[kwargs['window']]
        f_rolling_return = f_daily_return365.rolling(window_days).agg(lambda x: em.cum_returns(x).tail(1))
        f_rolling_return.columns = [Fund_ID + "_" + kwargs['window']]
        return f_rolling_return

    elif index == "Rolling Cumulative Return Table":  # 滚动回报分布
        window_param = {"1m": 30, "3m": 90, "6m": 180, "9m": 270, "1y": 365, '2y': 730, '3y': 1095, '5y': 1825,
                        '10y': 3650}
        daterange = pd.date_range(start=f_daily_return.index[0],
                                  end=f_daily_return.index[-1])  # 先把f_daily_return填充到自然日度，再rolling
        f_daily_return365 = pd.DataFrame(daterange.map(f_daily_return.iloc[:, 0])).fillna(0)  # 用0填充Nan值
        f_daily_return365.set_index(daterange, inplace=True)
        window_days = window_param[kwargs['window']]
        f_rolling_return = f_daily_return365.rolling(window_days).agg(lambda x: em.cum_returns(x).tail(1))
        f_return_dist = f_rolling_return.quantile([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
        f_return_dist.columns = [Fund_ID + "_" + kwargs['window']]
        return f_return_dist

    elif index == "Rolling Annualized Return Detail":  # 滚动年化回报明细，计算年化回报的时候要剔除非交易日，否则年化值会低估
        window_param = {"1m": 30, "3m": 90, "6m": 180, "9m": 270, "1y": 365, '2y': 730, '3y': 1095, '5y': 1825,
                        '10y': 3650}
        daterange = pd.date_range(start=f_daily_return.index[0],
                                  end=f_daily_return.index[-1])  # 先把f_daily_return填充到自然日度，再rolling
        f_daily_return365 = pd.DataFrame(daterange.map(f_daily_return.iloc[:, 0])).fillna(0)  # 用0填充Nan值
        f_daily_return365.set_index(daterange, inplace=True)
        window_days = window_param[kwargs['window']]
        f_rolling_return = f_daily_return365.rolling(window_days).agg(
            lambda x: em.annual_return(x[x.index.isin(tradeday_list)], annualization=kwargs['annualization']))
        f_rolling_return.columns = [Fund_ID + "_" + kwargs['window']]
        return f_rolling_return

    elif index == "Rolling Annualized Return Table":  # 滚动年化回报分布，计算年化回报的时候要剔除非交易日，否则年化值会低估
        window_param = {"1m": 30, "3m": 90, "6m": 180, "9m": 270, "1y": 365, '2y': 730, '3y': 1095, '5y': 1825,
                        '10y': 3650}
        daterange = pd.date_range(start=f_daily_return.index[0],
                                  end=f_daily_return.index[-1])  # 先把f_daily_return填充到自然日度，再rolling
        f_daily_return365 = pd.DataFrame(daterange.map(f_daily_return.iloc[:, 0])).fillna(0)  # 用0填充Nan值
        f_daily_return365.set_index(daterange, inplace=True)
        window_days = window_param[kwargs['window']]
        f_rolling_return = f_daily_return365.rolling(window_days).agg(
            lambda x: em.annual_return(x[x.index.isin(tradeday_list)], annualization=kwargs['annualization']))
        f_return_dist = f_rolling_return.quantile([0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
        f_return_dist.columns = [Fund_ID + "_" + kwargs['window']]
        return f_return_dist
    #TODO 增加指标计算剥离风格后的Alpha，以及Alpha稳定性

    # 顺境收益率、逆境收益率、etc
    else:
        print("请检查指标名称")
        return


# %% 代码示例

# 通过fetch_nav取数据框，成为长数据

'''
# 累积回报序列
cal_perf_index(Fund_ID='360001.OF', index="Cumulative Return Series", start_date="20190101", end_date="20211231",
               data_mode="DF", dataframe=fund_nav_table,
               tradeday_list=tradeday_list).plot()
plt.show()
# 累积回报
cal_perf_index(Fund_ID='360001.OF', index="Cumulative Return", start_date="20190101", end_date="20211231",
               data_mode="DF", dataframe=fund_nav_table,
               tradeday_list=tradeday_list)

# 累积回报 - Series模式
fund_series = w.wsd('360001.OF', "NAV_adj", "20190101", "20211231", usedf=True)[1]
cal_perf_index(Fund_ID="360001.OF", fund_series=fund_series, index="Cumulative Return", data_mode="Series",
               tradeday_list=tradeday_list,
               annualization=245, required_return=0)

# 年化回报
cal_perf_index(Fund_ID='360001.OF', index="Annual Return", start_date="20190101", end_date="20211231", data_mode="DF",
               dataframe=fund_nav_table,
               tradeday_list=tradeday_list, annualization=245)
# 区间回报表
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
period_rtn=cal_perf_index(Fund_ID='360001.OF', index="Cumulative Return Table", start_date="20190101", end_date="20211231",
               data_mode="DF", dataframe=fund_nav_table,
               tradeday_list=tradeday_list,bm_series=bm_series)
period_rtn['period_return']
period_rtn['yearly_return']
period_rtn['quarter_return']
period_rtn['month_return']
cal_perf_index(Fund_ID='360001.OF', index="Cumulative Return Table", start_date="20190101", end_date="20211231",
               data_mode="DF", dataframe=fund_nav_table,
               tradeday_list=tradeday_list,bm_series="")
# 年化波动
cal_perf_index(Fund_ID='360001.OF', index="Annual Volativity", start_date="20190101", end_date="20211231",
               data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list, annualization=245)

# 夏普比率
cal_perf_index(Fund_ID='360001.OF', index="Sharpe Ratio", start_date="20190101", end_date="20211231", data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list, annualization=245, risk_free=0.015)

# 动态最大回撤序列
cal_perf_index(Fund_ID='360001.OF', index="Draw Down Series", start_date="20190101", end_date="20211231",
               data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list).plot()
plt.rcParams['axes.unicode_minus'] = False  # 处理负号显示问题
plt.show()

# 最大回撤
cal_perf_index(Fund_ID='360001.OF', index="Max Draw Down", start_date="20190101", end_date="20211231", data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list)

# 最大回撤明细
cal_perf_index(Fund_ID='360001.OF', index="Draw Down Detail", start_date="20190101", end_date="20211231",
               data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list)

# 平均回撤
cal_perf_index(Fund_ID='360001.OF', index="Average Draw Down", start_date="20190101", end_date="20211231",
               data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list)

# Calmar比率
cal_perf_index(Fund_ID='360001.OF', index="Calmar Ratio", start_date="20190101", end_date="20211231", data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list, annualization=245)

# 下行风险
cal_perf_index(Fund_ID='360001.OF', index="Downside Risk", start_date="20190101", end_date="20211231", data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list, annualization=245, required_return=0)

# Sortino比率
cal_perf_index(Fund_ID='360001.OF', index="Sortino Ratio", start_date="20190101", end_date="20211231", data_mode="DF",
               dataframe=fund_nav_table, tradeday_list=tradeday_list, annualization=245, required_return=0)

# Beta
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Beta", start_date="20190101", end_date="20211231", data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, risk_free=0.015)

# Alpha
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Alpha", start_date="20190101", end_date="20211231", data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, risk_free=0.015, annualization=245)

# Up Capture
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Up Capture", start_date="20190101", end_date="20211231", data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, risk_free=0.015, annualization=245)

# Down Capture
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Down Capture", start_date="20190101", end_date="20211231",
               data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, risk_free=0.015, annualization=245)

# Up-Down Capture
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Up-Down Capture", start_date="20190101", end_date="20211231",
               data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, risk_free=0.015, annualization=245)

# 区间累计超额回报type1
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Cumulative Excess Return_type1", start_date="20190101", end_date="20211231",
               data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series)

# 区间累计超额回报type2
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Cumulative Excess Return_type2", start_date="20190101", end_date="20211231",
               data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series)

# 年化超额回报type1
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Annual Excess Return_type1", start_date="20190101", end_date="20211231",
               data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, annualization=245)

# 年化超额回报type2
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Annual Excess Return_type2", start_date="20190101", end_date="20211231",
               data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, annualization=245)

# 超额回报明细表
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Excess Return Detail", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series=bm_series, period='eoq')  # 季度超额
cal_perf_index(Fund_ID='005137.OF', index="Excess Return Detail", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series=bm_series, period='eom')  # 月度超额

# 年化跟踪误差
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Tracking Error", start_date="20190101", end_date="20211231",
               data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, annualization=245)

# 信息比率information Ratio
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Information Ratio", start_date="20190101", end_date="20211231",
               data_mode="WindAPI",
               tradeday_list=tradeday_list, bm_series=bm_series, annualization=245)
# 胜率win rate
bm_series = w.wsd('000300.SH', "Close", "20190101", "20211231", usedf=True)[1]  # 指数
cal_perf_index(Fund_ID='005137.OF', index="Win Rate", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series="", period='eoq')  # 基准为空就是正收益概率
cal_perf_index(Fund_ID='005137.OF', index="Win Rate", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series=bm_series, period='')  # 基准不为空就是超额胜率
# 正收益概率/胜率Table
cal_perf_index(Fund_ID='005137.OF', index="Win Rate Table", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series=bm_series, period='eom')
cal_perf_index(Fund_ID='005137.OF', index="Win Rate Table", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series="", period='eom')
# 滚动累积回报明细
cal_perf_index(Fund_ID='005137.OF', index="Rolling Cumulative Return Detail", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series=bm_series, window='6m').hist()
plt.title("连续持有收益分布",fontsize=20)
plt.show()

# 滚动累计回报分位数
cal_perf_index(Fund_ID='005137.OF', index="Rolling Cumulative Return Table", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series=bm_series, window='6m')
cal_perf_index(Fund_ID='005137.OF', index="Rolling Cumulative Return Table", start_date="20190101", end_date="20211231",
               data_mode="WindAPI", tradeday_list=tradeday_list, bm_series=bm_series, window='1y').plot.bar()
plt.title("连续持有收益累计概率曲线",fontsize=20)
plt.show()

# 滚动累积年化回报明细
index_series = w.wsd('885001.WI', "Close", "20031231", "20220624", usedf=True)[1]  # 指数


rolling_1y=cal_perf_index(Fund_ID='', index="Rolling Annualized Return Detail", start_date="20031231", end_date="20211231",
               data_mode="Series", tradeday_list=tradeday_list, fund_series=index_series, window='1y',annualization=245)
rolling_3y=cal_perf_index(Fund_ID='', index="Rolling Annualized Return Detail", start_date="20031231", end_date="20211231",
               data_mode="Series", tradeday_list=tradeday_list, fund_series=index_series, window='3y',annualization=245)
rolling_5y=cal_perf_index(Fund_ID='', index="Rolling Annualized Return Detail", start_date="20031231", end_date="20211231",
               data_mode="Series", tradeday_list=tradeday_list, fund_series=index_series, window='5y',annualization=245)
rolling_10y=cal_perf_index(Fund_ID='', index="Rolling Annualized Return Detail", start_date="20031231", end_date="20211231",
               data_mode="Series", tradeday_list=tradeday_list, fund_series=index_series, window='10y',annualization=245)

rolling_df=pd.concat([rolling_1y,rolling_3y,rolling_5y,rolling_10y],axis=1)
rolling_df.columns=['连续持有1年','连续持有3年','连续持有5年','连续持有10年']
# rolling_df.plot.kde(bw_method=0.5)
rolling_df.boxplot()
plt.show()
rolling_df.to_excel('rolling.xlsx')
'''

# %% 分层回测函数

'''参考研报
# 20210630-渤海证券-渤海证券FOF研究系列之二：偏股型基金的因子测试
# FOF 研究系列之一：如何系统搭建基金经理的研究框架？
# 东方证券：FOF 基金池的定量构建
# 华西证券：主动权益基金的量化评价体系构建
# 动量时间占比策略：优选业绩稳健的主动基金
'''
"""
factor_data格式
FundID  InspectDate  Factor
"""


# TODO 为了降低日历效应的影响，回测窗口与预测区间可以不一样，例如按照月频取预测，但是预测区间可以是未来3个月、6个月、一年等等
def fund_backtesting(factor_data="", ngroup=5, output='backtesting_result.xlsx', win_threshold=[0, 1],
                     test_end_date="", reset_nav=False, data_mode='DF', dataframe='', database_path="",
                     tradeday_list=tradeday_list, **kwargs):
    # 开始回测流程。数据结果全部储存到backtesting_result字典中
    backtesting_result = dict()
    factor_data = factor_data.copy()
    factor_data['InspectDate'] = factor_data['InspectDate'].dt.strftime('%Y-%m-%d')
    # 设定缩尾阈值参数，默认是[0,1],不缩尾
    print("开始因子缩尾")
    factor_data_gp = factor_data.groupby('InspectDate')['Factor']
    # Assign the lower-bound ('lb') and upper-bound ('ub') for Winsorizing
    factor_data[f'factor_lb_{win_threshold[0]}'] = factor_data_gp.transform('quantile', win_threshold[0])
    factor_data[f'factor_ub_{win_threshold[1]}'] = factor_data_gp.transform('quantile', win_threshold[1])
    # Winsorize
    factor_data['Factor_wins'] = factor_data['Factor'].clip(upper=factor_data[f'factor_ub_{win_threshold[1]}'],
                                                            lower=factor_data[f'factor_lb_{win_threshold[0]}'])
    backtesting_result['factor_detail'] = factor_data  # 输出: 因子明细

    # 统计各期基金数量和因子分布
    print("统计因子分布")
    backtesting_result['factor_ori_summary'] = factor_data[['FundID', 'InspectDate', 'Factor']].groupby(
        'InspectDate').describe()  # 输出原始因子分布
    g = sns.FacetGrid(factor_data, col='InspectDate', hue='InspectDate', col_wrap=3)
    g = g.map(sns.kdeplot, "Factor", cut=0, fill=True, common_norm=False, alpha=1, legend=False)
    g = g.set_titles("{col_name}")
    g.fig.suptitle('各期原始因子分布', fontsize=20)
    plt.savefig('各期原始因子分布.png')
    plt.show()

    backtesting_result['factor_wins_summary'] = factor_data[['FundID', 'InspectDate', 'Factor_wins']].groupby(
        'InspectDate').describe()  # 输出缩尾后因子分布
    g = sns.FacetGrid(factor_data, col='InspectDate', hue='InspectDate', col_wrap=3)
    g = g.map(sns.kdeplot, "Factor_wins", cut=0, fill=True, common_norm=False, alpha=1, legend=False)
    g = g.set_titles("{col_name}")
    g.fig.suptitle('各期缩尾后因子分布', fontsize=20)
    plt.savefig('各期缩尾后因子分布.png')
    plt.show()

    # 生成最终的因子数据
    factor_data_final = factor_data[['FundID', 'InspectDate', 'Factor_wins']].rename(columns={"Factor_wins": 'Factor'})

    # 统计相邻两期共有的基金数量及相应的因子相关性 输出：总共期数N，滞后阶数1~N-1，共有元素，因子暴露相关性
    factor_pivot = factor_data_final.pivot(index='FundID', columns='InspectDate', values='Factor')
    corr_mat = factor_pivot.corr(method='spearman')
    factor_corr_info = pd.DataFrame()
    if len(factor_pivot.columns) == 1:
        print('因子期数不足两期!')
    else:
        for i in range(len(factor_pivot.columns) - 1):  # 循环起始日期
            np.diagonal(corr_mat, offset=i + 1)
            for j in range(i + 1, len(factor_pivot.columns)):  # 循环滞后阶数
                common_items = factor_pivot.iloc[:, [i, j]].dropna(how='any').shape[0]
                factor_corr_info = pd.concat(
                    [factor_corr_info, pd.DataFrame([factor_pivot.columns[i], factor_pivot.columns[j],
                                                     j - i, common_items, corr_mat.iloc[j, i]]).T])
        factor_corr_info.columns = ['Inspect_Date1', 'Inspect_Date2', "Lag", "Common_Items", 'Factor_Corr']

    backtesting_result['factor_corr_detail'] = factor_corr_info
    # 相邻两期的因子相关系数
    backtesting_result['factor_corr_lag1'] = factor_corr_info.loc[factor_corr_info.Lag == 1, :]

    # 对因子进行分组  Group1数值最小，Group5数值最大
    print("进行因子分组")
    factor_group = factor_data_final.groupby('InspectDate').Factor.agg(
        lambda x: pd.qcut(x, q=ngroup, duplicates='drop',
                          labels=['Group' + str(i) for i in range(1, ngroup + 1)])).explode()
    # factor_group.reset_index(drop=True)
    factor_data_final['Factor_Group'] = factor_group.reset_index(drop=True)
    # 检查哪个日期的分组数目过多
    for inspectdate in sorted(set(factor_data_final['InspectDate'])):
        if len(set(
                factor_data_final.loc[factor_data_final.InspectDate == inspectdate, "Factor_Group"].tolist())) < ngroup:
            print(f"{inspectdate}存在部分分组基金数量为0，请缩减分组数量！")
    backtesting_result['factor_group'] = factor_data_final

    # 分组回测业绩
    test_end_date = [pd.to_datetime(test_end_date).strftime("%Y-%m-%d")]
    inspectdates = sorted(set(factor_data['InspectDate'])) + test_end_date
    result_collect = nav_collect = factor_data_plus = pd.DataFrame()
    start_nav = [1.0] * ngroup
    print("开始因子分层回测")
    for i in tqdm(range(0, len(inspectdates) - 1)):
        # 起始日期：调仓日的下一个交易日为起始日（含当天）
        start_date = fendday(inspectdates[i], shift_length='', tradeday=True, tradeday_shift='after')
        # 终止日期：如果end_date是交易日，则取前一个交易日，如果end_date不是交易日，则取当天
        end_date0 = fendday(inspectdates[i + 1], shift_length='', tradeday=True, tradeday_shift='before')
        end_date = tradeday_list[tradeday_list.get_loc(end_date0) - 1] if end_date0 in tradeday_list else end_date0
        factor_data_i = factor_data_final.loc[factor_data_final.InspectDate == inspectdates[i], :]
        nav_group = sub_fund_ret_collect = pd.DataFrame()
        for index, group_j in enumerate(sorted(set(factor_data_i['Factor_Group']))):
            fund_list_j = factor_data_i.loc[factor_data_i.Factor_Group == group_j, "FundID"]
            fof_result = fof_run(fund_list=fund_list_j, ini_weight_list=[1 / len(fund_list_j)] * len(fund_list_j),
                                 ini_fund=10000, start_nav=start_nav[index], start_date=start_date, end_date=end_date,
                                 data_mode=data_mode, tradeday_list=tradeday_list,
                                 dataframe=dataframe, database_path=database_path)
            # 1. 核心结果的汇总
            result_vector = pd.DataFrame([group_j, inspectdates[i], fof_result['first_day'], fof_result['last_day'],
                                          fof_result['first_nav'], fof_result['last_nav'],
                                          fof_result['last_nav'] / fof_result['first_nav'] - 1]).T
            result_collect = result_collect.append(result_vector)  # 将结果归集到一个大的dataframe
            # 2. 净值的拼接
            fof_nav_j = fof_result['nav']
            fof_nav_j.name = group_j
            nav_group = pd.concat([nav_group, fof_nav_j], axis=1)
            if reset_nav == False:
                start_nav[index] = fof_result['last_nav']
            # 3. 子基金业绩表现汇总
            sub_fund_ret_collect = pd.concat([sub_fund_ret_collect, fof_result['sub_fund_return']], axis=0)
        # 子基金业绩表现与原始因子数据匹配
        factor_data_i_plus = factor_data_i.merge(sub_fund_ret_collect, left_on='FundID', right_index=True, how='left')
        factor_data_plus = pd.concat([factor_data_plus, factor_data_i_plus], axis=0)
        nav_collect = pd.concat([nav_collect, nav_group], axis=0)

    backtesting_result['facotr_and_return'] = factor_data_plus  # 输出：各期因子及下期回报
    g = sns.FacetGrid(factor_data_plus, col='InspectDate', hue='InspectDate', col_wrap=3)
    g = g.map(sns.regplot, "Factor", 'Return', ci=None)
    g = g.set_titles("{col_name}")
    g.fig.suptitle('各期因子及下期回报散点图', fontsize=20)
    plt.savefig('各期因子及下期回报散点图.png')
    plt.show()

    result_collect.reset_index(drop=True, inplace=True)
    result_collect.columns = ['Group', 'Inspect_Date', 'Start_Date', 'End_Date', 'Start_Nav', "End_Nav",
                              'Period_Return']
    backtesting_result['result_collect'] = result_collect  # 输出：分组回测净值汇总结果
    backtesting_result['nav_collect'] = nav_collect  # 输出：分组回测净值序列

    print("绘制分层回测结果")

    # Plot 1 累积净值曲线图
    nav_collect.plot()
    for i in range(0, len(inspectdates) - 1):
        plt.axvline(inspectdates[i], color="grey", linestyle=":")
    plt.grid(axis="x")
    plt.suptitle('分层净值曲线图', fontsize=20)
    plt.savefig('分层净值曲线图.png')
    plt.show()

    # Plot 2 各期分组区间回报
    aa = result_collect.loc[:, ['Inspect_Date', 'Group', 'Period_Return']]
    bb = aa.pivot(index=["Inspect_Date"], values=['Period_Return'], columns=['Group'])
    bb = pd.DataFrame(bb, dtype=np.float)
    bb.columns = bb.columns.droplevel()
    bb.index = bb.index.astype(str)
    cc = aa.pivot(index=['Group'], values=['Period_Return'], columns=["Inspect_Date"])
    cc = pd.DataFrame(cc, dtype=np.float)
    cc.columns = cc.columns.droplevel()
    cc.columns = cc.columns.astype(str)
    fig, (ax, ax2) = plt.subplots(ncols=2, sharey=True)
    ax.yaxis.tick_right()
    bb.boxplot(ax=ax)
    cc.plot.bar(ax=ax2, legend=False)
    plt.suptitle('分组区间回报分布', fontsize=20)
    plt.savefig('分组区间回报分布.png')
    plt.show()

    # Plot 3 多空组合回报（因子数值最大的组别-因子数值最小的组别）
    long_short = nav_collect.iloc[:, -1] - nav_collect.iloc[:, 0]
    long_short.name = nav_collect.iloc[:, -1].name + "-" + nav_collect.iloc[:, 0].name
    backtesting_result['long_short_nav'] = long_short
    pd.DataFrame(long_short).plot()
    plt.suptitle(f'多空组合净值曲线图({long_short.name})', fontsize=20)
    plt.savefig('多空组合净值曲线图.png')
    plt.show()

    # TODO TOP N 组合
    # 计算各期RankIC
    RankIC = factor_data_plus.groupby('InspectDate').corr(method='spearman').swaplevel().loc['Return', 'Factor']
    RankIC.name = 'RankIC'
    AvgIC = RankIC.mean()
    ICIR = AvgIC / RankIC.std()
    RankIC_total = RankIC.append(pd.Series([AvgIC, ICIR], index=['AvgIC', 'ICIR']))
    backtesting_result['Rank_IC'] = RankIC_total

    print("导出数据结果")
    plot_dict = {"factor_ori_summary": "各期原始因子分布.png", "factor_wins_summary": "各期缩尾后因子分布.png",
                 "facotr_and_return": "各期因子及下期回报散点图.png", "nav_collect": "分层净值曲线图.png",
                 "result_collect": "分组区间回报分布.png", "long_short_nav": "多空组合净值曲线图.png"}

    output_to_excel(backtesting_result, output, resetcol=True, pic_include=plot_dict)

    if os.path.exists("各期原始因子分布.png"):
        for key, value in plot_dict.items():
            os.remove(value)

    return backtesting_result


# %% 代码示例
# 生成各期基金池和因子数据

# df = pd.read_excel('基金备选池_成立两年以上基金.xlsx')  # 另有生成代码
# fund_list = list(set(df['证券代码']))
# db_start_date = '2009-01-05'
# db_end_date = '2022-04-25'  # 查看当前数据库净值截止时间,保险起见再减1交易日，防止仅更新了部分数据
# path_fund = r"{}:\Wind数据库\DB_Fund.db".format(root)
#
# nav_table_long = fetch_nav(asset_list=fund_list, type_list="",
#                            start_date=db_start_date, end_date=db_end_date, data_mode='DB', database_path=path_fund,
#                            check_na=False, censor_rebase=False, to_long=True)
#
#
# # 计算复合因子要先转化为得分再加权
# def cal_2y_ret(s):
#     rst1 = cal_perf_index(Fund_ID=s[0], index="Max Draw Down",
#                           start_date=fstartday(s[1], shift_length='2y', tradeday=True, tradeday_shift='before'),
#                           end_date=s[1],
#                           data_mode="DF", dataframe=nav_table_long)
#     rst2 = cal_perf_index(Fund_ID=s[0], index="Sharpe Ratio",
#                           start_date=fstartday(s[1], shift_length='2y', tradeday=True, tradeday_shift='before'),
#                           end_date=s[1],
#                           data_mode="DF", dataframe=nav_table_long, annualization=245, risk_free=0.015)
#
#     return 0.5 * rst1.iloc[0] + 0.5 * rst2.iloc[0]
#
#
# # 链式法则构造数据
# factor_data0 = df[['证券代码', "观察日期"]] \
#     .rename(columns={"证券代码": 'FundID', "观察日期": 'InspectDate'}) \
#     .assign(Factor=lambda x: x.apply(cal_2y_ret, axis=1))
#
# bt_rst = fund_backtesting(factor_data=factor_data0, ngroup=3, output='backtesting_result.xlsx', win_threshold=[0, 1],
#                           test_end_date=db_end_date, reset_nav=False, data_mode='DF', dataframe=nav_table_long)

# %% 获取公募基金定期报持仓函数
# 支持批量导出，可能WindAPI模式的基金代码*报告期有最大导出限制，如果有限制则分块导出

def get_fund_stk_holding(fund_code='', start_date="", end_date="", freq="H", top10=False, data_mode='WindAPI',
                         database_path=path_fund, dataframe="", show_summary=True):
    if freq == "Q":  # 生成季频截止日Index
        report_date = pd.date_range(start_date, end_date, freq='Q-DEC').strftime('%Y%m%d')
    elif freq == "H":  # 生成半年频截止日Index
        report_date = pd.date_range(start_date, end_date, freq='Q-DEC').strftime('%Y%m%d')
        report_date = report_date[report_date.map(lambda x: x.endswith("630", 5, 8) or x.endswith("231", 5, 8))]
    if data_mode == 'WindAPI':
        if w.isconnected() == False:  # 判断WindPy是否已经登录成功
            w.start()
        # 单只循环构造持仓矩阵
        wset_fund_holding = pd.DataFrame()
        for fund_code_i, report_date_j in product(fund_code, report_date):
            wset_obj_ij = w.wset("allfundhelddetail",
                                 f"rptdate={report_date_j};windcode={fund_code_i};"
                                 f"field=stock_code,marketvalueofstockholdings,hold_number,"
                                 f"proportiontototalstockinvestments,proportiontonetvalue",
                                 usedf=True)
            if wset_obj_ij[0] == 0:
                wset_fund_holding_ij = wset_obj_ij[1]
                wset_fund_holding_ij.insert(0, 'F_INFO_WINDCODE', fund_code_i)
                wset_fund_holding_ij.insert(1, 'F_PRT_ENDDATE', report_date_j)
                wset_fund_holding_ij.rename(columns={'marketvalueofstockholdings': 'F_PRT_STKVALUE',
                                                     'proportiontototalstockinvestments': 'STOCK_PER',
                                                     'proportiontonetvalue': 'F_PRT_STKVALUETONAV',
                                                     'stock_code': 'S_INFO_STOCKWINDCODE',
                                                     'hold_number': 'F_PRT_STKQUANTITY'}, inplace=True)
                wset_fund_holding_ij['STOCK_PER'] = wset_fund_holding_ij['STOCK_PER'] / 100
                wset_fund_holding_ij['F_PRT_STKVALUETONAV'] = wset_fund_holding_ij['F_PRT_STKVALUETONAV'] / 100
                wset_fund_holding = pd.concat([wset_fund_holding, wset_fund_holding_ij], axis=0)
            else:
                continue

    elif data_mode == 'DB':
        rpt_dates_str = str(list(report_date)).replace("'", "").replace(' ', '')[1:-1]
        fund_list_str = str(fund_code)[1:-1].replace(".OF", "").replace(".SH", "").replace(".SZ", "")
        query = f"select S_INFO_WINDCODE, F_PRT_ENDDATE,S_INFO_STOCKWINDCODE,F_PRT_STKVALUE,F_PRT_STKQUANTITY,STOCK_PER,F_PRT_STKVALUETONAV " \
                f"from '中国共同基金持股明细' " \
                f"where substr(S_INFO_WINDCODE, 0, 7) in ({fund_list_str}) and F_PRT_ENDDATE in ({rpt_dates_str}) " \
                f"and S_INFO_WINDCODE not like '%!%' " \
                f"order by S_INFO_WINDCODE, F_PRT_ENDDATE,STOCK_PER desc"
        wset_fund_holding = Obtain_DBData(query, database_path)
        wset_fund_holding.rename(columns={'S_INFO_WINDCODE': 'F_INFO_WINDCODE'}, inplace=True)
        wset_fund_holding['F_PRT_STKVALUE'] = wset_fund_holding['F_PRT_STKVALUE'] / 10000  # 万元
        wset_fund_holding['F_PRT_STKQUANTITY'] = wset_fund_holding['F_PRT_STKQUANTITY'] / 10000  # 万股
        wset_fund_holding['STOCK_PER'] = wset_fund_holding['STOCK_PER'] / 100
        wset_fund_holding['F_PRT_STKVALUETONAV'] = wset_fund_holding['F_PRT_STKVALUETONAV'] / 100

    elif data_mode == 'DF':
        fund_code = list(map(lambda x: x.replace(".OF", "").replace(".SH", "").replace(".SZ", ""), fund_code))
        dataframe['tempcol'] = dataframe.F_INFO_WINDCODE.str[:6]
        wset_fund_holding = dataframe.query(f" tempcol in {fund_code} and F_PRT_ENDDATE in {list(report_date)}")
        dataframe.drop(columns='tempcol', inplace=True)
        wset_fund_holding.drop(columns='tempcol', inplace=True)

    wset_fund_holding.sort_values(by=['F_INFO_WINDCODE', 'F_PRT_ENDDATE', 'STOCK_PER'], ascending=[True, True, False],
                                  inplace=True)
    wset_fund_holding = wset_fund_holding.groupby(['F_INFO_WINDCODE', 'F_PRT_ENDDATE']).head(
        10) if top10 == True else wset_fund_holding

    wset_fund_holding.reset_index(drop=True, inplace=True)

    wset_fund_summary = wset_fund_holding.groupby(
        ['F_INFO_WINDCODE', 'F_PRT_ENDDATE']).sum() if show_summary == True else None

    return wset_fund_holding, wset_fund_summary


# %% 代码示例

# # 再检查，输出有问题
# stk_holding1, stk_hld1_sum = get_fund_stk_holding(fund_code=['001694.OF', '006567.OF'], start_date="20210101",
#                                                   end_date="20220510",freq="H", top10=True, data_mode='WindAPI')
# stk_holding2, _ = get_fund_stk_holding(fund_code=['001694.OF', '006567.OF'], start_date="20210101", end_date="20220510",
#                                        freq="H", top10=True, data_mode='DB')
# fcodd=list(pd.read_excel('fundID.xlsx')['FundID'])
# stk_holding3, _ = get_fund_stk_holding(fund_code=fcodd, start_date="20180101", end_date="20220510",
#                                        freq="H", top10=False, data_mode='DB')
# # DF模式，从DB模式取出的较大数据源里取子集
# stk_holding4, _ = get_fund_stk_holding(fund_code=['006345.OF','006385.OF','005117.OF'], start_date="20190101", end_date="20220510",
#                                        freq="H", top10=True, data_mode='DF',dataframe=stk_holding3)

# %% 获取指数日度权重的函数
# 目前DB模式能支持的指数仅有沪深300/中证500/中证800/中证1000/中证100/上证50/申万指数/债券指数等日权重
# WindAPI支持债券指数成份的提取，不支持中债指数成份提取

def get_index_composite(index_code='', start_date="", end_date="", freq="QE", date_list='', data_mode='DB',
                        database_path=path_index,
                        dataframe="", tradeday_list=tradeday_list, show_summary=False):
    if date_list != "":
        report_date = pd.DatetimeIndex(date_list)
        report_date = report_date.strftime('%Y%m%d')
    else:
        report_date = gen_td_series(start_date=start_date, end_date=end_date, freq=freq, tradeday_list=tradeday_list,
                                    opt_type='str')
    if data_mode == 'WindAPI':
        if w.isconnected() == False:  # 判断WindPy是否已经登录成功
            w.start()
        # 单个指数循环提取持仓
        wset_idx_comp = pd.DataFrame()
        if isinstance(index_code, list) == False:
            index_code = [index_code]
        for idx_code_i, report_date_j in product(index_code, report_date):
            # print(idx_code_i,report_date_j)
            wset_obj_ij = w.wset("indexconstituent", f"date={report_date_j};windcode={idx_code_i}",
                                 usedf=True)  # 只能一天一天取，如果当天没有数值，则用最近日数值替代

            if wset_obj_ij[0] == 0:
                wset_idx_comp_ij = wset_obj_ij[1]
                wset_idx_comp_ij.insert(0, 'S_INFO_WINDCODE', idx_code_i)
                wset_idx_comp_ij.insert(1, 'TRADE_DT', report_date_j)
                wset_idx_comp_ij.rename(columns={'date': 'AS_OF_DATE',
                                                 'wind_code': 'S_CON_WINDCODE',
                                                 'sec_name': 'S_INFO_NAME',
                                                 'i_weight': 'WEIGHT',
                                                 'industry': 'WIND_INDUSTRY'}, inplace=True)
                wset_idx_comp_ij['WEIGHT'] = wset_idx_comp_ij['WEIGHT'] / 100
                wset_idx_comp_ij = wset_idx_comp_ij[
                    ['S_INFO_WINDCODE', 'TRADE_DT', 'S_CON_WINDCODE', 'WEIGHT', 'AS_OF_DATE']]
                wset_idx_comp = pd.concat([wset_idx_comp, wset_idx_comp_ij], axis=0)
            else:
                continue
        wset_idx_comp.sort_values(by=['S_INFO_WINDCODE', 'TRADE_DT', 'WEIGHT'], ascending=[True, True, False])

    elif data_mode == 'DB':

        # TODO 检查查询出的TRADE_DT是否包含全部rpt_dates,如果不是，弹出提示或者补全

        index_code = [code.upper() for code in index_code]
        index_list_str = str(index_code)[1:-1]
        rpt_dates_str = str(list(report_date)).replace("'", "").replace(' ', '')[1:-1]
        # 先查沪深300
        query = f"select upper(S_INFO_WINDCODE) as S_INFO_WINDCODE, TRADE_DT,S_CON_WINDCODE,WEIGHT from '沪深300指数成份日权重' " \
                f"where upper(S_INFO_WINDCODE) in ({index_list_str})  and TRADE_DT in ({rpt_dates_str}) " \
                f"order by S_INFO_WINDCODE, TRADE_DT, WEIGHT desc"
        idx_comp1 = Obtain_DBData(query, database_path)
        idx_comp1['WEIGHT'] = idx_comp1['WEIGHT'] / 100

        # 再查询中证500
        index_code_left1 = set(index_code).difference(set(idx_comp1["S_INFO_WINDCODE"]))
        index_list_left_str1 = str(list(index_code_left1))[1:-1]

        query = f"select upper(S_INFO_WINDCODE) as S_INFO_WINDCODE, TRADE_DT,S_CON_WINDCODE,WEIGHT from '中证500指数成份日权重' " \
                f"where upper(S_INFO_WINDCODE) in ({index_list_left_str1})  and TRADE_DT in ({rpt_dates_str}) " \
                f"order by S_INFO_WINDCODE, TRADE_DT, WEIGHT desc"
        idx_comp2 = Obtain_DBData(query, database_path)
        idx_comp2['WEIGHT'] = idx_comp2['WEIGHT'] / 100

        # 再查询中证800
        index_code_left2 = set(index_code_left1).difference(set(idx_comp2["S_INFO_WINDCODE"]))
        index_list_left_str2 = str(list(index_code_left2))[1:-1]

        query = f"select upper(S_INFO_WINDCODE) as S_INFO_WINDCODE, TRADE_DT,S_CON_WINDCODE,WEIGHT from '中证800指数成份日权重' " \
                f"where upper(S_INFO_WINDCODE) in ({index_list_left_str2})  and TRADE_DT in ({rpt_dates_str}) " \
                f"order by S_INFO_WINDCODE, TRADE_DT, WEIGHT desc"
        idx_comp3 = Obtain_DBData(query, database_path)
        idx_comp3['WEIGHT'] = idx_comp3['WEIGHT'] / 100

        # 再查询中证1000
        index_code_left3 = set(index_code_left2).difference(set(idx_comp3["S_INFO_WINDCODE"]))
        index_list_left_str3 = str(list(index_code_left3))[1:-1]

        query = f"select upper(S_INFO_WINDCODE) as S_INFO_WINDCODE, TRADE_DT,S_CON_WINDCODE,WEIGHT from '中证1000指数成份日权重' " \
                f"where upper(S_INFO_WINDCODE) in ({index_list_left_str3})  and TRADE_DT in ({rpt_dates_str}) " \
                f"order by S_INFO_WINDCODE, TRADE_DT, WEIGHT desc"
        idx_comp4 = Obtain_DBData(query, database_path)
        idx_comp4['WEIGHT'] = idx_comp4['WEIGHT'] / 100

        # 再查询中证100
        index_code_left4 = set(index_code_left3).difference(set(idx_comp4["S_INFO_WINDCODE"]))
        index_list_left_str4 = str(list(index_code_left4))[1:-1]

        query = f"select upper(S_INFO_WINDCODE) as S_INFO_WINDCODE, TRADE_DT,S_CON_WINDCODE,WEIGHT from '中证100指数成份日权重' " \
                f"where upper(S_INFO_WINDCODE) in ({index_list_left_str4})  and TRADE_DT in ({rpt_dates_str}) " \
                f"order by S_INFO_WINDCODE, TRADE_DT, WEIGHT desc"
        idx_comp5 = Obtain_DBData(query, database_path)
        idx_comp5['WEIGHT'] = idx_comp5['WEIGHT'] / 100

        # 再查询上证50
        index_code_left5 = set(index_code_left4).difference(set(idx_comp5["S_INFO_WINDCODE"]))
        index_list_left_str5 = str(list(index_code_left5))[1:-1]

        query = f"select upper(S_INFO_WINDCODE) as S_INFO_WINDCODE, TRADE_DT,S_CON_WINDCODE,WEIGHT from '上证50指数成份日权重' " \
                f"where upper(S_INFO_WINDCODE) in ({index_list_left_str5})  and TRADE_DT in ({rpt_dates_str}) " \
                f"order by S_INFO_WINDCODE, TRADE_DT, WEIGHT desc"
        idx_comp6 = Obtain_DBData(query, database_path)
        idx_comp6['WEIGHT'] = idx_comp6['WEIGHT'] / 100

        # 再查询申万行业指数
        index_code_left6 = set(index_code_left5).difference(set(idx_comp6["S_INFO_WINDCODE"]))
        index_list_left_str6 = str(list(index_code_left6))[1:-1]

        query = f"select upper(S_INFO_WINDCODE) as S_INFO_WINDCODE, TRADE_DT,S_CON_WINDCODE,WEIGHT from '申万指数成份日权重' " \
                f"where upper(S_INFO_WINDCODE) in ({index_list_left_str6})  and TRADE_DT in ({rpt_dates_str}) " \
                f"order by S_INFO_WINDCODE, TRADE_DT, WEIGHT desc"
        idx_comp7 = Obtain_DBData(query, database_path)
        idx_comp7['WEIGHT'] = idx_comp7['WEIGHT'] / 100

        index_code_left7 = set(index_code_left6).difference(set(idx_comp7["S_INFO_WINDCODE"]))

        if index_code_left7 == set():
            print('指数数据查询完毕')
        else:
            print(f"{index_code_left7}没有查询到指数价格数据！")

        wset_idx_comp = pd.concat([idx_comp1, idx_comp2, idx_comp3, idx_comp4, idx_comp5, idx_comp6, idx_comp7])

    elif data_mode == 'DF':
        index_code = [code.upper() for code in index_code]
        wset_idx_comp = pd.DataFrame()
        wset_idx_comp = dataframe.query(f"S_INFO_WINDCODE in {index_code} and TRADE_DT in {list(report_date)}")

    wset_idx_comp.reset_index(drop=True, inplace=True)

    wset_idx_comp=wset_idx_comp[['S_INFO_WINDCODE', 'TRADE_DT', 'S_CON_WINDCODE', 'WEIGHT']] # 仅保留前四列，剔除AS_OF_DATE

    wset_idx_summary = wset_idx_comp.groupby(['S_INFO_WINDCODE', 'TRADE_DT']).agg(
        {'WEIGHT': ['count', 'sum']}) if show_summary == True else None

    return wset_idx_comp, wset_idx_summary


# %% 代码示例
# # DB模式取数
# idx_comp1, idx_summary1 = get_index_composite(
#     index_code=['000300.SH', '000905.SH', '000906.SH', '000852.SH', '000903.SH', '000016.SH', '801780.SI'],
#     start_date="20220301", end_date="20220401", freq="D", data_mode='DB',
#     database_path=path_index, dataframe="", tradeday_list=tradeday_list, show_summary=True)
# idx_summary1
# # DB取数结果应用到DF上
# idx_comp2, idx_summary2 = get_index_composite(
#     index_code=['000300.SH', '000905.SH'], date_list=['20220301', '20220302', '20220303', '20220304'], data_mode='DF',
#     dataframe=idx_comp1, tradeday_list=tradeday_list, show_summary=True)
# idx_summary2
# # WindAPI模式取数
# idx_comp3, idx_summary3 = get_index_composite(
#     index_code=['000300.SH'],
#     start_date="20220301", end_date="20220305", freq="D", data_mode='WindAPI',
#     database_path=path_index, dataframe="", tradeday_list=tradeday_list, show_summary=True)
# idx_summary3


# %% 计算证券涨跌幅函数(TODO 支持股票、指数、基金，暂不支持转债，DB模式暂时不支持美股）
# start_day=end_day 就是当日涨跌幅
# 支持批量输入资产代码，批量输出
# start_date 为区间首个交易日前收盘价
# end_date 为区间最后交易日收盘价
def get_price_chg(stock_code="", index_code="", fund_code="", start_date="", end_date="", data_mode='WindAPI',
                  database_path=[path_stock, path_index, path_fund], dataframe="", IPO_day_consider=True):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    if data_mode == 'WindAPI':
        if w.isconnected() == False:  # 判断WindPy是否已经登录成功
            w.start()
        # Stock和Index合并提取，统称为asset
        if stock_code != "" and index_code != "":
            asset_code = stock_code + index_code
        elif stock_code == "":
            asset_code = index_code
        elif index_code == "":
            asset_code = stock_code
        # pct_chg_per2包含上市首日涨跌幅,pct_chg_per不包含上市首日涨跌幅
        if IPO_day_consider == True:
            asset_price_chg = w.wss(asset_code, "pct_chg_per2",
                                    f"startDate={start_date.strftime('%Y%m%d')};endDate={end_date.strftime('%Y%m%d')}")
        else:
            asset_price_chg = w.wss(asset_code, "pct_chg_per",
                                    f"startDate={start_date.strftime('%Y%m%d')};endDate={end_date.strftime('%Y%m%d')}")

        fund_price_chg = w.wss(fund_code, "NAV_adj_return",
                               f"startDate={start_date.strftime('%Y%m%d')};endDate={end_date.strftime('%Y%m%d')}")
        # TODO 如果fund_price_chg 提取出来为NA，应区分是基金没成立还是区间不包含任何交易日，前者NA，后者0
        asset_chg_df = pd.DataFrame({"S_INFO_WINDCODE": asset_price_chg.Codes,
                                     "S_DQ_PCTCHANGE": asset_price_chg.Data[
                                         0]}) if asset_price_chg.ErrorCode == 0 else pd.DataFrame()
        fund_chg_df = pd.DataFrame({"S_INFO_WINDCODE": fund_price_chg.Codes,
                                    "S_DQ_PCTCHANGE": fund_price_chg.Data[0]
                                    }) if fund_price_chg.ErrorCode == 0 else pd.DataFrame()
        chg_df_total = pd.concat([asset_chg_df, fund_chg_df], axis=0)
        chg_df_total["S_DQ_PCTCHANGE"] = chg_df_total.S_DQ_PCTCHANGE / 100
    if data_mode == 'DB':
        if IPO_day_consider == True:
            # 基于Wind数据库S_DQ_PCTCHANGE序列的算法
            asset_series_df = fetch_asset_series(stock_code=stock_code, index_code=index_code, fund_code=fund_code,
                                                 start_date=fstartday(start_date, shift_length='1m'), end_date=end_date,
                                                 data_mode=data_mode, database_path=database_path,
                                                 tradeday_list=tradeday_list, censor_rebase=False, to_wide=True,
                                                 show_wide='pct_chg')  # index是DatetimeIndex
            asset_series_df_final = asset_series_df.loc[start_date:end_date, :]
            chg_df_total = pd.DataFrame()
            if asset_series_df_final.empty == True:
                chg_df_total["S_INFO_WINDCODE"] = asset_series_df.columns
                chg_df_total["S_DQ_PCTCHANGE"] = 0.0
            else:
                chg_df_total["S_DQ_PCTCHANGE"] = ((asset_series_df_final + 1).cumprod() - 1).fillna(
                    method='ffill').tail(1).T.iloc[:, 0]
                chg_df_total.reset_index(inplace=True)
        elif IPO_day_consider == False:
            # 基于资产价格序列的算法
            asset_series_df = fetch_asset_series(stock_code=stock_code, index_code=index_code, fund_code=fund_code,
                                                 start_date=fstartday(start_date, shift_length='1m'), end_date=end_date,
                                                 data_mode=data_mode, database_path=database_path,
                                                 tradeday_list=tradeday_list, censor_rebase=False,
                                                 to_wide=True)  # index是DatetimeIndex
            if asset_series_df.loc[start_date:end_date, :].empty == True:
                chg_df_total["S_INFO_WINDCODE"] = asset_series_df.columns
                chg_df_total["S_DQ_PCTCHANGE"] = 0.0
            else:
                first_day = asset_series_df.loc[start_date:end_date, :].index[0]  # 区间首个共同交易日
                zero_day = asset_series_df.index[asset_series_df.index.get_loc(first_day) - 1]  # 区间首个共同交易日前一交易日
                last_day = asset_series_df.loc[start_date:end_date, :].index[-1]  # 区间最后共同交易日
                last_day_close = asset_series_df.loc[last_day, :]
                zero_day_close = asset_series_df.loc[zero_day, :]
                if np.any(np.isnan(zero_day_close)) == True:
                    print('区间首个共同交易日前一交易日有资产价格为空')
                if np.any(np.isnan(last_day_close)) == True:
                    print('区间最后共同交易日有资产价格为空')
                asset_series_df_final = asset_series_df.loc[zero_day:last_day, :].fillna(method='bfill')
                chg_df_total = pd.DataFrame()
                chg_df_total["S_DQ_PCTCHANGE"] = asset_series_df_final.tail(1).T.iloc[:, 0] / (
                    asset_series_df_final.head(1).T.iloc[:, 0]) - 1
                chg_df_total.reset_index(inplace=True)

    if data_mode == 'DF':
        fund_code_trim = list(map(lambda x: x.replace(".OF", "").replace(".SH", "").replace(".SZ", ""), fund_code))
        stock_code_lst = list() if stock_code == "" else stock_code
        index_code_lst = list() if index_code == "" else index_code
        fund_code_trim_lst = fund_code_trim

        asset_series_df_long = dataframe[
            dataframe.S_INFO_WINDCODE.isin(stock_code_lst) | dataframe.S_INFO_WINDCODE.isin(
                index_code_lst) | dataframe.S_INFO_WINDCODE.str[:6].isin(fund_code_trim_lst)]
        asset_series_df_long['TRADE_DT'] = pd.DatetimeIndex(asset_series_df_long.TRADE_DT)
        if IPO_day_consider == True:
            # 基于Wind数据库S_DQ_PCTCHANGE序列的算法
            asset_series_df = asset_series_df_long.pivot(index='TRADE_DT', columns='S_INFO_WINDCODE',
                                                         values='S_DQ_PCTCHANGE')  # pct_chg不能做填充操作
            asset_series_df_final = asset_series_df.loc[start_date:end_date, :]
            chg_df_total = pd.DataFrame()
            if asset_series_df_final.empty == True:
                chg_df_total["S_INFO_WINDCODE"] = asset_series_df.columns
                chg_df_total["S_DQ_PCTCHANGE"] = 0.0
            else:
                chg_df_total["S_DQ_PCTCHANGE"] = ((asset_series_df_final + 1).cumprod() - 1).fillna(
                    method='ffill').tail(1).T.iloc[:, 0]
                chg_df_total.reset_index(inplace=True)
        elif IPO_day_consider == False:
            # 基于资产价格序列的算法
            asset_series_df = asset_series_df_long.pivot(index='TRADE_DT', columns='S_INFO_WINDCODE',
                                                         values='S_DQ_ADJCLOSE').fillna(
                method='ffill')  # 向下填充空值，若下一交易日没有行情，则沿用上一日行情

            if asset_series_df.loc[start_date:end_date, :].empty == True:
                chg_df_total["S_INFO_WINDCODE"] = asset_series_df.columns
                chg_df_total["S_DQ_PCTCHANGE"] = 0.0
            else:
                first_day = asset_series_df.loc[start_date:end_date, :].index[0]  # 区间首个共同交易日
                zero_day = asset_series_df.index[asset_series_df.index.get_loc(first_day) - 1]  # 区间首个共同交易日前一交易日
                last_day = asset_series_df.loc[start_date:end_date, :].index[-1]  # 区间最后共同交易日
                last_day_close = asset_series_df.loc[last_day, :]
                zero_day_close = asset_series_df.loc[zero_day, :]
                if np.any(np.isnan(zero_day_close)) == True:
                    print('区间首个共同交易日前一交易日有资产价格为空')
                if np.any(np.isnan(last_day_close)) == True:
                    print('区间最后共同交易日有资产价格为空')
                asset_series_df_final = asset_series_df.loc[zero_day:last_day, :].fillna(method='bfill')
                chg_df_total = pd.DataFrame()
                chg_df_total["S_DQ_PCTCHANGE"] = asset_series_df_final.tail(1).T.iloc[:, 0] / (
                    asset_series_df_final.head(1).T.iloc[:, 0]) - 1
                chg_df_total.reset_index(inplace=True)

    chg_df_total.sort_values(by='S_INFO_WINDCODE', inplace=True)  # 最后对指数排序
    chg_df_total.reset_index(inplace=True, drop=True)

    return chg_df_total


# %% 代码示例

# # 301106.SZ 为新股，测试是否考虑新股首日涨幅
# priceA1 = get_price_chg(stock_code=["000007.SZ", "000009.SZ", "0005.HK", "600519.SH","301106.SZ"], index_code=["000300.SH"],
#                        fund_code=["000471.OF"], start_date="20220103", end_date="20220310", data_mode='WindAPI',IPO_day_consider=True)
# priceA2 = get_price_chg(stock_code=["000007.SZ", "000009.SZ", "0005.HK", "600519.SH","301106.SZ"], index_code=["000300.SH"],
#                        fund_code=["000471.OF"], start_date="20220103", end_date="20220310", data_mode='WindAPI',IPO_day_consider=False)
# #
# priceB1 = get_price_chg(stock_code=["000007.SZ", "000009.SZ", "0005.HK", "600519.SH","301106.SZ"], index_code=["000300.SH"],
#                        fund_code=["000471.OF"], start_date="20220103", end_date="20220310", data_mode='DB',IPO_day_consider=True)
# priceB2 = get_price_chg(stock_code=["000007.SZ", "000009.SZ", "0005.HK", "600519.SH","301106.SZ"], index_code=["000300.SH"],
#                        fund_code=["000471.OF"], start_date="20220103", end_date="20220310", data_mode='DB',IPO_day_consider=False)
# # 获取当日涨跌幅(公共非交易日)
# priceC1 = get_price_chg(stock_code=["000007.SZ", "000009.SZ", "0005.HK", "600519.SH","301106.SZ"], index_code=["000300.SH"],
#                        fund_code=["000471.OF"], start_date="20220101", end_date="20220101", data_mode='WindAPI')
# priceC2 = get_price_chg(stock_code=["000007.SZ", "000009.SZ", "0005.HK", "600519.SH","301106.SZ"], index_code=["000300.SH"],
#                        fund_code=["000471.OF"], start_date="20220101", end_date="20220101", data_mode='DB')
# DF模式 如果dataframe没有某资产净值，则函数无法计算价格变动，同时不会弹出提示
# dataframe = fetch_asset_series(stock_code=["000007.SZ", "000009.SZ", "0005.HK", "600519.SH", "301106.SZ"],
#                                index_code=["000300.SH"], fund_code=["161005.OF"],
#                                start_date='20150101', end_date='20220310',
#                                data_mode='DB', database_path=[path_stock, path_index, path_fund],
#                                tradeday_list=tradeday_list, censor_rebase=False, to_wide=False) # 先把所有可能涉及到的资产提取出净值
# priceD1 = get_price_chg(stock_code=["0005.HK", "600519.SH","301106.SZ"], index_code=["000300.SH"],
#                        fund_code=["000471.OF"], start_date="20220101", end_date="20220130", data_mode='DF',dataframe=dataframe)
# priceD2 = get_price_chg(stock_code=["0005.HK", "600519.SH","301106.SZ"], index_code="",
#                        fund_code="", start_date="20220101", end_date="20220130", data_mode='DF',dataframe=dataframe)

# priceB1 = get_price_chg(stock_code=["605286.SH"], index_code="",
#                        fund_code="", start_date="20210323", end_date="20210325", data_mode='DB',IPO_day_consider=True)
# %% 查询行业分类函数
# 支持行业分类标准SW2014/SW2021/CITIC/Wind
# 由于港股数据库不全，当选取DB数据源时，港股先调用WindAPI接口查询
# holding_df格式要求: 第一列日期，第二列股票代码!
# holding_df 日期必须是字符串格式
# TODO 为了提高行业搜索速度，增加获取最新行业的参数，CUR_SIGN==1

def get_industry(holding_df="", ind_class='SW', level=1, AH_comb=True, datamode='WindAPI', database_path=path_stock,
                 dataframe=""):
    def combine_name(row_item):
        if row_item[1] != None:
            name = row_item[1]
        elif row_item[3] != None:
            name = row_item[3]
        else:
            name = '其他'
        return name

    def combine_code(row_item):
        if row_item[2] != None:
            code = row_item[2]
        elif row_item[4] != None:
            code = row_item[4]
        else:
            code = '其他'
        return code

    def match_ind(dt_stk):
        temp = ind_hist_df.loc[(ind_hist_df['S_INFO_WINDCODE'] == dt_stk[1]) & (ind_hist_df['ENTRY_DT'] <= dt_stk[0])
                               & ((ind_hist_df['REMOVE_DT'] > dt_stk[0]) | (ind_hist_df['REMOVE_DT'].isnull())),
                               'INDUSTRIESNAME']
        temp = None if temp.empty == True else temp.to_list()[0]
        return temp

    # 判定holding_df第一列数据类型
    holding_df_org_dtype = holding_df.dtypes[0]  # 记录原始dtype
    # 将第一列日期强制转化成字符串格式，便于后续处理
    if holding_df.dtypes[0] == 'datetime64[ns]':
        holding_df.iloc[:, 0] = holding_df.iloc[:, 0].dt.strftime('%Y%m%d')
    elif holding_df.dtypes[0] == 'object':
        holding_df = holding_df
    else:
        print('检查holding_df日期数据格式')

    holding_df_unique = holding_df.drop_duplicates()  # 提取不重复的股票代码和日期组合，WindAPI不接受重复代码
    holding_df_unique.columns = ['TRADE_DT', 'STOCK_CODE']  # 重命列名使得代码一致性
    td_list = list(holding_df_unique.TRADE_DT.drop_duplicates())

    if datamode == "WindAPI":
        ind_class_df = pd.DataFrame()
        if w.isconnected() == False:  # 判断WindPy是否已经登录成功
            w.start()
        for td in td_list:
            stock_code = list(holding_df_unique.loc[holding_df_unique.TRADE_DT == td].STOCK_CODE)
            stock_list_str = str(list(stock_code)).replace("'", "").replace(' ', '')[1:-1]
            if ind_class == 'SW':
                ind_class_obj_i = w.wss(f"{stock_list_str}",
                                        "industry_sw,industry_swcode,industry_sw_hk,industry_swcode_hk",
                                        f"industryType={level};tradeDate={td}", usedf=True)  # 存在部分记录匹配出Name但未匹配出Code
            elif ind_class == 'SW2021':
                ind_class_obj_i = w.wss(f"{stock_list_str}",
                                        "industry_sw_2021,industry_swcode_2021,industry_sw_2021_hk,industry_swcode_2021_hk",
                                        f"tradeDate={td};industryType={level}", usedf=True)  # 2021年7月前部分股票没有新版申万分类
            elif ind_class == 'CITIC':
                ind_class_obj_i = w.wss(f"{stock_list_str}",
                                        "industry_citic,industry_citiccode,industry_citic_hk,industry_citiccode_hk",
                                        f"tradeDate={td};industryType={level}", usedf=True)  # 存在部分记录匹配出Name但未匹配出Code
            elif ind_class == 'Wind':
                ind_class_obj_i = w.wss(f"{stock_list_str}", "industry_gics,industry_gicscode",
                                        f"tradeDate={td};industryType={level}", usedf=True)  #
            # elif ind_class == 'Wind_Theme':
            #     ind_class_obj_i = w.wss(f"{stock_list_str}", "thematicindustry_wind,indexcode_windthematic",
            #                             f"tradeDate={td};industryType={level}", usedf=True)  #
            if ind_class_obj_i[0] != 0:
                ind_class_df_i = None
                print(f'日期{td}未提取出{ind_class}行业代码!')
            else:
                ind_class_df_i = ind_class_obj_i[1]
                ind_class_df_i.insert(0, 'TRADE_DT', td)
            ind_class_df = pd.concat([ind_class_df, ind_class_df_i])
        if ind_class in ['SW', 'SW2021', 'CITIC']:
            ind_class_df['INDUSTRY_NAME'] = ind_class_df.apply(combine_name, axis=1)
            ind_class_df['INDUSTRY_CODE'] = ind_class_df.apply(combine_code, axis=1)
        elif ind_class == 'Wind':
            ind_class_df.rename(columns={'INDUSTRY_GICS': 'INDUSTRY_NAME',
                                         'INDUSTRY_GICSCODE': 'INDUSTRY_CODE'}, inplace=True)

        ind_class_df['S_INFO_WINDCODE'] = ind_class_df.index
        ind_class_df.reset_index(drop=True, inplace=True)
        ind_class_df = ind_class_df[['TRADE_DT', 'S_INFO_WINDCODE', 'INDUSTRY_NAME', 'INDUSTRY_CODE']]

    elif datamode == "DB":
        stock_code = list(set(holding_df_unique.STOCK_CODE))
        stock_list_str = str(stock_code)[1:-1]

        if ind_class == 'SW':
            level_num = level + 1
            code_len = 2 * level_num  # 1级行业截取4位长度，2级行业截取6位，3级行业截取8位
            query = f"select a.S_INFO_WINDCODE, a.SW_IND_CODE,a.ENTRY_DT,a.REMOVE_DT,a.CUR_SIGN, b.INDUSTRIESNAME " \
                    f"from '申万行业分类(2014版)' as a, '行业代码' as b " \
                    f"where S_INFO_WINDCODE in ({stock_list_str})" \
                    f"and substr(a.SW_IND_CODE, 1, {code_len}) = substr(b.INDUSTRIESCODE, 1, {code_len}) " \
                    f"and b.levelnum = '{level_num}' --2表示1级，3表示2级，4表示3级"
            ind_hist_df = Obtain_DBData(query, database_path)

            # holding_df_unique['INDUSTRY_NAME'] = holding_df_unique.apply(match_ind, axis=1)
            # holding_df_unique['INDUSTRY_NAME'] = holding_df_unique.swifter.apply(match_ind, axis=1)
            holding_df_unique['INDUSTRY_NAME'] = holding_df_unique.swifter.apply(match_ind, axis=1)
            holding_df_unique['INDUSTRY_CODE'] = None  # DF模式暂时先不匹配行业代码
            ind_class_df_matched = holding_df_unique[holding_df_unique['INDUSTRY_NAME'].notnull()]

            # 查询出的结果可能是非A股，也可能是没找到行业名称的A股(如新股）
            ind_class_df_left = holding_df_unique[holding_df_unique['INDUSTRY_NAME'].isnull()][
                ['TRADE_DT', 'STOCK_CODE']]
            if ind_class_df_left.empty == True:
                ind_class_df_left = None
            else:
                # 由于数据库不全，港股先调用WindAPI接口查询
                if w.isconnected() == False:
                    w.start()
                ind_class_df_left = get_industry(holding_df=ind_class_df_left, ind_class=ind_class, level=level,
                                                 AH_comb=False, datamode='WindAPI')
            ind_class_df = pd.concat([ind_class_df_matched, ind_class_df_left])
            ind_class_df.columns = ['TRADE_DT', 'S_INFO_WINDCODE', 'INDUSTRY_NAME', 'INDUSTRY_CODE']
        elif ind_class == 'SW2021':
            # ind_class='SW2021'
            level_num = level + 1
            code_len = 2 * level_num  # 1级行业截取4位长度，2级行业截取6位，3级行业截取8位
            query = f"select a.S_INFO_WINDCODE, a.SW_IND_CODE,a.ENTRY_DT,a.REMOVE_DT,a.CUR_SIGN, b.INDUSTRIESNAME " \
                    f"from '申万行业分类(2021版)' as a, '行业代码' as b " \
                    f"where S_INFO_WINDCODE in ({stock_list_str})" \
                    f"and substr(a.SW_IND_CODE, 1, {code_len}) = substr(b.INDUSTRIESCODE, 1, {code_len}) " \
                    f"and b.levelnum = '{level_num}' --2表示1级，3表示2级，4表示3级"
            ind_hist_df = Obtain_DBData(query, database_path)

            holding_df_unique['INDUSTRY_NAME'] = holding_df_unique.swifter.apply(match_ind, axis=1)
            holding_df_unique['INDUSTRY_CODE'] = None  # DF模式暂时先不匹配行业代码
            ind_class_df_matched = holding_df_unique[holding_df_unique['INDUSTRY_NAME'].notnull()]
            # 查询出的结果可能是非A股，也可能是A股，但是没找到行业名称
            ind_class_df_left = holding_df_unique[holding_df_unique['INDUSTRY_NAME'].isnull()][
                ['TRADE_DT', 'STOCK_CODE']]
            if ind_class_df_left.empty == True:
                ind_class_df_left = None
            else:
                # 由于数据库不全，港股先调用WindAPI接口查询
                if w.isconnected() == False:  # 判断WindPy是否已经登录成功
                    w.start()
                ind_class_df_left = get_industry(holding_df=ind_class_df_left, ind_class=ind_class, level=level,
                                                 AH_comb=False, datamode='WindAPI')

            ind_class_df = pd.concat([ind_class_df_matched, ind_class_df_left])
            ind_class_df.columns = ['TRADE_DT', 'S_INFO_WINDCODE', 'INDUSTRY_NAME', 'INDUSTRY_CODE']
        elif ind_class == 'CITIC':
            # ind_class = 'CITIC'
            level_num = level + 1
            code_len = 2 * level_num  # 1级行业截取4位长度，2级行业截取6位，3级行业截取8位
            query = f"select a.S_INFO_WINDCODE, a.CITICS_IND_CODE,a.ENTRY_DT,a.REMOVE_DT,a.CUR_SIGN, b.INDUSTRIESNAME " \
                    f"from '中信行业分类' as a, '行业代码' as b " \
                    f"where S_INFO_WINDCODE in ({stock_list_str})" \
                    f"and substr(a.CITICS_IND_CODE, 1, {code_len}) = substr(b.INDUSTRIESCODE, 1, {code_len}) " \
                    f"and b.levelnum = '{level_num}' --2表示1级，3表示2级，4表示3级"
            ind_hist_df = Obtain_DBData(query, database_path)

            holding_df_unique['INDUSTRY_NAME'] = holding_df_unique.swifter.apply(match_ind, axis=1)
            holding_df_unique['INDUSTRY_CODE'] = None  # DF模式暂时先不匹配行业代码
            ind_class_df_matched = holding_df_unique[holding_df_unique['INDUSTRY_NAME'].notnull()]
            # 查询出的结果可能是非A股，也可能是A股，但是没找到行业名称
            ind_class_df_left = holding_df_unique[holding_df_unique['INDUSTRY_NAME'].isnull()][
                ['TRADE_DT', 'STOCK_CODE']]
            # 由于数据库不全，港股先调用WindAPI接口查询
            if ind_class_df_left.empty == True:
                ind_class_df_left = None
            else:
                if w.isconnected() == False:  # 判断WindPy是否已经登录成功
                    w.start()
                ind_class_df_left = get_industry(holding_df=ind_class_df_left, ind_class=ind_class, level=level,
                                                 AH_comb=False, datamode='WindAPI')

            ind_class_df = pd.concat([ind_class_df_matched, ind_class_df_left])
            ind_class_df.columns = ['TRADE_DT', 'S_INFO_WINDCODE', 'INDUSTRY_NAME', 'INDUSTRY_CODE']
        elif ind_class == 'Wind':
            # ind_class = 'Wind'
            level_num = level + 1
            code_len = 2 * level_num  # 1级行业截取4位长度，2级行业截取6位，3级行业截取8位
            query = f"select a.S_INFO_WINDCODE, a.WIND_IND_CODE,a.ENTRY_DT,a.REMOVE_DT,a.CUR_SIGN, b.INDUSTRIESNAME " \
                    f"from 'Wind行业分类' as a, '行业代码' as b " \
                    f"where S_INFO_WINDCODE in ({stock_list_str})" \
                    f"and substr(a.WIND_IND_CODE, 1, {code_len}) = substr(b.INDUSTRIESCODE, 1, {code_len}) " \
                    f"and b.levelnum = '{level_num}' --2表示1级，3表示2级，4表示3级"
            ind_hist_df = Obtain_DBData(query, database_path)

            holding_df_unique['INDUSTRY_NAME'] = holding_df_unique.swifter.apply(match_ind, axis=1)
            holding_df_unique['INDUSTRY_CODE'] = None  # DF模式暂时先不匹配行业代码
            ind_class_df_matched = holding_df_unique[holding_df_unique['INDUSTRY_NAME'].notnull()]
            # 查询出的结果可能是非A股，也可能是A股，但是没找到行业名称
            ind_class_df_left = holding_df_unique[holding_df_unique['INDUSTRY_NAME'].isnull()][
                ['TRADE_DT', 'STOCK_CODE']]
            if ind_class_df_left.empty == True:
                ind_class_df_left = None
            else:
                # 港股从Wind港股行业分类数据库查询
                stock_list_str_left = str(list(set(ind_class_df_left.STOCK_CODE)))[1:-1]
                query = f"select a.S_INFO_WINDCODE, a.WIND_IND_CODE,a.ENTRY_DT,a.REMOVE_DT,a.CUR_SIGN, b.INDUSTRIESNAME " \
                        f"from '香港股票Wind行业分类' as a, '行业代码' as b " \
                        f"where S_INFO_WINDCODE in ({stock_list_str_left})" \
                        f"and substr(a.WIND_IND_CODE, 1, {code_len}) = substr(b.INDUSTRIESCODE, 1, {code_len}) " \
                        f"and b.levelnum = '{level_num}' --2表示1级，3表示2级，4表示3级"
                ind_hist_df = Obtain_DBData(query, database_path)
                ind_class_df_left['INDUSTRY_NAME'] = ind_class_df_left.apply(match_ind, axis=1)
                ind_class_df_left['INDUSTRY_CODE'] = None  # DF模式暂时先不匹配行业代码

            ind_class_df = pd.concat([ind_class_df_matched, ind_class_df_left])
            ind_class_df.columns = ['TRADE_DT', 'S_INFO_WINDCODE', 'INDUSTRY_NAME', 'INDUSTRY_CODE']
            ind_class_df["INDUSTRY_NAME"].fillna(value='其他', inplace=True)  # 最后未匹配的行业名称归类到其他

    elif datamode == 'DF':
        # 1. 获取holdingdf持仓和日期
        # 2. 在dataframe中query对应的行业名称和行业代码
        # 3. 整理数据，输出
        stock_code = list(set(holding_df_unique.STOCK_CODE))
        report_date = list(set(holding_df_unique.TRADE_DT))

        ind_class_df = dataframe.query(
            f" {dataframe.columns[1]} in {stock_code} and {dataframe.columns[0]}  in {report_date}")

    if AH_comb == True:
        ind_class_df['INDUSTRY_NAME'] = ind_class_df['INDUSTRY_NAME'].apply(
            lambda x: re.sub(r"\(.*?\)|\{.*?\}|\[.*?\]", "", x))

    ind_class_df.drop_duplicates(inplace=True)
    ind_class_df.rename(columns={'S_INFO_WINDCODE': holding_df.columns[1],
                                 'TRADE_DT': holding_df.columns[0]}, inplace=True)

    # 将ind_class_df第一列日期强制转化成字符串格式，便于merge
    if ind_class_df.dtypes[0] == 'datetime64[ns]':
        ind_class_df.iloc[:, 0] = ind_class_df.iloc[:, 0].dt.strftime('%Y%m%d')
    elif ind_class_df.dtypes[0] == 'object':
        ind_class_df = ind_class_df
    else:
        print('检查ind_class_df日期数据格式')

    holding_df = pd.merge(holding_df, ind_class_df, on=[holding_df.columns[0], holding_df.columns[1]], how='left')

    # 将数据类型转化为原本数据类型
    holding_df.iloc[:, 0] = holding_df.iloc[:, 0].astype(holding_df_org_dtype)

    return holding_df


# %% 函数示例
# stk_holding1, stk_hld1_sum = get_fund_stk_holding(fund_code=['001694.OF', '006567.OF'], start_date="20210101",
#                                                   end_date="20220510", freq="H", top10=False, data_mode='DB')
# holding_df_obj = stk_holding1[['F_PRT_ENDDATE', 'S_INFO_STOCKWINDCODE']]
# holding_df_with_ind1 = get_industry(holding_df=holding_df_obj, ind_class='SW', level=1, AH_comb=False,
#                                     datamode='WindAPI')
# holding_df_with_ind2 = get_industry(holding_df=holding_df_obj, ind_class='SW', level=1, AH_comb=False, datamode='DB')
# holding_df_with_ind3 = get_industry(holding_df=holding_df_obj, ind_class='CITIC', level=2, AH_comb=False, datamode='DB')
# holding_df_with_ind4 = get_industry(holding_df=holding_df_obj, ind_class='Wind', level=3, AH_comb=False, datamode='DB')
# #DF模式,先生成一个大的数据集，再从中提取小的数据集
# holding_df_obj_subset=holding_df_obj.sample(20)
# holding_df_with_ind5 = get_industry(holding_df=holding_df_obj_subset, AH_comb=False, datamode='DF', dataframe=holding_df_with_ind2)

# %% Brinson归因
# datamode对应一个三维数组，分别为行情取数模式基准取数模式和行业取数模式
# database_path对应一个三维数组，分别为股票数据库、指数数据库和基金数据库位置
# dataframe对应一个三维数组，分别为行情dataframe、基准成份dataframe、行业分类dataframe
# method=BHB/BF/BFt(考虑择时收益)
def brinson_analysis(holding_data="", benchmark_code='000300.SH', bm_cash_pct=0, end_date="", method='BF',
                     IR_TREAT_METHOD='toAR', datamode=["", "", ""], database_path=[path_stock, path_index, path_fund],
                     dataframe=['', '', ''], tradeday_list=tradeday_list, ind_class='SW', level=1, AH_comb=False,
                     Find_latest_td=False, **kwargs):
    datamode_price, datamode_bm, datamode_ind = datamode[0], datamode[1], datamode[2]
    path_stock, path_index, path_fund = database_path[0], database_path[1], database_path[2]
    dataframe_price, dataframe_bm, dataframe_ind = dataframe[0], dataframe[1], dataframe[2]
    # 持仓数据预处理
    holding_data.columns = ['HLD_DATE', "STOCK_CODE", "STOCK_PER", "STKVALUETONAV"]  # 重命名

    # 如果该参数为真，则向前找到最近交易日
    if Find_latest_td == True:
        holding_data['HLD_DATE'] = holding_data['HLD_DATE'].apply(
            lambda x: fstartday(x, shift_length='', tradeday=True, tradeday_shift='before'))

    print("持仓数据有重复记录！") if any(holding_data.duplicated()) == True else print("持仓数据检查完毕！")

    holding_data['STOCK_PER'] = holding_data.groupby('HLD_DATE').STOCK_PER.apply(lambda x: x / sum(x))  # 对各期持仓归一化
    # 生成日期映射，holding_days，from_days和to_days建立映射关系
    holding_data['HLD_DATE'] = pd.DatetimeIndex(holding_data['HLD_DATE'])
    holding_days = pd.DatetimeIndex(holding_data['HLD_DATE'].unique())
    from_days = pd.DatetimeIndex(map(lambda x: fendday(x, shift_length='1d', tradeday=True, tradeday_shift='after'),
                                     holding_days))  # 向后找到最近一个A股交易日
    to_days = pd.DatetimeIndex(pd.concat([holding_days[1:].to_series(), pd.DatetimeIndex([end_date]).to_series()]))
    days_match = pd.DataFrame({"HLD_DATE": holding_days, "FROM_DATE": from_days, 'TO_DATE': to_days})
    # 读取基准持仓及数据预处理
    benchmark_data, _ = get_index_composite(
        index_code=[benchmark_code], date_list=list(holding_days), data_mode=datamode_bm,
        dataframe=dataframe_bm, tradeday_list=tradeday_list, show_summary=False)  # 提取基准持仓
    benchmark_data.columns = ['BENCH_CODE', "HLD_DATE", "STOCK_CODE", "STOCK_PER"]
    benchmark_data['STOCK_PER'] = benchmark_data.groupby('HLD_DATE').STOCK_PER.apply(lambda x: x / sum(x))  # 对各期持仓归一化
    benchmark_data['HLD_DATE'] = pd.DatetimeIndex(benchmark_data['HLD_DATE'])
    benchmark_data["STKVALUETONAV"] = (1.0 - bm_cash_pct) * benchmark_data['STOCK_PER']

    # Step 1：计算各期产品持仓收益和基准持仓收益
    print('开始计算各期产品持仓收益和基准持仓收益')
    holding_data = pd.merge(holding_data, days_match, on='HLD_DATE', how="left")
    benchmark_data = pd.merge(benchmark_data, days_match, on='HLD_DATE', how="left")

    holding_return = pd.DataFrame()
    benchmark_return = pd.DataFrame()
    for hd, fd, td in zip(holding_days, from_days, to_days):  # 计算相邻两个持仓日期的收益
        holding_return_i = holding_data.loc[holding_data.HLD_DATE == hd]
        benchmark_return_i = benchmark_data.loc[benchmark_data.HLD_DATE == hd]
        # 持仓和基准统一提取行情数据
        get_return_i = get_price_chg(
            stock_code=list(pd.concat([holding_return_i.STOCK_CODE, benchmark_return_i.STOCK_CODE]).unique()),
            index_code="", fund_code="", start_date=fd, end_date=td, data_mode=datamode_price,
            database_path=database_path, dataframe=dataframe_price)

        holding_return_i = pd.merge(holding_return_i, get_return_i, left_on='STOCK_CODE', right_on='S_INFO_WINDCODE',
                                    how='left')
        benchmark_return_i = pd.merge(benchmark_return_i, get_return_i, left_on='STOCK_CODE',
                                      right_on='S_INFO_WINDCODE', how='left')
        holding_return_i.drop(columns='S_INFO_WINDCODE', inplace=True)
        benchmark_return_i.drop(columns='S_INFO_WINDCODE', inplace=True)

        if np.any(np.isnan(holding_return_i.S_DQ_PCTCHANGE)) == True:  # 打印未计算出收益的记录
            naloc = holding_return_i.S_DQ_PCTCHANGE.copy(deep=True)
            print("持仓数据中以下股票未计算出收益!\n", holding_return_i.iloc[np.where(np.isnan(naloc))[0], :3])
        if np.any(np.isnan(benchmark_return_i.S_DQ_PCTCHANGE)) == True:  # 打印未计算出收益的记录
            naloc = benchmark_return_i.S_DQ_PCTCHANGE.copy(deep=True)
            print("基准数据中以下股票未计算出收益!\n", benchmark_return_i.iloc[np.where(np.isnan(naloc))[0], :4])

        holding_return = pd.concat([holding_return, holding_return_i])
        benchmark_return = pd.concat([benchmark_return, benchmark_return_i])

    holding_return.reset_index(drop=True, inplace=True)
    benchmark_return.reset_index(drop=True, inplace=True)
    # Step 2：产品持仓数据和基准持仓数据匹配行业
    print('开始为持仓匹配行业')
    holding_df_obj = pd.concat(
        [holding_return[['HLD_DATE', 'STOCK_CODE']], benchmark_return[['HLD_DATE', 'STOCK_CODE']]]).drop_duplicates()

    if type(dataframe_ind) != str:
        if dataframe_ind.empty == False:  # 做个日期转化处理
            dataframe_ind['HLD_DATE'] = pd.DatetimeIndex(dataframe_ind['HLD_DATE'])
        else:
            print('检查dataframe_ind列名称或数据格式！')

    holding_df_with_ind = get_industry(holding_df=holding_df_obj, ind_class=ind_class, level=level, AH_comb=AH_comb,
                                       datamode=datamode_ind, dataframe=dataframe_ind, database_path=path_stock)[
        ['HLD_DATE', 'STOCK_CODE', 'INDUSTRY_NAME']]
    holding_df_with_ind['HLD_DATE'] = pd.DatetimeIndex(holding_df_with_ind['HLD_DATE'])

    holding_return = pd.merge(holding_return, holding_df_with_ind, on=['HLD_DATE', 'STOCK_CODE'], how='left')
    benchmark_return = pd.merge(benchmark_return, holding_df_with_ind, on=['HLD_DATE', 'STOCK_CODE'], how='left')
    # Step 3: 开始Brinson归因
    # 先生成行业名称列
    print('开始Brinson归因')
    ind_list = pd.concat([holding_return.INDUSTRY_NAME, benchmark_return.INDUSTRY_NAME]).drop_duplicates()
    ind_list.reset_index(drop=True, inplace=True)

    if method == 'BHB':
        holding_return['RTN_TIMES_WEIGHT'] = holding_return['STOCK_PER'] * holding_return['S_DQ_PCTCHANGE']
        benchmark_return['RTN_TIMES_WEIGHT'] = benchmark_return['STOCK_PER'] * benchmark_return['S_DQ_PCTCHANGE']
        BHB_df = pd.DataFrame()
        for hd in tqdm(holding_days):
            BHB_df_i = pd.DataFrame()
            BHB_df_i['HLD_DATE'] = [hd] * len(ind_list)
            BHB_df_i['INDUSTRY_NAME'] = ind_list

            # sumif汇总
            BHB_df_i['PORT_WEIGHT'] = BHB_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: holding_return.STOCK_PER.loc[
                    (holding_return.HLD_DATE == x[0]) & (holding_return.INDUSTRY_NAME == x[1])].sum(), axis=1)
            BHB_df_i['BMK_WEIGHT'] = BHB_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: benchmark_return.STOCK_PER.loc[
                    (benchmark_return.HLD_DATE == x[0]) & (benchmark_return.INDUSTRY_NAME == x[1])].sum(), axis=1)

            BHB_df_i['PORT_IND_RTN'] = BHB_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: holding_return.RTN_TIMES_WEIGHT.loc[
                    (holding_return.HLD_DATE == x[0]) & (holding_return.INDUSTRY_NAME == x[1])].sum(), axis=1) / \
                                       BHB_df_i['PORT_WEIGHT']
            BHB_df_i['BMK_IND_RTN'] = BHB_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: benchmark_return.RTN_TIMES_WEIGHT.loc[
                    (benchmark_return.HLD_DATE == x[0]) & (benchmark_return.INDUSTRY_NAME == x[1])].sum(), axis=1) / \
                                      BHB_df_i['BMK_WEIGHT']
            BHB_df_i.fillna(0, inplace=True)  # NA填充为0
            BHB_df_i['TR'] = BHB_df_i['PORT_WEIGHT'] * BHB_df_i['PORT_IND_RTN'] - BHB_df_i['BMK_WEIGHT'] * BHB_df_i[
                'BMK_IND_RTN']
            BHB_df_i['AR'] = (BHB_df_i['PORT_WEIGHT'] - BHB_df_i['BMK_WEIGHT']) * BHB_df_i['BMK_IND_RTN']
            BHB_df_i['SR'] = (BHB_df_i['PORT_IND_RTN'] - BHB_df_i['BMK_IND_RTN']) * BHB_df_i['BMK_WEIGHT']
            BHB_df_i['IR'] = (BHB_df_i['PORT_WEIGHT'] - BHB_df_i['BMK_WEIGHT']) * (
                    BHB_df_i['PORT_IND_RTN'] - BHB_df_i['BMK_IND_RTN'])

            '''
            根据配置思路，将交叉收益合并到选股收益或者配置收益中去。
            1.如果投资经理使用自下而上的配置方法，先选个股，再决定权重，那么交叉收益可合并到配置收益中去。
            这时候，配置收益为实际组合和选股组合的收益之差，含义为配置给选股组合所带来的超额收益。
            2.如果投资经理使用自上而下的配置方法，先配置行业权重，再挑个股，那么交叉收益和合并到选股收益中去。
            这时候，选股收益为实际组合和配置组合的收益之差，含义为个股的选择在当前配置基础上所带来的超额收益。
            通常情形2较多
            '''
            if IR_TREAT_METHOD == 'toAR':
                BHB_df_i['AR'] = BHB_df_i['AR'] + BHB_df_i['IR']
                BHB_df_i.drop(columns='IR', inplace=True)
            elif IR_TREAT_METHOD == 'toSR':
                BHB_df_i['SR'] = BHB_df_i['SR'] + BHB_df_i['IR']
                BHB_df_i.drop(columns='IR', inplace=True)
            BHB_df = pd.concat([BHB_df, BHB_df_i])

    elif method == 'BF':
        holding_return['RTN_TIMES_WEIGHT'] = holding_return['STOCK_PER'] * holding_return['S_DQ_PCTCHANGE']
        benchmark_return['RTN_TIMES_WEIGHT'] = benchmark_return['STOCK_PER'] * benchmark_return['S_DQ_PCTCHANGE']
        BF_df = BF_Stock_SR_df = pd.DataFrame()
        for hd in tqdm(holding_days):
            BF_df_i = pd.DataFrame()
            BF_df_i['HLD_DATE'] = [hd] * len(ind_list)
            BF_df_i['INDUSTRY_NAME'] = ind_list

            stock_rtn_df_i = holding_return.loc[holding_return.HLD_DATE == hd,
                                                ['HLD_DATE', 'STOCK_CODE', 'STOCK_PER', 'INDUSTRY_NAME',
                                                 'S_DQ_PCTCHANGE']]
            stock_rtn_df_i.rename(columns={'STOCK_PER': 'PORT_WEIGHT'}, inplace=True)

            # sumif汇总
            BF_df_i['PORT_WEIGHT'] = BF_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: holding_return.STOCK_PER.loc[
                    (holding_return.HLD_DATE == x[0]) & (holding_return.INDUSTRY_NAME == x[1])].sum(), axis=1)
            BF_df_i['BMK_WEIGHT'] = BF_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: benchmark_return.STOCK_PER.loc[
                    (benchmark_return.HLD_DATE == x[0]) & (benchmark_return.INDUSTRY_NAME == x[1])].sum(), axis=1)

            BF_df_i['PORT_IND_RTN'] = BF_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: holding_return.RTN_TIMES_WEIGHT.loc[
                    (holding_return.HLD_DATE == x[0]) & (holding_return.INDUSTRY_NAME == x[1])].sum(), axis=1) / \
                                      BF_df_i['PORT_WEIGHT']
            BF_df_i['BMK_IND_RTN'] = BF_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: benchmark_return.RTN_TIMES_WEIGHT.loc[
                    (benchmark_return.HLD_DATE == x[0]) & (benchmark_return.INDUSTRY_NAME == x[1])].sum(), axis=1) / \
                                     BF_df_i['BMK_WEIGHT']
            BF_df_i.fillna(0, inplace=True)  # NA填充为0
            # 计算基准组合总收益Rb
            # port_rtn_total_i = sum(BF_df_i['PORT_WEIGHT'] * BF_df_i['PORT_IND_RTN'])
            bmk_rtn_total_i = sum(BF_df_i['BMK_WEIGHT'] * BF_df_i['BMK_IND_RTN'])
            BF_df_i['TR'] = bmk_rtn_total_i * (BF_df_i['BMK_WEIGHT'] - BF_df_i['PORT_WEIGHT']) + \
                            (BF_df_i['PORT_WEIGHT'] * BF_df_i['PORT_IND_RTN'] - BF_df_i['BMK_WEIGHT'] * BF_df_i[
                                'BMK_IND_RTN'])
            BF_df_i['AR'] = (BF_df_i['PORT_WEIGHT'] - BF_df_i['BMK_WEIGHT']) * (
                    BF_df_i['BMK_IND_RTN'] - bmk_rtn_total_i)
            BF_df_i['SR'] = BF_df_i['PORT_WEIGHT'] * (BF_df_i['PORT_IND_RTN'] - BF_df_i['BMK_IND_RTN'])

            # 计算个股层面选股贡献
            stock_rtn_df_i = pd.merge(stock_rtn_df_i, BF_df_i[['HLD_DATE', 'INDUSTRY_NAME', 'BMK_IND_RTN']],
                                      on=['HLD_DATE', 'INDUSTRY_NAME'], how='left')
            stock_rtn_df_i['SR'] = stock_rtn_df_i['PORT_WEIGHT'] * (
                    stock_rtn_df_i['S_DQ_PCTCHANGE'] - stock_rtn_df_i['BMK_IND_RTN'])

            BF_df = pd.concat([BF_df, BF_df_i])
            BF_Stock_SR_df = pd.concat([BF_Stock_SR_df, stock_rtn_df_i])
            # BF_Stock_SR_df[['INDUSTRY_NAME','SR']].groupby('INDUSTRY_NAME').sum('SR')

    elif method == 'BFt':
        holding_return['RTN_TIMES_WEIGHT'] = holding_return['STKVALUETONAV'] * holding_return['S_DQ_PCTCHANGE']
        benchmark_return['RTN_TIMES_WEIGHT'] = benchmark_return['STKVALUETONAV'] * benchmark_return['S_DQ_PCTCHANGE']
        BFt_df = BFt_Stock_SR_df = pd.DataFrame()
        for hd in tqdm(holding_days):
            BFt_df_i = pd.DataFrame()
            BFt_df_i['HLD_DATE'] = [hd] * len(ind_list)
            BFt_df_i['INDUSTRY_NAME'] = ind_list

            stock_rtn_df_i = holding_return.loc[holding_return.HLD_DATE == hd,
                                                ['HLD_DATE', 'STOCK_CODE', 'STKVALUETONAV', 'INDUSTRY_NAME',
                                                 'S_DQ_PCTCHANGE']]
            stock_rtn_df_i.rename(columns={'STKVALUETONAV': 'PORT_WEIGHT'}, inplace=True)
            # sumif汇总
            BFt_df_i['PORT_WEIGHT'] = BFt_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: holding_return.STKVALUETONAV.loc[
                    (holding_return.HLD_DATE == x[0]) & (holding_return.INDUSTRY_NAME == x[1])].sum(), axis=1)
            BFt_df_i['BMK_WEIGHT'] = BFt_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: benchmark_return.STKVALUETONAV.loc[
                    (benchmark_return.HLD_DATE == x[0]) & (benchmark_return.INDUSTRY_NAME == x[1])].sum(), axis=1)

            BFt_df_i['PORT_IND_RTN'] = BFt_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: holding_return.RTN_TIMES_WEIGHT.loc[
                    (holding_return.HLD_DATE == x[0]) & (holding_return.INDUSTRY_NAME == x[1])].sum(), axis=1) / \
                                       BFt_df_i['PORT_WEIGHT']
            BFt_df_i['BMK_IND_RTN'] = BFt_df_i[['HLD_DATE', 'INDUSTRY_NAME']].apply(
                lambda x: benchmark_return.RTN_TIMES_WEIGHT.loc[
                    (benchmark_return.HLD_DATE == x[0]) & (benchmark_return.INDUSTRY_NAME == x[1])].sum(), axis=1) / \
                                      BFt_df_i['BMK_WEIGHT']
            BFt_df_i.fillna(0, inplace=True)  # NA填充为0

            # 计算基准组合总收益Rb
            # port_rtn_total_i = sum(BF_df_i['PORT_WEIGHT'] * BF_df_i['PORT_IND_RTN'])
            bmk_rtn_total_i = sum(BFt_df_i['BMK_WEIGHT'] * BFt_df_i['BMK_IND_RTN'])
            BFt_df_i['TR'] = BFt_df_i['PORT_WEIGHT'] * BFt_df_i['PORT_IND_RTN'] - BFt_df_i['BMK_WEIGHT'] * BFt_df_i[
                'BMK_IND_RTN']
            BFt_df_i['AR'] = (BFt_df_i['PORT_WEIGHT'] - BFt_df_i['BMK_WEIGHT']) * (
                    BFt_df_i['BMK_IND_RTN'] - bmk_rtn_total_i)  # 行业选择收益
            BFt_df_i['SR'] = BFt_df_i['PORT_WEIGHT'] * (BFt_df_i['PORT_IND_RTN'] - BFt_df_i['BMK_IND_RTN'])  # 个股选择收益
            BFt_df_i['MR'] = (BFt_df_i['PORT_WEIGHT'] - BFt_df_i['BMK_WEIGHT']) * bmk_rtn_total_i

            # 计算个股层面选股贡献
            stock_rtn_df_i = pd.merge(stock_rtn_df_i, BFt_df_i[['HLD_DATE', 'INDUSTRY_NAME', 'BMK_IND_RTN']],
                                      on=['HLD_DATE', 'INDUSTRY_NAME'], how='left')
            stock_rtn_df_i['SR'] = stock_rtn_df_i['PORT_WEIGHT'] * (
                    stock_rtn_df_i['S_DQ_PCTCHANGE'] - stock_rtn_df_i['BMK_IND_RTN'])

            BFt_df = pd.concat([BFt_df, BFt_df_i])
            BFt_Stock_SR_df = pd.concat([BFt_Stock_SR_df, stock_rtn_df_i])

    # Step 4: 结果汇总
    if method == 'BHB':
        Brinson_result = BHB_df.copy()
        # BHB模型暂不输出个股选股贡献

    elif method == 'BF':
        Brinson_result = BF_df.copy()
        Brinson_result_stock = BF_Stock_SR_df.copy()

    elif method == 'BFt':
        Brinson_result = BFt_df.copy()
        Brinson_result_stock = BFt_Stock_SR_df.copy()

    # 按日度拆分（未多期调整）
    Brinson_result.insert(6, 'PORT_RTN', Brinson_result.PORT_WEIGHT * Brinson_result.PORT_IND_RTN)
    Brinson_result.insert(7, 'BMK_RTN', Brinson_result.BMK_WEIGHT * Brinson_result.BMK_IND_RTN)
    Brinson_result_summary_by_day = Brinson_result.groupby('HLD_DATE').sum().drop(
        columns=['PORT_IND_RTN', 'BMK_IND_RTN'])
    Brinson_result_summary_by_day.loc['Total'] = Brinson_result_summary_by_day.sum(axis=0)
    # 按行业拆分（未多期调整）
    Brinson_result_summary_by_ind = Brinson_result.groupby('INDUSTRY_NAME').sum().drop(
        columns=['PORT_IND_RTN', 'BMK_IND_RTN'])
    Brinson_result_summary_by_ind['PORT_WEIGHT'] = Brinson_result_summary_by_ind['PORT_WEIGHT'] / len(holding_days)
    Brinson_result_summary_by_ind['BMK_WEIGHT'] = Brinson_result_summary_by_ind['BMK_WEIGHT'] / len(holding_days)
    Brinson_result_summary_by_ind.sort_values(by='PORT_WEIGHT', ascending=False, inplace=True)
    Brinson_result_summary_by_ind.loc['Total'] = Brinson_result_summary_by_ind.sum(axis=0)
    #  按个股拆分（未多期调整）
    Brinson_result_summary_by_stock = Brinson_result_stock.groupby('STOCK_CODE').sum().drop(
        columns=['S_DQ_PCTCHANGE', 'BMK_IND_RTN'])
    Brinson_result_summary_by_stock['PORT_WEIGHT'] = Brinson_result_summary_by_stock['PORT_WEIGHT'] / len(holding_days)
    Brinson_result_summary_by_stock.sort_values(by='SR', ascending=False, inplace=True)
    Brinson_result_summary_by_stock.loc['Total'] = Brinson_result_summary_by_stock.sum(axis=0)

    # 多期Brinson调整
    Brinson_result_daily_series = Brinson_result_summary_by_day.iloc[:-1, 2:]
    effect_col = Brinson_result_daily_series.columns[2:]

    Brinson_result_cum_series = pd.DataFrame()
    Brinson_result_cum_series[['PORT_RTN', 'BMK_RTN']] = em.cum_returns(
        Brinson_result_daily_series[['PORT_RTN', 'BMK_RTN']])
    Brinson_result_cum_series[effect_col] = None

    def cal_kt(R):
        try:
            k = (math.log(1 + R[0]) - math.log(1 + R[1])) / (R[0] - R[1])
        except:
            k = 1
        return k

    kt_series = Brinson_result_daily_series[['PORT_RTN', 'BMK_RTN']].apply(cal_kt, axis=1)
    k_series = Brinson_result_cum_series[['PORT_RTN', 'BMK_RTN']].apply(cal_kt, axis=1)
    for hd in holding_days:
        k = k_series[hd]
        Brinson_result_temp = Brinson_result_daily_series[:hd]
        Brinson_result_temp['kt'] = kt_series[:hd]
        Brinson_result_temp['scale_factor'] = Brinson_result_temp['kt'] / k
        Brinson_result_cum_series.loc[hd, effect_col] = Brinson_result_temp[effect_col].mul(
            Brinson_result_temp['scale_factor'], axis=0).sum()

    Brinson_result_collect = dict()
    Brinson_result_collect['Cum_Series'] = Brinson_result_cum_series
    Brinson_result_collect['By_Ind_Daily'] = Brinson_result
    Brinson_result_collect['Stock_AR_Daily'] = Brinson_result_stock
    Brinson_result_collect['By_Day_Summary'] = Brinson_result_summary_by_day
    Brinson_result_collect['By_Ind_Summary'] = Brinson_result_summary_by_ind
    Brinson_result_collect['Stock_AR_Summary'] = Brinson_result_summary_by_stock

    return Brinson_result_collect


# %% 函数示例
# # 公募基金的的Brinson归因示例
# holding_df, holding_summary = get_fund_stk_holding(
#     fund_code=['001694.OF', '006567.OF', '000017.OF', '000031.OF', '000083.OF'], start_date="20200101",
#     end_date="20220510", freq="H", top10=False, data_mode='DB')
# holding_data = holding_df.loc[holding_df.F_INFO_WINDCODE == '000017.OF'][
#     ["F_PRT_ENDDATE", 'S_INFO_STOCKWINDCODE', 'STOCK_PER', 'F_PRT_STKVALUETONAV']]
# #
# brinson_rst = brinson_analysis(
#     holding_data=holding_data, benchmark_code='000300.SH', bm_cash_pct=0.9, end_date="20220430",
#     method='BFt', IR_TREAT_METHOD='toAR', datamode=["DB", "DB", "DB"],
#     database_path=[path_stock, path_index, path_fund],
#     dataframe=['', '', ''], tradeday_list=tradeday_list, ind_class='SW', level=1,
#     AH_comb=True, Find_latest_td=True)
# output_to_excel(brinson_rst, 'brinson_rst.xlsx')
# # # 公募基金的的Brinson归因示例
# holding_df, holding_summary = get_fund_stk_holding(
#     fund_code=['003822.OF'], start_date="20190101",
#     end_date="20221026", freq="H", top10=False, data_mode='WindAPI')
# holding_data = holding_df.loc[holding_df.F_INFO_WINDCODE == '003822.OF'][
#     ["F_PRT_ENDDATE", 'S_INFO_STOCKWINDCODE', 'STOCK_PER', 'F_PRT_STKVALUETONAV']]
# #
# brinson_rst = brinson_analysis(
#     holding_data=holding_data, benchmark_code='000300.SH', bm_cash_pct=0.4, end_date="20221026",
#     method='BF', IR_TREAT_METHOD='toAR', datamode=["WindAPI", "WindAPI", "WindAPI"],tradeday_list=tradeday_list,
#     ind_class='SW', level=1, AH_comb=True, Find_latest_td=True)
# output_to_excel(brinson_rst, 'brinson_rst.xlsx')



# # 日度持仓的Brinson归因示例
'''
HLD_DATE	STOCK_CODE	STOCK_VALUE	STKVALUETONAV
20210104	600031.SH	11427310.8	0.2004
20210104	600048.SH	8956882	0.1571
20210104	600109.SH	9096915	0.1596
'''


# holding_df = pd.read_excel('holding data.xlsx', converters={'HLD_DATE': str})
# holding_df['STOCK_PER'] = holding_df.groupby('HLD_DATE').STOCK_VALUE.apply(lambda x: x / sum(x))  # 对各期持仓归一化
# holding_df = holding_df[['HLD_DATE', 'STOCK_CODE', 'STOCK_PER', 'STKVALUETONAV']]
# holding_df['STKVALUETONAV'] = holding_df['STKVALUETONAV'] / 100
#
# dataframe_bm, idx_summary = get_index_composite(
#     index_code=['000300.SH'], date_list=sorted(list(set(holding_df.HLD_DATE))), data_mode='DB',
#     database_path=path_index, dataframe="", tradeday_list=tradeday_list, show_summary=True)
#
# stock_list_all = list(set(list(holding_df['STOCK_CODE'])).union(set(list(dataframe_bm['S_CON_WINDCODE']))))
#
# dataframe_price = fetch_asset_series(stock_code=stock_list_all,
#                                      index_code='', fund_code='',
#                                      start_date='20201228', end_date='20220104',
#                                      data_mode='DB', database_path=[path_stock, path_index, path_fund],
#                                      tradeday_list=tradeday_list, censor_rebase=False,
#                                      to_wide=False)  # 先把所有可能涉及到的资产提取出净值
# # 保留两列，第一列交易日期，第二列股票代码
# df1 = holding_df[['HLD_DATE', 'STOCK_CODE']]
# df2 = dataframe_bm[['TRADE_DT', 'S_CON_WINDCODE']]
# df2.columns = ['HLD_DATE', 'STOCK_CODE']
# df3 = pd.concat([df1, df2]).drop_duplicates()
#
# # dataframe_ind = get_industry(holding_df=df3, ind_class='SW', level=1, AH_comb=False, datamode='DB')
# # dataframe_ind.to_pickle('dataframe_ind.pk1')
# dataframe_ind=pd.read_pickle('dataframe_ind.pk1')
#
# brinson_rst2 = brinson_analysis(
#     holding_data=holding_df, benchmark_code='000300.SH', bm_cash_pct=0, end_date="20220105",
#     method='BF', IR_TREAT_METHOD='toAR', datamode=["DF", "DF", "DF"],
#     database_path=[path_stock, path_index, path_fund],
#     dataframe=[dataframe_price, dataframe_bm, dataframe_ind], tradeday_list=tradeday_list, ind_class='SW2021', level=1,
#     AH_comb=True, Find_latest_td=False)
# output_to_excel(brinson_rst2,'brinson_rst2.xlsx')


# %%  RBSA分析基金风格
# TODO 研究如何做带约束逐步回归
# 带约束回归
# cash_col指定现金资产所在的列位置，min_position和max_position指定,如果为空，则不指定仓位约束
def fit_sharpe_model(asset_df, min_coef=0, max_coef=1, cash_col=None, min_position=0, max_position=1, round_to=4,
                     Opt_Rsq=True):
    asset_series = asset_df.iloc[:, 0]
    index_df = asset_df.iloc[:, 1:]

    # Generate data.
    X = index_df.values
    y = asset_series.values
    n = X.shape[1]
    # Define Constraints:

    if cash_col is not None:
        # 1.beta求和为1  2.beta系数大于等于0  3.beta系数小于等于1 4. min_position<=权益beta系数仓位和<=max_position
        min_posi_const = np.ones((1, n))
        max_posi_const = min_posi_const.copy()
        min_posi_const[0, cash_col - 1] = 0
        max_posi_const[0, cash_col - 1] = 0

        C = np.concatenate(
            [np.ones((1, n)), -np.ones((1, n)), -min_posi_const, max_posi_const, -np.identity(n), np.identity(n)])
        bound = np.array([1, -1] + [-min_position, max_position] + [min_coef] * n + [max_coef] * n)
    else:
        C = np.concatenate(
            [np.ones((1, n)), -np.ones((1, n)), -np.identity(n), np.identity(n)])
        bound = np.array([1, -1] + [min_coef] * n + [max_coef] * n)

    # Define and solve the CVXPY problem. 不带截距项
    beta = cp.Variable(n)
    cost = cp.sum_squares(X @ beta - y)
    constrant = [C @ beta <= bound]

    prob = cp.Problem(cp.Minimize(cost), constrant)
    prob.solve()

    fitted_expo = pd.DataFrame(beta.value).T.set_axis(index_df.columns, axis=1)

    if Opt_Rsq == True:
        residual_series = asset_series - (index_df * beta.value).sum(axis=1)
        SSE = sum(residual_series ** 2)
        SST = sum((y - np.mean(y)) ** 2)
        R_square = 1 - SSE / SST
        fitted_expo = pd.concat([fitted_expo, pd.Series(R_square, name='R_Squared')], axis=1)

    fitted_expo = round(fitted_expo, round_to)

    return fitted_expo


# %% 函数示例
# 价值成长风格
# 成长/价值/中债总财富
asset_df = fetch_asset_series(stock_code='',
                              index_code=["399372.SZ", "399373.SZ", "399376.SZ","399377.SZ","H11001.CSI"],
                              fund_code=["000031.OF"],
                              start_date="20200101", end_date="20231231", data_mode='WindAPI', keep_td=True,
                              tradeday_list=tradeday_list, censor_rebase=False, to_wide=True, show_wide="pct_chg")
# 399370.SZ  399371.SZ  CBA00301.CS  006567.OF
asset_df.columns = ['大盘成长', '大盘价值', '小盘成长', '小盘价值','中债总财富', '基金']
asset_df = asset_df[['基金', '大盘成长', '大盘价值', '小盘成长', '小盘价值', '中债总财富']]

# 中信五风格
# 金融/消费/成长/周期/稳定/中债总财富
# asset_df = fetch_asset_series(stock_code='',
#                               index_code=["CI005917.WI", "CI005919.WI", 'CI005920.WI', 'CI005918.WI','CI005921.WI',
#                                           'CBA00301.CS'],
#                               fund_code=["006567.OF"],
#                               start_date="20190301", end_date="20220531", data_mode='WindAPI', keep_td=True,
#                               tradeday_list=tradeday_list, censor_rebase=False, to_wide=True, show_wide="pct_chg")
# # CI005917.WI  CI005919.WI  CI005920.WI  CI005918.WI  CI005921.WI  CBA00301.CS  006567.OF
# asset_df.columns=['金融','周期','消费','成长','稳定','中债总财富','基金']
# asset_df = asset_df[['基金', '金融','周期','消费','成长','稳定','中债总财富']]

# # 对全部数据做回归
# fit_sharpe_model(asset_df=asset_df, cash_col=3, min_position=0.8, max_position=1)
# # 分季度做回归
asset_df_copy = asset_df.copy()
asset_df_copy['Quarter'] = pd.PeriodIndex(asset_df_copy.index, freq='Q')
quarter_list = sorted(list(set(asset_df_copy['Quarter'])))
# # 批量跑夏普模型
expo_result = pd.DataFrame()
for qt in quarter_list:
    asset_df_qt = asset_df_copy.loc[asset_df_copy.Quarter == qt, :].iloc[:, :-1]
    expo_qt = fit_sharpe_model(asset_df=asset_df_qt, cash_col=5, min_position=0, max_position=1)
    expo_result = pd.concat([expo_result, pd.DataFrame(expo_qt)])
expo_result.index = quarter_list

expo_result.iloc[:, :-1].plot.area(stacked=True)
plt.plot(expo_result.iloc[:, -1], color='grey', marker='D')
plt.show()


# 债券基金久期
# 1年以下/1-3年/3-5年/5-7年/7-10年/10年以上
# asset_df = fetch_asset_series(stock_code='',
#                               index_code=["CBA00111.CS", "CBA00121.CS", 'CBA00131.CS', 'CBA00141.CS','CBA00151.CS',
#                                           'CBA00161.CS'],
#                               fund_code=["270048.OF"],
#                               start_date="20190301", end_date="20220531", data_mode='WindAPI', keep_td=True,
#                               tradeday_list=tradeday_list, censor_rebase=False, to_wide=True, show_wide="pct_chg")
# # CBA00111.CS  CBA00121.CS  CBA00131.CS  CBA00141.CS  CBA00151.CS  CBA00161.CS  270048.OF
# asset_df.columns=['1年以下','1-3年','3-5年','5-7年','7-10年','10年以上','基金']
# asset_df = asset_df[['基金', '1年以下','1-3年','3-5年','5-7年','7-10年','10年以上']]
#
# # 分季度做回归
# asset_df_copy = asset_df.copy()
# asset_df_copy['Quarter'] = pd.PeriodIndex(asset_df_copy.index, freq='Q')
# quarter_list = sorted(list(set(asset_df_copy['Quarter'])))
# # 批量跑夏普模型
# expo_result = pd.DataFrame()
# for qt in quarter_list:
#     asset_df_qt = asset_df_copy.loc[asset_df_copy.Quarter == qt, :].iloc[:, :-1]
#     expo_qt = fit_sharpe_model(asset_df=asset_df_qt, min_coef=0, max_coef=1, cash_col=None)
#     expo_result = pd.concat([expo_result, pd.DataFrame(expo_qt)])
# expo_result.index = quarter_list
# expo_result.iloc[:, :-1].plot.area(stacked=True)
# plt.plot(expo_result.iloc[:, -1], color='grey', marker='D')
# plt.show()


# %% 组合优化函数
'''
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

asset_df = fetch_asset_series(stock_code='',
                               index_code=["000300.SH", "CBA00101.CS", "HSI.HI"], fund_code='',
                               start_date="20170101",
                               end_date="20220320", data_mode='DB', tradeday_list=tradeday_list,
                               censor_rebase=False, to_wide=True)
mu = expected_returns.mean_historical_return(asset_df,frequency=245)
S = risk_models.sample_cov(asset_df,frequency=245)
# Optimize for maximal Sharpe ratio
ef = EfficientFrontier(mu, S)
raw_weights = ef.max_sharpe()
cleaned_weights = ef.clean_weights()
ef.save_weights_to_file("weights.csv")  # saves to file
print(cleaned_weights)
ef.portfolio_performance(verbose=True)

latest_prices = get_latest_prices(asset_df)

da = DiscreteAllocation(cleaned_weights, latest_prices, total_portfolio_value=10000)
allocation, leftover = da.greedy_portfolio()
print("Discrete allocation:", allocation)
print("Funds remaining: ${:.2f}".format(leftover))
'''

# %% 基金申赎费率函数（只能调用数据库）
# 输入：基金类别，交易金额，交易方向（申购、赎回），申购折扣，持有时长
# 输出：基金费用额，基金费用率
