# -*- coding: utf-8 -*-
"""
    基金分析三步：基于拉取的基金数据做分析
"""

import pandas as pd
import numpy as np
import argparse
import datetime

from func import get_product_exist
from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_files


#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)


def cal_company_asset_sum(input_file, statistics_date):
    all_data_df = pd.read_csv(input_file)

    # 筛选存续期产品
    all_data_df = get_product_exist(all_data_df, statistics_date)

    # 筛选子产品 all_data_df
    def get_main_product_ind(data_set_RegistrationCode):
        ProductTypes = data_set_RegistrationCode['ProductType']
        tags = ['母产品', '产品', '子产品']
        for tag in tags:
            if tag in ProductTypes.values:
                return ProductTypes[ProductTypes == tag].index[0]

    RegistrationCodes = list(set(all_data_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = all_data_df[all_data_df['RegistrationCode'] == RegistrationCode]
        data_set_RegistrationCode = data_set_RegistrationCode.sort_values(by=['AssetValue'], ascending=False)
        if len(data_set_RegistrationCode.dropna(subset=['AssetValue']).index) > 0:
            data_set_RegistrationCode = data_set_RegistrationCode.dropna(subset=['AssetValue'])
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    output_df = all_data_df[all_data_df.index.isin(RegistrationCode_mainind)]

    # 公司名称改为全称
    company_list = list(output_df['CompanyName'])
    new_company_list = []
    for i in range(len(company_list)):
        if company_list[i] != '汇华理财有限公司':
            new_company_list.append(company_list[i][:-6])
        else:
            new_company_list.append('汇华理财')
    output_df['CompanyName'] = new_company_list

    company_asset_num_sum = output_df.groupby('CompanyName')['AssetValue'].sum()
    res_list = []
    for line in list(company_asset_num_sum.items()):
        res_list.append([line[0], line[1]])
    col_name = ['理财子公司', '公司资产总规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)
    return df_res


def cal_company_fund_asset_sum(input):
    df_input = input.copy()
    df_input['近一年收益总量'] = df_input['一年收益率'] * df_input['MarketValue']

    # 统计基金一级分类情况
    grouped = df_input.groupby(['AgentName', '基金一级分类']).agg({'MarketValue': sum, '近一年收益总量': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    profit_list = list(grouped['近一年收益总量'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0][0], MarketValue_list[i][0][1], MarketValue_list[i][1], profit_list[i][1]])

    # 统计理财子全部收益
    grouped = df_input.groupby(['AgentName']).agg({'MarketValue': sum, '近一年收益总量': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    profit_list = list(grouped['近一年收益总量'].items())
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0], '全部', MarketValue_list[i][1], profit_list[i][1]])
    col_name = ['理财子公司', '基金类型', '基金资产规模', '近一年收益总量']
    df_res = pd.DataFrame(data=res_list, columns=col_name)
    df_res['近一年收益率'] = df_res['近一年收益总量'] / df_res['基金资产规模']

    # 统计理财子公司
    grouped = df_input.groupby(['AgentName']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0], MarketValue_list[i][1]])
    col_name = ['理财子公司', '理财公司基金总规模']
    df_res2 = pd.DataFrame(data=res_list, columns=col_name)

    df_res = df_res.merge(df_res2, how='left', on='理财子公司')
    df_res['基金类型占公司基金总规模之比'] = df_res['基金资产规模'] / df_res['理财公司基金总规模']

    return df_res


def cal_company_fund_asset_top(input):
    df_input = input.copy()
    topK = 5    # 取top多少

    grouped = df_input.groupby(['AgentName', '基金简称', '基金一级分类', '一年收益率', '基金代码']).agg({'MarketValue': sum})
    g = grouped.groupby(level=[0, 2], group_keys=False)['MarketValue'].nlargest(topK)
    res_list = []

    rank_index = 0
    tmp_company_name = ''
    tmp_fund_category = ''
    for line in list(g.items()):
        if line[0][2] != tmp_company_name or line[0][4] != tmp_fund_category:
            tmp_company_name = line[0][2]
            tmp_fund_category = line[0][4]
            rank_index = 0
        rank_index += 1
        res_list.append([line[0][2], line[0][3], line[0][4], line[0][5], line[1], rank_index, line[0][6]])
    col_name = ['理财子公司', '基金名称', '基金类型', '一年收益率', '基金资产规模', '排名', '基金代码']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    # 统计理财子公司
    grouped = df_input.groupby(['AgentName']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0], MarketValue_list[i][1]])
        col_name = ['理财子公司', '理财公司基金总规模']
    df_res2 = pd.DataFrame(data=res_list, columns=col_name)

    df_res = df_res.merge(df_res2, how='left', on='理财子公司')
    df_res['基金占公司基金总规模之比'] = df_res['基金资产规模'] / df_res['理财公司基金总规模']

    fund_code = df_res.pop('基金代码')
    df_res.insert(loc=df_res.shape[1]-1, column='基金代码', value=fund_code, allow_duplicates=False)

    return df_res


def code_preprocess(input_list):
    res_list = []
    for x in input_list:
        x = str(x)
        if len(x) > 6:
            x = x[:6]
        x = x.split('.')[0].split(' ')[0]
        res_list.append(x + '.OF')
    return res_list


def get_wind_classification(row):
    if row["type_code"].startswith("csc_mutual_fund_type"):
        return False
    else:
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--score_file', type=str, help='input_file', default='../../data_pybz/公募基金3年期指标排名20230426.csv')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财子重仓基金分析.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    args = parser.parse_args()

    score_file = args.score_file
    output_file = args.output_file
    statistics_date = args.statistics_date

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    input_file = '基金信息_{}.xlsx'.format(statistics_date)

    writer = pd.ExcelWriter(output_file)
    df = pd.read_excel(input_file)
    score_df = pd.read_csv(score_file)
    # 只保留wind分类的打分排名
    score_df = score_df[(score_df.apply(lambda x: get_wind_classification(x), axis=1))]

    df["基金代码"] = code_preprocess(df['SecuCode'].values)

    # 公司披露基金总资产计算
    company_asset_sum_df = cal_company_asset_sum(all_data_file, statistics_date)

    # 各类型基金占公司占比
    company_fund_asset_sum = cal_company_fund_asset_sum(df)
    company_fund_asset_sum_add_company_asset = company_fund_asset_sum.merge(company_asset_sum_df, how='left', on='理财子公司')
    company_fund_asset_sum_add_company_asset['基金资产占比'] = company_fund_asset_sum_add_company_asset['基金资产规模'] / company_fund_asset_sum_add_company_asset['公司资产总规模']
    # 根据溪恒使用的要求，对index做+1操作
    company_fund_asset_sum_add_company_asset.index = company_fund_asset_sum_add_company_asset.index + 1
    company_fund_asset_sum_add_company_asset.to_excel(writer, sheet_name='理财子各基金类型占比')

    # 各理财子前五大基金
    company_fund_rank = cal_company_fund_asset_top(df)
    company_fund_rank_add_company_asset = company_fund_rank.merge(company_asset_sum_df, how='left', on='理财子公司')
    company_fund_rank_add_company_asset['基金资产占比'] = company_fund_rank_add_company_asset['基金资产规模'] / company_fund_rank_add_company_asset['公司资产总规模']

    df_tmp = df.drop_duplicates(subset='基金代码')
    company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.merge(df_tmp[["基金代码", "基金二级分类"]], how="left", on="基金代码")
    # 获得基金评分与排名
    score_df['二级分类下量化打分'] = 0   # 这列没有用
    score_df['二级分类下量化打分排名'] = score_df['annual_return_rank'].map(lambda x: x.replace("|", "/"))
    company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.merge(score_df[['fund_code', '二级分类下量化打分', '二级分类下量化打分排名']], how="left", left_on="基金代码", right_on='fund_code')
    company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.drop(labels='fund_code', axis=1)
    # 根据溪恒使用的要求，对index做+1操作
    company_fund_rank_add_company_asset.index = company_fund_rank_add_company_asset.index + 1
    company_fund_rank_add_company_asset['基金名称'] = company_fund_rank_add_company_asset['基金名称'] + "(" + company_fund_rank_add_company_asset['基金代码'] + ")"

    company_fund_rank_add_company_asset['二级分类下量化打分排名'].fillna('-', inplace=True)

    company_fund_rank_add_company_asset.to_excel(writer, sheet_name='理财子前十大基金')

    writer.save()
    writer.close()
