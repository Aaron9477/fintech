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
    # 最短持有期一年左右的产品
    input_df = input_df[(input_df['MinInvestDay'] > 359) & (input_df['MinInvestDay'] < 374) & (input_df['RiskLevel'] == '中低')]
    # # 22年年中仍然存续的产品
    # input_df = input_df[(((input_df['MaturityDate'].isnull()) | (input_df['MaturityDate'] >= '20220101')))
    #                     & (input_df['product_establish_date'] <= '20221231')]
    # 22年年中处于投资期的产品
    input_df = input_df[(input_df['invest_end_date'] >= '2022-01-01') & (input_df['invest_end_date'] <= '2022-12-31')]
    return input_df


def preprocess(input_df):
    # 筛选符合时间要求的产品
    input_df = get_product_exist(input_df)

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../../../data_pybz/pybz_到期收益表.csv')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    args = parser.parse_args()

    input_file = args.input_file

    if args.statistics_date == '2022-09-30':
        target_file = '../../../data_pybz/pyjy_bank_wealth_product_0930.csv'
    elif args.statistics_date == '2022-12-31':
        # target_file = '../data_pybz/pyjy_bank_wealth_product_0306.csv'
        target_file = '../../../data_pybz/pyjy_bank_wealth_product_0321.csv'
    else:
        raise ValueError

    target_df = pd.read_csv(target_file)
    input_df = pd.read_csv(input_file)

    target_df = target_df.merge(input_df, left_on='FinProCode', right_on='cp_id', how='left')
    target_df = preprocess(target_df)

    target_df.to_excel('test.xlsx')

