# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/10 17:46 
# @Author    : Wangyd5 
# @File      : mysql_conn
# @Project   : licai
# @Function  ：
# --------------------------------


# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/9/3 9:10
# @Author  : wangxybjs
# @File    : res_con.py
# @Project : workspaces_jjpg
# @Function: 恒天财富库连接
# @Version : V0.0.1
# ------------------------------
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DatabaseInfo
from database.connection.connection_base import ConnectionBase
from tools.encrypt import decrypt_des
from urllib.parse import  quote_plus as urlquote

class MySQLConnection(ConnectionBase):
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
        connect_str = f"mysql+pymysql://{user}:{urlquote(password)}@{host}:{port}/{database}"
        self._engine = create_engine(connect_str, pool_recycle=300, pool_pre_ping=True,
                                     max_identifier_length=99999,
                                     execution_options={'stream_results': True}, encoding='gbk')
        self.Session = sessionmaker(bind=self.engine)
        self._session = self.Session()

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session


def get_default_py_connection():
    host = DatabaseInfo.py["host"]
    user = DatabaseInfo.py["user"]
    password = decrypt_des(DatabaseInfo.py["password"])
    database = DatabaseInfo.py["database"]
    port = DatabaseInfo.py["port"]
    res_connection = MySQLConnection(host, user, password, database, port)
    return res_connection

def get_licai_connection():
    host = DatabaseInfo.licai["host"]
    user = DatabaseInfo.licai["user"]
    password = decrypt_des(DatabaseInfo.licai["password"])
    database = DatabaseInfo.licai["database"]
    port = DatabaseInfo.licai["port"]
    res_connection = MySQLConnection(host, user, password, database, port)
    return res_connection