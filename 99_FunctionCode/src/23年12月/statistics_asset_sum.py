import pandas as pd
import numpy as np
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../../tests/平安理财专户持仓明细_23年12月.xlsx')
    parser.add_argument('--middle_file', type=str, help='output_file', default='持仓规模求和_23年12月.xlsx')
    parser.add_argument('--output_file', type=str, help='output_file', default='统计资产占比_23年12月.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)
    output_file = args.output_file

    output_list = []

    grouped = df.groupby(['类别', '债券代码', '债券简称']).agg({'持仓净值(元)': sum})

    MarketValue_list = list(grouped['持仓净值(元)'].items())
    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0][0], MarketValue_list[i][0][1].replace(' ', ''),
                         MarketValue_list[i][0][2], MarketValue_list[i][1]])
    col_name = ['类别', '债券代码', '债券简称', '持仓净值(元)']
    df = pd.DataFrame(data=res_list, columns=col_name)
    df.to_excel(args.middle_file)

    all_sum = df['持仓净值(元)'].sum()
    bond_sum = df[~df['类别'].isin(['中长期纯债型基金', '可转换债券型基金', '优先股', '混合债券型二级基', '被动指数型债券基',
                                  '货币市场型基金'])]['持仓净值(元)'].sum() / all_sum
    fund_sum = df[df['类别'].isin(['中长期纯债型基金', '可转换债券型基金', '混合债券型二级基', '被动指数型债券基',
                                 '货币市场型基金'])]['持仓净值(元)'].sum() / all_sum
    youxiangu_sum = df[df['类别'].isin(['优先股'])]['持仓净值(元)'].sum() / all_sum

    output_list.append(['债券', bond_sum])
    output_list.append(['基金', fund_sum])
    output_list.append(['优先股', youxiangu_sum])


    col_name = ['类别', '占比']
    output_df = pd.DataFrame(data=output_list, columns=col_name)

    output_df.to_excel(output_file)
