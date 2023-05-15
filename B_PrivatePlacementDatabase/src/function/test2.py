# -*- coding: utf-8 -*-

import src.object.fund
import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
import timestamp

#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)


def create_database(database_conn):
    fund_nval = '''
        CREATE TABLE fund_nval(
            fund_name text Not Null, 
            nval_date date not null,
            nval Double not null,
            remarks text,
            primary key (fund_name, nval_date))
    '''
    database_conn.execute(fund_nval)
    print("fund_nval表创建成功！")

def update_database():
    input_database_dir = 'test3.db'
    input_conn = sqlite3.connect(input_database_dir)
    input_cursor = input_conn.cursor()
    sql = "select * from fund_nval where date(nval_date) > date('2022-05-08') limit 100"
    input_conn.commit()
    res = input_cursor.execute(sql)
    print(res.fetchall())

    input_cursor.close()
    input_conn.close()

if __name__ == '__main__':
    update_database()