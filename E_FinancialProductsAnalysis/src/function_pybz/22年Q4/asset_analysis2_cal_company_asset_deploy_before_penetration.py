# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤三：基于产品的大类资产配置，计算公司的大类资产配置
"""
import pandas as pd
import numpy as np
import argparse
import datetime
import copy

from func import get_product_exist


def cal_fixed_income_enhance_type(input_df, company_asset_sum):
    output_dict = {"产品数量": dict(), "产品规模": dict(), "产品规模占比": dict(), "产品系列名称": dict()}

    fixed_income_enhance_type_list = ['纯固收', '非标资产', 'QDII', '权益类', '商品及衍生品', 'FOF增强']

    for enhance_type in fixed_income_enhance_type_list:
        output_dict["产品数量"][enhance_type] = len(input_df[(input_df['InvestmentType'] == '固定收益类') & (input_df['enhance_type'] == enhance_type)])
        output_dict["产品规模"][enhance_type] = input_df[(input_df['InvestmentType'] == '固定收益类') & (input_df['enhance_type'] == enhance_type)]['AssetValue'].sum()
        if company_asset_sum != 0:
            output_dict["产品规模占比"][enhance_type] = output_dict["产品规模"][enhance_type] / company_asset_sum
        else:
            output_dict["产品规模占比"][enhance_type] = 0

        # 取top3产品名称
        grouped = input_df[(input_df['InvestmentType'] == '固定收益类') & (input_df['enhance_type'] == enhance_type)].groupby('set_name')
        sorted_product = list(grouped[['AssetValue']].sum().sort_values(by='AssetValue').index)
        if '其他' in sorted_product:
            sorted_product.remove('其他')
            sorted_product.append('其他')
        output_dict["产品系列名称"][enhance_type] = '、'.join(sorted_product[:3])

    output_dict["产品数量"]['其他'] = len(input_df[(input_df['InvestmentType'] == '固定收益类') & ((input_df['enhance_type'] == '混合类') | (input_df['enhance_type'] == 'None'))])
    output_dict["产品规模"]['其他'] = input_df[(input_df['InvestmentType'] == '固定收益类') & ((input_df['enhance_type'] == '混合类') | (input_df['enhance_type'] == 'None'))]['AssetValue'].sum()
    if company_asset_sum != 0:
        output_dict["产品规模占比"]['其他'] = output_dict["产品规模"]['其他'] / company_asset_sum
    else:
        output_dict["产品规模占比"]['其他'] = 0

    # 取top3产品名称
    grouped = input_df[(input_df['InvestmentType'] == '固定收益类') & ((input_df['enhance_type'] == '混合类') |
                                                                       (input_df['enhance_type'] == 'None'))].groupby('set_name')
    sorted_product = list(grouped[['AssetValue']].sum().sort_values(by='AssetValue').index)
    if '其他' in sorted_product:
        sorted_product.remove('其他')
        sorted_product.append('其他')
    output_dict["产品系列名称"]['其他'] = '、'.join(sorted_product[:3])

    return output_dict


def cal_fixed_income_company_ratio(input_df):
    res_list = []
    input_df = input_df[(input_df['InvestmentType'] == '固定收益类')]
    fixed_income_enhance_type_list = ['纯固收', '非标资产', 'QDII', '权益类', '商品及衍生品', 'FOF增强', '其他']
    fixed_income_name_reflect_dict = {'纯固收': '固收（纯债）', '非标资产': '固收增强（非标）', 'QDII': '固收增强（QDII）', '权益类': '固收增强（权益）',
                                      '商品及衍生品': '固收增强（衍生品）', 'FOF增强': '固收增强（FOF）', '其他': '固收增强（其他）'}
    # 除了'其他'类
    for enhance_type in fixed_income_enhance_type_list:
        if enhance_type != '其他':
            enhance_type_df = input_df[(input_df['enhance_type'] == enhance_type)]
        # '其他'类需要单独搞
        else:
            enhance_type_df = input_df[(input_df['enhance_type'] == '混合类') | (input_df['enhance_type'] == 'None')]

        enhance_type_asset_sum = enhance_type_df['AssetValue'].sum()
        grouped = enhance_type_df.groupby('CompanyName')
        for group_name in list(grouped.groups.keys()):
            if enhance_type != '其他':
                company_asset_ratio = input_df[(input_df['enhance_type'] == enhance_type) & (input_df['CompanyName'] == group_name)]['AssetValue'].sum() / enhance_type_asset_sum
            # '其他'类需要单独搞
            else:
                company_asset_ratio = input_df[((input_df['enhance_type'] == '混合类') | (input_df['enhance_type'] == 'None')) &
                                               (input_df['CompanyName'] == group_name)]['AssetValue'].sum() / enhance_type_asset_sum

            output_dict = {'公司名称': group_name, '产品类别': fixed_income_name_reflect_dict[enhance_type], '同类市场占比': company_asset_ratio}
            res_list.append(output_dict)

    return pd.DataFrame(res_list)


# 统计各类型资产的规模和占比
def cal_asset_scale_and_ratio(input_df, company_asset_sum, asset_list):
    output_dict = {"资产规模": dict(), "资产占比": dict()}
    for asset in asset_list:
        output_dict["资产规模"][asset] = (input_df[asset] * input_df['AssetValue']).sum()
        if company_asset_sum != 0:
            output_dict["资产占比"][asset] = output_dict["资产规模"][asset] / company_asset_sum
        else:
            output_dict["资产占比"][asset] = 0
    return output_dict


def cal_outsourcing_ratio(input_df):
    output_dict = {"委外（明确披露）": dict(), "委外（估算）": dict()}
    investment_type_list = ['现金管理类', '固定收益类', '混合类', '权益类', '商品及衍生品类']

    for investment_type in investment_type_list:
        investment_type_asset_sum = input_df[(input_df['InvestmentType'] == investment_type)]['AssetValue'].sum()
        if investment_type_asset_sum != 0:
            output_dict["委外（明确披露）"][investment_type] = (input_df[(input_df['InvestmentType'] == investment_type)]['资管产品:委外投资']
                                                        * input_df[(input_df['InvestmentType'] == investment_type)]['AssetValue']).sum() / investment_type_asset_sum
            output_dict["委外（估算）"][investment_type] = output_dict["委外（明确披露）"][investment_type] \
                                                     + ((input_df[(input_df['InvestmentType'] == investment_type)]["资管产品:私募/信托/保险产品"] +
                                                         input_df[(input_df['InvestmentType'] == investment_type)]['资管产品:未公布投资细类'])
                                                        * input_df[(input_df['InvestmentType'] == investment_type)]['AssetValue']).sum() / investment_type_asset_sum
        else:
            output_dict["委外（明确披露）"][investment_type] = 0
            output_dict["委外（估算）"][investment_type] = 0

    company_asset_sum = input_df['AssetValue'].sum()
    if company_asset_sum != 0:
        output_dict["委外（明确披露）"]['全部'] = (input_df['资管产品:委外投资'] * input_df['AssetValue']).sum() / company_asset_sum
        output_dict["委外（估算）"]['全部'] = output_dict["委外（明确披露）"]['全部'] + ((input_df['资管产品:私募/信托/保险产品'] +
                                                                        input_df['资管产品:未公布投资细类']) * input_df['AssetValue']).sum() / company_asset_sum
    else:
        output_dict["委外（明确披露）"]['全部'] = 0
        output_dict["委外（估算）"]['全部'] = 0
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


def preprocess(input_df, statistics_date):
    # 筛选存续期产品
    input_df = get_product_exist(input_df, statistics_date)

    def get_main_product_ind(data_set_RegistrationCode):
        ProductTypes = data_set_RegistrationCode['ProductType']
        tags = ['母产品', '产品', '子产品']
        for tag in tags:
            if tag in ProductTypes.values:
                return ProductTypes[ProductTypes == tag].index[0]

    # 筛选子产品 all_data_df
    RegistrationCodes = list(set(input_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = input_df[input_df['RegistrationCode'] == RegistrationCode]
        data_set_RegistrationCode = data_set_RegistrationCode.sort_values(by=['AssetValue'], ascending=False)
        if len(data_set_RegistrationCode.dropna(subset=['AssetValue']).index) > 0:
            data_set_RegistrationCode = data_set_RegistrationCode.dropna(subset=['AssetValue'])
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    output_df = input_df[input_df.index.isin(RegistrationCode_mainind)]

    return output_df


# 定义各产品类型统计各类型资产 投资规模and比例 的dict
def define_product_asset_dict(asset_list, investment_type_list):
    # 定义各产品类型，需要统计的资产类别
    asset_sum_dict = dict()
    asset_ratio_dict = dict()
    for asset in asset_list:
        # 名称拆分
        asset_origin_name_list = asset.split(':')
        asset_name_first, asset_name_second = asset_origin_name_list[0], asset_origin_name_list[1]
        if asset_name_first not in asset_sum_dict.keys():
            asset_sum_dict[asset_name_first] = dict()
        if asset_name_first not in asset_ratio_dict.keys():
            asset_ratio_dict[asset_name_first] = dict()
        asset_sum_dict[asset_name_first][asset_name_second] = []
        asset_ratio_dict[asset_name_first][asset_name_second] = []

    # 每种产品类型
    product_asset_scale_dict = dict()
    product_asset_ratio_dict = dict()
    for investment_type in investment_type_list:
        # 浅拷贝只能拷贝根目录，必须要深拷贝
        product_asset_scale_dict[investment_type] = copy.deepcopy(asset_sum_dict)
        product_asset_ratio_dict[investment_type] = copy.deepcopy(asset_ratio_dict)

    return product_asset_scale_dict, product_asset_ratio_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='穿透前资产投资比例统计.xlsx')
    parser.add_argument('--output_file', type=str, help='output_file', default='大类资产统计_委外分析.xlsx')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-12-31')
    args = parser.parse_args()

    output_file = args.output_file
    statistics_date = args.statistics_date
    df = pd.read_excel(args.input_file)

    # 前处理
    df = preprocess(df, statistics_date)

    # 定义存储最终结果的dict
    outsourcing_res_list = []
    asset_res_dict = {"全部": [], "现金管理类": [], "固定收益类": [], "混合类": [], "权益类": [], "商品及衍生品类": []}

    # 资产类别集合
    asset_list = ['货币市场类:现金及银行存款', '货币市场类:同业存单', '货币市场类:拆放同业及买入返售', '货币市场类:未公布投资细类',
                  '固定收益类:债券类', '固定收益类:非标准化债权类资产', '固定收益类:未公布投资细类', '权益类:股票', '权益类:股权',
                  '权益类:未公布投资细类', 'QDII:QDII', '商品及衍生品:商品及衍生品', '资管产品:公募基金', "资管产品:委外投资",
                  "资管产品:私募/信托/保险产品", '资管产品:未公布投资细类', '其他:其他']
    # 产品类型集合
    investment_type_list = ['现金管理类', '固定收益类', '混合类', '权益类', '商品及衍生品类', '全部']

    # 定义各产品类型统计各类型资产 投资规模and比例 的dict
    product_asset_scale_dict, product_asset_ratio_dict = define_product_asset_dict(asset_list, investment_type_list)

    # 按公司遍历
    grouped = df.groupby('CompanyName')
    for group_name in list(grouped.groups.keys()):
        company_df = grouped.get_group(group_name)

        # 计算公司总资产
        company_asset_sum = company_df['AssetValue'].sum()

        # 过滤掉没有资产的公司
        if company_asset_sum == 0:
            continue

        # # 委外分析结果统计
        # 统计 委外 的资产量和占比
        outsourcing_ratio = cal_outsourcing_ratio(company_df)
        investment_type_reflect_dict = {'固定收益类': '固定收益类（非现金）'}
        for investment_type in investment_type_list:
            # 对'固定收益类'改名字为'固定收益类（非现金）'
            investment_name = investment_type_reflect_dict[investment_type] if investment_type in investment_type_reflect_dict.keys() else investment_type
            tmp_dict = {'公司名称': group_name, '产品类别': investment_name, '公布财报总产品规模': company_asset_sum}

            for data_type in outsourcing_ratio.keys():
                tmp_dict[data_type] = outsourcing_ratio[data_type][investment_type]
            outsourcing_res_list.append(tmp_dict)

        # 大类资产穿透结果导出
        # 统计 大类资产 的资产量和占比
        asset_ratio_category = dict()
        for category_type in asset_res_dict.keys():
            # 选取特定类型的理财产品
            if category_type == '全部':
                category_df = company_df.copy()
            else:
                category_df = company_df[(company_df['InvestmentType'] == category_type)]
            category_asset_sum = category_df['AssetValue'].sum()

            # 统计该产品类型各类资产占比
            asset_scale_and_ratio = cal_asset_scale_and_ratio(category_df, category_asset_sum, asset_list)

            # 提取asset_scale_and_ratio中的结果，并按指定名称存储
            for asset in asset_list:
                # 名称拆分
                asset_origin_name_list = asset.split(':')
                asset_name_first, asset_name_second = asset_origin_name_list[0], asset_origin_name_list[1]

                tmp_dict = {'公司名称': group_name, '资产大类': asset_name_first, '资产细类': asset_name_second,
                            '公布财报总产品规模': company_asset_sum}
                for data_type in asset_scale_and_ratio.keys():
                    tmp_dict[data_type] = asset_scale_and_ratio[data_type][asset]

                asset_res_dict[category_type].append(tmp_dict)

                # 记录有披露的公司资产规模/资产占比，存储方式为asset_sum_dict[产品类型][一级资产][二级资产]，用于统计规模和占比的均值
                # 未公布投资细类的资产，即使公司没投，也去计算均值，所以此处会记录。其他类的资产只对>0的统计均值
                if asset_scale_and_ratio['资产规模'][asset] > 0 or asset.endswith('未公布投资细类'):
                    product_asset_scale_dict[category_type][asset_name_first][asset_name_second].append(asset_scale_and_ratio['资产规模'][asset])
                if asset_scale_and_ratio['资产占比'][asset] > 0 or asset.endswith('未公布投资细类'):
                    product_asset_ratio_dict[category_type][asset_name_first][asset_name_second].append(asset_scale_and_ratio['资产占比'][asset])

    # 大类资产补充均值 只对有该类资产的公司统计均值
    for category_type in asset_res_dict.keys():
        for asset_res in asset_res_dict[category_type]:
            asset_name_first = asset_res['资产大类']
            asset_name_second = asset_res['资产细类']
            if asset_name_first in product_asset_scale_dict[category_type].keys() and asset_name_second in product_asset_scale_dict[category_type][asset_name_first].keys():
                # 有大于一家公司有该类资产
                if len(product_asset_scale_dict[category_type][asset_name_first][asset_name_second]) > 0:
                    asset_res['有披露的公司资产规模均值'] = sum(product_asset_scale_dict[category_type][asset_name_first][asset_name_second]) / len(product_asset_scale_dict[category_type][asset_name_first][asset_name_second])

    # 大类资产补充均值 只补充有披露公司的均值
    for category_type in asset_res_dict.keys():
        for asset_res in asset_res_dict[category_type]:
            asset_name_first = asset_res['资产大类']
            asset_name_second = asset_res['资产细类']
            if asset_name_first in product_asset_ratio_dict[category_type].keys() and asset_name_second in product_asset_ratio_dict[category_type][asset_name_first].keys():
                # 有大于一家公司有该类资产
                if len(product_asset_ratio_dict[category_type][asset_name_first][asset_name_second]) > 0:
                    asset_res['有披露的公司资产占比均值'] = sum(product_asset_ratio_dict[category_type][asset_name_first][asset_name_second]) / len(product_asset_ratio_dict[category_type][asset_name_first][asset_name_second])

    # 大类资产排序
    asset_order = {'货币市场类': ['现金及银行存款', '同业存单', '拆放同业及买入返售', '未公布投资细类'],
                   '固定收益类': ['债券类', '非标准化债权类资产', '未公布投资细类'], '权益类': ['股票', '股权', '未公布投资细类'],
                   'QDII': ['QDII'], '商品及衍生品': ['商品及衍生品'], '资管产品': ['公募基金', '委外投资', '私募/信托/保险产品', '未公布投资细类'],
                   '其他': ['其他']}
    for category_type in asset_res_dict.keys():
        for asset_res in asset_res_dict[category_type]:
            first_asset_index = 0
            for first_asset in asset_order.keys():
                if first_asset != asset_res['资产大类']:
                    first_asset_index += 1
                else:
                    break
            if asset_res['资产细类'] in asset_order[asset_res['资产大类']]:
                second_asset_index = asset_order[asset_res['资产大类']].index(asset_res['资产细类'])
            else:
                second_asset_index = 999
            asset_res['资产大类序号'] = first_asset_index
            asset_res['资产细类序号'] = second_asset_index

    outsourcing_res_list_df = pd.DataFrame(outsourcing_res_list)
    asset_res_list_final = []
    for category_type in asset_res_dict.keys():
        for asset_res in asset_res_dict[category_type]:
            # 固定收益类改名
            category_type = '固定收益类（非现金）' if category_type == '固定收益类' else category_type
            asset_res['产品类型'] = category_type
            asset_res_list_final.append(asset_res)
    asset_res_list_df = pd.DataFrame(asset_res_list_final).sort_values(['公司名称', '产品类型', '资产大类序号', '资产细类序号'])
    asset_res_list_df['穿透类型'] = '穿透前'

    writer = pd.ExcelWriter(output_file)
    asset_res_list_df.to_excel(writer, sheet_name='资产配置统计分析')
    outsourcing_res_list_df.to_excel(writer, sheet_name='委外分析')
    writer.save()
