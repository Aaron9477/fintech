import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
import pandas as pd
import numpy as np
from datetime import datetime
import sqlite3
from dateutil.relativedelta import relativedelta
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 参数配置
# =============================================================================
#季报截止日期
end_date = '20210630'
#考察季报数 近三年：12
num= 12
path_fund =  r"D:\work\database\DB_Fund.db"
path_save = r"D:\work\csc\公募基金分类与主题\基金分类结果.xlsx"
# =============================================================================
# 将数据连接到 DB Browser, 输入为下载所需要的sql语句
# =============================================================================
def Obtain_DBData(sql_str, path):
    conn = sqlite3.connect(path)
    data = pd.read_sql(sql_str,conn)
    return data
# =============================================================================
# 从数据库获取相关数据及预处理
# =============================================================================



query = "select * from '中国共同基金资产配置比例'"
asset_allocation = Obtain_DBData(query, path_fund)


query= "select * from '中国共同基金基本资料'"
basic_info = Obtain_DBData(query, path_fund)
rename = {'F_INFO_WINDCODE':"基金代码",'F_INFO_FULLNAME':"基金全称",'F_INFO_NAME':"基金简称",
          'F_INFO_CORP_FUNDMANAGEMENTCOMP':"基金公司",'F_INFO_SETUPDATE':'成立日期','F_INFO_BENCHMARK':'业绩基准',
          'F_INFO_TYPE':'运作类型','F_INFO_ISSUEDATE':'发行日期','F_INFO_INVESTSCOPE':'投资范围','F_INFO_INVESTOBJECT':'投资目标',
          'F_INFO_INVESTCONCEPTION':'投资理念','IS_INDEXFUND':'是否指数基金','RISK_RETURN':'风险收益特征'}
basic_info.rename(columns=rename,inplace=True)
basic_info = basic_info.set_index('基金代码')
basic_info['场外代码'] = basic_info.index.str.replace('.SZ','.OF').str.replace('.SH','.OF')
output = ['场外代码','基金全称',"基金简称","基金公司",'成立日期','业绩基准','投资范围','投资目标','投资理念','风险收益特征','是否指数基金']