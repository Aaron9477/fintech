# -*- coding: utf-8 -*-
"""
"""
import pandas as pd
import numpy as np
import argparse
from enum import Enum


class FixedIncomeDataType(Enum):
    noFixedIncome = 0       # 没有固收类分类
    onlyFirstLevel = 1      # 只有一级分类
    onlySecondLevel = 2     # 只有二级分类
    bothFirstSecond = 3     # 一二级分类都有


class AssetManagementDataType(Enum):
    noAssetManagement = 0           # 没有资管产品分类
    onlyOne = 1                     # 资管产品模糊匹配只有一个
    aboveOneFundNumOne = 2          # 资管产品模糊匹配有多个 且 资管产品:公募基金只有一个
    aboveOneFundNumAboveOne = 3     # 资管产品模糊匹配有多个 且 资管产品:公募基金有多个

# #测试阶段使用# 统计归类后的各细分资产之和与'合计'是否一致
def compare_asset_sum_and_total(input_df, proportion_dict, use_data_col_name):
    if len(input_df[(input_df['AssetName'] == '合计')]) > 0:
        total = input_df[(input_df['AssetName'] == '合计')][use_data_col_name].iloc[0]
        if abs(sum(proportion_dict.values()) - total) > 0.01:
            print(input_df['FinProCode'].iloc[0])
            print(proportion_dict)


def proportion_normalization(proportion_dict):
    proportion_sum = sum(proportion_dict.values())
    for key in proportion_dict.keys():
        proportion_dict[key] = round(proportion_dict[key] / proportion_sum, 5)
    return proportion_dict


def cal_asset_proportion(input_df, col_name, fixedIncomeDataType, assetManagementDataType):
    # 资产比例记录
    res = {"fixed_income": 0, "asset_management": 0, "blend": 0, "qd_2": 0, "other": 0, "equity": 0, "prod_deriv": 0, "non_standard": 0}

    # 统计固定收益类资产占比
    if fixedIncomeDataType == FixedIncomeDataType.onlyFirstLevel:
        res['fixed_income'] = input_df[(input_df['大类资产'] == '固定收益类')][col_name].sum()
    elif fixedIncomeDataType == FixedIncomeDataType.onlySecondLevel or fixedIncomeDataType == FixedIncomeDataType.bothFirstSecond:
        for idx, row in input_df.iterrows():
            if row['大类资产'] == '固定收益类' and row['详细大类资产'] != '固定收益类' and not np.isnan(row[col_name]):
                res['fixed_income'] += row[col_name]

    # 统计资管产品资产占比
    if assetManagementDataType == AssetManagementDataType.onlyOne or assetManagementDataType == AssetManagementDataType.aboveOneFundNumOne:
        res['asset_management'] = input_df[(input_df['大类资产'] == '资管产品')][col_name].sum()
    elif assetManagementDataType == AssetManagementDataType.aboveOneFundNumAboveOne:
        # 有两个资管产品:公募基金时，只取相对小的一个（即求和后减去大的那个）
        res['asset_management'] = input_df[(input_df['大类资产'] == '资管产品')][col_name].sum() - input_df[(input_df['详细大类资产'] == '资管产品:公募基金')][col_name].max()

    # 统计混合资产占比，该类资产一般只有一个
    res['blend'] = input_df[(input_df['大类资产'] == '混合类')][col_name].sum()

    # 统计境外投资资产占比，该类资产一般只有一个
    res['qd_2'] = input_df[(input_df['大类资产'] == '境外投资资产')][col_name].sum()

    # 统计其他资产占比。该类资产需要求和
    res['other'] = input_df[(input_df['大类资产'] == '其他资产')][col_name].sum()

    # 统计权益资产占比，该类资产匹配出多个时，只取一个
    if len(input_df[(input_df['大类资产'] == '权益类')]) > 0:
        res['equity'] = input_df[(input_df['大类资产'] == '权益类')][col_name].iloc[0]

    # 统计商品及金融衍生品资产占比
    if len(input_df[(input_df['大类资产'] == '商品及金融衍生品类')]) > 0:
        res['prod_deriv'] = input_df[(input_df['大类资产'] == '商品及金融衍生品类')][col_name].iloc[0]

    # 统计非标资产占比
    if len(input_df[(input_df['大类资产'] == '非标资产')]) > 0:
        res['non_standard'] = input_df[(input_df['大类资产'] == '非标资产')][col_name].iloc[0]

    return res


def preprocessing(input_df):
    # # 去掉空值
    # input_df = input_df[(input_df['大类资产'] != 'None')]

    # 去掉上银和交银的数据
    input_df = input_df[(input_df['AgentName'] != '上银理财有限责任公司') & (input_df['AgentName'] != '交银理财有限责任公司')]

    # 按 半年度投资管理报告、季度投资管理报告、定期报告 的顺序，选取一份报告做后续处理
    if len(input_df[(input_df['InfoSource'] == '半年度投资管理报告')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '半年度投资管理报告')]
    elif len(input_df[(input_df['InfoSource'] == '季度投资管理报告')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '季度投资管理报告')]
    elif len(input_df[(input_df['InfoSource'] == '定期报告')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '定期报告')]

    return input_df


def judge_enhance_type(proportion_dict):
    # 判断纯固收
    if proportion_dict['fixed_income'] > 0.98:
        return 'fixed_income'

    tmp_dict = proportion_dict.copy()
    # 移除固定收益类、资管类、其他类
    del tmp_dict['fixed_income'], tmp_dict['asset_management'], tmp_dict['other']
    asset_weight_list = sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True)
    if asset_weight_list[0][1] < 0.05:
        return 'None'
    else:
        return asset_weight_list[0][0]


def judge_enhancement_type(input_df):
    # 前处理
    input_df = preprocessing(input_df)
    if input_df.shape[0] == 0:
        return

    output_dict = dict(input_df.iloc[0])
    del output_dict['Unnamed: 0'], output_dict['AssetTypeCode'], output_dict['AssetName'], output_dict['MarketValue'],\
        output_dict['RatioInNV'], output_dict['详细大类资产'], output_dict['大类资产'], output_dict['RatioInTotalAsset']

    fixedIncomeDataType = None
    # 固定收益类数据情况分类
    # 是否有固收一级分类（即'固定收益类'）
    if len(input_df[(input_df['详细大类资产'] == '固定收益类')]) > 0:
        fixedIncomeDataType = FixedIncomeDataType.onlyFirstLevel
        for detail in input_df['详细大类资产']:
            if detail.startswith('固定收益类:'):
                fixedIncomeDataType = FixedIncomeDataType.bothFirstSecond
    else:
        fixedIncomeDataType = FixedIncomeDataType.noFixedIncome
        for detail in input_df['详细大类资产']:
            if detail.startswith('固定收益类:'):
                fixedIncomeDataType = FixedIncomeDataType.onlySecondLevel

    # 资管产品数据情况分类
    if len(input_df[(input_df['大类资产'] == '资管产品')]) == 0:
        assetManagementDataType = AssetManagementDataType.noAssetManagement
    elif len(input_df[(input_df['大类资产'] == '资管产品')]) == 1:
        assetManagementDataType = AssetManagementDataType.onlyOne
    else:
        if len(input_df[(input_df['详细大类资产'] == '资管产品:公募基金')]) <= 1:
            assetManagementDataType = AssetManagementDataType.aboveOneFundNumOne
        else:
            assetManagementDataType = AssetManagementDataType.aboveOneFundNumAboveOne

    # 若RatioInTotalAsset字段均为空 且 RatioInNV 字段有值，RatioInNV，否则使用RatioInTotalAsset
    if input_df['RatioInTotalAsset'].count() == 0 and input_df['RatioInNV'].count() > 0:
        use_data_col_name = 'RatioInNV'
    else:
        use_data_col_name = 'RatioInTotalAsset'

    proportion_dict = cal_asset_proportion(input_df, use_data_col_name, fixedIncomeDataType, assetManagementDataType)
    # # #测试使用# 数据验证
    compare_asset_sum_and_total(input_df, proportion_dict, use_data_col_name)

    # print(proportion_dict)
    # 数据归一化
    proportion_norm_dict = proportion_normalization(proportion_dict)
    # print(proportion_norm_dict)

    output_dict.update(proportion_norm_dict)
    output_dict['enhance_type'] = judge_enhance_type(proportion_norm_dict)
    return output_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='金融产品资产配置表_全产品_包含权益等_JYDB221027_分类后.xlsx')
    parser.add_argument('--target_file', type=str, help='target_file', default='../data/bank_wealth_product_toyongzhen.csv')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)
    grouped = df.groupby('FinProCode')

    output_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode', 'InfoPublDate', 'InfoSource', 'enhance_type',
                                      'fixed_income', 'asset_management', 'blend', 'qd_2', 'other', 'equity', 'prod_deriv', 'non_standard'])

    index = 0
    for group_name in list(grouped.groups.keys()):
        res_dict = judge_enhancement_type(grouped.get_group(group_name))
        # print(res_dict)
        output_df = output_df.append(res_dict, ignore_index=True)
        index += 1
        if index % 1000 == 0:
            print(index)

    output_df.to_excel('固收增强分类结果.xlsx')

    target_df = pd.read_csv(args.target_file, encoding="utf-8", error_bad_lines=False)
    res_df = pd.merge(target_df, output_df[['FinProCode', 'InfoSource', 'enhance_type', 'fixed_income',
                                           'asset_management', 'blend', 'qd_2', 'other', 'equity', 'prod_deriv',
                                           'non_standard']], how='left', on=['FinProCode'])
    res_df.to_excel('合并结果.xlsx')




    # test_group = grouped.get_group('SEC000035UNK')
    # test_group = grouped.get_group('SEC000034SOP')
    # test_group = grouped.get_group('SEC000033H9V')
    # test_group = grouped.get_group('SEC0000386MS')
    # test_group = grouped.get_group('SEC00003E0WZ')
    # test_group = grouped.get_group('SEC000035SRG')
    # test_group = grouped.get_group('SEC00007GWSL')

    # print(test_group)
    # print(type(test_group))
    # judge_enhancement_type(test_group)
    # print(judge_enhancement_type(test_group))
