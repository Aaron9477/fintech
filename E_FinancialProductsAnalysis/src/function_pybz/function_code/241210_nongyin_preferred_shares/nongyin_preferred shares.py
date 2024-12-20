import dateutil
import pandas as pd
import numpy as np

from preprocess import preprocess
import argparse


def date_omit(df, col):
    df[col] = pd.to_datetime(df[col])
    df[col] = df[col].dt.strftime('%Y/%m/%d')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # 去年同期一天
    parser.add_argument('--path_优先股产品数据', type=str, help='path_优先股产品数据', default='银行理财优先股持仓.csv')
    parser.add_argument('--path_基本数据', type=str, help='path_基本数据', default='bank_wealth_product_base_pyjy_24Q3_241108.csv')
    parser.add_argument('--path_业绩数据', type=str, help='path_业绩数据', default='py_licai_product_nv_indicator_for_zhongyinlicai_20220101_20241122.csv')
    parser.add_argument('--path_top10', type=str, help='output_file', default='pybz_金融产品前十名持仓_24年Q3_241107.csv')
    parser.add_argument('--path_asset', type=str, help='output_file', default='pybz_金融产品资产配置_24年Q3_241107.csv')
    parser.add_argument('--analysis_date', type=str, help='analysis_date', default='2024-11-15')
    args = parser.parse_args()

    preferred_shares_prod_file = args.path_优先股产品数据
    all_data_file = args.path_基本数据
    performance_data_file = args.path_业绩数据
    top10_file = args.path_top10
    asset_file = args.path_asset
    analysis_date = args.analysis_date

    preferred_shares_prod_df = pd.read_csv(preferred_shares_prod_file, encoding='gbk')
    all_data_df = pd.read_csv(all_data_file)
    performance_data_df = pd.read_csv(performance_data_file, encoding='gbk')
    top10_df = pd.read_csv(top10_file)
    asset_df = pd.read_csv(asset_file)

    preferred_shares_FinProCode_df = preferred_shares_prod_df[['FinProCode']].drop_duplicates()

    prod_detail_df = preprocess(preferred_shares_FinProCode_df, all_data_df, analysis_date)
    performance_data__result_df = performance_data_df.merge(prod_detail_df[['FinProCode']], how='inner', on='FinProCode')
    top10_result_df = top10_df.merge(prod_detail_df[['FinProCode']], how='inner', on='FinProCode')
    asset_result_df = asset_df.merge(prod_detail_df[['FinProCode']], how='inner', on='FinProCode')

    prod_detail_df.to_excel('持仓优先股理财产品明细.xlsx')
    performance_data__result_df.to_excel('持仓优先股理财产品收益情况.xlsx')
    top10_result_df.to_excel('持仓优先股理财产品前十大持仓.xlsx')
    asset_result_df.to_excel('持仓优先股理财产品资产配置表.xlsx')