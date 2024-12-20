
import numpy as np
import pandas as pd


# 筛选筛选存续期产品
def preprocess(input: pd.DataFrame, statistics_date, if_filter_exsist=True):
    input_df = input.copy()
    # 筛选存续期产品
    if if_filter_exsist:
        input_df = get_product_exist(input_df, statistics_date)
    input_df_copy = input_df.copy()

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

    input_df['tag'] = input_df.apply(temp_func, axis=1)
    input_df['index'] = input_df.index
    input_df = input_df.fillna({'tag': 2})
    target_index = list(input_df.groupby('RegistrationCode')[['tag', 'index']].apply(
        lambda x: x.sort_values(by='tag', ascending=True)['index'].iloc[0]))
    output_df = input_df_copy.loc[target_index, :]
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
