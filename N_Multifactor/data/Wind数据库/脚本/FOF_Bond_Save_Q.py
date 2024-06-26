# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:06:27 2022

@author: lihbjs
"""

"""
A股。港股股票相关季频或基本信息数据库下载
"""
import os

import sqlalchemy

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from datetime import datetime

DB_HOST = "10.16.233.38"
DB_USER = "jgbuser"
DB_PWD  = "jgbuser"
DB_NAME = "wande"
DB_PORT = '1433'

path_save = r"D:\gjl\database\DB_Bond.db" #改写入地址
conn_save = sqlite3.connect(path_save)

c=conn_save.cursor()

############################################################################################################
# 定义从RDF下载原始数据表的函数， 输入为下载所需要的sql语句
def Obtain_RDFData(sql_str):
    engine = create_engine("mssql+pymssql://{}:{}@{}:{}/{}".format(DB_USER, DB_PWD, DB_HOST,DB_PORT, DB_NAME))
    # engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME))

    data = pd.read_sql(sql_str, engine)

    # c = conn.cursor()
    # sql = c.execute(sql_str)
    # res = sql.fetchall()
    # data = pd.DataFrame(res).round(4)

    # 获取表的列名
    # data.columns = [i[0] for i in c.description]
    # c.close()
    # conn.close()

    return data

#获取中国债券Wind分类板块
table_Name='中国债券Wind分类板块'
sql_fund = "select * from CBONDINDUSTRYWIND"
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【中国债券Wind分类板块】
pd.io.sql.to_sql(res_fund_code, table_Name, con=conn_save, index=False, if_exists='replace')
print(table_Name)

# #获取中国债券债券行情(沪深交易所)
# table_Name='中国债券债券行情(沪深交易所)'
# sql_fund = "select * from CBONDEODPRICES"
# res_fund_code = Obtain_RDFData(sql_fund)
# # 保存【中国债券Wind分类板块】
# pd.io.sql.to_sql(res_fund_code, table_Name, con=conn_save, index=False, if_exists='replace')
# print(table_Name)

conn_save.close()