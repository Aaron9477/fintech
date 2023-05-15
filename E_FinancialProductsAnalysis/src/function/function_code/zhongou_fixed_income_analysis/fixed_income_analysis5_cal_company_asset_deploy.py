# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤三：基于产品的大类资产配置，计算公司的大类资产配置
"""
import pandas as pd
import numpy as np
import argparse
import datetime
import copy


def cal_fixed_income_enhance_type(input_df, company_asset_sum, fixed_income_enhance_type_list):
    output_dict = {"产品数量": dict(), "产品规模": dict(), "产品规模占比": dict(), "产品系列名称": dict()}

    for enhance_type in fixed_income_enhance_type_list:
        output_dict["产品数量"][enhance_type] = len(input_df[(input_df['InvestmentType'] == '固定收益类') & (input_df['enhance_type'] == enhance_type)])
        output_dict["产品规模"][enhance_type] = input_df[(input_df['InvestmentType'] == '固定收益类') & (input_df['enhance_type'] == enhance_type)]['AssetValue'].sum()
        if company_asset_sum != 0:
            output_dict["产品规模占比"][enhance_type] = output_dict["产品规模"][enhance_type] / company_asset_sum
        else:
            output_dict["产品规模占比"][enhance_type] = 0

        # 取top3产品名称
        grouped = input_df[(input_df['InvestmentType'] == '固定收益类') & (input_df['enhance_type'] == enhance_type)].groupby('set')
        sorted_product = list(grouped[['AssetValue']].sum().sort_values(by='AssetValue').index)
        if '其他' in sorted_product:
            sorted_product.remove('其他')
            sorted_product.append('其他')
        output_dict["产品系列名称"][enhance_type] = '、'.join(sorted_product[:3])

    return output_dict


def cal_fixed_income_company_ratio(input_df, fixed_income_enhance_type_list):
    res_list = []
    input_df = input_df[(input_df['InvestmentType'] == '固定收益类')]

    # 除了'其他'类
    for enhance_type in fixed_income_enhance_type_list:
        enhance_type_df = input_df[(input_df['enhance_type'] == enhance_type)]
        enhance_type_asset_sum = enhance_type_df['AssetValue'].sum()
        grouped = enhance_type_df.groupby('CompanyName')
        for group_name in list(grouped.groups.keys()):
            company_asset_ratio = input_df[(input_df['enhance_type'] == enhance_type) & (input_df['CompanyName'] == group_name)]['AssetValue'].sum() / enhance_type_asset_sum
            output_dict = {'公司名称': group_name, '产品类别': enhance_type, '同类市场占比': company_asset_ratio}
            res_list.append(output_dict)

    return pd.DataFrame(res_list)


def preprocess(input_df):
    # 识别现金管理类产品
    input_df.loc[input_df['inv_type'] == 1, 'InvestmentType'] = '现金管理类'

    return input_df


# 对固收增强进行归类
def fixed_income_type_reflect(input):
    input_df = input.copy()
    asset_name_reflect_dict = {'纯债': '固收（纯债）', '固收+(权益)': '固收增强（权益）', '固收+(非标)': '固收增强（非标）',
                               '固收+(权益,非标)': '固收增强（多资产）', '固收+(权益,衍生品,非标)': '固收增强（多资产）',
                               '固收+(衍生品,非标)': '固收增强（多资产）', '固收+(衍生品)': '固收增强（衍生品）',
                               '固收+(权益,衍生品)': '固收增强（衍生品）', '固收+(QDII)': '固收增强（QDII）',
                               '固收+(QDII,权益)': '固收增强（QDII）', '固收+(其他)': '固收增强（资管）', '底层数据未披露': '固收增强（未披露）'}
    enhance_type = input_df['enhance_type_asset']
    enhance_type_reflect = [asset_name_reflect_dict[x] for x in enhance_type]
    input_df['enhance_type'] = enhance_type_reflect
    return input_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='固收增强分类结果.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)

    # 前处理
    df = preprocess(df)

    enhance_type_res_list = []
    fixed_income_enhance_type_list = ['固收（纯债）', '固收增强（权益）', '固收增强（非标）', '固收增强（多资产）', '固收增强（衍生品）',
                                      '固收增强（QDII）', '固收增强（资管）', '固收增强（未披露）']
    # 对固收增强类型进行归类
    df = fixed_income_type_reflect(df)

    # 计算固收增强产品的同类市场占比
    fix_income_company_ratio = cal_fixed_income_company_ratio(df, fixed_income_enhance_type_list)

    grouped = df.groupby('CompanyName')
    # 按公司遍历，计算单个公司的占比
    for group_name in list(grouped.groups.keys()):

        company_df = grouped.get_group(group_name)

        # 计算公司总资产
        company_asset_sum = company_df['AssetValue'].sum()
        company_fixed_income_sum = company_df[(company_df['InvestmentType'] == '固定收益类')]['AssetValue'].sum()

        # 过滤掉没有资产的公司
        if company_asset_sum == 0:
            continue

        # # 固收增强结果统计
        # 统计 非现金固收类 的资产量和占比
        fixed_income_enhance_type = cal_fixed_income_enhance_type(company_df, company_fixed_income_sum, fixed_income_enhance_type_list)
        # 输出固收增强
        for enhance_type in fixed_income_enhance_type_list:
            tmp_dict = {'公司名称': group_name, '产品类别': enhance_type, '固收类产品总规模': company_fixed_income_sum}
            for data_type in fixed_income_enhance_type.keys():
                tmp_dict[data_type] = fixed_income_enhance_type[data_type][enhance_type]
            enhance_type_res_list.append(tmp_dict)

    enhance_type_res_df = pd.DataFrame(enhance_type_res_list).merge(fix_income_company_ratio, how='left', on=['公司名称', '产品类别'])

    writer = pd.ExcelWriter('固收+分类.xlsx')
    enhance_type_res_df.to_excel(writer, sheet_name='固收增强分类')
    writer.save()
