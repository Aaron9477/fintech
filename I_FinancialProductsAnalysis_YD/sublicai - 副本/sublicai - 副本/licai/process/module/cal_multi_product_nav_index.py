# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/12/11 15:46 
# @Author    : Wangyd5 
# @File      : cal_multi_product_nav_index
# @Project   : sublicai
# @Function  ：根据多个产品净值数据计算指数序列
# --------------------------------

import numpy as np
import pandas as pd
from cscfist.model.net_value_indicator_model.net_value_indicator import NetValueIndicator
from sublicai.tools.date_util import NatureDateUtils
import os
from sublicai.database.read.read_juyuan_base import JuyuanReader
from sublicai.tools.tools import Timer,tool_set
import datetime

def dot_value(ret_df: pd.DataFrame, weight_ser: pd.Series) -> pd.DataFrame:
    """
    用于计算理财子的加权收益
    :param ret_df:  收益矩阵
    :param weight_ser: 市值加权向量
    :return:
    """
    ser: pd.Series = pd.Series()
    for index, row in ret_df.iterrows():
        tmp_df = pd.DataFrame({'ret': row.values, 'w': weight_ser.values}, index=weight_ser.index)
        tmp_df = tmp_df.dropna()
        ret = tmp_df['ret'].dot(tmp_df['w']) / tmp_df['w'].sum()
        ser[index] = ret
    return ser


def CalWeekFreqNavData(net_value,begin_date,end_date):
    """
    理财净值数据降到周频处理
    :param net_value:  df [['FinProCode', 'EndDate', 'net_value']]
    :param begin_date: '20220101'
    :param end_date: '20220630'
    :param end_date: mkt_ser
    :return:
    """
    # 检查数据
    if net_value.empty:
        raise ValueError('该类别没有净值数据')
    # 数据长变宽
    net_value_nv = net_value[['FinProCode', 'EndDate', 'net_value']].drop_duplicates(
        subset=['FinProCode', 'EndDate']).set_index(
        ['EndDate', 'FinProCode']).unstack()  # 长数据变为宽数据，去重是因为一些产品有多条记录，如上银理财中出现
    net_value_nv.columns = net_value_nv.columns.droplevel(level=0)
    # 日期处理，数据降频到周频
    business_day = pd.date_range(begin_date, end_date)
    net_value_nv = net_value_nv.reindex(business_day)
    net_value_nv['day_week'] = None
    for x in net_value_nv.index:
        tmp = [str(i) if len(str(i)) > 1 else '0' + str(i) for i in x.isocalendar()]
        tmp = '_'.join(tmp)
        net_value_nv.loc[x, 'day_week'] = tmp[:-3]
    grouped = net_value_nv.groupby('day_week')
    net_value_nv_week = pd.DataFrame([])

    def get_latest_data_beside_friday(ser):
        """ 每周中取距离周五最近的数"""
        ser_denan = ser.dropna()
        if len(ser_denan) == 0:
            return np.nan
        else:
            return ser_denan.tail(1)[0]

    # 对每周找最近的净值数据
    for day_week, tmp_df in grouped:
        if len(tmp_df) < 7:
            continue
        else:
            date = tmp_df.index[-3]  # 取出周五日期
            value = tmp_df.apply(get_latest_data_beside_friday, axis=0)
            value.name = date
            net_value_nv_week = net_value_nv_week.append(value)
    return net_value_nv_week



def CalMultiProductNavIndex(net_value,mkt_value_ser,begin_date,end_date,not_null_threshold=0.3,company=None, investment_type=None):
    """
    计算指数
    :param net_value: df   [['FinProCode', 'EndDate', 'net_value']]
    :param begin_date: '20220101'
    :param end_date: '20220630'
    :param not_null_threshold: 净值数据非空率
    :return: 处理后的净值序列 和 净值计算指标

    """
    # ---------------------------------------------- 处理净值数据 ----------------------------------------------
    # 降频处理净值
    net_value_week = CalWeekFreqNavData(net_value=net_value,begin_date=begin_date,end_date=end_date)
    # 计算空值率（每列）
    net_value_nv_week_cal_notnull = net_value_week.apply(lambda x: 1 - len(x[x.isnull()]) / len(x), axis=0)
    # 选择非空率大于0.3 的产品,如果都不符合 选择非空率最高的前10个产品作为代替
    chosed_col = list(net_value_nv_week_cal_notnull[net_value_nv_week_cal_notnull > not_null_threshold].index)[:-1]
    if len(chosed_col) == 0:
        chosed_col = list(net_value_nv_week_cal_notnull.iloc[:-1].sort_values(ascending=False).index)[:10]
    chosed_not_null_percent = net_value_nv_week_cal_notnull[net_value_nv_week_cal_notnull > not_null_threshold].mean()
    net_value_nv_week_chosed = net_value_week[chosed_col]
    #  对净值线性插值
    net_value_nv_week_interpolate = net_value_nv_week_chosed.interpolate()

    if not mkt_value_ser.dropna().empty:
        mkt_value_ser = mkt_value_ser.reindex(chosed_col).fillna(mkt_value_ser.mean())
    else:
        mkt_value_ser = mkt_value_ser.reindex(chosed_col).fillna(1)
    weight_ser = mkt_value_ser / mkt_value_ser.sum()

    # 计算收益率
    net_value_nv_week_ret = net_value_nv_week_interpolate[net_value_nv_week_interpolate.columns].pct_change()
    # 市值加权,如果没有的，用平均值填充
    cal_data = pd.DataFrame(dot_value(net_value_nv_week_ret, weight_ser), columns=['ret'],
                            index=net_value_nv_week_ret.index)
    cal_data['net_value'] = (1 + cal_data['ret']).cumprod()

    # ---------------------------------------------- 计算指标 ----------------------------------------------
    # 计算资管新规成立来的指标
    begin_date_ = cal_data['net_value'].dropna().index[0]
    end_date_ = cal_data['net_value'].dropna().index[-1]
    period = (end_date_ - begin_date_).days

    if period < 30 * 2:  # 如果日期不足两个月，就不纳入计算
        raise ValueError('数据不足两个月，不参与计算')
    if list(cal_data['net_value'].dropna().unique()) == [1]:
        print('净值数据全部为0，不适合计算，跳过')
        return None

    cal_ret_obj = NetValueIndicator(net_value=cal_data['net_value'].dropna(),
                                    benchmark_close=cal_data['net_value'].dropna(),
                                    risk_free_rate=0.015, period='w',trade_date_list=list(cal_data.index))
    interval_ret = cal_ret_obj.interval_return(is_annual=False)
    interval_ret_annual = cal_ret_obj.interval_return(is_annual=True)
    max_draw_down = cal_ret_obj.max_draw_down()
    sharpe = cal_ret_obj.sharpe()
    calmar = np.nan
    try:
        calmar = cal_ret_obj.calmar()
    except:
        pass
    sortino = cal_ret_obj.sortino()
    volatility_annual = cal_ret_obj.volatility(is_annual=True)

    # 计算近半年以来的指标
    half_year_date = NatureDateUtils.date_period_change(end_date, '-1h')
    half_cal_data = cal_data.loc[half_year_date:].copy()
    interval_ret_half = half_cal_data['net_value'].dropna().iloc[-1] / half_cal_data['net_value'].dropna().iloc[0] - 1
    # 计算最近三个月以来的指标
    three_month_date = NatureDateUtils.date_period_change(end_date, '-3m')
    three_m_cal_data = cal_data.loc[three_month_date:].copy()
    interval_ret_three_m = three_m_cal_data['net_value'].dropna().iloc[-1] / \
                           three_m_cal_data['net_value'].dropna().iloc[0] - 1
    indicator_ser = pd.Series()
    indicator_ser['begin_date'] = begin_date
    indicator_ser['end_date'] = end_date
    indicator_ser['period'] = period
    indicator_ser['interval_ret'] = interval_ret
    indicator_ser['interval_ret_annual'] = interval_ret_annual
    indicator_ser['max_draw_down'] = max_draw_down
    indicator_ser['sharp_ratio'] = sharpe if sharpe >= 0 else 0
    indicator_ser['sortino'] = sortino
    indicator_ser['calmar'] = calmar
    indicator_ser['volatility_annual'] = volatility_annual
    indicator_ser['interval_ret_half'] = interval_ret_half
    indicator_ser['interval_ret_three_m'] = interval_ret_three_m
    indicator_ser['chosed_num'] = len(chosed_col)
    indicator_ser['chosed_not_null_percent'] = chosed_not_null_percent
    chosed_col = [str(x) for x in chosed_col]
    indicator_ser['chosed_code'] = '_'.join(chosed_col)
    indicator_ser['sharp_ratio_original'] = sharpe
    indicator_ser['sharp_ratio_str_negative'] = sharpe if sharpe >= 0 else '小于0'
    indicator_ser['company'] = company
    indicator_ser['investment_type'] = investment_type
    if (company is not None) & (investment_type is not None):
        indicator_ser.name = '_'.join([company, investment_type])
    else:
        indicator_ser.name = ''

    cal_data_net_value = cal_data['net_value'].copy()
    cal_data_net_value.iloc[0] = 1
    cal_data_net_value = cal_data_net_value.fillna(method='ffill')
    cal_data_net_value['company'] = company
    cal_data_net_value['investment_type'] = investment_type
    cal_data_net_value = cal_data_net_value.reindex(
        list(cal_data_net_value.index[-2:]) + list(cal_data_net_value.index[:-2]))
    return indicator_ser, cal_data_net_value



if __name__ == '__main__':

    begin_date = '20220101'
    end_date = '20220930'
    # juyuan_reader = JuyuanReader()
    # # 从文档中获取有效信息
    # product_info = juyuan_reader.get_basic_info_from_csv()
    # product_info = product_info[product_info['FinProCode'].notnull()]
    # product_info = product_info.loc[product_info['ProductType'].isin(['产品','母产品']) &
    #                                 product_info['OperationType'].isin(['开放式净值型','封闭式净值型'])].copy()
    # def judge_cash_type(row):
    #     res = row.inv_type
    #     if res == 1:
    #         return '现金管理类'
    #     else:
    #         return row.InvestmentType
    #
    # product_info['InvestmentType'] = product_info.apply(lambda x:judge_cash_type(x),axis=1)
    # tmp = product_info[product_info['CompanyName'] == '徽银理财有限责任公司'].copy()
    # tmp = tmp[tmp['InvestmentType'] == '混合类']
    # finprocode_list = tmp['FinProCode'].tolist()



































