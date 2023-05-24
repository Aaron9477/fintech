# -*- coding: utf-8 -*-
"""
    基金分析1-1：拉取前十大资产中基金类型
    TODO:下次运行时，需要讲1-1和1-2代码合并
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime
from func import bond_analysis_code_preprocess, bond_analysis_df_preprocess


target_feature = ["fullname", "amount", "windl1type", "chinabondl1type", "municipalbond", "municipalbondYY",
                  "municipalbondWind", "subordinateornot", "perpetualornot", "latestissurercreditrating", "abs_province"]
feature_name = ['债券名称', '债券评级', 'wind一级分类', '中债债券一级分类', '是否城投债', '是否城投债(wind)',
                '是否城投债(YY)', '是否次级债', '是否永续债', '发行人评级', '主体地区']


def get_info_from_wind(fund_set, index, search_feat):
    tmp_list = fund_set[index * 1000: index * 1000 + 1000]
    fund_str = ','.join(tmp_list)
    wind_return = w.wsd(fund_str, search_feat, "2022-09-30", "2022-09-30", "")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    return fund_value_dict


def get_bond_feat_and_code(feat, fund_set_IB, fund_set_SH, fund_set_SZ):
    fund_value_dict_IB = dict()
    fund_value_dict_SH = dict()
    fund_value_dict_SZ = dict()
    for i in range(int(len(fund_set_IB) / 1000) + 1):
        fund_value_dict_IB = dict(fund_value_dict_IB, **get_info_from_wind(fund_set_IB, i, feat))
        fund_value_dict_SH = dict(fund_value_dict_SH, **get_info_from_wind(fund_set_SH, i, feat))
        fund_value_dict_SZ = dict(fund_value_dict_SZ, **get_info_from_wind(fund_set_SZ, i, feat))

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



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品前十大持仓_加入产品总资产_221116.csv')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/资产明细_221216.csv')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品投资组合明细_22年三季报_230105_手动修改.csv')
    args = parser.parse_args()

    df = pd.read_csv(args.input_file)
    # 前处理
    df = bond_analysis_df_preprocess(df)

    # 不确定债券的后缀
    fund_list, fund_list_IB, fund_list_SH, fund_list_SZ = bond_analysis_code_preprocess(df['SecuCode'].values)
    fund_set_IB = list(set(fund_list_IB))
    fund_set_SH = list(set(fund_list_SH))
    fund_set_SZ = list(set(fund_list_SZ))

    w.start()

    # 确定能否拉到数据，将第一个（债券名称）拉到不是None的数据保存。从而确保不会拉取不同债券的数据
    feat = target_feature[0]
    search_res, bond_code = get_bond_feat_and_code(feat, fund_list_IB, fund_list_SH, fund_list_SZ)
    df[feat] = search_res
    df['债券代码'] = bond_code

    bond_code_set = set(bond_code)
    bond_code_set.remove("")

    # todo：拉取其他的数据，之前的代码只拉了名称


    fund_value_dict_IB = dict()
    fund_value_dict_SH = dict()
    fund_value_dict_SZ = dict()
    for i in range(int(len(fund_set_IB) / 1000) + 1):
        fund_value_dict_IB = dict(fund_value_dict_IB, **get_info_from_wind(fund_set_IB, i, feat))
        fund_value_dict_SH = dict(fund_value_dict_SH, **get_info_from_wind(fund_set_SH, i, feat))
        fund_value_dict_SZ = dict(fund_value_dict_SZ, **get_info_from_wind(fund_set_SZ, i, feat))

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
        df[feat] = search_res
        df['债券代码'] = search_res






    index = 0
    for feat in target_feature:
        fund_value_dict_IB = dict()
        fund_value_dict_SH = dict()
        fund_value_dict_SZ = dict()
        for i in range(int(len(fund_set_IB) / 1000) + 1):
            fund_value_dict_IB = dict(fund_value_dict_IB, **get_info_from_wind(fund_set_IB, i, feat))
            fund_value_dict_SH = dict(fund_value_dict_SH, **get_info_from_wind(fund_set_SH, i, feat))
            fund_value_dict_SZ = dict(fund_value_dict_SZ, **get_info_from_wind(fund_set_SZ, i, feat))

        bond_code = []
        get_bond_code_flag = False
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
        df[feature_name[index]] = search_res
        index += 1

    # df.to_excel("债券信息.xlsx")