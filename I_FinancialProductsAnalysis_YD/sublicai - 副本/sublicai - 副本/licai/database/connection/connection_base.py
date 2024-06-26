# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/9/14 13:54 
# @Author    : Wangyd5 
# @File      : connection_base
# @Project   : sublicai
# @Function  ：
# --------------------------------

import abc
from contextlib import contextmanager

from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session, sessionmaker


class ConnectionBase(metaclass=abc.ABCMeta):
    """
    关系型基础数据库连接, 包含engine和session属性
    """

    @property
    @abc.abstractmethod
    def engine(self) -> Engine:
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def session(self) -> Session:
        """长会话"""
        raise NotImplementedError

    @contextmanager
    def make_session(self) -> Session:
        """上下文形式的短会话"""
        session = sessionmaker(bind=self.engine)()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise ValueError(e)
        finally:
            session.close()
