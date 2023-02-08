# -*- coding: utf-8 -*-
"""
Created on Tue AUG 08 10:42:45 2022
@author: 王永镇
"""

import src.object.fund
import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
import timestamp
import sys
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--db_path', type=str, help='数据库路径', default='test2.db')
    parser.add_argument('--target_strategy', type=str, help='输入文件', default='沪深300增强')
    parser.add_argument('--start_time', type=str, help='2022/01/01', default='2022-01-01')
    parser.add_argument('--end_time', type=str, help='2022/01/31', default='2022-01-31')

    args = parser.parse_args()

    conn = sqlite3.connect(args.db_path)
    cursor = conn.cursor()

    sql = "select fund_name from fund_base_info where strategy='{a}'".format(a=args.target_strategy)
    cursor.execute(sql)
    conn.commit()
    raw_res = cursor.fetchall()
    fund_list = [x[0] for x in raw_res]

    fund_nval_change_list = []
    for fund in fund_list:
        sql = "select nval_date, nval from fund_nval where fund_name='{a}' and nval_date between '{b}' and '{c}' order by nval_date asc".format(a=fund, b=args.start_time, c=args.end_time)
        cursor.execute(sql)
        conn.commit()
        raw_res = cursor.fetchall()
        if len(raw_res) <= 1:
            continue
        start_nval = raw_res[0][1]
        end_nval = raw_res[-1][1]
        fund_nval_change_list.append(float(end_nval) / float(start_nval))

    print('{}在{}到{}之间表现 均值：{:.2%} 中位数：{:.2%}'.format(args.target_strategy, args.start_time, args.end_time,
                                             np.mean(fund_nval_change_list) - 1, np.median(fund_nval_change_list) - 1))

    cursor.close()
    conn.close()
