# -*- coding: utf-8 -*-
"""
    债券分析三步：基于拉取的债券数据做分析
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
    df_input = input.copy()

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
        if bond_perpetual_list[i] == '是':
            bond_perpetual_classify.append("是")
        elif bond_perpetual_list[i] == '否':
            bond_perpetual_classify.append("否")
        else:
            bond_perpetual_classify.append("无标识")
    df_input["债券是否次级债"] = bond_perpetual_classify

    # 统计债券是否次级债情况
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
        if bond_perpetual_list[i] == '是':
            bond_perpetual_classify.append("是")
        elif bond_perpetual_list[i] == '否':
            bond_perpetual_classify.append("否")
        else:
            bond_perpetual_classify.append("无标识")
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
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    return df_res


def cal_average_ratio(input_df, company_num, target_name, ratio_name):
    for bond_type in list(input_df[target_name]):
        input_df.loc[input_df[target_name] == bond_type, target_name + '占公司债券总规模之比均值'] = \
            sum(input_df[input_df[target_name] == bond_type][ratio_name]) / company_num


def cal_inter_bank_receipt(input):
    df_input = input.copy()
    df_input = df_input[df_input['InvestObject'] == 'FCC0000001WP']
    grouped = df_input.groupby(['AgentName']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0], MarketValue_list[i][1]])
    col_name = ['理财子公司', '理财公司同业存单总规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)
    return df_res


def bond_classified_statistics(input):
    df_input = input.copy()

    # 其他统计
    company_bond_sum_df = cal_company_sum(df_input)
    bond_type_df = bond_type_statistics(df_input)
    # bond_grade_df = bond_grade_statistics(df_input)
    bond_urban_investment_df = bond_urban_investment_statistics(df_input)
    bond_subordinated_df = bond_subordinated_statistics(df_input)
    bond_perpetual_df = bond_perpetual_statistics(df_input)

    bond_type_df = bond_type_df.merge(company_bond_sum_df, how='left', on='理财子公司')
    # bond_grade_df = bond_grade_df.merge(company_bond_sum_df, how='left', on='理财子公司')
    bond_urban_investment_df = bond_urban_investment_df.merge(company_bond_sum_df, how='left', on='理财子公司')
    bond_subordinated_df = bond_subordinated_df.merge(company_bond_sum_df, how='left', on='理财子公司')
    bond_perpetual_df = bond_perpetual_df.merge(company_bond_sum_df, how='left', on='理财子公司')

    bond_type_df['债券类型占公司债券总规模之比'] = bond_type_df['债券类型资产规模'] / bond_type_df['理财公司债券总规模']
    # bond_grade_df['债券评级占公司债券总规模之比'] = bond_grade_df['债券评级资产规模'] / bond_grade_df['理财公司债券总规模']
    bond_urban_investment_df['债券是否城投债占公司债券总规模之比'] = bond_urban_investment_df['债券是否城投债资产规模'] / bond_urban_investment_df['理财公司债券总规模']
    bond_subordinated_df['债券是否次级债占公司债券总规模之比'] = bond_subordinated_df['债券是否次级债资产规模'] / bond_subordinated_df['理财公司债券总规模']
    bond_perpetual_df['债券是否永续债占公司债券总规模之比'] = bond_perpetual_df['债券是否永续债资产规模'] / bond_perpetual_df['理财公司债券总规模']

    cal_average_ratio(bond_type_df, len(company_bond_sum_df), "债券类型", "债券类型占公司债券总规模之比")
    # cal_average_ratio(bond_grade_df, len(company_bond_sum_df), "债券评级", "债券评级占公司债券总规模之比")
    cal_average_ratio(bond_urban_investment_df, len(company_bond_sum_df), "债券是否城投债", "债券是否城投债占公司债券总规模之比")
    cal_average_ratio(bond_subordinated_df, len(company_bond_sum_df), "债券是否次级债", "债券是否次级债占公司债券总规模之比")
    cal_average_ratio(bond_perpetual_df, len(company_bond_sum_df), "债券是否永续债", "债券是否永续债占公司债券总规模之比")

    return bond_type_df, bond_urban_investment_df, bond_subordinated_df, bond_perpetual_df
    # return bond_type_df, bond_grade_df, bond_urban_investment_df, bond_subordinated_df, bond_perpetual_df


def get_bond_topK(input, target_feat, topK):
    '''
        各个公司，特定维度提取资产规模前topK
    '''
    df_input = input.copy()

    # 拼接债券名称与代码
    name_list = list(df_input['债券名称'])
    code_list = list(df_input['SecuCode'])
    name_code_list = []
    for i in range(len(name_list)):
        if not isinstance(code_list[i], str) and np.isnan(code_list[i]):
            name_code_list.append(name_list[i])
        else:
            name_code_list.append(name_list[i] + "(" + code_list[i] + ")")

    df_input['债券名称_代码'] = name_code_list
    df_input = df_input[['AgentName', target_feat, '债券名称_代码', 'MarketValue']]
    grouped = df_input.groupby(['AgentName', target_feat, '债券名称_代码']).agg({'MarketValue': sum})
    g = grouped.groupby(level=[0, 1], group_keys=False)['MarketValue'].nlargest(topK)
    res_list = []

    rank_index = 0
    tmp_company_name = ''
    tmp_fund_category = ''
    for line in list(g.items()):
        if line[0][0] != tmp_company_name or line[0][1] != tmp_fund_category:
            tmp_company_name = line[0][0]
            tmp_fund_category = line[0][1]
            rank_index = 0
        rank_index += 1
        res_list.append([line[0][2], line[0][3], line[0][4], line[1], rank_index])
    col_name = ['理财子公司', target_feat, '债券名称_代码', '债券资产规模', '排名']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    # 统计理财子公司
    grouped = df_input.groupby(['AgentName']).agg({'MarketValue': sum})
    MarketValue_list = list(grouped['MarketValue'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0], MarketValue_list[i][1]])
        col_name = ['理财子公司', '理财公司债券总规模']
    df_res2 = pd.DataFrame(data=res_list, columns=col_name)

    df_res = df_res.merge(df_res2, how='left', on='理财子公司')
    df_res['债券占公司债券总规模之比'] = df_res['债券资产规模'] / df_res['理财公司债券总规模']

    return df_res


def df_preprocess(input):
    df_input = input.copy()
    bond_name_list = list(df_input["SecuName"])
    nihuigou_list = ['R001', 'R002', 'R004', 'R007', 'R014', 'R028', 'GC001', 'GC002', 'GC004', 'GC007', 'GC014', 'GC028']
    foreign_currency_list = ['PERP', 'ZZREAL']

    # 识别逆回购
    is_nihuigou = []
    for i in range(len(bond_name_list)):
        if bond_name_list[i] in nihuigou_list:
            is_nihuigou.append('1')
        else:
            is_nihuigou.append('0')
    df_input['是否逆回购'] = is_nihuigou

    # 识别外币理财
    is_foreign_currency = []
    for i in range(len(bond_name_list)):
        if str(bond_name_list[i]).count('/') >= 2 or bond_name_list[i] in foreign_currency_list:
            is_foreign_flag = '1'
        else:
            is_foreign_flag = '0'
            for foreign_currency_word in foreign_currency_list:
                if foreign_currency_word in bond_name_list[i]:
                    is_foreign_flag = '1'
        is_foreign_currency.append(is_foreign_flag)

    df_input['是否外币理财'] = is_foreign_currency
    return df_input[(df_input['是否逆回购'] == '0') & (df_input['是否外币理财'] == '0')]


def get_bond_urban_investment_distribution(input):
    df_input = input.copy()
    df_input = df_input[df_input['债券是否城投债'] == '是']

    df_input = df_input[['AgentName', '主体地区', 'MarketValue']]
    grouped = df_input.groupby(['AgentName', '主体地区']).agg({'MarketValue': sum})
    g = grouped.groupby(level=[0, 1], group_keys=False)['MarketValue'].nlargest(100000)
    res_list = []

    tmp_company_name = ''
    for line in list(g.items()):
        if line[0][0] != tmp_company_name:
            tmp_company_name = line[0][0]
        res_list.append([line[0][0], line[0][1], line[1]])
    col_name = ['理财子公司', '主体地区', '债券资产规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    # 按照MarketValue进行排序
    df_res.sort_values(['理财子公司', '债券资产规模'], ascending=[1, 0], inplace=True)

    return df_res


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='理财子债券打标签.xlsx')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财子重仓债券分析.xlsx')
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file

    writer = pd.ExcelWriter(output_file)
    df = pd.read_excel(input_file)

    # 占比统计
    bond_type_ratio_df, bond_urban_investment_ratio_df, bond_subordinated_ratio_df, bond_perpetual_ratio_df = bond_classified_statistics(df)
    bond_type_ratio_df.to_excel(writer, sheet_name='各债券类型占比')
    bond_urban_investment_ratio_df.to_excel(writer, sheet_name='是否城投债占比')
    bond_subordinated_ratio_df.to_excel(writer, sheet_name='是否次级债占比')
    bond_perpetual_ratio_df.to_excel(writer, sheet_name='是否永续债占比')

    # 前十大统计
    topk = 5
    bond_type_top10_df = get_bond_topK(df, '债券类型', topk)
    bond_urban_investment_top10_df = get_bond_topK(df, '债券是否城投债', topk)
    bond_subordinated_top10_df = get_bond_topK(df, '是否次级债', topk)
    bond_perpetual_top10_df = get_bond_topK(df, '是否永续债', topk)

    bond_type_top10_df.to_excel(writer, sheet_name='各债券类型前十大')
    bond_urban_investment_top10_df.to_excel(writer, sheet_name='是否城投债前十大')
    bond_subordinated_top10_df.to_excel(writer, sheet_name='是否次级债前十大')
    bond_perpetual_top10_df.to_excel(writer, sheet_name='是否永续债前十大')

    # 城投债地区分布
    bond_urban_investment_distribution_df = get_bond_urban_investment_distribution(df)
    bond_urban_investment_distribution_df.to_excel(writer, sheet_name='城投债地区分布')

    writer.save()
    writer.close()


