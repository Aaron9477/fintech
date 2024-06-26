# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/11/22 9:56 
# @Author    : Wangyd5 
# @File      : read_fund_analysis
# @Project   : sublicai
# @Function  ：读取基金评估系统中的数据
# --------------------------------


import os
from typing import Optional
from typing import Union

import numpy as np
import pandas as pd
from sqlalchemy import or_,and_

from sublicai.database.connection.connection_base import ConnectionBase
from sublicai.database.connection.oracle_con import get_default_fund_connection,get_default_fundtest_connection
from sublicai.database.operator_base import BaseReader
from sublicai.database.data_field.fund_field.fund_field import *
from sublicai.database.data_field.fund_field.fund_test_field import *
from sublicai.config.specify_variable import *
from sublicai.config.basic_config import project_path
from functools import lru_cache


class FundTestReader(BaseReader):
    def __init__(self, fund_connection: Optional[ConnectionBase] = None):
        """
        Args:
            fund_connection: 数据库连接。如果为None则使用默认配置连接
        """
        if fund_connection is None:
            fund_connection = get_default_fundtest_connection()
        super().__init__(db_connection=fund_connection)


    def get_fund_product_score(self) -> dict:
        """
        获取基金产品评分
        :return: {str: int }
        """
        table_name = FundProductScore
        columns = ['code','cal_date','total_score_rank_short_term','total_score_rank_medium_term',
                    'total_score_rank_long_term']
        query = self.query(table_name, columns)
        df = self.batch_query(query)
        # df = df[df['CAL_DATE'] == df['CAL_DATE'].max()]
        return df


class FundReader(BaseReader):
    def __init__(self, fund_connection: Optional[ConnectionBase] = None):
        """
        Args:
            fund_connection: 数据库连接。如果为None则使用默认配置连接
        """
        if fund_connection is None:
            fund_connection = get_default_fund_connection()
        super().__init__(db_connection=fund_connection)


    def get_fund_baisc_info(self) -> dict:
        """
        获取基本信息
        :return: {str: int }
        """
        table_name = FundBasicInfo
        query = self.query(table_name)
        df = self.batch_query(query)
        # df = df[df['CAL_DATE'] == df['CAL_DATE'].max()]
        return df

if __name__ == '__main__':
    fund_reader = FundReader()
    basic_info = fund_reader.get_fund_baisc_info()
    fund_test_reader = FundTestReader()
    score = fund_test_reader.get_fund_product_score()


