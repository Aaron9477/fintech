# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月25日14:42:08
# @Author    : Noah Zhan
# @File      : daixiao_comp_daixiaoproduct_info
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_代销产品概况_代销机构】和【底层数据_代销产品概况_代销机构_绘图】依赖表
# --------------------------------
import dateutil
import numpy as np
import pandas as pd
from data_process_codes.preprocess import exclude_mother_child_relation, preprocess
from sectorize import sectorize

def daixiao_comp_daixiaoproduct_info(start_date,end_date,df1,df2,result_type='single'):
    '''
    :function:生成【底层数据_代销产品概况_代销机构】依赖表
    :params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - result_type:str,数据生成的报表类型，取值有'single'(代表单个公司数据)，'licai_sector'(理财公司分版块),'daixiao_sector'(代销公司分版块)，'sector'(理财公司和代销机构都分版块)。
    :return:
        - 底层数据_代销产品概况_代销机构:【底层数据_代销产品概况_代销机构】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_代销产品概况_代销机构】依赖表, ",start_date,"到",end_date,"...")
    底层数据_代销产品概况_代销机构 = pd.DataFrame()
    date = end_date
    i = 1
    while date >= start_date:
        print(" -Processing date ",date)
        month_begin_date = date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
        df1_temp = preprocess(df1,month_begin_date)
        df2_temp = df2[(df2['代销开始日']<date)&(df2['代销结束日']>month_begin_date)]
        df3_temp = df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
        df3_temp['代销机构_copy'] = df3_temp['代销机构'].copy()
        df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系

        #根据result_type做数据修改
        df3_temp = sectorize(df3_temp,type=result_type)
        df4_temp = sectorize(df4_temp,type=result_type)
        #根据变量名称和column名字基本能看明白在算什么东西
        #先计算不剔除母子关系的情况（用数据df3_temp）
        底层数据_代销产品概况_代销机构_temp = pd.DataFrame(columns = ['日期','代销机构','是否剔除母子关系','准入管理人数','准入管理人数排名','代销产品数量','代销产品数量排名','第一大代销理财子代销产品数'])
        准入管理人数 = df3_temp.groupby('代销机构').apply(lambda x:np.average(x.groupby('代销机构_copy').apply(lambda y:len(y.drop_duplicates(subset='发行机构')))))
        底层数据_代销产品概况_代销机构_temp['准入管理人数'] = 准入管理人数
        底层数据_代销产品概况_代销机构_temp['代销机构'] = 准入管理人数.index
        底层数据_代销产品概况_代销机构_temp.index = 准入管理人数.index
        底层数据_代销产品概况_代销机构_temp['日期'] = date
        底层数据_代销产品概况_代销机构_temp['是否剔除母子关系'] = '否'
        底层数据_代销产品概况_代销机构_temp['准入管理人数排名'] = 底层数据_代销产品概况_代销机构_temp['准入管理人数'].rank(method='min',ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_代销机构_temp)))
        底层数据_代销产品概况_代销机构_temp['代销产品数量'] = df3_temp.groupby('代销机构').apply(lambda x:np.average(x.groupby('代销机构_copy').apply(lambda y:len(y.drop_duplicates(subset='RegistrationCode')))))
        底层数据_代销产品概况_代销机构_temp['代销产品数量排名'] = 底层数据_代销产品概况_代销机构_temp['代销产品数量'].rank(method='min',ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_代销机构_temp)))
        底层数据_代销产品概况_代销机构_temp['第一大代销理财子代销产品数'] = df3_temp.groupby('代销机构').apply(lambda x:np.average(x.groupby(['代销机构_copy','发行机构'])['产品登记编码'].agg(lambda x: len(x.unique())).unstack().apply(lambda x:x.max(),axis=1)))
        
        #计算剔除母子关系的情况（用数据df4_temp）计算几乎同上，除了是否剔除母子关系为“是”
        底层数据_代销产品概况_代销机构_temp2 = pd.DataFrame(columns = ['日期','代销机构','是否剔除母子关系','准入管理人数','准入管理人数排名','代销产品数量','代销产品数量排名','第一大代销理财子代销产品数'])
        准入管理人数 = df4_temp.groupby('代销机构').apply(lambda x:np.average(x.groupby('代销机构_copy').apply(lambda y:len(y.drop_duplicates(subset='发行机构')))))
        底层数据_代销产品概况_代销机构_temp2['准入管理人数'] = 准入管理人数
        底层数据_代销产品概况_代销机构_temp2['代销机构'] = 准入管理人数.index
        底层数据_代销产品概况_代销机构_temp2.index = 准入管理人数.index
        底层数据_代销产品概况_代销机构_temp2['日期'] = date
        底层数据_代销产品概况_代销机构_temp2['是否剔除母子关系'] = '是'
        底层数据_代销产品概况_代销机构_temp2['准入管理人数排名'] = 底层数据_代销产品概况_代销机构_temp2['准入管理人数'].rank(method='min',ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_代销机构_temp2)))
        底层数据_代销产品概况_代销机构_temp2['代销产品数量'] = df4_temp.groupby('代销机构').apply(lambda x:np.average(x.groupby('代销机构_copy').apply(lambda y:len(y.drop_duplicates(subset='RegistrationCode')))))
        底层数据_代销产品概况_代销机构_temp2['代销产品数量排名'] = 底层数据_代销产品概况_代销机构_temp2['代销产品数量'].rank(method='min',ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_代销机构_temp2)))
        底层数据_代销产品概况_代销机构_temp2['第一大代销理财子代销产品数'] = df4_temp.groupby('代销机构').apply(lambda x:np.average(x.groupby(['代销机构_copy','发行机构'])['产品登记编码'].agg(lambda x: len(x.unique())).unstack().apply(lambda x:x.max(),axis=1)))
        
        #合并数据
        底层数据_代销产品概况_代销机构 = pd.concat([底层数据_代销产品概况_代销机构,底层数据_代销产品概况_代销机构_temp,底层数据_代销产品概况_代销机构_temp2],axis=0)#合并不同时期的数据
        date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
        i= i+1
    # 底层数据_代销产品概况_代销机构.to_excel(path_outputdir+r'\底层数据_代销产品概况_代销机构.xlsx')
    return 底层数据_代销产品概况_代销机构


def daixiao_comp_daixiaoproduct_info_draw(start_date,end_date,df_daixiao_comp_daixiaoproduct_info):
    '''
    function:生成【底层数据_代销产品概况_代销机构_绘图】依赖表
    params:
        - start_date: datetime64，数据更新的开始时间;
        - end_date: datetime64，数据更新的截止时间;
        - df_daixiao_comp_daixiaoproduct_info: dataframe，通过daixiao_comp_daixiaoproduct_info()生成的结果数据。
    return:
        - 底层数据_代销产品概况_代销机构_绘图:【底层数据_代销产品概况_代销机构_绘图】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_代销产品概况_代销机构_绘图】依赖表, ",start_date,"到",end_date,"...")
    date = end_date
    i = 1
    底层数据_代销产品概况_代销机构_绘图=pd.DataFrame()
    while date > start_date:
        print("processing date:",date)
        底层数据_代销产品概况_代销机构_绘图_temp = df_daixiao_comp_daixiaoproduct_info[df_daixiao_comp_daixiaoproduct_info['日期']==date][['日期','是否剔除母子关系','准入管理人数','准入管理人数排名','代销产品数量','代销产品数量排名']]
        底层数据_代销产品概况_代销机构_绘图_temp = 底层数据_代销产品概况_代销机构_绘图_temp.reset_index().set_index(['代销机构','是否剔除母子关系'])
        底层数据_代销产品概况_代销机构_绘图_temp.columns = 底层数据_代销产品概况_代销机构_绘图_temp.columns+str(i)
        if 底层数据_代销产品概况_代销机构_绘图.empty:
            底层数据_代销产品概况_代销机构_绘图 = 底层数据_代销产品概况_代销机构_绘图_temp
        else:
            底层数据_代销产品概况_代销机构_绘图 = pd.merge(底层数据_代销产品概况_代销机构_绘图,底层数据_代销产品概况_代销机构_绘图_temp,how='left',left_index=True,right_index=True).drop_duplicates()
        date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
        i = i + 1
    
    # 底层数据_代销产品概况_代销机构_绘图.to_excel(path_outputdir+"/底层数据_代销产品概况_代销机构_绘图.xlsx")
    # 底层数据_代销产品概况_代销机构_绘图 
    return 底层数据_代销产品概况_代销机构_绘图  

