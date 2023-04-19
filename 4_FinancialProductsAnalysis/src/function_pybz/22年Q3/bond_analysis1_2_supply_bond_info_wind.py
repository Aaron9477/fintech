# -*- coding: utf-8 -*-
"""
    基金分析1-2：补充要拉取的字段
    本代码不需要前处理，因为bond_analysis1_get_bond_info_wind.py已经进行了
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse


# target_feature = ["maturitydate", "bduration", "sduration", "sprdura_cnbd", "calc_mduration"]
# feature_name = ['到期日期', '基准久期', '利差久期', '估值利差久期(中债)', '修正久期']
target_feature = ["modifiedduration"]
feature_name = ['收盘价修正久期']


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
    if np.nan in bond_code_set:
        bond_code_set.remove(np.nan)

    index = start_index
    for feat in target_feature[start_index:]:
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='债券信息.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    parser.add_argument('--output_file', type=str, help='output_file', default='债券信息_补充.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)
    statistics_date = args.statistics_date
    output_file = args.output_file


    w.start()

    bond_code_list = df['SecuCode']

    # 批量拉取债券字段（除了前面已经拉取的债券名称，所以start_index从1开始）
    start_index = 0
    get_bond_feat(df, bond_code_list, statistics_date, start_index)

    df.to_excel("债券信息_补充.xlsx")