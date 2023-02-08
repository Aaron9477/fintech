# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤一：基于智妍的大类资产映射关系，对大类资产做分类
"""
import pandas as pd
import numpy as np
import argparse
from func import choose_report_asset_table, choose_product_mother_son, get_product_exist

# 对大类资产中的固定收益类和资管产品做详细分类
def get_major_assets(row):
    if row['AssetName'] not in reflact_dict.keys():
        return 'None'
    major_assets_detail = reflact_dict[row['AssetName']]
    # '固定收益类:权益类'在智妍映射关系里映射到了权益类，此处应当过滤
    if major_assets_detail.startswith('固定收益类') and major_assets_detail != '固定收益类:权益类':
        return '固定收益类'
    # '资管产品:'开头的均为'资管产品'大类
    elif major_assets_detail.startswith('资管产品'):
        return '资管产品'
    else:
        return major_assets_detail


# 基于get_major_assets增加非标资产的拆解
def get_major_assets2(row):
    if row['AssetName'] not in reflact_dict.keys():
        return 'None'
    major_assets_detail = reflact_dict[row['AssetName']]
    if major_assets_detail == '固定收益类:非标准化债权类':
        return '非标资产'
    # '固定收益类:权益类'在智妍映射关系里映射到了权益类，此处应当过滤
    elif major_assets_detail.startswith('固定收益类') and major_assets_detail != '固定收益类:权益类':
        return '固定收益类'
    # '资管产品:'开头的均为'资管产品'大类
    elif major_assets_detail.startswith('资管产品'):
        return '资管产品'
    else:
        return major_assets_detail


def get_major_assets_detail(row):
    if row['AssetName'] not in reflact_dict.keys():
        if row['AssetName'] not in asset_name_not_in_dict.keys():
            asset_name_not_in_dict[row['AssetName']] = 0
        asset_name_not_in_dict[row['AssetName']] += 1
        return 'None'
    major_assets_detail = reflact_dict[row['AssetName']]
    return major_assets_detail


# 前处理模块 部分规则由智妍提供
def df_preprocess(input_df, all_data_df, statistics_date):
    # 筛选子产品 all_data_df
    all_data_df = choose_product_mother_son(all_data_df)
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    # 筛选存续期产品
    input_df = get_product_exist(input_df, statistics_date)

    # 报告筛选
    input_df = choose_report_asset_table(input_df, statistics_date)

    # 只使用穿透前的数据（当前资产配置表只有穿透前的数据）
    input_df = input_df[(input_df['PenetrationType'] == 'FCC0000019PK')]

    # 光大理财：将“固定收益投资“修改为”私募资管产品:固定收益投资“
    input_df.loc[(input_df['AgentName'] == '光大理财有限责任公司') & (input_df['AssetName'] == '固定收益投资'), 'AssetName'] = '私募资管产品:固定收益投资'

    # 广银理财&平安理财：AssetName=="基金投资"直接删掉
    input_df = input_df.drop(input_df[((input_df['AgentName'] == '广银理财有限责任公司') | (input_df['AgentName'] == '平安理财有限责任公司')) & (input_df['AssetName'] == '基金投资')].index)

    return input_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/大类资产对应关系.xlsx')
    parser.add_argument('--raw_asset_file', type=str, help='raw_asset_file', default='../data/金融产品资产配置_22年三季报_230105.csv')
    parser.add_argument('--all_data_file', type=str, help='all_data_file', default='../data/bank_wealth_product_12_22.csv')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')


    args = parser.parse_args()
    input_file = args.input_file
    raw_asset_file = args.raw_asset_file
    statistics_date = args.statistics_date

    raw_asset_data = pd.read_csv(raw_asset_file)
    df = pd.read_excel(input_file, sheet_name='原始科目对应详细大类资产')
    all_data_df = pd.read_csv(args.all_data_file)[['FinProCode', 'ActMaturityDate', 'ProductMaturityDate',
                                                   'product_establish_date', 'RegistrationCode', 'ProductType']]

    reflact_dict = dict()
    output_list = set()

    for idx, row in df.iterrows():
        reflact_dict[row['原始科目名称']] = row['修改科目名称']
        output_list.add(row['修改科目名称'])

    raw_asset_data.insert(loc=9, column='详细大类资产', value='')
    raw_asset_data.insert(loc=10, column='大类资产', value='')

    # 统计大类资产映射表不能覆盖的字段
    asset_name_not_in_dict = dict()

    # 数据前处理
    raw_asset_data = df_preprocess(raw_asset_data, all_data_df, statistics_date)

    raw_asset_data['详细大类资产'] = raw_asset_data.apply(lambda x: get_major_assets_detail(x), axis=1)
    # # 对大类资产中的固定收益类和资管产品做详细分类
    # raw_asset_data['大类资产'] = raw_asset_data.apply(lambda x: get_major_assets(x), axis=1)
    # 基于get_major_assets增加非标资产的拆解
    raw_asset_data['大类资产'] = raw_asset_data.apply(lambda x: get_major_assets2(x), axis=1)

    raw_asset_data.to_excel('金融产品资产配置表_分类后.xlsx')




