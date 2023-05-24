# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 17:20:45 2022
根据前十大持仓分析固收增强
@author: 王永镇
"""

import pandas as pd
import numpy as np
import argparse

# # 分类方法：固收+定义为投资了权益类、商品、衍生品类、基金、理财产品/信托计划及资产管理计划的固收类产品

name_set = set()

supplement_type_list = ['混合类', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产']

# FCC0000001T8-固定收益类、FCC0000001WN-标准化债权资产、FCC0000001WL-债券、
# FCC000001DY1-固定收益类：其他资产、FCC0000014T8-可转债
fixed_income_list = ["FCC0000001T8", "FCC0000001WN", "FCC0000001WL", "FCC000001DY1", "FCC0000014T8", ]

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


def preprocess(input_df):
    # 只保留穿透后的数据
    input_df = input_df[input_df['PenetrationType'] == 'FCC0000019PL']

    invest_object_list = input_df['InvestObject']
    invest_type_list = []
    for invest_object in invest_object_list:
        if invest_object in reflect_dict.keys():
            invest_type_list.append(reflect_dict[invest_object])
        else:
            invest_type_list.append('None')
    input_df['invest_type'] = invest_type_list

    return input_df


def choose_report(input_df):
    # 按 2022中报、2022二季报 的顺序，选取一份报告做后续处理
    if len(input_df[(input_df['InfoSource'] == '2022中报')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '2022中报')]
    elif len(input_df[(input_df['InfoSource'] == '2022二季报')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '2022二季报')]

    return input_df


# 统计大类资产情况
def cal_asset_proportion(input_df, col_name):
    # 资产比例记录
    asset_proportion = {"固收类": 0, "权益类": 0, "商品及衍生品": 0, "非标资产": 0, "QDII": 0}
    asset_proportion['固收类'] = input_df[(input_df['invest_type'] == '固收类')][col_name].sum()
    asset_proportion['权益类'] = input_df[(input_df['invest_type'] == '权益类')][col_name].sum()
    asset_proportion['商品及衍生品'] = input_df[(input_df['invest_type'] == '商品及衍生品')][col_name].sum()
    asset_proportion['非标资产'] = input_df[(input_df['invest_type'] == '非标资产')][col_name].sum()
    asset_proportion['QDII'] = input_df[(input_df['invest_type'] == 'QDII')][col_name].sum()

    return asset_proportion


def judge_enhance_type(proportion_dict):
    tmp_dict = proportion_dict.copy()

    # 移除固定收益类、资管类、其他类
    del tmp_dict['固收类']

    asset_weight_list = sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True)
    # 占比最大且超过5%的作为增强类型
    if asset_weight_list[0][1] >= 0.05:
        return asset_weight_list[0][0]
    else:
        if proportion_dict['固收类'] > 0.95:
            return '纯固收'


def judge_enhancement_type(input_df, reflect_dict):
    # 前处理
    input_df = choose_report(input_df)
    if input_df.shape[0] == 0:
        return
    output_dict = dict(input_df.iloc[0])
    del output_dict['SerialNumber'], output_dict['SecuCode'], output_dict['SecuName'],\
        output_dict['MarketValue'], output_dict['RatioInNV'], output_dict['AssetValue'], output_dict['AssetValueRatio']
    product_name = output_dict['ChiName']

    # 优先使用 RatioInNV ，为空使用AssetValueRatio
    if input_df['RatioInNV'].count() > 0:
        use_data_col_name = 'RatioInNV'
    elif input_df['AssetValueRatio'].count() > 0:
        use_data_col_name = 'AssetValueRatio'
    else:
        return

    # 资产总和须在1.2以下，有可能加杠杆
    if input_df[use_data_col_name].sum() > 1.2:
        return

    asset_proportion = cal_asset_proportion(input_df, use_data_col_name)
    output_dict.update(asset_proportion)
    output_dict['enhance_type_top10'] = judge_enhance_type(asset_proportion)
    return output_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品前十大持仓_加入产品总资产_221116.csv')
    args = parser.parse_args()

    reflect_dict = dict()
    for i in non_standardized_assets:
        reflect_dict[i] = '非标资产'
    for i in product_derivatives_list:
        reflect_dict[i] = '商品及衍生品类'
    for i in equity_list:
        reflect_dict[i] = '权益类'
    for i in fixed_income_list:
        reflect_dict[i] = '固收类'

    df = pd.read_csv(args.input_file)
    # 前处理
    df = preprocess(df)

    output_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode', 'InfoPublDate', 'InfoSource', 'enhance_type_top10',
                                      '权益类', '非标资产', '商品及衍生品类', 'QDII'])

    # 固收+产品分类
    index = 0
    grouped = df.groupby('FinProCode')
    for group_name in list(grouped.groups.keys()):
        res_dict = judge_enhancement_type(grouped.get_group(group_name), reflect_dict)
        output_df = output_df.append(res_dict, ignore_index=True)
        index += 1
        if index % 1000 == 0:
            print(index)

    output_df.to_excel("前十大持仓固收增强分析.xlsx")