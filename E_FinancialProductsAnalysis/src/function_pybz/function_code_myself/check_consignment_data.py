# -*- coding: utf-8 -*-
"""
    聚源代销数据与普益数据对比
"""
import pandas as pd
import numpy as np
import argparse
import datetime
import copy
import openpyxl

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--jy_file', type=str, help='jy_df', default='jy_22年以来四家理财子代销统计_230518(1).csv')
    parser.add_argument('--py_file', type=str, help='py_df', default='中信建投-代销.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    args = parser.parse_args()

    jy_df = pd.read_csv(args.jy_file)
    py_df = pd.read_excel(args.py_file)

    py_df['代销开始日'] = pd.to_datetime(py_df['代销开始日'])
    py_df = py_df[(py_df['代销开始日'] > '20230101')]

    jy_RegistrationCode = jy_df['RegistrationCode'].unique().tolist()
    py_RegistrationCode = py_df['产品登记编码'].unique().tolist()

    diff = list(set(py_RegistrationCode).difference(set(jy_RegistrationCode)))

    output = pd.DataFrame(diff, columns=['缺失代销数据的产品登记编码'])

    output.to_excel('代销数据缺失产品产品登记编码明细.xlsx')

    print(len(jy_RegistrationCode))
    print(len(py_RegistrationCode))
    print(len(diff))

    print("\n")
    print(diff)