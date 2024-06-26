# -*- coding: utf-8 -*-
"""
    基金分析中间步骤：计算基金排名情况
"""
import pandas as pd
import argparse

# #显示所有的列
# pd.set_option('display.max_columns', None)
#
# #显示所有的行
# pd.set_option('display.max_rows', None)
#
# #设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)

def rank_fund_with_score(input):
    df_input = input.copy()
    df_input = df_input.drop_duplicates(subset='CODE')
    df_input['rank_index'] = df_input.groupby(['FUND_TYPE_2_NAME'])['TOTAL_SCORE_RANK_SHORT_TERM']\
        .rank(method='dense', na_option='keep', pct=False, ascending=False)
    return df_input[['CODE', 'rank_index']]


def get_sum_second_category(input):
    df_input = input.copy()
    df_input = df_input.drop_duplicates(subset='CODE')
    df_input["count"] = 1
    df_input = df_input.groupby("FUND_TYPE_2_NAME")["count"].sum()
    return df_input


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--score_file', type=str, help='input_file', default='../../data/fund_score_data.csv')
    parser.add_argument('--type_file', type=str, help='input_file', default='../../data/fund_type_data.csv')
    parser.add_argument('--output_file', type=str, help='output_file', default='理财子基金分析.xlsx')
    args = parser.parse_args()
    score_file = args.score_file
    type_file = args.type_file
    output_file = args.output_file

    score_df = pd.read_csv(score_file)
    type_df = pd.read_csv(type_file)
    score_df = score_df.dropna(axis=0, subset=['CODE', 'TOTAL_SCORE_RANK_SHORT_TERM'])
    score_df = score_df.merge(type_df, how='left', left_on='CODE', right_on='FUND_CODE')

    rank_df = rank_fund_with_score(score_df)
    second_category_sum = get_sum_second_category(score_df)

    score_df = score_df.merge(rank_df, how='left', on='CODE')

    score_df = score_df.merge(second_category_sum, how='left', on='FUND_TYPE_2_NAME')
    score_df = score_df.dropna(axis=0, subset=['rank_index', 'count'])
    score_df['二级分类下量化打分排名'] = score_df['rank_index'].astype(int).astype(str) + '/' + score_df['count'].astype(int).astype(str)
    # score_df['排名'] = score_df['rank_index'].astype(int).astype(str)

    score_df['无后缀代码'] = [int(x.split('.')[0]) for x in list(score_df['CODE'])]

    score_df.to_excel('全部基金量化打分排名.xlsx')
