# -*- coding: utf-8 -*-
"""
    基金分析第一步：拉取前十大资产中基金类型
"""

import pandas as pd
import numpy as np
import argparse
import datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--wrong_list_file', type=str, help='wrong_list_file', default='../data/疑似有问题的产品列表.txt')
    parser.add_argument('--all_data_file', type=str, help='all_data_file', default='../data/金融产品投资组合明细_22年三季报_230105.csv')
    parser.add_argument('--output_file', type=str, help='all_data_file', default='../data/金融产品投资组合明细_22年三季报_230105_手动修改.csv')
    args = parser.parse_args()

    wrong_fund_name = []
    with open(args.wrong_list_file, 'r', encoding='utf-8') as f:
        for line in f:
            wrong_fund_name.append(line.strip())

    df = pd.read_csv(args.all_data_file)
    ChiName_list = list(df['ChiName'])
    MarketValue_list = list(df['MarketValue'])

    for i in range(len(ChiName_list)):
        if ChiName_list[i] in wrong_fund_name:
            MarketValue_list[i] /= 100

    df['MarketValue'] = MarketValue_list

    df.to_csv(args.output_file)


