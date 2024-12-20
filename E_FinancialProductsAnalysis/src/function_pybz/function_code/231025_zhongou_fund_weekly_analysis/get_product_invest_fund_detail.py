# -*- coding: utf-8 -*-
"""
    基金分析第一步：拉取前十大资产中基金类型
"""

import pandas as pd
import numpy as np
import argparse
from datetime import datetime
import pdb


def code_preprocess(input_list):
    res_list = []
    for x in input_list:
        x = str(x)
        if len(x) > 6:
            x = x[:6]
        x = x.split('.')[0].split(' ')[0]
        res_list.append(x + '.OF')
    return res_list


def append_product_fund_sum(input_df):
    df = input_df.copy()
    company_asset_num_sum = df.groupby('FinProCode')['MarketValue'].sum()
    res_list = []
    for line in list(company_asset_num_sum.items()):
        res_list.append([line[0], line[1]])
    col_name = ['FinProCode', '理财产品持有基金总规模（万元）']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    df_res = input_df.merge(df_res, how='left', on='FinProCode')

    return df_res


def df_preprocess(input_df, statistics_date):
    def get_main_product_ind(data_set_RegistrationCode):
        ProductTypes = data_set_RegistrationCode['ProductType']
        tags = ['母产品', '产品', '子产品']
        for tag in tags:
            if tag in ProductTypes.values:
                return ProductTypes[ProductTypes == tag].index[0]

    def get_product_exist(input, statistics_date):
        input_df = input.copy()

        input_df = input_df[(((input_df['MaturityDate'].isnull()) | (input_df['MaturityDate'] > statistics_date)))
                            & (input_df['product_establish_date'] < statistics_date)]
        return input_df

    output_df = input_df.copy()

    output_df = get_product_exist(output_df, statistics_date)

    # 筛选子产品 all_data_df
    RegistrationCodes = list(set(output_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = output_df[output_df['RegistrationCode'] == RegistrationCode]
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    output_df = output_df[output_df.index.isin(RegistrationCode_mainind)]

    return output_df


def init_add_latest_asset(input, latest_asset_df, zxjt_classify_df):
    input_df = input.copy()
    input_df = input_df.merge(latest_asset_df[['FinProCode', 'Latest_AssetValue_Date', 'Latest_AssetValue']], how='left', on='FinProCode')
    input_df['最新产品规模（万元）'] = np.where(input_df['Latest_AssetValue_Date'] > '2023-06-30',
                                  input_df['Latest_AssetValue'], input_df['AssetValue']) / 10000
    input_df['最新规模披露时间'] = np.where(input_df['Latest_AssetValue_Date'] > '2023-06-30',
                                  input_df['Latest_AssetValue_Date'], '2023-06-30')

    input_df['理财规模数据本周是否更新'] = np.where(input_df['Latest_AssetValue_Date'] > '2023-06-30', "是", "否")
    input_df['上次披露规模（万元）'] = input_df['AssetValue'] / 10000
    input_df['上次披露时间'] = '2023-06-30'
    input_df['相对上次披露的规模变化'] = input_df['Latest_AssetValue'] / input_df['上次披露规模（万元）'] / 10000 -1
    input_df['相对季初的规模变化'] = input_df['Latest_AssetValue'] / input_df['AssetValue'] - 1

    # 普益固收+分类细化
    def adjust_zxjt_classify(row):
        if not isinstance(row['final_enhance_type_asset'], str) and np.isnan(row['final_enhance_type_asset']) and \
                (row['product_type_son'] == '偏债混合' or row['product_type_son'] == '偏股混合'):
            return row['product_type_son']
        else:
            return row['final_enhance_type_asset']

    input_df = input_df.merge(zxjt_classify_df[['FinProCode', 'final_enhance_type_asset']], how='left', on='FinProCode')
    input_df['中信建投二级分类'] = input_df.apply(lambda x: adjust_zxjt_classify(x), axis=1)

    # 普益固收+分类细化
    def adjust_pybz_classify(row):
        if row['product_type_son'] != '固收+':
            return row['product_type_son']
        else:
            if np.isnan(row['equity_upper']) or row['equity_upper'] == 0:
                return '不可投权益固收+'
            else:
                return '可投权益固收+'

    input_df['普益二级分类'] = input_df.apply(lambda x: adjust_pybz_classify(x), axis=1)

    return input_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-06-30')

    parser.add_argument('--latest_asset_file', type=str, help='latest_asset_file', default='../../../data_pybz/pybz_bank表_增加最新规模_231025.csv')
    parser.add_argument('--zxjt_classify_file', type=str, help='latest_asset_file', default='../../../function_pybz/23年Q2/固收增强分类结果_final.xlsx')
    parser.add_argument('--score_file', type=str, help='score_file', default='全部基金量化打分排名.xlsx')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财产品重仓基金明细表.xlsx')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    latest_asset_file = args.latest_asset_file
    zxjt_classify_file = args.zxjt_classify_file
    score_file = args.score_file
    output_file = args.output_file.split('.')[0] + '_' + statistics_date + '.xlsx'

    if args.statistics_date == '2022-09-30':
        input_file = '../../22年Q3/基金信息_2022-09-30.xlsx'
        all_data_file = '../../../data_pybz/pyjy_bank_wealth_product_0930.csv'
    elif args.statistics_date == '2022-12-31':
        input_file = '../../22年Q4/基金信息_2022-12-31.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_1231.csv'
    elif args.statistics_date == '2023-03-31':
        input_file = '../../23年Q1/基金信息_2023-03-31.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
    elif args.statistics_date == '2023-06-30':
        input_file = '../../23年Q2/基金信息_2023-06-30.xlsx'
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_0630.csv'
    else:
        raise ValueError

    all_data_df = pd.read_csv(all_data_file)
    latest_asset_df = pd.read_csv(latest_asset_file)
    zxjt_classify_df = pd.read_excel(zxjt_classify_file)
    all_data_df = df_preprocess(all_data_df, args.statistics_date)
    all_data_df = all_data_df[['FinProCode', 'EndDate', 'AssetValue', 'InvestmentType', 'product_type_son', 'equity_upper']]
    all_data_df.rename(columns={'AssetValue': 'AssetValue_new'}, inplace=True)

    df = pd.read_excel(input_file)
    df = df.merge(all_data_df, how='left', on='FinProCode')

    # # 一般数据有正确都会有EndDate
    EndDate_list = list(df['EndDate_y'])
    AssetValue_new_list = list(df['AssetValue_new'])
    for i in range(len(EndDate_list)):
        if not isinstance(EndDate_list[i], str) and np.isnan(EndDate_list[i]):
            AssetValue_new_list[i] = 0
    df['AssetValue_new'] = AssetValue_new_list

    AssetValue_new_list = list(df['AssetValue_new'])
    for i in range(len(AssetValue_new_list)):
        if not isinstance(AssetValue_new_list[i], str) and np.isnan(AssetValue_new_list[i]):
            AssetValue_new_list[i] = 0
    df['AssetValue_new'] = AssetValue_new_list

    df = append_product_fund_sum(df)

    SecuCode_new = code_preprocess(df['SecuCode'].values)
    df['SecuCode_new'] = SecuCode_new

    df['该基金市值占理财产品资产比例'] = df['MarketValue'] / df['AssetValue_new']
    df['AssetValue_new'].replace(0, '', inplace=True)
    df['该基金市值占理财产品资产比例'].replace(np.inf, '', inplace=True)

    df.rename(columns={'AgentName': '理财公司', 'ChiName': '理财产品', 'InvestmentType': '理财产品一级分类',
                       'SecuCode_new': '基金代码',
                       '基金一级分类': 'wind一级分类', '基金二级分类': 'wind二级分类', 'MarketValue': '理财产品持有基金市值（万元）',
                       'AssetValue_new': '理财产品总资产（万元）', '一年回报': '基金近一年收益', '二年回报': '基金近二年收益',
                       '三年回报': '基金近三年收益', '五年回报': '基金近五年收益'}, inplace=True)

    df['理财产品持有基金市值（万元）'] = df['理财产品持有基金市值（万元）'] / 10000
    df['理财产品持有基金总规模（万元）'] = df['理财产品持有基金总规模（万元）'] / 10000
    all_asset_list = list(df['理财产品总资产（万元）'])
    for i in range(len(all_asset_list)):
        if not isinstance(all_asset_list[i], str) and not np.isnan(all_asset_list[i]):
            all_asset_list[i] = all_asset_list[i] / 10000
    df['理财产品总资产（万元）'] = all_asset_list
    df['基金近一年收益'] = df['基金近一年收益'] / 100
    df['基金近二年收益'] = df['基金近二年收益'] / 100
    df['基金近三年收益'] = df['基金近三年收益'] / 100
    df['基金近五年收益'] = df['基金近五年收益'] / 100

    # pdb.set_trace()

    df = init_add_latest_asset(df, latest_asset_df, zxjt_classify_df)

    # pdb.set_trace()

    final_df = df[['理财公司', '理财产品', '理财产品一级分类', '普益二级分类', '中信建投二级分类', '理财规模数据本周是否更新', '最新产品规模（万元）',
                   '最新规模披露时间', '上次披露规模（万元）', '上次披露时间', '相对上次披露的规模变化', '相对季初的规模变化', '基金简称',
                   '基金代码', '基金公司', 'wind一级分类', 'wind二级分类', '理财产品持有基金市值（万元）', '理财产品持有基金总规模（万元）',
                   '理财产品总资产（万元）', '该基金市值占理财产品资产比例', '基金近一年收益', '基金近二年收益', '基金近三年收益', '基金近五年收益', ]]


    # final_df = df[['理财公司', '理财产品', '基金简称', '基金代码', '基金公司', 'wind一级分类', 'wind二级分类', '理财产品持有基金市值（万元）',
    #                '理财产品持有基金总规模（万元）', '理财产品总资产（万元）', '该基金市值占理财产品资产比例', '基金近一年收益', '基金近二年收益',
    #                '基金近三年收益', '基金近五年收益']]

    final_df.to_excel(output_file)