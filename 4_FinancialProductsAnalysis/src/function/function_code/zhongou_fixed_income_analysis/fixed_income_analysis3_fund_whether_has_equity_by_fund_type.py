# -*- coding: utf-8 -*-
"""
    通过统计前十大中基金类型，判断是否有含权基金
"""
import pandas as pd
import numpy as np
import argparse
from func import choose_report_asset_table, choose_product_mother_son, get_product_exist


# 前处理模块 部分规则由智妍提供
def df_preprocess(all_data_df, statistics_date):
    # 筛选子产品 all_data_df
    screen_df = choose_product_mother_son(all_data_df)['FinProCode']
    output_df = all_data_df.merge(screen_df, how='inner', on='FinProCode')

    # 筛选存续期产品
    output_df = get_product_exist(output_df, statistics_date)

    return output_df


def judge_equity_fund(df):
    bond_first_type = ["货币市场型基金", "债券型基金"]
    bond_second_type = ["混合债券型一级基金", "混合债券型二级基金", "可转换债券型基金"]

    fund_first_type_list = df['基金一级分类'].values
    fund_second_fund_type_list = df['基金二级分类'].values
    FLAG = 0
    for i in range(len(fund_first_type_list)):
        if fund_first_type_list[i] not in bond_first_type or \
            (fund_first_type_list[i] in bond_first_type and fund_second_fund_type_list[i] not in bond_second_type):
            FLAG = 1

    return FLAG


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--all_data_file', type=str, help='all_data_file', default='../../../data/bank_wealth_product_01_06.csv')
    parser.add_argument('--fund_data_file', type=str, help='fund_data_file', default='../../基金信息_2022-09-30.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    parser.add_argument('--output_file', type=str, help='output_file', default='资产明细是否有含权基金.xlsx')
    args = parser.parse_args()

    # all_data_file = args.all_data_file
    fund_data_file = args.fund_data_file
    statistics_date = args.statistics_date
    output_file = args.output_file

    fund_df = pd.read_excel(fund_data_file)
    # all_data_df = pd.read_csv(all_data_file)[['FinProCode', 'ActMaturityDate', 'ProductMaturityDate',
    #                                                'product_establish_date', 'RegistrationCode', 'ProductType']]

    # all_data_df = df_preprocess(all_data_df, statistics_date)
    whether_has_equity_df = pd.DataFrame(columns=["FinProCode", "资产明细是否有含权基金"])

    grouped = fund_df.groupby('FinProCode')
    for group_name in list(grouped.groups.keys()):
        res_dict = {"FinProCode": group_name, "资产明细是否有含权基金": judge_equity_fund(grouped.get_group(group_name))}
        whether_has_equity_df = whether_has_equity_df.append(res_dict, ignore_index=True)

    whether_has_equity_df.to_excel(output_file)