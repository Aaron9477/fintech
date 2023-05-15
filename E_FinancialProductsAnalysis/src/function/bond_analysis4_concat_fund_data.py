# -*- coding: utf-8 -*-
"""
    债券分析四步：将债券分析结果和基金分析结果合并
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


def concat_ratio_date_and_output(fund_df_input, bond_df_input, writer):
    fund_df = fund_df_input.copy()
    bond_df = bond_df_input.copy()

    output_df = fund_df['理财子各基金类型占比'][['理财子公司', '基金类型', '基金资产规模', '基金类型占公司基金总规模之比', '近一年收益率']]
    output_df.rename(columns={'基金类型': '资产类型', '基金资产规模': '资产规模', '基金类型占公司基金总规模之比': '基金:资产占公司基金总规模比例 / 债券:资产占公司债券总规模比例',
                              '近一年收益率': '基金:近一年收益率 / 债券:资产占公司债券总规模比例市场均值'}, inplace=True)
    output_df['大类资产类型'] = '基金'

    bond_type_df = bond_df['各债券类型占比'][['理财子公司', '债券类型', '债券类型资产规模', '债券类型占公司债券总规模之比', '债券类型占公司债券总规模之比均值']]
    bond_type_df.rename(columns={'债券类型': '资产类型', '债券类型资产规模': '资产规模', '债券类型占公司债券总规模之比': '基金:资产占公司基金总规模比例 / 债券:资产占公司债券总规模比例',
                              '债券类型占公司债券总规模之比均值': '基金:近一年收益率 / 债券:资产占公司债券总规模比例市场均值'}, inplace=True)
    bond_type_df['大类资产类型'] = '债券(按评级)'

    bond_urban_investment_df = bond_df['是否城投债占比']
    bond_urban_investment_df = bond_urban_investment_df[bond_urban_investment_df['债券是否城投债'] == '是'][['理财子公司', '债券是否城投债资产规模', '债券是否城投债占公司债券总规模之比', '债券是否城投债占公司债券总规模之比均值']]
    bond_urban_investment_df.rename(columns={'债券是否城投债资产规模': '资产规模', '债券是否城投债占公司债券总规模之比': '基金:资产占公司基金总规模比例 / 债券:资产占公司债券总规模比例',
                              '债券是否城投债占公司债券总规模之比均值': '基金:近一年收益率 / 债券:资产占公司债券总规模比例市场均值'}, inplace=True)
    bond_urban_investment_df['大类资产类型'] = '债券(按类型)'
    bond_urban_investment_df['资产类型'] = '城投债'

    bond_subordinated_df = bond_df['是否次级债占比']
    bond_subordinated_df = bond_subordinated_df[bond_subordinated_df['债券是否次级债'] == '是'][['理财子公司', '债券是否次级债资产规模', '债券是否次级债占公司债券总规模之比', '债券是否次级债占公司债券总规模之比均值']]
    bond_subordinated_df.rename(columns={'债券是否次级债资产规模': '资产规模', '债券是否次级债占公司债券总规模之比': '基金:资产占公司基金总规模比例 / 债券:资产占公司债券总规模比例',
                              '债券是否次级债占公司债券总规模之比均值': '基金:近一年收益率 / 债券:资产占公司债券总规模比例市场均值'}, inplace=True)
    bond_subordinated_df['大类资产类型'] = '债券(按类型)'
    bond_subordinated_df['资产类型'] = '次级债'

    bond_perpetual_df = bond_df['是否永续债占比']
    bond_perpetual_df = bond_perpetual_df[bond_perpetual_df['债券是否永续债'] == '是'][['理财子公司', '债券是否永续债资产规模', '债券是否永续债占公司债券总规模之比', '债券是否永续债占公司债券总规模之比均值']]
    bond_perpetual_df.rename(columns={'债券是否永续债资产规模': '资产规模', '债券是否永续债占公司债券总规模之比': '基金:资产占公司基金总规模比例 / 债券:资产占公司债券总规模比例',
                              '债券是否永续债占公司债券总规模之比均值': '基金:近一年收益率 / 债券:资产占公司债券总规模比例市场均值'}, inplace=True)
    bond_perpetual_df['大类资产类型'] = '债券(按类型)'
    bond_perpetual_df['资产类型'] = '永续债'

    output = pd.concat([output_df, bond_type_df, bond_urban_investment_df, bond_subordinated_df, bond_perpetual_df])
    # 根据溪恒使用的要求，对index做+1操作
    output.reset_index(drop=True, inplace=True)
    output.index = output.index + 1
    output.to_excel(writer, sheet_name='重仓资产占比分析')


def concat_top10_date_and_output(fund_df_input, bond_df_input, writer):
    fund_df = fund_df_input.copy()
    bond_df = bond_df_input.copy()

    # 读取基金类型占比数据
    output_df = fund_df['理财子前十大基金'][['理财子公司', '基金名称', '基金类型', '基金二级分类', '基金资产规模', '基金占公司基金总规模之比',
                                     '排名', '一年收益率', '二级分类下量化打分', '二级分类下量化打分排名']]
    output_df.rename(columns={'基金名称': '产品名称', '基金类型': '产品一级类型', '基金二级分类': '基金:产品二级类型 / 债券:空', '基金资产规模': '产品资产规模',
                              '基金占公司基金总规模之比': '产品占公司该类型产品总规模之比', '排名': '规模排名', '一年收益率': '基金:一年收益率 / 债券:空',
                              '二级分类下量化打分': '基金:二级分类下量化打分 / 债券:空', '二级分类下量化打分排名': '基金:二级分类下量化打分排名 / 债券:空'}, inplace=True)
    output_df['大类资产类型'] = '基金'

    bond_type_df = bond_df['各债券类型前十大']
    bond_type_df = bond_type_df[['理财子公司', '债券类型', '债券名称_代码', '债券资产规模', '债券占公司债券总规模之比', '排名']]
    bond_type_df.rename(columns={'债券类型': '产品一级类型', '债券名称_代码': '产品名称', '债券资产规模': '产品资产规模',
                                 '债券占公司债券总规模之比': '产品占公司该类型产品总规模之比', '排名': '规模排名'}, inplace=True)
    bond_type_df['大类资产类型'] = '债券(按评级)'

    bond_urban_investment_df = bond_df['是否城投债前十大']
    bond_urban_investment_df = bond_urban_investment_df[bond_urban_investment_df['债券是否城投债'] == '是']
    bond_urban_investment_df = bond_urban_investment_df[['理财子公司', '债券名称_代码', '债券资产规模', '债券占公司债券总规模之比', '排名']]
    bond_urban_investment_df.rename(columns={'债券名称_代码': '产品名称', '债券资产规模': '产品资产规模',
                                 '债券占公司债券总规模之比': '产品占公司该类型产品总规模之比', '排名': '规模排名'}, inplace=True)
    bond_urban_investment_df['大类资产类型'] = '债券(按类型)'
    bond_urban_investment_df['产品一级类型'] = '城投债'

    bond_subordinated_df = bond_df['是否次级债前十大']
    bond_subordinated_df = bond_subordinated_df[bond_subordinated_df['是否次级债'] == '是']
    bond_subordinated_df = bond_subordinated_df[['理财子公司', '债券名称_代码', '债券资产规模', '债券占公司债券总规模之比', '排名']]
    bond_subordinated_df.rename(columns={'债券名称_代码': '产品名称', '债券资产规模': '产品资产规模',
                                 '债券占公司债券总规模之比': '产品占公司该类型产品总规模之比', '排名': '规模排名'}, inplace=True)
    bond_subordinated_df['大类资产类型'] = '债券(按类型)'
    bond_subordinated_df['产品一级类型'] = '次级债'

    bond_perpetual_df = bond_df['是否永续债前十大']
    bond_perpetual_df = bond_perpetual_df[bond_perpetual_df['是否永续债'] == '是']
    bond_perpetual_df = bond_perpetual_df[['理财子公司', '债券名称_代码', '债券资产规模', '债券占公司债券总规模之比', '排名']]
    bond_perpetual_df.rename(columns={'债券名称_代码': '产品名称', '债券资产规模': '产品资产规模',
                                 '债券占公司债券总规模之比': '产品占公司该类型产品总规模之比', '排名': '规模排名'}, inplace=True)
    bond_perpetual_df['大类资产类型'] = '债券(按类型)'
    bond_perpetual_df['产品一级类型'] = '永续债'

    output = pd.concat([output_df, bond_type_df, bond_urban_investment_df, bond_subordinated_df, bond_perpetual_df])
    # 空白数据用"-"补充
    output.fillna("-", inplace=True)
    # 根据溪恒使用的要求，对index做+1操作
    output.reset_index(drop=True, inplace=True)
    output.index = output.index + 1
    output.to_excel(writer, sheet_name='重仓资产前十大分析')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--fund_file', type=str, help='fund_file', default='理财子基金分析.xlsx')
    parser.add_argument('--bond_file', type=str, help='bond_file', default='理财子债券分析.xlsx')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财子重仓资产分析.xlsx')
    args = parser.parse_args()
    fund_file = args.fund_file
    bond_file = args.bond_file
    output_file = args.output_file

    writer = pd.ExcelWriter(output_file)
    fund_df = pd.read_excel(fund_file, sheet_name=None)
    bond_df = pd.read_excel(bond_file, sheet_name=None)

    # 拼接占比信息并输出
    concat_ratio_date_and_output(fund_df, bond_df, writer)
    # 拼接top10数据并输出
    concat_top10_date_and_output(fund_df, bond_df, writer)

    writer.save()
    writer.close()


