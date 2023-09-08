# %%
import pandas as pd
from daixiao_comp_product_shelves_paint import \
    daixiao_comp_product_shelves_paint
from licai_comp_product_shelves_paint import licai_comp_product_shelves_paint

navs=pd.concat([pd.read_csv(r".\raw_datas\理财产品净值数据-普益1.csv"),pd.read_csv(r".\raw_datas\理财产品净值数据-普益2.csv")])
navs.to_csv(r".\raw_datas\理财产品净值数据.csv")



# %%
import sys

sys.path.append('data_process_codes')
sys.path.append('result_process_codes')
sys.path.append('raw_datas')
sys.path.append('output_dir')
import numpy as np
import pandas as pd
from parameter import *
# %%
from main_xianjinguanli_df9result import *
from main_first_累计净值填充 import *
from main_周度加权平均净值处理 import *

fill_accumulated_nav()
get_cash_annual_return()
weekly_average_nav()


# %%
df1 = pd.read_excel(path_基本数据,index_col=0)
df1['理财公司简称'] = df1.apply(lambda x:x[0].split('有限')[0],axis=1)
df2 = pd.read_excel(path_代销数据)
df2 = df2.rename(columns={'代销机构名称':'代销机构'})
df7 = pd.read_excel(path_净值数据,index_col=0).fillna(method='ffill',axis=1)
df8 = pd.read_csv(path_代销机构数据,encoding='utf-8').drop_duplicates(subset='comp_simple_name', keep='first', inplace=False)
df9 = pd.read_excel(path_现金管理类数据)
df9['EndDate'] = df9['EndDate'].astype('datetime64[ns]')

# 生成银行类型
from result_process_codes.daixiao_comp_basic_info import \
    daixiao_comp_basic_info

底层数据_代销机构基本信息 = daixiao_comp_basic_info(start_date_month_start,end_date,df2,df8)
df1 = pd.merge(df1,底层数据_代销机构基本信息[['comp_type']],how='left',left_on='ParentCompName',right_index=True)

import dateutil
import empyrical as emp
# %%
import numpy as np
from data_process_codes.preprocess import (exclude_mother_child_relation,
                                           preprocess)

df1['MaturityDate']=pd.to_datetime(df1['MaturityDate'])
df1['product_establish_date']=pd.to_datetime(df1['product_establish_date'])
#%%


# 生成用于检查的数据
month_begin_date = end_date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
df1_temp = preprocess(df1,end_date)

# 开始日在月末之前 且结束日在月初之后
df2_temp = df2[(df2['代销开始日']<end_date)&(df2['代销结束日']>month_begin_date)]
df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
df3_temp = df3_temp.drop(df3_temp [(df3_temp['MinInvestTimeType']=='数据缺失')|(df3_temp['MinInvestTimeType']=='其他')].index)#处理数据缺失的情况
df3_temp = df3_temp.dropna(subset=['MinInvestTimeType'])
df7_temp = df7.loc[:,df7.columns<end_date]
年化收益 = df7_temp.apply(lambda x:emp.annual_return((x/x.shift(1)-1).dropna(),annualization=52),axis=1).rename('年化收益').reset_index()
df3_temp = pd.merge(df3_temp,年化收益,how='left',on='FinProCode')
df3_temp.replace('其他半开型','封闭式',inplace = True)
df3_temp['发行机构_copy'] = df3_temp['发行机构'].copy()
df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系
df3_temp.to_excel(path_outputdir + '\用于检查的数据_未剔除母子关系.xlsx')
df4_temp.to_excel(path_outputdir + '\用于检查的数据_剔除母子关系.xlsx')

#%%
import xlwings as xw
from cash_product_info import *
from daixiao_comp_basic_info import daixiao_comp_basic_info
from daixiao_comp_daixiaoproduct_info import (
    daixiao_comp_daixiaoproduct_info, daixiao_comp_daixiaoproduct_info_draw)
from daixiao_comp_fixed_shalves import daixiao_comp_fixed_shalves
from daixiao_comp_gonggao_analysis import daixiao_comp_gonggao_analysis
from daixiao_comp_netvalue_analysis import daixiao_comp_netvalue_analysis
from daixiao_comp_product_recommendation import \
    daixiao_comp_product_recommendation
from daixiao_comp_product_shelves_info import daixiao_comp_product_shelves_info
from daixiao_comp_product_shelves_paint import daixiao_comp_product_shelves_paint
from hezuoproduct_num import hezuoproduct_num
from licai_comp_basic_info import licai_comp_basic_info
from licai_comp_daixiaoproduct_info import (
    licai_comp_daixiaoproduct_info, licai_comp_daixiaoproduct_info_draw)
from licai_comp_fixed_shalves import licai_comp_fixed_shalves
from licai_comp_gonggao_analysis import licai_comp_gonggao_analysis
from licai_comp_netvalue_analysis import licai_comp_netvalue_analysis
from licai_comp_product_recommendation import licai_comp_product_recommendation
from licai_comp_product_shelves_info import licai_comp_product_shelves_info
from netvalue_analysis_paint import netvalue_analysis_paint
from licai_comp_product_shelves_paint import licai_comp_product_shelves_paint
from product_fees import product_fees

underlying_sheets={}

#%%
#基本信息表
underlying_sheets['底层数据_理财公司基本信息'] = licai_comp_basic_info(start_date_month_start,end_date,df1.copy())
underlying_sheets['底层数据_代销机构基本信息'] = daixiao_comp_basic_info(start_date_month_start,end_date,df2.copy(),df8.copy())

#%%
#代销产品概况
底层数据_代销产品概况_理财公司 = pd.concat([licai_comp_daixiaoproduct_info(start_date_1y,end_date,df1.copy(),df2.copy()),#单机构数据
                                        licai_comp_daixiaoproduct_info(start_date_1y,end_date,df1.copy(),df2.copy(),result_type="licai_sector")],#板块数据
                                        axis=0)

underlying_sheets['底层数据_代销产品概况_理财公司']=底层数据_代销产品概况_理财公司[底层数据_代销产品概况_理财公司['日期']==end_date]

底层数据_代销产品概况_理财公司_temp = 底层数据_代销产品概况_理财公司.copy()
底层数据_代销产品概况_理财公司_temp.loc[:,['准入代销机构排名','被代销产品数排名','产品被代销次数排名']] = 底层数据_代销产品概况_理财公司[['准入代销机构排名','被代销产品数排名','产品被代销次数排名']].apply(lambda x:x.apply(lambda y:float(y.split('/')[0])),axis=0)
underlying_sheets['底层数据_代销产品概况_理财公司_绘图'] = licai_comp_daixiaoproduct_info_draw(start_date_1y,end_date,底层数据_代销产品概况_理财公司_temp)


底层数据_代销产品概况_代销机构= pd.concat([daixiao_comp_daixiaoproduct_info(start_date_1y,end_date,df1.copy(),df2.copy()),#单机构数据
                                        daixiao_comp_daixiaoproduct_info(start_date_1y,end_date,df1.copy(),df2.copy(),result_type="daixiao_sector")],#板块数据
                                        axis=0)
underlying_sheets['底层数据_代销产品概况_代销机构'] = 底层数据_代销产品概况_代销机构[底层数据_代销产品概况_代销机构['日期']==end_date]
底层数据_代销产品概况_代销机构_temp = 底层数据_代销产品概况_代销机构.copy()
底层数据_代销产品概况_代销机构_temp.loc[:,['准入管理人数排名','代销产品数量排名']] = 底层数据_代销产品概况_代销机构[['准入管理人数排名','代销产品数量排名']].apply(lambda x:x.apply(lambda y:float(y.split('/')[0])),axis=0)
underlying_sheets['底层数据_代销产品概况_代销机构_绘图'] = daixiao_comp_daixiaoproduct_info_draw(start_date_1y,end_date,底层数据_代销产品概况_代销机构_temp)

#合作产品数
underlying_sheets['底层数据_合作产品'] = pd.concat([hezuoproduct_num(start_date_month_start,end_date,df1.copy(),df2.copy()),#单机构数据
                            hezuoproduct_num(start_date_month_start,end_date,df1.copy(),df2.copy(),if_sector=True)],#板块数据
                            axis=0)
#%%
#代销产品货架
underlying_sheets['底层数据_代销产品货架_理财公司'] = pd.concat([licai_comp_product_shelves_info(start_date_ytd,end_date,df1.copy(),df2.copy(),df7.copy()),
                                        licai_comp_product_shelves_info(start_date_ytd,end_date,df1.copy(),df2.copy(),df7.copy(),result_type='licai_sector')],
                                        axis=0)

underlying_sheets['底层数据_代销产品货架_代销机构'] = pd.concat([daixiao_comp_product_shelves_info(start_date_ytd,end_date,df1.copy(),df2.copy(),df7.copy()),
                                        daixiao_comp_product_shelves_info(start_date_ytd,end_date,df1.copy(),df2.copy(),df7.copy(),result_type='daixiao_sector')],
                                        axis=0)

underlying_sheets['底层数据_代销产品货架_理财公司_绘图']=pd.concat([licai_comp_product_shelves_paint(start_date_ytd,end_date,df1.copy(),df2.copy(),result_type='single'),
licai_comp_product_shelves_paint(start_date_ytd,end_date,df1.copy(),df2.copy(),result_type='licai_sector')])

underlying_sheets['底层数据_代销产品货架_代销机构_绘图']=pd.concat([daixiao_comp_product_shelves_paint(start_date_ytd,end_date,df1.copy(),df2.copy(),result_type='single'),
daixiao_comp_product_shelves_paint(start_date_ytd,end_date,df1.copy(),df2.copy(),result_type='daixiao_sector')])



#%%
#固定收益类货架
underlying_sheets['底层数据_固定收益类货架_理财公司'] = pd.concat([licai_comp_fixed_shalves(start_date_month_start,end_date,df1.copy(),df2.copy(),df7.copy()),
                                        licai_comp_fixed_shalves(start_date_month_start,end_date,df1.copy(),df2.copy(),df7.copy(),result_type='licai_sector')],
                                        axis=0)
underlying_sheets['底层数据_固定收益类货架_代销机构'] = pd.concat([daixiao_comp_fixed_shalves(start_date_month_start,end_date,df1.copy(),df2.copy(),df7.copy()),
                                        daixiao_comp_fixed_shalves(start_date_month_start,end_date,df1.copy(),df2.copy(),df7.copy(),result_type='daixiao_sector')],
                                        axis=0)
#产品费率
underlying_sheets['底层数据_产品费率'] = pd.concat([product_fees(start_date_month_start,end_date,df1.copy(),df2.copy()),
                            product_fees(start_date_month_start,end_date,df1.copy(),df2.copy(),if_sector=True)],
                            axis=0)
#公告分析
底层数据_公告分析_理财公司_single = licai_comp_gonggao_analysis(start_date_month_start,df1.copy(),df2.copy(),df7.copy())
底层数据_公告分析_理财公司_sector = licai_comp_gonggao_analysis(start_date_month_start,df1.copy(),df2.copy(),df7.copy(),result_type='licai_sector')
underlying_sheets['底层数据_公告分析_理财公司']=pd.concat([底层数据_公告分析_理财公司_single,底层数据_公告分析_理财公司_sector])
底层数据_公告分析_代销机构_single = daixiao_comp_gonggao_analysis(start_date_month_start,df1.copy(),df2.copy(),df7.copy())
底层数据_公告分析_代销机构_sector = daixiao_comp_gonggao_analysis(start_date_month_start,df1.copy(),df2.copy(),df7.copy(),result_type='daixiao_sector')
underlying_sheets['底层数据_公告分析_代销机构']=pd.concat([底层数据_公告分析_代销机构_single,底层数据_公告分析_代销机构_sector])

#净值分析
underlying_sheets['底层数据_净值走势']=pd.concat([netvalue_analysis_paint(start_date_month_start,df1.copy(),df2.copy(),df7.copy(),result_type1='single',result_type2='single'),netvalue_analysis_paint(start_date_month_start,df1.copy(),df2.copy(),df7.copy(),result_type1='licai_sector',result_type2='daixiao_sector')],axis=1)
underlying_sheets['底层数据_净值指标_理财公司'] = pd.concat([licai_comp_netvalue_analysis(start_date_month_start,df1.copy(),df2.copy(),df7.copy(),result_type='single'),
        licai_comp_netvalue_analysis(start_date_month_start,df1.copy(),df2.copy(),df7.copy(),result_type='licai_sector')],
        axis=0)
underlying_sheets['底层数据_净值指标_代销机构'] = pd.concat([daixiao_comp_netvalue_analysis(start_date_month_start,df1.copy(),df2.copy(),df7.copy(),result_type='single'),
        daixiao_comp_netvalue_analysis(start_date_month_start,df1.copy(),df2.copy(),df7.copy(),result_type='daixiao_sector')],
        axis=0)
#现金管理类产品分析
底层数据_现金管理类产品七日年化收益率作图_single = cash_product_return_draw(start_date_month_start,end_date,df1.copy(),df2.copy(),df9.copy(),if_sector=False)
底层数据_现金管理类产品七日年化收益率作图_sector = cash_product_return_draw(start_date_month_start,end_date,df1.copy(),df2.copy(),df9.copy(),if_sector=True)
underlying_sheets['底层数据_现金管理类产品七日年化收益率作图'] = pd.concat([底层数据_现金管理类产品七日年化收益率作图_single.iloc[:,:-1],
                                                底层数据_现金管理类产品七日年化收益率作图_sector],
                                                axis=1)
underlying_sheets['底层数据_现金管理类产品分析'] = pd.concat([cash_product_info(底层数据_现金管理类产品七日年化收益率作图_single.iloc[:,:-1]),
                                    cash_product_info(底层数据_现金管理类产品七日年化收益率作图_sector.iloc[:,:-1])],
                                    axis=0)
#%%
#产品甄选
underlying_sheets['底层数据_产品甄选_理财公司'],产品特征1,p1=licai_comp_product_recommendation(start_date_month_start,end_date,df1.copy(),df2.copy(),df7.copy(),df9.copy())
underlying_sheets['底层数据_产品甄选_代销机构'],产品特征2,p2=daixiao_comp_product_recommendation(start_date_month_start,end_date,df1.copy(),df2.copy(),df7.copy(),df9.copy())
匹配__产品特征=pd.concat([产品特征1,产品特征2])
匹配__产品特征.drop_duplicates('FinProCode',inplace=True)
underlying_sheets['匹配__产品特征']=匹配__产品特征.fillna('-')


underlying_sheets['底层数据_产品甄选_理财公司'].to_excel("底层数据_产品甄选_理财公司.xlsx")
underlying_sheets['底层数据_产品甄选_代销机构'].to_excel("底层数据_产品甄选_代销机构.xlsx")
underlying_sheets['匹配__产品特征'].to_excel("匹配__产品特征.xlsx")


#%%
for sheet_name,data in underlying_sheets.items():
    data.to_excel(path_outputdir+'\\'+sheet_name+'.xlsx')
        
print("p1:{},p2:{}".format(p1,p2))

#%%
#输出
app = xw.App(visible=True,add_book=False)
template_file_path=r"a.xlsx"
wb_template=app.books.open(template_file_path)
for sheet_name,data in underlying_sheets:
    sheet_template =wb_template.sheets['sheet_name']
    with app.books.open(sheet_name+'.xlsx') as data_wb:
        data_sheet=data_wb.sheets[0]
        data_range=data_sheet.used_range
        target_range=sheet_template.range('A4')
        data_range.copy(target_range)