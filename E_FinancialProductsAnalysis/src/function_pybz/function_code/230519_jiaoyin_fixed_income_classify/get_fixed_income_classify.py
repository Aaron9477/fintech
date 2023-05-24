# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/5/22 10:31
# @Author    : Wangyz5
# @File      : get_fixed_income_classify
# @Project   : E_FinancialProductsAnalysis
# @Function  ：产出向客户提供的固收+分类体系
# --------------------------------

import pandas as pd
import numpy as np
import argparse

from E_FinancialProductsAnalysis.src.function_pybz.func import shorter_company_name
from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_files, get_intermediate_files


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    parser.add_argument('--output_file1', type=str, help='output_file1', default='底层数据.xlsx')
    parser.add_argument('--output_file2', type=str, help='output_file2', default='固收类理财分类.xlsx')
    args = parser.parse_args()

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    intermediate_files_files = get_intermediate_files(args.statistics_date)
    fixed_income_file = intermediate_files_files[0]

    fixed_income_df = pd.read_excel(fixed_income_file)

    fixed_income_df = fixed_income_df[['CompanyName', 'product_name', 'RegistrationCode', 'AssetValue', '固收', '非标资产',
                                       '权益类', '商品及衍生品', 'QDII', '公募基金', '其他', '前十大_权益类', '前十大_非标资产',
                                       '前十大_商品及衍生品', '前十大_QDII', '资产明细是否有含权基金', '非标资产投资比例', 'enhance_type_asset']]

    # 转化为万元
    fixed_income_df['AssetValue'] = fixed_income_df['AssetValue'] / 10000
    # 对未披露规模的非标修改名称
    fixed_income_df['非标资产投资比例'].replace(99, '披露非标投资，但未披露规模', inplace=True)
    # 理财子名称改用缩写
    shorter_company_name(fixed_income_df, 'CompanyName')

    short_fixed_income_df = fixed_income_df[['CompanyName', 'product_name', 'RegistrationCode', 'AssetValue', 'enhance_type_asset']]

    fixed_income_df.to_excel(args.output_file1)
    short_fixed_income_df.to_excel(args.output_file2)





