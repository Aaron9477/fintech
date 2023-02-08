# -*- coding: utf-8 -*-
"""
Created on Tue JUL 21 17:20:45 2022
数据库初始化时使用，读取pv_list.csv和匹配表_第28周.xlsx中的排排网id、朝阳永续id
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


def update_smpp_from_pv_list():
    '''
        基于pv_list,更新私募排排基金id 私募周报数据来源设定为私募排排 使用数据设定为累积净值
    '''
    conn = sqlite3.connect('test2.db')
    cursor = conn.cursor()
    sql = "update fund_base_info set fund_id_smpp=?, report_data_source='smpp', report_nval_type='cumulative_nav' where fund_name=?"

    # 读取全量的私募排排名称_id表
    smpp_info = pd.read_csv('../../tests/pv_list.csv')
    for index, col in smpp_info.iterrows():
        updata_info = (col[1], col[0])
        cursor.execute(sql, updata_info)
        conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


def update_smpp_from_nav_data_dic(db_file_dir):
    '''
        基于nav_data_dic 更新私募排排基金id
    '''
    conn = sqlite3.connect(db_file_dir)
    cursor = conn.cursor()
    sql = "update fund_base_info set fund_id_smpp=? where fund_name=?"
    smpp_info = pd.read_csv('D:/中信建投/7_组内工具/CAT/Data/nav_data_dic.csv')
    for index, col in smpp_info.iterrows():
        if col['fund_id'] != '-1':
            updata_info = (col['fund_id'], col['产品简称'])
            # updata_info = (col['fund_id'], col['产品简称_原'])
            # updata_info = (col['fund_id'], col['产品简称_模糊匹配'])
            cursor.execute(sql, updata_info)
            conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


def update_smpp_from_all_smpp_fund_id(db_file_dir):
    '''
        基于拉取的私募排排所有私募数据 更新私募排排基金id
    '''
    conn = sqlite3.connect(db_file_dir)
    cursor = conn.cursor()
    sql = "update fund_base_info set fund_id_smpp=? where fund_name=?"
    smpp_info = pd.read_csv('smpp_fund.csv')
    for index, col in smpp_info.iterrows():
        updata_info = (col['fund_id'], col['fund_name'])
        cursor.execute(sql, updata_info)
        updata_info = (col['fund_id'], col['fund_short_name'])
        cursor.execute(sql, updata_info)
        conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


def update_zyyx_from_matching_tbl():
    '''
        基于匹配表 更新朝阳永续基金id 私募周报数据来源设定为朝阳永续 使用数据设定为累积净值
    '''
    sheet_list = ['股票多头-多空', '指数增强', '市场中性', '管理期货', '宏观', '套利', '债券', '混合']
    # sheet_list = ['股票多头-多空']
    conn = sqlite3.connect('test2.db')
    cursor = conn.cursor()
    sql = "update fund_base_info set fund_id_zyyx=?, fund_name_zyyx=?, report_data_source='zyyx', report_nval_type='cumulative_nav' where fund_name=?"

    for fund_base_info in sheet_list:
        smpp_info = pd.read_excel('../../tests/匹配表_第28周.xlsx', sheet_name=fund_base_info)

        for index, row in smpp_info.iteritems():
            updata_info = (row[6], row[3], row[0])
            cursor.execute(sql, updata_info)
            conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--db_file', type=str, help='输入文件', default='test2.db')

    args = parser.parse_args()

    # update_smpp_from_pv_list()
    # update_zyyx_from_matching_tbl()
    # update_smpp_from_nav_data_dic(args.db_file)
    # 基于拉取的私募排排所有私募数据 更新私募排排基金id
    update_smpp_from_all_smpp_fund_id(args.db_file)



