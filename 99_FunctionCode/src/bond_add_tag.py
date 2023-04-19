# -*- coding: utf-8 -*-
"""
    债券分析二步：拉取的债券数据过滤回购与外币资产，补充同业存单数据，并对债券打标签
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

    # 分类情况如下。特殊类型:同业存单、金融债
    # 1、同业存单单独打标签;2、金融债中政策银行债算利率债，其他算信用债
    interest_rate_bond = ["国债", "证金债", "央行票据", "地方政府债", "政府支持机构债"]
    credit_bond = ["短期融资券", "中期票据", "公司债", "企业债", "国际机构债", "项目收益票据", "资产支持证券", "定向工具"]
    partial_bond = ["可交换债", "可转债"]

    bond_name_list = list(df_input["债券简称"])
    wind_type_first_list = list(df_input["wind一级分类"])
    wind_type_second_list = list(df_input["wind二级分类"])
    bond_grade_list = list(df_input["债券评级"])

    bond_type = []
    for i in range(len(bond_name_list)):
        # 部分国债 证金债 没有编码或者在万德上查不到，直接标为利率债
        # 金融债中的政策银行债为利率债
        if wind_type_first_list[i] in interest_rate_bond or "国债" in bond_name_list[i] or "证金" in bond_name_list[i] or \
                (wind_type_first_list[i] == '金融债' and wind_type_second_list[i] == '政策银行债'):
            bond_type.append("利率债")
        elif wind_type_first_list[i] in credit_bond or (wind_type_first_list[i] == '金融债' and wind_type_second_list[i] != '政策银行债'):
            # 部分国债和证金债没有编码或者在万德上查不到
            if bond_grade_list[i] == 'AAA' or bond_grade_list[i] == 'A-1':
                bond_type.append("AAA信用债")
            elif bond_grade_list[i] == 'AA+' or bond_grade_list[i] == 'A-2':
                bond_type.append("AA+信用债")
            elif pd.isna(bond_grade_list[i]):
                bond_type.append("无评级信用债")
            else:
                bond_type.append("AA+以下信用债")
        elif wind_type_first_list[i] in partial_bond:
            bond_type.append("偏股型债")
        elif wind_type_first_list[i] == '同业存单':
            bond_type.append("同业存单")
        else:
            bond_type.append("无评级信用债")
    df_input["债券类型"] = bond_type

    return df_input


def df_preprocess(input):
    df_input = input.copy()
    bond_name_list = list(df_input["债券简称"])
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

    df_output = df_input[(df_input['是否逆回购'] == '0') & (df_input['是否外币理财'] == '0')]
    del df_output['是否逆回购'], df_output['是否外币理财']

    return df_output


def makeup_bond_grade(input):
    input_df = input.copy()
    bond_grade_list = input_df['债券评级'].values
    publisher_grade_list = input_df['发行人评级'].values
    for i in range(len(bond_grade_list)):
        if not isinstance(bond_grade_list[i], str) and np.isnan(bond_grade_list[i]):
            bond_grade_list[i] = publisher_grade_list[i]
    input_df['债券评级'] = bond_grade_list
    return input_df


def get_bond_urban_investment_tag(input):
    df_input = input.copy()

    bond_urban_investment_list = list(df_input["是否城投债"])
    bond_urban_investment_wind_list = list(df_input["是否城投债(wind)"])
    bond_urban_investment_yy_list = list(df_input["是否城投债(YY)"])
    bond_urban_investment_classify = []
    for i in range(len(bond_urban_investment_list)):
        # 只要有一个标签标为城投债，则认为是城投债
        if bond_urban_investment_list[i] == '是' or bond_urban_investment_wind_list[i] == '是' or bond_urban_investment_yy_list[i] == '是':
            bond_urban_investment_classify.append("是")
        elif bond_urban_investment_list[i] == '否' or bond_urban_investment_wind_list[i] == '否' or bond_urban_investment_yy_list[i] == '否':
            bond_urban_investment_classify.append("否")
        else:
            bond_urban_investment_classify.append("无标识")
    df_input["债券是否城投债"] = bond_urban_investment_classify

    # 删除原始标记
    del df_input["是否城投债"], df_input["是否城投债(wind)"], df_input["是否城投债(YY)"]

    return df_input


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='债券信息_12月.xlsx')
    parser.add_argument('--output_file', type=str, help='output_file', default='统计债券占比_12月.xlsx')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file

    writer = pd.ExcelWriter(output_file)
    df = pd.read_excel(input_file)

    # 打城投债标签
    df = get_bond_urban_investment_tag(df)

    # 使用发行人主体评级补充债券评级缺失的数据
    df = makeup_bond_grade(df)
    # 统计利率债、AA+以上信用债、AA+以下信用债
    bond_type_df = bond_type_statistics(df)

    bond_type_df.to_excel(writer)

    writer.save()
    writer.close()

    output_df = pd.DataFrame(columns=['类别', '占比'])

    output_list = []

    bond_type_df['券面总额(元)'] = bond_type_df['持仓净值(元)']

    bond_sum = bond_type_df['券面总额(元)'].sum()

    bond_type_df['久期乘积'] = bond_type_df['券面总额(元)'] * bond_type_df['收盘价修正久期']
    jiaquanjiuqi = bond_type_df['久期乘积'].sum() / bond_sum
    print("加权久期为: {}".format(jiaquanjiuqi))

    bond_ratio = bond_type_df[bond_type_df['债券类型'] == '利率债']['券面总额(元)'].sum() / bond_sum
    bond_AAA = bond_type_df[bond_type_df['债券类型'] == 'AAA信用债']['券面总额(元)'].sum() / bond_sum
    bond_AAjia = bond_type_df[bond_type_df['债券类型'] == 'AA+信用债']['券面总额(元)'].sum() / bond_sum
    bond_AA_blow = bond_type_df[bond_type_df['债券类型'] == 'AA+以下信用债']['券面总额(元)'].sum() / bond_sum
    bond_none = bond_type_df[bond_type_df['债券类型'] == '无评级信用债']['券面总额(元)'].sum() / bond_sum
    bond_tongye = bond_type_df[bond_type_df['债券类型'] == '同业存单']['券面总额(元)'].sum() / bond_sum
    bond_equ = bond_type_df[bond_type_df['债券类型'] == '偏股型债']['券面总额(元)'].sum() / bond_sum

    output_list.append(['利率债', bond_ratio])
    output_list.append(['AAA信用债', bond_AAA])
    output_list.append(['AA+信用债', bond_AAjia])
    output_list.append(['AA+以下信用债', bond_AA_blow])
    output_list.append(['无评级信用债', bond_none])
    output_list.append(['同业存单', bond_tongye])
    output_list.append(['偏股型债', bond_equ])

    bond_ciji = bond_type_df[bond_type_df['是否次级债'] == '是']['券面总额(元)'].sum() / bond_sum
    bond_yongxu = bond_type_df[bond_type_df['是否永续债'] == '是']['券面总额(元)'].sum() / bond_sum
    bond_chengtou = bond_type_df[bond_type_df['债券是否城投债'] == '是']['券面总额(元)'].sum() / bond_sum

    output_list.append(['次级债', bond_ciji])
    output_list.append(['永续债', bond_yongxu])
    output_list.append(['城投债', bond_chengtou])

    col_name = ['类别', '占比']
    output_df = pd.DataFrame(data=output_list, columns=col_name)

    output_df.to_excel(output_file)

    # print('利率债: {}'.format(bond_ratio))
    # print('AAA信用债: {}'.format(bond_AAA))
    # print('AA+信用债: {}'.format(bond_AAjia))
    # print('AA+以下信用债: {}'.format(bond_AA_blow))
    # print('无评级信用债: {}'.format(bond_none))
    # print('同业存单: {}'.format(bond_tongye))
    # print('偏股型债: {}'.format(bond_equ))
    #
    # bond_ciji = bond_type_df[bond_type_df['是否次级债'] == '是']['券面总额(元)'].sum() / bond_sum
    # bond_yongxu = bond_type_df[bond_type_df['是否永续债'] == '是']['券面总额(元)'].sum() / bond_sum
    # bond_chengtou = bond_type_df[bond_type_df['债券是否城投债'] == '是']['券面总额(元)'].sum() / bond_sum
    #
    # print('次级债: {}'.format(bond_ciji))
    # print('永续债: {}'.format(bond_yongxu))
    # print('城投债: {}'.format(bond_chengtou))