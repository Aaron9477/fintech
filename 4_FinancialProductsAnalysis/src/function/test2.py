# -*- coding: utf-8 -*-
"""
    基金分析第一步：拉取前十大资产中基金类型
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime
from func import choose_report_detail_table

#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

target_feature = ["name_official", "fund_corp_fundmanagementcompany", "fund_firstinvesttype", "fund_investtype",
                  "return_1y", "return_2y", "return_3y", "return_5y"]
feature_name = ['基金简称', '基金公司', '基金一级分类', '基金二级分类', '一年回报', '二年回报', '三年回报', '五年回报']


def df_preprocess(input_df, all_data_df, statistics_date):
    def get_main_product_ind(data_set_RegistrationCode):
        ProductTypes = data_set_RegistrationCode['ProductType']
        tags = ['母产品', '产品', '子产品']
        for tag in tags:
            if tag in ProductTypes.values:
                return ProductTypes[ProductTypes == tag].index[0]

    output_df = input_df.copy()

    # 筛选子产品 all_data_df
    RegistrationCodes = list(set(all_data_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = all_data_df[all_data_df['RegistrationCode'] == RegistrationCode]
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    all_data_df = all_data_df[all_data_df.index.isin(RegistrationCode_mainind)]

    output_df = output_df.merge(all_data_df, how='inner', on='FinProCode')

    # 筛选公募基金
    output_df = output_df[(output_df['primary_type_chi'] == '基金') & (output_df['secondary_type_chi'] == '公募基金')]

    # 合并基金代码，筛选代码非空的基金
    output_df = output_df[(output_df['SecuCode'].notnull())]

    # 筛选存续期产品
    output_df = output_df[(output_df['MaturityDate'] > statistics_date) & (output_df['product_establish_date'] < statistics_date)]

    return output_df


def code_preprocess(input_list):
    res_list = []
    for x in input_list:
        x = str(x)
        if len(x) > 6:
            x = x[:6]
        x = x.split('.')[0].split(' ')[0]
        res_list.append(x + '.OF')
    return res_list


def split_list_average_n(origin_list, n):
    for i in range(0, len(origin_list), n):
        yield origin_list[i:i + n]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='基金风格稳定度标签(3).xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)

    fund_list = df['证券代码'].values
    fund_str = ','.join(fund_list)

    w.start()
    index = 0

    statistics_date_list = ['2022-12-30', '2021-12-31', '2020-12-31', '2019-12-31', '2018-12-28', '2017-12-29']

    for statistics_date in statistics_date_list:
        wind_return = w.wsd(fund_str, "NAV_adj", statistics_date, statistics_date, "PriceAdj=F")
        fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
        value_list = [fund_value_dict[x] for x in fund_list]
        df[statistics_date] = value_list

    for i in range(len(statistics_date_list) - 1):
        df[statistics_date_list[i][:4] + '收益率'] = df[statistics_date_list[i]] / df[statistics_date_list[i+1]] - 1

    df.to_excel("羽洁姐文件收益统计.xlsx")




