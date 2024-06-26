# -*- coding: utf-8 -*-

import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.basic_config import DatabaseInfo
from database.connection.connection_base import ConnectionBase
from tools.encrypt import decrypt_des


class SQLServerConnection(ConnectionBase):
    def __init__(self, host: str, user: str, password: str, database: str, charset: str = "utf8", **kwargs):
        """

        Args:
            host: 主机
            user: 用户名
            password: 密码
            database: 数据库
            charset: 字符集
            **kwargs: 其他参数
        """
        driver = list(pyodbc.drivers())[0]
        self._engine = create_engine(f"mssql+pyodbc://{user}:{password}@{host}/{database}?driver={driver}",
                                     connect_args={'charset': charset}, pool_pre_ping=True,
                                     execution_options={'stream_results': True}, **kwargs)
        self.Session = sessionmaker(bind=self.engine)
        self._session = self.Session()

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session


def get_default_juyuan_connection():
    host = DatabaseInfo.juyuan['host']
    user = DatabaseInfo.juyuan['user']
    password = decrypt_des(DatabaseInfo.juyuan["password"])
    database = DatabaseInfo.juyuan['database']
    juyuan_connection = SQLServerConnection(host, user, password, database)
    return juyuan_connection


def get_default_wind_connection():
    host = DatabaseInfo.wind['host']
    user = DatabaseInfo.wind['user']
    password = decrypt_des(DatabaseInfo.wind["password"])
    database = DatabaseInfo.wind['database']
    wind_connection = SQLServerConnection(host, user, password, database)
    return wind_connection


