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
DB_PWD = "jgbuser"
DB_NAME = "wande"
DB_PORT = '1433'

path_save = r"D:\gjl\database\DB_Stock.db"
conn_save = sqlite3.connect(path_save)
# conn_save = sqlite3.connect(r"D:\gjl\database\DB_Fund.db")
c = conn_save.cursor()

end_date = datetime.today()
dates_Q = pd.date_range('20171231', end_date, freq="Q-DEC")
dates_Q_str = dates_Q.map(lambda x: x.strftime('%Y%m%d'))
date_list_str = str(list(dates_Q_str))[1:-1]


############################################################################################################
# 定义从RDF下载原始数据表的函数， 输入为下载所需要的sql语句
def Obtain_RDFData(sql_str):
    engine = create_engine("mssql+pymssql://{}:{}@{}:{}/{}".format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME))
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


# 获取中国A股基本资料
sql_fund = "select * from ASHAREDESCRIPTION"
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【中国A股基本资料】
pd.io.sql.to_sql(res_fund_code, "中国A股基本资料", con=conn_save, index=False, if_exists='replace')
print("中国A股基本资料")

# 获取【香港股票基本资料】
sql_fund_info = "select * from HKSHAREDESCRIPTION "
res_fund_hk_info = Obtain_RDFData(sql_fund_info)
# 保存【香港股票基本资料】
pd.io.sql.to_sql(res_fund_hk_info, "香港股票基本资料", con=conn_save, index=False, if_exists='replace')
print("香港股票基本资料")

# 获取申万行业分类(2021版)
sql_fund = "select * from ASHARESWNINDUSTRIESCLASS"
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【申万行业分类(2021版)】
pd.io.sql.to_sql(res_fund_code, "申万行业分类(2021版)", con=conn_save, index=False, if_exists='replace')
print("申万行业分类(2021版)")

# 获取A股日行情估值指标
sql_fund = "select S_INFO_WINDCODE,TRADE_DT,S_VAL_MV,S_DQ_MV,S_VAL_PE_TTM,S_VAL_PB_NEW,S_VAL_PCF_OCFTTM from ASHAREEODDERIVATIVEINDICATOR where TRADE_DT in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【A股日行情估值指标】
pd.io.sql.to_sql(res_fund_code, "A股日行情估值指标", con=conn_save, index=False, if_exists='replace')
print("A股日行情估值指标")

# 获取A股TTM与MRQ
sql_fund = "select S_INFO_WINDCODE,REPORT_PERIOD,STATEMENT_TYPE,S_FA_ROE_TTM,FA_ROIC_TTM from ASHARETTMANDMRQ where STATEMENT_TYPE = '408001000'and REPORT_PERIOD in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【A股TTM与MRQ】
pd.io.sql.to_sql(res_fund_code, "A股TTM与MRQ", con=conn_save, index=False, if_exists='replace')
print("A股TTM与MRQ")
# 获取中国A股TTM指标历史数据
sql_fund = "select S_INFO_COMPCODE,S_INFO_WINDCODE,REPORT_PERIOD,STATEMENT_TYPE,S_FA_ROE_TTM,FA_ROIC_TTM,NET_PROFIT_TTM,S_FA_EBIT_TTM_INVERSE,S_FA_TOTALEQUITY_MRQ from ASHARETTMHIS where STATEMENT_TYPE = '合并报表'and REPORT_PERIOD in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【中国A股TTM指标历史数据】
pd.io.sql.to_sql(res_fund_code, "中国A股TTM指标", con=conn_save, index=False, if_exists='replace')
print("中国A股TTM指标")

# 获取中国A股财务指标
sql_fund = "select S_INFO_WINDCODE,REPORT_PERIOD,S_FA_YOYNETPROFIT,S_FA_YOY_TR,S_FA_YOYROE from ASHAREFINANCIALINDICATOR where REPORT_PERIOD in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【A股财务指标】
pd.io.sql.to_sql(res_fund_code, "A股财务指标", con=conn_save, index=False, if_exists='replace')
print("A股财务指标")

# Wind一致预测个股未来两年值
sql_fund = "select S_INFO_WINDCODE,EST_DT,ROLLING_TYPE,EST_PEG,EST_ROE from ASHARECONSENSUSROLLINGDATA where ROLLING_TYPE = 'FY2' and EST_DT in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【Wind一致预测个股未来两年平均增速】
pd.io.sql.to_sql(res_fund_code, "Wind一致预测个股未来两年值", con=conn_save, index=False, if_exists='replace')
print("Wind一致预测个股未来两年值")

# Wind一致预测个股未来两年平均增速
sql_fund = "select S_INFO_WINDCODE,EST_DT,ROLLING_TYPE,NET_PROFIT,EST_OPER_REVENUE,EST_ROE from ASHARECONSENSUSROLLINGDATA where ROLLING_TYPE = 'CAGR' and EST_DT in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【Wind一致预测个股未来两年平均增速】
pd.io.sql.to_sql(res_fund_code, "Wind一致预测个股未来两年平均增速", con=conn_save, index=False, if_exists='replace')
print("Wind一致预测个股未来两年平均增速")

# 获取港股日行情估值指标
sql_fund = "select S_INFO_WINDCODE,FINANCIAL_TRADE_DT TRADE_DT,S_VAL_MV,S_DQ_MV,S_VAL_PE_TTM,S_VAL_PB_NEW,S_VAL_PCF_OCFTTM from HKSHAREEODDERIVATIVEINDEX where FINANCIAL_TRADE_DT in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【港股日行情估值指标】
pd.io.sql.to_sql(res_fund_code, "港股日行情估值指标", con=conn_save, index=False, if_exists='replace')
print("港股日行情估值指标")

# 获取港股TTM与MRQ
sql_fund = "select S_INFO_COMPCODE,TRADE_DT,STATEMENT_TYPE,S_FA_ROE_TTM,FA_ROIC_TTM from HKSHARETTMANDMRQ where STATEMENT_TYPE = '合并报表' and TRADE_DT in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【A股TTM与MRQ】
pd.io.sql.to_sql(res_fund_code, "港股TTM与MRQ", con=conn_save, index=False, if_exists='replace')
print("港股TTM与MRQ")

# 获取港股TTM指标历史数据
sql_fund = "select * from HKSHARETTMHIS where STATEMENT_TYPE = '合并报表' and TRADE_DT in ({})".format(date_list_str)
# sql_fund = "select S_INFO_COMPCODE,TRADE_DT,STATEMENT_TYPE,S_FA_ROE_TTM,FA_ROIC_TTM,NET_PROFIT_TTM,S_FA_EBIT_TTM_INVERSE from HKSHARETTMHIS where STATEMENT_TYPE = '合并报表'and TRADE_DT in ({})".format(date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【港股TTM指标历史数据】
pd.io.sql.to_sql(res_fund_code, "港股TTM指标", con=conn_save, index=False, if_exists='replace')
print("港股TTM指标")

# 获取港股资产负债表历史数据（报错）
# sql_fund = "select S_INFO_COMPCODE,REPORT_PERIOD,STATEMENT_TYPE,PARSH_INT,TOT_SHRHLDR_EQY,TOT_LIAB_EQY from HKGSDBALANCESHEET where STATEMENT_TYPE = '合并报表'and REPORT_PERIOD in ({})".format(
#     date_list_str)
# res_fund_code = Obtain_RDFData(sql_fund)
# # 保存【港股资产负债表历史数据】
# pd.io.sql.to_sql(res_fund_code, "港股资产负债表", con=conn_save, index=False, if_exists='replace')
# print("港股资产负债表")

# 获取香港股票财务衍生指标
sql_fund = "select S_INFO_COMPCODE,ENDDATE,STATEMENT_TYPE,YOYNETPROFIT,YOY_TR,YOYROE from HKSHAREFINANCIALDERIVATIVE where ENDDATE in ({})".format(
    date_list_str)
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【香港股票财务衍生指标】
pd.io.sql.to_sql(res_fund_code, "香港股票财务衍生指标", con=conn_save, index=False, if_exists='replace')
print("香港股票财务衍生指标")

# 获取【中国A股首次公开发行数据】
sql_fund = "select * from ASHAREIPO"
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【中国A股首次公开发行数据】
pd.io.sql.to_sql(res_fund_code, "中国A股首次公开发行数据", con=conn_save, index=False, if_exists='replace')
print("中国A股首次公开发行数据")

# 获取【IPO初步询价明细】
sql_fund = "select * from IPOINQUIRYDETAILS where ANN_DT >= '20200101'"
res_fund_code = Obtain_RDFData(sql_fund)
# 保存【IPO初步询价明细】
pd.io.sql.to_sql(res_fund_code, "IPO初步询价明细", con=conn_save, index=False, if_exists='replace')
print("IPO初步询价明细")

# 获取【A股网下机构获配统计】
sql_fund_tras = "select * from ASHAREPLACEMENTINFO where TRADE_DT >= '20200101'"
res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# 保存【A股网下机构获配统计】
pd.io.sql.to_sql(res_fund_bench_tras, "A股网下机构获配统计", con=conn_save, index=False, if_exists='replace')
print("A股网下机构获配统计")

# 获取【A股网下机构获配明细】
sql_fund_tras = "select * from ASHAREPLACEMENTDETAILS where TRADE_DT >= '20200101' and S_HOLDER_TYPE = '基金公司'"
res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# 保存【中国转型基金信息】
pd.io.sql.to_sql(res_fund_bench_tras, "A股网下机构获配明细", con=conn_save, index=False, if_exists='replace')
print("A股网下机构获配明细")

"""初次下载"""
# 获取【中国A股日行情】
sql_fund_tras = "select S_INFO_WINDCODE,TRADE_DT,S_DQ_ADJCLOSE,S_DQ_AVGPRICE,S_DQ_PCTCHANGE,S_DQ_TRADESTATUS from ASHAREEODPRICES where TRADE_DT >= '20080101'"
res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# 保存【中国A股日行情】
pd.io.sql.to_sql(res_fund_bench_tras, "中国A股日行情", con=conn_save, index=False, if_exists='replace')
print("中国A股日行情")

# # 获取【香港股票日行情】
sql_fund_tras = "select S_INFO_WINDCODE,TRADE_DT,S_DQ_ADJCLOSE,S_DQ_AVGPRICE from HKSHAREEODPRICES where TRADE_DT >= '20080101'"
res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# 保存【香港股票日行情】
pd.io.sql.to_sql(res_fund_bench_tras, "香港股票日行情", con=conn_save, index=False, if_exists='replace')
print("香港股票日行情")

# # 获取【香港股票日行情收益率】
sql_fund_tras = "select S_INFO_WINDCODE,TRADE_DT, PCT_CHANGE_D from HKSHAREYIELD where TRADE_DT >= '20080101'"
res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# 保存【香港股票日行情收益率】
pd.io.sql.to_sql(res_fund_bench_tras, "香港股票日行情收益率", con=conn_save, index=False, if_exists='replace')
print("香港股票日行情收益率")


"""二次更新"""
# # 先删除日期数据可能会继续更新的数据表，然后重新下载更新 收盘数据保存到20211231
# c.execute("delete from '中国A股日行情' where TRADE_DT > '20211231'")
# print('20211231后中国A股日行情已删除')
# c.execute("delete from '香港股票日行情' where TRADE_DT > '20211231'")
# print('20211231后香港股票日行情已删除')
# c.execute("delete from '香港股票日行情收益率' where TRADE_DT > '20211231'")
# print('20211231后香港股票日行情已删除')
# conn_save.commit()
#
# # 获取【中国A股日行情】
# sql_fund_tras = "select S_INFO_WINDCODE,TRADE_DT,S_DQ_ADJCLOSE,S_DQ_AVGPRICE,S_DQ_PCTCHANGE,S_DQ_TRADESTATUS from ASHAREEODPRICES where TRADE_DT >= '20211231'"
# res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# # 保存【中国A股日行情】
# pd.io.sql.to_sql(res_fund_bench_tras, "中国A股日行情", con=conn_save, index=False, if_exists='append')
# print("中国A股日行情")
#
# # 获取【香港股票日行情】
# sql_fund_tras = "select S_INFO_WINDCODE,TRADE_DT,S_DQ_ADJCLOSE,S_DQ_AVGPRICE from HKSHAREEODPRICES where TRADE_DT >= '20211231'"
# res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# # 保存【香港股票日行情】
# pd.io.sql.to_sql(res_fund_bench_tras, "香港股票日行情", con=conn_save, index=False, if_exists='append')
# print("香港股票日行情")
#
# # # 获取【香港股票日行情收益率】
# sql_fund_tras = "select S_INFO_WINDCODE,TRADE_DT, PCT_CHANGE_D from HKSHAREYIELD where TRADE_DT >= '20211231'"
# res_fund_bench_tras = Obtain_RDFData(sql_fund_tras)
# # 保存【香港股票日行情收益率】
# pd.io.sql.to_sql(res_fund_bench_tras, "香港股票日行情收益率", con=conn_save, index=False, if_exists='append')
# print("香港股票日行情收益率")

conn_save.close()

