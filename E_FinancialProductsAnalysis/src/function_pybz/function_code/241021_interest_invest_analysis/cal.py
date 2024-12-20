# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤二：计算各个理财产品大类资产的配比情况
"""
import copy
import pandas as pd
import numpy as np
import argparse
from enum import Enum

from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_filesV2
from func import choose_product_mother_son, get_product_exist

time_list = ['2021-12-31', '2022-06-30', '2022-12-31', '2023-06-30', '2023-12-31', '2024-06-30']


# 前处理模块
def df_preprocess(input_df, all_data_df, statistics_date):
    # 筛选存续期产品
    all_data_df = get_product_exist(all_data_df, statistics_date)

    # 筛选子产品 all_data_df
    all_data_df = choose_product_mother_son(all_data_df)
    all_data_df = all_data_df['FinProCode']
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    return input_df


# 筛选权益类理财产品
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--input_file', type=str, help='input_file', default='金融产品资产配置表映射后.xlsx')
    # parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2024-06-30')
    args = parser.parse_args()

    statistics_date = args.statistics_date

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_filesV2(args.statistics_date)

    try:
        all_data_df = pd.read_csv(all_data_file)
    except:
        all_data_df = pd.read_csv(all_data_file, encoding='gbk')

    raw_asset_data = all_data_df.copy()

    # 数据前处理
    raw_asset_data = df_preprocess(raw_asset_data, all_data_df, statistics_date)

    raw_asset_data = raw_asset_data[raw_asset_data['InvestmentType'] == '权益类']

    raw_asset_data.to_excel('权益类理财产品筛选.xlsx')