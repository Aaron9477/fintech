# -*- coding: utf-8 -*-
"""
    固收+/大类资产统计分析步骤三：基于产品的大类资产配置，计算公司的大类资产配置
"""
import pandas as pd
import numpy as np
import argparse
import datetime
import copy


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


def cal_outsourcing_ratio(input_df):
    output_dict = {"委外（明确披露）": dict(), "委外（估算）": dict()}
    # outsourcing_list = ['资管产品:私募资管产品/信托计划/计划类资产', '资管产品:委外投资']
    investment_type_list = ['现金管理类', '固定收益类', '混合类', '权益类', '商品及衍生品类']

    for investment_type in investment_type_list:
        investment_type_asset_sum = input_df[(input_df['InvestmentType'] == investment_type)]['AssetValue'].sum()
        if investment_type_asset_sum != 0:
            output_dict["委外（明确披露）"][investment_type] = (input_df[(input_df['InvestmentType'] == investment_type)]['资管产品:委外投资']
                                                        * input_df[(input_df['InvestmentType'] == investment_type)]['AssetValue']).sum() / investment_type_asset_sum
            output_dict["委外（估算）"][investment_type] = output_dict["委外（明确披露）"][investment_type] \
                                                     + ((input_df[(input_df['InvestmentType'] == investment_type)]['资管产品:私募资管产品/信托计划/计划类资产'] +
                                                         input_df[(input_df['InvestmentType'] == investment_type)]['未穿透的资管产品'])
                                                        * input_df[(input_df['InvestmentType'] == investment_type)]['AssetValue']).sum() / investment_type_asset_sum
        else:
            output_dict["委外（明确披露）"][investment_type] = 0
            output_dict["委外（估算）"][investment_type] = 0

    company_asset_sum = input_df['AssetValue'].sum()
    if company_asset_sum != 0:
        output_dict["委外（明确披露）"]['全部'] = (input_df['资管产品:委外投资'] * input_df['AssetValue']).sum() / company_asset_sum
        output_dict["委外（估算）"]['全部'] = output_dict["委外（明确披露）"]['全部'] + ((input_df['资管产品:私募资管产品/信托计划/计划类资产'] +
                                                                        input_df['未穿透的资管产品']) * input_df['AssetValue']).sum() / company_asset_sum
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


def get_main_product_ind(data_set_RegistrationCode):
    ProductTypes = data_set_RegistrationCode['ProductType']
    tags = ['母产品', '产品', '子产品']
    for tag in tags:
        if tag in ProductTypes.values:
            return ProductTypes[ProductTypes == tag].index[0]


def preprocess(input_df):
    # 识别现金管理类产品
    input_df.loc[input_df['inv_type'] == 1, 'InvestmentType'] = '现金管理类'

    # 过滤过期产品
    input_df = input_df[input_df['ActMaturityDate'].apply(lambda x: get_not_before_enddate(x))]
    input_df = input_df[input_df['product_establish_date'].apply(lambda x: get_before_enddate(x))]
    input_df = input_df[(input_df['enhance_type'].notnull()) &
        ((input_df['OperationType'] == '开放式净值型') | (input_df['OperationType'] == '封闭式净值型'))]

    RegistrationCodes = list(set(input_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = input_df[input_df['RegistrationCode'] == RegistrationCode]
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    output_df = input_df[input_df.index.isin(RegistrationCode_mainind)]

    return output_df


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='合并结果.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)

    # 前处理
    df = preprocess(df)

    grouped = df.groupby('CompanyName')

    enhance_type_res_list = []
    outsourcing_res_list = []
    asset_res_dict = {"全部": [], "现金管理类": [], "固定收益类": [], "混合类": [], "权益类": [], "商品及衍生品类": [], }
    # asset_res_list = []


    fix_income_company_ratio = cal_fixed_income_company_ratio(df)

    # TODO:该部分代码写得过于杂乱后续修改
    # 定义存储数据的dict
    asset_name_reflect_dict = {'未穿透的固定': '固定收益类:未公布投资细类', '未穿透的资管产品': '资管产品:未公布投资细类',
                               '非标资产': '固定收益类:非标债权资产', '资管产品:私募资管产品/信托计划/计划类资产': '资管产品:私募/信托产品'}
    asset_list = ['非标资产', '固定收益类:货币类', '固定收益类:债券类', '固定收益类:资产支持证券', '资管产品:公募基金', '资管产品:私募资管产品/信托计划/计划类资产',
                  '资管产品:委外投资', '混合类', 'QDII', '权益类', '商品及衍生品', '其他', "未穿透的固定", "未穿透的资管产品"]
    asset_sum_dict = dict()
    asset_ratio_dict = dict()
    for asset in asset_list:
        # 名称拆分
        asset_origin_name = asset_name_reflect_dict[asset] if asset in asset_name_reflect_dict.keys() else asset
        asset_origin_name_list = asset_origin_name.split(':')
        if len(asset_origin_name_list) == 1:
            asset_name_first, asset_name_second = asset_origin_name, asset_origin_name
        else:
            asset_name_first, asset_name_second = asset_origin_name_list[0], asset_origin_name_list[1]
        if asset_name_first not in asset_sum_dict.keys():
            asset_sum_dict[asset_name_first] = dict()
        if asset_name_first not in asset_ratio_dict.keys():
            asset_ratio_dict[asset_name_first] = dict()
        asset_sum_dict[asset_name_first][asset_name_second] = []
        asset_ratio_dict[asset_name_first][asset_name_second] = []

    # 为每种产品类型定义存储资产的dict
    investment_type_list = ['现金管理类', '固定收益类', '混合类', '权益类', '商品及衍生品类', '全部']
    asset_sum_dict_dict = dict()
    asset_ratio_dict_dict = dict()
    for investment_type in investment_type_list:
        # 浅拷贝只能拷贝根目录，必须要深拷贝
        asset_sum_dict_dict[investment_type] = copy.deepcopy(asset_sum_dict)
        asset_ratio_dict_dict[investment_type] = copy.deepcopy(asset_ratio_dict)

    # 按公司遍历
    for group_name in list(grouped.groups.keys()):
        # # 上银和交银当前策略不支持，先过滤掉
        # if group_name == '上银理财有限责任公司' or group_name == '交银理财有限责任公司':
        #     continue

        company_df = grouped.get_group(group_name)

        # 计算公司总资产
        company_asset_sum = company_df['AssetValue'].sum()
        company_fixed_income_sum = company_df[(company_df['InvestmentType'] == '固定收益类')]['AssetValue'].sum()

        # 过滤掉没有资产的公司
        if company_asset_sum == 0:
            continue

        # # 固收增强结果统计
        # 统计 非现金固收类 的资产量和占比
        fixed_income_enhance_type = cal_fixed_income_enhance_type(company_df, company_fixed_income_sum)
        # 名称映射关系字典
        fixed_income_name_reflect_dict = {'纯固收': '固收（纯债）', '非标资产': '固收增强（非标）', 'QDII': '固收增强（QDII）', '权益类': '固收增强（权益）',
                                          '商品及衍生品': '固收增强（衍生品）', 'FOF增强': '固收增强（FOF）', '其他': '固收增强（其他）'}
        # 原名称，使用字典映射为新名称
        fixed_income_enhance_type_list = ['纯固收', '非标资产', 'QDII', '权益类', '商品及衍生品', 'FOF增强', '其他']
        # 输出固收增强
        for enhance_type in fixed_income_enhance_type_list:
            tmp_dict = {'公司名称': group_name, '产品类别': fixed_income_name_reflect_dict[enhance_type], '固收类产品总规模': company_fixed_income_sum}
            for data_type in fixed_income_enhance_type.keys():
                tmp_dict[data_type] = fixed_income_enhance_type[data_type][enhance_type]
            enhance_type_res_list.append(tmp_dict)

        # # 委外分析结果统计
        # 统计 委外 的资产量和占比
        outsourcing_ratio = cal_outsourcing_ratio(company_df)
        investment_type_reflect_dict = {'固定收益类': '固定收益类（非现金）'}
        investment_type_list = ['现金管理类', '固定收益类', '混合类', '权益类', '商品及衍生品类', '全部']
        for investment_type in investment_type_list:
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
            asset_ratio = cal_asset_ratio(category_df, category_asset_sum)

            # 提取asset_ratio中的结果，并按指定名称存储
            asset_name_reflect_dict = {'未穿透的固定': '固定收益类:未公布投资细类', '未穿透的资管产品': '资管产品:未公布投资细类',
                                       '非标资产': '固定收益类:非标债权资产', '资管产品:私募资管产品/信托计划/计划类资产': '资管产品:私募/信托产品'}
            asset_list = ['非标资产', '固定收益类:货币类', '固定收益类:债券类', '固定收益类:资产支持证券', '资管产品:公募基金', '资管产品:私募资管产品/信托计划/计划类资产',
                          '资管产品:委外投资', '混合类', 'QDII', '权益类', '商品及衍生品', '其他', "未穿透的固定", "未穿透的资管产品"]
            for asset in asset_list:
                # 名称拆分
                asset_origin_name = asset_name_reflect_dict[asset] if asset in asset_name_reflect_dict.keys() else asset
                asset_origin_name_list = asset_origin_name.split(':')
                if len(asset_origin_name_list) == 1:
                    asset_name_first, asset_name_second = asset_origin_name, asset_origin_name
                else:
                    asset_name_first, asset_name_second = asset_origin_name_list[0], asset_origin_name_list[1]

                tmp_dict = {'公司名称': group_name, '资产大类': asset_name_first, '资产细类': asset_name_second, '公布财报总产品规模': company_asset_sum}
                for data_type in asset_ratio.keys():
                    tmp_dict[data_type] = asset_ratio[data_type][asset]

                asset_res_dict[category_type].append(tmp_dict)

                # 记录有披露的公司资产规模/资产占比，存储方式为asset_sum_dict[产品类型][一级资产][二级资产]
                # 未穿透的资产包含未披露的公司
                if asset_ratio['资产规模'][asset] > 0 or asset.startswith('未穿透的'):
                    asset_sum_dict_dict[category_type][asset_name_first][asset_name_second].append(asset_ratio['资产规模'][asset])
                if asset_ratio['资产占比'][asset] > 0 or asset.startswith('未穿透的'):
                    asset_ratio_dict_dict[category_type][asset_name_first][asset_name_second].append(asset_ratio['资产占比'][asset])

    # 大类资产补充均值 只补充有披露公司的均值
    for category_type in asset_res_dict.keys():
        for asset_res in asset_res_dict[category_type]:
            asset_name_first = asset_res['资产大类']
            asset_name_second = asset_res['资产细类']
            if asset_name_first in asset_sum_dict_dict[category_type].keys() and asset_name_second in asset_sum_dict_dict[category_type][asset_name_first].keys():
                # 有大于一家公司有该类资产
                if len(asset_sum_dict_dict[category_type][asset_name_first][asset_name_second]) > 0:
                    asset_res['有披露的公司资产规模均值'] = sum(asset_sum_dict_dict[category_type][asset_name_first][asset_name_second]) / len(asset_sum_dict_dict[category_type][asset_name_first][asset_name_second])

    # 大类资产补充均值 只补充有披露公司的均值
    for category_type in asset_res_dict.keys():
        for asset_res in asset_res_dict[category_type]:
            asset_name_first = asset_res['资产大类']
            asset_name_second = asset_res['资产细类']
            if asset_name_first in asset_ratio_dict_dict[category_type].keys() and asset_name_second in asset_ratio_dict_dict[category_type][asset_name_first].keys():
                # 有大于一家公司有该类资产
                if len(asset_ratio_dict_dict[category_type][asset_name_first][asset_name_second]) > 0:
                    asset_res['有披露的公司资产占比均值'] = sum(asset_ratio_dict_dict[category_type][asset_name_first][asset_name_second]) / len(asset_ratio_dict_dict[category_type][asset_name_first][asset_name_second])

    # 大类资产排序
    asset_order = {'固定收益类': ['货币类', '债券类', '资产支持证券', '非标债权资产', '未公布投资细类'], '权益类': ['权益类'], '混合类': ['混合类'],
                   '商品及衍生品': ['商品及衍生品'], 'QDII': ['QDII'], '资管产品': ['公募基金', '委外投资', '私募/信托产品', '未公布投资细类'], '其他': ['其他']}
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

    enhance_type_res_df = pd.DataFrame(enhance_type_res_list).merge(fix_income_company_ratio, how='left', on=['公司名称', '产品类别'])
    outsourcing_res_list_df = pd.DataFrame(outsourcing_res_list)
    asset_res_list_final = []
    for category_type in asset_res_dict.keys():
        for asset_res in asset_res_dict[category_type]:
            # 固定收益类改名
            category_type = '固定收益类（非现金）' if category_type == '固定收益类' else category_type
            asset_res['产品类型'] = category_type
            asset_res_list_final.append(asset_res)
    asset_res_list_df = pd.DataFrame(asset_res_list_final).sort_values(['公司名称', '产品类型', '资产大类序号', '资产细类序号'])

    writer = pd.ExcelWriter('固收+分类_大类资产穿透_委外分析.xlsx')
    enhance_type_res_df.to_excel(writer, sheet_name='固收增强分类')
    asset_res_list_df.to_excel(writer, sheet_name='大类资产穿透')
    outsourcing_res_list_df.to_excel(writer, sheet_name='委外分析')
    writer.save()
