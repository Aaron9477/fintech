# -*- coding: utf-8 -*-
"""
    债券分析二步：拉取的债券数据过滤回购与外币资产，补充同业存单数据，并对债券打标签
"""

import pandas as pd
import numpy as np
import argparse
import datetime

from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_files

#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


def bond_type_statistics(input):

    df_input = input.copy()

    # 分类情况如下。特殊类型:同业存单、金融债
    # 1、同业存单单独打标签;2、金融债中政策银行债算利率债，其他算信用债
    interest_rate_bond = ["国债", "证金债", "央行票据", "地方政府债", "政府支持机构债"]
    credit_bond = ["短期融资券", "中期票据", "公司债", "企业债", "国际机构债", "项目收益票据", "资产支持证券", "定向工具"]
    partial_bond = ["可交换债", "可转债"]

    bond_name_list = list(df_input["SecuName"])
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
        elif wind_type_first_list[i] in partial_bond:
            bond_type.append("偏股型债")
        elif wind_type_first_list[i] == '同业存单':
            bond_type.append("同业存单")
        else:
            # 部分国债和证金债没有编码或者在万德上查不到
            if bond_grade_list[i] == 'AAA' or bond_grade_list[i] == 'AA+' or bond_grade_list[i] == 'A-1' or \
                    bond_grade_list[i] == 'A-2':
                bond_type.append("AA+(含)及以上信用债")
            elif pd.isna(bond_grade_list[i]):
                bond_type.append("无评级信用债")
            else:
                bond_type.append("AA+以下信用债")
    df_input["债券类型"] = bond_type

    return df_input


def cal_inter_bank_receipt(input):
    df_input = input.copy()
    df_input = df_input[df_input['secondary_type_chi'] == '同业存单']
    df_input['债券类型'] = '同业存单'
    return df_input


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


def mix_up_bond_name_with_report_name(input):
    df_input = input.copy()
    SecuName_list = list(df_input["SecuName"])
    bond_name_list = list(df_input["债券名称"])
    for i in range(len(bond_name_list)):
        if not isinstance(bond_name_list[i], str) and np.isnan(bond_name_list[i]):
            bond_name_list[i] = SecuName_list[i]
    df_input["债券名称"] = bond_name_list
    return df_input


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2023-09-30')
    parser.add_argument('--input_file', type=str, help='input_file', default='债券信息.xlsx')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财子债券打标签.xlsx')
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    statistics_date = args.statistics_date

    all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files(args.statistics_date)

    writer = pd.ExcelWriter(output_file)
    df = pd.read_excel(input_file)
    investment_details_df = pd.read_csv(top10_file)

    # 前处理 过滤逆回购和外币理财
    df = df_preprocess(df)

    # 打城投债标签
    df = get_bond_urban_investment_tag(df)

    # 使用发行人主体评级补充债券评级缺失的数据
    df = makeup_bond_grade(df)
    # 统计利率债、AA+以上信用债、AA+以下信用债
    bond_type_df = bond_type_statistics(df)

    # 筛选同业存单
    inter_bank_receipt_df = cal_inter_bank_receipt(investment_details_df)
    # 连接其他分类和同业存单
    df_res = pd.concat([bond_type_df, inter_bank_receipt_df])

    # 使用普益数据库的原名称补充万德拉不到数据的内容（如同业存单）
    df_res = mix_up_bond_name_with_report_name(df_res)

    df_res.to_excel(writer)

    writer.save()
    writer.close()


