# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/13 18:37 
# @Author    : Wangyd5 
# @File      : cal_bank_table
# @Project   : licai
# @Function  ：计算对比工具的第一个表 （要素+ 业绩指标）
# --------------------------------

from process.module.cal_non_cash_nav_net_value import cal_product_nav
from process.module.preprocess_bank_table import select_product_info_cache
from process.util_cal.process_net_value import representative

from database.read.read_py_base import PyReader
from process.util_cal.process_net_value import nav_fill
import pandas as pd
from tools.tools import Timer
from process.pk_project.cal_product_score import cal_rank

from process.util_cal.set_identify import *
from config.basic_variable import set_exist_dict
from database.saver.licai_saver import ResDataSaver
import traceback
import datetime
import numpy as np

if __name__ == '__main__':

    with Timer(True):
        begin_date = '20200101'
        end_date = '20230930'
        reader = PyReader()
        product_info = select_product_info_cache(end_date=end_date)
        # 计算存续状态
        product_info['state'] = 1
        index = (product_info['MaturityDate'] <= end_date) & (product_info['MaturityDate'].notnull())
        product_info.loc[index, 'state'] = 0
        # （1） 不计算2020-01-01以前结束的产品 （2） 非现金管理类
        product_info = product_info[(product_info['InvestmentType'] != '现金管理类') &
                                             ((product_info['MaturityDate'] > '2020-01-01') |
                                              (product_info['MaturityDate']).isnull())]



        # # 计算代表性产品标识
        # register_code_list = list(product_info['RegistrationCode'].unique())
        # valid_register_code_dict = {}
        # with Timer(True):
        #     for i, register_code in enumerate(register_code_list):
        #         print(i, register_code)
        #         # register_code = 'Z7000819A000048'
        #         tmp_nav_ser = representative(RegistrationCode=register_code, info=product_info)
        #         if len(tmp_nav_ser) > 1:
        #             valid_register_code_dict[register_code] = tmp_nav_ser.name
        #         else:
        #             continue
        # product_info['representative'] = product_info['FinProCode'].map(
        #     lambda x: 1 if x in list(valid_register_code_dict.values()) else 0)
        # # ------ 计算净值产品条件 ------
        # # （1） 不计算2020-01-01以前结束的产品 （2） 非现金管理类
        # product_nav_code_info = product_info[(product_info['InvestmentType'] != '现金管理类') &
        #                                      ((product_info['MaturityDate'] > '2020-01-01') |
        #                                       (product_info['MaturityDate']).isnull())]
        #
        # product_nav_code_info.to_csv(r'M:\Device\C\Users\csc23998\sublicai\licai\docs\product_nav_code_info.csv')

        product_info['representative'] = product_info['ProductType'].map(lambda x: 1 if x != '子产品' else 0)

        product_nav_code_info = product_info

        # 计算净值业绩
        code_list = product_nav_code_info['FinProCode'].tolist()
        result = pd.DataFrame()
        for i, cp_id in enumerate(code_list):
            try:
                print(i, cp_id)
                net_value = reader.get_net_value(cp_id=cp_id)
                df_new = nav_fill(net_value)
                if df_new.empty:
                    continue
                tmp_res = cal_product_nav(tmp_nav=df_new[['FinProCode', 'trade_dt', 'net_value']], finprocode=cp_id)
                result = result.append(tmp_res)

            except:
                print(traceback.format_exc())

        nv_indicator = pd.merge(product_info.set_index(['FinProCode'])[
                                    ['RegistrationCode', 'CompanyName', 'product_name', 'InvestmentType',
                                     'OperationType', 'open_type',
                                     'RaisingType', 'AssetValue']],
                                result, left_index=True, right_index=True, how='inner')

        nv_indicator = nv_indicator.reset_index()
        nv_indicator = nv_indicator.rename(columns={'index': 'FinProCode'})

        # a = 1/0
        # 进行分组计算得分
        # 参与排名条件：（1） 目前存续 （2） 是代表性产品
        representative_info = product_info[(product_info['representative'] == 1) & (product_info['state'] == 1)]
        repre_product_code_list = list(representative_info['FinProCode'].unique())
        nv_indicator = nv_indicator[nv_indicator['FinProCode'].isin(repre_product_code_list)].copy()


        # 筛选数据
        base_data = pd.merge(nv_indicator, product_info[['FinProCode', 'close_open']], on='FinProCode')
        base_data = base_data[base_data['close_open'] != '数据缺失']

        base_data = base_data.dropna(
            subset=['interval_ret_annual', 'max_draw_down', 'sharpe', 'InvestmentType', 'RaisingType',
                    'close_open']).copy()
        base_data = base_data.fillna('-')
        grouped = base_data.groupby(['InvestmentType', 'RaisingType', 'close_open'])
        score_df = pd.DataFrame([])
        for type, df in grouped:
            print(type)
            tmp_df = cal_rank(df)
            score_df = score_df.append(tmp_df)

        # 整合数据
        tmp_score = score_df[
            ['FinProCode', 'interval_ret_three_m', 'interval_ret_annual', 'max_draw_down', 'sharpe', 'rank_str']].copy()
        product_info = product_info.drop(['spec_lag', 'close_open', 'state', 'representative'], axis=1)

        data = pd.merge(product_info, tmp_score, on='FinProCode', how='left')
        data['open_rules'] = np.nan
        def adjust_date(date_item):
            if date_item is None:
                return
            elif isinstance(date_item,str):
                return date_item.replace('-','')
            elif isinstance(date_item,(int,float)):
                return None
            elif isinstance(date_item,(pd.Timestamp,datetime.date)):
                # 判断NaT:
                if pd.notna(date_item):
                    return date_item.strftime('%Y%m%d')
                else:
                    return None
            else:
                raise ValueError('date type goes wrong')

        def func(item):
            if isinstance(item, str):
                if item == "":
                    return None
                else:
                    return datetime.datetime.strptime(item, "%Y%m%d")
            elif isinstance(item, (int, float)):
                if item == 0:
                    return None
                elif np.isnan(item):
                    return None
                else:
                    return datetime.datetime.strptime(str(int(item)), "%Y%m%d")
            else:
                print(item)
                raise ValueError('data type goes wrong')


        data['open_rules'] = data['']
        data['EstablishmentDate'] = data['EstablishmentDate'].map(lambda x: adjust_date(x))
        data['report_date'] = data['report_date'].map(lambda x: adjust_date(x))

        data['EndDate'] = data['EndDate'].map(lambda x: adjust_date(x))
        data['PopularizeStDate'] = data['PopularizeStDate'].map(lambda x: adjust_date(x))
        data['product_establish_date'] = data['product_establish_date'].map(lambda x: adjust_date(x))
        data['MaturityDate'] = data['MaturityDate'].map(lambda x: adjust_date(x))

        data['EstablishmentDate'] = data['EstablishmentDate'].map(lambda x: func(x))
        data['PopularizeStDate'] = data['PopularizeStDate'].map(lambda x: func(x))
        data['EndDate'] = data['EndDate'].map(lambda x: func(x))
        data['product_establish_date'] = data['product_establish_date'].map(lambda x: func(x))
        data['MaturityDate'] = data['MaturityDate'].map(lambda x: func(x))
        data['report_date'] = data['report_date'].map(lambda x: func(x))

        # 增加系列识别
        data = get_set(data, set_exist_dict)
        data['ident_benchmark'] = data['Benchmark']
        data['benchmark_low'] = data['BenchmarkMin']
        data['benchmark_high'] = data['BenchmarkMax']

        data = data[['CompanyName', 'ParentCompName', 'ParentCompType', 'EstablishmentDate',
         'FinProCode', 'product_name', 'SecuState', 'PopularizeStDate',
         'MinInvestTimeType', 'RaisingType', 'OperationType', 'InvestmentType',
         'EndDate', 'AssetValue', 'ProductType', 'product_establish_date',
         'CurrencyUnit', 'SecuAbbr', 'MinInvestTerm', 'MinInvestTermUnit',
         'RiskLevel', 'Benchmark', 'BenchmarkMax', 'BenchmarkMin',
         'manage_fee_x', 'manage_fee_y', 'manage_fee_unit', 'carry_fee_x',
         'carry_fee_y', 'carry_fee_unit', 'MaturityDate', 'inv_type',
         'RegistrationCode', 'MinInvestDay', 'IfStructure', 'InvestTerm',
         'product_series', 'IssueObject_x', 'IssueObject_y', 'open_type',
         'product_object', 'fixed_income_upper', 'fixed_income_lower',
         'equity_upper', 'equity_lower', 'derivatives_upper',
         'derivatives_lower', 'invest_strategy', 'top_raise_scale',
         'actual_raise_scale', 'is_index', 'is_early_redeem', 'old_invest_scope',
         'report_date', 'product_type_son', 'asset_type', 'resource', 'interval_ret_three_m', 'interval_ret_annual',
         'max_draw_down', 'sharpe', 'rank_str', 'tag', 'set0', 'set',
         'ident_benchmark', 'benchmark_low', 'benchmark_high']]

        def convert_str_to_float(item):
            if isinstance(item,str):
                if item != '':
                    return float(item)
                else:
                    return None
            else:
                raise ValueError('data type goes wrong ......')

        data['AssetValue'] = data['AssetValue'].map(lambda x:convert_str_to_float(x))
        saver = ResDataSaver()
        saver.save_basic_info(data)
        data.to_csv('info.csv')
