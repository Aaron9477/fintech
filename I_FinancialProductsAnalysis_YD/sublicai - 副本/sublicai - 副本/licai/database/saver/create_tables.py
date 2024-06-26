# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/10 18:42 
# @Author    : Wangyd5 
# @File      : create_tables
# @Project   : licai
# @Function  ：
# --------------------------------

from database.data_field.licai_field import *
from database.connection.mysql_conn import get_licai_connection


def create_tables(connection):
    Base.metadata.create_all(connection.engine)


if __name__ == '__main__':
    conn = get_licai_connection()
    create_tables(conn)