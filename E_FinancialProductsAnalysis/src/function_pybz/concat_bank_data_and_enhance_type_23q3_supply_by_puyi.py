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


def get_final_enhance_type(row):
    # 从23q1到22q3先依次找非空且不是'底层数据未披露'的数据
    if isinstance(row['enhance_type_asset_23q1'], str) and row['enhance_type_asset_23q1'] != '底层数据未披露':
        return row['enhance_type_asset_23q1']
    elif isinstance(row['enhance_type_asset_22q4'], str) and row['enhance_type_asset_22q4'] != '底层数据未披露':
        return row['enhance_type_asset_22q4']
    elif isinstance(row['enhance_type_asset_22q3'], str):
        return row['enhance_type_asset_22q3']
    # 如果以上均不满足，从23q1到22q3依次找非空数据
    elif isinstance(row['enhance_type_asset_23q1'], str):
        return row['enhance_type_asset_23q1']
    elif isinstance(row['enhance_type_asset_22q4'], str):
        return row['enhance_type_asset_22q4']
    else:
        return row['enhance_type_asset_22q3']


def get_final_equity(row):
    # 从23q1到22q3先依次找非空
    if not np.isnan(row['equity_23q1']):
        return row['equity_23q1']
    elif not np.isnan(row['equity_22q4']):
        return row['equity_22q4']
    else:
        return row['equity_22q3']


def get_raw_fix_enhance_data(target_df):
    fix_enhance_22q3 = '22年Q3/固收增强分类结果.xlsx'
    fix_enhance_22q4 = '22年Q4/固收增强分类结果.xlsx'
    fix_enhance_23q1 = '23年Q1/固收增强分类结果.xlsx'

    fix_enhance_22q3_df = pd.read_excel(fix_enhance_22q3)[['FinProCode', 'enhance_type_asset']]
    fix_enhance_22q4_df = pd.read_excel(fix_enhance_22q4)[['FinProCode', 'enhance_type_asset']]
    fix_enhance_23q1_df = pd.read_excel(fix_enhance_23q1)[['FinProCode', 'enhance_type_asset']]

    fix_enhance_22q3_df.rename(columns={'enhance_type_asset': 'enhance_type_asset_22q3'}, inplace=True)
    fix_enhance_22q4_df.rename(columns={'enhance_type_asset': 'enhance_type_asset_22q4'}, inplace=True)
    fix_enhance_23q1_df.rename(columns={'enhance_type_asset': 'enhance_type_asset_23q1'}, inplace=True)

    target_df = target_df.merge(fix_enhance_22q3_df, on='FinProCode', how='left')
    target_df = target_df.merge(fix_enhance_22q4_df, on='FinProCode', how='left')
    target_df = target_df.merge(fix_enhance_23q1_df, on='FinProCode', how='left')

    return target_df


def get_raw_equity_data(target_df):
    equity_22q3 = '22年Q3/穿透后资产投资比例统计.xlsx'
    equity_22q4 = '22年Q4/穿透后资产投资比例统计.xlsx'
    equity_23q1 = '23年Q1/穿透后资产投资比例统计.xlsx'

    equity_22q3_df = pd.read_excel(equity_22q3)[['FinProCode', '权益类']]
    equity_22q4_df = pd.read_excel(equity_22q4)[['FinProCode', '权益类']]
    equity_23q1_df = pd.read_excel(equity_23q1)[['FinProCode', '权益类']]

    equity_22q3_df.rename(columns={'权益类': 'equity_22q3'}, inplace=True)
    equity_22q4_df.rename(columns={'权益类': 'equity_22q4'}, inplace=True)
    equity_23q1_df.rename(columns={'权益类': 'equity_23q1'}, inplace=True)

    target_df = target_df.merge(equity_22q3_df, on='FinProCode', how='left')
    target_df = target_df.merge(equity_22q4_df, on='FinProCode', how='left')
    target_df = target_df.merge(equity_23q1_df, on='FinProCode', how='left')

    return target_df


def enhance_type_asset_supply_son_by_parent(target_df):
    RegistrationCode_list = list(target_df['RegistrationCode'])
    final_list = list(target_df['enhance_type_asset_final'])
    RegistrationCode_dict = dict()
    for i in range(len(RegistrationCode_list)):
        # 优先读取识别为 非"底层数据未披露"的产品
        if isinstance(final_list[i], str):
            if RegistrationCode_list[i] in RegistrationCode_dict.keys() and RegistrationCode_dict[RegistrationCode_list[i]] != '底层数据未披露':
                continue
            RegistrationCode_dict[RegistrationCode_list[i]] = final_list[i]

    supply_list = []
    for i in range(len(RegistrationCode_list)):
        if RegistrationCode_list[i] in RegistrationCode_dict.keys():
            supply_list.append(RegistrationCode_dict[RegistrationCode_list[i]])
        else:
            supply_list.append(np.nan)

    target_df['enhance_type_asset_supply_son_by_parent'] = supply_list
    return target_df


def equity_supply_son_by_parent(target_df):
    RegistrationCode_list = list(target_df['RegistrationCode'])
    final_list = list(target_df['equity_final'])
    RegistrationCode_dict = dict()
    for i in range(len(RegistrationCode_list)):
        if not np.isnan(final_list[i]):
            RegistrationCode_dict[RegistrationCode_list[i]] = final_list[i]

    supply_list = []
    for i in range(len(RegistrationCode_list)):
        if RegistrationCode_list[i] in RegistrationCode_dict.keys():
            supply_list.append(RegistrationCode_dict[RegistrationCode_list[i]])
        else:
            supply_list.append(np.nan)

    target_df['equity_supply_son_by_parent'] = supply_list
    return target_df


def enhance_type_asset_supply_source(row):
    if isinstance(row['enhance_type_asset_supply_son_by_parent'], str) and row['enhance_type_asset_supply_son_by_parent'] != '底层数据未披露':
        return "事后"
    else:
        return row['resource']


def enhance_type_asset_supply_son_by_puyi(row):
    if isinstance(row['enhance_type_asset_supply_son_by_parent'], str) and row['enhance_type_asset_supply_son_by_parent'] != '底层数据未披露':
        return row['enhance_type_asset_supply_son_by_parent']
    elif row['product_type_son'] == '纯固收':
        return '纯债'
    else:
        return row['product_type_son']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='金融产品资产配置表映射后.xlsx')
    parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-06-30')
    args = parser.parse_args()

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    target_df = pd.read_csv(all_data_file)
    target_df = get_raw_fix_enhance_data(target_df)
    target_df = get_raw_equity_data(target_df)

    target_df['enhance_type_asset_final'] = target_df.apply(lambda x: get_final_enhance_type(x), axis=1)
    target_df['equity_final'] = target_df.apply(lambda x: get_final_equity(x), axis=1)

    # 对子产品的固收增强类型和权益持仓，使用母产品的进行补充
    target_df = enhance_type_asset_supply_son_by_parent(target_df)
    target_df = equity_supply_son_by_parent(target_df)

    # 设定数据来源，如果是自分类是事后，如果用普益的，采用普益的resource
    target_df['resource_new'] = target_df.apply(lambda x: enhance_type_asset_supply_source(x), axis=1)
    target_df['enhance_type_asset_supply_son_by_parent'] = target_df.apply(lambda x: enhance_type_asset_supply_son_by_puyi(x), axis=1)
    target_df.to_excel('bank表增加固收加分类和权益持仓.xlsx')