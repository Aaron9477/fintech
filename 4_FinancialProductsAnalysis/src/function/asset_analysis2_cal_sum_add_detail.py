# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤二：计算各个理财产品大类资产的配比情况
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
    shangYinOrJiaoYinOrMinShengOrBeiYin = 4   # 上银或者交银或者民生或者北银


class AssetManagementDataType(Enum):
    noAssetManagement = 0           # 没有资管产品分类
    onlyOne = 1                     # 资管产品模糊匹配只有一个
    aboveOneFundNumOne = 2          # 资管产品模糊匹配有多个 且 资管产品:公募基金只有一个
    aboveOneFundNumAboveOne = 3     # 资管产品模糊匹配有多个 且 资管产品:公募基金有多个

# #测试阶段使用# 统计归类后的各细分资产之和与'合计'是否一致
def compare_first_asset_sum_with_total(input_df, proportion_dict, use_data_col_name):
    if len(input_df[(input_df['AssetName'] == '合计')]) > 0:
        total = input_df[(input_df['AssetName'] == '合计')][use_data_col_name].iloc[0]
        if abs(sum(proportion_dict.values()) - total) > 0.01:
            print(input_df['FinProCode'].iloc[0])
            print(proportion_dict)


def compare_second_asset_sum_with_total(input_df, first_asset_proportion_dict, second_asset_proportion_dict, use_data_col_name):
    test_dict = second_asset_proportion_dict.copy()
    supplement_type_list = ['混合类', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产']
    for type in supplement_type_list:
        test_dict[type] = first_asset_proportion_dict[type]
    if len(input_df[(input_df['AssetName'] == '合计')]) > 0:
        total = input_df[(input_df['AssetName'] == '合计')][use_data_col_name].iloc[0]
        if abs(sum(test_dict.values()) - total) > 0.01:
            print(input_df['FinProCode'].iloc[0])
            print(test_dict)
            print('总和:{}'.format(sum(test_dict.values())))


def proportion_normalization(proportion_dict):
    proportion_sum = sum(proportion_dict.values())
    for key in proportion_dict.keys():
        proportion_dict[key] = round(proportion_dict[key] / proportion_sum, 5)
    return proportion_dict


# 统计大类资产情况
def cal_first_asset_proportion(input_df, col_name, fixedIncomeDataType, assetManagementDataType):
    # 资产比例记录
    first_asset = {"固收": 0, "资管产品": 0, "混合类": 0, "QDII": 0, "其他": 0, "权益类": 0, "商品及衍生品": 0, "非标资产": 0}

    # 统计固定收益类资产占比
    if fixedIncomeDataType == FixedIncomeDataType.onlyFirstLevel:
        first_asset['固收'] = input_df[(input_df['大类资产'] == '固定收益类')][col_name].sum()
    elif fixedIncomeDataType == FixedIncomeDataType.onlySecondLevel or fixedIncomeDataType == FixedIncomeDataType.bothFirstSecond:
        for idx, row in input_df.iterrows():
            if row['大类资产'] == '固定收益类' and row['详细大类资产'] != '固定收益类' and not np.isnan(row[col_name]):
                first_asset['固收'] += row[col_name]
    # 针对上银和交银需要单独处理
    elif fixedIncomeDataType == FixedIncomeDataType.shangYinOrJiaoYinOrMinShengOrBeiYin:
        for idx, row in input_df.iterrows():
            if row['大类资产'] == '固定收益类':
                first_asset['固收'] += row[col_name]

    # 统计资管产品资产占比
    if assetManagementDataType == AssetManagementDataType.onlyOne or assetManagementDataType == AssetManagementDataType.aboveOneFundNumOne:
        first_asset['资管产品'] = input_df[(input_df['大类资产'] == '资管产品')][col_name].sum()
    elif assetManagementDataType == AssetManagementDataType.aboveOneFundNumAboveOne:
        # 有两个资管产品:公募基金时，只取相对小的一个（即求和后减去大的那个）
        first_asset['资管产品'] = input_df[(input_df['大类资产'] == '资管产品')][col_name].sum() - input_df[(input_df['详细大类资产'] == '资管产品:公募基金')][col_name].max()

    # 统计混合类资产占比，该类资产一般只有一个
    first_asset['混合类'] = input_df[(input_df['大类资产'] == '混合类')][col_name].sum()

    # 统计境外投资资产占比，该类资产一般只有一个
    first_asset['QDII'] = input_df[(input_df['大类资产'] == '境外投资资产')][col_name].sum()

    # 统计其他资产占比。该类资产需要求和
    first_asset['其他'] = input_df[(input_df['大类资产'] == '其他资产')][col_name].sum()

    # 统计权益资产占比，该类资产匹配出多个时，只取一个
    if len(input_df[(input_df['大类资产'] == '权益类')]) > 0:
        first_asset['权益类'] = input_df[(input_df['大类资产'] == '权益类')][col_name].iloc[0]

    # 统计商品及金融衍生品资产占比，该类资产匹配出多个时，只取一个
    if len(input_df[(input_df['大类资产'] == '商品及金融衍生品类')]) > 0:
        first_asset['商品及衍生品'] = input_df[(input_df['大类资产'] == '商品及金融衍生品类')][col_name].iloc[0]

    # 统计非标资产占比
    first_asset['非标资产'] = input_df[(input_df['大类资产'] == '非标资产')][col_name].sum()

    return first_asset


# 统计细分类资产情况
def cal_second_asset_proportion(input_df, col_name, first_asset_proportion_dict, fixedIncomeDataType):
    first_asset_list = ['混合类', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产']
    second_asset_list = ['固定收益类:货币类', '固定收益类:债券类', '固定收益类:资产支持证券',
                         '资管产品:私募资管产品/信托计划/计划类资产', '资管产品:委外投资']

    # 资产比例记录
    second_asset_dict = dict()

    # 不能穿透的一级资产直接copy
    for asset in first_asset_list:
        second_asset_dict[asset] = first_asset_proportion_dict[asset]

    # 可穿透的资产统计
    for asset in second_asset_list:
        second_asset_dict[asset] = input_df[(input_df['详细大类资产'] == asset)][col_name].sum()

    # 统计资管产品:公募基金占比，该类资产匹配出多个时，只取一个
    if len(input_df[(input_df['详细大类资产'] == '资管产品:公募基金')]) > 0:
        second_asset_dict['资管产品:公募基金'] = input_df[(input_df['详细大类资产'] == '资管产品:公募基金')][col_name].iloc[0]

    # 统计未穿透的固定收益类资产占比
    if fixedIncomeDataType == FixedIncomeDataType.onlyFirstLevel:
        second_asset_dict['未穿透的固定'] = first_asset_proportion_dict['固收']
    # 针对上银和交银需要单独处理
    elif fixedIncomeDataType == FixedIncomeDataType.shangYinOrJiaoYinOrMinShengOrBeiYin and len(input_df[(input_df['大类资产'] == '固定收益类') & (input_df['详细大类资产'] == '固定收益类')][col_name]) > 0:
        second_asset_dict['未穿透的固定'] = input_df[(input_df['大类资产'] == '固定收益类') & (input_df['详细大类资产'] == '固定收益类')][col_name].iloc[0]

    # 统计资管产品资产占比
    second_asset_dict['未穿透的资管产品'] = input_df[(input_df['大类资产'] == '资管产品') & (input_df['详细大类资产'] == '资管产品')][col_name].sum()

    return second_asset_dict


def preprocessing(input_df):
    # 按 半年度投资管理报告、季度投资管理报告、定期报告 的顺序，选取一份报告做后续处理
    if len(input_df[(input_df['InfoSource'] == '半年度投资管理报告')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '半年度投资管理报告')]
    elif len(input_df[(input_df['InfoSource'] == '季度投资管理报告')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '季度投资管理报告')]
    elif len(input_df[(input_df['InfoSource'] == '定期报告')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '定期报告')]

    return input_df


def judge_enhance_type(proportion_dict, product_name):
    # 判断是否是根据FOF进行增强
    if 'FOF' in product_name or 'fof' in product_name:
        return 'FOF增强'

    # 判断纯固收
    if proportion_dict['固收'] > 0.95:
        return '纯固收'

    tmp_dict = proportion_dict.copy()
    # 移除固定收益类、资管类、其他类
    del tmp_dict['固收'], tmp_dict['资管产品'], tmp_dict['其他']

    asset_weight_list = sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True)
    # 占比最大且超过5%的作为增强类型
    if asset_weight_list[0][1] >= 0.05:
        return asset_weight_list[0][0]
    else:
        return 'None'


def judge_enhancement_type(input_df):
    # 前处理
    input_df = preprocessing(input_df)
    if input_df.shape[0] == 0:
        return

    output_dict = dict(input_df.iloc[0])
    del output_dict['Unnamed: 0'], output_dict['AssetTypeCode'], output_dict['AssetName'], output_dict['MarketValue'],\
        output_dict['RatioInNV'], output_dict['详细大类资产'], output_dict['大类资产'], output_dict['RatioInTotalAsset']
    product_name = output_dict['ChiName']

    fixedIncomeDataType = None
    # 固定收益类数据情况分类
    # 是否有固收一级分类（即'固定收益类'）
    # 非标准化债权其实当做一个一级分类
    if input_df.iloc[0]['AgentName'] == '上银理财有限责任公司' or input_df.iloc[0]['AgentName'] == '交银理财有限责任公司' \
            or input_df.iloc[0]['AgentName'] == '民生理财有限责任公司' or input_df.iloc[0]['AgentName'] == '北银理财有限责任公司':
        fixedIncomeDataType = FixedIncomeDataType.shangYinOrJiaoYinOrMinShengOrBeiYin
    else:
        if len(input_df[(input_df['详细大类资产'] == '固定收益类')]) > 0:
            fixedIncomeDataType = FixedIncomeDataType.onlyFirstLevel
            for detail in input_df['详细大类资产']:
                if detail.startswith('固定收益类:') and detail != '固定收益类:非标准化债权类':
                    fixedIncomeDataType = FixedIncomeDataType.bothFirstSecond
        else:
            fixedIncomeDataType = FixedIncomeDataType.noFixedIncome
            for detail in input_df['详细大类资产']:
                if detail.startswith('固定收益类:') and detail != '固定收益类:非标准化债权类':
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

    first_asset_proportion_dict = cal_first_asset_proportion(input_df, use_data_col_name, fixedIncomeDataType,
                                                 assetManagementDataType)
    second_asset_proportion_dict = cal_second_asset_proportion(input_df, use_data_col_name, first_asset_proportion_dict,
                                                               fixedIncomeDataType)

    # # #测试使用# 数据验证
    compare_first_asset_sum_with_total(input_df, first_asset_proportion_dict, use_data_col_name)
    compare_second_asset_sum_with_total(input_df, first_asset_proportion_dict, second_asset_proportion_dict, use_data_col_name)

    # 数据归一化
    first_asset_proportion_norm_dict = proportion_normalization(first_asset_proportion_dict)
    second_asset_proportion_norm_dict = proportion_normalization(second_asset_proportion_dict)

    output_dict.update(first_asset_proportion_norm_dict)
    output_dict['enhance_type_asset'] = judge_enhance_type(first_asset_proportion_norm_dict, product_name)
    output_dict.update(second_asset_proportion_norm_dict)
    return output_dict


def add_final_enhancement_type(input_df):
    enhance_type_asset_list = input_df['enhance_type_asset']
    enhance_type_top10_list = input_df['enhance_type_top10']
    final_enhancement_list = []

    # 优先判断前十大的增强方式，再判断大类资产的增强方式（因为前十大是穿透后的）
    for i in range(len(enhance_type_asset_list)):
        if enhance_type_top10_list[i] in ['纯固收', '权益类', '商品及衍生品', '非标资产', 'QDII']:
            final_enhancement_list.append(enhance_type_top10_list[i])
        else:
            final_enhancement_list.append(enhance_type_asset_list[i])
    input_df['enhance_type'] = final_enhancement_list
    return input_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='金融产品资产配置表_分类后.xlsx')
    parser.add_argument('--target_file', type=str, help='target_file', default='../data/bank_wealth_product_12_22.csv')
    parser.add_argument('--series_name_file', type=str, help='series_name_file', default='../data/系列名称对应_22三季报_221222.xlsx')
    parser.add_argument('--top10_file', type=str, help='input_file', default='前十大持仓固收增强分析.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)
    top10_df = pd.read_excel(args.top10_file)

    grouped = df.groupby('FinProCode')

    output_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode', 'InfoPublDate', 'InfoSource', 'enhance_type_asset',
                                      '固收', '资管产品', '混合类', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产'])

    # 固收+产品分类
    index = 0
    for group_name in list(grouped.groups.keys()):
        res_dict = judge_enhancement_type(grouped.get_group(group_name))
        # print(res_dict)
        output_df = output_df.append(res_dict, ignore_index=True)
        index += 1
        if index % 1000 == 0:
            print(index)

    # 增加产品名称
    series_name_df = pd.read_excel(args.series_name_file)
    series_name_df['set_name'] = series_name_df['set'].apply(lambda x: x.split('-')[0])

    output_df = pd.merge(output_df, series_name_df[['FinProCode', 'set_name']], how='left', on=['FinProCode'])
    output_df = pd.merge(output_df, top10_df[['FinProCode', 'enhance_type_top10']], how='left', on=['FinProCode'])
    output_df = add_final_enhancement_type(output_df)

    output_df.to_excel('固收增强分类结果.xlsx')

    target_df = pd.read_csv(args.target_file, encoding="utf-8", error_bad_lines=False)
    res_df = pd.merge(target_df, output_df[['FinProCode', 'set_name', 'InfoSource', 'enhance_type_asset', 'enhance_type_top10',
                                            'enhance_type', '固收', '资管产品', '混合类',
                                            'QDII', '其他', '权益类', '商品及衍生品', '非标资产', "固定收益类:货币类",
                                            "固定收益类:债券类", "固定收益类:资产支持证券", "资管产品:公募基金",
                                            "资管产品:私募资管产品/信托计划/计划类资产", "资管产品:委外投资", "未穿透的固定", "未穿透的资管产品"]], how='left', on=['FinProCode'])
    res_df.to_excel('合并结果.xlsx')


