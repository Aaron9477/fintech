# -*- coding: utf-8 -*-
"""
获取私募排排一个基金的所有净值情况，北京信托的需求
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

#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

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


class Pvn_nav_all_business(Base):
    """
    私募排排，基金净值表，新表，结构与pvn_nav一致
    """
    __tablename__ = 'pvn_nav_all_business'
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
    issuer_id = Column(VARCHAR(10))  # 发行人ID
    trust_id = Column(VARCHAR(10))  # 基金管理公司ID
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


class Pvn_fund_strategy(Base):
    """
    私募排排，公司基本信息
    """
    __tablename__ = 'pvn_fund_strategy'
    fund_id = Column(VARCHAR(10), primary_key=True)
    first_strategy = Column(Integer)
    second_strategy = Column(Integer)
    third_strategy = Column(Integer)
    isvalid = Column(Integer)


class Pvn_amac_company_scale_history(Base):
    """
    私募排排，公司规模分布情况
    """
    __tablename__ = 'pvn_amac_company_scale_history'
    company_id = Column(VARCHAR(20), primary_key=True)
    company_name = Column(VARCHAR(100))
    fundscale_range_desc = Column(VARCHAR(50))
    fundscale_range = Column(VARCHAR(50))
    crawl_date = Column(DateTime)
    isvalid = Column(Integer)
    is_latest = Column(Integer)
    createtime = Column(DateTime)
    updatetime = Column(DateTime)


class Pvn_stat_amac_private_fund_scale_range_amount(Base):
    """
    私募排排，公司规模分布情况
    """
    __tablename__ = 'pvn_stat_amac_private_fund_scale_range_amount'
    id = Column(Integer, primary_key=True)
    stat_period_type = Column(Integer)
    stat_period_desc = Column(VARCHAR(50))
    stat_period = Column(Integer)
    sub_stat_period = Column(Integer)
    scale_range_desc = Column(VARCHAR(128))
    scale_range = Column(VARCHAR(4))
    manage_amount = Column(VARCHAR(20))
    isvalid = Column(Integer)
    createtime = Column(DateTime)
    updatetime = Column(DateTime)


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
        fund_nav = self.session.query(Pvn_nav_all_business).filter(Pvn_nav_all_business.fund_id == fund_id, Pvn_nav_all_business.isvalid == 1)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt

    def get_all_fund_nav_by_date(self, date):
        # 通过ORM操作数据库
        fund_nav = self.session.query(Pvn_nav_all_business).filter(Pvn_nav_all_business.price_date == date, Pvn_nav_all_business.isvalid == 1)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt

    def get_pvn_amac_company_scale_history(self):
        fund_nav = self.session.query(Pvn_amac_company_scale_history)
        dt = pd.read_sql(fund_nav.statement, self.engine).filter(Pvn_amac_company_scale_history.isvalid == 1)
        return dt

    def get_pvn_stat_amac_private_fund_scale_range_amount(self):
        fund_nav = self.session.query(Pvn_stat_amac_private_fund_scale_range_amount)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt

    def get_company_info(self, company_id):
        # 通过ORM操作数据库
        fund_nav = self.session.query(Pvn_company_info).filter(Pvn_company_info.company_id == company_id, Pvn_company_info.isvalid == 1)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt

    def get_all_fund_strategy(self):
        fund_strategy = self.session.query(Pvn_fund_strategy).filter(Pvn_fund_strategy.isvalid == 1)
        res = pd.read_sql(fund_strategy.statement, self.engine)
        return res

    def get_pvn_fund_info(self):
        fund_strategy = self.session.query(Pvn_fund_info).filter(Pvn_fund_info.isvalid == 1)
        res = pd.read_sql(fund_strategy.statement, self.engine)
        return res

    def get_all_company_info(self):
        # 通过ORM操作数据库
        fund_nav = self.session.query(Pvn_company_info).filter(Pvn_company_info.isvalid == 1)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt


def get_data(fund_id):
    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    fund_nav = base_data_obj.get_fund_nav(fund_id)
    return fund_nav


def get_data_tmp(begin_date, end_date, now_date):
    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    fund_strategy_df = base_data_obj.get_all_fund_strategy()
    # 筛选债券型私募
    bond_fund_strategy_df = fund_strategy_df[fund_strategy_df['first_strategy'] == 1002]

    bond_name_reflect_dict = {100201: "纯债策略", 100202: "债券增强", 100203: "债券复合策略", 100204: "转债交易策略"}
    second_strategy_list = bond_fund_strategy_df["second_strategy"]
    second_strategy_chi_list = []
    for second_strategy in second_strategy_list:
        if second_strategy in bond_name_reflect_dict.keys():
            second_strategy_chi_list.append(bond_name_reflect_dict[int(second_strategy)])
        else:
            second_strategy_chi_list.append('无分类数据')
    bond_fund_strategy_df["second_strategy_new"] = second_strategy_chi_list

    # 拉取基金名称
    bond_name_df = base_data_obj.get_pvn_fund_info()
    bond_name_df = bond_name_df[["fund_id", "fund_name", "fund_short_name", "issuer_id", "trust_id", "advisor_id"]]
    res = bond_fund_strategy_df.merge(bond_name_df, how='left', on='fund_id')

    # 拉取管理人名称
    advisor_name_df = base_data_obj.get_all_company_info()
    advisor_name_df = advisor_name_df[["company_id", "company_name"]]

    # 对基金发行人、管理人、投顾进行名称拼接
    res = res.merge(advisor_name_df, how='left', left_on='issuer_id', right_on="company_id")
    res = res.rename(columns={'company_name': "issuer_name"})
    res = res.merge(advisor_name_df, how='left', left_on='trust_id', right_on="company_id")
    res = res.rename(columns={'company_name': "trust_name"})
    res = res.merge(advisor_name_df, how='left', left_on='advisor_id', right_on="company_id")
    res = res.rename(columns={'company_name': "advisor_name"})

    # 拉取起始日期和结束日期的净值数据
    begin_date_df = base_data_obj.get_all_fund_nav_by_date(begin_date)
    end_date_df = base_data_obj.get_all_fund_nav_by_date(end_date)
    now_date_df = base_data_obj.get_all_fund_nav_by_date(now_date)

    # 只保留fund_id和复权累计净值
    begin_date_df = begin_date_df[['fund_id', 'cumulative_nav']]
    end_date_df = end_date_df[['fund_id', 'cumulative_nav']]
    now_date_df = now_date_df[['fund_id', 'cumulative_nav']]

    begin_date_df = begin_date_df.rename(columns={'cumulative_nav': begin_date + '复权累计净值'})
    end_date_df = end_date_df.rename(columns={'cumulative_nav': end_date + '复权累计净值'})
    now_date_df = now_date_df.rename(columns={'cumulative_nav': now_date + '复权累计净值'})

    res = res.merge(begin_date_df, how='left', on='fund_id')
    res = res.merge(end_date_df, how='left', on='fund_id')
    res = res.merge(now_date_df, how='left', on='fund_id')

    res['2022年收益率'] = res[end_date + '复权累计净值'] / res[begin_date + '复权累计净值'] - 1
    res['2023年至' + now_date + '收益率'] = res[now_date + '复权累计净值'] / res[end_date + '复权累计净值'] - 1

    return res


def get_pvn_amac_company_scale_history():
    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    fund_nav = base_data_obj.get_pvn_amac_company_scale_history()
    return fund_nav


def get_fund_scale_range_amount():
    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    fund_nav = base_data_obj.get_pvn_stat_amac_private_fund_scale_range_amount()
    return fund_nav


def get_company_info(company_id):
    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    fund_nav = base_data_obj.get_company_info(company_id)
    return fund_nav


if __name__ == '__main__':

    # 获取净值信息
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--fund_id', type=str, help='fund_id', default='PPWMFDI')
    parser.add_argument('--begin_date', type=str, help='begin_date', default='2021-12-31')
    parser.add_argument('--end_date', type=str, help='end_date', default='2022-12-30')
    parser.add_argument('--now_date', type=str, help='now_date', default='2023-05-19')
    args = parser.parse_args()

    updata_data = get_data_tmp(args.begin_date, args.end_date, args.now_date)

    # 获取规模信息
    # updata_data = get_fund_scale_range_amount()
    # updata_data = get_pvn_amac_company_scale_history()

    # fund_list_smpp = ["HF00000JZE", "HF00000BRS", "HF00000X0X", "HF00001WK1", "HF000026II", "HF000028T5", "HF0000640E",
    #                   "HF00007CSO", "HF000094SF", "HF00000VP1", "HF00003ZUI", "HF000049PM", "HF000040VD", "HF00001ENV",
    #                   "HF00006QZT", "HF00003ZU0", "HF000063FW", "HF00005FAB",]

    print(updata_data)
    updata_data.to_excel('数据提取结果.xlsx')



    # # 获取公司信息
    # parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--company_id', type=str, help='company_id', default='CO00003MNB')
    # args = parser.parse_args()
    # updata_data = get_company_info(args.company_id)
    #
    # print(updata_data)
    # # updata_data.to_excel('明汯价值成长1期.xlsx')
