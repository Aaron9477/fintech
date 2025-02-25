'''
    统计各个理财子投资基金规模之和
    基于get_company_invest_fund_detail.py的统计结果，该结果是先统计穿透后，再统计穿透前（如果穿透后没有数据）
    数据输出到给中欧基金报告“24Q3理财投基金的规模统计数据.xlsx”的半年报披露规模统计sheet的“产品季报统计基金投资规模（万元）”和“产品季报统计前十大基金投资规模（万元）”
'''
import pandas as pd
import numpy as np
import argparse
import datetime


def cal_company_fund_invest_asset_sum(input_df):
    grouped = input_df.groupby(['理财公司']).agg({'基金投资规模(万元)': sum})
    actual_proportion_list = list(grouped['基金投资规模(万元)'].items())
    res_list = []
    for i in range(len(actual_proportion_list)):
        res_list.append([actual_proportion_list[i][0], actual_proportion_list[i][1]])

    col_name = ['理财公司', '基金投资规模(万元)']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    return df_res


def cal_company_fund_invest_top10_sum(input_df):
    grouped = input_df.groupby(['理财公司']).agg({'持有基金市值（万元）': sum})
    actual_proportion_list = list(grouped['持有基金市值（万元）'].items())
    res_list = []
    for i in range(len(actual_proportion_list)):
        res_list.append([actual_proportion_list[i][0], actual_proportion_list[i][1]])

    col_name = ['理财公司', '持有基金市值（万元）']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    return df_res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file1', type=str, help='input_file1', default='理财投资公募穿透后统计.xlsx')
    parser.add_argument('--input_file2', type=str, help='input_file2', default='理财公司重仓基金明细表.xlsx')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-06-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-09-30')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2024-12-31')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财公司投资公募总规模and前十大统计.xlsx')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    input_file1 = args.input_file1.split('.')[0] + '_' + statistics_date + '.xlsx'
    input_file2 = args.input_file2.split('.')[0] + '_' + statistics_date + '.xlsx'
    output_file = args.output_file.split('.')[0] + '_' + statistics_date + '.xlsx'

    input_df1 = pd.read_excel(input_file1)
    input_df2 = pd.read_excel(input_file2, sheet_name='理财子前十大基金')

    output_df1 = cal_company_fund_invest_asset_sum(input_df1)
    output_df2 = cal_company_fund_invest_top10_sum(input_df2)

    writer = pd.ExcelWriter(output_file)
    output_df1.to_excel(writer, sheet_name='穿透后总规模统计')
    output_df2.to_excel(writer, sheet_name='前十大总规模统计')
    writer.save()

