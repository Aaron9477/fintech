# -*- coding: utf-8 -*-
"""
Created on Tue JUL 21 17:20:45 2022
通过手动输入（部分需要手动拉取的基金净值）更新净值数据库数据
@author: 王永镇
"""
import pandas as pd
import sqlite3
import math
import func
import argparse

def update_handle(conn, cursor, handle_input_path):
    sql = "insert into fund_nval(fund_name, nval_date, nval) values(?, ?, ?)"

    smpp_info = pd.read_excel(handle_input_path)

    for index, row in smpp_info.iterrows():
        # 数据过滤
        if not func.is_number(row[2]) or math.isnan(row[2]):
            continue
        updata_info = (row[0], row[1].strftime('%Y-%m-%d'), row[2])

        try:
            cursor.execute(sql, updata_info)
        except sqlite3.IntegrityError as e:
            if e.__str__().startswith('UNIQUE constraint failed'):
                print('手工输入：基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(updata_info[0], updata_info[1]))
                print(updata_info)
                continue
            else:
                print(e)
        conn.commit()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--db_path', type=str, help='数据库路径', default='test2.db')
    parser.add_argument('--handle_input_path', type=str, help='手工输入数据文件位置', default='../../tests/手工输入数据.xlsx')
    args = parser.parse_args()

    conn = sqlite3.connect(args.db_path)
    cursor = conn.cursor()

    update_handle(conn, cursor, args.handle_input_path)

    cursor.close()
    conn.close()