# -*- coding: utf-8 -*-
"""
Created on Tue JUL 21 17:20:45 2022
数据库初始化时使用，导入周报中的净值数据
@author: 王永镇
"""

# import src.object.fund
import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
import timestamp
import sys
import argparse

#显示所有的列
pd.set_option('display.max_columns', None)
#显示所有的行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

sheet_list = ['股票多头-多空', '指数增强', '市场中性', '管理期货', '宏观', '套利', '债券', '混合']

def is_number(s):
    try:
        float(s)
        return True
    except (TypeError, ValueError):
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def create_database(database_conn):
    fund_nval = '''
        CREATE TABLE fund_nval(
            fund_name text Not Null, 
            nval_date text not null,
            nval Double not null,
            remarks text,
            primary key (fund_name, nval_date))
    '''
    database_conn.execute(fund_nval)
    print("fund_nval表创建成功！")

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

def delete_database(database_conn):
    database_conn.executescript('drop table if exists fund_nval;')
    print('delete fund_nval successful')
    database_conn.executescript('drop table if exists fund_base_info;')
    print('delete fund_base_info successful')

def read_update_file(input_file):
    fund_base_info_list = []
    for fund_base_info in sheet_list:
        fund_base_info_list.append(pd.read_excel(input_file, sheet_name=fund_base_info))
    # fund_base_info = pd.read_excel('../../tests/重点观察私募周报-测试数据.xlsx')
    return fund_base_info_list

def write_fund_base_info(conn, cursor, fund_info_content_list):
    # 记录录入基金名称
    insert_fund_list = []

    for category_index in range(len(fund_info_content_list)):
        for index, col in fund_info_content_list[category_index].iteritems():
            # 略过周报第一行
            if index == 'Unnamed: 0':
                continue
            # 基金有名称，且存在管理人和成立时间（用于过滤非基金基本信息的备注性的文字）
            if isinstance(col[0], str) and isinstance(col[2], str) and isinstance(col[5], datetime.datetime):
                fund_name, category, strategy, administrator, region, manager, establish_time = \
                    col[0], sheet_list[category_index], col[1], col[2], col[3], col[4], col[5].strftime('%Y-%m-%d')
                # print(fund_name, strategy, administrator, region, manager, establish_time)
                input_info = (fund_name, category, strategy, administrator, region, manager, establish_time)
                try:
                    # 尝试插入基金详情，并记录插入的基金
                    cursor.execute("insert into fund_base_info(fund_name, category, strategy, administrator, region, manager, establish_time)\
                    values(?, ?, ?, ?, ?, ?, ?)", input_info)
                    insert_fund_list.append(fund_name)
                except sqlite3.IntegrityError as e:
                    if e.__str__().startswith('UNIQUE constraint failed'):
                        # 打印信息
                        # print('基金{}已经在库中了，本次未录入。该条数据详情如下：'.format(input_info[0]))
                        # print(input_info)
                        continue
                    else:
                        print(e)
            else:
                # print(col[:6])
                pass
            conn.commit()
    return insert_fund_list

def write_fund_nval(conn, cursor, fund_info_content_list):
    for fund_info_content in fund_info_content_list:
        # 获取最后一行数据的位置
        nval_end_index = 0
        for i in range(len(fund_info_content.iloc[:, 0].values)):
            if (fund_info_content.iloc[:, 0].values[i] == '数据分析指标'):
                nval_end_index = i - 1
        if nval_end_index <= 0:
            print('not find nval_end_index. Exit!')
            break

        # 获取时间序列
        nval_time_list = fund_info_content.iloc[7: nval_end_index, 0].apply(lambda x: x.strftime('%Y-%m-%d'))
        nval_time_list = list(np.array(nval_time_list))

        for index, col in fund_info_content.iteritems():
            if index == 'Unnamed: 0':
                continue
            if isinstance(col[0], str) and isinstance(col[2], str) and isinstance(col[5], datetime.datetime):
                fund_name = col[0]
                if fund_name == '沪深300指数':
                    break
                for j in range(7, nval_end_index):
                    if is_number(col[j]) and col[j] is not np.nan:
                        input_info = (fund_name, nval_time_list[j - 7], col[j])
                        try:
                            cursor.execute("insert into fund_nval(fund_name, nval_date, nval) values(?, ?, ?)", input_info)
                        except sqlite3.IntegrityError as e:
                            if e.__str__().startswith('UNIQUE constraint failed'):
                                # 打印信息
                                # print('基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(input_info[0], input_info[1]))
                                # print(input_info)
                                continue
                            else:
                                print(e)
            else:
                continue
            conn.commit()

def update_database(args):
    # 连接数据库
    conn = sqlite3.connect(args.output_file)
    cursor = conn.cursor()
    if args.is_delete_old_database == 1:
        delete_database(cursor)
    if args.is_create_new_database == 1:
        # 新建数据库，只需要执行一次。后续更新数据库不需要再执行
        create_database(cursor)

    # 读取excel各个sheet
    fund_info_content_list = read_update_file(args.input_file)
    # 写入基金详情库
    insert_fund_list = write_fund_base_info(conn, cursor, fund_info_content_list)
    # 写入基金净值库
    write_fund_nval(conn, cursor, fund_info_content_list)

    cursor.close()
    conn.close()

    print("写入详情库的私募基金有:")
    print(insert_fund_list)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='输入文件', default='../../tests/重点观察私募周报（2023年第13周，2023.03.31）.xlsx')
    parser.add_argument('--output_file', type=str, help='输出文件', default='test2.db')
    parser.add_argument('--is_create_new_database', type=int, help='是否新建数据库', default=0)
    parser.add_argument('--is_delete_old_database', type=int, help='是否删除老数据库', default=0)

    args = parser.parse_args()

    update_database(args)


'''
python3 src/function/init_database_from_weekly.py --input_file=tests/重点观察私募周报（2022年第34周，2022.08.26）.xlsx --output_file=src/function/test2.db --is_create_new_database=1 --is_delete_old_database=1
'''