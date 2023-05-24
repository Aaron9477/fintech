# -*- coding: utf-8 -*-
"""
function code
"""

import numpy as np


# 资产配置表筛选报告
def choose_report_asset_table(input, statistics_date):
    input_df = input.copy()

    # 筛选周报
    def get_report_index(data_set_RegistrationCode, statistics_date):
        InfoSources = data_set_RegistrationCode['InfoSource']
        if statistics_date == "2022-09-30":
            tags = ['季度投资管理报告']
        elif statistics_date == "2022-06-30":
            tags = ['半年度投资管理报告', '2022二季报', '季度投资管理报告']
        else:
            raise ValueError("statistics_date 错误")

        for tag in tags:
            if tag in InfoSources.values:
                return InfoSources[InfoSources == tag].index

    # 删除InfoSource部分数据多余回车符
    InfoSource_list = list(input_df['InfoSource'])
    InfoSource_list_new = [x.strip() for x in InfoSource_list]
    input_df['InfoSource'] = InfoSource_list_new

    FinProCodes = list(set(input_df['FinProCode'].dropna()))
    RegistrationCode_mainind = []
    for FinProCode in FinProCodes[:]:
        data_set_FinProCode = input_df[input_df['FinProCode'] == FinProCode]
        RegistrationCode_mainind += list(get_report_index(data_set_FinProCode, statistics_date))
    input_df = input_df[input_df.index.isin(RegistrationCode_mainind)]

    return input_df


# 资产投资明细表筛选报告
def choose_report_detail_table(input, statistics_date):
    input_df = input.copy()

    # 筛选周报
    def get_report_index(data_set_RegistrationCode, statistics_date):
        InfoSources = data_set_RegistrationCode['InfoSource']
        if statistics_date == "2022-09-30":
            tags = ['2022三季报']
        elif statistics_date == "2022-06-30":
            tags = ['2022中报', '2022二季报', '2022二季报暨半年报']
        elif statistics_date == "2022-03-31":
            tags = ['2022一季报']
        elif statistics_date == "2021-12-31":
            tags = ['2021年报', '2021四季报']
        else:
            raise ValueError("statistics_date 错误")

        for tag in tags:
            if tag in InfoSources.values:
                return InfoSources[InfoSources == tag].index

    # InfoSource部分数据多余回车符
    InfoSource_list = list(input_df['InfoSource'])
    InfoSource_list_new = [x.strip() for x in InfoSource_list]
    input_df['InfoSource'] = InfoSource_list_new

    FinProCodes = list(set(input_df['FinProCode'].dropna()))
    RegistrationCode_mainind = []
    for FinProCode in FinProCodes[:]:
        data_set_FinProCode = input_df[input_df['FinProCode'] == FinProCode]
        RegistrationCode_mainind += list(get_report_index(data_set_FinProCode, statistics_date))
    input_df = input_df[input_df.index.isin(RegistrationCode_mainind)]

    return input_df


# 资产投资明细表筛选报告
def choose_penetration_data(input):
    input_df = input.copy()

    def get_penetration_index(all_data):
        # 优先使用穿透后数据，其次使用穿透前数据
        tags = ['FCC0000019PL', 'FCC0000019PK']
        PenetrationType = all_data['PenetrationType']
        for tag in tags:
            if tag in PenetrationType.values:
                return PenetrationType[PenetrationType == tag].index

    FinProCodes = list(set(input_df['FinProCode'].dropna()))
    RegistrationCode_mainind = []
    for FinProCode in FinProCodes[:]:
        data_set_FinProCode = input_df[input_df['FinProCode'] == FinProCode]
        RegistrationCode_mainind += list(get_penetration_index(data_set_FinProCode))
    input_df = input_df[input_df.index.isin(RegistrationCode_mainind)]

    return input_df


# 提取母子产品
def choose_product_mother_son(input_df):

    def get_main_product_ind(data_set_RegistrationCode):
        ProductTypes = data_set_RegistrationCode['ProductType']
        tags = ['母产品', '产品', '子产品']
        for tag in tags:
            if tag in ProductTypes.values:
                return ProductTypes[ProductTypes == tag].index[0]

    all_data_df = input_df.copy()
    all_data_df = all_data_df[['FinProCode', 'MaturityDate', 'product_establish_date', 'RegistrationCode', 'ProductType', 'AssetValue']]
    # 筛选子产品 all_data_df
    RegistrationCodes = list(set(all_data_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = all_data_df[all_data_df['RegistrationCode'] == RegistrationCode]
        data_set_RegistrationCode = data_set_RegistrationCode.sort_values(by=['AssetValue'], ascending=False)
        if len(data_set_RegistrationCode.dropna(subset=['AssetValue']).index) > 0:
            data_set_RegistrationCode = data_set_RegistrationCode.dropna(subset=['AssetValue'])
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    all_data_df = all_data_df[all_data_df.index.isin(RegistrationCode_mainind)]

    # 删除'AssetValue'以防后续字段重复
    del all_data_df['AssetValue']
    return all_data_df


# 筛选存续期产品
def get_product_exist(input, statistics_date):
    input_df = input.copy()

    input_df = input_df[(((input_df['MaturityDate'].isnull()) | (input_df['MaturityDate'] >= statistics_date)))
                        & (input_df['product_establish_date'] < statistics_date)]
    return input_df


# 债券分析数据前处理
def bond_analysis_df_preprocess(input_df):
    # 筛选条件：债券
    output_df = input_df[(input_df['secondary_type_chi'] == '债券') & (input_df['SecuCode'].notnull())]
    return output_df


def get_trading_day(statistics_date):
    if statistics_date == '2022-09-30':
        trading_day = '2022-09-30'
    elif statistics_date == '2022-12-31':
        # 2022-12-31 不是交易日，所以使用2022-12-30去wind拉取数据
        trading_day = '2022-12-30'
    elif statistics_date == '2023-03-31':
        trading_day = '2023-03-31'
    else:
        raise ValueError
    return trading_day


def shorter_company_name(all_data_df, col_name):
    company_list = list(all_data_df[col_name])
    new_company_list = []
    for i in range(len(company_list)):
        if company_list[i] != '汇华理财有限公司':
            new_company_list.append(company_list[i][:-6])
        else:
            new_company_list.append('汇华理财')
    all_data_df[col_name] = new_company_list