# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月20日16:51:18
# @Author    : Noah Zhan
# @File      : licai_comp_daixiaoproduct_info
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_代销产品概况_理财公司】和【底层数据_代销产品概况_理财公司_绘图】依赖表
# --------------------------------
import dateutil
import numpy as np
import pandas as pd
from data_process_codes.preprocess import exclude_mother_child_relation, preprocess
from sectorize import sectorize


def licai_comp_daixiaoproduct_info(start_date, end_date, df1, df2, result_type='single'):
    '''
    function:生成【底层数据_代销产品概况_理财公司】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表。
        - result_type:str,数据生成的报表类型，取值有'single'(代表单个公司数据)，'licai_sector'(理财公司分版块),'daixiao_sector'(代销公司分版块)，'sector'(理财公司和代销机构都分版块)。
    return:
        - 底层数据_代销产品概况_理财公司:【底层数据_代销产品概况_理财公司】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_代销产品概况_理财公司】依赖表, ", start_date, "到", end_date, "...")
    底层数据_代销产品概况_理财公司 = pd.DataFrame()
    date = end_date
    i = 1
    while date >= start_date:
        print(" -Processing date ", date)
        # 按照时间结点对数据进行处理
        month_begin_date = date - dateutil.relativedelta.relativedelta(
            months=1) + dateutil.relativedelta.relativedelta(days=1)  # 月初
        df1_temp = preprocess(df1, date)
        df2_temp = df2[(df2['代销开始日'] < date) & (
            df2['代销结束日'] > month_begin_date)]
        df3_temp = pd.merge(df1_temp, df2_temp, how='inner', left_on=[
                            'RegistrationCode', 'FinProCode'], right_on=['产品登记编码', '普益代码'])  # 合并匹配基础数据和代销数据
        df3_temp['发行机构_copy'] = df3_temp['发行机构'].copy()
        df1_temp['发行机构_copy'] = df1_temp['理财公司简称'].copy()
        df3_temp = df3_temp[df3_temp['发行机构'].str.contains('理财')]
        df4_temp = exclude_mother_child_relation(df3_temp)  # 剔除母子公司之间建立的代销关系

        # 根据result_type做数据修改
        df1_temp = sectorize(df1_temp, type=result_type)
        df3_temp = sectorize(df3_temp, type=result_type)
        df4_temp = sectorize(df4_temp, type=result_type)

        # 根据变量名称和column名字基本能看明白在算什么东西
        # 先计算不剔除母子关系的情况（用数据df3_temp）
        底层数据_代销产品概况_理财公司_temp = pd.DataFrame(columns=[
                                             '日期', '理财公司', '是否剔除母子关系', '准入代销机构数', '准入代销机构排名', '产品总数', '被代销产品数', '被代销产品数排名', '产品被代销次数', '产品被代销次数排名', '第一大代销机构代销次数'])
        准入代销机构数 = df3_temp.groupby('发行机构', group_keys=False).apply(lambda x: np.average(
            x.groupby('发行机构_copy').apply(lambda y: len(y.drop_duplicates(subset='代销机构')))))
        底层数据_代销产品概况_理财公司_temp['准入代销机构数'] = 准入代销机构数
        底层数据_代销产品概况_理财公司_temp['理财公司'] = 准入代销机构数.index
        底层数据_代销产品概况_理财公司_temp.index = 准入代销机构数.index
        底层数据_代销产品概况_理财公司_temp['日期'] = date
        底层数据_代销产品概况_理财公司_temp['是否剔除母子关系'] = '否'
        底层数据_代销产品概况_理财公司_temp['准入代销机构排名'] = 底层数据_代销产品概况_理财公司_temp['准入代销机构数'].rank(
            method='min', ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_理财公司_temp)))  # 对准入代销机构数排名
        底层数据_代销产品概况_理财公司_temp['产品总数'] = df1_temp.groupby('理财公司简称').apply(lambda x: np.average(x.groupby(
            '发行机构_copy').apply(lambda y: len(y.drop_duplicates(subset='RegistrationCode')))))  # 产品总数应该要用df1
        底层数据_代销产品概况_理财公司_temp['被代销产品数'] = df3_temp.groupby('发行机构').apply(lambda x: np.average(x.groupby(
            '发行机构_copy').apply(lambda y: len(y.drop_duplicates(subset='RegistrationCode')))))  # 被代销产品数用df3或df4
        底层数据_代销产品概况_理财公司_temp['被代销产品数排名'] = 底层数据_代销产品概况_理财公司_temp['被代销产品数'].rank(
            method='min', ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_理财公司_temp)))  # 对被代销产品数进行排名
        底层数据_代销产品概况_理财公司_temp['产品被代销次数'] = df3_temp.groupby('发行机构').apply(lambda x: np.average(x.groupby(
            '发行机构_copy').apply(lambda y: len(y.drop_duplicates(subset=['产品登记编码', '代销机构'])))))  # 一个登记编码和代销机构对应一次代销
        底层数据_代销产品概况_理财公司_temp['产品被代销次数排名'] = 底层数据_代销产品概况_理财公司_temp['产品被代销次数'].rank(
            method='min', ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_理财公司_temp)))
        底层数据_代销产品概况_理财公司_temp['第一大代销机构代销次数'] = df3_temp.groupby('发行机构').apply(lambda x: np.average(x.groupby(
            ['发行机构_copy', '代销机构'])['产品登记编码'].agg(lambda x: len(x.unique())).unstack().apply(lambda x: x.max(), axis=1)))
        
        # 计算剔除母子关系的情况（用数据df4_temp）计算几乎同上，除了是否剔除母子关系为“是”
        底层数据_代销产品概况_理财公司_temp2 = pd.DataFrame(
            columns=['日期', '理财公司', '是否剔除母子关系', '准入代销机构数', '准入代销机构排名', '产品总数', '被代销产品数', '被代销产品数排名', '产品被代销次数', '产品被代销次数排名', '第一大代销机构代销次数'])
        准入代销机构数 = df4_temp.groupby('发行机构').apply(lambda x: np.average(
            x.groupby('发行机构_copy').apply(lambda y: len(y.drop_duplicates(subset='代销机构')))))
        底层数据_代销产品概况_理财公司_temp2['准入代销机构数'] = 准入代销机构数
        底层数据_代销产品概况_理财公司_temp2['理财公司'] = 准入代销机构数.index
        底层数据_代销产品概况_理财公司_temp2.index = 准入代销机构数.index
        底层数据_代销产品概况_理财公司_temp2['日期'] = date
        底层数据_代销产品概况_理财公司_temp2['是否剔除母子关系'] = '是'
        底层数据_代销产品概况_理财公司_temp2['准入代销机构排名'] = 底层数据_代销产品概况_理财公司_temp2['准入代销机构数'].rank(
            method='min', ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_理财公司_temp2)))
        底层数据_代销产品概况_理财公司_temp2['产品总数'] = df1_temp.groupby('理财公司简称').apply(lambda x: np.average(
            x.groupby('发行机构_copy').apply(lambda y: len(y.drop_duplicates(subset='RegistrationCode')))))
        底层数据_代销产品概况_理财公司_temp2['被代销产品数'] = df4_temp.groupby('发行机构').apply(lambda x: np.average(
            x.groupby('发行机构_copy').apply(lambda y: len(y.drop_duplicates(subset='RegistrationCode')))))
        底层数据_代销产品概况_理财公司_temp2['被代销产品数排名'] = 底层数据_代销产品概况_理财公司_temp2['被代销产品数'].rank(
            method='min', ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_理财公司_temp2)))
        底层数据_代销产品概况_理财公司_temp2['产品被代销次数'] = df4_temp.groupby('发行机构').apply(lambda x: np.average(
            x.groupby('发行机构_copy').apply(lambda y: len(y.drop_duplicates(subset=['产品登记编码', '代销机构'])))))
        底层数据_代销产品概况_理财公司_temp2['产品被代销次数排名'] = 底层数据_代销产品概况_理财公司_temp2['产品被代销次数'].rank(
            method='min', ascending=False).apply(lambda x: str(x)+"/"+str(len(底层数据_代销产品概况_理财公司_temp2)))
        底层数据_代销产品概况_理财公司_temp2['第一大代销机构代销次数'] = df4_temp.groupby('发行机构').apply(lambda x: np.average(x.groupby(
            ['发行机构_copy', '代销机构'])['产品登记编码'].agg(lambda x: len(x.unique())).unstack().apply(lambda x: x.max(), axis=1)))
        # 合并数据
        底层数据_代销产品概况_理财公司 = pd.concat(
            [底层数据_代销产品概况_理财公司, 底层数据_代销产品概况_理财公司_temp, 底层数据_代销产品概况_理财公司_temp2], axis=0)  # 合并不同时期的数据
        date = end_date - \
            dateutil.relativedelta.relativedelta(months=i)  # date减一个月
        i = i+1
    return 底层数据_代销产品概况_理财公司
# 底层数据_代销产品概况_理财公司.to_excel(path_outputdir+r'\底层数据_代销产品概况_理财公司.xlsx')
# 底层数据_代销产品概况_理财公司


def licai_comp_daixiaoproduct_info_draw(start_date, end_date, df_licai_comp_daixiaoproduct_info):
    '''
    function:生成【底层数据_代销产品概况_理财公司_绘图】依赖表
    params:
        - start_date: datetime64，数据更新的开始时间;
        - end_date: datetime64，数据更新的截止时间;
        - df_licai_comp_daixiaoproduct_info: dataframe，通过licai_comp_daixiaoproduct_info()生成的结果数据。
    return:
        - 底层数据_代销产品概况_理财公司_绘图:【底层数据_代销产品概况_理财公司_绘图】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_代销产品概况_理财公司_绘图】依赖表, ", start_date, "到", end_date, "...")
    date = end_date
    i = 1
    底层数据_代销产品概况_理财公司_绘图 = pd.DataFrame()
    while date > start_date:
        print("processing date:", date)
        底层数据_代销产品概况_理财公司_绘图_temp = df_licai_comp_daixiaoproduct_info[df_licai_comp_daixiaoproduct_info['日期'] == date][[
            '日期', '是否剔除母子关系', '准入代销机构数', '准入代销机构排名', '产品被代销次数', '产品被代销次数排名']]
        底层数据_代销产品概况_理财公司_绘图_temp = 底层数据_代销产品概况_理财公司_绘图_temp.reset_index().set_index([
            '发行机构', '是否剔除母子关系'])
        底层数据_代销产品概况_理财公司_绘图_temp.columns = 底层数据_代销产品概况_理财公司_绘图_temp.columns + \
            str(i)
        if 底层数据_代销产品概况_理财公司_绘图.empty:
            底层数据_代销产品概况_理财公司_绘图 = 底层数据_代销产品概况_理财公司_绘图_temp
        else:
            底层数据_代销产品概况_理财公司_绘图 = pd.merge(底层数据_代销产品概况_理财公司_绘图, 底层数据_代销产品概况_理财公司_绘图_temp,
                                           how='left', left_index=True, right_index=True).drop_duplicates()
        date = end_date - \
            dateutil.relativedelta.relativedelta(months=i)  # date减一个月
        i = i + 1

    # 底层数据_代销产品概况_理财公司_绘图.to_excel(path_outputdir+"/底层数据_代销产品概况_理财公司_绘图.xlsx")
    # 底层数据_代销产品概况_理财公司_绘图
    return 底层数据_代销产品概况_理财公司_绘图
