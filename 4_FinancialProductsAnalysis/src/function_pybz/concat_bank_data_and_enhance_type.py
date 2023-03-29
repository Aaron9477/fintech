# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤二：计算各个理财产品大类资产的配比情况
"""
import copy

import pandas as pd
import numpy as np
import argparse
from enum import Enum


def get_final_enhance_type(row):
    if isinstance(row['enhance_type_asset_q4'], str):
        if row['enhance_type_asset_q4'] != '底层数据未披露':
            return row['enhance_type_asset_q4']
        elif isinstance(row['enhance_type_asset_q3'], str):
            return row['enhance_type_asset_q3']
        else:
            return row['enhance_type_asset_q4']
    else:
        return row['enhance_type_asset_q3']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='金融产品资产配置表映射后.xlsx')
    parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--series_name_file', type=str, help='series_name_file', default='../data_pybz/out5.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    args = parser.parse_args()

    if args.statistics_date == '2022-09-30':
        target_file = '../data_pybz/pyjy_bank_wealth_product_0930.csv'
    elif args.statistics_date == '2022-12-31':
        # target_file = '../data_pybz/pyjy_bank_wealth_product_0306.csv'
        target_file = '../data_pybz/pyjy_bank_wealth_product_0321.csv'
    else:
        raise ValueError

    fix_enhance_q3 = '22年Q3/固收增强分类结果.xlsx'
    fix_enhance_q4 = '固收增强分类结果.xlsx'

    target_df = pd.read_csv(target_file)
    fix_enhance_q3_df = pd.read_excel(fix_enhance_q3)[['FinProCode', 'enhance_type_asset']]
    fix_enhance_q4_df = pd.read_excel(fix_enhance_q4)[['FinProCode', 'enhance_type_asset']]

    fix_enhance_q3_df.rename(columns={'enhance_type_asset': 'enhance_type_asset_q3'}, inplace=True)
    fix_enhance_q4_df.rename(columns={'enhance_type_asset': 'enhance_type_asset_q4'}, inplace=True)

    target_df = target_df.merge(fix_enhance_q3_df, on='FinProCode', how='left')
    target_df = target_df.merge(fix_enhance_q4_df, on='FinProCode', how='left')

    target_df['enhance_type_asset_final'] = target_df.apply(lambda x: get_final_enhance_type(x), axis=1)

    RegistrationCode_list = list(target_df['RegistrationCode'])
    enhance_type_asset_final_list = list(target_df['enhance_type_asset_final'])
    RegistrationCode_dict = dict()
    for i in range(len(RegistrationCode_list)):
        if isinstance(enhance_type_asset_final_list[i], str):
            RegistrationCode_dict[RegistrationCode_list[i]] = enhance_type_asset_final_list[i]

    enhance_type_asset_append_list = []
    for i in range(len(RegistrationCode_list)):
        if RegistrationCode_list[i] in RegistrationCode_dict.keys():
            enhance_type_asset_append_list.append(RegistrationCode_dict[RegistrationCode_list[i]])
        else:
            enhance_type_asset_append_list.append(np.nan)

    target_df['enhance_type_asset_append'] = enhance_type_asset_append_list

    target_df.to_excel('bank表增加固收加分类.xlsx')