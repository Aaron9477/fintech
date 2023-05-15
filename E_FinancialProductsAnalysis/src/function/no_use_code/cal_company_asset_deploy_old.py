# -*- coding: utf-8 -*-
"""
"""
import pandas as pd
import numpy as np
import argparse
import datetime


def cal_fixed_income_enhance_type(input_df, company_asset_sum):
    output_dict = {"产品数量": dict(), "产品规模": dict(), "产品规模占比": dict()}

    fixed_income_enhance_type_list = ['纯固收', '非标资产', 'QDII', '权益类', '商品及衍生品']

    for enhance_type in fixed_income_enhance_type_list:
        output_dict["产品数量"][enhance_type] = len(input_df[(input_df['InvestmentType'] == '固定收益类') & (input_df['enhance_type'] == enhance_type)])
        output_dict["产品规模"][enhance_type] = input_df[(input_df['InvestmentType'] == '固定收益类') & (input_df['enhance_type'] == enhance_type)]['AssetValue'].sum()
        if company_asset_sum != 0:
            output_dict["产品规模占比"][enhance_type] = output_dict["产品规模"][enhance_type] / company_asset_sum
        else:
            output_dict["产品规模占比"][enhance_type] = 0

    output_dict["产品数量"]['其他'] = len(input_df[(input_df['InvestmentType'] == '固定收益类') & ((input_df['enhance_type'] == '混合类') | (input_df['enhance_type'] == 'None'))])
    output_dict["产品规模"]['其他'] = input_df[(input_df['InvestmentType'] == '固定收益类') & ((input_df['enhance_type'] == '混合类') | (input_df['enhance_type'] == 'None'))]['AssetValue'].sum()
    if company_asset_sum != 0:
        output_dict["产品规模占比"]['其他'] = output_dict["产品规模"]['其他'] / company_asset_sum
    else:
        output_dict["产品规模占比"]['其他'] = 0

    return output_dict


def cal_asset_ratio(input_df, company_asset_sum):
    output_dict = {"资产规模": dict(), "资产占比": dict()}
    asset_list = ['非标资产', '固定收益类:货币类', '固定收益类:债券类', '固定收益类:资产支持证券', '资管产品:公募基金', '资管产品:私募资管产品/信托计划/计划类资产',
                  '资管产品:委外投资', '混合类', 'QDII', '权益类', '商品及衍生品', '其他', "未穿透的固定", "未穿透的资管产品"]
    for asset in asset_list:
        output_dict["资产规模"][asset] = (input_df[asset] * input_df['AssetValue']).sum()
        if company_asset_sum != 0:
            output_dict["资产占比"][asset] = output_dict["资产规模"][asset] / company_asset_sum
        else:
            output_dict["资产占比"][asset] = 0
    return output_dict


def cal_outsourcing_ratio(input_df, company_asset_sum):
    output_dict = {"资产规模": dict(), "资产占比": dict()}
    outsourcing_list = ['资管产品:私募资管产品/信托计划/计划类资产', '资管产品:委外投资']
    investment_type_list = ['现金管理类', '固定收益类', '混合类', '权益类', '商品及衍生品类']

    for outsourcing in outsourcing_list:
        for investment_type in investment_type_list:
            output_dict["资产规模"][investment_type + '_' + outsourcing] = (input_df[(input_df['InvestmentType'] == investment_type)][outsourcing]
                                                                        * input_df[(input_df['InvestmentType'] == investment_type)]['AssetValue']).sum()
            output_dict["资产占比"][investment_type + '_' + outsourcing] = output_dict["资产规模"][investment_type + '_' + outsourcing] / company_asset_sum
    return output_dict


# 设定截止日期
end_date = '2022-06-30 00:00:00'
def get_not_before_enddate(x):
    if (str(x) in ['NaT','nan']):
        return True
    if x < end_date:
        return False
    return True


def get_before_enddate(x):
    if (str(x) in ['NaT','nan']):
        return False
    if x <= end_date:
        return True
    return False


def preprocess(input_df):
    # 识别现金管理类产品
    target_word_for_cash = ["货币", "现金", "流动"]
    for word in target_word_for_cash:
        try:
            input_df.loc[input_df['product_name'].str.contains(word), 'InvestmentType'] = '现金管理类'
        except:
            continue

    # 过滤过期产品
    input_df = input_df[input_df['ActMaturityDate'].apply(lambda x: get_not_before_enddate(x))]
    input_df = input_df[input_df['product_establish_date'].apply(lambda x: get_before_enddate(x))]
    output_df = input_df[(input_df['enhance_type'].notnull()) & (input_df['ProductType'] != '子产品') &
        ((input_df['OperationType'] == '开放式净值型') | (input_df['OperationType'] == '封闭式净值型'))]
    return output_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='合并结果.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)
    grouped = df.groupby('CompanyName')

    enhance_type_res_list = []
    asset_res_list = []
    outsourcing_res_list = []
    index = 0

    for group_name in list(grouped.groups.keys()):
        # 上银和交银当前策略不支持，先过滤掉
        if group_name == '上银理财有限责任公司' or group_name == '交银理财有限责任公司':
            continue

        company_df = grouped.get_group(group_name)
        # 前处理
        company_df_filtered = preprocess(company_df)

        # 计算公司总资产
        company_asset_sum = company_df_filtered['AssetValue'].sum()
        company_fixed_income_sum = company_df_filtered[(company_df_filtered['InvestmentType'] == '固定收益类')]['AssetValue'].sum()

        # 过滤掉没有资产的公司
        if company_asset_sum == 0:
            continue

        # 分别统计 非现金固收类、大类资产、委外 的资产量和占比
        fixed_income_enhance_type = cal_fixed_income_enhance_type(company_df_filtered, company_fixed_income_sum)
        asset_ratio = cal_asset_ratio(company_df_filtered, company_asset_sum)
        outsourcing_ratio = cal_outsourcing_ratio(company_df_filtered, company_asset_sum)

        # 结果导出
        company_enhance_res_dict = {'CompanyName': group_name, '固收类产品总规模': company_fixed_income_sum}
        for data_type in fixed_income_enhance_type.keys():
            for enhance_type in fixed_income_enhance_type[data_type].keys():
                company_enhance_res_dict[enhance_type + '-' + data_type] = fixed_income_enhance_type[data_type][enhance_type]
        enhance_type_res_list.append(company_enhance_res_dict)

        company_asset_res_dict = {'CompanyName': group_name, '公布财报总产品规模': company_asset_sum}
        for data_type in asset_ratio.keys():
            for asset in asset_ratio[data_type].keys():
                company_asset_res_dict[asset + '-' + data_type] = asset_ratio[data_type][asset]
        asset_res_list.append(company_asset_res_dict)

        company_outsourcing_res_dict = {'CompanyName': group_name, '公布财报总产品规模': company_asset_sum}
        for data_type in outsourcing_ratio.keys():
            for outsourcing in outsourcing_ratio[data_type].keys():
                company_outsourcing_res_dict[outsourcing + '-' + data_type] = outsourcing_ratio[data_type][outsourcing]
        outsourcing_res_list.append(company_outsourcing_res_dict)

    enhance_type_res_df = pd.DataFrame(enhance_type_res_list)
    asset_res_list_df = pd.DataFrame(asset_res_list)
    outsourcing_res_list_df = pd.DataFrame(outsourcing_res_list)

    writer = pd.ExcelWriter('最终结果.xlsx')
    enhance_type_res_df.to_excel(writer, sheet_name='固收增强分类')
    asset_res_list_df.to_excel(writer, sheet_name='大类资产穿透')
    outsourcing_res_list_df.to_excel(writer, sheet_name='委外分析')
    writer.save()
