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
        time_datetime = datetime.datetime.strptime(time, '%Y/%m/%d %H:%M')
        output_time = time_datetime.strftime('%Y/%m/%d %H:%M')
        output_time_list.append(output_time)
    return output_time_list


def get_nval_from_database(conn, cursor):
    sql = "select fund_name, fund_id_smpp from fund_base_info"
    cursor.execute(sql)
    fund_info = pd.DataFrame(cursor.fetchall())
    fund_info.columns = ["fund_name", "fund_id_smpp"]
    fund_info = fund_info.replace(to_replace='None', value=np.nan).dropna()

    sql = "select fund_name, nval_date, nval from fund_nval"
    cursor.execute(sql)
    fund_nval = pd.DataFrame(cursor.fetchall())
    fund_nval.columns = ["fund_name", "nval_date", "nval"]

    fund_nval_with_smpp_id = pd.merge(fund_nval, fund_info, how='left', on='fund_name')
    fund_nval_with_smpp_id = fund_nval_with_smpp_id.dropna()

    fund_nval_with_smpp_id = fund_nval_with_smpp_id[["fund_id_smpp", "nval_date", "nval"]]
    fund_nval_with_smpp_id.columns = ["FUND_ID", "PRICE_DATE", "CUMULATIVE_NAV"]

    dir = 'nav_data.csv'

    old_nval = pd.read_csv(dir)
    old_nval = old_nval[["FUND_ID", "PRICE_DATE", "NAV", "CUMULATIVE_NAV"]]

    time_list = list(old_nval['PRICE_DATE'])
    # old_nval['PRICE_DATE'] = datatime_transfer1(time_list)
    old_nval['PRICE_DATE'] = datatime_transfer2(time_list)

    time_list = list(fund_nval_with_smpp_id['PRICE_DATE'])
    fund_nval_with_smpp_id['PRICE_DATE'] = datatime_transfer1(time_list)

    new_nval = old_nval.append(fund_nval_with_smpp_id)
    new_nval.drop_duplicates(subset=['FUND_ID', 'PRICE_DATE'], keep='first')

    new_nval.to_csv(dir, index=None)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--db_path', type=str, help='输出文件', default='test2.db')
    # parser.add_argument('--input_file', type=str, help='输入文件', default='../../tests/重点观察私募周报_第28周.xlsx')
    # parser.add_argument('--is_create_new_database', type=int, help='是否新建数据库', default=1)
    # parser.add_argument('--is_delete_old_database', type=int, help='是否删除老数据库', default=1)

    args = parser.parse_args()

    conn = sqlite3.connect(args.db_path)
    cursor = conn.cursor()

    get_nval_from_database(conn, cursor)

    cursor.close()
    conn.close()

