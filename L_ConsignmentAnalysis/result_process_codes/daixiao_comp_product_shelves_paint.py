# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月24日14:29:51
# @Author    : Noah Zhan
# @File      : daixiao_comp_product_shelves_info
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_代销产品货架_代销机构】依赖表
# --------------------------------
import dateutil
import numpy as np
import pandas as pd
from data_process_codes.preprocess import exclude_mother_child_relation, preprocess
import empyrical as emp
from data_process_codes.sort_by_frequency_return_top_n_join_with_sign import sort_by_frequency_return_top_n_join_with_sign

from data_process_codes.weighted_avg import weighted_avg_2
from sectorize import sectorize
from parameter import *


def func11(x):
    # 计算达标率
    try:
        unique_data = x.drop_duplicates(subset='RegistrationCode').dropna()
        condition_met = unique_data['年化收益'] > (
            unique_data['BenchmarkMin'] * 0.01)
        ratio = condition_met.sum() / len(unique_data)
        return ratio
    except:
        return np.nan


def daixiao_comp_product_shelves_paint(start_date, end_date, df1, df2, result_type='single'):
    '''
    function:生成【底层数据_代销产品货架_代销机构】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df7:dataframe，银行理财产品产品的周度收益率数据;
        - result_type:str,数据生成的报表类型，取值有'single'(代表单个公司数据)，'licai_sector'(理财公司分版块),'daixiao_sector'(代销公司分版块)，'sector'(理财公司和代销机构都分版块)。
    return:
        - 底层数据_代销产品货架_代销机构:【底层数据_代销产品货架_代销机构】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_代销产品货架_代销机构_绘图】依赖表, ", start_date, "到", end_date, "...")

    date = end_date
    i = 1
    Investment_type_ts_dict_n = {}
    MinInvestTimeType_ts_dict_n = {}
    Investment_type_ts_dict_y={}
    MinInvestTimeType_ts_dict_y={}
    while date >= start_date:
        print(" -Processing date ", date)
        month_begin_date = date - dateutil.relativedelta.relativedelta(
            months=1) + dateutil.relativedelta.relativedelta(days=1)  # 月初
        df1_temp = preprocess(df1, month_begin_date)
        df2_temp = df2[(df2['代销开始日'] < date) & (
            df2['代销结束日'] > month_begin_date)]
        df3_temp = pd.merge(df1_temp, df2_temp, how='inner', left_on=[
                            'RegistrationCode', 'FinProCode'], right_on=['产品登记编码', '普益代码'])  # 合并匹配基础数据和代销数据
        df3_temp = df3_temp.drop(df3_temp[(df3_temp['MinInvestTimeType'] == '数据缺失') | (
            df3_temp['MinInvestTimeType'] == '其他')].index)  # 处理数据缺失的情况
        df3_temp = df3_temp.dropna(subset=['MinInvestTimeType'])
        df4_temp = exclude_mother_child_relation(df3_temp)  # 剔除母子公司之间建立的代销关系
        # 根据result_type做数据修改
        df3_temp = sectorize(df3_temp, type=result_type)
        df4_temp = sectorize(df4_temp, type=result_type)
        
        #不剔除
        Investment_type_ts_dict_n[date] = df3_temp.groupby(
            ['代销机构', 'InvestmentType'])['FinProCode'].count()
        Investment_type_ts_dict_y[date] = df4_temp.groupby(
            ['代销机构', 'InvestmentType'])['FinProCode'].count()
        
        MinInvestTimeType_ts_dict_n[date] = df3_temp.groupby(
            ['代销机构', 'MinInvestTimeType'])['FinProCode'].count()
        MinInvestTimeType_ts_dict_y[date] = df4_temp.groupby(
            ['代销机构', 'MinInvestTimeType'])['FinProCode'].count()

        date = end_date - \
            dateutil.relativedelta.relativedelta(months=i)  # date减一个月
        i = i+1

    Investment_type_ts_n = pd.concat(Investment_type_ts_dict_n).reset_index()
    Investment_type_ts_n = Investment_type_ts_n.rename(columns={'level_0': '日期'})
    Investment_type_ts_n = Investment_type_ts_n.pivot(
        index=['代销机构', '日期'], columns='InvestmentType')

    Investment_type_ts_y = pd.concat(Investment_type_ts_dict_y).reset_index()
    Investment_type_ts_y = Investment_type_ts_y.rename(columns={'level_0': '日期'})
    Investment_type_ts_y = Investment_type_ts_y.pivot(
        index=['代销机构', '日期'], columns='InvestmentType')

    MinInvestTimeType_ts_n = pd.concat(MinInvestTimeType_ts_dict_n).reset_index()
    MinInvestTimeType_ts_n = MinInvestTimeType_ts_n.rename(
        columns={'level_0': '日期'})
    MinInvestTimeType_ts_n = MinInvestTimeType_ts_n.pivot(
        index=['代销机构', '日期'], columns='MinInvestTimeType')
        
    MinInvestTimeType_ts_y = pd.concat(MinInvestTimeType_ts_dict_y).reset_index()
    MinInvestTimeType_ts_y = MinInvestTimeType_ts_y.rename(
        columns={'level_0': '日期'})
    MinInvestTimeType_ts_y = MinInvestTimeType_ts_y.pivot(
        index=['代销机构', '日期'], columns='MinInvestTimeType')

    
    底层数据_代销产品货架_代销机构_绘图_n = pd.concat(
        [Investment_type_ts_n, MinInvestTimeType_ts_n], axis=1)

    底层数据_代销产品货架_代销机构_绘图_n.columns = 底层数据_代销产品货架_代销机构_绘图_n.columns.droplevel(None)
    底层数据_代销产品货架_代销机构_绘图_n.rename(columns={'固定收益类': '固收非现金', '封闭短期': '封闭短期（一年内）', '封闭中期': '封闭中期（一年到三年）', '封闭长期': '封闭长期（三年以上）', '封闭长期': '封闭长期（三年以上）',
                                        '开放短期': '开放短期（一个月内）', '开放短中期': '开放短中期（一月到三月）', '开放中期': '开放中期（三月到半年）', '开放中长期': '开放中长期（半年到一年）', '开放长期': '开放长期（一年以上）'}, inplace=True)

    底层数据_代销产品货架_代销机构_绘图_n = 底层数据_代销产品货架_代销机构_绘图_n.loc[:,
                                                  ["现金管理类", "固收非现金", "混合类", "权益类", "商品及金融衍生品类",'封闭短期（一年内）', '封闭中期（一年到三年）', '封闭长期（三年以上）', '开放短期（一个月内）', '开放短中期（一月到三月）', '开放中期（三月到半年）', '开放中长期（半年到一年）', '开放长期（一年以上）']]

    底层数据_代销产品货架_代销机构_绘图_y =pd.concat(
        [Investment_type_ts_y, MinInvestTimeType_ts_y], axis=1) 

    底层数据_代销产品货架_代销机构_绘图_y.columns = 底层数据_代销产品货架_代销机构_绘图_y.columns.droplevel(None)
    底层数据_代销产品货架_代销机构_绘图_y.rename(columns={'固定收益类': '固收非现金', '封闭短期': '封闭短期（一年内）', '封闭中期': '封闭中期（一年到三年）', '封闭长期': '封闭长期（三年以上）', '封闭长期': '封闭长期（三年以上）',
                                        '开放短期': '开放短期（一个月内）', '开放短中期': '开放短中期（一月到三月）', '开放中期': '开放中期（三月到半年）', '开放中长期': '开放中长期（半年到一年）', '开放长期': '开放长期（一年以上）'}, inplace=True)
    if "权益类" not in 底层数据_代销产品货架_代销机构_绘图_y.columns:
        底层数据_代销产品货架_代销机构_绘图_y["权益类"]=np.nan
    底层数据_代销产品货架_代销机构_绘图_y = 底层数据_代销产品货架_代销机构_绘图_y.loc[:,
                                                  ["现金管理类", "固收非现金", "混合类", "权益类", "商品及金融衍生品类",'封闭短期（一年内）', '封闭中期（一年到三年）', '封闭长期（三年以上）', '开放短期（一个月内）', '开放短中期（一月到三月）', '开放中期（三月到半年）', '开放中长期（半年到一年）', '开放长期（一年以上）']]

    底层数据_代销产品货架_代销机构=pd.concat([底层数据_代销产品货架_代销机构_绘图_n,底层数据_代销产品货架_代销机构_绘图_y],keys=['否','是'],names=['是否剔除母子关系'],axis=1)
    # 一些处理
    return 底层数据_代销产品货架_代销机构
