# -*- coding: utf-8 -*-
"""
    债券分析1：从万德拉取前十大资产中债券的字段信息
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime
from func import bond_analysis_df_preprocess, choose_report_detail_table, \
    choose_product_mother_son, get_product_exist


target_feature = ["fullname", "amount", "windl1type", "windl2type", "municipalbond", "municipalbondYY",
                  "municipalbondWind", "subordinateornot", "perpetualornot", "latestissurercreditrating", "abs_province"]
feature_name = ['债券名称', '债券评级', 'wind一级分类', 'wind二级分类', '是否城投债', '是否城投债(wind)',
                '是否城投债(YY)', '是否次级债', '是否永续债', '发行人评级', '主体地区']


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
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品前十大持仓_加入产品总资产_221116.csv')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/资产明细_221216.csv')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data_pybz/pybz_金融产品前十名持仓_22年三季报_230309_2.csv')
    parser.add_argument('--all_data_file', type=str, help='all_data_file', default='../data_pybz/pyjy_bank_wealth_product_0306.csv')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    parser.add_argument('--output_file', type=str, help='output_file', default='债券信息.xlsx')
    args = parser.parse_args()

    df = pd.read_csv(args.input_file)
    all_data_df = pd.read_csv(args.all_data_file)
    statistics_date = args.statistics_date
    output_file = args.output_file

    # 理财产品前处理
    df = df_preprocess(df, all_data_df, statistics_date)
    # 债券产品前处理
    df = bond_analysis_df_preprocess(df)
    # 删除无用的列
    df = df.drop(['MaturityDate', 'product_establish_date', 'RegistrationCode', 'ProductType'], axis=1)

    # 不确定债券的后缀
    bond_code_list = df['SecuCode'].values

    w.start()

    get_bond_feat(df, bond_code_list, statistics_date)

    df.to_excel(output_file)