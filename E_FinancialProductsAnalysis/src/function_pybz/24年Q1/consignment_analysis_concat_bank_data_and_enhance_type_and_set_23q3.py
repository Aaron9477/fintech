# -*- coding: utf-8 -*-
"""
    由于22年Q4数据披露不全，使用22年Q3数据进行补充
"""
import copy

import pandas as pd
import numpy as np
import argparse
from enum import Enum

from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_files


def get_raw_fix_enhance_data(target_df):
    fix_enhance_23q1 = '代销分析使用的固收+分类.xlsx'

    fix_enhance_23q1_df = pd.read_excel(fix_enhance_23q1)[['FinProCode', 'enhance_type_asset']]
    fix_enhance_23q1_df = fixed_income_type_reflect(fix_enhance_23q1_df)

    fix_enhance_23q1_df.rename(columns={'enhance_type': '固收增强分类'}, inplace=True)

    target_df = target_df.merge(fix_enhance_23q1_df, on='FinProCode', how='left')

    return target_df


def get_set_data(target_df):
    set_file = '../../data_pybz/out5-23q2.xlsx'
    set_df = pd.read_excel(set_file)[['FinProCode', 'set']]
    set_df.rename(columns={'set': '系列名称'}, inplace=True)
    target_df = target_df.merge(set_df, on='FinProCode', how='left')

    return target_df


def enhance_type_asset_supply_son_by_parent(target_df):
    RegistrationCode_list = list(target_df['RegistrationCode'])
    final_list = list(target_df['固收增强分类'])
    RegistrationCode_dict = dict()
    for i in range(len(RegistrationCode_list)):
        if isinstance(final_list[i], str):
            RegistrationCode_dict[RegistrationCode_list[i]] = final_list[i]

    supply_list = []
    for i in range(len(RegistrationCode_list)):
        if RegistrationCode_list[i] in RegistrationCode_dict.keys():
            supply_list.append(RegistrationCode_dict[RegistrationCode_list[i]])
        else:
            supply_list.append(np.nan)

    target_df['固收增强分类_补充子产品'] = supply_list
    return target_df


def equity_supply_son_by_parent(target_df):
    RegistrationCode_list = list(target_df['RegistrationCode'])
    final_list = list(target_df['系列名称'])

    RegistrationCode_dict = dict()
    for i in range(len(RegistrationCode_list)):
        if isinstance(final_list[i], str):
            RegistrationCode_dict[RegistrationCode_list[i]] = final_list[i]

    supply_list = []
    for i in range(len(RegistrationCode_list)):
        if RegistrationCode_list[i] in RegistrationCode_dict.keys():
            supply_list.append(RegistrationCode_dict[RegistrationCode_list[i]])
        else:
            supply_list.append(np.nan)

    target_df['系列名称_补充子产品'] = supply_list
    return target_df


# 对固收增强进行归类
def fixed_income_type_reflect(input):
    input_df = input.copy()
    # 对具体的固收增强产品做映射
    # 注：固收+(其他)映射为固收增强（未披露）；固收+(其他)为投资了“其他”类资产的产品
    asset_name_reflect_dict = {'纯债': '固收（纯债）',
                               '固收+(权益)': '固收增强（权益）',
                               '固收+(含权基金)': '固收增强（权益）', '固收+(含权基金,非标)': '固收增强（权益）',
                               '固收+(基金)': '固收增强（基金）',
                               '固收+(非标)': '固收增强（非标）',

                               '固收+(权益,非标)': '固收增强（多资产）', '固收+(权益,衍生品,非标)': '固收增强（多资产）', '固收+(QDII,权益,非标)': '固收增强（多资产）',
                               '固收+(衍生品,非标)': '固收增强（多资产）', '固收+(QDII,权益,衍生品)': '固收增强（多资产）', '固收+(QDII,衍生品)': '固收增强（多资产）',
                               '固收+(QDII,衍生品,非标)': '固收增强（多资产）', '固收+(QDII,权益,衍生品,非标)': '固收增强（多资产）', '固收+(QDII,非标)': '固收增强（多资产）',
                               '固收+(QDII,含权基金,非标)': '固收增强（多资产）', '固收+(QDII,含权基金,衍生品,非标)': '固收增强（多资产）',
                               '固收+(含权基金,衍生品,非标)': '固收增强（多资产）', '固收+(QDII,含权基金,衍生品)': '固收增强（多资产）',

                               '固收+(衍生品)': '固收增强（衍生品）', '固收+(权益,衍生品)': '固收增强（衍生品）', '固收+(含权基金,衍生品)': '固收增强（衍生品）',

                               '固收+(QDII)': '固收增强（QDII）', '固收+(QDII,权益)': '固收增强（QDII）', '固收+(QDII,含权基金)': '固收增强（QDII）',
                               '固收+(其他)': '固收增强（未披露）', '底层数据未披露': '固收增强（未披露）'}
    enhance_type = input_df['enhance_type_asset']
    enhance_type_reflect = [asset_name_reflect_dict[x] for x in enhance_type]
    input_df['enhance_type'] = enhance_type_reflect
    return input_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='金融产品资产配置表映射后.xlsx')
    parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2024-03-31')
    args = parser.parse_args()

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    target_df = pd.read_csv(all_data_file)
    target_df = get_raw_fix_enhance_data(target_df)
    target_df = get_set_data(target_df)

    # 对子产品的固收增强类型和权益持仓，使用母产品的进行补充
    target_df = enhance_type_asset_supply_son_by_parent(target_df)
    target_df = equity_supply_son_by_parent(target_df)
    
    target_df.to_excel('基础数据.xlsx')