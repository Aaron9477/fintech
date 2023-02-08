# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:20:45 2022
判断是否是固收+产品
@author: 王永镇
"""

import pandas as pd
import numpy as np
import argparse

# # 分类方法：固收+定义为投资了权益类、商品、衍生品类、基金、理财产品/信托计划及资产管理计划的固收类产品

name_set = set()

# FCC0000001X6-金融衍生品、FCC000000YHQ-期货、FCC000000HEP-权证、FCC00000139U-期权、FCC000001DY3-商品及金融衍生品类：其他资产、
# FCC000001DY0-商品类基金、FCC000001CN5-权益类和商品及金融衍生品类、FCC000001CN7-固定收益类和商品及金融衍生品类
financial_derivatives_list = ["FCC0000001X6", "FCC000000YHQ", "FCC000000HEP", "FCC00000139U", "FCC000001DY3",
                              "FCC000001DY0", "FCC000001CN5", "FCC000001CN7"]
# FCC0000014T8-可转债，FCC0000001T9-权益类、FCC0000001WJ-股票、FCC000001DY2-权益类：其他资产、FCC000001DXZ-权益类基金、
equity_list = ["FCC0000014T8", "FCC0000001T9", "FCC0000001WJ", "FCC000001DY2", "FCC000001DXZ"]
# CFN0000001CB-基金(130个)、CFN000000274-理财产品/信托计划及资产管理计划(1114个)、CBS000000028-其他资产(6202个)(以资产管理计划为主)
fund_or_asset_management_list = ["CFN0000001CB", "CFN000000274", "CBS000000028", ]

# FCC0000001T8-固定收益类、FCC0000001WN-标准化债权资产、FCC0000001WL-债券、FCC0000001WO-非标准化债权资产、
# FCC000001DY1-固定收益类：其他资产、FCC000001DXY-优先股、FCC0000014SB-债券基金、FCC000001CN6-固定收益类和资管产品(327个)
fixed_income_list = ["FCC0000001T8", "FCC0000001WN", "FCC0000001WL", "FCC0000001WO", "FCC000001DY1", "FCC000001DXY", "FCC0000014SB", "FCC000001CN6"]

# FCC0000001X3-现金类资产、CFN0000002OC-回购及逆回购、FCC0000013BX-高流动性资产(611个)
cash_type_list = ["FCC0000001X3", "CFN0000002OC", "FCC0000013BX"]


# CBS00000000K-买入返售金融资产(1个)、CFN000000ADG-股票质押式回购(0个)、FCC000000076-股权(0个)
other_list = ["CBS00000000K", "CFN000000ADG", ]

target_word_for_cash = ["货币", "现金", "流动"]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品投资目标与业绩基准_new.csv')
    args = parser.parse_args()
    input_file = args.input_file

    df = pd.read_csv(input_file)


    # 所有产品
    all_product_set = set()
    # 含有权益类和商品及金融衍生品类、基金、资管计划等
    fin_derivat_or_equity_or_fund_or_asset_managementset = set()
    # 含有固收类(非现金管理)
    fixed_income_no_cash_set = set()
    # 现金管理类
    cash_set = set()
    # 名称中含有货币理财相关的产品
    word_cash_set = set()

    for idx, row in df.iterrows():
        all_product_set.add(row['FinProCode'])

        has_word_for_cash = False
        for word in target_word_for_cash:
            if word in row['ChiName']:
                has_word_for_cash = True
        if has_word_for_cash:
            word_cash_set.add(row['FinProCode'])
            continue

        if row['InvestTarget'] in financial_derivatives_list or row['InvestTarget'] in equity_list or row['InvestTarget'] in fund_or_asset_management_list:
            fin_derivat_or_equity_or_fund_or_asset_managementset.add(row['FinProCode'])
        elif row['InvestTarget'] in fixed_income_list:
            fixed_income_no_cash_set.add(row['FinProCode'])
        elif row['InvestTarget'] in cash_type_list:
            cash_set.add(row['FinProCode'])

    no_fin_derivat_or_equity_set_final = all_product_set.difference(fin_derivat_or_equity_or_fund_or_asset_managementset).difference(fund_or_asset_management_list)
    fixed_income_set_final = no_fin_derivat_or_equity_set_final.intersection(fixed_income_no_cash_set)
    cash_set_final = no_fin_derivat_or_equity_set_final.difference(fixed_income_no_cash_set).intersection(cash_set).union(word_cash_set)

    print("总共有{}个产品".format(len(all_product_set)))
    print("涉及权益衍生品有{}个产品".format(len(fin_derivat_or_equity_or_fund_or_asset_managementset)))
    print(list(fin_derivat_or_equity_or_fund_or_asset_managementset)[:100])
    print("\n固收类总共有{}个产品,样例产品如下：".format(len(fixed_income_set_final)))
    print(list(fixed_income_set_final)[:100])
    print("\n现金管理类总共有{}个产品,样例产品如下：".format(len(cash_set_final)))
    print(list(cash_set_final))

    print(no_fin_derivat_or_equity_set_final.difference(fixed_income_no_cash_set).intersection(cash_set).difference(word_cash_set))
    print(len(no_fin_derivat_or_equity_set_final.difference(fixed_income_no_cash_set).intersection(word_cash_set)))

    exit()

    output_dict = {"固收+": fin_derivat_or_equity_or_fund_or_asset_managementset, "纯固收": fixed_income_set_final, "现金管理类": cash_set_final}
    np.save('../basic_classification.npy', output_dict)




    # # 验证InvestTarget是否有注释中没有的
    # for idx, row in df.iterrows():
    #     if row['InvestTarget'] in financial_derivatives_list or row['InvestTarget'] in equity_list \
    #             or row['InvestTarget'] in fund_or_asset_management_list or row['InvestTarget'] in fixed_income_list \
    #             or row['InvestTarget'] in cash_type_list or row['InvestTarget'] in other_list:
    #         continue
    #     name_set.add(row['InvestTarget'])
    # print(name_set)
    # exit()


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='')
#     parser.add_argument('--input_file', type=str, help='input_file', default='../data/投资目标表.csv')
#     args = parser.parse_args()
#     input_file = args.input_file
#
#     df = pd.read_csv(input_file)
#     type_dict = dict()
#
#
#     for idx, row in df.iterrows():
#         if row['InvestTarget'] not in type_dict.keys():
#             type_dict[row['InvestTarget']] = set()
#         type_dict[row['InvestTarget']].add(row['FinProCode'])
#
#         # if idx >= 500:
#         #     break
#
#     for type in type_dict.keys():
#         print("{}类有{}个产品".format(type, len(type_dict[type])))


