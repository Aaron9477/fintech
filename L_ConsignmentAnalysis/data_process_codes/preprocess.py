# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月20日16:11:33
# @Author    : Noah Zhan
# @File      : preprocess
# @Project   : 银行理财代销图鉴
# @Function  ：筛选存续期产品、筛选主要产品、剔除母子关系
# --------------------------------

import numpy as np

def preprocess(input, statistics_date,if_filter_exsist=True):
    input_df = input.copy()
    # 筛选存续期产品
    if if_filter_exsist:
        input_df = get_product_exist(input_df, statistics_date)
    input_df_copy = input_df.copy()

#     def get_main_product_ind(data_set_RegistrationCode):
#         ProductTypes = data_set_RegistrationCode['ProductType']
#         tags = ['母产品', '产品', '子产品']
#         for tag in tags:
#             if tag in ProductTypes.values:
#                 return ProductTypes[ProductTypes == tag].index[0]

#     # 筛选子产品 all_data_df
#     RegistrationCodes = list(set(input_df['RegistrationCode'].dropna()))
#     RegistrationCode_mainind = []
#     for RegistrationCode in RegistrationCodes[:]:
#         data_set_RegistrationCode = input_df[input_df['RegistrationCode'] == RegistrationCode]
#         data_set_RegistrationCode = data_set_RegistrationCode.sort_values(by=['AssetValue'], ascending=False)
#         if len(data_set_RegistrationCode.dropna(subset=['AssetValue']).index) > 0:
#             data_set_RegistrationCode = data_set_RegistrationCode.dropna(subset=['AssetValue'])
#         RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
#     output_df = input_df[input_df.index.isin(RegistrationCode_mainind)]

    # 修改版本，加速了一点
    def temp_func(x):
        if(x['ProductType']=='母产品'): return 1
        elif(x['ProductType']=='产品'): return 2
        elif(x['ProductType']=='子产品'): return 3
        else: return np.NaN
    input_df['tag'] = input_df.apply(temp_func,axis = 1)
    input_df['index'] = input_df.index
    input_df = input_df.dropna(subset=['tag'])
    target_index = list(input_df.groupby('RegistrationCode')[['tag','index']].apply(lambda x:x.sort_values(by='tag',ascending=True)['index'].iloc[0]))
    output_df = input_df_copy.loc[target_index,:]
    return output_df

# 筛选存续期产品
def get_product_exist(input, statistics_date):
    input_df = input.copy()

    input_df = input_df[(((input_df['MaturityDate'].isnull()) | (input_df['MaturityDate'] >= statistics_date)))
                        & (input_df['product_establish_date'] <= statistics_date)]
    return input_df

# 剔除母子关系的数据
def exclude_mother_child_relation(input_df):
    return input_df[~(input_df['ParentCompName']==input_df['代销机构'])]

