# -*- coding: utf-8 -*-
"""
获取私募排排一个基金的所有净值情况，并保存
"""
import pandas as pd
import numpy as np
import datetime
import sqlite3
import sqlalchemy
import pymysql
import argparse

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
    私募排排，基金净值表
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


class GetBaseData(object):
    def __init__(self, base_data):
        self.engine = base_data.engine
        self.session = base_data.session

    def get_fund_nav(self, fund_id):
        # 通过ORM操作数据库
        fund_nav = self.session.query(Pvn_nav).filter(Pvn_nav.fund_id == fund_id, Pvn_nav.isvalid == 1).order_by(Pvn_nav.price_date)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt


def check_fund_nval(base_data_obj, fund_id, check_time):

    updata_data = base_data_obj.get_fund_nav(fund_id)

    if updata_data.empty:
        return False

    fund_latest_time = updata_data.values[-1][2]
    if fund_latest_time < datetime.datetime.date(datetime.datetime.strptime(check_time, "%Y%m%d")):
        print(updata_data)
        return False
    return True


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--file_dir', type=str, help='file_dir', default='C:/Users/15620/Desktop/缺失净值问题整理.xlsx')
    parser.add_argument('--fund_id', type=str, help='fund_id', default='HF000029GQ')
    parser.add_argument('--check_time', type=str, help='check_time', default='20220811')
    args = parser.parse_args()

    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    no_nval_find_list = []
    raw_data = pd.read_excel(args.file_dir)
    raw_data["近期净值是否存在"] = "存在"
    for index, line in raw_data.iterrows():
        if(check_fund_nval(base_data_obj, line["排排id"], args.check_time)) == False:
            no_nval_find_list.append(line["排排id"])
            raw_data["近期净值是否存在"][index] = "不存在"
    writer = pd.ExcelWriter('C:/Users/15620/Desktop/test.xlsx')
    raw_data.to_excel(writer, sheet_name='data')

    print(no_nval_find_list)
    writer.save()
    writer.close()

    # fund_list_smpp = ["HF00000JZE", "HF00000BRS", "HF00000X0X", "HF00001WK1", "HF000026II", "HF000028T5", "HF0000640E",
    #                   "HF00007CSO", "HF000094SF", "HF00000VP1", "HF00003ZUI", "HF000049PM", "HF000040VD", "HF00001ENV",
    #                   "HF00006QZT", "HF00003ZU0", "HF000063FW", "HF00005FAB",]

    # print(updata_data.values[-1][2] < datetime.date(2022, 8, 27))


