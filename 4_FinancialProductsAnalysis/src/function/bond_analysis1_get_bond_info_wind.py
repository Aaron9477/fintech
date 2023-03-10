# -*- coding: utf-8 -*-
"""
    债券分析1：从万德拉取前十大资产中债券的字段信息
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime
from func import bond_analysis_code_preprocess, bond_analysis_df_preprocess, choose_report_detail_table, \
    choose_product_mother_son, get_product_exist


target_feature = ["fullname", "amount", "windl1type", "windl2type", "municipalbond", "municipalbondYY",
                  "municipalbondWind", "subordinateornot", "perpetualornot", "latestissurercreditrating", "abs_province"]
feature_name = ['债券名称', '债券评级', 'wind一级分类', 'wind二级分类', '是否城投债', '是否城投债(wind)',
                '是否城投债(YY)', '是否次级债', '是否永续债', '发行人评级', '主体地区']


# target_feature = ["fullname", "amount", "windl1type"]
# feature_name = ['债券名称', '债券评级', 'wind一级分类']


# 从万德拉取特定日期的数据
def get_info_from_wind_on_fixed_day(fund_set, index, search_feat, statistics_date):
    tmp_list = fund_set[index * 1000: index * 1000 + 1000]
    fund_str = ','.join(tmp_list)
    wind_return = w.wsd(fund_str, search_feat, statistics_date, statistics_date, "")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    return fund_value_dict


# 批量拉取债券字段（除了债券名称）
def get_bond_feat(input_df, bund_code_list, statistics_date, start_index):
    # list转set，用于从万德拉取数据
    bond_code_set = list(set(bund_code_list))
    if "" in bond_code_set:
        bond_code_set.remove("")

    index = start_index
    for feat in target_feature[1:]:
        fund_value_dict = dict()
        # 数据拉取。一次性拉取太多会报错，所以分批拉取数据
        for i in range(int(len(bond_code_set) / 1000) + 1):
            fund_value_dict = dict(fund_value_dict, **get_info_from_wind_on_fixed_day(bond_code_set, i, feat, statistics_date))

        # 按债券代码从拉取结果中提取字段
        search_res = []
        for fund_code in bund_code_list:
            if fund_code in fund_value_dict and fund_value_dict[fund_code] is not None:
                search_res.append(fund_value_dict[fund_code])
            else:
                search_res.append("")
        input_df[feature_name[index]] = search_res
        index += 1


def get_bond_code_and_name(feat, fund_set_IB, fund_set_SH, fund_set_SZ, statistics_date):
    fund_value_dict_IB = dict()
    fund_value_dict_SH = dict()
    fund_value_dict_SZ = dict()
    for i in range(int(len(fund_set_IB) / 1000) + 1):
        fund_value_dict_IB = dict(fund_value_dict_IB, **get_info_from_wind_on_fixed_day(fund_set_IB, i, feat,
                                                                                        statistics_date))
        fund_value_dict_SH = dict(fund_value_dict_SH, **get_info_from_wind_on_fixed_day(fund_set_SH, i, feat,
                                                                                        statistics_date))
        fund_value_dict_SZ = dict(fund_value_dict_SZ, **get_info_from_wind_on_fixed_day(fund_set_SZ, i, feat,
                                                                                        statistics_date))

    bond_code = []
    search_res = []
    for fund in fund_list:
        fund_IB = fund + '.IB'
        fund_SH = fund + '.SH'
        fund_SZ = fund + '.SZ'
        if fund_IB in fund_value_dict_IB and fund_value_dict_IB[fund_IB] is not None:
            bond_code.append(fund_IB)
            search_res.append(fund_value_dict_IB[fund_IB])
        elif fund_SH in fund_value_dict_SH and fund_value_dict_SH[fund_SH] is not None:
            bond_code.append(fund_SH)
            search_res.append(fund_value_dict_SH[fund_SH])
        elif fund_SZ in fund_value_dict_SZ and fund_value_dict_SZ[fund_SZ] is not None:
            bond_code.append(fund_SZ)
            search_res.append(fund_value_dict_SZ[fund_SZ])
        else:
            bond_code.append("")
            search_res.append("")

    return search_res, bond_code


def df_preprocess(input_df, all_data_df, statistics_date):
    input_df = input_df.copy()
    all_data_df = all_data_df.copy()

    # 筛选子产品 all_data_df
    all_data_df = choose_product_mother_son(all_data_df)
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    # 筛选存续期产品
    input_df = get_product_exist(input_df, statistics_date)

    # 报告筛选
    output_df = choose_report_detail_table(input_df, statistics_date)

    return output_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品前十大持仓_加入产品总资产_221116.csv')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/资产明细_221216.csv')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品投资组合明细_22年三季报_230105_手动修改.csv')
    parser.add_argument('--all_data_file', type=str, help='all_data_file', default='../data/bank_wealth_product_01_16.csv')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    parser.add_argument('--output_file', type=str, help='output_file', default='债券信息.xlsx')
    args = parser.parse_args()

    df = pd.read_csv(args.input_file)
    all_data_df = pd.read_csv(args.all_data_file, encoding='gbk')[['FinProCode', 'MaturityDate', 'product_establish_date',
                                                                   'RegistrationCode', 'ProductType']]
    statistics_date = args.statistics_date
    output_file = args.output_file

    # 理财产品前处理
    df = df_preprocess(df, all_data_df, statistics_date)
    # 债券产品前处理
    df = bond_analysis_df_preprocess(df)
    # 删除无用的列
    df = df.drop(['MaturityDate', 'product_establish_date', 'RegistrationCode', 'ProductType'], axis=1)

    # 不确定债券的后缀
    fund_list, fund_list_IB, fund_list_SH, fund_list_SZ = bond_analysis_code_preprocess(df['SecuCode'].values)
    fund_set_IB = list(set(fund_list_IB))
    fund_set_SH = list(set(fund_list_SH))
    fund_set_SZ = list(set(fund_list_SZ))

    w.start()

    # 确定能否拉到债券名称，将拉到不是None的债券编码保存。从而确保不会拉取不同债券的字段
    feat = target_feature[0]
    search_res, bond_code_list = get_bond_code_and_name(feat, fund_set_IB, fund_set_SH, fund_set_SZ, statistics_date)
    df['债券名称'] = search_res
    df['债券代码'] = bond_code_list

    # 批量拉取债券字段（除了前面已经拉取的债券名称，所以start_index从1开始）
    start_index = 1
    get_bond_feat(df, bond_code_list, statistics_date, start_index)

    df.to_excel(output_file)