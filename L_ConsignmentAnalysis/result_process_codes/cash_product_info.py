# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月21日10:40:37
# @Author    : Noah Zhan
# @File      : cash_product_info
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_现金管理类产品分析】依赖表和【底层数据_现金管理类产品七日年化收益率作图】依赖表
# --------------------------------


import dateutil
import numpy as np
import pandas as pd
from tqdm import tqdm
from data_process_codes.WeeklyYield_to_rangereturn import WeeklyYield_to_rangereturn
from data_process_codes.WeeklyYield_to_rangereturn_to_annulized import WeeklyYield_to_rangereturn_to_annulized
from data_process_codes.merge2cols_ues_col2_if_col1_empty import merge2cols_ues_col2_if_col1_empty

from data_process_codes.preprocess import exclude_mother_child_relation, preprocess
from data_process_codes.weighted_avg import weighted_avg, weighted_avg_2
from sectorize import sectorize

def cash_product_return_draw(start_date,end_date,df1:pd.DataFrame,df2,df9,if_sector = False):
    '''
    function:生成【底层数据_现金管理类产品七日年化收益率作图】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df9:dataframe，银行理财现金管理类产品产品的日度收益率数据;
        - if_sector:是否计算板块数据。
    return:
        - 底层数据_现金管理类产品七日年化收益率作图:【底层数据_现金管理类产品七日年化收益率作图】依赖表，用于更新理财图鉴。
    '''
    现金管理类_七日年化 = df9.copy()
    LatestWeeklyYield = 现金管理类_七日年化.set_index(['EndDate','FinProCode']).unstack()['LatestWeeklyYield']
    LatestWeeklyYield=LatestWeeklyYield.loc[:,LatestWeeklyYield.mean()>1]
    LatestWeeklyYield=LatestWeeklyYield.loc[:,LatestWeeklyYield.count()>50]
    LatestWeeklyYield=LatestWeeklyYield.interpolate()
    df1_temp = preprocess(df1,None,if_filter_exsist=False)
    df1_temp = df1_temp[df1_temp['InvestmentType']=='现金管理类']
    df2_temp = df2
    df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
    df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系
    if if_sector:
        df3_temp_licai_sector = sectorize(df3_temp,type='licai_sector')
        df4_temp_licai_sector = sectorize(df4_temp,type='licai_sector')
        df3_temp_daixiao_sector = sectorize(df3_temp,type='daixiao_sector')
        df4_temp_daixiao_sector = sectorize(df4_temp,type='daixiao_sector')
    else:
        df3_temp_licai_sector = df3_temp
        df4_temp_licai_sector = df4_temp
        df3_temp_daixiao_sector = df3_temp
        df4_temp_daixiao_sector = df4_temp
    #未剔除母子关系
    temp1_list=[]
    for jg_type in ['代销机构','发行机构']:
        if jg_type == '代销机构':
            df3_temp = df3_temp_daixiao_sector
        elif jg_type == '发行机构':
            df3_temp = df3_temp_licai_sector
        for (name,group) in tqdm(df3_temp.groupby(jg_type),desc = jg_type):
            codes = group[['RegistrationCode','FinProCode']].drop_duplicates(subset='RegistrationCode').dropna()['FinProCode']
            codes = codes[codes.isin(LatestWeeklyYield.columns)]
    #         wight = group[['RegistrationCode','AssetValue']].drop_duplicates(subset='RegistrationCode').dropna()['AssetValue']
            wight = group.loc[codes.index,'AssetValue']
            wight.index = codes
            if len(codes)>1:
                if jg_type=='发行机构':
                    temp = LatestWeeklyYield[codes].apply(lambda x:weighted_avg(x,wight),axis=1).rename((name))
                else:
                    temp = LatestWeeklyYield[codes].mean(axis=1).rename((name))
            elif len(codes)==1:
                temp = LatestWeeklyYield[codes].copy()
                temp.columns = [name]
            else:
                continue
            temp.loc['机构类型'] = jg_type
            temp1_list.append(temp)
    
    底层数据_七日年化收益率作图_temp1 = pd.concat(temp1_list,axis=1)
    if not if_sector:
        代销机构平均_temp1=底层数据_七日年化收益率作图_temp1.loc[:,底层数据_七日年化收益率作图_temp1.loc['机构类型',:]=='代销机构']
        代销机构平均_temp1=代销机构平均_temp1.iloc[:-2].mean(axis=1)
        代销机构平均_temp1.loc['机构类型']='代销机构'
        底层数据_七日年化收益率作图_temp1['代销机构平均']=代销机构平均_temp1
    底层数据_七日年化收益率作图_temp1.loc['是否剔除母子关系'] = '否'

    #剔除母子关系
    temp2_list=[]
    for jg_type in ['代销机构','发行机构']:
        if jg_type == '代销机构':
            df4_temp = df4_temp_daixiao_sector
        elif jg_type == '发行机构':
            df4_temp = df4_temp_licai_sector
        for (name,group) in tqdm(df4_temp.groupby(jg_type),desc = jg_type):
            codes = group[['RegistrationCode','FinProCode']].drop_duplicates(subset='RegistrationCode').dropna()['FinProCode']
            codes = codes[codes.isin(LatestWeeklyYield.columns)]
    #         wight = group[['RegistrationCode','AssetValue']].drop_duplicates(subset='RegistrationCode').dropna()['AssetValue']
            wight = group.loc[codes.index,'AssetValue']
            wight.index = codes
        #     print(LatestWeeklyYield[codes])
            if len(codes)>1:
                if jg_type=='发行机构':
                    temp = LatestWeeklyYield[codes].apply(lambda x:weighted_avg(x,wight),axis=1).rename((name))
                else:
                    temp = LatestWeeklyYield[codes].mean(axis=1).rename((name))
            elif len(codes)==1:
                temp = LatestWeeklyYield[codes].copy()
                temp.columns = [name]
            else:
                continue
            temp.loc['机构类型'] = jg_type
            temp2_list.append(temp)
    底层数据_七日年化收益率作图_temp2 = pd.concat(temp2_list,axis=1)
    if not if_sector:
        代销机构平均_temp2=底层数据_七日年化收益率作图_temp2.loc[:,底层数据_七日年化收益率作图_temp2.loc['机构类型',:]=='代销机构']
        代销机构平均_temp2=代销机构平均_temp2.iloc[:-2].mean(axis=1)
        代销机构平均_temp2.loc['机构类型']='代销机构'
        底层数据_七日年化收益率作图_temp2['代销机构平均']=代销机构平均_temp2
    
    底层数据_七日年化收益率作图_temp2.loc['是否剔除母子关系'] = '是'
    底层数据_七日年化收益率作图 = pd.concat([底层数据_七日年化收益率作图_temp1,底层数据_七日年化收益率作图_temp2],axis=1)
    #计算市场收益
    codes = df3_temp[['RegistrationCode','FinProCode']].drop_duplicates(subset='RegistrationCode').dropna()['FinProCode']
    codes = codes[codes.isin(LatestWeeklyYield.columns)]
    wight = df3_temp.loc[codes.index,'AssetValue']
    wight.index = codes
    底层数据_七日年化收益率作图['市场'] = LatestWeeklyYield.apply(lambda x:weighted_avg(x,wight),axis=1)
    # 底层数据_七日年化收益率作图.loc[['是否剔除母子关系']+list(底层数据_七日年化收益率作图.index[:-1]),:].to_excel(path_outputdir+"/底层数据_现金管理类产品七日年化收益率作图.xlsx")
    底层数据_七日年化收益率作图.loc['辅助',:]=底层数据_七日年化收益率作图.columns+底层数据_七日年化收益率作图.loc['是否剔除母子关系',:]
    底层数据_七日年化收益率作图=底层数据_七日年化收益率作图.loc[['是否剔除母子关系','辅助','机构类型']+list(底层数据_七日年化收益率作图.index[:-2]),:]
    return 底层数据_七日年化收益率作图


def cash_product_info(cash_product_info_draw):
    '''
    function:生成【底层数据_现金管理类产品分析】依赖表
    params:
        - cash_product_info_draw:pd.DataFrame,由cash_product_info_draw函数生成的数据。
    return:
        - 底层数据_现金管理类产品分析:【底层数据_现金管理类产品分析】依赖表，用于更新理财图鉴。
    '''
    底层数据_现金管理类产品 = pd.DataFrame()
    cash_product_info_draw=cash_product_info_draw.iloc[:-1,:]
    #计算各期限年化收益率和排名
    for if_exclud_mom_relation in ['是','否']:
        for jg_type in ['发行机构','代销机构']:
            cash_product_info_draw_temp = cash_product_info_draw.loc[:,(cash_product_info_draw.loc['是否剔除母子关系',:]==if_exclud_mom_relation)&(cash_product_info_draw.iloc[2,:]==jg_type)]
            result_temp = cash_product_info_draw_temp.iloc[3:,:].apply(WeeklyYield_to_rangereturn_to_annulized,length = 1,frequency = 1,axis=0).rename('近一周年化收益率').to_frame()
            result_temp['近一月年化收益率'] = cash_product_info_draw_temp.iloc[3:,:].apply(WeeklyYield_to_rangereturn_to_annulized,length = 4,frequency = 1,axis=0)
            result_temp['近三月年化收益率'] = cash_product_info_draw_temp.iloc[3:,:].apply(WeeklyYield_to_rangereturn_to_annulized,length = 13,frequency = 1,axis=0)
            result_temp['近半年年化收益率'] = cash_product_info_draw_temp.iloc[3:,:].apply(WeeklyYield_to_rangereturn_to_annulized,length = 26,frequency = 1,axis=0)
            result_temp['近一年年化收益率'] = cash_product_info_draw_temp.iloc[3:,:].apply(WeeklyYield_to_rangereturn_to_annulized,length = 52,frequency = 1,axis=0)
            result_temp['近一周年化收益率_排名'] = result_temp['近一周年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(result_temp['近一周年化收益率'].dropna())))
            result_temp['近一月年化收益率_排名'] = result_temp['近一月年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(result_temp['近一月年化收益率'].dropna())))
            result_temp['近三月年化收益率_排名'] = result_temp['近三月年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(result_temp['近三月年化收益率'].dropna())))
            result_temp['近半年年化收益率_排名'] = result_temp['近半年年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(result_temp['近半年年化收益率'].dropna())))
            result_temp['近一年年化收益率_排名'] = result_temp['近一年年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(result_temp['近一年年化收益率'].dropna())))
            result_temp['机构类型'] = cash_product_info_draw_temp.iloc[1,:]
            result_temp['是否剔除母子关系'] = cash_product_info_draw_temp.iloc[0,:]
            底层数据_现金管理类产品 = pd.concat([底层数据_现金管理类产品,result_temp],axis=0)
    return 底层数据_现金管理类产品

def cash_product_info_from_original(start_date,end_date,df1,df2,df9):
    '''
    function:生成【底层数据_产品甄选_理财公司】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df9:dataframe，银行理财现金管理类产品产品的日度收益率数据。
    return:
        - 底层数据_产品甄选_理财公司:【底层数据_产品甄选_理财公司】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_产品甄选_理财公司】依赖表, ",start_date,"到",end_date,"...")

    现金管理类_七日年化 = df9.copy()
    现金管理分析_字段计算 = pd.DataFrame(index=list(现金管理类_七日年化['FinProCode'].unique()))
    现金管理分析_字段计算['近一周年化收益率'] = 现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn_to_annulized,1)
    现金管理分析_字段计算['近一月年化收益率'] = 现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn_to_annulized,4)
    现金管理分析_字段计算['近三月年化收益率'] = 现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn_to_annulized,13)
    现金管理分析_字段计算['近半年年化收益率'] = 现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn_to_annulized,26)
    现金管理分析_字段计算['近一年收益率'] = 现金管理类_七日年化.groupby('FinProCode').apply(WeeklyYield_to_rangereturn_to_annulized,52)
    # 现金管理分析_字段计算['近一周年化收益率-排名'] = 现金管理分析_字段计算['近一周年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(现金管理分析_字段计算['近一周年化收益率'].dropna())))
    # 现金管理分析_字段计算['近一月年化收益率-排名'] = 现金管理分析_字段计算['近一月年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(现金管理分析_字段计算['近一月年化收益率'].dropna())))
    # 现金管理分析_字段计算['近三月年化收益率-排名'] = 现金管理分析_字段计算['近三月年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(现金管理分析_字段计算['近三月年化收益率'].dropna())))
    # 现金管理分析_字段计算['近半年年化收益率-排名'] = 现金管理分析_字段计算['近半年年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(现金管理分析_字段计算['近半年年化收益率'].dropna())))
    # 现金管理分析_字段计算['近一年收益率-排名'] = 现金管理分析_字段计算['近一年收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(现金管理分析_字段计算['近一年收益率'].dropna())))

    底层数据_现金管理类产品分析= pd.DataFrame()
    date = end_date
    i = 1
    while date >= start_date:
        print("Processing date ",date)
        #按照时间结点对数据进行处理
        for jg_type in ['代销机构','发行机构']:
            month_begin_date = date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
            df1_temp = preprocess(df1,month_begin_date,if_filter_exsist=False)
            df1_temp = df1_temp[df1_temp['InvestmentType']=='现金管理类']
            df1_temp['manage_fee'] = df1_temp[['manage_fee_y','manage_fee_x']].apply(merge2cols_ues_col2_if_col1_empty,axis=1)#新生成一列管理费，综合使用之前的两列数据
            df1_temp['二级分类'] = df1_temp[['固收增强分类_补充子产品','product_type_son']].apply(merge2cols_ues_col2_if_col1_empty,axis=1)#新生成一列二级分类，综合使用之前的两列数据
            df2_temp = df2[(df2['代销开始日']<date)&(df2['代销结束日']>month_begin_date)]
            df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
            df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系
            df3_temp = pd.merge(df3_temp,现金管理分析_字段计算,how='left',left_on='FinProCode',right_index=True)
            df4_temp = pd.merge(df4_temp,现金管理分析_字段计算,how='left',left_on='FinProCode',right_index=True)

            #先计算未剔除母子关系的数据
            底层数据_现金管理类产品分析_temp = pd.DataFrame()
            底层数据_现金管理类产品分析_temp['近一周年化收益率'] = df3_temp.groupby([jg_type]).apply(weighted_avg_2,'近一周年化收益率').rename('近一周年化收益率')
            底层数据_现金管理类产品分析_temp['近一月年化收益率'] = df3_temp.groupby([jg_type]).apply(weighted_avg_2,'近一月年化收益率').rename('近一月年化收益率')
            底层数据_现金管理类产品分析_temp['近三月年化收益率'] = df3_temp.groupby([jg_type]).apply(weighted_avg_2,'近三月年化收益率').rename('近三月年化收益率')
            底层数据_现金管理类产品分析_temp['近半年年化收益率'] = df3_temp.groupby([jg_type]).apply(weighted_avg_2,'近半年年化收益率').rename('近半年年化收益率')
            底层数据_现金管理类产品分析_temp['近一年收益率'] = df3_temp.groupby([jg_type]).apply(weighted_avg_2,'近一年收益率').rename('近一年收益率')
    #         底层数据_现金管理类产品分析_temp['现金管理类产品总规模'] = df3_temp.groupby([jg_type]).apply(weighted_avg_2,'近一年收益率').rename('近一年收益率')
            底层数据_现金管理类产品分析_temp['近一周年化收益率_排名'] = 底层数据_现金管理类产品分析_temp['近一周年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp['近一周年化收益率'].dropna())))
            底层数据_现金管理类产品分析_temp['近一月年化收益率_排名'] = 底层数据_现金管理类产品分析_temp['近一月年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp['近一月年化收益率'].dropna())))
            底层数据_现金管理类产品分析_temp['近三月年化收益率_排名'] = 底层数据_现金管理类产品分析_temp['近三月年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp['近三月年化收益率'].dropna())))
            底层数据_现金管理类产品分析_temp['近半年年化收益率_排名'] = 底层数据_现金管理类产品分析_temp['近半年年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp['近半年年化收益率'].dropna())))
            底层数据_现金管理类产品分析_temp['近一年收益率_排名'] = 底层数据_现金管理类产品分析_temp['近一年收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp['近一年收益率'].dropna())))
            底层数据_现金管理类产品分析_temp['日期'] = date
            底层数据_现金管理类产品分析_temp['是否剔除母子关系'] = '否'
            #计算剔除母子关系的数据
            底层数据_现金管理类产品分析_temp1 = pd.DataFrame()
            底层数据_现金管理类产品分析_temp1['近一周年化收益率'] = df4_temp.groupby([jg_type]).apply(weighted_avg_2,'近一周年化收益率').rename('近一周年化收益率')
            底层数据_现金管理类产品分析_temp1['近一月年化收益率'] = df4_temp.groupby([jg_type]).apply(weighted_avg_2,'近一月年化收益率').rename('近一月年化收益率')
            底层数据_现金管理类产品分析_temp1['近三月年化收益率'] = df4_temp.groupby([jg_type]).apply(weighted_avg_2,'近三月年化收益率').rename('近三月年化收益率')
            底层数据_现金管理类产品分析_temp1['近半年年化收益率'] = df4_temp.groupby([jg_type]).apply(weighted_avg_2,'近半年年化收益率').rename('近半年年化收益率')
            底层数据_现金管理类产品分析_temp1['近一年收益率'] = df4_temp.groupby([jg_type]).apply(weighted_avg_2,'近一年收益率').rename('近一年收益率')
            底层数据_现金管理类产品分析_temp1['近一周年化收益率_排名'] = 底层数据_现金管理类产品分析_temp1['近一周年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp1['近一周年化收益率'].dropna())))
            底层数据_现金管理类产品分析_temp1['近一月年化收益率_排名'] = 底层数据_现金管理类产品分析_temp1['近一月年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp1['近一月年化收益率'].dropna())))
            底层数据_现金管理类产品分析_temp1['近三月年化收益率_排名'] = 底层数据_现金管理类产品分析_temp1['近三月年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp1['近三月年化收益率'].dropna())))
            底层数据_现金管理类产品分析_temp1['近半年年化收益率_排名'] = 底层数据_现金管理类产品分析_temp1['近半年年化收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp1['近半年年化收益率'].dropna())))
            底层数据_现金管理类产品分析_temp1['近一年收益率_排名'] = 底层数据_现金管理类产品分析_temp1['近一年收益率'].rank(method='min',ascending=False).astype(str).apply(lambda x :x+"/"+str(len(底层数据_现金管理类产品分析_temp1['近一年收益率'].dropna())))
            底层数据_现金管理类产品分析_temp1['日期'] = date
            底层数据_现金管理类产品分析_temp1['是否剔除母子关系'] = '是'

            #合并数据
            底层数据_现金管理类产品分析_temp = 底层数据_现金管理类产品分析_temp.reset_index()
            底层数据_现金管理类产品分析_temp.rename(columns={jg_type: "机构"}, inplace=True)
            底层数据_现金管理类产品分析_temp1 = 底层数据_现金管理类产品分析_temp1.reset_index()
            底层数据_现金管理类产品分析_temp1.rename(columns={jg_type: "机构"}, inplace=True)
            底层数据_现金管理类产品分析 = pd.concat([底层数据_现金管理类产品分析,底层数据_现金管理类产品分析_temp,底层数据_现金管理类产品分析_temp1],axis=0,ignore_index=True)

        date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
        i= i+1
    # 底层数据_现金管理类产品分析.to_excel(path_outputdir+"/底层数据_现金管理类产品分析.xlsx")
    return 底层数据_现金管理类产品分析