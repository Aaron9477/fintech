import pandas as pd
import numpy as np
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../tests/平安理财专户持仓明细.xlsx')
    parser.add_argument('--statistics_sheet', type=str, help='statistics_sheet', default='12月')
    parser.add_argument('--output_file', type=str, help='output_file', default='统计资产占比_12月.xlsx')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file, sheet_name=args.statistics_sheet)
    output_file = args.output_file

    output_list = []

    df['券面总额(元)'] = df['持仓净值(元)']

    all_sum = df['券面总额(元)'].sum()

    bond_sum = df[~df['类别'].isin(['货币基金', '其他', '衍生品', '债券型基金'])]['券面总额(元)'].sum() / all_sum
    fund_sum = df[df['类别'].isin(['货币基金', '债券型基金'])]['券面总额(元)'].sum() / all_sum
    yanshengpin_sum = df[df['类别'].isin(['衍生品'])]['券面总额(元)'].sum() / all_sum
    other_sum = df[df['类别'].isin(['其他'])]['券面总额(元)'].sum() / all_sum

    output_list.append(['债券', bond_sum])
    output_list.append(['基金', fund_sum])
    output_list.append(['衍生品', yanshengpin_sum])
    output_list.append(['其他', other_sum])


    col_name = ['类别', '占比']
    output_df = pd.DataFrame(data=output_list, columns=col_name)

    output_df.to_excel(output_file)
