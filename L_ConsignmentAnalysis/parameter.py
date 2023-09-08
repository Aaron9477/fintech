import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta
#全局变量设置
##数据路径
path_基本数据 = r'.\raw_datas\基础数据.xlsx'
path_代销数据 = r'.\raw_datas\代销数据.xlsx'
path_净值数据 = r'.\raw_datas\周度净值_均值处理_未筛选存续期.xlsx'
path_代销机构数据 = r'.\raw_datas\wind_bank_info_230628.csv'
path_现金管理类数据 = r'.\raw_datas\现金管理类_七日年化.xlsx'
path_all净值数据 = r'.\raw_datas\理财产品净值数据.csv'
path_周度日期 = r'.\raw_datas\周度日期.xlsx'
path_outputdir = r'.\output_dir'

##时间区间
end_date = dt.datetime(2023,7,31)#需要更新的数据结束时间（一般为最新时间）
start_date_month_start = dt.datetime(end_date.year,end_date.month,1)#需要更新的数据所在月的月初
start_date_ytd = dt.datetime(end_date.year,1,1)#需要更新的时间序列数据中年初至今的起始日期
start_date_1y= end_date-relativedelta(years=1)#需要更新的时间序列数据中近一年的起始日期
