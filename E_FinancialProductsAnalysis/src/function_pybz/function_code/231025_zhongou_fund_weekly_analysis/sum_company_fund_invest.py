'''
    统计各个理财子投资基金规模之和
    基于get_company_invest_fund_detail.py的统计结果，该结果是先统计穿透后，再统计穿透前（如果穿透后没有数据）
'''
import pandas as pd
import numpy as np
import argparse
import datetime


# 统计理财产品在非标资产的总投资比例
def cal_non_standard_asset_sum(input_df):
    grouped = input_df.groupby(['理财公司']).agg({'基金投资规模(万元)': sum})
    actual_proportion_list = list(grouped['基金投资规模(万元)'].items())
    res_list = []
    for i in range(len(actual_proportion_list)):
        res_list.append([actual_proportion_list[i][0], actual_proportion_list[i][1]])

    col_name = ['理财公司', '基金投资规模(万元)']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    return df_res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='理财投资公募穿透后统计.xlsx')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-06-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-06-30')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财公司投资公募穿透后统计.xlsx')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    input_file = args.input_file.split('.')[0] + '_' + statistics_date + '.xlsx'
    output_file = args.output_file.split('.')[0] + '_' + statistics_date + '.xlsx'

    input_df = pd.read_excel(input_file)
    output_df = cal_non_standard_asset_sum(input_df)
    output_df.to_excel(output_file)
