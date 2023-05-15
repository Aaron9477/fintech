# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤二：计算各个理财产品大类资产的配比情况
"""
import copy
import pandas as pd
import numpy as np
import argparse
from enum import Enum

from ..reader_func import get_raw_files


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
    if len(input_df[(input_df['primary_type_chi'] == '合计')]) > 0:
        total = input_df[(input_df['primary_type_chi'] == '合计')][use_data_col_name].iloc[0]
        if abs(sum(proportion_dict.values()) - total) > 0.01:
            print(input_df['FinProCode'].iloc[0])
            print(proportion_dict)


# def compare_second_asset_sum_with_total(input_df, first_asset_proportion_dict, second_asset_proportion_dict, use_data_col_name):
#     test_dict = second_asset_proportion_dict.copy()
#     supplement_type_list = ['混合类', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产']
#     for type in supplement_type_list:
#         test_dict[type] = first_asset_proportion_dict[type]
#     if len(input_df[(input_df['primary_type_chi'] == '合计')]) > 0:
#         total = input_df[(input_df['primary_type_chi'] == '合计')][use_data_col_name].iloc[0]
#         if abs(sum(test_dict.values()) - total) > 0.01:
#             print(input_df['FinProCode'].iloc[0])
#             print(test_dict)
#             print('总和:{}'.format(sum(test_dict.values())))


def proportion_normalization(proportion_dict):
    proportion_sum = sum(proportion_dict.values())
    for key in proportion_dict.keys():
        proportion_dict[key] = round(proportion_dict[key] / proportion_sum, 5)
    return proportion_dict


# 统计大类资产情况
def cal_first_asset_proportion(input_df, col_name):
    # 资产比例记录
    first_asset = {"货币市场类": 0, "固收": 0, "资管产品": 0, "QDII": 0, "其他": 0, "权益类": 0, "商品及衍生品": 0}

    first_asset['货币市场类'] = input_df[(input_df['大类资产'] == '货币市场类')][col_name].sum()
    first_asset['固收'] = input_df[(input_df['大类资产'] == '固定收益类')][col_name].sum()
    first_asset['资管产品'] = input_df[(input_df['大类资产'] == '资管产品')][col_name].sum()
    first_asset['QDII'] = input_df[(input_df['大类资产'] == 'QDII')][col_name].sum()
    first_asset['其他'] = input_df[(input_df['大类资产'] == '其他')][col_name].sum()
    first_asset['权益类'] = input_df[(input_df['大类资产'] == '权益类')][col_name].sum()
    first_asset['商品及衍生品'] = input_df[(input_df['大类资产'] == '商品及衍生品')][col_name].sum()

    return first_asset


# 统计细分类资产情况
def cal_second_asset_proportion(input_df, col_name, reflect_classify_set):
    second_asset_dict = dict()
    for reflect_classify in reflect_classify_set:
        first_asset, second_asset = reflect_classify.split(':')
        second_asset_dict[reflect_classify] = input_df[(input_df['大类资产'] == first_asset) & (input_df['详细大类资产'] == second_asset)][col_name].sum()

    return second_asset_dict


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


def cal_asset_ratio_by_filed(input_df, used_filed, output_dict, reflect_classify_set):
    input_df = input_df.copy()

    first_asset_proportion_dict = cal_first_asset_proportion(input_df, used_filed)
    second_asset_proportion_dict = cal_second_asset_proportion(input_df, used_filed, reflect_classify_set)

    # # #测试使用# 数据验证
    compare_first_asset_sum_with_total(input_df, first_asset_proportion_dict, used_filed)
    compare_first_asset_sum_with_total(input_df, second_asset_proportion_dict, used_filed)

    # 数据归一化
    first_asset_proportion_norm_dict = proportion_normalization(first_asset_proportion_dict)
    second_asset_proportion_norm_dict = proportion_normalization(second_asset_proportion_dict)

    output_dict.update(first_asset_proportion_norm_dict)
    output_dict.update(second_asset_proportion_norm_dict)


def cal_asset_ratio(input_df, reflect_classify_set):
    if input_df.shape[0] == 0:
        return

    output_dict = dict(input_df.iloc[0])

    del output_dict['product_code'], output_dict['AssetValue'], output_dict['product_type_chi'], output_dict['primary_type_chi'], output_dict['secondary_type_chi'], \
        output_dict['direct_scale'], output_dict['direct_proportion'], output_dict['direct_proportion_cal_myself'], \
        output_dict['actual_scale'], output_dict['actual_proportion'], output_dict['actual_proportion_cal_myself'],\
        output_dict['actual_proportion_type_chi'], output_dict['data_type_chi']

    before_penetration_dict = copy.deepcopy(output_dict)
    after_penetration_dict = copy.deepcopy(output_dict)

    # 如果穿透前该产品没有穿透前数据，不进行统计
    if input_df['direct_proportion'].count() == 0 and input_df['direct_proportion_cal_myself'].count() == 0:
        before_penetration_dict = None
    else:
        # 穿透后的数据，若actual_proportion字段均为空 且 actual_proportion_cal_myself 字段有值，actual_proportion_cal_myself，actual_proportion
        if input_df['direct_proportion'].count() > 0:
            use_data_col_name = 'direct_proportion'
        else:
            use_data_col_name = 'direct_proportion_cal_myself'
        cal_asset_ratio_by_filed(input_df, use_data_col_name, before_penetration_dict, reflect_classify_set)

    # 如果穿透后该产品没有穿透前数据，不进行统计
    if input_df['actual_proportion'].count() == 0 and input_df['actual_proportion_cal_myself'].count() == 0:
        after_penetration_dict = None
    else:
        # 穿透后的数据，若actual_proportion字段均为空 且 actual_proportion_cal_myself 字段有值，actual_proportion_cal_myself，actual_proportion
        if input_df['actual_proportion'].count() > 0:
            use_data_col_name = 'actual_proportion'
        else:
            use_data_col_name = 'actual_proportion_cal_myself'
        cal_asset_ratio_by_filed(input_df, use_data_col_name, after_penetration_dict, reflect_classify_set)

    return before_penetration_dict, after_penetration_dict


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


# 获取资产一二级类目的映射关系
def get_reflect_classify_set(input_df):
    reflect_set = set()
    for idx, row in input_df.iterrows():
        reflect_set.add(row['映射后一级类目'] + ':' + row['映射后二级类目'] )
    reflect_set.remove('合计:合计')
    return reflect_set


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='金融产品资产配置表映射后.xlsx')
    parser.add_argument('--reflect_file', type=str, help='reflect_file', default='../../data_pybz/大类资产映射划分_230227.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    args = parser.parse_args()

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    df = pd.read_excel(args.input_file)
    reflect_df = pd.read_excel(args.reflect_file, sheet_name='资产配置表映射关系')

    # 获取映射后资产set
    reflect_classify_set = get_reflect_classify_set(reflect_df)

    grouped = df.groupby('FinProCode')

    # 穿透前后数据分别统计
    before_penetration_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode', 'enhance_type_asset',
                                      '货币市场类', '固收', '资管产品', 'QDII', '其他', '权益类', '商品及衍生品'])
    after_penetration_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode', 'enhance_type_asset',
                                      '货币市场类', '固收', '资管产品', 'QDII', '其他', '权益类', '商品及衍生品'])
    # 固收+产品分类
    index = 0
    for group_name in list(grouped.groups.keys()):
        before_penetration_dict, after_penetration_dict = cal_asset_ratio(grouped.get_group(group_name), reflect_classify_set)
        # 穿透前后为空的数据不做补充
        if before_penetration_dict is not None:
            before_penetration_df = before_penetration_df.append(before_penetration_dict, ignore_index=True)
        if after_penetration_dict is not None:
            after_penetration_df = after_penetration_df.append(after_penetration_dict, ignore_index=True)
        index += 1
        if index % 1000 == 0:
            print(index)

    # 增加产品名称
    series_name_df = pd.read_excel(series_name_file)
    series_name_df['set_name'] = series_name_df['set'].apply(lambda x: x.split('-')[0])

    before_penetration_df = pd.merge(before_penetration_df, series_name_df[['FinProCode', 'set_name']], how='left', on=['FinProCode'])
    after_penetration_df = pd.merge(after_penetration_df, series_name_df[['FinProCode', 'set_name']], how='left', on=['FinProCode'])

    first_asset = {"货币市场类": 0, "固收": 0, "资管产品": 0, "QDII": 0, "其他": 0, "权益类": 0, "商品及衍生品": 0}
    second_asset_dict = {"QDII": 0, "其他": 0, "商品及衍生品": 0, "债券类": 0, "非标准化债权类资产": 0, "公募基金": 0,
                         "私募/信托/保险产品": 0, "委外投资": 0, "股权": 0, "股票": 0, "现金及银行存款": 0, "同业存单": 0, "拆放同业及买入返售": 0}

    all_data_df = pd.read_csv(all_data_file, encoding="utf-8", error_bad_lines=False)

    output_column_list = ['FinProCode', 'set_name', "货币市场类", '固收', '资管产品', 'QDII', '其他', '权益类', '商品及衍生品']
    output_column_list = output_column_list + list(reflect_classify_set)

    # 使用inner做拼接，原因是部分产品不发季报，只对发季报的产品进行统计
    before_penetration_df = pd.merge(all_data_df, before_penetration_df[output_column_list], how='inner', on='FinProCode')
    after_penetration_df = pd.merge(all_data_df, after_penetration_df[output_column_list], how='inner', on='FinProCode')
    before_penetration_df.to_excel('穿透前资产投资比例统计.xlsx')
    after_penetration_df.to_excel('穿透后资产投资比例统计.xlsx')


