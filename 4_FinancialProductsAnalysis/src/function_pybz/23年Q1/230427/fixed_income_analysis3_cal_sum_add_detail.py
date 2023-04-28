# -*- coding: utf-8 -*-
"""
    固收+统计分析步骤三：固收+/大类资产统计分析步骤四：计算各个理财产品大类资产的配比情况
"""
import pandas as pd
import numpy as np
import argparse
from enum import Enum
from func import choose_report_asset_table, choose_product_mother_son, get_product_exist
import datetime, time


# 前处理模块 部分规则由智妍提供
def df_preprocess(all_data_df, statistics_date):
    # 筛选子产品 all_data_df
    screen_df = choose_product_mother_son(all_data_df)['FinProCode']
    output_df = all_data_df.merge(screen_df, how='inner', on='FinProCode')

    # 筛选存续期产品
    output_df = get_product_exist(output_df, statistics_date)

    return output_df


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
    if len(input_df[(input_df['大类资产'] == '合计')]) > 0:
        total = input_df[(input_df['大类资产'] == '合计')][use_data_col_name].iloc[0]
        if abs(sum(proportion_dict.values()) - total) > 0.04:
            print(input_df['FinProCode'].iloc[0])
            print(proportion_dict)


# def compare_second_asset_sum_with_total(input_df, first_asset_proportion_dict, second_asset_proportion_dict, use_data_col_name):
#     test_dict = second_asset_proportion_dict.copy()
#     supplement_type_list = ['混合类', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产']
#     for type in supplement_type_list:
#         test_dict[type] = first_asset_proportion_dict[type]
#     if len(input_df[(input_df['大类资产'] == '合计')]) > 0:
#         total = input_df[(input_df['大类资产'] == '合计')][use_data_col_name].iloc[0]
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
def cal_first_asset_proportion_and_fund_proportion(input_df, col_name):
    # 资产比例记录
    first_asset = {"固收": 0, "资管产品": 0, "QDII": 0, "其他": 0, "权益类": 0, "商品及衍生品": 0, "非标资产": 0}
    fund_asset = {"公募基金": 0}

    first_asset['固收'] = input_df[((input_df['大类资产'] == '固定收益类') & (input_df['详细大类资产'] != '非标准化债权类资产')
                                  | (input_df['大类资产'] == '货币市场类'))][col_name].sum()
    first_asset['资管产品'] = input_df[(input_df['大类资产'] == '资管产品')][col_name].sum()
    first_asset['QDII'] = input_df[(input_df['大类资产'] == 'QDII')][col_name].sum()
    first_asset['其他'] = input_df[(input_df['大类资产'] == '其他')][col_name].sum()
    first_asset['权益类'] = input_df[(input_df['大类资产'] == '权益类')][col_name].sum()
    first_asset['商品及衍生品'] = input_df[(input_df['大类资产'] == '商品及衍生品')][col_name].sum()
    first_asset['非标资产'] = input_df[(input_df['详细大类资产'] == '非标准化债权类资产')][col_name].sum()

    fund_asset["公募基金"] = input_df[(input_df['详细大类资产'] == '公募基金')][col_name].sum()

    return first_asset, fund_asset


def judge_enhance_type(input):
    input_df = input.copy()

    equity_asset_list = ['权益类', '前十大_权益类']
    commodities_derivatives_asset_list = ['商品及衍生品']
    non_standard_asset_list = ['非标资产', '前十大_非标资产']
    QDII_list = ['QDII', '前十大_QDII']
    enhance_type_list = []

    for index, row in input_df.iterrows():
        asset_list = []
        for asset in equity_asset_list:
            if row[asset] > 0:
                asset_list.append('权益')
                break
        for asset in commodities_derivatives_asset_list:
            # 衍生品投资有亏钱的
            if not np.isnan(row[asset]) and row[asset] != 0:
                asset_list.append('衍生品')
                break
        for asset in non_standard_asset_list:
            if row[asset] > 0:
                asset_list.append('非标')
                break
        for asset in QDII_list:
            if row[asset] > 0:
                asset_list.append('QDII')
                break

        # 是否投资了含权基金
        if row['资产明细是否有含权基金'] == 1 and '权益' not in asset_list:
            asset_list.append('权益')

        # 未识别出固收增强的，判断是否是纯债还是无法判断
        if len(asset_list) == 0:
            # 固收投资>95% 或者 只投纯债类公募的产品基金+固收投资>95% 认为是纯债
            if row['固收'] > 0.95:
                enhance_type_list.append('纯债')
            else:
                enhance_type_list.append('底层数据未披露')
        else:
            asset_list.sort()
            tmp = '固收+(' + ','.join(asset_list) + ')'
            enhance_type_list.append(tmp)

    input_df['enhance_type_asset'] = enhance_type_list
    return input_df


def cal_asset_allocation_ratio(input_df):
    if input_df.shape[0] == 0:
        return

    # 提取用于输出的基础信息
    output_dict = dict(input_df.iloc[0])

    del output_dict['product_code'], output_dict['AssetValue'], output_dict['product_type_chi'], output_dict['primary_type_chi'], output_dict['secondary_type_chi'], \
        output_dict['direct_scale'], output_dict['direct_proportion'], output_dict['direct_proportion_cal_myself'], \
        output_dict['actual_scale'], output_dict['actual_proportion'], output_dict['actual_proportion_cal_myself'],\
        output_dict['actual_proportion_type_chi'], output_dict['data_type_chi']

    # 若actual_proportion字段均为空 且 actual_proportion_cal_myself 字段有值，actual_proportion_cal_myself，actual_proportion
    # 固收+只看穿透后的数据，不看穿透前的数据
    if input_df['actual_proportion'].count() == 0 and input_df['actual_proportion_cal_myself'].count() > 0:
        use_data_col_name = 'actual_proportion_cal_myself'
    else:
        use_data_col_name = 'actual_proportion'

    first_asset_proportion_dict, public_fund_proportion_dict = cal_first_asset_proportion_and_fund_proportion(input_df, use_data_col_name)

    # # #测试使用# 数据验证
    compare_first_asset_sum_with_total(input_df, first_asset_proportion_dict, use_data_col_name)

    # 数据归一化
    first_asset_proportion_norm_dict = proportion_normalization(first_asset_proportion_dict)

    output_dict.update(first_asset_proportion_norm_dict)
    output_dict.update(public_fund_proportion_dict)
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


def get_asset_allocation_ratio(input):
    input_df = input.copy()

    output_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode',
                                      '固收', '资管产品', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产', '公募基金'])

    grouped = input_df.groupby('FinProCode')
    # 固收+产品分类
    index = 0
    print("开始计算资产配置表的资产占比")
    for group_name in list(grouped.groups.keys()):
        res_dict = cal_asset_allocation_ratio(grouped.get_group(group_name))
        output_df = output_df.append(res_dict, ignore_index=True)
        index += 1
        if index % 1000 == 0:
            print(index)
    return output_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--asset_allocation_file', type=str, help='asset_allocation_file', default='金融产品资产配置表映射后.xlsx')
    parser.add_argument('--top10_file', type=str, help='top10_file', default='前十大持仓固收增强分析.xlsx')
    parser.add_argument('--fund_whether_has_equity_file', type=str, help='fund_whether_has_equity_file', default='资产明细是否有含权基金_基于基金持仓.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    args = parser.parse_args()

    asset_allocation_file = args.asset_allocation_file
    top10_file = args.top10_file
    fund_whether_has_equity_file = args.fund_whether_has_equity_file
    statistics_date = args.statistics_date

    if args.statistics_date == '2022-09-30':
        all_data_file = '../../data_pybz/pyjy_bank_wealth_product_0930.csv'
        series_name_file = '../../data_pybz/out5.xlsx'
    elif args.statistics_date == '2022-12-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0424.csv'
        series_name_file = '../../data_pybz/out5-22q4.xlsx'
    elif args.statistics_date == '2023-03-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
        series_name_file = '../../data_pybz/out5-23q1.xlsx'
    else:
        raise ValueError

    all_data_df = pd.read_csv(all_data_file)
    asset_allocation_df = pd.read_excel(asset_allocation_file)
    series_name_df = pd.read_excel(series_name_file)
    top10_df = pd.read_excel(top10_file)
    fund_whether_has_equity_df = pd.read_excel(fund_whether_has_equity_file)

    # 计算理财产品资产配置表投资产的比例
    asset_allocation_ratio_df = get_asset_allocation_ratio(asset_allocation_df)

    # 对bank表进行过滤
    all_data_df = df_preprocess(all_data_df, statistics_date)

    all_data_df = all_data_df.merge(asset_allocation_ratio_df[[
        'FinProCode', '固收', '资管产品', 'QDII', '其他', '权益类', '商品及衍生品', '非标资产', '公募基金']], how='left', on='FinProCode')
    all_data_df = all_data_df.merge(top10_df[['FinProCode', '前十大_权益类', '前十大_非标资产', '前十大_商品及衍生品', '前十大_QDII',
                                              '非标资产投资比例']], how='left', on='FinProCode')
    all_data_df = all_data_df.merge(fund_whether_has_equity_df[['FinProCode', '资产明细是否有含权基金']], how='left', on='FinProCode')

    # 增加系列名称
    series_name_df['set'] = series_name_df['set'].str.split('-').str.get(0)
    all_data_df = pd.merge(all_data_df, series_name_df[['FinProCode', 'set']], how='left', on='FinProCode')

    output_df = judge_enhance_type(all_data_df)
    tmp_output_df = output_df[(output_df['InvestmentType'] == '固定收益类') & (output_df['inv_type'] == 0)]
    tmp_output_df.to_excel('固收增强分类结果.xlsx')
