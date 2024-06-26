# -*- coding: utf-8 -*-
"""
基金相关季频或基本信息数据库下载
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
path_save = r"D:\gjl\database\DB_Fund.db"
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

print("中国Wind基金分类")

# 获取Wind基金分类说明 【Wind基金分类中文说明】
sql_str = "select INDUSTRIESCODE S_INFO_SECTOR_All, INDUSTRIESNAME INDNAME, LEVELNUM L from ASHAREINDUSTRIESCODE where LEFT(INDUSTRIESCODE,4) = '2001' "
res = Obtain_RDFData(sql_str)
pd.io.sql.to_sql(res,"中国Wind基金分类_中文说明", con = conn_save, index = False, if_exists = 'replace')
print("中国Wind基金分类说明")


######################################################################################################
# 获取【中国共同基金基金经理】
sql_fund_manager = "select * from CHINAMUTUALFUNDMANAGER order by F_INFO_WINDCODE, F_INFO_MANAGER_STARTDATE"
res_fund_manager = Obtain_RDFData(sql_fund_manager)

# 保存【中国共同基金基金经理】
pd.io.sql.to_sql(res_fund_manager,"中国共同基金基金经理", con = conn_save,index = False, if_exists = 'replace')

print("中国共同基金基金经理")

#####################################################################################################
# 获取【中国共同基金基本资料】
# 增加了是否初始基金字段F_INFO_ISINITIAL
sql_fund_baseinfo = "select F_INFO_WINDCODE, F_INFO_FULLNAME, F_INFO_NAME, F_INFO_CORP_FUNDMANAGEMENTCOMP, F_INFO_FIRSTINVESTTYPE, F_INFO_SETUPDATE, \
                     F_INFO_MATURITYDATE, F_INFO_MANAGEMENTFEERATIO, F_INFO_CUSTODIANFEERATIO, F_INFO_PTMYEAR,  \
                     F_INFO_BENCHMARK, F_INFO_STATUS, F_INFO_FIRSTINVESTSTYLE, F_INFO_ISSUEDATE, F_INFO_TYPE, \
                     F_INFO_ISINITIAL, F_INFO_INVESTSCOPE, F_INFO_INVESTOBJECT, F_INFO_INVESTCONCEPTION, F_INFO_DECISION_BASIS, \
                     IS_INDEXFUND, F_INFO_DELISTDATE,RISK_RETURN from CHINAMUTUALFUNDDESCRIPTION order by F_INFO_WINDCODE"

res_fund_baseinfo = Obtain_RDFData(sql_fund_baseinfo)

# 保存【中国共同基金基本资料】
pd.io.sql.to_sql(res_fund_baseinfo,"中国共同基金基本资料", con = conn_save, index = False, if_exists = 'replace')

print("中国共同基金基本资料")

# 获取【中国共同基金投资品种比例信息】
sql_fund_assetpct = "select * from CMFPROPORTIONOFINVEOBJ order by S_INFO_WINDCODE"

res_fund_assetpct = Obtain_RDFData(sql_fund_assetpct)

# 保存【中国共同基金投资品种比例信息】
pd.io.sql.to_sql(res_fund_assetpct, "中国共同基金投资品种比例信息", con=conn_save, index=False, if_exists='replace')

######################################################################################################
# 获取【中国共同基金资产配置(%)】 ChinaMutualFundAssetPortfolio
sql_fund_assetpct = "select * from CHINAMUTUALFUNDASSETPORTFOLIO order by S_INFO_WINDCODE,F_PRT_ENDDATE"

res_fund_assetpct = Obtain_RDFData(sql_fund_assetpct)

# 保存【中国共同基金资产配置比例】
pd.io.sql.to_sql(res_fund_assetpct,"中国共同基金资产配置比例", con = conn_save, index = False, if_exists = 'replace')

print("中国共同基金资产配置比例")

######################################################################################################
# 获取【中国共同基金持券明细(%)】 ChinaMutualFundBondPortfolio
sql_fund_bondport = "select * from CHINAMUTUALFUNDBONDPORTFOLIO order by S_INFO_WINDCODE, F_PRT_ENDDATE"

res_fund_bondport = Obtain_RDFData(sql_fund_bondport)

# 保存【中国共同基金持券明细(%)】
pd.io.sql.to_sql(res_fund_bondport,"中国共同基金持券明细", con = conn_save, index = False, if_exists = 'replace')

print("中国共同基金持券明细")

# 获取【中国共同基金转型信息】
sql_fund_tras = "select * from CHINAMUTUALFUNDTRANSFORMATION"
res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# 保存【中国转型基金信息】
pd.io.sql.to_sql(res_fund_bench_tras, "中国共同基金转型信息", con=conn_save, index=False, if_exists='replace')
print("中国共同基金转型信息")

# #####################################################################################################
# 获取【中国共同基金业绩比较基准行情】
# sql_fund_benindex_pit = "select S_INFO_WINDCODE, TRADE_DT, S_DQ_CLOSE from CHINAMUTUALFUNDBENCHMARKEOD  \
#                           order by S_INFO_WINDCODE, TRADE_DT"
# res_fund_benindex_pit = Obtain_RDFData(sql_fund_benindex_pit)
# # 保存【中国共同基金基准净值】
# pd.io.sql.to_sql(res_fund_benindex_pit, "中国共同基金业绩比较基准行情", con=conn_save, index=False, if_exists='replace')
#
# print("中国共同基金业绩比较基准行情")

######################################################################################################
# 获取【中国共同基金业绩比较基准配置】
sql_fund_bench_desp = "select * from CHINAMUTUALFUNDBENCHMARK"
res_fund_bench_desp = Obtain_RDFData(sql_fund_bench_desp)

# 保存【中国共同基金业绩比较基准配置】
pd.io.sql.to_sql(res_fund_bench_desp, "中国共同基金业绩比较基准配置", con=conn_save, index=False, if_exists='replace')

print("中国共同基金业绩比较基准配置")


######################################################################################################
# 获取【中国共同基金行业配置(%)】 -证监会行业分类
sql_fund_indport = "select * from CHINAMUTUALFUNDINDPORTFOLIO order by S_INFO_WINDCODE, F_PRT_ENDDATE"

res_fund_indport = Obtain_RDFData(sql_fund_indport)

# 保存【中国共同基金行业配置(%)】
pd.io.sql.to_sql(res_fund_indport,"中国共同基金行业配置", con = conn_save, index = False, if_exists = 'replace')

print("中国共同基金行业配置")



######################################################################################################
# 获取【中国共同基金暂停申购赎回】 ChinaMutualFundSuspendPchRedm
sql_fund_SuspendPchRedm = "select * from CHINAMUTUALFUNDSUSPENDPCHREDM order by S_INFO_WINDCODE"

res_fund_SuspendPchRedm = Obtain_RDFData(sql_fund_SuspendPchRedm)

# 保存【中国共同基金暂停申购赎回】
pd.io.sql.to_sql(res_fund_SuspendPchRedm,"中国共同基金暂停申购赎回", con = conn_save, index = False, if_exists = 'replace')

print("中国共同基金暂停申购赎回")


######################################################################################################
# 获取【中国共同基金持有人结构】 CMFHolderStructure
sql_fund_CMFHolderStructure = "select * from CMFHOLDERSTRUCTURE order by S_INFO_WINDCODE"

res_fund_CMFHolderStructure = Obtain_RDFData(sql_fund_CMFHolderStructure)

# 保存【中国共同基金持有人结构】
pd.io.sql.to_sql(res_fund_CMFHolderStructure,"中国共同基金持有人结构", con = conn_save, index = False, if_exists = 'replace')

print("中国共同基金持有人结构")

# 获取【中国共同基金份额】ChinaMutualFundShare
sql_fund_MutualFundShare = "select * from CHINAMUTUALFUNDSHARE order by F_INFO_WINDCODE,CHANGE_DATE"

res_fund_MutualFundShare = Obtain_RDFData(sql_fund_MutualFundShare)

# 保存【中国共同基金份额】
pd.io.sql.to_sql(res_fund_MutualFundShare, "中国共同基金份额", con=conn_save, index=False, if_exists='replace')

print("中国共同基金份额")

#获取证证券代码关系表
sql_fund = "select * from RALATEDSECURITIESCODE"

res_fund_code = Obtain_RDFData(sql_fund)

# 保存【证券代码关系表】
pd.io.sql.to_sql(res_fund_code, "证券代码关系表", con=conn_save, index=False, if_exists='replace')

print("证券代码关系表")


# 获取【中国共同基金财务指标(报告期)】
sql_fund_nav = "select * from CMFFINANCIALINDICATOR"
sql_fund_nav = Obtain_RDFData(sql_fund_nav)
# res_sql_fund_nav = res_sql_fund_nav.append(sql_fund_nav)
pd.io.sql.to_sql(sql_fund_nav, "中国共同基金财务指标(报告期)", con=conn_save, index=False, if_exists='replace')
# 保存【中国共同基金财务指标(报告期)】
print("中国共同基金财务指标(报告期)")

# 获取【中国共同基金利润表】
sql_fund_nav = "select * from CMFINCOME"
sql_fund_nav = Obtain_RDFData(sql_fund_nav)
# res_sql_fund_nav = res_sql_fund_nav.append(sql_fund_nav)
pd.io.sql.to_sql(sql_fund_nav, "中国共同基金利润表", con=conn_save, index=False, if_exists='replace')
# 保存【中国共同基金利润表】
print("中国共同基金利润表")

# # 获取【中国基金公司十大股东】
sql_fund_nav = "select * from FUNDCOMPANYINSIDEHOLDER"
sql_fund_nav = Obtain_RDFData(sql_fund_nav)
pd.io.sql.to_sql(sql_fund_nav, "中国基金公司十大股东", con=conn_save, index=False, if_exists='replace')
# 保存【中国基金公司十大股东】
print("中国基金公司十大股东")

# # 获取【中国基金公司诚信记录】
sql_fund_nav = "select * from FUNDCREDITRECORD"
sql_fund_nav = Obtain_RDFData(sql_fund_nav)
pd.io.sql.to_sql(sql_fund_nav, "中国基金公司诚信记录", con=conn_save, index=False, if_exists='replace')
# 保存【中国基金公司诚信记录】
print("中国基金公司诚信记录")

# # 获取【中国基金公司管理层成员】
sql_fund_nav = "select * from CFUNDMANAGEMENT"
sql_fund_nav = Obtain_RDFData(sql_fund_nav)
pd.io.sql.to_sql(sql_fund_nav, "中国基金公司管理层成员", con=conn_save, index=False, if_exists='replace')
# 保存【中国基金公司管理层成员】
print("中国基金公司管理层成员")

# # 获取【基金公司申购赎回基金情况】
sql_fund_nav = "select * from CFUNDPCHREDMCMF"
sql_fund_nav = Obtain_RDFData(sql_fund_nav)
pd.io.sql.to_sql(sql_fund_nav, "基金公司申购赎回基金情况", con=conn_save, index=False, if_exists='replace')
# 保存【基金公司申购赎回基金情况】
print("基金公司申购赎回基金情况")


######################################################################################################

"""二次更新"""
#先删除日期数据可能会继续更新的数据表，然后重新下载更新 持股明细保存到20211231 净值数据保存到20211231
c.execute("delete from '中国共同基金持股明细' where F_PRT_ENDDATE > '20211231'")
print('20211231后中国共同基金持股明细已删除')

c.execute("delete from '中国共同基金净值' where TRADE_DT > '20211231'")
print('20211231后中国共同基金净值已删除')
conn_save.commit()


# 获取【中国共同基金持股明细(%)】 ChinaMutualFundStockPortfolio
sql_fund_stockport = "select * from CHINAMUTUALFUNDSTOCKPORTFOLIO  where F_PRT_ENDDATE > '20211231' order by S_INFO_WINDCODE, F_PRT_ENDDATE"
fund_stockport = Obtain_RDFData(sql_fund_stockport)
# res_fund_stockport = res_fund_stockport.append(fund_stockport)
pd.io.sql.to_sql(fund_stockport, "中国共同基金持股明细", con=conn_save, index=False, if_exists='append')
# 保存【中国共同基金持股明细(%)】
print("中国共同基金持股明细")


# 获取【中国共同基金净值】
# 日度日期重命名为TRADE_DT
sql_fund_nav = "select F_INFO_WINDCODE, PRICE_DATE TRADE_DT, F_NAV_ADJUSTED, F_PRT_NETASSET/POWER(10,8) F_PRT_NETASSET, \
                NETASSET_TOTAL/POWER(10,8) NETASSET_TOTAL from CHINAMUTUALFUNDNAV where PRICE_DATE > '20211231'"
sql_fund_nav = Obtain_RDFData(sql_fund_nav)
# res_sql_fund_nav = res_sql_fund_nav.append(sql_fund_nav)
pd.io.sql.to_sql(sql_fund_nav, "中国共同基金净值", con=conn_save, index=False, if_exists='append')
# 保存【中国共同基金净值】
print("中国共同基金净值")

conn_save.close()