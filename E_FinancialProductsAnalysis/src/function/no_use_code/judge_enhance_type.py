# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:20:45 2022
判断固收+产品是怎么+的
@author: 王永镇
"""

import pandas as pd
import numpy as np
import argparse

#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', None)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/全量金融产品投资组合明细_new.csv')
    args = parser.parse_args()
    input_file = args.input_file

    df = pd.read_csv(input_file)[:1000]

    # FCC0000001WJ-股票，FCC0000001WL-债券，CFN0000001H1-转股期可转债，FCC000000HE-权证，FCC0000001WQ-资产支持证券，FCC0000001WK-基金，
    # FCC000000YHP-港股，CFN000000274-理财产品，FCC0000001D1-其他资产，CFN0000008TM-资产证券化产品，FCC000000YHQ-期货，FCC00000139U-期权，
    # FCC000000SO6-远期外汇合约，FCC000000CIH-现金及银行存款，FCC000000N3P-买入返售金融资产，FCC0000001WP-同业存单，FCC0000001WV-同业借款

    grouped = df.groupby('FinProCode').apply(lambda t: t[t.InfoPublDate == t.InfoPublDate.max()])
    i = 0

    for name, c in grouped.iterrows():
        print(name)
        print(c)
        i += 1
        if i > 1000:
            break
    exit()
    print(grouped)
    print(type(grouped))

    print(list(grouped))
    exit()

    i = 0
    for name, group in grouped:
        print(name)
        print(group)
        i += 1
        if i > 1000:
            break
    exit()

    # print(grouped[:100])
    exit()

    for idx, row in df.iterrows():
        df.sort_values(['FinProCode', 'InfoPublDate'], ascending=[1, 0], inplace=True)
        grouped = df.groupby(['class']).head(2)




    # # 验证InvestTarget是否有注释中没有的
    # count_dict = {}
    # name_list = ['FCC0000001WJ', 'FCC0000001WL', 'CFN0000001H1', 'FCC000000HE', 'FCC0000001WQ', 'FCC0000001WK',
    #              'FCC000000YHP', 'CFN000000274', 'FCC0000001D1', 'CFN0000008TM', 'FCC000000YHQ', 'FCC000000SO6',
    #              'FCC000000CIH', 'FCC000000N3P', 'FCC0000001WP', 'FCC0000001WV']
    # not_in_name_set = set()
    # for idx, row in df.iterrows():
    #     if row['InvestObject'] in name_list:
    #         if row['InvestObject'] not in count_dict.keys():
    #             count_dict[row['InvestObject']] = set()
    #         count_dict[row['InvestObject']].add(row['FinProCode'])
    #     else:
    #         not_in_name_set.add(row['InvestObject'])
    #
    # print("投资对象在聚源注释中没有，但在数据中有的如下：")
    # print(not_in_name_set)
    # print("\n每种投资对象有多少只产品：")
    # for InvestObject in count_dict.keys():
    #     print("{}有{}只产品。".format(InvestObject, len(count_dict[InvestObject])))



