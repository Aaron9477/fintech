# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤二：计算各个理财产品大类资产的配比情况
"""
import copy

import pandas as pd
import numpy as np
import argparse
from enum import Enum

from WindPy import w


if __name__ == '__main__':

    a = w.start()
    print(a)

    # parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data_pybz/代销产品-中信建投.xlsx')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    # args = parser.parse_args()
    #
    # if args.statistics_date == '2022-09-30':
    #     target_file = '../data_pybz/pyjy_bank_wealth_product_0930.csv'
    # elif args.statistics_date == '2022-12-31':
    #     # target_file = '../data_pybz/pyjy_bank_wealth_product_0306.csv'
    #     target_file = '../data_pybz/pyjy_bank_wealth_product_0321.csv'
    # else:
    #     raise ValueError
    #
    # input_file = args.input_file
    #
    # input_df = pd.read_excel(input_file)
    # target_df = pd.read_csv(target_file)
    #
    # input_df = input_df.merge(target_df, left_on='普益代码', right_on='FinProCode', how='left')
    # input_df.to_excel('test.xlsx')