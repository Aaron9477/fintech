# -*- coding: utf-8 -*-
"""
Created on Tue JUL 21 17:20:45 2022
通过朝阳永续（需要手动excel更新）更新净值数据库数据
@author: 王永镇
"""
import pandas as pd
import sqlite3
import math
import func
import argparse

# 拉取数据来源是朝阳永续的基金序列
def get_fund_list_zzyx(conn, cursor):
    sql = "select fund_name, fund_id_smpp from fund_base_info where report_data_source='zzyx' and report_nval_type='cumulative_nav'"
    fund_list_zyyx = pd.read_sql(sql, conn)
    conn.commit()
    return fund_list_zyyx


def update_zyyx(update_data, db_path, input_file):
    insert_time = str(update_data)[:4] + '-' + str(update_data)[4:6] + '-'+str(update_data)[6:]

    sheet_list = ['股票多头-多空', '指数增强', '市场中性', '管理期货', '宏观', '套利', '债券', '混合']
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = "insert into fund_nval(fund_name, nval_date, nval) values(?, ?, ?)"

    for fund_base_info in sheet_list:
        smpp_info = pd.read_excel(input_file, sheet_name=fund_base_info)

        for index, row in smpp_info.iteritems():
            if not func.is_number(row[1]) or math.isnan(row[1]):
                continue
            updata_info = (row[0], insert_time, row[1])

            try:
                cursor.execute(sql, updata_info)
            except sqlite3.IntegrityError as e:
                if e.__str__().startswith('UNIQUE constraint failed'):
                    print('基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(updata_info[0], updata_info[1]))
                    print(updata_info)
                    continue
                else:
                    print(e)
            conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--update_data', type=str, help='更新时间', default='20220715')
    parser.add_argument('--db_path', type=str, help='数据库位置', default='test2.db')
    parser.add_argument('--input_file', type=str, help='输入文件', default='../../tests/匹配表_第28周.xlsx')
    args = parser.parse_args()

    update_zyyx(args.update_data, args.db_path, args.input_file)


