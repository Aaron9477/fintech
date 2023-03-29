# -*- coding: utf-8 -*-
'''
    代码内容：粗略统计优先股的投资比例判断
    代码目的：通过资产配置表里权益投资占比，预估真权益投资占比是否可行
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

    top10_preferred_stock_df = top10_df[(top10_df['three_level_type'] == '优先股')]
    top10_preferred_stock_count = top10_preferred_stock_df['MarketValue'].sum()

    top10_equity_df = top10_df[(top10_df['primary_type_chi'] == '权益类')]
    top10_equity_count = top10_equity_df['MarketValue'].sum()

    print(top10_preferred_stock_count)
    print(top10_equity_count)

    # asset_deploy_equity_df = asset_deploy_df[(asset_deploy_df['primary_type_chi']) == '权益类']
    # equity_count = asset_deploy_equity_df['actual_scale'].sum()

    print(top10_preferred_stock_count / (top10_preferred_stock_count + top10_equity_count))



