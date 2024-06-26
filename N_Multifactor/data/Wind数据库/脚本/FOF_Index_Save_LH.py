"""
指数相关信息下载
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

# 将数据存储到 DB Browser
# conn_save = sqlite3.connect(r"D:\FOF研究\Code - RDF_Download\DB_FOF_Fund.db")
# path_save = r"D:\work\database\DB_Fund.db"
path_save = r"D:\gjl\database\DB_Index.db"
conn_save = sqlite3.connect(path_save)
c=conn_save.cursor()


###########################################################################################################
######################################### 获取所需WindID - 基金数据 ###################################################

"""
中国A股-指数数据
"""
# # 获取【中国A股指数基本资料】
# sql = "select * from AINDEXDESCRIPTION"
# res = Obtain_RDFData(sql)
# # 保存【中国A股指数基本资料】
# pd.io.sql.to_sql(res, "中国A股指数基本资料", con=conn_save, index=False, if_exists='replace')
# print("中国A股指数基本资料")
#
# # 获取【中国A股指数成份股】
# sql = "select * from AINDEXMEMBERS"
# res = Obtain_RDFData(sql)
# # 保存【中国A股指数成份股】
# pd.io.sql.to_sql(res, "中国A股指数成份股", con=conn_save, index=False, if_exists='replace')
# print("中国A股指数成份股")
#
#
# # 获取【中国A股指数日行情】-Part 1
# sql = "select S_INFO_WINDCODE, TRADE_DT, S_DQ_CLOSE, S_DQ_PCTCHANGE from AINDEXEODPRICES where TRADE_DT<='20180101'"
# res = Obtain_RDFData(sql)
# # 保存【中国A股指数日行情】
# pd.io.sql.to_sql(res, "中国A股指数日行情", con=conn_save, index=False, if_exists='replace')
# print("中国A股指数日行情")
#
# # 获取【中国A股指数日行情】-Part 2
# sql = "select S_INFO_WINDCODE, TRADE_DT, S_DQ_CLOSE, S_DQ_PCTCHANGE from AINDEXEODPRICES where TRADE_DT>'20180101'"
# res = Obtain_RDFData(sql)
# # 保存【中国A股指数日行情】
# pd.io.sql.to_sql(res, "中国A股指数日行情", con=conn_save, index=False, if_exists='append')
# print("中国A股指数日行情")
#
#
# # 获取【中国A股Wind行业指数日行情】
# sql = "select S_INFO_WINDCODE,TRADE_DT,S_DQ_CLOSE,S_DQ_PCTCHANGE from AINDEXWINDINDUSTRIESEOD"
# res = Obtain_RDFData(sql)
# # 保存【中国A股Wind行业指数日行情】
# pd.io.sql.to_sql(res, "中国A股Wind行业指数日行情", con=conn_save, index=False, if_exists='replace')
# print("中国A股Wind行业指数日行情")
#
#
# # 获取【中国A股万得指数成份股】
# sql = "select * from AINDEXMEMBERSWIND"
# res = Obtain_RDFData(sql)
# # 保存【中国A股万得指数成份股】
# pd.io.sql.to_sql(res, "中国A股万得指数成份股", con=conn_save, index=False, if_exists='replace')
# print("中国A股万得指数成份股")


"""
中国A股-指数衍生数据
"""
#
# # 获取【中国A股指数估值数据】
# # 预测类估值指标暂未提取
# sql = "select S_INFO_WINDCODE, TRADE_DT, CON_NUM, PE_TTM, PB_LF, PCF_TTM,PS_TTM, DIVIDEND_YIELD, TURNOVER, TURNOVER_FREE from AINDEXVALUATION"
# res = Obtain_RDFData(sql)
# # 保存【中国A股指数估值数据】
# pd.io.sql.to_sql(res, "中国A股指数估值数据", con=conn_save, index=False, if_exists='replace')
# print("中国A股指数估值数据")
#
# # 获取【中国A股指数财务衍生指标】
# sql = "select * from AINDEXFINANCIALDERIVATIVE"
# res = Obtain_RDFData(sql)
# # 保存【中国A股指数财务衍生指标】
# pd.io.sql.to_sql(res, "中国A股指数财务衍生指标", con=conn_save, index=False, if_exists='replace')
# print("中国A股指数财务衍生指标")
#
# """
# 中国A股第三方数据 - 中证和上证
# """
# # 获取【沪深300指数成份日权重】
# sql = "select TRADE_DT,S_INFO_WINDCODE,S_CON_WINDCODE,I_WEIGHT as WEIGHT,I_WEIGHT_14 as WEIGHTFACTOR from AINDEXHS300CLOSEWEIGHT"
# res = Obtain_RDFData(sql)
# # 保存【沪深300指数成份日权重】
# pd.io.sql.to_sql(res, "沪深300指数成份日权重", con=conn_save, index=False, if_exists='replace')
# print("沪深300指数成份日权重")
#
# # 获取【中证500指数成份日权重】
# sql = "select TRADE_DT, S_INFO_WINDCODE,S_CON_WINDCODE,WEIGHT,WEIGHTFACTOR from AINDEXCSI500WEIGHT"
# res = Obtain_RDFData(sql)
# # 保存【中证500指数成份日权重】
# pd.io.sql.to_sql(res, "中证500指数成份日权重", con=conn_save, index=False, if_exists='replace')
# print("中证500指数成份日权重")
#
# # 获取【中证800指数成份日权重】
# sql = "select TRADE_DT, S_INFO_WINDCODE,S_CON_WINDCODE,WEIGHT,WEIGHTFACTOR from AINDEXCSI800WEIGHT"
# res = Obtain_RDFData(sql)
# # 保存【中证800指数成份日权重】
# pd.io.sql.to_sql(res, "中证800指数成份日权重", con=conn_save, index=False, if_exists='replace')
# print("中证800指数成份日权重")
#
# # 获取【中证100指数成份日权重】
# sql = "select TRADE_DT, S_INFO_WINDCODE,S_CON_WINDCODE,WEIGHT,WEIGHTFACTOR from AINDEXCSI100WEIGHT"
# res = Obtain_RDFData(sql)
# # 保存【中证100指数成份日权重】
# pd.io.sql.to_sql(res, "中证100指数成份日权重", con=conn_save, index=False, if_exists='replace')
# print("中证100指数成份日权重")
#
# # 获取【中证1000指数成份日权重】
# sql = "select TRADE_DT, S_INFO_WINDCODE,S_CON_WINDCODE,WEIGHT,WEIGHTFACTOR from AINDEXCSI1000WEIGHT"
# res = Obtain_RDFData(sql)
# # 保存【中证1000指数成份日权重】
# pd.io.sql.to_sql(res, "中证1000指数成份日权重", con=conn_save, index=False, if_exists='replace')
# print("中证1000指数成份日权重")
#
# # 获取【上证50指数成份日权重】
# sql = "select TRADE_DT, S_INFO_WINDCODE,S_CON_WINDCODE,WEIGHT,WEIGHTFACTOR from AINDEXSSE50WEIGHT"
# res = Obtain_RDFData(sql)
# # 保存【上证50指数成份日权重】
# pd.io.sql.to_sql(res, "上证50指数成份日权重", con=conn_save, index=False, if_exists='replace')
# print("上证50指数成份日权重")
#
"""
中国A股第三方数据 - 申万
"""
# # 获取【申万指数日行情】
# sql = "select S_INFO_WINDCODE, TRADE_DT ,S_DQ_CLOSE,S_VAL_PE,S_VAL_PB,S_VAL_MV from ASWSINDEXEOD"
# res = Obtain_RDFData(sql)
# # 保存【申万指数日行情】
# pd.io.sql.to_sql(res, "申万指数日行情", con=conn_save, index=False, if_exists='replace')
# print("申万指数日行情")
#
# # 获取【申万指数成份明细】
# sql = "select * from SWINDEXMEMBERS"
# res = Obtain_RDFData(sql)
# # 保存【申万指数成份明细】
# pd.io.sql.to_sql(res, "申万指数成份明细", con=conn_save, index=False, if_exists='replace')
# print("申万指数成份明细")
#
# # 获取【申万指数成份日权重】
# sql = "select TRADE_DT,S_INFO_WINDCODE,S_CON_WINDCODE,I_WEIGHT as WEIGHT from ASWSINDEXCLOSEWEIGHT"
# res = Obtain_RDFData(sql)
# # 保存【申万指数成份日权重】
# pd.io.sql.to_sql(res, "申万指数成份日权重", con=conn_save, index=False, if_exists='replace')
# print("申万指数成份日权重")
#
# # 获取【申万行业分类】
# sql = "select * from ASHARESWINDUSTRIESCLASS"
# res = Obtain_RDFData(sql)
# # 保存【申万行业分类】
# pd.io.sql.to_sql(res, "申万行业分类", con=conn_save, index=False, if_exists='replace')
# print("申万行业分类")
#
# # 获取【申万行业分类(2021版)】
# sql = "select * from ASHARESWNINDUSTRIESCLASS"
# res = Obtain_RDFData(sql)
# # 保存【申万行业分类(2021版)】
# pd.io.sql.to_sql(res, "申万行业分类(2021版)", con=conn_save, index=False, if_exists='replace')
# print("申万行业分类(2021版)")
#
# # 获取【行业代码】
# sql = "select * from ASHAREINDUSTRIESCODE"
# res = Obtain_RDFData(sql)
# # 保存【行业代码】
# pd.io.sql.to_sql(res, "行业代码", con=conn_save, index=False, if_exists='replace')
# print("行业代码")
#
"""
中国A股第三方数据 - 中信
"""
# # 获取【中信指数日行情】
# sql = "select S_INFO_WINDCODE, TRADE_DT ,S_DQ_CLOSE,S_DQ_PCTCHANGE from AINDEXINDUSTRIESEODCITICS"
# res = Obtain_RDFData(sql)
# # 保存【中信指数日行情】
# pd.io.sql.to_sql(res, "中信指数日行情", con=conn_save, index=False, if_exists='replace')
# print("中信指数日行情")
#
# # 获取【中信指数成份明细】
# sql = "select * from AINDEXMEMBERSCITICS"
# res = Obtain_RDFData(sql)
# # 保存【中信指数成份明细】
# pd.io.sql.to_sql(res, "中信指数成份明细", con=conn_save, index=False, if_exists='replace')
# print("中信指数成份明细")
#
# # 缺少【中信指数成分日度权重】表
#
# # 获取【中信行业分类】
# sql = "select * from ASHAREINDUSTRIESCLASSCITICS"
# res = Obtain_RDFData(sql)
# # 保存【中信行业分类】
# pd.io.sql.to_sql(res, "中信行业分类", con=conn_save, index=False, if_exists='replace')
# print("中信行业分类")

"""
债券指数
"""
# # 获取【中国债券指数基本资料】
# sql = "select * from CBINDEXDESCRIPTION"
# res = Obtain_RDFData(sql)
# # 保存【中国债券指数基本资料】
# pd.io.sql.to_sql(res, "中国债券指数基本资料", con=conn_save, index=False, if_exists='replace')
# print("中国债券指数基本资料")
#
# # 获取【中国债券指数日行情】
# sql = "select S_INFO_WINDCODE, TRADE_DT, S_DQ_CLOSE, S_DQ_PCTCHANGE from CBINDEXEODPRICES"
# res = Obtain_RDFData(sql)
# # 保存【中国债券指数日行情】
# pd.io.sql.to_sql(res, "中国债券指数日行情", con=conn_save, index=False, if_exists='replace')
# print("中国债券指数日行情")
#
# # 获取【中国债券指数成分】
# sql = "select * from CBINDEXMEMBERS"
# res = Obtain_RDFData(sql)
# # 保存【中国债券指数成分】
# pd.io.sql.to_sql(res, "中国债券指数成分", con=conn_save, index=False, if_exists='replace')
# print("中国债券指数成分")
#
# # 获取【中国债券指数权重】
# sql = "select * from CBINDEXWEIGHT"
# res = Obtain_RDFData(sql)
# # 保存【中国债券指数权重】
# pd.io.sql.to_sql(res, "中国债券指数权重", con=conn_save, index=False, if_exists='replace')
# print("中国债券指数权重")
#
# # 获取【中证全债指数参数】
# sql = "select * from CSITOTALBONDINDEEODPRICE"
# res = Obtain_RDFData(sql)
# # 保存【中证全债指数参数】
# pd.io.sql.to_sql(res, "中证全债指数参数", con=conn_save, index=False, if_exists='replace')
# print("中证全债指数参数")

"""
基金指数
"""
# 获取【中国共同基金指数基本资料】
sql = "select * from CMFINDEXDESCRIPTION"
res = Obtain_RDFData(sql)
# 保存【中国共同基金指数基本资料】
pd.io.sql.to_sql(res, "中国共同基金指数基本资料", con=conn_save, index=False, if_exists='replace')
print("中国共同基金指数基本资料")

# 获取【中国共同基金指数行情】
sql = "select S_INFO_WINDCODE, TRADE_DT, S_DQ_CLOSE from CMFINDEXEOD"
res = Obtain_RDFData(sql)
# 保存【中国共同基金指数行情】
pd.io.sql.to_sql(res, "中国共同基金指数行情", con=conn_save, index=False, if_exists='replace')
print("中国共同基金指数行情")

# 暂时更新到这里，后续如需添加再说
conn_save.close()


