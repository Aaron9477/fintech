# -*- coding: utf-8 -*-
"""
对比私募周报和和数据库，找出数据库中没有该私募的数量
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

sheet_list = ['股票多头-多空', '指数增强', '市场中性', '管理期货', '宏观', '套利', '债券', '混合']
# sheet_list = ['股票多头-多空']


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
    私募排排，基金净值表，已失效
    """
    __tablename__ = 'pvn_nav'
    id = Column(Integer, primary_key=True)
    fund_id = Column(VARCHAR(10))
    price_date = Column(DATE)
    nav = Column(Numeric(22, 6))
    cumulative_nav = Column(Numeric(22, 6))
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

    def get_fund_nav(self, fund_id, price_date):
        # 通过ORM操作数据库
        fund_nav = self.session.query(Pvn_nav_all_business).filter(Pvn_nav_all_business.fund_id == fund_id, Pvn_nav_all_business.price_date == price_date,
                                                      Pvn_nav_all_business.isvalid == 1)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt

    def get_fund_nav_between(self, fund_id, begin_date, end_date):
        # 通过ORM操作数据库
        fund_nav = self.session.query(Pvn_nav_all_business).filter(Pvn_nav_all_business.fund_id == fund_id, Pvn_nav_all_business.price_date > begin_date,
                                                      Pvn_nav_all_business.price_date < end_date, Pvn_nav_all_business.isvalid == 1)
        dt = pd.read_sql(fund_nav.statement, self.engine)
        return dt


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def read_update_file(input_file):
    fund_base_info_list = []
    for fund_base_info in sheet_list:
        fund_base_info_list.append(pd.read_excel(input_file, sheet_name=fund_base_info))
    return fund_base_info_list


def check_fund_nval(conn, cursor, base_data_obj, fund_info_content_list):
    database_no_fund_list = []
    database_has_smpp_id_list = []
    database_no_smpp_id_list = []
    weekly_no_nval_list = []
    smpp_no_fund_list = []
    smpp_wrong_fund_list = []

    for fund_info_content in fund_info_content_list:
        # 目标行的位置 - 设定为倒数第四行(人工设置)
        nval_end_index = 0
        for i in range(len(fund_info_content.iloc[:, 0].values)):
            if (fund_info_content.iloc[:, 0].values[i] == '数据分析指标'):
                nval_end_index = i - 4

        # 净值日期
        nval_time = fund_info_content.iloc[nval_end_index, 0]

        # 计数器
        num = 0

        for index, col in fund_info_content.iteritems():
            # 略过周报第一行
            if index == 'Unnamed: 0':
                continue
            # 基金有名称，且存在管理人和成立时间（用于过滤非基金基本信息的备注性的文字）
            if isinstance(col[0], str) and isinstance(col[2], str) and isinstance(col[5], datetime.datetime):
                num += 1
                if num % 50 == 0:
                    print(num)

                fund_name = col[0]

                # 从数据库中搜索私募排排id
                cursor.execute("SELECT fund_id_smpp FROM fund_base_info WHERE fund_name='{}'".format(fund_name))
                conn.commit()
                database_smpp_id = cursor.fetchall()

                # 数据库是否存在该私募产品
                if len(database_smpp_id) == 0:
                    database_no_fund_list.append(fund_name)
                    continue

                # 数据库是否存在私募排排id
                if database_smpp_id[0][0] == None:
                    database_no_smpp_id_list.append(fund_name)
                    continue
                else:
                    database_has_smpp_id_list.append(fund_name)
                    fund_id_smpp = database_smpp_id[0]

                # 周报中本身就没有净值信息，跳过
                fund_nval = col[nval_end_index]
                if not is_number(fund_nval) or fund_nval is np.nan:
                    weekly_no_nval_list.append(fund_name)
                    continue

                # 基于私募排排id从私募排排数据库中拉取净值   拉取是目标日期前后6天的净值
                nval_begin_time = (nval_time + datetime.timedelta(days=-6)).strftime('%Y-%m-%d')
                nval_end_time = (nval_time + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
                fund_nval_smpp = base_data_obj.get_fund_nav_between(fund_id_smpp, nval_begin_time, nval_end_time).values
                if len(fund_nval_smpp) == 0:
                    smpp_no_fund_list.append(fund_name)
                    continue

                # 搜索是否有私募排排数据和私募周报数据相近
                flag = False
                for i in range(len(fund_nval_smpp)):
                    if abs(float(fund_nval) - float(fund_nval_smpp[i][4])) < 0.01:
                        flag = True
                if not flag:
                    smpp_wrong_fund_list.append(fund_name)
            else:
                pass
    return database_no_fund_list, database_has_smpp_id_list, database_no_smpp_id_list, \
           weekly_no_nval_list, smpp_no_fund_list, smpp_wrong_fund_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # parser.add_argument('--file_dir', type=str, help='file_dir', default='C:/Users/15620/Desktop/缺失净值问题整理.xlsx')
    # parser.add_argument('--fund_id', type=str, help='fund_id', default='HF000029GQ')
    # parser.add_argument('--check_time', type=str, help='check_time', default='20220812')
    parser.add_argument('--weekly_file', type=str, help='周报数据', default='重点观察私募周报（2022年第39周，2022.09.30）.xlsx')
    parser.add_argument('--database_file', type=str, help='数据库文件', default='test2.db')
    args = parser.parse_args()

    # 连接私募排排数据库
    base_data = BaseData()
    base_data_obj = GetBaseData(base_data)

    # 连接本地数据库
    conn = sqlite3.connect(args.database_file)
    cursor = conn.cursor()

    fund_info_content_list = read_update_file(args.weekly_file)
    # 检查数据问题
    database_no_fund_list, database_has_smpp_id_list, database_no_smpp_id_list, weekly_no_nval_list, smpp_no_fund_list, \
    smpp_wrong_fund_list = check_fund_nval(conn, cursor, base_data_obj, fund_info_content_list)

    print("数据库中没有该私募的数量：{}".format(len(database_no_fund_list)))
    print("周报中有私募最新净值的数量：{}".format(len(weekly_no_nval_list)))
    print("数据库中有私募排排id的数量：{}".format(len(database_has_smpp_id_list)))
    print("\n数据库中没有私募排排id的数量：{}。详情如下:".format(len(database_no_smpp_id_list)))
    print(database_no_smpp_id_list)
    print("\n私募排排没有该产品净值信息的数量：{}。详情如下:".format(len(smpp_no_fund_list)))
    print(smpp_no_fund_list)
    print("\n私募排排该产品净值对不上的数量：{}。详情如下:".format(len(smpp_wrong_fund_list)))
    print(smpp_wrong_fund_list)

    res = []
    res += database_no_smpp_id_list
    res += smpp_no_fund_list
    res += smpp_wrong_fund_list
    with open('res.txt', 'w') as f:
        for i in res:
            f.write(str(i) + '\n')

    # no_nval_find_list = []
    # raw_data = pd.read_excel(args.file_dir)
    # raw_data["近期净值是否存在"] = "存在"
    # for index, line in raw_data.iterrows():
    #     if(check_fund_nval(base_data_obj, line["排排id"], args.check_time)) == False:
    #         no_nval_find_list.append(line["排排id"])
    #         raw_data["近期净值是否存在"][index] = "不存在"
    # writer = pd.ExcelWriter('C:/Users/15620/Desktop/test.xlsx')
    # raw_data.to_excel(writer, sheet_name='data')
    #
    # print(no_nval_find_list)
    #
    # writer.save()
    # writer.close()

    cursor.close()
    conn.close()

    # fund_list_smpp = ["HF00000JZE", "HF00000BRS", "HF00000X0X", "HF00001WK1", "HF000026II", "HF000028T5", "HF0000640E",
    #                   "HF00007CSO", "HF000094SF", "HF00000VP1", "HF00003ZUI", "HF000049PM", "HF000040VD", "HF00001ENV",
    #                   "HF00006QZT", "HF00003ZU0", "HF000063FW", "HF00005FAB",]

    # print(updata_data.values[-1][2] < datetime.date(2022, 8, 27))
