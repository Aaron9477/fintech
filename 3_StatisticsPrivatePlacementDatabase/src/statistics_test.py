# -*- coding: utf-8 -*-
"""
Created on Tue AUG 08 10:42:45 2022
基于私募数据库统计某维度某一时间段的净值增长
如：主观CTA策略在2022/01/06-2022/06/03之间的变化
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
    parser.add_argument('--db_path', type=str, help='输出文件', default='test2.db')
    parser.add_argument('--target_category', type=str, help='输入文件', default='指数增强')
    parser.add_argument('--target_strategy', type=str, help='输入文件', default='CTA')
    parser.add_argument('--start_time', type=str, help='2022/01/01', default='2022-01-01')
    parser.add_argument('--end_time', type=str, help='2022/01/31', default='2022-01-31')

    args = parser.parse_args()

    conn = sqlite3.connect(args.db_path)
    cursor = conn.cursor()

    sql = "select fund_name from fund_base_info where category='{a}'".format(a=args.target_category)
    # sql = "select fund_name from fund_base_info where strategy='{a}'".format(a=args.target_strategy)
    cursor.execute(sql)
    conn.commit()
    raw_res = cursor.fetchall()
    fund_list = [x[0] for x in raw_res]
    if '丰岭稳健成长1期' in fund_list:
        fund_list.remove('丰岭稳健成长1期')

    time_list = [('2022-01-01', '2022-01-31'), ('2022-02-01', '2022-02-31'), ('2022-03-01', '2022-03-31'), ('2022-04-01', '2022-04-31'), ('2022-05-01', '2022-05-31'), ('2022-06-01', '2022-06-31'), ]

    time_list = [('2019-01-01', '2019-12-31'), ('2020-01-01', '2020-12-31'), ('2021-01-01', '2021-12-31')]
    time_list = [('2022-01-01', '2022-06-31')]

    for time in time_list:
        fund_nval_change_list = []
        for fund in fund_list:
            sql = "select nval_date, nval from fund_nval where fund_name='{a}' and nval_date between '{b}' and '{c}' order by nval_date asc".format(a=fund, b=time[0], c=time[1])
            cursor.execute(sql)
            conn.commit()
            raw_res = cursor.fetchall()

            # 过滤数据量少的私募基金
            if len(raw_res) <= 22:
                continue
            flag = 1
            for tmp in raw_res:
                if(type(tmp[1]) != float):
                    print(tmp[1])
                    flag = 0
                    break
            if flag == 0:
                continue

            start_nval = raw_res[0][1]
            end_nval = raw_res[-1][1]
            ratio = float(end_nval) / float(start_nval)

            # 输出极端值
            if ratio > 2:
                print(raw_res)
                print(start_nval)
                print(end_nval)
            fund_nval_change_list.append(ratio)

        print('{}在{}到{}之间表现 均值：{:.2%} 中位数：{:.2%}'.format(args.target_strategy, time[0], time[1],
                                             np.mean(fund_nval_change_list) - 1, np.median(fund_nval_change_list) - 1))

    cursor.close()
    conn.close()

