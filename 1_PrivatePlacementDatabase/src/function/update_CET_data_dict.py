# -*- coding: utf-8 -*-
"""
Created on Tue JUL 22 13:42:45 2022
读取基金净值数据库，对CET平台的净值信息做更新
@author: 王永镇
"""

import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
import timestamp
import sys
import argparse

#显示所有的列
pd.set_option('display.max_columns', 50)
# #显示所有的行
# pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

# category_reflact_dict = {"股票多头-多空": "股票多头", "宏观": "股票多头", }


def datatime_transfer1(input_time_list):
    output_time_list = []
    for time in input_time_list:
        time_datetime = datetime.datetime.strptime(time, '%Y-%m-%d')
        output_time = time_datetime.strftime('%Y/%m/%d %H:%M')
        output_time_list.append(output_time)
    return output_time_list


def datatime_transfer2(input_time_list):
    output_time_list = []
    for time in input_time_list:
        time_datetime = datetime.datetime.strptime(time, '%Y/%m/%d')
        output_time = time_datetime.strftime('%Y/%m/%d %H:%M')
        output_time_list.append(output_time)
    return output_time_list


def get_fund_info_list_from_database(conn, cursor):
    sql = "select fund_name as 产品简称, \
          case when fund_id_smpp is not null then fund_id_smpp else '-1' end as fund_id,\
          category as 投资策略,\
          administrator as 机构简称,\
          establish_time as 成立日期\
          from fund_base_info"
    fund_info_list = pd.read_sql(sql, conn)
    conn.commit()
    return fund_info_list


def write_CET_data_dict(cet_data_dict_path, add_fund_list):
    print(cet_data_dict_path)
    old_data = pd.read_csv(cet_data_dict_path, encoding='gb18030')
    # old_data = pd.read_csv(cet_data_dict_path, encoding='utf_8_sig')

    # time_list = list(old_data['成立日期'])
    # old_data['成立日期'] = datatime_transfer1(time_list)

    new_fund_list = old_data.append(add_fund_list)
    new_fund_list.drop_duplicates(subset=['产品简称'], keep='first')

    # print("fund_base_info中的establish_time形式由2022/01/01改为了2022-01-01")
    # print("当前工具不能使用，需要修改！！！！")
    # exit()
    print(new_fund_list)
    new_fund_list.to_csv(cet_data_dict_path, encoding='utf_8_sig', index=None)
    # dt = pd.merge(fund_nav, dt, how='left', left_on='fund_id', right_on='fund_id_smpp')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--db_path', type=str, help='数据库路径', default='test2.db')
    parser.add_argument('--cet_data_dict_path', type=str, help='CET基金详情文件位置', default='nav_data_dic.csv')
    # parser.add_argument('--cet_data_dict_path', type=str, help='CET基金详情文件位置', default='D:/中信建投/7_组内工具/CET/Data/nav_data_dic.csv')
    args = parser.parse_args()

    conn = sqlite3.connect(args.db_path)
    cursor = conn.cursor()

    fund_info_list = get_fund_info_list_from_database(conn, cursor)

    time_list = list(fund_info_list['成立日期'])
    fund_info_list['成立日期'] = datatime_transfer1(time_list)

    write_CET_data_dict(args.cet_data_dict_path, fund_info_list)

    cursor.close()
    conn.close()