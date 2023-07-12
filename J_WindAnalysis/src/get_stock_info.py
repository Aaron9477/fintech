import os

import sqlalchemy

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from datetime import datetime

DB_HOST = "10.16.233.38"
DB_USER = "jgbuser"
DB_PWD  = "fund_evaluation"
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

def Obtain_DBData(sql_str, path):
    conn = sqlite3.connect(path)
    data = pd.read_sql(sql_str, conn)
    return data

# 将数据存储到 DB Browser
# conn_save = sqlite3.connect(r"D:\FOF研究\Code - RDF_Download\DB_FOF_Fund.db")
# path_save = r"D:\work\database\DB_Fund.db"
# path_save = r"D:\gjl\database\DB_Fund.db"
path_save = r"F:\gjl\database\DB_Fund.db"
conn_save = sqlite3.connect(path_save)
c=conn_save.cursor()


###########################################################################################################
######################################### 获取所需WindID - 基金数据 ###################################################


# 获取【基金Wind分类】信息
sql_fund_windclassify = "select F_INFO_WINDCODE, S_INFO_SECTOR, S_INFO_SECTORENTRYDT,S_INFO_SECTOREXITDT, CUR_SIGN \
                         from CHINAMUTUALFUNDSECTOR  order by F_INFO_WINDCODE, S_INFO_SECTORENTRYDT "
res_fund_windclassify = Obtain_RDFData(sql_fund_windclassify)

# 保存【中国Wind基金分类】
pd.io.sql.to_sql(res_fund_windclassify,"中国Wind基金分类", con = conn_save, index = False, if_exists = 'replace')