# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/8/28 15:03 
# @Author    : Wangyd5 
# @File      : cal_cash_ret
# @Project   : licai
# @Function  ：计算现金管理收益
# --------------------------------

import datetime

import pandas as pd

from tools.date_util import NatureDateUtils


def cal_cash_ret(finprocode, nv_data):
    """
    计算现金管理类产品收益，
    @finprocode：int ,1303326
    @nv_data: pd.DataFrame [['FinProCode', 'trade_dt',  'yield_7_days_annual']]
    return: ps.Series
            interval_ret_one_m        1.812500
            interval_ret_three_m      1.880538
            interval_ret_six_m        1.890876
            interval_ret_base_year    1.860715
                                            Name: 1303326, dtype: float64
    """
    cash_nv = nv_data.copy()
    nav_col = cash_nv.columns[2]
    end_date = nv_data['trade_dt'].iloc[-1].strftime('%Y%m%d')
    begin_date = nv_data['trade_dt'].iloc[0].strftime('%Y%m%d')
    period = (datetime.datetime.strptime(end_date, '%Y%m%d') - (
        datetime.datetime.strptime(begin_date, '%Y%m%d'))).days + 1
    cash_nv = cash_nv.set_index('trade_dt')
    num_ratio = len(cash_nv[nav_col].dropna()) / period
    one_month_date = NatureDateUtils.date_period_change(end_date, '-1m')
    three_month_date = NatureDateUtils.date_period_change(end_date, '-3m')
    six_month_date = NatureDateUtils.date_period_change(end_date, '-6m')
    base_year_date = end_date[0:4] + '0101'
    if num_ratio > 0.3:
        if nav_col == 'LatestWeeklyYield':
            # 近一个月收益
            one_m_cal_data = cash_nv.loc[one_month_date:].copy()
            interval_ret_one_m = one_m_cal_data[nav_col].mean()
            # 近三个月收益
            three_m_cal_data = cash_nv.loc[three_month_date:].copy()
            interval_ret_three_m = three_m_cal_data[nav_col].mean()
            # 近半年收益
            six_m_cal_data = cash_nv.loc[six_month_date:].copy()
            interval_ret_six_m = six_m_cal_data[nav_col].mean()
            # 今年以来收益
            base_year_cal_data = cash_nv.loc[base_year_date:].copy()
            interval_ret_base_year = base_year_cal_data[nav_col].mean()

        elif nav_col == 'DailyProfit':
            # 近一个月收益

            one_m_cal_data = cash_nv.loc[one_month_date:].copy()
            inner_period = (one_m_cal_data.dropna(subset=['DailyProfit'])['trade_dt'].iloc[-1] -
                            one_m_cal_data.dropna(subset=['DailyProfit'])['trade_dt'].iloc[0]).days
            interval_ret_one_m = one_m_cal_data['DailyProfit'].sum() / 10000 / inner_period * 365

            # 近三个月收益
            three_m_cal_data = cash_nv.loc[three_month_date:].copy()
            inner_period = (three_m_cal_data.dropna(subset=['DailyProfit'])['trade_dt'].iloc[-1] -
                            three_m_cal_data.dropna(subset=['DailyProfit'])['trade_dt'].iloc[0]).days
            interval_ret_three_m = three_m_cal_data['DailyProfit'].sum() / 10000 / inner_period * 365
            # 近半年收益

            six_m_cal_data = cash_nv.loc[six_month_date:].copy()
            inner_period = (six_m_cal_data.dropna(subset=['DailyProfit'])['trade_dt'].iloc[-1] -
                            six_m_cal_data.dropna(subset=['DailyProfit'])['trade_dt'].iloc[0]).days
            interval_ret_six_m = six_m_cal_data['DailyProfit'].sum() / 10000 / inner_period * 365
            # 今年以来收益

            base_year_cal_data = cash_nv.loc[base_year_date:].copy()
            inner_period = (cash_nv.dropna(subset=['DailyProfit'])['trade_dt'].iloc[-1] -
                            cash_nv.dropna(subset=['DailyProfit'])['trade_dt'].iloc[0]).days
            interval_ret_base_year = base_year_cal_data['DailyProfit'].sum() / 10000 / inner_period * 365

        elif nav_col == 'net_value':
            # 近一个月收益
            one_m_cal_data = cash_nv.loc[one_month_date:].copy()
            inner_period = (one_m_cal_data.dropna(subset=['net_value'])['trade_dt'].iloc[-1] -
                            one_m_cal_data.dropna(subset=['net_value'])['trade_dt'].iloc[0]).days
            interval_ret_one_m = (one_m_cal_data.dropna(subset=['net_value'])['net_value'].iloc[-1] /
                                  one_m_cal_data.dropna(subset=['net_value'])['net_value'].iloc[
                                      0] - 1) / inner_period * 365

            # 近三个月收益

            three_m_cal_data = cash_nv.loc[three_month_date:].copy()
            inner_period = (three_m_cal_data.dropna(subset=['net_value'])['trade_dt'].iloc[-1] -
                            three_m_cal_data.dropna(subset=['net_value'])['trade_dt'].iloc[0]).days
            interval_ret_three_m = (three_m_cal_data.dropna(subset=['net_value'])['net_value'].iloc[-1] /
                                    three_m_cal_data.dropna(subset=['net_value'])['net_value'].iloc[
                                        0] - 1) / inner_period * 365
            # 近半年收益

            six_m_cal_data = cash_nv.loc[six_month_date:].copy()
            inner_period = (six_m_cal_data.dropna(subset=['net_value'])['trade_dt'].iloc[-1] -
                            six_m_cal_data.dropna(subset=['net_value'])['trade_dt'].iloc[0]).days
            interval_ret_six_m = (six_m_cal_data.dropna(subset=['net_value'])['net_value'].iloc[-1] /
                                  six_m_cal_data.dropna(subset=['net_value'])['net_value'].iloc[
                                      0] - 1) / inner_period * 365
            # 今年以来收益

            base_year_cal_data = cash_nv.loc[base_year_date:].copy()
            inner_period = (base_year_cal_data.dropna(subset=['net_value'])['trade_dt'].iloc[-1] -
                            base_year_cal_data.dropna(subset=['net_value'])['trade_dt'].iloc[0]).days
            interval_ret_base_year = (base_year_cal_data.dropna(subset=['net_value'])['net_value'].iloc[-1] /
                                      base_year_cal_data.dropna(subset=['net_value'])['net_value'].iloc[
                                          0] - 1) / inner_period * 365

        else:
            interval_ret_one_m = None
            interval_ret_three_m = None
            interval_ret_six_m = None
            interval_ret_base_year = None

            print(f'{finprocode} 净值数据不符合标准，收益为None......')

        indicator_ser = pd.Series()
        # 近一个月收益
        if one_month_date < begin_date:
            interval_ret_one_m = None
        indicator_ser['interval_ret_one_m'] = interval_ret_one_m

        # 近三个月收益
        if three_month_date < begin_date:
            interval_ret_three_m = None

        indicator_ser['interval_ret_three_m'] = interval_ret_three_m
        # 近半年收益
        if six_month_date < begin_date:
            interval_ret_six_m = None

        indicator_ser['interval_ret_six_m'] = interval_ret_six_m
        # 今年以来收益
        if base_year_date < begin_date:
            interval_ret_base_year = None

        indicator_ser['interval_ret_base_year'] = interval_ret_base_year
        indicator_ser.name = finprocode
        return indicator_ser
    else:
        print('数据不足')
        return None


if __name__ == '__main__':
    finprocode = 1303326
    from database.read.read_py_base import PyReader

    reader = PyReader()
    nv_data = reader.get_net_value(cp_id=finprocode)
    nv_data = nv_data[['FinProCode', 'trade_dt', 'yield_7_days_annual']]
    nv_data = nv_data.rename(columns={'yield_7_days_annual': 'LatestWeeklyYield'})
    ret = cal_cash_ret(finprocode=finprocode, nv_data=nv_data)
