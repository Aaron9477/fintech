# -*- coding: utf-8 -*-
"""
    提取挂钩衍生品的理财产品
"""
import pandas as pd
import numpy as np
import argparse

from E_FinancialProductsAnalysis.src.function_pybz.func import choose_product_mother_son, get_product_exist
from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_files


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2024-06-30')

    args = parser.parse_args()
    reflect_file = args.reflect_file
    statistics_date = args.statistics_date

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    input_df = pd.read_csv(all_data_file)
    all_data_df = pd.read_csv(all_data_file)

    all_data_df = choose_product_mother_son(all_data_df)
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    filtered_df = input_df[
        (input_df['old_invest_scope'].str.contains('衍生金融工具', na=False)) &
        (
                input_df['product_name'].str.contains('联动', na=False) |
                input_df['product_name'].str.contains('挂钩', na=False)
        )]

    filtered_df.to_excel('filtered_file.xlsx')