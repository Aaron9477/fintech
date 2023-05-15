# -*- coding: utf-8 -*-
"""
    基金分析三步：基于拉取的基金数据做分析
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
pd.set_option('max_colwidth',100)

# def cal_company_asset_sum(input_file):
#     df = pd.read_csv(input_file)
#     company_asset_num_sum = df.groupby('CompanyName')['AssetValue'].sum()
#     res_list = []
#     for line in list(company_asset_num_sum.items()):
#         res_list.append([line[0], line[1]])
#     col_name = ['理财子公司', '公司资产总规模']
#     df_res = pd.DataFrame(data=res_list, columns=col_name)
#     return df_res


def code_preprocess(input_list):
    res_list = []
    for x in input_list:
        x = str(x)
        if len(x) > 6:
            x = x[:6]
        x = x.split('.')[0].split(' ')[0]
        res_list.append(x + '.OF')
    return res_list


def bond_grade_statistics(input):
    df_input = input.copy()

    bond_grade_list = list(df_input["债券评级"])
    bond_grade_classify = []
    for i in range(len(bond_grade_list)):
        # 部分国债和证金债没有编码或者在万德上查不到
        if bond_grade_list[i] == 'AAA' or bond_grade_list[i] == 'A-1':
            bond_grade_classify.append("AAA")
        elif pd.isna(bond_grade_list[i]):
            bond_grade_classify.append("未披露")
        else:
            bond_grade_classify.append("低于AAA")
    df_input["债券评级"] = bond_grade_classify

    # 统计债券评级情况
    grouped = df_input.groupby(['AgentName', '债券评级']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0][0], MarketValue_list[i][0][1], MarketValue_list[i][1]])
    col_name = ['理财子公司', '债券评级', '债券评级资产规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)
    return df_res


def bond_type_statistics(input):
    # df_interest_rate = input.loc[(input["wind一级分类"] == "国债") | (input["wind一级分类"] == "证金债") | (input["wind一级分类"] == "金融债")
    #                              | (input["wind一级分类"] == "央行票据") | (input["wind一级分类"] == "地方政府债")
    #                              | (input["wind一级分类"] == "同业存单") | (input["wind一级分类"] == "政府支持机构债券")]
    # df_credit = input.loc[(input["wind一级分类"] == "短期融资券") | (input["wind一级分类"] == "中期票据") | (input["wind一级分类"] == "公司债")
    #                              | (input["wind一级分类"] == "企业债") | (input["wind一级分类"] == "国际机构债") | (input["wind一级分类"] == "项目收益票据")
    #                              | (input["wind一级分类"] == "资产支持证券") | (input["wind一级分类"] == "定向工具")]

    df_input = input.copy()

    interest_rate_bond = ["国债", "证金债", "金融债", "央行票据", "地方政府债", "同业存单", "政府支持机构债券"]
    credit_bond = ["短期融资券", "中期票据", "公司债", "企业债", "国际机构债", "项目收益票据", "资产支持证券", "定向工具"]
    partial_bond = ["可交换债", "可转债"]

    bond_name_list = list(df_input["SecuName"])
    wind_type_list = list(df_input["wind一级分类"])
    bond_type = []
    for i in range(len(bond_name_list)):
        # 部分国债 证金债 国债正逆回购没有编码或者在万德上查不到
        if "国债" in bond_name_list[i] or "证金" in bond_name_list[i] or "GC0" in bond_name_list[i] or wind_type_list[i] in interest_rate_bond:
            bond_type.append("利率债")
        elif wind_type_list[i] in credit_bond:
            bond_type.append("信用债")
        elif wind_type_list[i] in partial_bond:
            bond_type.append("偏股型债")
        else:
            bond_type.append("未披露")
    df_input["债券类型"] = bond_type

    # 统计债券分类情况
    grouped = df_input.groupby(['AgentName', '债券类型']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0][0], MarketValue_list[i][0][1], MarketValue_list[i][1]])
    col_name = ['理财子公司', '债券类型', '债券类型资产规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    return df_res


def bond_urban_investment_statistics(input):
    df_input = input.copy()

    bond_urban_investment_list = list(df_input["是否城投债"])
    bond_urban_investment_wind_list = list(df_input["是否城投债(wind)"])
    bond_urban_investment_yy_list = list(df_input["是否城投债(YY)"])
    bond_urban_investment_classify = []
    for i in range(len(bond_urban_investment_list)):
        # 部分国债和证金债没有编码或者在万德上查不到
        if bond_urban_investment_list[i] == '是' or bond_urban_investment_wind_list[i] == '是' or bond_urban_investment_yy_list[i] == '是':
            bond_urban_investment_classify.append("是")
        else:
            bond_urban_investment_classify.append("否")
    df_input["债券是否城投债"] = bond_urban_investment_classify

    # 统计债券评级情况
    grouped = df_input.groupby(['AgentName', '债券是否城投债']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0][0], MarketValue_list[i][0][1], MarketValue_list[i][1]])
    col_name = ['理财子公司', '债券是否城投债', '债券是否城投债资产规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)
    return df_res


def bond_subordinated_statistics(input):
    df_input = input.copy()

    bond_perpetual_list = list(df_input["是否次级债"])
    bond_perpetual_classify = []
    for i in range(len(bond_perpetual_list)):
        # 部分国债和证金债没有编码或者在万德上查不到
        if bond_perpetual_list[i] == '是':
            bond_perpetual_classify.append("是")
        else:
            bond_perpetual_classify.append("否")
    df_input["债券是否次级债"] = bond_perpetual_classify

    # 统计债券是否永续债情况
    grouped = df_input.groupby(['AgentName', '债券是否次级债']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0][0], MarketValue_list[i][0][1], MarketValue_list[i][1]])
    col_name = ['理财子公司', '债券是否次级债', '债券是否次级债资产规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)
    return df_res


def bond_perpetual_statistics(input):
    df_input = input.copy()

    bond_perpetual_list = list(df_input["是否永续债"])
    bond_perpetual_classify = []
    for i in range(len(bond_perpetual_list)):
        # 部分国债和证金债没有编码或者在万德上查不到
        if bond_perpetual_list[i] == '是':
            bond_perpetual_classify.append("是")
        else:
            bond_perpetual_classify.append("否")
    df_input["债券是否永续债"] = bond_perpetual_classify

    # 统计债券是否永续债情况
    grouped = df_input.groupby(['AgentName', '债券是否永续债']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0][0], MarketValue_list[i][0][1], MarketValue_list[i][1]])
    col_name = ['理财子公司', '债券是否永续债', '债券是否永续债资产规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)
    return df_res


def cal_company_sum(input):
    # 统计理财子公司
    df_input = input.copy()
    grouped = df_input.groupby(['AgentName']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0], MarketValue_list[i][1]])
    col_name = ['理财子公司', '理财公司债券总规模']
    df_res2 = pd.DataFrame(data=res_list, columns=col_name)
    return df_res2


def cal_average_ratio(input_df, company_num, target_name, ratio_name):
    for bond_type in list(input_df[target_name]):
        input_df.loc[input_df[target_name] == bond_type, target_name + '占公司债券总规模之比均值'] = \
            sum(input_df[input_df[target_name] == bond_type][ratio_name]) / company_num


def bond_classified_statistics(input):
    df_input = input.copy()

    company_bond_sum_df = cal_company_sum(df_input)
    bond_type_df = bond_type_statistics(df_input)
    bond_grade_df = bond_grade_statistics(df_input)
    bond_urban_investment_df = bond_urban_investment_statistics(df_input)
    bond_subordinated_df = bond_subordinated_statistics(df_input)
    bond_perpetual_df = bond_perpetual_statistics(df_input)

    bond_type_df = bond_type_df.merge(company_bond_sum_df, how='left', on='理财子公司')
    bond_grade_df = bond_grade_df.merge(company_bond_sum_df, how='left', on='理财子公司')
    bond_urban_investment_df = bond_urban_investment_df.merge(company_bond_sum_df, how='left', on='理财子公司')
    bond_subordinated_df = bond_subordinated_df.merge(company_bond_sum_df, how='left', on='理财子公司')
    bond_perpetual_df = bond_perpetual_df.merge(company_bond_sum_df, how='left', on='理财子公司')

    bond_type_df['债券类型占公司债券总规模之比'] = bond_type_df['债券类型资产规模'] / bond_type_df['理财公司债券总规模']
    bond_grade_df['债券评级占公司债券总规模之比'] = bond_grade_df['债券评级资产规模'] / bond_grade_df['理财公司债券总规模']
    bond_urban_investment_df['债券是否城投债占公司债券总规模之比'] = bond_urban_investment_df['债券是否城投债资产规模'] / bond_urban_investment_df['理财公司债券总规模']
    bond_subordinated_df['债券是否次级债占公司债券总规模之比'] = bond_subordinated_df['债券是否次级债资产规模'] / bond_subordinated_df['理财公司债券总规模']
    bond_perpetual_df['债券是否永续债占公司债券总规模之比'] = bond_perpetual_df['债券是否永续债资产规模'] / bond_perpetual_df['理财公司债券总规模']

    cal_average_ratio(bond_type_df, len(company_bond_sum_df), "债券类型", "债券类型占公司债券总规模之比")
    cal_average_ratio(bond_grade_df, len(company_bond_sum_df), "债券评级", "债券评级占公司债券总规模之比")
    cal_average_ratio(bond_urban_investment_df, len(company_bond_sum_df), "债券是否城投债", "债券是否城投债占公司债券总规模之比")
    cal_average_ratio(bond_subordinated_df, len(company_bond_sum_df), "债券是否次级债", "债券是否次级债占公司债券总规模之比")
    cal_average_ratio(bond_perpetual_df, len(company_bond_sum_df), "债券是否永续债", "债券是否永续债占公司债券总规模之比")

    return bond_type_df, bond_grade_df, bond_urban_investment_df, bond_subordinated_df, bond_perpetual_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='债券信息.xlsx')
    parser.add_argument('--all_data_file', type=str, help='input_file', default='../data/bank_wealth_product_12_22.csv')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财子债券分析.xlsx')
    args = parser.parse_args()
    input_file = args.input_file
    all_data_file = args.all_data_file
    output_file = args.output_file

    writer = pd.ExcelWriter(output_file)
    df = pd.read_excel(input_file)

    # df["基金代码"] = code_preprocess(df['SecuCode'].values)

    # # 公司披露基金总资产计算
    # company_asset_sum_df = cal_company_asset_sum(all_data_file)

    # 各类型基金占公司占比
    bond_type_df, bond_grade_df, bond_urban_investment_df, bond_subordinated_df, bond_perpetual_df = bond_classified_statistics(df)

    bond_type_df.to_excel(writer, sheet_name='债券类型')
    bond_grade_df.to_excel(writer, sheet_name='债券评级')
    bond_urban_investment_df.to_excel(writer, sheet_name='是否城投债')
    bond_subordinated_df.to_excel(writer, sheet_name='是否次级债')
    bond_perpetual_df.to_excel(writer, sheet_name='是否永续债')

    writer.save()
    writer.close()

    # exit()
    #
    # company_fund_asset_sum = cal_company_fund_asset_sum(df)
    # company_fund_asset_sum_add_company_asset = company_fund_asset_sum.merge(company_asset_sum_df, how='left', on='理财子公司')
    # company_fund_asset_sum_add_company_asset['基金资产占比'] = company_fund_asset_sum_add_company_asset['基金资产规模'] / company_fund_asset_sum_add_company_asset['公司资产总规模']
    # company_fund_asset_sum_add_company_asset.index = company_fund_asset_sum_add_company_asset.index + 1
    # company_fund_asset_sum_add_company_asset.to_excel(writer, sheet_name='理财子各基金类型占比')
    #
    # # 各理财子前十大基金
    # company_fund_rank = cal_company_fund_asset_top(df)
    # company_fund_rank_add_company_asset = company_fund_rank.merge(company_asset_sum_df, how='left', on='理财子公司')
    # company_fund_rank_add_company_asset['基金资产占比'] = company_fund_rank_add_company_asset['基金资产规模'] / company_fund_rank_add_company_asset['公司资产总规模']
    #
    # df_tmp = df.drop_duplicates(subset='基金代码')
    # company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.merge(df_tmp[["基金代码", "基金二级分类"]], how="left", on="基金代码")
    # # 获得基金评分与排名
    # company_fund_rank_add_company_asset['无后缀代码'] = [int(x.split('.')[0])  for x in list(company_fund_rank_add_company_asset['基金代码'])]
    # company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.merge(score_df[['无后缀代码', 'TOTAL_SCORE_RANK_SHORT_TERM', '二级分类下量化打分排名']], how="left", on="无后缀代码")
    # company_fund_rank_add_company_asset = company_fund_rank_add_company_asset.drop(labels='无后缀代码', axis=1)
    # company_fund_rank_add_company_asset.rename(columns={'TOTAL_SCORE_RANK_SHORT_TERM': '二级分类下量化打分'}, inplace=True)
    # company_fund_rank_add_company_asset.index = company_fund_rank_add_company_asset.index + 1
    # company_fund_rank_add_company_asset['基金名称'] = company_fund_rank_add_company_asset['基金名称'] + "(" + company_fund_rank_add_company_asset['基金代码'] + ")"
    #
    # company_fund_rank_add_company_asset['二级分类下量化打分'].fillna('-', inplace=True)
    # company_fund_rank_add_company_asset['二级分类下量化打分排名'].fillna('-', inplace=True)
    #
    # company_fund_rank_add_company_asset.to_excel(writer, sheet_name='理财子前十大基金')
    #
    # writer.save()
    # writer.close()

