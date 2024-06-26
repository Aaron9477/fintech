# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/11 11:25 
# @Author    : Wangyd5 
# @File      : cal_nav_net_value
# @Project   : licai
# @Function  ：计算非现金管理类产品的净值收益
# --------------------------------


import numpy as np
import pandas as pd
from cscfist.model.net_value_indicator_model.net_value_indicator import NetValueIndicator

from tools.date_util import NatureDateUtils


def cal_product_nav(tmp_nav, finprocode):
    """ 计算单个产品净值"""
    begin_date = tmp_nav['trade_dt'].iloc[0].strftime('%Y%m%d')
    end_date = tmp_nav['trade_dt'].iloc[-1].strftime('%Y%m%d')

    tmp_nav.set_index('trade_dt', inplace=True)
    # 净值数据降频计算（周频）  -- fixme 现金管理类另算
    business_day = pd.date_range(begin_date, end_date)
    tmp_nav = tmp_nav.reindex(business_day)
    tmp_nav['day_week'] = None
    for x in tmp_nav.index:
        tmp = [str(i) if len(str(i)) > 1 else '0' + str(i) for i in x.isocalendar()]
        tmp = '_'.join(tmp)
        tmp_nav.loc[x, 'day_week'] = tmp[:-3]
    grouped = tmp_nav.groupby('day_week')
    tmp_nav_week = pd.DataFrame([])

    def func(ser):
        """ 每周中取距离周五最近的数"""
        ser_denan = ser.dropna()
        if len(ser_denan) == 0:
            return np.nan
        else:
            return ser_denan.tail(1)[0]

    for day_week, tmp_df in grouped:
        if len(tmp_df) < 7:
            continue
        else:
            date = tmp_df.index[-3]  # 取出周五日期
            value = tmp_df.apply(func, axis=0)  # ag
            value.name = date
            tmp_nav_week = tmp_nav_week.append(value)
    tmp_nav_week = tmp_nav_week[['FinProCode', 'net_value']].copy()

    indicator_ser = pd.Series([], dtype=pd.StringDtype())
    # 计算空值率（每列）
    if len(tmp_nav_week.dropna()) == 0:
        raise ValueError(f'{finprocode}不存在净值数据.....')
    else:
        # 找到第一个非空的值进行截断
        begin_index = tmp_nav_week[tmp_nav_week['net_value'].notnull()].index[0]
        end_index = tmp_nav_week[tmp_nav_week['net_value'].notnull()].index[-1]
        tmp_nav_week = tmp_nav_week.loc[begin_index:end_index].copy()
        # 计算空值率
        valid_ratio = len(tmp_nav_week[tmp_nav_week['net_value'].notnull()]) / len(tmp_nav_week)
        """
        如果数据量过少，不参与计算，如果空值率过高，也不参与计算
        """
        if (valid_ratio < 0.3) | (len(tmp_nav_week) <= 10):
            raise ValueError(f'{finprocode}净值数据不足两个月，不参与计算.....')
        else:
            # 填充数据，保证每个每个频次的数据都有
            tmp_nav_week['net_value'] = tmp_nav_week['net_value'].interpolate()
            tmp_nav_week['FinProCode'] = tmp_nav_week['FinProCode'].fillna(method='ffill')
            # 计算指标
            rf = 0.015
            cal_ret_obj = NetValueIndicator(net_value=tmp_nav_week['net_value'].dropna(),
                                            benchmark_close=tmp_nav_week['net_value'].dropna(),
                                            risk_free_rate=rf, period='w',trade_date_list=list(tmp_nav_week.index))
            interval_ret_annual = cal_ret_obj.interval_return(is_annual=True)
            max_draw_down = cal_ret_obj.max_draw_down()
            sharpe = cal_ret_obj.sharpe()
            # 近三个月收益
            three_month_date = NatureDateUtils.date_period_change(end_date, '-3m')
            three_m_cal_data = tmp_nav_week.loc[three_month_date:].copy()
            interval_ret_three_m = three_m_cal_data['net_value'].dropna().iloc[-1] / \
                                   three_m_cal_data['net_value'].dropna().iloc[0] - 1

            indicator_ser['interval_ret_three_m'] = interval_ret_three_m
            indicator_ser['interval_ret_annual'] = interval_ret_annual
            indicator_ser['max_draw_down'] = max_draw_down
            indicator_ser['sharpe'] = sharpe if sharpe >= 0 else 0
            indicator_ser['shapre_original'] = sharpe
            indicator_ser['shapre_str_negative'] = sharpe if sharpe >= 0 else '小于0'
            indicator_ser.name = finprocode
    return indicator_ser


def cal_product_nav_from_database(tmp_nav, finprocode):
    """ 从数据库中取数，计算单个产品净值"""

    begin_date = tmp_nav['trade_dt'].iloc[0].strftime('%Y%m%d')
    end_date = tmp_nav['trade_dt'].iloc[-1].strftime('%Y%m%d')

    tmp_nav.set_index('trade_dt', inplace=True)
    # 净值数据降频计算（周频）  -- fixme 现金管理类另算
    business_day = pd.date_range(begin_date, end_date)
    tmp_nav = tmp_nav.reindex(business_day)
    tmp_nav['day_week'] = None
    for x in tmp_nav.index:
        tmp = [str(i) if len(str(i)) > 1 else '0' + str(i) for i in x.isocalendar()]
        tmp = '_'.join(tmp)
        tmp_nav.loc[x, 'day_week'] = tmp[:-3]
    grouped = tmp_nav.groupby('day_week')
    tmp_nav_week = pd.DataFrame([])

    def func(ser):
        """ 每周中取距离周五最近的数"""
        ser_denan = ser.dropna()
        if len(ser_denan) == 0:
            return np.nan
        else:
            return ser_denan.tail(1)[0]

    for day_week, tmp_df in grouped:
        if len(tmp_df) < 7:
            continue
        else:
            date = tmp_df.index[-3]  # 取出周五日期
            value = tmp_df.apply(func, axis=0)  # ag
            value.name = date
            tmp_nav_week = tmp_nav_week.append(value)
    tmp_nav_week = tmp_nav_week[['FinProCode', 'net_value']].copy()

    indicator_ser = pd.Series([], dtype=pd.StringDtype())
    # 计算空值率（每列）
    if len(tmp_nav_week.dropna()) == 0:
        raise ValueError(f'{finprocode}不存在净值数据.....')
    else:
        # 找到第一个非空的值进行截断
        begin_index = tmp_nav_week[tmp_nav_week['net_value'].notnull()].index[0]
        end_index = tmp_nav_week[tmp_nav_week['net_value'].notnull()].index[-1]
        tmp_nav_week = tmp_nav_week.loc[begin_index:end_index].copy()
        # 计算空值率
        valid_ratio = len(tmp_nav_week[tmp_nav_week['net_value'].notnull()]) / len(tmp_nav_week)
        """
        如果数据量过少，不参与计算，如果空值率过高，也不参与计算
        """
        if (valid_ratio < 0.3) | (len(tmp_nav_week) <= 10):
            raise ValueError(f'{finprocode}净值数据不足两个月，不参与计算.....')
        else:
            # 填充数据，保证每个每个频次的数据都有
            tmp_nav_week['net_value'] = tmp_nav_week['net_value'].interpolate()
            tmp_nav_week['FinProCode'] = tmp_nav_week['FinProCode'].fillna(method='ffill')
            # 计算指标
            rf = 0.015
            cal_ret_obj = NetValueIndicator(net_value=tmp_nav_week['net_value'].dropna(),
                                            benchmark_close=tmp_nav_week['net_value'].dropna(),
                                            risk_free_rate=rf, period='w')
            interval_ret_annual = cal_ret_obj.interval_return(is_annual=True)
            max_draw_down = cal_ret_obj.max_draw_down()
            sharpe = cal_ret_obj.sharpe()
            # 近三个月收益
            three_month_date = NatureDateUtils.date_period_change(end_date, '-3m')
            three_m_cal_data = tmp_nav_week.loc[three_month_date:].copy()
            interval_ret_three_m = three_m_cal_data['net_value'].dropna().iloc[-1] / \
                                   three_m_cal_data['net_value'].dropna().iloc[0] - 1

            indicator_ser['interval_ret_three_m'] = interval_ret_three_m
            indicator_ser['interval_ret_annual'] = interval_ret_annual
            indicator_ser['max_draw_down'] = max_draw_down
            indicator_ser['sharpe'] = sharpe if sharpe >= 0 else 0
            indicator_ser['shapre_original'] = sharpe
            indicator_ser['shapre_str_negative'] = sharpe if sharpe >= 0 else '小于0'
            indicator_ser.name = finprocode
    return indicator_ser

if __name__ == '__main__':
    from database.read.read_py_base import PyReader
    from process.util_cal.process_net_value import nav_fill
    reader = PyReader()
    cp_id = 7740826
    net_value = reader.get_net_value(cp_id=cp_id)
    df_new = nav_fill(net_value)
    tmp_res = cal_product_nav(tmp_nav=df_new[['FinProCode', 'trade_dt', 'net_value']], finprocode=cp_id)

