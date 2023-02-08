# -*- coding: utf-8 -*-
"""
    基金分析第一步：拉取前十大资产中基金类型
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime
from func import choose_report_detail_table

#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

target_feature = ["name_official", "fund_corp_fundmanagementcompany", "fund_firstinvesttype", "fund_investtype",
                  "return_1y", "return_2y", "return_3y", "return_5y"]
feature_name = ['基金简称', '基金公司', '基金一级分类', '基金二级分类', '一年回报', '二年回报', '三年回报', '五年回报']



def df_preprocess(input_df, all_data_df, statistics_date):
    def get_main_product_ind(data_set_RegistrationCode):
        ProductTypes = data_set_RegistrationCode['ProductType']
        tags = ['母产品', '产品', '子产品']
        for tag in tags:
            if tag in ProductTypes.values:
                return ProductTypes[ProductTypes == tag].index[0]

    output_df = input_df.copy()

    # 筛选报告时间
    output_df = choose_report_detail_table(statistics_date, output_df)

    # 筛选子产品 all_data_df
    RegistrationCodes = list(set(all_data_df['RegistrationCode'].dropna()))
    RegistrationCode_mainind = []
    for RegistrationCode in RegistrationCodes[:]:
        data_set_RegistrationCode = all_data_df[all_data_df['RegistrationCode'] == RegistrationCode]
        RegistrationCode_mainind.append(get_main_product_ind(data_set_RegistrationCode))
    all_data_df = all_data_df[all_data_df.index.isin(RegistrationCode_mainind)]

    output_df = output_df.merge(all_data_df, how='inner', on='FinProCode')

    # 筛选基金和过滤基金代码为空的数据
    output_df = output_df[(output_df['InvestObject'] == 'FCC0000001WK') & (output_df['SecuCode'].notnull())]

    # 筛选存续期产品
    ActMaturityDate = list(output_df['ActMaturityDate'])
    ProductMaturityDate = list(output_df['ProductMaturityDate'])
    for i in range(len(ProductMaturityDate)):
        if not isinstance(ActMaturityDate[i], str) and np.isnan(ActMaturityDate[i]):
            ActMaturityDate[i] = ProductMaturityDate[i]
    output_df['ActMaturityDate'] = ActMaturityDate
    output_df = output_df[(output_df['ActMaturityDate'] > statistics_date) & (output_df['product_establish_date'] < statistics_date)]

    return output_df


def code_preprocess(input_list):
    res_list = []
    for x in input_list:
        x = str(x)
        if len(x) > 6:
            x = x[:6]
        x = x.split('.')[0].split(' ')[0]
        res_list.append(x + '.OF')
    return res_list


def split_list_average_n(origin_list, n):
    for i in range(0, len(origin_list), n):
        yield origin_list[i:i + n]


# def get_fund_type(row):
#     fund_id = row['SecuCode'] if row['SecuCode'].endswith('.OF') else row['SecuCode'] + '.OF'
#
#     # w.wsd("000312.OF", "name_official,fund_corp_fundmanagementcompany,fund_firstinvesttype,fund_investtype,return_1y,return_2y,return_3y,return_5y,style_marketvaluestyleattribute", "2022-11-16", "2022-11-16", "annualized=0;PriceAdj=F")
#     res = w.wsd(fund_id, "fund_firstinvesttype,fund_investtype", "2022-11-16", "2022-11-16", "PriceAdj=F")
#     print(res)
#
#     return res.Data[0][0], res.Data[1][0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2021-12-31')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品投资组合明细_21年四季报_230105.csv')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-03-31')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品投资组合明细_22年一季报_230105.csv')
    # parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-06-30')
    # parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品投资组合明细_22年中报_230105.csv')
    parser.add_argument('--statistics_date', type=str, help='statistics_date', default='2022-09-30')
    parser.add_argument('--input_file', type=str, help='input_file', default='../data/金融产品投资组合明细_22年三季报_230105_手动修改.csv')

    parser.add_argument('--all_data_file', type=str, help='all_data_file', default='../data/bank_wealth_product_01_06.csv')
    args = parser.parse_args()

    statistics_date = args.statistics_date
    df = pd.read_csv(args.input_file)

    # df = df[df["AgentName"] == "上银理财有限责任公司"]
    # df = df[df["AgentName"] == "民生理财有限责任公司"]

    all_data_df = pd.read_csv(args.all_data_file)[['FinProCode', 'ActMaturityDate', 'ProductMaturityDate',
                                                   'product_establish_date', 'RegistrationCode', 'ProductType']]

    # 前处理
    df = df_preprocess(df, all_data_df, statistics_date)

    fund_list = code_preprocess(df['SecuCode'].values)
    fund_set = set(fund_list)
    fund_str = ','.join(fund_set)

    w.start()
    index = 0
    for feat in target_feature:
        wind_return = w.wsd(fund_str, feat, statistics_date, statistics_date, "annualized=0;PriceAdj=F")
        fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
        value_list = [fund_value_dict[x] for x in fund_list]
        df[feature_name[index]] = value_list
        index += 1

    statistics_date_before_1y = str(int(statistics_date[:4])-1) + statistics_date[4:]
    wind_return = w.wsd(fund_str, "NAV_adj", statistics_date_before_1y, statistics_date_before_1y, "PriceAdj=F")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    value_list = [fund_value_dict[x] for x in fund_list]
    df['统计日一年前净值'] = value_list

    wind_return = w.wsd(fund_str, "NAV_adj", statistics_date, statistics_date, "PriceAdj=F")
    fund_value_dict = dict(zip(wind_return.Codes, wind_return.Data[0]))
    value_list = [fund_value_dict[x] for x in fund_list]
    df['统计日净值'] = value_list

    df['一年收益率'] = df['统计日净值'] / df['统计日一年前净值'] - 1

    df.to_excel("基金信息_" + statistics_date + ".xlsx")






    # exit()
    #
    # res = w.wsd(fund_str, "name_official", "2022-11-16", "2022-11-16", "PriceAdj=F")
    # dict_all = dict(zip(res.Codes, res.Data[0]))
    # print(dict_all)
    #
    # res_list = [dict_all[x] for x in fund_list[:100]]
    # print(res_list)
    #
    # exit()
    #
    # fund_list = fund_list[:100]
    #
    #
    # fund_list_split = split_list_average_n(fund_list, 10)
    # for x in fund_list_split:
    #     print(x)



    # w.start()
    # for index, feat in target_feature:
    #     final_res = []
    #     for tmp_list in fund_list_split:
    #         fund_str = ','.join(tmp_list)
    #         res = w.wsd(fund_str, "name_official", "2022-11-16", "2022-11-16", "PriceAdj=F")
    #         final_res.append(res.)
    #         print(res)
    #
    # exit()
    # res = w.wsd(fund_str, "name_official", "2022-11-16", "2022-11-16", "PriceAdj=F")
    # print(res)
    # exit()
    #
    # fund_list = [x if x.endswith('.OF') else x + '.OF' for x in fund_list_raw]
    # print(fund_list)
    # exit()

    # w.start()
    #
    # # df.insert(loc=17, column='基金一级分类', value='')
    # # df.insert(loc=18, column='基金二级分类', value='')
    #
    # res_list = [[] for x in range(9)]
    #
    # index = 0
    # for idx, row in df.iterrows():
    #     index += 1
    #     if index % 100 == 0:
    #         print(index)
    #
    #     try:
    #         fund_id = row['SecuCode'] if row['SecuCode'].endswith('.OF') else row['SecuCode'] + '.OF'
    #         res = w.wsd(fund_id, "name_official,fund_corp_fundmanagementcompany,fund_firstinvesttype,fund_investtype,return_1y,return_2y,return_3y,return_5y,style_marketvaluestyleattribute", "2022-11-16", "2022-11-16", "annualized=0;PriceAdj=F")
    #         # row.loc['基金一级分类'], row.loc['基金二级分类'] = res.Data[0][0], res.Data[1][0]
    #         for i in range(9):
    #             res_list[i].append(res.Data[i][0])
    #     except:
    #         for i in range(9):
    #             res_list[i].append(np.nan)
    #
    # df['基金简称'] = res_list[0]
    # df['基金公司'] = res_list[1]
    # df['基金一级分类'] = res_list[2]
    # df['基金二级分类'] = res_list[3]
    # df['一年回报'] = res_list[4]
    # df['二年回报'] = res_list[5]
    # df['三年回报'] = res_list[6]
    # df['五年回报'] = res_list[7]
    # df['风格'] = res_list[8]
    #
    # df.to_excel('fund_res.xlsx')

    # grouped = df.groupby('FinProCode')
    # for group_name in list(grouped.groups.keys()):
    #     tmp_res = w.wsd("513050.OF", "name_official,fund_corp_fundmanagementcompany,fund_firstinvesttype,fund_investtype,return_1y,return_2y,return_3y,return_5y,style_marketvaluestyleattribute", "2022-11-16", "2022-11-16", "annualized=0;PriceAdj=F")



# w.start()
# res = w.wsd("513050.OF", "name_official,fund_corp_fundmanagementcompany,fund_firstinvesttype,fund_investtype,return_1y,return_2y,return_3y,return_5y,style_marketvaluestyleattribute", "2022-11-16", "2022-11-16", "annualized=0;PriceAdj=F")
# print(res)
# print(res.Data)

# res = w.wsd("000312.OF", "name_official,fund_corp_fundmanagementcompany,fund_firstinvesttype,fund_investtype,return_1y,return_2y,return_3y,return_5y,style_marketvaluestyleattribute", "2022-11-16", "2022-11-16", "annualized=0;PriceAdj=F")
# print(res)