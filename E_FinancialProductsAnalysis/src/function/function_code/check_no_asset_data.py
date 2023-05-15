# -*- coding: utf-8 -*-

"""
Created on Tue Dec 12 17:20:45 2022
检查资产配置数据不存在的产品，是否有总资产规模
@author: 王永镇
"""
import pandas as pd
import numpy as np
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--asset_allocation_file', type=str, help='input_file', default='没有资产规模的资产配置表.xlsx')
    parser.add_argument('--details_file', type=str, help='input_file', default='../../data/bank_wealth_product_12_11.xlsx')
    args = parser.parse_args()
    asset_allocation_file = args.asset_allocation_file
    details_file = args.details_file

    asset_allocation_df = pd.read_excel(asset_allocation_file)
    details_df = pd.read_excel(details_file)
    details_df = details_df[['FinProCode', 'AssetValue']]

    res_df = pd.merge(asset_allocation_df, details_df, how='left', on='FinProCode')
    res_df.to_excel('res.xlsx')




