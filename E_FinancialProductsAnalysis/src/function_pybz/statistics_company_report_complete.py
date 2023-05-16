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
    grouped = input_df.groupby(['CompanyName']).agg({'是否需要发季报': "sum", '是否已发季报': "sum", 'FinProCode': "count"})
    need_push = list(grouped['是否需要发季报'].items())
    already_push = list(grouped['是否已发季报'].items())
    all_num = list(grouped['FinProCode'].items())
    res_list = []
    for i in range(len(need_push)):
        res_list.append([need_push[i][0], need_push[i][1], already_push[i][1], all_num[i][1]])

    col_name = ['理财公司', '需要发季报数量', '已发季报数量', '产品总数']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    df_res["已发季报占总产品数的比例"] = df_res["已发季报数量"] / df_res["产品总数"]
    df_res["已发季报占需要发季报产品数的比例"] = df_res["已发季报数量"] / df_res["需要发季报数量"]

    return df_res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='产品是否披露季报明细.xlsx')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-06-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财公司披露季报后统计.xlsx')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    input_file = args.input_file.split('.')[0] + '_' + statistics_date + '.xlsx'
    output_file = args.output_file.split('.')[0] + '_' + statistics_date + '.xlsx'

    input_df = pd.read_excel(input_file)
    output_df = cal_non_standard_asset_sum(input_df)
    output_df.to_excel(output_file)
