# -*- coding: utf-8 -*-
"""
Created on Tue JUL 21 17:20:45 2022
获取私募排排（数据库获取）所有私募信息，用于update_fund_id.py使用
@author: 王永镇
"""
import pandas as pd
import numpy as np
import datetime
import sqlite3
import sqlalchemy
import pymysql
import argparse

#显示所有的列
pd.set_option('display.max_columns', 50)
# #显示所有的行
# pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

engine = sqlalchemy.create_engine(
    'mysql+pymysql://data_user_zxjt:K93Qxrme3GsSO589@120.24.90.158:3306/rz_hfdb_core?charset=utf8')

from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import NVARCHAR, Float, Integer, VARCHAR, String, Numeric, CLOB, DateTime, DATE

from sqlalchemy import create_engine, func, or_, distinct
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Pvn_fund_performance_ranking(Base):
    """
    私募排排，基金业绩排名表
    """
    __tablename__ = 'pvn_fund_performance_ranking'
    id = Column(Integer, primary_key=True)
    fund_id = Column(VARCHAR(10))
    class_id = Column(Integer)
    end_date = Column(VARCHAR(10))
    perrank_ret_3m = Column(Integer)
    perrank_ret_1y = Column(Integer)
    perrank_ret_3y = Column(Integer)
    perrank_ret_5y = Column(Integer)
    perrank_ret_incep = Column(Integer)
    isvalid = Column(Integer)


class Pvn_nav(Base):
    """
    私募排排，基金业绩排名表
    """
    __tablename__ = 'pvn_nav'
    id = Column(Integer, primary_key=True)
    fund_id = Column(VARCHAR(10))
    price_date = Column(DATE)
    nav = Column(Numeric(22, 6))
    cumulative_nav = Column(Numeric(22, 6))
    isvalid = Column(Integer)


class Pvn_fund_performance(Base):
    """
    私募排排，基金历史业绩表
    """
    __tablename__ = 'pvn_fund_performance'
    id = Column(Integer, primary_key=True)
    price_date = Column(VARCHAR(10))
    fund_id = Column(VARCHAR(10))
    end_date = Column(VARCHAR(10))
    cumulative_nav = Column(Numeric(22, 6))
    ret_3m = Column(Numeric(22, 6))
    ret_1y = Column(Numeric(22, 6))
    ret_3y = Column(Numeric(22, 6))
    ret_5y = Column(Numeric(22, 6))
    ret_incep = Column(Numeric(22, 6))
    isvalid = Column(Integer)


class Pvn_fund_info(Base):
    """
    私募排排，基金基本信息
    """
    __tablename__ = 'pvn_fund_info'
    id = Column(Integer, primary_key=True)
    fund_id = Column(VARCHAR(10))
    fund_name = Column(VARCHAR(255))
    fund_short_name = Column(VARCHAR(80))
    advisor_id = Column(VARCHAR(10))  # 投资顾问id
    performance_disclosure_mark = Column(Integer)  # 产品披露业绩等级
    isvalid = Column(Integer)


class Pvn_company_info(Base):
    """
    私募排排，公司基本信息
    """
    __tablename__ = 'pvn_company_info'
    company_id = Column(VARCHAR(10), primary_key=True)
    company_name = Column(VARCHAR(255))
    company_short_name = Column(VARCHAR(80))
    register_number = Column(VARCHAR(20))  # 备案编码
    register_status = Column(Integer)  # 备案状态
    isvalid = Column(Integer)


class BaseData(object):
    def __init__(self):
        self.engine = sqlalchemy.create_engine(
                'mysql+pymysql://data_user_zxjt:K93Qxrme3GsSO589@120.24.90.158:3306/rz_hfdb_core?charset=utf8')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()


class GetSmppFund(object):
    def __init__(self, base_data):
        self.engine = base_data.engine
        self.session = base_data.session

    def get_fund_nav(self):
        fund_nav = self.session.query(Pvn_fund_info)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt


def get_smpp_fund():
    base_data = BaseData()
    base_data_obj = GetSmppFund(base_data)
    fund_nav = base_data_obj.get_fund_nav()
    return fund_nav


if __name__ == '__main__':
    smpp_fund = get_smpp_fund()
    smpp_fund.to_csv('smpp_fund.csv', encoding='utf_8_sig', index=None)


    # parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--update_date', type=str, help='更新净值时间', default='20220715')
    # parser.add_argument('--db_path', type=str, help='数据库路径', default='test2.db')
    # parser.add_argument('--zyyx_input_path', type=str, help='朝阳永续数据文件位置', default='../../tests/重点观察私募周报_第28周.xlsx')
    # parser.add_argument('--handle_input_path', type=str, help='手工输入数据文件位置', default='../../tests/手工输入数据.xlsx')
    # args = parser.parse_args()
    #
    # conn = sqlite3.connect(args.db_path)
    # cursor = conn.cursor()
    #
    # update_smpp(conn, cursor, args.update_date)
    #
    # cursor.close()
    # conn.close()