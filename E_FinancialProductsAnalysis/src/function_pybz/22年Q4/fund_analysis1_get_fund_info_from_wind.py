# -*- coding: utf-8 -*-
"""
    基金分析第一步：拉取前十大资产中基金类型
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime

from func import get_trading_day
from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_files

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

    # 筛选存续期产品
    output_df = output_df[(output_df['MaturityDate'] > statistics_date) & (output_df['product_establish_date'] < statistics_date)]

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
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    args = parser.parse_args()

    statistics_date = args.statistics_date

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    trading_day = get_trading_day(statistics_date)

    df = pd.read_csv(top10_file)
    all_data_df = pd.read_csv(all_data_file)[['FinProCode', 'MaturityDate',
                                                   'product_establish_date', 'RegistrationCode', 'ProductType']]

    # 前处理
    df = df_preprocess(df, all_data_df, statistics_date)

    fund_list = code_preprocess(df['SecuCode'].values)
    fund_set = set(fund_list)
    fund_str = ','.join(fund_set)

    w.start()
    index = 0
    for feat in target_feature:
        wind_return = w.wsd(fund_str, feat, trading_day, trading_day, "annualized=0;PriceAdj=F")
        fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
        value_list = [fund_value_dict[x] for x in fund_list]
        df[feature_name[index]] = value_list
        index += 1

    trading_day_before_1y = str(int(trading_day[:4])-1) + trading_day[4:]
    wind_return = w.wsd(fund_str, "NAV_adj", trading_day_before_1y, trading_day_before_1y, "PriceAdj=F")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    value_list = [fund_value_dict[x] for x in fund_list]
    df['统计日一年前净值'] = value_list

    wind_return = w.wsd(fund_str, "NAV_adj", trading_day, trading_day, "PriceAdj=F")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    value_list = [fund_value_dict[x] for x in fund_list]
    df['统计日净值'] = value_list

    df['一年收益率'] = df['统计日净值'] / df['统计日一年前净值'] - 1

    df.to_excel("基金信息_" + statistics_date + ".xlsx")




