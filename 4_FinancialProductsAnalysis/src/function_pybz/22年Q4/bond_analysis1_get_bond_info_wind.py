# -*- coding: utf-8 -*-
"""
    债券分析1：从万德拉取前十大资产中债券的字段信息
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime
from func import bond_analysis_df_preprocess, get_trading_day, choose_product_mother_son, get_product_exist


target_feature = ["fullname", "amount", "windl1type", "windl2type", "municipalbond", "municipalbondYY",
                  "municipalbondWind", "subordinateornot", "perpetualornot", "latestissurercreditrating", "abs_province", "modifiedduration"]
feature_name = ['债券名称', '债券评级', 'wind一级分类', 'wind二级分类', '是否城投债', '是否城投债(wind)',
                '是否城投债(YY)', '是否次级债', '是否永续债', '发行人评级', '主体地区', '收盘价修正久期']


# 从万德拉取特定日期的数据
def get_info_from_wind_on_fixed_day(fund_set, index, search_feat, statistics_date):
    tmp_list = fund_set[index * 1000: index * 1000 + 1000]
    fund_str = ','.join(tmp_list)
    wind_return = w.wsd(fund_str, search_feat, statistics_date, statistics_date, "")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    return fund_value_dict


# 批量拉取债券字段
def get_bond_feat(input_df, bund_code_list, statistics_date):
    # list转set，用于从万德拉取数据
    bond_code_set = list(set(bund_code_list))
    if "" in bond_code_set:
        bond_code_set.remove("")

    for index in range(len(target_feature)):
        fund_value_dict = dict()
        # 数据拉取。一次性拉取太多会报错，所以分批拉取数据
        for i in range(int(len(bond_code_set) / 1000) + 1):
            fund_value_dict = dict(fund_value_dict, **get_info_from_wind_on_fixed_day(bond_code_set, i, target_feature[index], statistics_date))

        # 按债券代码从拉取结果中提取字段
        search_res = []
        for fund_code in bund_code_list:
            if fund_code in fund_value_dict and fund_value_dict[fund_code] is not None:
                search_res.append(fund_value_dict[fund_code])
            else:
                search_res.append("")
        input_df[feature_name[index]] = search_res


def df_preprocess(input_df, all_data_df, statistics_date):
    input_df = input_df.copy()
    all_data_df = all_data_df.copy()

    # 筛选子产品 all_data_df
    all_data_df = choose_product_mother_son(all_data_df)
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    # 筛选存续期产品
    output_df = get_product_exist(input_df, statistics_date)

    return output_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    parser.add_argument('--output_file', type=str, help='output_file', default='债券信息.xlsx')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    output_file = args.output_file
    trading_day = get_trading_day(statistics_date)

    if args.statistics_date == '2022-09-30':
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_22年三季报_230314.csv'
        all_data_file = '../../data_pybz/pyjy_bank_wealth_product_0930.csv'
    elif args.statistics_date == '2022-12-31':
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_22年四季报_230424.csv'
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0424.csv'
        # 221231是节假日，无数据
        statistics_date = '2022-12-30'
    elif args.statistics_date == '2023-03-31':
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_23年Q1_230425.csv'
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
    else:
        raise ValueError

    df = pd.read_csv(top10_file)
    all_data_df = pd.read_csv(all_data_file)

    # 理财产品前处理
    df = df_preprocess(df, all_data_df, trading_day)
    # 债券产品前处理
    df = bond_analysis_df_preprocess(df)
    # 删除无用的列
    df = df.drop(['MaturityDate', 'product_establish_date', 'RegistrationCode', 'ProductType'], axis=1)

    # 不确定债券的后缀
    bond_code_list = df['SecuCode'].values

    w.start()

    get_bond_feat(df, bond_code_list, trading_day)

    df.to_excel(output_file)