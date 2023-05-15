# -*- coding: utf-8 -*-
"""
Created on Tue JUL 21 17:20:45 2022
从私募排排数据库里查询私募数据
@author: 王永镇
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


class GetBaseData(object):
    def __init__(self, base_data):
        self.engine = base_data.engine
        self.session = base_data.session

    def get_fund_nav(self, fund_list, tradeday):
        fund_nav = self.session.query(Pvn_nav).filter(Pvn_nav.fund_id.in_(fund_list), Pvn_nav.isvalid == 1,
                                                      Pvn_nav.price_date == tradeday)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt


def get_data(fund_list_zyyx, nval_time):
    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    dt = fund_list_zyyx
    daystr = datetime.datetime.strptime(nval_time, "%Y%m%d")
    fund_list = list(dt["fund_id_smpp"].values)

    fund_nav = base_data_obj.get_fund_nav(fund_list, daystr)

    # 只对查到净值数据的进行补充
    dt = pd.merge(fund_nav, dt, how='left', left_on='fund_id', right_on='fund_id_smpp')
    dt = dt.loc[:, ["fund_name", "nav", "cumulative_nav"]]
    # dt['净值日期'] = dt['净值日期'].apply(lambda x: str(x)[:4]+'/'+str(x)[4:6]+'/'+str(x)[6:])
    return dt


def get_data2(fund_list_zyyx, nval_time):
    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    daystr = datetime.datetime.strptime(nval_time, "%Y%m%d")
    fund_list = fund_list_zyyx

    fund_nav = base_data_obj.get_fund_nav(fund_list, daystr)
    return fund_nav


# 拉取数据来源是私募排排的基金序列
def get_fund_list_smpp(conn, cursor):
    sql = "select fund_name, fund_id_smpp from fund_base_info where report_data_source='smpp' and report_nval_type='cumulative_nav'"
    fund_list_smpp = pd.read_sql(sql, conn)
    conn.commit()
    return fund_list_smpp


def update_database(conn, cursor, updata_data, nval_time):
    sql = "insert into fund_nval(fund_name, nval_date, nval) values(?, ?, ?)"
    insert_time = str(nval_time)[:4] + '-' + str(nval_time)[4:6] + '-'+str(nval_time)[6:]
    # 计数新数据，成功插入数据
    new_data, num_insert = 0, 0

    for index, row in updata_data.iterrows():
        updata_info = (row[0], insert_time, row[2])
        new_data += 1

        # 尝试将新数据插入到数据库中，主键（基金名称*日期）重复的会插入失败
        try:
            cursor.execute(sql, updata_info)
        except sqlite3.IntegrityError as e:
            if e.__str__().startswith('UNIQUE constraint failed'):
                print('基金{}在{}已经在库中了，本次未录入。该条数据详情如下：'.format(updata_info[0], nval_time))
                print(updata_info)
                continue
            else:
                print(e)
        num_insert += 1
        conn.commit()
    return new_data, num_insert


def update_smpp(conn, cursor, nval_time):
    # fund_list_zyyx = func.get_fund_list_smpp(conn, cursor, 'smpp')
    fund_list_zyyx = get_fund_list_smpp(conn, cursor)
    updata_data = get_data(fund_list_zyyx, nval_time)
    new_data, num_insert = update_database(conn, cursor, updata_data, nval_time)
    return new_data, num_insert


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--update_date', type=str, help='更新净值时间', default='20220916')
    args = parser.parse_args()

    fund_list_smpp = ["HF00000JZE", "HF00000BRS", "HF00000X0X", "HF00001WK1", "HF000026II", "HF000028T5", "HF0000640E",
                      "HF00007CSO", "HF000094SF", "HF00000VP1", "HF00003ZUI", "HF000049PM", "HF000040VD", "HF00001ENV",
                      "HF00006QZT", "HF00003ZU0", "HF000063FW", "HF00005FAB",]

    updata_data = get_data2(fund_list_smpp, args.update_date)
    print(updata_data)

