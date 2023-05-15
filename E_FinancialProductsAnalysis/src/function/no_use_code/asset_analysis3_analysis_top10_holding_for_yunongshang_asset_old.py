# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 17:20:45 2022
固收+/大类资产统计分析步骤三：根据前十大持仓和非标数据分析渝农商的资产配置（穿透前）
原因：渝农商资产配置数据为穿透后的，需要补充穿透前的数据
@author: 王永镇
"""

import pandas as pd
import numpy as np
import argparse

# # 分类方法：固收+定义为投资了权益类、商品、衍生品类、基金、理财产品/信托计划及资产管理计划的固收类产品

name_set = set()

a = ['固收', '资管产品', '混合类',
                                            'QDII', '其他', '权益类', '商品及衍生品', '非标资产', "固定收益类:货币类",
                                            "固定收益类:债券类", "固定收益类:资产支持证券", "资管产品:公募基金",
                                            "资管产品:私募资管产品/信托计划/计划类资产", "资管产品:委外投资", "未穿透的固定", "未穿透的资管产品"]



# FCC0000001X3-现金类资产、FCC000000CIH-现金及银行存款、FCC0000001WP-同业存单
# FCC0000001WL-债券、CFN0000001H1-可转债
# FCC0000001WQ-资产支持证券、CFN0000008TM-资产证券化产品
# FCC000000SO6-远期外汇合约、FCC000000YHQ-期货、FCC000000HE-权证、FCC00000139U-期权
# FCC0000001WJ-股票、FCC000000YHP-港股
# CFN000000274-理财产品
# FCC0000001WK-基金
# FCC0000001D1-其他
# FCC0000001WV-同业借款
reflect_dict = {"FCC0000001X3": "固定收益类:货币类", "FCC000000CIH": "固定收益类:货币类", "FCC0000001WP": "固定收益类:货币类",
                "FCC0000001WL": "固定收益类:债券类", "CFN0000001H1": "固定收益类:债券类",
                "FCC0000001WQ": "固定收益类:资产支持证券", "CFN0000008TM": "固定收益类:资产支持证券",
                "FCC000000SO6": "商品及衍生品", "FCC000000YHQ": "商品及衍生品", "FCC000000HE": "商品及衍生品", "FCC00000139U": "商品及衍生品",
                "FCC0000001WJ": "权益类", "FCC000000YHP": "权益类",
                "CFN000000274": "资管产品:私募资管产品/信托计划/计划类资产",
                "FCC0000001WK": "资管产品:公募基金",
                "FCC0000001D1": "其他",
                "FCC0000001WV": "非标资产"
                }
reflect_dict_second = {"固定收益类:货币类": "固收", "固定收益类:债券类": "固收", "固定收益类:资产支持证券": "固收", "商品及衍生品": "商品及衍生品",
                       "权益类": "权益类", "资管产品:私募资管产品/信托计划/计划类资产": "资管产品", "资管产品:公募基金": "资管产品", "混合类": "混合类",
                       "其他": "其他", "非标资产": "非标资产"}


def preprocess(input_df):
    # 只保留穿透前的数据渝农商
    input_df = input_df[(input_df['PenetrationType'] == 'FCC0000019PK') & (input_df['AgentName'] == '渝农商理财有限责任公司')]

    invest_object_list = list(input_df['InvestObject'])
    non_standard_list = list(input_df['IfNonStandardAssets'])
    first_invest_type_list = []
    second_invest_type_list = []
    for i in range(len(invest_object_list)):
        if non_standard_list[i] == 'FCC000000005':
            first_invest_type_list.append('非标资产')
            second_invest_type_list.append('非标资产')
        else:
            if invest_object_list[i] in reflect_dict.keys():
                first_invest_type_list.append(reflect_dict_second[reflect_dict[invest_object_list[i]]])
                second_invest_type_list.append(reflect_dict[invest_object_list[i]])
            else:
                first_invest_type_list.append('其他')
                second_invest_type_list.append('其他')
    input_df['first_invest_type_list'] = first_invest_type_list
    input_df['second_invest_type_list'] = second_invest_type_list

    return input_df


def choose_report(input_df):
    # 按 2022中报、2022二季报 的顺序，选取一份报告做后续处理
    if len(input_df[(input_df['InfoSource'] == '2022中报')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '2022中报')]
    elif len(input_df[(input_df['InfoSource'] == '2022二季报')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '2022二季报')]

    return input_df


# 统计大类资产情况
def cal_asset_proportion(input_df, col_name):
    first_asset_list = ['固收', '资管产品', '混合类',
         'QDII', '其他', '权益类', '商品及衍生品', '非标资产']
    second_asset_list = ["固定收益类:货币类",
         "固定收益类:债券类", "固定收益类:资产支持证券", "资管产品:公募基金",
         "资管产品:私募资管产品/信托计划/计划类资产"]
    asset_proportion = dict()
    for asset in first_asset_list:
        asset_proportion[asset] = input_df[(input_df['first_invest_type_list'] == asset)][col_name].sum()
    for asset in second_asset_list:
        asset_proportion[asset] = input_df[(input_df['second_invest_type_list'] == asset)][col_name].sum()

    return asset_proportion


def judge_enhance_type(proportion_dict):
    tmp_dict = proportion_dict.copy()

    # 移除固定收益类、资管类、其他类
    del tmp_dict['固收类']

    asset_weight_list = sorted(tmp_dict.items(), key=lambda x: x[1], reverse=True)
    # 占比最大且超过5%的作为增强类型
    if asset_weight_list[0][1] >= 0.05:
        return asset_weight_list[0][0]
    else:
        if proportion_dict['固收类'] > 0.9:
            return '纯固收'


def cal_asset_num(input_df):
    # 前处理
    input_df = choose_report(input_df)
    if input_df.shape[0] == 0:
        return
    output_dict = dict(input_df.iloc[0])
    del output_dict['SerialNumber'], output_dict['SecuCode'], output_dict['SecuName'],\
        output_dict['MarketValue'], output_dict['RatioInNV'], output_dict['AssetValue'], output_dict['AssetValueRatio']

    # 优先使用 RatioInNV ，为空使用AssetValueRatio
    if input_df['RatioInNV'].count() > 0:
        use_data_col_name = 'RatioInNV'
    elif input_df['AssetValueRatio'].count() > 0:
        use_data_col_name = 'AssetValueRatio'
    else:
        return

    # 资产总和须在[0.5,1.2]之间，有可能加杠杆
    if input_df[use_data_col_name].sum() > 1.2 or input_df[use_data_col_name].sum() < 0.5:
        return

    asset_proportion = cal_asset_proportion(input_df, use_data_col_name)
    output_dict.update(asset_proportion)
    return output_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品前十大持仓_加入产品总资产_221116.csv')
    parser.add_argument('--non_standard_statistics_file', type=str, help='non_standard_statistics_file', default='../data/FP_PortfolioDetails.csv')
    args = parser.parse_args()

    df = pd.read_csv(args.input_file)
    # 读取非标信息并合并
    non_standard_df = pd.read_csv(args.non_standard_file)
    non_standard_df = non_standard_df[["FinProCode", "InfoSource", "SecuName", "PenetrationType", "IfNonStandardAssets"]]
    df = df.merge(non_standard_df, how="inner", on=["FinProCode", "SecuName", "InfoSource", "PenetrationType"])

    # 前处理
    df = preprocess(df)

    # df.to_excel("资产标注.xlsx")
    output_df = pd.DataFrame(columns=['AgentName', 'ChiName', 'FinProCode', 'InfoPublDate', 'InfoSource', '固收', '资管产品', '混合类',
                                            'QDII', '其他', '权益类', '商品及衍生品', '非标资产', "固定收益类:货币类",
                                            "固定收益类:债券类", "固定收益类:资产支持证券", "资管产品:公募基金",
                                            "资管产品:私募资管产品/信托计划/计划类资产", "资管产品:委外投资", "未穿透的固定", "未穿透的资管产品"])

    # 固收+产品分类
    index = 0
    grouped = df.groupby('FinProCode')
    for group_name in list(grouped.groups.keys()):
        res_dict = cal_asset_num(grouped.get_group(group_name))
        output_df = output_df.append(res_dict, ignore_index=True)
        index += 1
        if index % 1000 == 0:
            print(index)

    output_df.to_excel("渝农商基于前十大持仓统计大类资产.xlsx")