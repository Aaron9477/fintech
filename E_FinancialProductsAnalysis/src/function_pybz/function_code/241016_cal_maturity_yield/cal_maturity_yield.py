# -*- coding: utf-8 -*-
"""
    根据苏银理财需求，过滤产品
"""
import copy

import pandas as pd
import numpy as np
import argparse
from enum import Enum


# 筛选存续期产品
def get_product_exist(input):
    input_df = input.copy()
    # 最短持有期一年左右、固定收益类、22年后运作的产品
    input_df = input_df[(input_df['MinInvestDay'] > 359) & (input_df['MinInvestDay'] < 374) &
                        (input_df['InvestmentType'] == '固定收益类') & (input_df['product_establish_date'] > '2022-01-01')]
    return input_df


def preprocess(input_df):
    def get_main_product_ind(data_set_RegistrationCode):
        ProductTypes = data_set_RegistrationCode['ProductType']
        tags = ['母产品', '产品', '子产品']
        for tag in tags:
            if tag in ProductTypes.values:
                return ProductTypes[ProductTypes == tag].index[0]

    # 筛选子产品 all_data_df
    RegistrationCodes = list(set(input_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = input_df[input_df['RegistrationCode'] == RegistrationCode]
        data_set_RegistrationCode = data_set_RegistrationCode.sort_values(by=['AssetValue'], ascending=False)
        if len(data_set_RegistrationCode.dropna(subset=['AssetValue']).index) > 0:
            data_set_RegistrationCode = data_set_RegistrationCode.dropna(subset=['AssetValue'])
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    output_df = input_df[input_df.index.isin(RegistrationCode_mainind)]

    return output_df


def get_target_prod(all_data_df):
    output_df = preprocess(all_data_df)
    # 筛选符合时间要求的产品
    output_df = get_product_exist(output_df)
    return output_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--maturity_yield_file', type=str, help='maturity_yield_file', default='../../../data_pybz/py_理财产品到期收益率_全部产品_241016.csv')
    args = parser.parse_args()

    maturity_yield_file = args.maturity_yield_file

    all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_24Q2_240923.csv'

    all_data_df = pd.read_csv(all_data_file)
    maturity_yield_df = pd.read_csv(maturity_yield_file)
    maturity_yield_df = maturity_yield_df[['cp_id', 'actual_yield']]

    target_df = get_target_prod(all_data_df)

    target_df = target_df.merge(maturity_yield_df, left_on='FinProCode', right_on='cp_id', how='left')

    target_df.to_excel('test.xlsx')

