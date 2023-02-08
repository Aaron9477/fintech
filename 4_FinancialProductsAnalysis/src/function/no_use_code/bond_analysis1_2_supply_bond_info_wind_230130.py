# -*- coding: utf-8 -*-
"""
    基金分析1-2：拉取前十大资产中基金
    TODO:下次运行时，需要讲1-1和1-2代码合并
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime
from func import bond_analysis_code_preprocess, bond_analysis_df_preprocess

target_feature = ["latestissurercreditrating", "abs_province"]
feature_name = ['发行人评级', '主体地区']


def get_info_from_wind(fund_set, index, search_feat):
    tmp_list = fund_set[index * 1000: index * 1000 + 1000]
    fund_str = ','.join(tmp_list)
    wind_return = w.wsd(fund_str, search_feat, "2022-09-30", "2022-09-30", "")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    return fund_value_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品前十大持仓_加入产品总资产_221116.csv')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/资产明细_221216.csv')
    parser.add_argument('--input_file', type=str, help='input_file', default='债券信息.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)
    # 前处理
    df = bond_analysis_df_preprocess(df)

    fund_list, fund_list_IB, fund_list_SH, fund_list_SZ = bond_analysis_code_preprocess(df['SecuCode'].values)
    fund_set_IB = list(set(fund_list_IB))
    fund_set_SH = list(set(fund_list_SH))
    fund_set_SZ = list(set(fund_list_SZ))

    w.start()

    index = 0
    for feat in target_feature:
        final_res = []
        fund_value_dict_IB = dict()
        fund_value_dict_SH = dict()
        fund_value_dict_SZ = dict()
        for i in range(int(len(fund_set_IB) / 1000) + 1):
            fund_value_dict_IB = dict(fund_value_dict_IB, **get_info_from_wind(fund_set_IB, i, feat))
            fund_value_dict_SH = dict(fund_value_dict_SH, **get_info_from_wind(fund_set_SH, i, feat))
            fund_value_dict_SZ = dict(fund_value_dict_SZ, **get_info_from_wind(fund_set_SZ, i, feat))

        search_res = []
        for fund in fund_list:
            fund_IB = fund + '.IB'
            fund_SH = fund + '.SH'
            fund_SZ = fund + '.SZ'
            if fund_IB in fund_value_dict_IB and fund_value_dict_IB[fund_IB] is not None:
                search_res.append(fund_value_dict_IB[fund_IB])
            elif fund_SH in fund_value_dict_SH and fund_value_dict_SH[fund_SH] is not None:
                search_res.append(fund_value_dict_SH[fund_SH])
            else:
                search_res.append(fund_value_dict_SZ[fund_SZ])
        df[feature_name[index]] = search_res
        index += 1

    df.to_excel("债券信息_补充.xlsx")