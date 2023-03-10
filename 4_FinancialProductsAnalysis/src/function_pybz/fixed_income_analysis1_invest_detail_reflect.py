# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 17:20:45 2022
先运行base_analysis1_asset_allocation_reflect.py,对资产名称进行映射
固收+统计分析步骤一：根据前十大持仓和非标数据分析固收增强
@author: 王永镇
"""

import pandas as pd
import numpy as np
import argparse
from func import choose_report_detail_table, choose_penetration_data, choose_product_mother_son, get_product_exist


# # 分类方法：固收+定义为投资了权益类、商品、衍生品类、基金、理财产品/信托计划及资产管理计划的固收类产品

name_set = set()

supplement_type_list = ['混合类', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产']

# FCC0000001T8-固定收益类、FCC0000001WN-标准化债权资产、FCC0000001WL-债券、
# FCC000001DY1-固定收益类：其他资产、FCC0000014T8-可转债、FCC0000001WQ-资产支持证券
fixed_income_list = ["FCC0000001T8", "FCC0000001WN", "FCC0000001WL", "FCC000001DY1", "FCC0000014T8", "FCC0000001WQ"]

# FCC0000001X6-金融衍生品、FCC000000YHQ-期货、FCC000000HEP-权证、FCC00000139U-期权、FCC000001DY3-商品及金融衍生品类：其他资产、FCC000000SO6-远期外汇合约
product_derivatives_list = ["FCC0000001X6", "FCC000000YHQ", "FCC000000HEP", "FCC00000139U", "FCC000001DY3", 'FCC000000SO6', ]

# FCC0000001T9-权益类、FCC0000001WJ-股票、FCC000001DY2-权益类：其他资产、FCC000001DXY-优先股、FCC000000YHP-港股
equity_list = ["FCC0000001T9", "FCC0000001WJ", "FCC000001DY2", "FCC000001DXY", 'FCC000000YHP']

# CFN000000274-理财产品/信托计划及资产管理计划(1114个)、CBS000000028-其他资产(6202个)(以资产管理计划为主)
# CFN0000001CB-基金(130个)、FCC000001DY0-商品类基金、FCC000001DXZ-权益类基金、FCC0000014SB-债券基金、
fund_asset_management_list = ["CFN000000274", "CBS000000028", "CFN0000001CB", "FCC000001DY0", "FCC000001DXZ",
                              "FCC0000014SB", ]

# FCC0000001X3-现金类资产、CFN0000002OC-回购及逆回购、FCC0000013BX-高流动性资产(611个)
cash_type_list = ["FCC0000001X3", "CFN0000002OC", "FCC0000013BX"]

# FCC000001CN5-权益类和商品及金融衍生品类、FCC000001CN7-固定收益类和商品及金融衍生品类、FCC000001CN6-固定收益类和资管产品(327个)
blend_list = ["FCC000001CN5", "FCC000001CN7", "FCC000001CN6", ]

# FCC0000001WO-非标准化债权资产
non_standardized_assets = ["FCC0000001WO", ]

# CBS00000000K-买入返售金融资产(1个)、CFN000000ADG-股票质押式回购(0个)、FCC000000076-股权(0个)
other_list = ["CBS00000000K", "CFN000000ADG", ]

# QDII_list = []


# 获取资产一二级类目的映射关系
def get_reflect_dict(input_df):
    reflact_dict = dict()
    for idx, row in input_df.iterrows():
        reflact_dict[row['映射前一级类目'] + ':' + row['映射前二级类目']] = row['映射后类目']

    return reflact_dict


def df_preprocess(input_df, all_data_df, statistics_date):
    # 筛选子产品 all_data_df
    all_data_df = choose_product_mother_son(all_data_df)
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    # 筛选存续期产品
    input_df = get_product_exist(input_df, statistics_date)

    return input_df


# 统计大类资产情况
def cal_asset_proportion(input_df, col_name):
    # 资产比例记录
    asset_proportion = {"前十大_固收类": 0, "前十大_权益类": 0, "前十大_商品及衍生品": 0, "前十大_非标资产": 0, "前十大_QDII": 0}
    asset_proportion['前十大_固收类'] = input_df[(input_df['资产映射结果'] == '固定收益类')][col_name].sum()
    asset_proportion['前十大_权益类'] = input_df[(input_df['资产映射结果'] == '权益类')][col_name].sum()
    asset_proportion['前十大_商品及衍生品'] = input_df[(input_df['资产映射结果'] == '商品及衍生品')][col_name].sum()
    asset_proportion['前十大_非标资产'] = input_df[(input_df['资产映射结果'] == '非标准化债权类资产')][col_name].sum()
    asset_proportion['前十大_QDII'] = input_df[(input_df['资产映射结果'] == 'QDII')][col_name].sum()

    return asset_proportion


def judge_enhance_type(proportion_dict):
    tmp_dict = proportion_dict.copy()

    # 移除固定收益类
    del tmp_dict['前十大_固收类']

    asset_weight_list = sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True)
    # 占比最大且超过5%的作为增强类型
    if asset_weight_list[0][1] >= 0.05:
        return asset_weight_list[0][0]
    else:
        if proportion_dict['前十大_固收类'] > 0.95:
            return '纯固收'


def judge_enhancement_type(input_df):
    if input_df.shape[0] == 0:
        return
    output_dict = dict(input_df.iloc[0])
    # del output_dict['product_code'], output_dict['product_sum_scale'], output_dict['product_type_chi'], output_dict['asset_rank'], output_dict['asset_name'], \
    #     output_dict['asset_scale'], output_dict['actual_proportion'], output_dict['actual_proportion_cal_myself'], \
    #     output_dict['actual_proportion_type_chi'], output_dict['primary_type_chi'], output_dict['secondary_type_chi'],\
    #     output_dict['three_level_type'], output_dict['sh_code'], output_dict['sz_code'], output_dict['other_generic_code'], \
    #     output_dict['comprehensive_code'], output_dict['data_type_chi']

    del output_dict['product_code'], output_dict['MarketValue'], output_dict['product_type_chi'], output_dict['asset_rank'], output_dict['SecuName'], \
        output_dict['AssetValue'], output_dict['actual_proportion'], output_dict['actual_proportion_cal_myself'], \
        output_dict['actual_proportion_type_chi'], output_dict['primary_type_chi'], output_dict['secondary_type_chi'],\
        output_dict['three_level_type'], output_dict['sh_code'], output_dict['sz_code'], output_dict['other_generic_code'], \
        output_dict['SecuCode'], output_dict['data_type_chi']

    # 优先使用 RatioInNV ，为空使用AssetValueRatio
    if input_df['actual_proportion'].count() > 0:
        use_data_col_name = 'actual_proportion'
    elif input_df['actual_proportion_cal_myself'].count() > 0:
        use_data_col_name = 'actual_proportion_cal_myself'
    else:
        return

    # 资产总和须在1.2以下，有可能加杠杆
    if input_df[use_data_col_name].sum() > 1.2:
        return

    asset_proportion = cal_asset_proportion(input_df, use_data_col_name)
    output_dict.update(asset_proportion)
    output_dict['enhance_type_top10'] = judge_enhance_type(asset_proportion)
    return output_dict


# 统计理财产品在非标资产的总投资比例
def cal_non_standard_asset_sum(input_df):
    grouped = input_df.groupby(['FinProCode']).agg({'proportion_of_product': sum, 'proportion_of_product_cal_myself': sum})
    proportion_of_product_list = list(grouped['proportion_of_product'].items())
    proportion_of_product_cal_myself_list = list(grouped['proportion_of_product_cal_myself'].items())
    res_list = []
    for i in range(len(proportion_of_product_list)):
        res_list.append([proportion_of_product_list[i][0], proportion_of_product_list[i][1], proportion_of_product_cal_myself_list[i][1]])

    col_name = ['FinProCode', 'proportion_of_product_sum', 'proportion_of_product_cal_myself_sum']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    df_res['non_std_asset_ratio'] = np.where(df_res['proportion_of_product_sum'].isnull(),
                                             df_res['proportion_of_product_sum'], df_res['proportion_of_product_cal_myself_sum'])

    return df_res[['FinProCode', 'non_std_asset_ratio']]


def get_major_assets_detail(row, reflact_dict):
    asset_name = row['primary_type_chi'] + ':' + row['secondary_type_chi']
    if asset_name not in reflact_dict.keys():
        if asset_name not in asset_name_not_in_dict.keys():
            asset_name_not_in_dict[asset_name] = 0
        asset_name_not_in_dict[asset_name] += 1
        return 'None'
    major_assets_detail = reflact_dict[asset_name]
    return major_assets_detail


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--top10_file', type=str, help='top10_file', default='../data_pybz/pybz_金融产品前十名持仓_22年三季报_230309_2.csv')
    parser.add_argument('--non_standard_file', type=str, help='non_standard_file', default='../data_pybz/pybz_非标准化债权及股权类资产表_22年三季报_230309.csv')
    parser.add_argument('--all_data_file', type=str, help='all_data_file', default='../data_pybz/pyjy_bank_wealth_product_0930.csv')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022/9/30')
    args = parser.parse_args()

    reflect_df = pd.read_excel(args.reflect_file, sheet_name='前10大持仓表映射关系')
    top10_df = pd.read_csv(args.top10_file)
    non_standard_df = pd.read_csv(args.non_standard_file)
    all_data_df = pd.read_csv(args.all_data_file)
    statistics_date = args.statistics_date

    # 映射关系
    reflact_dict = get_reflect_dict(reflect_df)

    # 理财产品前处理
    top10_df = df_preprocess(top10_df, all_data_df, statistics_date)

    # 统计产品非标投资比例
    non_standard_sum_df = cal_non_standard_asset_sum(non_standard_df)

    # 统计大类资产映射表不能覆盖的字段
    asset_name_not_in_dict = dict()
    top10_df['资产映射结果'] = top10_df.apply(lambda x: get_major_assets_detail(x, reflact_dict), axis=1)

    # df = invest_detail_reflect(top10_df)

    output_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode', 'enhance_type_top10',
                                      '前十大_权益类', '前十大_非标资产', '前十大_商品及衍生品', '前十大_QDII', '前十大_固收类'])

    # 固收+产品分类
    index = 0
    grouped = top10_df.groupby('FinProCode')
    for group_name in list(grouped.groups.keys()):
        res_dict = judge_enhancement_type(grouped.get_group(group_name))
        output_df = output_df.append(res_dict, ignore_index=True)
        index += 1
        if index % 1000 == 0:
            print(index)

    output_df = output_df.merge(non_standard_sum_df, how='left', on='FinProCode')

    output_df.rename(columns={'non_std_asset_ratio': '非标资产投资比例'}, inplace=True)

    output_df.to_excel("前十大持仓固收增强分析.xlsx")