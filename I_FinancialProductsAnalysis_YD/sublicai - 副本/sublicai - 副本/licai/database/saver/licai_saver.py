# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/10/25 14:33 
# @Author    : Wangyd5 
# @File      : licai_saver
# @Project   : sublicai
# @Function  ：
# --------------------------------



from typing import Optional

from database.connection.connection_base import ConnectionBase
from database.connection.mysql_conn import get_licai_connection
from database.data_field.licai_field import *
from database.operator_base import BaseSaver


class ResDataSaver(BaseSaver):
    def __init__(self, db_connection: Optional[ConnectionBase] = None):
        """
        Args:
            db_connection: 数据库连接。如果为None则使用默认配置连接
        """
        if db_connection is None:
            db_connection = get_licai_connection()
        super().__init__(db_connection=db_connection)

    def save_licai_financial_report(self, res_dict_list):
        self._save(LicaiFInancialReport, res_dict_list)

    def save_asset_portfolio(self, res_dict_list):
        self._save(AssetPortfolio, res_dict_list)

    def save_top10(self, res_dict_list):
        self._save(AssetTop10, res_dict_list)

    def save_basic_info(self, res_dict_list):
        self._save(BasicInfo, res_dict_list)

    def save_week_nav(self, res_dict_list):
        self._save(WeekNav, res_dict_list)

