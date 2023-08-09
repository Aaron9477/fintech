# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析基础步骤：基于智妍的大类资产映射关系，对大类资产做分类
"""
import pandas as pd
import numpy as np
import argparse

from func import choose_product_mother_son, get_product_exist
from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_files


# primary_type_reflect_dict = {'代客境外理财投资qdii': 'QDII', '商品类': '商品及衍生品', '基金': '', '委外投资————协议方式': '资管产品',
#                              '金融衍生品类': '商品及衍生品'}
# secondary_type_reflect_dict = {'空值': '未公布投资细类', '债券': '债券类', '理财直接融资工具': '非标准化债权类资产', '委外投资————协议方式': '资管产品',
#                              '金融衍生品类': '商品及衍生品'}


# 获取资产一二级类目的映射关系
def get_reflect_dict(input_df):
    primary_reflact_dict = dict()
    secondary_reflact_dict = dict()
    for idx, row in input_df.iterrows():
        primary_reflact_dict[row['映射前一级类目'] + ':' + row['映射前二级类目']] = row['映射后一级类目']
        secondary_reflact_dict[row['映射前一级类目'] + ':' + row['映射前二级类目']] = row['映射后二级类目']

    return primary_reflact_dict, secondary_reflact_dict


def get_major_assets_detail(row, reflact_dict):
    asset_name = row['primary_type_chi'] + ':' + row['secondary_type_chi']
    if asset_name not in reflact_dict.keys():
        if asset_name not in asset_name_not_in_dict.keys():
            asset_name_not_in_dict[asset_name] = 0
        asset_name_not_in_dict[asset_name] += 1
        return 'None'
    major_assets_detail = reflact_dict[asset_name]
    return major_assets_detail


# 前处理模块
def df_preprocess(input_df, all_data_df, statistics_date):
    # 筛选存续期产品
    all_data_df = get_product_exist(all_data_df, statistics_date)

    # 筛选子产品 all_data_df
    all_data_df = choose_product_mother_son(all_data_df)
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    return input_df


# 统计理财产品在非标资产的总投资比例
def cal_non_standard_asset_sum(input_df):
    grouped = input_df.groupby(['FinProCode']).agg({'proportion_of_product': sum})
    actual_proportion_list = list(grouped['proportion_of_product'].items())
    res_list = []
    for i in range(len(actual_proportion_list)):
        res_list.append([actual_proportion_list[i][0], actual_proportion_list[i][1]])

    col_name = ['FinProCode', 'non_std_asset_ratio']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    df_res['non_std_asset_ratio'] =  df_res['non_std_asset_ratio'] / 100.0
    df_res['non_std_asset_ratio'].replace(0, 99, inplace=True)

    return df_res[['FinProCode', 'non_std_asset_ratio']]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-06-30')

    args = parser.parse_args()
    reflect_file = args.reflect_file
    statistics_date = args.statistics_date

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    reflect_df = pd.read_excel(reflect_file, sheet_name='资产配置表映射关系')
    try:
        raw_asset_data = pd.read_csv(raw_asset_file)
    except:
        raw_asset_data = pd.read_csv(raw_asset_file, encoding='gbk')
    all_data_df = pd.read_csv(all_data_file)
    non_standard_df = pd.read_csv(non_standard_file)

    # 映射关系
    primary_reflact_dict, secondary_reflact_dict = get_reflect_dict(reflect_df)

    # 插入两列名，后续补充数据
    raw_asset_data.insert(loc=9, column='详细大类资产', value='')
    raw_asset_data.insert(loc=10, column='大类资产', value='')

    # 统计大类资产映射表不能覆盖的字段
    asset_name_not_in_dict = dict()

    # 数据前处理
    raw_asset_data = df_preprocess(raw_asset_data, all_data_df, statistics_date)

    raw_asset_data['大类资产'] = raw_asset_data.apply(lambda x: get_major_assets_detail(x, primary_reflact_dict), axis=1)
    raw_asset_data['详细大类资产'] = raw_asset_data.apply(lambda x: get_major_assets_detail(x, secondary_reflact_dict), axis=1)

    raw_asset_data.to_excel('金融产品资产配置表映射后.xlsx')

    # 统计产品非标投资比例
    non_standard_sum_df = cal_non_standard_asset_sum(non_standard_df)
    non_standard_sum_df.to_excel('产品非标投资规模统计.xlsx')



