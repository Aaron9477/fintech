import pandas as pd
import numpy as np
import argparse
import datetime


def preprocess(input_df):
    # 过滤过期产品
    input_df = input_df[input_df['ActMaturityDate'].apply(lambda x: get_not_before_enddate(x))]
    input_df = input_df[input_df['product_establish_date'].apply(lambda x: get_before_enddate(x))]
    input_df = input_df[(input_df['ProductType'] != '子产品') &
        ((input_df['OperationType'] == '开放式净值型') | (input_df['OperationType'] == '封闭式净值型'))]

    RegistrationCodes = list(set(input_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = input_df[input_df['RegistrationCode'] == RegistrationCode]
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    output_df = input_df[input_df.index.isin(RegistrationCode_mainind)]

    return output_df


# 设定截止日期
end_date = '2022-06-30 00:00:00'
def get_not_before_enddate(x):
    if (str(x) in ['NaT','nan']):
        return True
    if x < end_date:
        return False
    return True


def get_before_enddate(x):
    if (str(x) in ['NaT','nan']):
        return False
    if x <= end_date:
        return True
    return False


def get_main_product_ind(data_set_RegistrationCode):
    ProductTypes = data_set_RegistrationCode['ProductType']
    tags = ['母产品', '产品', '子产品']
    for tag in tags:
        if tag in ProductTypes.values:
            return ProductTypes[ProductTypes == tag].index[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/bank_wealth_product_221122.xlsx')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/bank_wealth_product_221114.csv')
    args = parser.parse_args()

    df = pd.read_excel(args.input_file)
    # df = pd.read_csv(args.input_file)

    res = preprocess(df)

    print(res)

    grouped = res.groupby(["ParentCompName", "InvestmentType"]).agg({'AssetValue': sum})
    MarketValue_list = list(grouped['AssetValue'].items())
    print(grouped)
    print(MarketValue_list)

    res_list = []
    for i in range(len(MarketValue_list)):
        res_list.append([MarketValue_list[i][0][0], MarketValue_list[i][0][1], MarketValue_list[i][1]])

    col_name = ['理财子公司', '基金类型', '基金资产规模']
    df_res = pd.DataFrame(data=res_list, columns=col_name)

    df_res.to_excel("产品规模统计.xlsx")



# def get_not_before_enddate(x):
#     if (str(x) in ['NaT','nan']):
#         return True
#     if x<=end_date:
#         return False
#     return True
#
# def get_before_enddate(x):
#     if (str(x) in ['NaT','nan']):
#         return False
#     if x<=end_date:
#         return True
#     return False
#
#
# ind = data_set.loc[data_set['ActMaturityDate'].isnull()].index
# data_set.loc[ind,'ActMaturityDate'] = data_set.loc[ind,'ProductMaturityDate']
#
# data_set['set'] = data_set['set'].apply(lambda x:x.split('-')[0])
# data_set = data_set[data_set['ActMaturityDate'].apply(lambda x:get_not_before_enddate(x))]
# data_set = data_set[data_set['product_establish_date'].apply(lambda x:get_before_enddate(x))]
#
# ind=data_set.loc[data_set['RegistrationCode'].isnull()].index
# data_set.loc[ind,'RegistrationCode']=data_set.loc[ind,'FinProCode']









