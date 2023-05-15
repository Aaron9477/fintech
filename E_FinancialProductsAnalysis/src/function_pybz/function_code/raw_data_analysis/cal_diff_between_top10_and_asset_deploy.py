# -*- coding: utf-8 -*-
'''
    代码内容：粗略统计某类资产在资产配置表里的投资比例与前十大投资比例之差（代码以债券为例）
    代码目的：分析前十大资产表能体现多少该类型资产
'''
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


def get_union_set(row):
    if np.isnan(row['actual_proportion']):
        return row['actual_proportion_cal_myself']
    else:
        return row['actual_proportion']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    if args.statistics_date == '2022-09-30':
        top10_file = '../../../data_pybz/pybz_金融产品前十名持仓_22年三季报_230314.csv'
        asset_deploy_file = '../../../data_pybz/pybz_金融产品资产配置_22年三季报_230314.csv'
    elif args.statistics_date == '2022-12-31':
        top10_file = '../../../data_pybz/pybz_金融产品前十名持仓_22年四季报_230315.csv'
        asset_deploy_file = '../../../data_pybz/pybz_金融产品资产配置_22年四季报_230315.csv'
    else:
        raise ValueError

    top10_df = pd.read_csv(top10_file)
    asset_deploy_df = pd.read_csv(asset_deploy_file)

    asset_deploy_bond_df = asset_deploy_df[(asset_deploy_df['secondary_type_chi']) == '债券']
    asset_deploy_bond_df['actual_proportion_union'] = asset_deploy_bond_df.apply(lambda x: get_union_set(x), axis=1)
    asset_deploy_bond_df = asset_deploy_bond_df[['FinProCode', 'actual_proportion_union']]

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

    output_df = output_df.merge(asset_deploy_bond_df, how='inner', on='FinProCode')
    output_df = output_df[output_df['top10_bond_ratio_sum'].notnull() & np.isnan(output_df['actual_proportion_union']).notnull()]
    output_df['bond_ratio_diff'] = output_df['actual_proportion_union'] - output_df['top10_bond_ratio_sum']
    output_df = output_df[(output_df['bond_ratio_diff'] >= -0.05)]

    output_df.to_excel('test.xlsx')

    print("债券资产配置比例与债券前十大投资比例之差的均值是{}".format(output_df['bond_ratio_diff'].mean()))
    print("债券资产配置比例与债券前十大投资比例之差的中位数是{}".format(output_df['bond_ratio_diff'].median()))


