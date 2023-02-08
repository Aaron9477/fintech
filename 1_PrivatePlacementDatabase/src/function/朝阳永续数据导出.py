# -*- coding: utf-8 -*-
import pymysql
import pandas as pd
config = {
 'host': '106.75.45.237',
 'port': 50007,
 'user': 'simu4_zxjt',
 'password': 'MAJGcOUiCSUwmYUR',
 'db': 'CUS_FUND_DB',
 'charset':'utf8',
 'cursorclass':pymysql.cursors.DictCursor,
 }
conn = pymysql.connect(**config)
#sqi这句里面的日期每周变更
sql="SELECT fund_id,fund_name,swanav,statistic_date FROM v_t_fund_nv_data_zyyx WHERE statistic_date='20220708' "
cur = conn.cursor() 
cur.execute(sql) 
data = pd.DataFrame(cur.fetchall(), columns = [col[0] for col in cur.description]) 

#这个地方填充一个能找得到的路径
data.to_excel('朝阳永续净值.xlsx')
