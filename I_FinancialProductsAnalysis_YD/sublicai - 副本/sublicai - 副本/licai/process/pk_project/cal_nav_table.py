# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/11 11:25 
# @Author    : Wangyd5 
# @File      : cal_week_net_value_table
# @Project   : licai
# @Function  ：计算周度净值表
# --------------------------------
import pandas as pd

from database.read.read_py_base import PyReader
from process.module.preprocess_bank_table import select_product_info_cache
from process.util_cal.cal_multi_product_nav_index import CalWeekFreqNavData
from process.util_cal.process_net_value import nav_fill
from database.saver.licai_saver import ResDataSaver


if __name__ == '__main__':

    # 注意事项： end_date 可以往前调整多7天 fixme 可以修改bug
    begin_date = '20200101'
    end_date = '20231011'
    reader = PyReader()
    product_info = select_product_info_cache(end_date='20230914',state=1)
    # product_info = pd.read_csv(r'M:\Device\C\Users\csc23998\sublicai\licai\docs\xh.csv')
    code_list = product_info['FinProCode'].tolist()
    code_list = [x for x in code_list if str(x) !='nan']
    week_nav_df = pd.DataFrame()

    for i, cp_id in enumerate(code_list):
        try:
            print(i, cp_id)
            # cp_id = 1209423
            net_value = reader.get_net_value(cp_id=cp_id,begin_date=begin_date,end_date=end_date)
            df_new = nav_fill(net_value)
            if df_new.empty:
                continue
            tmp_res = CalWeekFreqNavData(net_value=df_new[['FinProCode', 'trade_dt', 'net_value']])
            week_nav_df = week_nav_df.append(tmp_res)
        except:
            pass

    week_nav_df['FinProCode'] = week_nav_df['FinProCode'].map(int)
    week_nav_df.columns = ['FinProCode','trade_dt',  'net_value']
    week_nav_df.to_csv('net_value.csv')

    saver = ResDataSaver()
    saver.save_week_nav(week_nav_df)

    # 人工
    data_pivot = pd.pivot_table(data=week_nav_df,index='FinProCode',columns='trade_dt',values='net_value')
    data_pivot.to_csv('net_value_for_pktool.csv')







