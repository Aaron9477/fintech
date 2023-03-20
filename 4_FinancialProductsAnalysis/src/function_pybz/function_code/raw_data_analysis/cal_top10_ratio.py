# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import argparse


def statistics_top10_ratio(input_df):
    if input_df.shape[0] == 0:
        return

    output_dict = {'AgentName': input_df.iloc[0]['AgentName'], 'ChiName': input_df.iloc[0]['ChiName'], 'FinProCode': input_df.iloc[0]['FinProCode']}

    # 优先使用 RatioInNV ，为空使用AssetValueRatio
    if input_df['actual_proportion'].count() > 0:
        use_data_col_name = 'actual_proportion'
    elif input_df['actual_proportion_cal_myself'].count() > 0:
        use_data_col_name = 'actual_proportion_cal_myself'
    else:
        return

    # 资产总和须在1.2以下，有可能加杠杆
    if input_df[use_data_col_name].sum() > 1.2:
        return

    output_dict['top10_ratio_sum'] = input_df[use_data_col_name].sum()
    output_dict['top10_bond_ratio_sum'] = input_df[(input_df['secondary_type_chi'] == '债券')][use_data_col_name].sum()

    return output_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    if args.statistics_date == '2022-09-30':
        top10_file = '../../../data_pybz/pybz_金融产品前十名持仓_22年三季报_230314.csv'
    elif args.statistics_date == '2022-12-31':
        top10_file = '../../../data_pybz/pybz_金融产品前十名持仓_22年四季报_230315.csv'
    else:
        raise ValueError

    top10_df = pd.read_csv(top10_file)

    output_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode', 'top10_ratio_sum', 'top10_bond_ratio_sum'])
    top10_ratio_sum_list = []
    top10_bond_ratio_sum_list = []

    index = 0
    grouped = top10_df.groupby('FinProCode')
    for group_name in list(grouped.groups.keys()):
        res_dict = statistics_top10_ratio(grouped.get_group(group_name))
        if res_dict:
            top10_ratio_sum_list.append(res_dict['top10_ratio_sum'])
            top10_bond_ratio_sum_list.append(res_dict['top10_bond_ratio_sum'])
            output_df = output_df.append(res_dict, ignore_index=True)
        index += 1
        if index % 1000 == 0:
            print(index)

    print("前十大投资比例之和的均值是{}".format(np.mean(top10_ratio_sum_list)))
    print("前十大投资比例之和的中位数是{}".format(np.median(top10_ratio_sum_list)))

    print("前十大中债券投资比例之和的均值是{}".format(np.mean(top10_bond_ratio_sum_list)))
    print("前十大中债券投资比例之和的中位数是{}".format(np.median(top10_bond_ratio_sum_list)))

