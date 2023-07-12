# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/10/27 11:21 
# @Author    : Wangyd5 
# @File      : cal_net_value
# @Project   : sublicai
# @Function  ：
# --------------------------------
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression

date_s = datetime.datetime(1900, 1, 1, 0, 0)
date_e = datetime.datetime(9999, 12, 31, 0, 0)
defect_tags = [np.nan, '手动更新', '等待朝阳永续更新', '朝阳永续更新数据超出当前日期', '未添加至朝阳关注库']
rf_default = 0.015
offsets = [30 * 1, 30 * 2, 30 * 3, 30 * 6, 365, 365 * 2, 365 * 3, 365 * 100]


def Remove_defects(nav_Series, drop_=False):
    for defect_tag in defect_tags:
        nav_Series = nav_Series.replace(defect_tag, np.nan)
    if drop_:
        nav_Series = nav_Series.dropna()
    nav_Series = nav_Series.astype(float)
    return nav_Series


def Filter_series(nav_Series, date_s=date_s, date_e=date_e, offset=36500):
    nav_Series = nav_Series[nav_Series.index >= date_s]
    nav_Series = nav_Series[nav_Series.index <= date_e]
    if len(nav_Series) == 0:
        return nav_Series
    elif offset > 0:  # 最后一行往前
        end_date = nav_Series.index[-1]
        start_date = end_date - datetime.timedelta(days=offset)
        nav_Series = nav_Series[nav_Series.index > start_date]
    else:  # 第一行往后
        start_date = nav_Series.index[0]
        end_date = start_date - datetime.timedelta(days=offset)
        nav_Series = nav_Series[nav_Series.index < end_date]
    # string of digits to float, else to NaN
    nav_Series = pd.to_numeric(nav_Series, errors='coerce')
    nav_Series.dropna(inplace=True)
    return (nav_Series)


# 收益率
def Cal_return(nav_Series, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    nav_Series = Filter_series(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    nav_Series = Remove_defects(nav_Series)
    if len(nav_Series) < 2:
        return np.nan
    factor_value = (nav_Series.iloc[-1] / nav_Series.iloc[0]) - 1
    return factor_value


# 波动率
def Cal_std(nav_Series, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    nav_Series = Filter_series(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    nav_Series = Remove_defects(nav_Series)
    if len(nav_Series) < 2:
        return np.nan
    ret_Series = (nav_Series / nav_Series.shift(1) - 1).dropna()
    factor_value = ret_Series.std()
    return factor_value


# 年化收益率
def Cal_ann_return(nav_Series, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    nav_Series = Filter_series(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    nav_Series = Remove_defects(nav_Series)
    if len(nav_Series) < 2:
        return np.nan
    Annual_data_num = len(nav_Series) / ((nav_Series.index[-1] - nav_Series.index[0]).days / 365)
    factor_value = (nav_Series.iloc[-1] / nav_Series.iloc[0]) ** (Annual_data_num / len(nav_Series)) - 1
    return factor_value


# 年化波动率
def Cal_ann_std(nav_Series, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    nav_Series = Filter_series(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    nav_Series = Remove_defects(nav_Series)
    if len(nav_Series) < 2:
        return np.nan
    ret_Series = (nav_Series / nav_Series.shift(1) - 1).dropna()
    Annual_data_num = len(nav_Series) / ((nav_Series.index[-1] - nav_Series.index[0]).days / 365)
    factor_value = (ret_Series.std()) * (Annual_data_num ** 0.5)
    return factor_value


# 最大回撤
def Cal_drawdown(nav_Series, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    nav_Series = Filter_series(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    nav_Series = Remove_defects(nav_Series)
    if len(nav_Series) < 2:
        return np.nan
    max_down = 1.0
    array_ = np.array(nav_Series.values)
    '''
    data=list(array_)
    index_j = np.argmax(np.maximum.accumulate(data) - data)
    index_i = np.argmax(data[:index_j])
    d = -(data[index_i] - data[index_j] )/data[index_i]
    return d
    '''
    for i in range(0, len(array_)):
        drawdown = min(array_[i] / array_[:i + 1] - 1)
        if max_down > drawdown:
            max_down = drawdown
    return max_down


# 夏普比
def Cal_sharp(nav_Series, rf=rf_default, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    ret = Cal_ann_return(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    std = Cal_ann_std(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    factor_value = (ret - rf) / std
    return factor_value


# sortino比率
def Cal_sortino(nav_Series, rf=rf_default, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    nav_Series = Filter_series(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    nav_Series = Remove_defects(nav_Series)
    if len(nav_Series) < 2:
        return np.nan
    Annual_data_num = len(nav_Series) / ((nav_Series.index[-1] - nav_Series.index[0]).days / 365)
    ret = Cal_ann_return(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    ret_Series = (nav_Series / nav_Series.shift(1)).dropna()
    ret_Series = ret_Series[ret_Series < 1] - 1
    std = (ret_Series.std()) * (Annual_data_num ** 0.5)
    factor_value = (ret - rf) / std
    return factor_value


# calmar比率
def Cal_calmar(nav_Series, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    ret = Cal_ann_return(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    drawdown = Cal_drawdown(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    factor_value = -ret / drawdown
    return factor_value


# 超额收益
def Cal_excret(nav_Series, benchmark_Series, date_s=date_s, date_e=date_e, offset=offsets[4]):
    if len(nav_Series) < 2:
        return np.nan
    fund_ret = Cal_return(nav_Series, date_s=date_s, date_e=date_e, offset=offset)
    benchmark_ret = Cal_return(benchmark_Series, date_s=date_s, date_e=date_e, offset=offset)
    fund_excret = (1 + fund_ret) / (1 + benchmark_ret) - 1
    return fund_excret


# H-M模型
def Cal_HMcoef(nav_Series, benchmark_Series, rf=rf_default, reg_bound=10, date_s=date_s, date_e=date_e,
               offset=offsets[4]):
    if len(nav_Series) < 2:
        return [np.nan, np.nan]
    nav_Series = Remove_defects(nav_Series)
    benchmark_Series = Remove_defects(benchmark_Series)
    fund_ret = (nav_Series / nav_Series.shift(1) - 1)
    benchmark_ret = (benchmark_Series / benchmark_Series.shift(1) - 1)
    fund_ret = Filter_series(fund_ret, date_s=date_s, date_e=date_e, offset=offset)
    benchmark_ret = Filter_series(benchmark_ret, date_s=date_s, date_e=date_e, offset=offset)
    benchmark_ret = benchmark_ret[(benchmark_ret.index).isin(fund_ret.index)]
    fund_rets = pd.DataFrame(index=fund_ret.index)
    fund_rets['fund_ret'] = fund_ret
    fund_rets['benchmark_excret'] = benchmark_ret - rf
    fund_rets['benchmark_excret2'] = (benchmark_ret - rf) * (benchmark_ret - rf > 0)
    HMcoef = [np.nan, np.nan]
    if len(fund_rets > reg_bound):
        reg = LinearRegression(fit_intercept=True)
        res = reg.fit(fund_rets[['benchmark_excret', 'benchmark_excret2']], fund_rets['fund_ret'])
        HMcoef[0] = res.intercept_
        HMcoef[1] = res.coef_[1]
    return HMcoef


class indicators(basic_class.basic):
    def __init__(self, nav_Series=None, offset=36500, date_s=date_s, date_e=date_e, rf=rf_default,
                 benchmark_Series=None, category=None, reg_bound=10):
        self.nav_Series = nav_Series
        self.offset = offset
        self.date_s = date_s
        self.date_e = date_e
        self.rf = rf
        self.benchmark_Series = benchmark_Series
        self.category = category
        self.reg_bound = reg_bound

    def cal_return(self):
        nav_Series = self.nav_Series
        offset = self.offset
        date_s = self.date_s
        date_e = self.date_e
        self.ret = Cal_return(nav_Series, date_s=date_s, date_e=date_e, offset=offset)

    def cal_std(self):
        nav_Series = self.nav_Series
        offset = self.offset
        date_s = self.date_s
        date_e = self.date_e
        self.std = Cal_std(nav_Series, date_s=date_s, date_e=date_e, offset=offset)

    def cal_ann_return(self):
        nav_Series = self.nav_Series
        offset = self.offset
        date_s = self.date_s
        date_e = self.date_e
        self.ann_ret = Cal_ann_return(nav_Series, date_s=date_s, date_e=date_e, offset=offset)

    def cal_ann_std(self):
        nav_Series = self.nav_Series
        offset = self.offset
        date_s = self.date_s
        date_e = self.date_e
        self.ann_std = Cal_ann_std(nav_Series, date_s=date_s, date_e=date_e, offset=offset)

    def cal_drawdown(self):
        nav_Series = self.nav_Series
        offset = self.offset
        date_s = self.date_s
        date_e = self.date_e
        self.drawdown = Cal_drawdown(nav_Series, date_s=date_s, date_e=date_e, offset=offset)

    def cal_sharp(self):
        nav_Series = self.nav_Series
        offset = self.offset
        rf = self.rf
        date_s = self.date_s
        date_e = self.date_e
        self.sharp = Cal_sharp(nav_Series, rf=rf, date_s=date_s, date_e=date_e, offset=offset)

    def cal_sortino(self):
        nav_Series = self.nav_Series
        offset = self.offset
        rf = self.rf
        date_s = self.date_s
        date_e = self.date_e
        self.sortino = Cal_sortino(nav_Series, date_s=date_s, date_e=date_e, offset=offset)

    def cal_calmar(self):
        nav_Series = self.nav_Series
        offset = self.offset
        date_s = self.date_s
        date_e = self.date_e
        self.calmar = Cal_calmar(nav_Series, date_s=date_s, date_e=date_e, offset=offset)

    def cal_excret(self):
        nav_Series = self.nav_Series
        offset = self.offset
        benchmark_Series = self.benchmark_Series
        date_s = self.date_s
        date_e = self.date_e
        self.excret = Cal_excret(nav_Series, benchmark_Series=benchmark_Series, date_s=date_s, date_e=date_e,
                                 offset=offset)

    def cal_HMcoef(self):
        nav_Series = self.nav_Series
        offset = self.offset
        rf = self.rf
        reg_bound = self.reg_bound
        benchmark_Series = self.benchmark_Series
        date_s = self.date_s
        date_e = self.date_e
        HMcoef = Cal_HMcoef(nav_Series, benchmark_Series=benchmark_Series, rf=rf, reg_bound=reg_bound, date_s=date_s,
                            date_e=date_e, offset=offset)
        self.HM_alpha = HMcoef[0]
        self.HM_beta = HMcoef[1]




