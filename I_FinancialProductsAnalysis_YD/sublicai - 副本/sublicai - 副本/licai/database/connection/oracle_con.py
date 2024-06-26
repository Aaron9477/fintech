# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/9/10 10:03
# @Author  : wangxybjs
# @File    : dfcf_con.py
# @Project : workspaces_jjpg
# @Function: 
# @Version : V0.0.1
# ------------------------------
import textwrap

import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateTable

from config import DatabaseInfo
from database.connection.connection_base import ConnectionBase
from tools.encrypt import decrypt_des


@compiles(CreateTable, "oracle")
def _add_suffixes(element, compiler, **kw):
    text = compiler.visit_create_table(element, **kw)
    if "oracle_partition" in element.element.info:
        text += textwrap.dedent(
            element.element.info["oracle_partition"]).strip()
    return text


class OracleConnection(ConnectionBase):
    def __init__(self, host: str, user: str, password: str, database: str, port, **kwargs):
        """

        Args:
            host: 主机
            user: 用户名
            password: 密码
            database: 数据库
            charset: 字符集
            **kwargs: 其他参数
        """
        import os
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'
        dsn_str = cx_Oracle.makedsn(host, port, service_name=database)
        connect_str = f'oracle://{user}:{password}@{dsn_str}'
        self._engine = create_engine(connect_str, encoding='gbk', max_identifier_length=128)

        self.Session = sessionmaker(bind=self.engine)
        self._session = self.Session()
        self.db = cx_Oracle.connect(f'{user}/{password}@{host}:{port}/{database}')
        self.cur = self.db.cursor()  # TODO to be deleted

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session


def get_default_licai_connection():
    host = DatabaseInfo.licai["host"]
    user = DatabaseInfo.licai["user"]
    password = decrypt_des(DatabaseInfo.licai["password"])
    database = DatabaseInfo.licai["database"]
    port = DatabaseInfo.licai["port"]
    res_connection = OracleConnection(host, user, password, database, port)
    return res_connection



def get_default_fund_connection():
    host = DatabaseInfo.fund['host']
    user = DatabaseInfo.fund['user']
    password = decrypt_des(DatabaseInfo.fund["password"])
    database = DatabaseInfo.fund['database']
    port = DatabaseInfo.fund['port']
    fund_connection = OracleConnection(host, user, password, database,port)
    return fund_connection


def get_default_fundtest_connection():
    host = DatabaseInfo.fundtest['host']
    user = DatabaseInfo.fundtest['user']
    password = decrypt_des(DatabaseInfo.fundtest["password"])
    database = DatabaseInfo.fundtest['database']
    port = DatabaseInfo.fundtest['port']
    fundtest_connection = OracleConnection(host, user, password, database,port)
    return fundtest_connection