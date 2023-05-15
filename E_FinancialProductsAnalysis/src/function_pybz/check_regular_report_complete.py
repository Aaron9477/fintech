# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/5/5 11:07
# @Author    : Wangyd5
# @File      : check_regular_report_complete
# @Project   : sublicai
# @Function  ：检查理财子是否披露完全定期公告
# --------------------------------

import os

import pandas as pd
import numpy as np
import argparse
from enum import Enum

import datetime

from func import get_product_exist, choose_product_mother_son


def df_preprocess(input_df, all_data_df, statistics_date):
    # 筛选子产品 all_data_df
    all_data_df = choose_product_mother_son(all_data_df)['FinProCode']
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    # 筛选存续期产品
    input_df = get_product_exist(input_df, statistics_date)

    return input_df

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='金融产品资产配置表映射后.xlsx')
    parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    args = parser.parse_args()

    if args.statistics_date == '2022-09-30':
        target_file = '../data_pybz/pyjy_bank_wealth_product_0930.csv'
        asset_portfolio_file = '../data_pybz/pybz_金融产品资产配置_22年三季报_230314.csv'
    elif args.statistics_date == '2022-12-31':
        target_file = '../data_pybz/bank_wealth_product_base_pyjy_1231.csv'
        asset_portfolio_file = '../data_pybz/pybz_金融产品资产配置_22年四季报_230503.csv'
    elif args.statistics_date == '2023-03-31':
        target_file = '../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
        asset_portfolio_file = '../data_pybz/pybz_金融产品资产配置_23年Q1_230513.csv'
    else:
        raise ValueError

    end_date = '20230331'

    bank_wealth_product_df = pd.read_csv(target_file)
    asset_portfolio_df = pd.read_csv(asset_portfolio_file)

    # 筛选存续产品&非子产品：属于理财半年报投资方向统计范畴
    bank_wealth_product_df = df_preprocess(bank_wealth_product_df, bank_wealth_product_df, args.statistics_date)

    time_col_list = ['product_establish_date', 'MaturityDate']
    for time_col in time_col_list:
        bank_wealth_product_df[time_col] = pd.to_datetime(bank_wealth_product_df[time_col])

    bank_wealth_product_df['是否需要发季报'] = np.nan
    bank_wealth_product_df['是否已发季报'] = np.nan

    # 筛选产品是否需要发季报
    bank_wealth_product_df['product_establish_date_plus_90'] = bank_wealth_product_df['product_establish_date'].map(
        lambda x: x + datetime.timedelta(days=90))
    bank_wealth_product_df['MaturityDate_minus_90'] = bank_wealth_product_df['MaturityDate'].map(
        lambda x: x - datetime.timedelta(days=90))
    bank_wealth_product_df.loc[(bank_wealth_product_df['product_establish_date_plus_90'] <= end_date) &
                               (bank_wealth_product_df['MaturityDate_minus_90'] >= end_date), '是否需要发季报'] = 1
    bank_wealth_product_df['是否需要发季报'].fillna(0, inplace=True)

    # 是否发了季报
    # 已发布定期报告的产品编码
    asset_portfolio_regis_code = list(asset_portfolio_df['product_code'].unique())
    bank_wealth_product_df.loc[bank_wealth_product_df['RegistrationCode'].isin(asset_portfolio_regis_code), '是否已发季报'] = 1
    bank_wealth_product_df['是否已发季报'].fillna(0, inplace=True)

    bank_wealth_product_df.to_excel('test2.xlsx')

    # info_df_exclude = info_df[~info_df['RegistrationCode'].isin(asset_portfolio_regis_code)]
    # info_df_exclude = info_df_exclude.sort_values(['CompanyName','AssetValue'],ascending=[False,False])
    # info_df_exclude[['CompanyName',	'FinProCode',	'product_name'	,'SecuState',	'PopularizeStDate',	'RaisingType',	'EndDate',	'AssetValue',	'ProductType',	'product_establish_date',
    #                   'MaturityDate',	'RegistrationCode']].to_csv('M:\\Device\\C\\Users\\wangyd5\\Downloads\\info_df_exclude_4.csv')


# end_date = '20221231'
# reader = JuyuanReader()
# bank_wealth_product_df = select_product_info_cache(end_date)
# # 成立以来超过三个月并且剩余存续期超过三个月 （90天）
# bank_wealth_product_df['product_establish_date_plus_90'] = bank_wealth_product_df['product_establish_date'].map(lambda x:x + datetime.timedelta(days=90))
# bank_wealth_product_df['MaturityDate_minus_90'] = bank_wealth_product_df['MaturityDate'].map(lambda x:x - datetime.timedelta(days=90))
# info_df = bank_wealth_product_df.loc[(bank_wealth_product_df['product_establish_date_plus_90'] <= end_date) &
#                                      (bank_wealth_product_df['MaturityDate_minus_90'] >= end_date) &
#                                      (bank_wealth_product_df['ProductType'].isin(['产品','母产品']))]
#
# path = os.path.join(os.path.join(project_path, 'docs'),'py_assset_portfolio_4.csv')
# asset_portfolio = pd.read_csv(path)
#
# asset_portfolio_regis_code = list(asset_portfolio['登记编码'].unique())
#
# info_df_exclude = info_df[~info_df['RegistrationCode'].isin(asset_portfolio_regis_code)]
# info_df_exclude = info_df_exclude.sort_values(['CompanyName','AssetValue'],ascending=[False,False])
# info_df_exclude[['CompanyName',	'FinProCode',	'product_name'	,'SecuState',	'PopularizeStDate',	'RaisingType',	'EndDate',	'AssetValue',	'ProductType',	'product_establish_date',
#                   'MaturityDate',	'RegistrationCode']].to_csv('M:\\Device\\C\\Users\\wangyd5\\Downloads\\info_df_exclude_4.csv')
#
