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


def create_fund_nval(database_conn):
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

def create_fund_base_info(database_conn):
    fund_base_info = '''
        CREATE TABLE fund_base_info(
            fund_name text not null,
            fund_id_zyyx text,
            fund_name_zyyx text ,
            fund_id_smpp Double ,
            strategy text,
            administrator int Not Null, 
            region text ,
            manager text ,
            establish_time text ,
            report_data_source Double ,
            report_nval_type text,
            remarks text,
            primary key (fund_name))
    '''

    database_conn.execute(fund_base_info)
    print("fund_base_info表创建成功！")

def update_fund_nval():
    input_database_dir = 'test2.db'
    output_database_dir = 'test3.db'
    input_conn = sqlite3.connect(input_database_dir)
    output_conn = sqlite3.connect(output_database_dir)
    input_cursor = input_conn.cursor()
    output_cursor = output_conn.cursor()
    # create_database(output_cursor)
    sql = "select * from fund_nval"
    input_conn.commit()
    res = input_cursor.execute(sql)

    sql = "insert into fund_nval(fund_name, nval_date, nval) values(?, ?, ?)"

    for input in res.fetchall():
        name, datetime, nval, remark = input
        new_datetime = datetime.replace("/", "-")
        updata_info = (name, new_datetime, nval)
        try:
            output_cursor.execute(sql, updata_info)
        except sqlite3.IntegrityError as e:
            if e.__str__().startswith('UNIQUE constraint failed'):
                print('基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(updata_info[0], updata_info[1]))
                print(updata_info)
                continue
            else:
                print(e)
        output_conn.commit()
    input_cursor.close()
    output_cursor.close()
    input_conn.close()
    output_conn.close()

def update_fund_base_info():
    input_database_dir = 'old_db_with_old_ts/test2.db'
    output_database_dir = 'test2.db'
    input_conn = sqlite3.connect(input_database_dir)
    output_conn = sqlite3.connect(output_database_dir)
    input_cursor = input_conn.cursor()
    output_cursor = output_conn.cursor()
    # create_fund_base_info(output_cursor)
    sql = "select fund_name, fund_id_zyyx, fund_name_zyyx, fund_id_smpp, strategy, administrator, region, \
          manager, establish_time, report_data_source, report_data_source, report_nval_type, remarks from fund_base_info"
    input_conn.commit()
    res = input_cursor.execute(sql)

    sql = "insert into fund_base_info(fund_name, fund_id_zyyx, fund_name_zyyx, fund_id_smpp, strategy, administrator, region, \
          manager, establish_time, report_data_source, report_data_source, report_nval_type, remarks) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

    for input in res.fetchall():
        updata_info = list(input)
        updata_info[8] = updata_info[8].replace("/", "-")

        try:
            output_cursor.execute(sql, updata_info)
        except sqlite3.IntegrityError as e:
            if e.__str__().startswith('UNIQUE constraint failed'):
                print('基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(updata_info[0], updata_info[1]))
                print(updata_info)
                continue
            else:
                print(e)
        output_conn.commit()
    input_cursor.close()
    output_cursor.close()
    input_conn.close()
    output_conn.close()

if __name__ == '__main__':
    # update_fund_nval()
    update_fund_base_info()
