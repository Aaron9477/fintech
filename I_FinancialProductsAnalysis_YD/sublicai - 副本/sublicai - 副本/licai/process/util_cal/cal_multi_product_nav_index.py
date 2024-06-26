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

from tools.date_util import NatureDateUtils


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


def CalWeekFreqNavData(net_value):
    """
    理财净值数据降到周频处理
    :param net_value:  df [['FinProCode', 'EndDate', 'net_value']]
    :return:
    """
    # 检查数据
    begin_date = net_value['trade_dt'].iloc[0].strftime('%Y%m%d')
    end_date = net_value['trade_dt'].iloc[-1].strftime('%Y%m%d')

    if net_value.empty:
        raise ValueError('该类别没有净值数据')
    # 数据长变宽
    net_value_nv = net_value[['FinProCode', 'trade_dt', 'net_value']].drop_duplicates(
        subset=['FinProCode', 'trade_dt']).set_index(
        ['trade_dt', 'FinProCode']).unstack()  # 长数据变为宽数据，去重是因为一些产品有多条记录，如上银理财中出现
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

    net_value_nv_week = net_value_nv_week.reset_index()

    net_value_nv_week.columns = ['trade_dt','nav_w','day_week']
    net_value_nv_week['FinProCode'] = net_value['FinProCode'].iloc[0]
    net_value_nv_week = net_value_nv_week[['FinProCode','trade_dt','nav_w']]
    net_value_nv_week = net_value_nv_week.dropna(subset=['nav_w'])
    return net_value_nv_week


if __name__ == '__main__':
    begin_date = '20220101'
    end_date = '20230630'

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
