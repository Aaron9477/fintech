# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/10/25 14:32 
# @Author    : Wangyd5 
# @File      : __init__.py
# @Project   : sublicai
# @Function  ：
# --------------------------------

from .licai_saver import ResDataSaver
from database.connection.mysql_conn import get_licai_connection


licai_saver = ResDataSaver(db_connection=get_licai_connection())
