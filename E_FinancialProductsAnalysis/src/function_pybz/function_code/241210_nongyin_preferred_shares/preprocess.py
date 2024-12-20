
import numpy as np
import pandas as pd


# 筛选筛选存续期产品且该产品是优先股持仓产品
def preprocess(input: pd.DataFrame, all_data_df, statistics_date, if_filter_exsist=True):
    input_df = input.copy()
    # 筛选存续期产品
    if if_filter_exsist:
        all_data_df = get_product_exist(all_data_df, statistics_date)

    # 修改版本，加速了一点
    def temp_func(x):
        if x['ProductType'] == '母产品':
            return 1
        elif x['ProductType'] == '产品':
            return 2
        elif x['ProductType'] == '子产品':
            return 3
        else:
            return np.NaN

    all_data_df['tag'] = all_data_df.apply(temp_func, axis=1)
    all_data_df['index'] = all_data_df.index
    all_data_df = all_data_df.fillna({'tag': 2})
    target_index = list(all_data_df.groupby('RegistrationCode')[['tag', 'index']].apply(
        lambda x: x.sort_values(by='tag', ascending=True)['index'].iloc[0]))
    all_data_df = all_data_df.loc[target_index, :]

    output_df = all_data_df.merge(input_df, how='inner', on='FinProCode')
    return output_df


# 筛选存续期产品
def get_product_exist(input: pd.DataFrame, statistics_date) -> pd.DataFrame:
    input_df = input.copy()
    input_df['product_establish_date'] = input_df['product_establish_date'].astype('datetime64[ns]')
    input_df['MaturityDate'] = input_df['MaturityDate'].astype('datetime64[ns]')
    input_df = input_df[((input_df['MaturityDate'].isnull()) | (input_df['MaturityDate'] >= statistics_date))
                        & (input_df['product_establish_date'] <= statistics_date)]
    return input_df


# 剔除母子关系的数据
def exclude_mother_child_relation(input_df):
    return input_df[~(input_df['ParentCompName'] == input_df['代销机构'])]
