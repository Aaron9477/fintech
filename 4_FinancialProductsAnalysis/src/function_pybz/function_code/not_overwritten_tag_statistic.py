# -*- coding: utf-8 -*-
"""
统计智妍的映射表没有覆盖的资产名称
"""
import pandas as pd
import numpy as np
import argparse

def get_major_assets(row):
    if row['AssetName'] not in reflact_dict.keys():
        return 'None'
    major_assets_detail = reflact_dict[row['AssetName']]
    # '固定收益类:'开头的均为'固定收益类'大类，除了'固定收益类:权益类'
    if major_assets_detail.startswith('固定收益类') and major_assets_detail != '固定收益类:权益类':
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/大类资产对应关系.xlsx')
    args = parser.parse_args()
    input_file = args.input_file

    df = pd.read_excel(input_file, sheet_name='原始科目对应详细大类资产')
    reflact_dict = dict()
    output_list = set()

    for idx, row in df.iterrows():
        reflact_dict[row['原始科目名称']] = row['修改科目名称']
        output_list.add(row['修改科目名称'])


    raw_asset_data = pd.read_csv('../data/全量金融产品资产配置表_限定理财子_221025.csv')
    raw_asset_data.insert(loc=9, column='详细大类资产', value='')
    raw_asset_data.insert(loc=10, column='大类资产', value='')
    asset_name_not_in_dict = dict()

    raw_asset_data['详细大类资产'] = raw_asset_data.apply(lambda x: get_major_assets_detail(x), axis=1)
    raw_asset_data['大类资产'] = raw_asset_data.apply(lambda x: get_major_assets(x), axis=1)

    # raw_asset_data.to_excel('全量金融产品资产配置表_限定理财子_221025_分类后.xlsx')

    print(asset_name_not_in_dict)
    asset_name_not_in_sort_list = sorted(asset_name_not_in_dict.items(), key=lambda x: x[1], reverse=True)
    print(asset_name_not_in_sort_list)

    output_name_list = []
    output_num_list = []
    for info in asset_name_not_in_sort_list:
        output_name_list.append(info[0])
        output_num_list.append(info[1])

    dict1 = {"标签名": output_name_list, "出现次数": output_num_list}
    output_df = pd.DataFrame(dict1)
    output_df.to_excel('未覆盖标签.xlsx')

    # for idx, row in raw_asset_data.iterrows():
    #     if idx % 1000 == 0:
    #         print(idx)
    #     # 该大类资产没有做归类
    #     if row['AssetName'] not in reflact_dict.keys():
    #         asset_name_not_in_dict.add(row['AssetName'])
    #         continue
    #     major_assets_detail = reflact_dict[row['AssetName']]
    #     row['详细大类资产'] = major_assets_detail
    #
    #     if major_assets_detail.startswith('固定收益类'):
    #         row['大类资产'] = '固定收益类'
    #     elif major_assets_detail.startswith('资管产品'):
    #         row['大类资产'] = '资管产品'
    #     else:
    #         row['大类资产'] = major_assets_detail
    #
    #     # 对row的修改是临时的，需要下面的语句，才能生效
    #     raw_asset_data.iloc[idx] = row
    #
    #
    # raw_asset_data.to_excel('大类资产分类后的资产配置.xlsx')





