# -*- coding: utf-8 -*-
"""
    基金分析1-2：补充要拉取的字段
    本代码不需要前处理，因为bond_analysis1_get_bond_info_wind.py已经进行了
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse

target_feature = ["windl1type", "windl2type", "modifiedduration", "amount", "latestissurercreditrating", "municipalbond", "municipalbondYY",
                  "municipalbondWind", "subordinateornot", "perpetualornot"]
feature_name = ['wind一级分类', 'wind二级分类', '收盘价修正久期', '债券评级', '发行人评级', '是否城投债', '是否城投债(wind)',
                '是否城投债(YY)', '是否次级债', '是否永续债']


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
    parser.add_argument('--input_file', type=str, help='input_file', default='../tests/平安理财专户持仓明细.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-30')
    parser.add_argument('--statistics_sheet', type=str, help='statistics_sheet', default='12月')
    parser.add_argument('--output_file', type=str, help='output_file', default='债券信息_12月.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file, sheet_name=args.statistics_sheet)
    statistics_date = args.statistics_date
    output_file = args.output_file


    w.start()

    bond_df = df[~df['类别'].isin(['货币基金', '其他', '衍生品', '债券型基金'])]
    bond_code_list = bond_df[' 债券代码']
    bond_code_list = [x.strip() for x in bond_code_list]
    bond_df[' 债券代码'] = bond_code_list

    # 批量拉取债券字段（除了前面已经拉取的债券名称，所以start_index从1开始）
    start_index = 0
    get_bond_feat(bond_df, bond_code_list, statistics_date, start_index)

    bond_df.to_excel(output_file)