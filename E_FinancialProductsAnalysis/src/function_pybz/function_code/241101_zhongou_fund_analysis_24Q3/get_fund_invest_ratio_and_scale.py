# -*- coding: utf-8 -*-
"""
    基金分析第一步：拉取前十大资产中基金类型
"""

import pandas as pd
import numpy as np
import argparse
import datetime

def df_preprocess(input_df, statistics_date):
    def get_main_product_ind(data_set_RegistrationCode):
        ProductTypes = data_set_RegistrationCode['ProductType']
        tags = ['母产品', '产品', '子产品']
        for tag in tags:
            if tag in ProductTypes.values:
                return ProductTypes[ProductTypes == tag].index[0]

    output_df = input_df.copy()

    # 筛选子产品 all_data_df
    RegistrationCodes = list(set(output_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = output_df[output_df['RegistrationCode'] == RegistrationCode]
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    output_df = output_df[output_df.index.isin(RegistrationCode_mainind)]

    return output_df


def get_fund_type(row):
    if row['secondary_type_chi'] == '公募基金':
        return 0
    else:
        return 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-06-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-06-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2024-06-30')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2024-09-30')

    parser.add_argument('--output_file', type=str, help='output_file', default='理财投资公募穿透后统计.xlsx')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    output_file = args.output_file.split('.')[0] + '_' + statistics_date + '.xlsx'

    if args.statistics_date == '2022-06-30':
        asset_invest_file = '../../22年Q2/金融产品资产配置表映射后.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
    elif args.statistics_date == '2022-09-30':
        asset_invest_file = '../../22年Q3/金融产品资产配置表映射后.xlsx'
        all_data_file = '../../../data_pybz/pyjy_bank_wealth_product_0930.csv'
    elif args.statistics_date == '2022-12-31':
        asset_invest_file = '../../22年Q4/金融产品资产配置表映射后.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_1231.csv'
    elif args.statistics_date == '2023-03-31':
        asset_invest_file = '../../23年Q1/金融产品资产配置表映射后.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
    elif args.statistics_date == '2023-06-30':
        asset_invest_file = '../../23年Q2/金融产品资产配置表映射后.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_0630.csv'
    elif args.statistics_date == '2023-09-30':
        asset_invest_file = '../../23年Q3/金融产品资产配置表映射后.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_0930.csv'
    elif args.statistics_date == '2024-03-31':
        asset_invest_file = '../../24年Q1/金融产品资产配置表映射后.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_240331_240514.csv'
    elif args.statistics_date == '2024-06-30':
        asset_invest_file = '../../24年Q2/金融产品资产配置表映射后.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_24Q2_240923.csv'
    elif args.statistics_date == '2024-09-30':
        asset_invest_file = '../../24年Q3/金融产品资产配置表映射后.xlsx'
        # todo:此处未修改
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_24Q2_240923.csv'
    else:
        raise ValueError

    asset_invest_df = pd.read_excel(asset_invest_file)
    asset_invest_df = asset_invest_df[(asset_invest_df['primary_type_chi'] == '基金') & (asset_invest_df['secondary_type_chi'] != '私募基金')]

    # 投资比例：优先使用穿透后的数据，优先使用季报提供的原始数据
    asset_invest_df['actual_proportion_used'] = np.where(asset_invest_df['actual_proportion'].isnull(),
                                             asset_invest_df['actual_proportion_cal_myself'], asset_invest_df['actual_proportion'])
    asset_invest_df['direct_proportion_used'] = np.where(asset_invest_df['direct_proportion'].isnull(),
                                             asset_invest_df['direct_proportion_cal_myself'], asset_invest_df['direct_proportion'])
    asset_invest_df['proportion_used'] = np.where(asset_invest_df['actual_proportion_used'].isnull(),
                                             asset_invest_df['direct_proportion_used'], asset_invest_df['actual_proportion_used'])

    # 投资规模：优先使用穿透后的数据
    asset_invest_df['scale_used'] = np.where(asset_invest_df['actual_scale'].isnull(),
                                             asset_invest_df['direct_scale'], asset_invest_df['actual_scale'])

    asset_invest_df['0-披露资产名为公募基金\n1-披露资产名为基金'] = asset_invest_df.apply(lambda x: get_fund_type(x), axis=1)

    # 转化为万元为单位
    asset_invest_df['AssetValue'] = asset_invest_df['AssetValue'] / 10000
    asset_invest_df['scale_used'] = asset_invest_df['scale_used'] / 10000

    asset_invest_df = asset_invest_df[['AgentName', 'ChiName', 'product_code', 'FinProCode', 'product_type_chi', 'EndDate',
                                       'AssetValue', 'scale_used', 'proportion_used', '0-披露资产名为公募基金\n1-披露资产名为基金']]


    all_data_df = pd.read_csv(all_data_file)

    # 过滤子产品保留母产品
    all_data_df = df_preprocess(all_data_df, args.statistics_date)
    all_data_df = all_data_df[['FinProCode']]

    asset_invest_df = asset_invest_df.merge(all_data_df, how='inner', on='FinProCode')
    asset_invest_df = asset_invest_df.drop(labels='FinProCode', axis=1)

    asset_invest_df.rename(columns={'AgentName': '理财公司', 'ChiName': '理财产品', 'product_code': '产品编码', 'product_type_chi': '产品类型',
                                    'EndDate': '报告日期', 'AssetValue': '产品规模(万元)', 'scale_used': '基金投资规模(万元)',
                                    'proportion_used': '基金投资比例'}, inplace=True)

    asset_invest_df.to_excel(output_file)



    # df = append_product_fund_sum(df)
    #
    # SecuCode_new = code_preprocess(df['SecuCode'].values)
    # df['SecuCode_new'] = SecuCode_new
    #
    # df['该基金市值占理财产品资产比例'] = df['MarketValue'] / df['AssetValue_new']
    # df['AssetValue_new'].replace(0, '', inplace=True)
    # df['该基金市值占理财产品资产比例'].replace(np.inf, '', inplace=True)
    #
    # df.rename(columns={'AgentName': '理财公司', 'ChiName': '理财产品', 'SecuCode_new': '基金代码',
    #                    '基金一级分类': 'wind一级分类', '基金二级分类': 'wind二级分类', 'MarketValue': '理财产品持有基金市值（万元）',
    #                    'AssetValue_new': '理财产品总资产（万元）', '一年回报': '基金近一年收益', '二年回报': '基金近二年收益',
    #                    '三年回报': '基金近三年收益', '五年回报': '基金近五年收益'}, inplace=True)
    #
    # df['理财产品持有基金市值（万元）'] = df['理财产品持有基金市值（万元）'] / 10000
    # df['理财产品持有基金总规模（万元）'] = df['理财产品持有基金总规模（万元）'] / 10000
    # all_asset_list = list(df['理财产品总资产（万元）'])
    # for i in range(len(all_asset_list)):
    #     if not isinstance(all_asset_list[i], str) and not np.isnan(all_asset_list[i]):
    #         all_asset_list[i] = all_asset_list[i] / 10000
    # df['理财产品总资产（万元）'] = all_asset_list
    # df['基金近一年收益'] = df['基金近一年收益'] / 100
    # df['基金近二年收益'] = df['基金近二年收益'] / 100
    # df['基金近三年收益'] = df['基金近三年收益'] / 100
    # df['基金近五年收益'] = df['基金近五年收益'] / 100
    #
    # final_df = df[['理财公司', '理财产品', '基金简称', '基金代码', '基金公司', 'wind一级分类', 'wind二级分类', '理财产品持有基金市值（万元）',
    #                '理财产品持有基金总规模（万元）', '理财产品总资产（万元）', '该基金市值占理财产品资产比例', '基金近一年收益', '基金近二年收益',
    #                '基金近三年收益', '基金近五年收益']]

