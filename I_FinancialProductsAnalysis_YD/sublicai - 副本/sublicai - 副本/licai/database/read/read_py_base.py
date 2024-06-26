# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/10 17:38 
# @Author    : Wangyd5 
# @File      : read_py_base
# @Project   : licai
# @Function  ：读取普益基础数据
# --------------------------------

import os
from typing import Optional
from typing import Union

import numpy as np
import pandas as pd
from sqlalchemy import or_,and_

from database.connection.connection_base import ConnectionBase
from database.connection.mysql_conn import get_default_py_connection
from database.data_field import *
from database.operator_base import BaseReader

from config.specify_variable import *
from config.basic_config import project_path
from functools import lru_cache
from config.licai_base_table_config import LicaiBaseTable

from sql import SqlStatement

class PyReader(BaseReader):
    def __init__(self, py_connection: Optional[ConnectionBase] = None):
        """
        Args:
            juyuan_connection: 数据库连接。如果为None则使用默认配置连接
        """
        if py_connection is None:
            py_connection = get_default_py_connection()
        super().__init__(db_connection=py_connection)


    def get_product_base_info(self,cp_id=None,regsiter_code=None) -> dict:
        """
        获取理财产品的基本信息
        :return: {dataframe }
        """
        table_name = ProductBaseInfo
        # columns = ['cp_id', 'trade_date', 'net_value', 'accumulated_net_value','yield_7_days_annual','earning_per_ten_thousand']
        query = self.query(table_name)
        # code = 2029  # 代表商业理财子公司
        if cp_id is not None:
            query = query.filter(table_name.cp_id == cp_id)
        if regsiter_code is not None:
            query = query.filter(table_name.product_code == regsiter_code)
        df = self.batch_query(query)
        return df


    def get_bank_wealth_product(self):
        sql_sate = SqlStatement.py_sql_bank
        df = pd.read_sql(sql_sate,con=self.engine)
        df['product_establish_date'] = pd.to_datetime(df['product_establish_date'])
        df['MaturityDate'] = pd.to_datetime(df['MaturityDate'])
        df['transfer_date'] = pd.to_datetime(df['transfer_date'])
        return df


    def get_pk_asset_portfolio(self):
        sql_sate = SqlStatement.sql_py_asset_portfolio
        df = pd.read_sql(sql_sate,con=self.engine)
        # 删除重复项
        df = df.drop_duplicates(subset=['registration_code','end_date','first_grade_type','second_grade_type'])
        # df['end_date'] = df['end_date'].map(lambda x:x.strftime('%Y%m%d'))
        return df

    def get_pk_top_10(self):
        sql_sate = SqlStatement.sql_py_top_10
        df = pd.read_sql(sql_sate,con=self.engine)
        # 删除重复项
        df = df.drop_duplicates(subset=['registration_code','end_date','asset_name','primary_type','three_level_type'])
        # df['end_date'] = df['end_date'].map(lambda x:x.strftime('%Y%m%d'))
        return df

    def get_product_buy(self):
        sql_sate = SqlStatement.sql_prodcut_buy
        df = pd.read_sql(sql_sate,con=self.engine)
        return  df

    def get_net_value(self,cp_id=None,register_code=None,begin_date=None,end_date=None):
        """
        获取理财产品的净值
        @begin_date : '20220101'
        @end_date: '20221010

        :return: {dataframe}
        """
        table_name = ProductNetValue
        columns = ['cp_id', 'trade_date', 'net_value', 'accumulated_net_value','yield_7_days_annual','earning_per_ten_thousand']
        query = self.query(table_name,columns=columns)
        # code = 2029  # 代表商业理财子公司
        if cp_id is not None:
            if not isinstance(cp_id,list):
                cp_id = [cp_id]
            query = query.filter(table_name.cp_id.in_(cp_id))
        if register_code is not None:
            query = query.filter(table_name.product_code == register_code)  # fixme 有错误
        if begin_date is not None:
            query = query.filter(table_name.trade_date >= begin_date)
        if end_date is not None:
            query = query.filter(table_name.trade_date <= end_date)

        df = self.batch_query(query)
        df = df.rename(columns={"cp_id": 'FinProCode',
                                "trade_date": 'trade_dt',
                                "net_value": 'UnitNV',
                                "accumulated_net_value": 'AccumulatedUnitNV'})
        df['trade_dt'] = pd.to_datetime(df['trade_dt'])
        return df



    def get_fee(self,cp_id=None,register_code=None):
        pass

    def get_asset_portfolio(self,cp_id=None,register_code=None):
        pass

    def get_asset_top_10(self, cp_id=None, register_code=None):
        pass



if __name__ == '__main__':
    reader = PyReader()
    cp_id = 1251034
    begin_date = '20220101'
    end_date = '20230630'
    reg_code = 'Z7001620000127'
    # data = reader.get_product_base_info(regsiter_code=reg_code)
    net_value = reader.get_net_value(cp_id=[1251034,7738510],begin_date=begin_date,end_date=end_date)
    # bank = reader.get_bank_wealth_product()

    # # 资产配置表create
    # from tools.tools import Timer
    # with Timer(True):
    #     asset_portfolio = reader.get_pk_asset_portfolio()
    #
    # with Timer(True):
    #     top10 = reader.get_pk_top_10()
    #
    # asset_portfolio.to_csv('asset_portfolio.csv')
    # top10.to_csv('top10.csv')



