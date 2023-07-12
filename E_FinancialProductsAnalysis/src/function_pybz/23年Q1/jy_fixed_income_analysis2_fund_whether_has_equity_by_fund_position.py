# -*- coding: utf-8 -*-
"""
    固收+统计分析步骤二：通过统计持仓前十大中基金的权益持仓占比，判断是否有含权基金
"""
import pandas as pd
import numpy as np
import argparse
from WindPy import w

from func import get_trading_day


def judge_equity_fund(df):
    fund_first_type_list = df['是否是含权基金'].values
    FLAG = 0
    for i in range(len(fund_first_type_list)):
        if fund_first_type_list[i] > 0:
            FLAG = 1

    return FLAG


def code_preprocess(input_list):
    res_list = []
    for x in input_list:
        x = str(x)
        if len(x) > 6:
            x = x[:6]
        x = x.split('.')[0].split(' ')[0]
        res_list.append(x + '.OF')
    return res_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    parser.add_argument('--output_file', type=str, help='output_file', default='jy_资产明细是否有含权基金_基于基金持仓.xlsx')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    output_file = args.output_file
    fund_data_file = 'jy_基金信息_{}.xlsx'.format(statistics_date)

    trading_day = get_trading_day(statistics_date)

    fund_data_df = pd.read_excel(fund_data_file)

    fund_list = code_preprocess(fund_data_df['SecuCode'].values)
    fund_set = set(fund_list)
    fund_str = ','.join(fund_set)

    w.start()
    wind_return = w.wsd(fund_str, "prt_stocktonav", trading_day, trading_day, "")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    value_list = [fund_value_dict[x] for x in fund_list]
    fund_data_df['权益持仓占比'] = value_list

    fund_data_df.to_excel("jy_基金权益持仓情况.xlsx")

    whether_has_equity = []
    for value in value_list:
        if value > 5:
            whether_has_equity.append(1)
        else:
            whether_has_equity.append(0)

    fund_data_df['是否是含权基金'] = whether_has_equity

    whether_has_equity_df = pd.DataFrame(columns=["FinProCode", "资产明细是否有含权基金"])


    grouped = fund_data_df.groupby('FinProCode')
    for group_name in list(grouped.groups.keys()):
        res_dict = {"FinProCode": group_name, "资产明细是否有含权基金": judge_equity_fund(grouped.get_group(group_name))}
        whether_has_equity_df = whether_has_equity_df.append(res_dict, ignore_index=True)

    whether_has_equity_df.to_excel(output_file)

