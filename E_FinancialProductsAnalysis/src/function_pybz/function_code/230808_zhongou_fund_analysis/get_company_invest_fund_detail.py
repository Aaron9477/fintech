# -*- coding: utf-8 -*-
"""
    客户服务分析：统计理财子购买基金情况
"""

import pandas as pd
import numpy as np
import argparse
import datetime


#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

def cal_company_asset_sum(input_df):
    company_asset_num_sum = input_df.groupby('CompanyName')['AssetValue'].sum()
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
    topK = 1000    # 取top多少

    grouped = df_input.groupby(['AgentName', '基金简称', '基金一级分类', '一年收益率', '基金代码', '基金公司']).agg({'MarketValue': sum})
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
        res_list.append([line[0][2], line[0][3], line[0][4], line[0][5], line[1], rank_index, line[0][6], line[0][7]])
    col_name = ['理财子公司', '基金名称', '基金类型', '一年收益率', '基金资产规模', '排名', '基金代码', '基金公司']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    # 统计理财子公司
    grouped = df_input.groupby(['AgentName']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0], MarketValue_list[i][1]])
        col_name = ['理财子公司', '理财公司基金总规模']
    df_res2 = pd.DataFrame(data=res_list, columns=col_name)

    # 统计基金各理财子购买之和排名
    grouped = df_input.groupby(['基金简称']).agg({'MarketValue': sum, 'AgentName': 'nunique', 'FinProCode': 'count'})
    MarketValue_list = list(grouped['MarketValue'].items())
    AgentName_nunique_list = list(grouped['AgentName'].items())
    FinProCode_count_list = list(grouped['FinProCode'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0], MarketValue_list[i][1], AgentName_nunique_list[i][1], FinProCode_count_list[i][1]])
        col_name = ['基金名称', '理财公司投资基金总规模', '理财公司投资该基金总数', '理财产品投资该基金总数']
    df_res3 = pd.DataFrame(data=res_list, columns=col_name)

    df_res = df_res.merge(df_res2, how='left', on='理财子公司')
    df_res = df_res.merge(df_res3, how='left', on='基金名称')
    df_res['基金占公司基金总规模之比'] = df_res['基金资产规模'] / df_res['理财公司基金总规模']

    fund_code = df_res.pop('基金代码')
    df_res.insert(loc=df_res.shape[1]-1, column='基金代码', value=fund_code, allow_duplicates=False)

    return df_res


# def rank_fund_with_score(input):
#     df_input = input.copy()
#     df_input = df_input.drop_duplicates(subset='基金代码')
#     # grouped = df_input.groupby(['基金二级分类'])['TOTAL_SCORE_RANK_SHORT_TERM'].rank(method='dense', na_option='keep', pct=True)
#     # grouped = df_input['TOTAL_SCORE_RANK_SHORT_TERM'].rank(method='dense', na_option='keep', pct=True)
#     df_input['rank_index'] = df_input.groupby(['基金二级分类'])['TOTAL_SCORE_RANK_SHORT_TERM'].rank(method='dense', na_option='keep', pct=False)
#     return df_input
#
#
# def get_sum_second_category(input):
#     df_input = input.copy()
#     df_input = df_input.drop_duplicates(subset='基金代码')
#     df_input["count"] = 1
#     df_input = df_input.groupby("基金二级分类")["count"].sum()
#     return df_input


def code_preprocess(input_list):
    res_list = []
    for x in input_list:
        x = str(x)
        if len(x) > 6:
            x = x[:6]
        x = x.split('.')[0].split(' ')[0]
        res_list.append(x + '.OF')
    return res_list


def get_trading_day(statistics_date):
    if statistics_date == '2022-09-30':
        trading_day = '2022-09-30'
    elif statistics_date == '2022-12-31':
        # 2022-12-31 不是交易日，所以使用2022-12-30去wind拉取数据
        trading_day = '2022-12-30'
    elif statistics_date == '2023-03-31':
        trading_day = '2023-03-31'
    elif statistics_date == '2023-06-30':
        trading_day = '2023-06-30'
    else:
        raise ValueError
    return trading_day


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-03-31')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-06-30')
    parser.add_argument('--score_file', type=str, help='score_file', default='全部基金量化打分排名.xlsx')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财公司重仓基金明细表.xlsx')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    score_file = args.score_file
    output_file = args.output_file.split('.')[0] + '_' + statistics_date + '.xlsx'
    trading_day = get_trading_day(statistics_date)

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

    writer = pd.ExcelWriter(output_file)
    df = pd.read_excel(input_file)
    score_df = pd.read_excel(score_file)

    df["基金代码"] = code_preprocess(df['SecuCode'].values)

    all_data_df = pd.read_csv(all_data_file)
    company_list = list(all_data_df['CompanyName'])
    new_company_list = []
    for i in range(len(company_list)):
        if company_list[i] != '汇华理财有限公司':
            new_company_list.append(company_list[i][:-6])
        else:
            new_company_list.append('汇华理财')
    all_data_df['CompanyName'] = new_company_list

    # 公司披露基金总资产计算
    company_asset_sum_df = cal_company_asset_sum(all_data_df)

    # 各类型基金占公司占比
    company_fund_asset_sum = cal_company_fund_asset_sum(df)
    company_fund_asset_sum_add_company_asset = company_fund_asset_sum.merge(company_asset_sum_df, how='left', on='理财子公司')
    company_fund_asset_sum_add_company_asset['基金资产占比'] = company_fund_asset_sum_add_company_asset['基金资产规模'] / company_fund_asset_sum_add_company_asset['公司资产总规模']
    company_fund_asset_sum_add_company_asset.index = company_fund_asset_sum_add_company_asset.index + 1
    company_fund_asset_sum_add_company_asset.to_excel(writer, sheet_name='理财子各基金类型占比')

    # 各理财子前十大基金
    company_fund_rank = cal_company_fund_asset_top(df)
    company_fund_rank_add_company_asset = company_fund_rank.merge(company_asset_sum_df, how='left', on='理财子公司')
    company_fund_rank_add_company_asset['基金资产占比'] = company_fund_rank_add_company_asset['基金资产规模'] / company_fund_rank_add_company_asset['公司资产总规模']

    df_tmp = df.drop_duplicates(subset='基金代码')
    company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.merge(df_tmp[["基金代码", "基金一级分类", "基金二级分类"]], how="left", on="基金代码")
    # 获得基金评分与排名
    company_fund_rank_add_company_asset['无后缀代码'] = [int(x.split('.')[0]) for x in list(company_fund_rank_add_company_asset['基金代码'])]
    company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.merge(score_df[['无后缀代码', 'TOTAL_SCORE_RANK_SHORT_TERM', '二级分类下量化打分排名']], how="left", on="无后缀代码")
    company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.drop(labels='无后缀代码', axis=1)
    company_fund_rank_add_company_asset.rename(columns={'TOTAL_SCORE_RANK_SHORT_TERM': '二级分类下量化打分'}, inplace=True)
    company_fund_rank_add_company_asset.index = company_fund_rank_add_company_asset.index + 1
    # company_fund_rank_add_company_asset['基金名称'] = company_fund_rank_add_company_asset['基金名称'] + "(" + company_fund_rank_add_company_asset['基金代码'] + ")"

    company_fund_rank_add_company_asset['二级分类下量化打分'].fillna('-', inplace=True)
    company_fund_rank_add_company_asset['二级分类下量化打分排名'].fillna('-', inplace=True)

    company_fund_rank_add_company_asset.rename(columns={'基金一级分类': 'wind一级分类', '基金二级分类': 'wind二级分类', '理财子公司': '理财公司',
                                                        '基金资产规模': '持有基金市值（万元）', '理财公司基金总规模': '理财公司投资基金总规模（万元）',
                                                        '基金占公司基金总规模之比': '该基金在理财子全部持仓基金中占比', '基金资产占比': '基金占理财公司总资产比例', '理财公司投资基金总规模': '全市场理财公司投资该基金总规模（万元）',
                                                        '理财公司投资该基金总数': '全市场投资该基金理财公司总数', '理财产品投资该基金总数': '全市场投资该基金理财产品总数',
                                                        '一年收益率': '基金近一年收益率(截至220930)', '二级分类下量化打分': '基金评估中心二级分类下量化打分',
                                                        '二级分类下量化打分排名': '二级分类下量化打分排名'}, inplace=True)

    company_fund_rank_add_company_asset['持有基金市值（万元）'] = company_fund_rank_add_company_asset['持有基金市值（万元）'] / 10000
    company_fund_rank_add_company_asset['理财公司投资基金总规模（万元）'] = company_fund_rank_add_company_asset['理财公司投资基金总规模（万元）'] / 10000
    company_fund_rank_add_company_asset['全市场理财公司投资该基金总规模（万元）'] = company_fund_rank_add_company_asset['全市场理财公司投资该基金总规模（万元）'] / 10000


    final_df = company_fund_rank_add_company_asset[['基金名称', '基金代码', 'wind一级分类', 'wind二级分类', '基金公司', '理财公司', '持有基金市值（万元）', '理财公司投资基金总规模（万元）',
                   '该基金在理财子全部持仓基金中占比', '基金占理财公司总资产比例', '全市场理财公司投资该基金总规模（万元）', '全市场投资该基金理财公司总数', '全市场投资该基金理财产品总数',
                   '基金近一年收益率(截至220930)', '基金评估中心二级分类下量化打分', '二级分类下量化打分排名']]

    final_df.to_excel(writer, sheet_name='理财子前十大基金')

    writer.save()
    writer.close()


    # grouped = df.groupby(['AgentName', '基金一级分类'])
    # res_sum = grouped['MarketValue'].sum()
    #
    # res_list = []
    # for line in list(res_sum.items()):
    #     res_list.append([line[0][0], line[0][1], line[1]])
    # col_name = ['理财子公司', '基金类型', '资产数量']
    #
    # df_res = pd.DataFrame(data=res_list, columns=col_name)
    #
    # df_res.to_excel('test.xlsx')

    # for group_name in list(grouped.groups.keys()):
    #     print(group_name)
    #     company_df = grouped.get_group(group_name)
    #     print(company_df)
