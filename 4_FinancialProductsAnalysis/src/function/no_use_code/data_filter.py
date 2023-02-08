# -*- coding: utf-8 -*-
"""
"""
import time

import pandas as pd
import numpy as np
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/大类资产对应关系.xlsx')
    args = parser.parse_args()
    input_file = args.input_file

    df = pd.read_excel(input_file)
    reflact_dict = dict()
    output_list = set()

    for idx, row in df.iterrows():
        reflact_dict[row['原始科目名称']] = row['修改科目名称']
        output_list.add(row['修改科目名称'])

    raw_asset_data = pd.read_csv('../data/全量金融产品资产配置表_有资产原始名称.csv')

    asset_data_filtered = raw_asset_data[(time.strptime(raw_asset_data['InfoPublDate'], "%Y-%m-%d %H:%M:%S") > time.strptime('2022-06-19', "%Y-%m-%d")) &
                                         raw_asset_data['InfoSource'] == '半年度投资管理报告']

    asset_data_filtered.to_csv('../data/全量金融产品资产配置表_有资产原始名称_filtered.csv')
