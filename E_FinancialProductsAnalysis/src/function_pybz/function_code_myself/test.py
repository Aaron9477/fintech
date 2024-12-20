import pandas as pd

from func import choose_product_mother_son, get_product_exist
from E_FinancialProductsAnalysis.src.function_pybz.reader_func import get_raw_files

# 前处理模块
def df_preprocess(input_df, all_data_df):

    # 筛选子产品 all_data_df
    all_data_df = choose_product_mother_son(all_data_df)
    all_data_df = all_data_df[['FinProCode']]
    input_df = input_df.merge(all_data_df, how='inner', on='FinProCode')

    return input_df


all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file = get_raw_files('2024-09-30')

all_data_df = pd.read_csv(all_data_file)

all_data_df = df_preprocess(all_data_df, all_data_df)

all_data_df.to_csv('test.csv')