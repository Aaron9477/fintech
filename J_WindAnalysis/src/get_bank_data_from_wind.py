import os

import sqlalchemy

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from datetime import datetime

DB_HOST = "10.16.233.38"
DB_USER = "jgbuser"
DB_PWD = "fund_evaluation"
DB_NAME = "wande"
DB_PORT = '1433'
engine = create_engine("mssql+pymssql://{}:{}@{}:{}/{}".format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME))
# engine = create_engine("mysql+mysqlconnector://{}:{}@{}:{}/{}".format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME))
############################################################################################################

# 定义从RDF下载原始数据表的函数， 输入为下载所需要的sql语句
def Obtain_RDFData(sql_str):
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


# 获取【基金Wind分类】信息
sql_fund_windclassify = "select * \
                         from CompIntroduction limit 100"
res_fund_windclassify = Obtain_RDFData(sql_fund_windclassify)

print(res_fund_windclassify)