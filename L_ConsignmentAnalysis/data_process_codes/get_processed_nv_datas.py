# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月20日16:11:33
# @Author    : Noah Zhan
# @File      : get_processed_nv_datas
# @Project   : 银行理财代销图鉴
# @Function  ：将从数据库中取出的产品净值数据进行预处理
# --------------------------------

import numpy as np
import pandas as pd
from typing import Union
from tqdm import tqdm
import warnings
import datetime

def get_processed_nv_datas(net_value_df_all:pd.DataFrame,
                           lc_codes:list,
                           begin_date: Union[str,None] = None,
                           end_date: Union[str,None] = None,
                           is_cash=False,
                           return_failed=False):
    #调用get_processed_nv_data，批量返回数据
    warnings.filterwarnings('ignore')
    result = pd.DataFrame()
    failed = []
    for lc_code,is_cash_single in tqdm(zip(lc_codes,is_cash),desc='get_processed_nv_datas'):
        try:
            result = pd.concat([result,get_processed_nv_data(net_value_df_all=net_value_df_all,lc_code=lc_code,begin_date= None,end_date = None,is_cash = is_cash_single)],axis=0)
        except:
            failed.append(lc_code)
    print("数据获取错误的产品代码有：",failed)
    warnings.filterwarnings('default')
    if return_failed: return result,failed
    else: return result

def get_processed_nv_data(net_value_df_all,lc_code,begin_date,end_date,is_cash=False):
    # net_value_df_all = reader.get_code_net_value_from_local(begin_date=begin_date, end_date=end_date)
    # groupd = net_value_df_all.groupby('FinProCode')
    net_value_df = net_value_df_all[net_value_df_all['FinProCode'] == lc_code].copy()
    net_value_df = net_value_df.reset_index(drop=True)
    data = GetProcessedNavData(net_value_df=net_value_df, licai_code=lc_code, begin_date=begin_date,
                               end_date=end_date, is_cash=is_cash)
    # 防止现金管理类识别错误，导致7日年化的数据却采用了净值计算
    nav_column = data.columns[2]
    if is_cash:
        if nav_column in ['LatestWeeklyYield']:
            return data
        else:
            return None
    else:
        if nav_column in ['AccumulatedUnitNV','UnitNV']:
            return data
        else:
            return None
        
def GetProcessedNavData(net_value_df: pd.DataFrame,
                        licai_code: str,
                        begin_date: Union[str,None] = None,
                        end_date: Union[str,None] = None,
                        is_cash: object = False,
                        spec_column: object = None) -> Union[pd.DataFrame, None]:
    """
    获取单个产品的净值，自动获取净值字段，如果是现金管理产品，根据7日年化收益率、万分收益和净值 自动转化为7日年化收益率
    :param net_value_df:
    :param is_cash: True 代表现金管理产品，False 代表非现金产品
    :param spec_column: 特殊指定相应字段，针对特殊个例情况
    :param licai_code:
    :param begin_date:
    :param end_date:
    :return: df
    """

    if net_value_df.empty:
        return None
    # 特殊处理：
    if spec_column is not None:
        return net_value_df[['FinProCode', 'EndDate', spec_column]]
    else:
        # 正常处理
        if begin_date is None:
            begin_date = datetime.datetime.strftime(net_value_df['EndDate'].iloc[0],'%Y%m%d')
        if end_date is None:
            end_date = datetime.datetime.strftime(net_value_df['EndDate'].iloc[-1],'%Y%m%d')

        net_value_df['UnitNVRestored'] = np.nan
        period = (datetime.datetime.strptime(end_date, '%Y%m%d') - datetime.datetime.strptime(begin_date,'%Y%m%d')).days
        not_null_count = net_value_df[
            ['DailyProfit', 'LatestWeeklyYield', 'UnitNV', 'AccumulatedUnitNV', 'UnitNVRestored']].apply(
            lambda x: len(x.dropna()) / len(x))
        if not is_cash:
            # 非现金产品，在复权净值、单位净值和累计净值中挑选
            if not_null_count['UnitNVRestored'] > 0:
                return net_value_df[['FinProCode', 'EndDate', 'UnitNVRestored']]

            if not_null_count['AccumulatedUnitNV'] == 0:  # 判断累计净值数据是否为空
                if not_null_count['UnitNV'] == 0:
                    return None
                else:
                    return net_value_df[['FinProCode', 'EndDate', 'UnitNV']]
            else:
                if not_null_count['UnitNV'] == 0:
                    return net_value_df[['FinProCode', 'EndDate', 'AccumulatedUnitNV']]
                else:
                    # 判断两个数据是否有差异数据
                    tmp = net_value_df[['UnitNV', 'AccumulatedUnitNV']].dropna(subset=['UnitNV', 'AccumulatedUnitNV'])
                    if tmp.empty:
                        return None
                    else:
                        tmp_diff_logic = tmp.apply(lambda x: 1 if x.UnitNV != x.AccumulatedUnitNV else 0, axis=1).sum()
                        if tmp_diff_logic == 0:  # 单位净值和累计净值数据一致
                            # 打分选择字段
                            not_null_count = not_null_count[['UnitNV', 'AccumulatedUnitNV']].copy()
                            period_nav_not_null_period = pd.Series()
                            try:
                                period_nav_not_null_period['UnitNV'] = (net_value_df.dropna(subset=['UnitNV'])[
                                                                            'EndDate'].iloc[-1] -
                                                                        net_value_df.dropna(subset=['UnitNV'])[
                                                                            'EndDate'].iloc[0]).days / period
                            except IndexError:
                                period_nav_not_null_period['UnitNV'] = 0
                            try:
                                period_nav_not_null_period['AccumulatedUnitNV'] = (net_value_df.dropna(
                                    subset=['AccumulatedUnitNV'])['EndDate'].iloc[-1] - net_value_df.dropna(
                                    subset=['AccumulatedUnitNV'])[
                                                                                       'EndDate'].iloc[
                                                                                       0]).days / period + 0.0001
                            except IndexError:
                                period_nav_not_null_period['AccumulatedUnitNV'] = 0
                            score = period_nav_not_null_period * 0.6 + not_null_count * 0.4
                            score = score.sort_values()
                            chosed_nav_col = score.idxmax()
                            return net_value_df[['FinProCode', 'EndDate', chosed_nav_col]]
                        else:
                            return net_value_df[['FinProCode', 'EndDate', 'AccumulatedUnitNV']]
        else:
            # 现金管理产品，在7日年化、万分收益和净值中挑选
            # 万分收益和7日年化打分判断
            not_null_count_cash = not_null_count[['DailyProfit', 'LatestWeeklyYield']].copy()
            period_cash_not_null_period = pd.Series()
            try:
                period_cash_not_null_period['DailyProfit'] = (net_value_df.dropna(subset=['DailyProfit'])[
                                                                  'EndDate'].iloc[-1] -
                                                              net_value_df.dropna(subset=['DailyProfit'])[
                                                                  'EndDate'].iloc[0]).days / period
            except IndexError:
                period_cash_not_null_period['DailyProfit'] = 0
            try:
                period_cash_not_null_period['LatestWeeklyYield'] = (net_value_df.dropna(subset=['LatestWeeklyYield'])[
                                                                        'EndDate'].iloc[-1] -
                                                                    net_value_df.dropna(subset=['LatestWeeklyYield'])[
                                                                        'EndDate'].iloc[0]).days / period + 0.0001
            except IndexError:
                period_cash_not_null_period['LatestWeeklyYield'] = 0
            score = period_cash_not_null_period * 0.6 + not_null_count_cash * 0.4
            score = score.sort_values()
            if score.max() >= 0.1:
                # 选择7日年化或者万份收益
                chosed_cash__col = score.idxmax()
                if chosed_cash__col == 'LatestWeeklyYield':
                    return net_value_df[['FinProCode', 'EndDate', 'LatestWeeklyYield']].copy()
                elif chosed_cash__col == 'DailyProfit':
                    net_value_df = net_value_df[['FinProCode', 'EndDate', 'DailyProfit']].copy()
                    net_value_df['LatestWeeklyYield'] = net_value_df['DailyProfit'].rolling(7).apply(
                        lambda x: np.power(x.apply(lambda i: (1 + i / 10000)).prod(), 365 / 7) - 1)
                    return net_value_df[['FinProCode', 'EndDate', 'LatestWeeklyYield']].copy()

                else:
                    raise ValueError('impossible error......')
            else:
                # 如果得分都很低的话，就采用净值来判断
                nav_df = GetProcessedNavData(net_value_df=net_value_df,licai_code=licai_code, begin_date=begin_date, end_date=end_date,
                                             is_cash=False)
                if nav_df is None:
                    return None
                else:
                    nav_df.columns = ['FinProCode', 'EndDate', 'net_value']
                    # 判断小数位数
                    digital_num = len(str(nav_df['net_value'].dropna().iloc[0]).split('.')[1]) + 1
                    if digital_num >= 6:
                        nav_df['ret'] = nav_df['net_value'].pct_change()
                        nav_df['LatestWeeklyYield'] = nav_df['ret'].rolling(7).apply(lambda x: (x.mean() * 365))
                        return nav_df[['FinProCode', 'EndDate', 'LatestWeeklyYield']]

                    else:
                        raise ValueError('现金管理类产品，净值数据精度不足，不能转化为7日年化收益......')