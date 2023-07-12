# -*- coding: utf-8 -*-
"""
    获取用于检查的代销数据
"""
import copy

import pandas as pd
import numpy as np
import argparse
from enum import Enum


# 筛选存续期产品
def get_product_exist(input, statistics_date):
    input_df = input.copy()

    input_df = input_df[(((input_df['MaturityDate'].isnull()) | (input_df['MaturityDate'] > statistics_date)))
                        & (input_df['product_establish_date'] < statistics_date)]
    return input_df


def preprocess(input_df, statistics_date):
    # 筛选存续期产品
    input_df = get_product_exist(input_df, statistics_date)

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
    parser.add_argument('--input_file', type=str, help='input_file', default='基础数据_增加销售费率.xlsx')
    parser.add_argument('--daixiao_file', type=str, help='daixiao_file', default='V2_代销存续在_230101至230526.xlsx')
    args = parser.parse_args()

    input_df = pd.read_excel(args.input_file)
    daixiao_df = pd.read_excel(args.daixiao_file)

    input_df = preprocess(input_df, '2023-05-01')
    daixiao_df = daixiao_df[(daixiao_df['代销开始日'] < '2023/05/30') & (daixiao_df['代销结束日'] > '2023/05/01')]

    res_df = pd.merge(daixiao_df, input_df, how='inner', left_on='普益代码', right_on='FinProCode')

    res_df.to_excel('用于检查的代销数据.xlsx')