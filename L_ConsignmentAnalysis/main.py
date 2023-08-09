import datetime as dt

import pandas as pd

from result_process_codes.daixiao_comp_basic_info import daixiao_comp_basic_info
#全局变量设置
##数据路径
path_基本数据 = r'.\raw_datas\基础数据.xlsx'
path_代销数据 = r'.\raw_datas\代销数据0526.xlsx'
path_净值数据 = r'.\raw_datas\周度净值_均值处理.xlsx'
path_代销机构数据 = r'.\raw_datas\wind_bank_info_230628.csv'
path_现金管理类数据 = r'.\raw_datas\现金管理类_七日年化.xlsx'
path_all净值数据 = r'.\raw_datas\py_all_net_value_0704.csv'
path_周度日期 = r'.\raw_datas\周度日期20220101-20230630.xlsx'
path_outputdir = r'.\output_dir'

##常规数据时间区间
start_date = dt.datetime(2023,5,1)#需要更新的数据起始时间
end_date = dt.datetime(2023,5,31)#需要更新的数据结束时间（一般为最新时间）
##时序数据时间区间
start_date_ts = dt.datetime(2023,4,30)#需要更新的数据起始时间
end_date_ts = dt.datetime(2023,5,31)#需要更新的数据结束时间（一般为最新时间）

df1 = pd.read_excel(path_基本数据,index_col=0).infer_objects()
df1['理财公司简称'] = df1.apply(lambda x:x[0].split('有限')[0],axis=1)
df2 = pd.read_excel(path_代销数据)
df_date = pd.read_excel(path_周度日期)
df7 = pd.read_excel(path_净值数据,index_col=0).fillna(method='ffill',axis=1)
df8 = pd.read_csv(path_代销机构数据,encoding='utf-8').drop_duplicates(subset='comp_simple_name', keep='first', inplace=False)
df9 = pd.read_excel(path_现金管理类数据)
df9['EndDate'] = df9['EndDate'].astype('datetime64')

daixiao_comp_basic_info(start_date,end_date,df2,df8)