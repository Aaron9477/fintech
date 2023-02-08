# -*- coding: utf-8 -*-
"""
Created on Tue JUL 21 17:20:45 2022
通过三种输入：朝阳永续（需要手动excel更新）、私募排排（数据库获取）、手动输入（部分需要手动拉取的基金净值）
更新净值数据库数据
@author: 王永镇
"""

import pandas as pd
import sqlite3
import math
import func
import argparse
import update_nval_from_smpp


def update_zyyx(conn, cursor, update_data, zyyx_input_path):
    insert_time = str(update_data)[:4] + '-' + str(update_data)[4:6] + '-'+str(update_data)[6:]
    sql = "insert into fund_nval(fund_name, nval_date, nval) values(?, ?, ?)"

    # 计数新数据，成功插入数据
    new_data, num_insert = 0, 0
    sheet_list = ['股票多头-多空', '指数增强', '市场中性', '管理期货', '宏观', '套利', '债券', '混合']
    for fund_base_info in sheet_list:
        smpp_info = pd.read_excel(zyyx_input_path, sheet_name=fund_base_info)

        for index, row in smpp_info.iteritems():
            # 数据过滤
            if not func.is_number(row[1]) or math.isnan(row[1]):
                continue
            updata_info = (row[0], insert_time, row[1])
            new_data += 1

            # 尝试将新数据插入到数据库中，主键（基金名称*日期）重复的会插入失败
            try:
                cursor.execute(sql, updata_info)
            except sqlite3.IntegrityError as e:
                if e.__str__().startswith('UNIQUE constraint failed'):
                    print('朝阳永续：基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(updata_info[0], updata_info[1]))
                    print(updata_info)
                    continue
                else:
                    print(e)
            num_insert += 1
            conn.commit()
    return new_data, num_insert


def update_handle(conn, cursor, handle_input_path):
    sql = "insert into fund_nval(fund_name, nval_date, nval) values(?, ?, ?)"
    smpp_info = pd.read_excel(handle_input_path)
    # 计数新数据，成功插入数据
    new_data, num_insert = 0, 0

    for index, row in smpp_info.iterrows():
        # 数据过滤
        if not func.is_number(row[2]) or math.isnan(row[2]):
            continue
        updata_info = (row[0], row[1].strftime('%Y-%m-%d'), row[2])
        new_data += 1

        # 尝试将新数据插入到数据库中，主键（基金名称*日期）重复的会插入失败
        try:
            cursor.execute(sql, updata_info)
        except sqlite3.IntegrityError as e:
            if e.__str__().startswith('UNIQUE constraint failed'):
                print('手工输入：基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(updata_info[0], updata_info[1]))
                print(updata_info)
                continue
            else:
                print(e)
        num_insert += 1
        conn.commit()
    return new_data, num_insert

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--update_date', type=str, help='更新净值时间', default='20220930')
    parser.add_argument('--db_path', type=str, help='数据库路径', default='test2.db')
    parser.add_argument('--zyyx_input_path', type=str, help='朝阳永续数据文件位置', default='../../tests/匹配表_第39周.xlsx')
    parser.add_argument('--handle_input_path', type=str, help='手工输入数据文件位置', default='../../tests/手工输入数据.xlsx')
    args = parser.parse_args()

    conn = sqlite3.connect(args.db_path)
    cursor = conn.cursor()

    new_data_zyyx, num_insert_zyyx = update_zyyx(conn, cursor, args.update_date, args.zyyx_input_path)
    new_data_smpp, num_insert_smpp = update_nval_from_smpp.update_smpp(conn, cursor, args.update_date)
    new_data_handle, num_insert_handle = update_handle(conn, cursor, args.handle_input_path)

    cursor.close()
    conn.close()

    print("\n本次更新情况汇总如下：")
    print("朝阳永续新数据{}条，插入数据库{}条数据。".format(new_data_zyyx, num_insert_zyyx))
    print("私募排排新数据{}条，插入数据库{}条数据。".format(new_data_smpp, num_insert_smpp))
    print("手工输入新数据{}条，插入数据库{}条数据。".format(new_data_handle, num_insert_handle))