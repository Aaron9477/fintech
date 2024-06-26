# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/9/14 15:03 
# @Author    : Wangyd5 
# @File      : operator_base
# @Project   : sublicai
# @Function  ：
# --------------------------------
# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/11/23 9:13
# @Author  : wangxybjs
# @File    : operator_base.py
# @Project : fund_analysis_base
# @Function:
# @Version : V0.0.1
# ------------------------------
import datetime
from typing import Dict, Union, Iterable
from typing import Optional, List

import pandas as pd
from sqlalchemy import inspect, cast, VARCHAR
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from log import logger

from database.connection.connection_base import ConnectionBase
from tools.res_cleaner import clean_res
import numpy as np


class BaseReader:
    """
    基础数据库读取
    """

    def __init__(self, db_connection: ConnectionBase):
        self.engine: Engine = db_connection.engine
        self.session: Session = db_connection.session
        self.make_session = db_connection.make_session

    def query(self, table_name=None, columns: Union[list, Dict, None] = None, func_query=None):
        """
        初始化查询query

        Args:
            table_name: 表名；
            columns: 查询的字段, 列表或字典. 若为字典, key是原始字段名, value是需要rename的别名；
            func_query: 聚合函数查询。
            注意：table_name与func_query必须至少指定一个，不可同时为None。

        Returns:
            query对象
        """
        query_columns = []
        # 查询某些字段
        if table_name is not None:
            if isinstance(columns, list):
                query_columns = [table_name.__dict__[name] for name in columns]
            elif isinstance(columns, dict):
                query_columns = [table_name.__dict__[name].label(alias) for name, alias in columns.items()]
            else:
                query_columns = [table_name]
        # 按聚合函数查询，如distinct、func.max
        if func_query is not None:
            if not isinstance(func_query, list):
                func_query = [func_query]
            query_columns += func_query

        if len(query_columns) == 0:
            raise ValueError('You must specify parameters of table_name or func_query, '
                             'which cannot be None at the same time')
        with self.make_session() as session:
            query = session.query(*query_columns)
        return query

    def read_sql(self, query, chunksize=None) -> pd.DataFrame:
        if chunksize is None:
            res = pd.read_sql(query.statement, self.engine)
        else:
            res = pd.DataFrame()
            for chunk_data in pd.read_sql(query.statement, self.engine, chunksize=chunksize):
                res = res.append(chunk_data)
        return res

    @staticmethod
    def filter_date(query, filter_column, begin_date=None, end_date=None, trade_date=None, date_type=VARCHAR(8)):
        """
        日期筛选

        Args:
            query: query对象；
            filter_column: 过滤字段，如：table_name.TRADE_DT；
            begin_date: 开始时间；
            end_date: 结束时间；
            trade_date: 交易日；
            date_type: 日期类型转换，默认转为VARCHAR(8)，为None时不转类型。

        Returns:
            query对象
        """

        def cast_date(date):
            """日期类型转换"""
            if date_type is not None:
                date = cast(date, date_type)
            return date

        if begin_date is not None:
            query = query.filter(filter_column >= cast_date(begin_date))
        if end_date is not None:
            query = query.filter(filter_column <= cast_date(end_date))
        if trade_date is not None:
            query = query.filter(filter_column == cast_date(trade_date))
        return query

    def batch_query(self, query, batch_column=None, batch_value=None, batch_size=500) -> pd.DataFrame:
        """
        分批量查询数据

        Args:
            query: 查询对象，如：query = self.session.query(table_name)；
            batch_column: 批量查询的字段，如：table_name.S_INFO_WINDCODE；
            batch_value: str,list,None, 查询字段值，如：['000001.OF']；
            batch_size: 每次批量获取的大小。

        Returns:
            查询数据DataFrame
        """
        df = pd.DataFrame()
        if batch_value is None:
            df = self.read_sql(query)
        elif isinstance(batch_value, str):
            query_single = query.filter(batch_column == batch_value)
            df = self.read_sql(query_single)
        elif isinstance(batch_value, list):
            if len(batch_value) <= batch_size:
                query_batch = query.filter(batch_column.in_(batch_value))
                df = self.read_sql(query_batch)
            else:
                for i in range(0, len(batch_value), batch_size):
                    batch_value_i = batch_value[i:i + batch_size]
                    query_batch_i = query.filter(batch_column.in_(batch_value_i))
                    df_batch_i = self.read_sql(query_batch_i)
                    df = df.append(df_batch_i)
        return df

    @staticmethod
    def get_table_dtype(table):
        """
        读取表结构
        Args:
            table: 表
        Returns:
            dtype_dict: Key是字段, Value是其类型
        """
        dtype_dict = {}
        for c in inspect(table).columns:
            column = c.name
            dtype = c.type.python_type.__name__
            dtype_transfer = {"str": "str", "Decimal": "float", "datetime": "datetime64"}
            if dtype in dtype_transfer:
                dtype = dtype_transfer[dtype]
            dtype_dict[column] = dtype
        return dtype_dict


class BaseSaver:
    """
    基础数据库存储
    """

    def __init__(self, db_connection: ConnectionBase):
        self.engine: Engine = db_connection.engine
        self.session: Session = db_connection.session
        self.make_session = db_connection.make_session

    @staticmethod
    def transfer_input_to_df(dict_list_or_dataframe):
        """
        将字典/DataFrame或其列表转为DataFrame
        """
        save_list = dict_list_or_dataframe
        if not isinstance(dict_list_or_dataframe, List):
            save_list = [dict_list_or_dataframe]
        df_list = []
        for d in save_list:
            if isinstance(d, pd.DataFrame):
                df_list.append(d)
            elif isinstance(d, Dict):
                df_list.append(pd.DataFrame([d]))
        df = pd.concat(df_list)
        return df

    @staticmethod
    def transfer_input_to_dict_list(dict_list_or_dataframe):
        """
        将字典/DataFrame或其列表转为字典列表
        """
        save_list = dict_list_or_dataframe
        if not isinstance(dict_list_or_dataframe, List):
            save_list = [dict_list_or_dataframe]
        dict_list = []
        for d in save_list:
            if isinstance(d, Dict):
                dict_list.append(d)
            elif isinstance(d, pd.DataFrame):
                dict_list.extend(d.to_dict(orient='records'))
        return dict_list

    def _save(self, table, dict_list_or_dataframe: Union[List, Dict, pd.DataFrame]):
        """
        Args:
            table: 表
            dict_list_or_dataframe: 字典或字典列表或DataFrame
                若为字典或字典列表, Key为字段名, Value为值
                若为DataFrame, 列为字段名
        """
        dict_list = self.transfer_input_to_dict_list(dict_list_or_dataframe)
        record_list = []
        columns = [c.name for c in inspect(table).columns]
        for d in dict_list:
            d = {k: clean_res(v) for k, v in d.items() if k in columns}
            if len(d) > 0:
                record = table(**d)
                record_list.append(record)
        with self.make_session() as session:
            session.bulk_save_objects(record_list)

    @staticmethod
    def transfer_df_numeric_precision(table, df: pd.DataFrame):
        """
        将DataFrame中相应的列转换为table字段定义的精度
        """
        table_define_columns = inspect(table).columns
        for column in df:
            if column in table_define_columns:
                dtype = table_define_columns[column].type
                if hasattr(dtype, 'scale'):
                    df[column] = df[column].apply(lambda x: np.round(x, dtype.scale) if x is not None else None)
        return df

    def _increment_save(self, table, dict_list_or_dataframe, read_func, update_func, filter_columns,
                        update_columns):
        """
        增量式保存, 若新记录不在结果表中则保存, 若新记录在结果表中且不一致则更新
        Args:
            table:
            dict_list_or_dataframe:
            read_func:
            update_func:
            filter_columns:
            update_columns:
        """
        df = self.transfer_input_to_df(dict_list_or_dataframe)
        df = self.transfer_df_numeric_precision(table, df)
        if len(df) == 0:
            return
        df['res'] = df[update_columns].apply(tuple, axis=1)
        res_dict = df.set_index(filter_columns)['res'].to_dict()
        cur_res = read_func()
        cur_res['res'] = cur_res[update_columns].apply(tuple, axis=1)
        cur_res_dict = cur_res.set_index(filter_columns)['res'].to_dict()
        save_list = []
        update_list = []
        for filter_res, update_res in res_dict.items():
            filter_column_dict = {column: clean_res(filter_res[i]) for i, column in enumerate(filter_columns)}
            update_column_dict = {column: clean_res(update_res[i]) for i, column in enumerate(update_columns)}
            if filter_res not in cur_res_dict:
                filter_column_dict.update(update_column_dict)
                record = table(**filter_column_dict)
                save_list.append(record)
            elif cur_res_dict[filter_res] != update_res:
                update_list.append({'filter': filter_column_dict, 'update': update_column_dict})
        if len(save_list) > 0:
            logger.info(f'{table.__tablename__}保存数据量:{len(save_list)}')
            self.session.bulk_save_objects(save_list)
            self.session.commit()
        if len(update_list) > 0:
            logger.info(f'{table.__tablename__}更新数据量:{len(update_list)}')
            update_func(update_list)

    def _update_report_cal_table(self, report_cal_table):
        pass


class BaseUpdater:
    """
    基础数据库更新
    """

    def __init__(self, db_connection: ConnectionBase):
        """
        Args:
            db_connection: 数据库连接
        """
        self.engine: Engine = db_connection.engine
        self.session: Session = db_connection.session
        self.make_session = db_connection.make_session

    def _update(self, table, update_list, batch_size=500):
        """
        Args:
            table: 表
            update_list: 是一个字典的列表, 每个字典是代表一个update语句, 有filter和update两个字典, 分别代表需要筛选和更新的部分
                例如update_list = [{'filter': {'match_column1': match_value1, 'match_column2': match_value2},
                'update': {'update_column1': update_value1, 'update_column2': update_value2}}, ...]
                表示`update table set update_column1=update_value1, update_column2=update_value2 where
                match_column1=match_value1 and match_column2=match_value2`
            batch_size: 一批更新内的记录数量
        """
        with self.make_session() as session:
            query = session.query(table)
            for i in range(0, len(update_list), batch_size):
                batch = update_list[i:i + batch_size]
                for update_record in batch:
                    filter_condition_dict = update_record['filter']
                    update_res_dict = update_record['update']
                    filter_condition = [getattr(table, col) == v for col, v in filter_condition_dict.items()]
                    single_query = query.filter(*filter_condition)
                    update_record_dict = {getattr(table, col): clean_res(v) for col, v in update_res_dict.items()}
                    single_query.update(update_record_dict, synchronize_session=False)
                session.commit()


class BaseDeleter(object):
    """
    基础数据库删除
    """

    def __init__(self, db_connection: ConnectionBase):
        """
        Args:
            db_connection: 数据库连接
        """
        self.engine: Engine = db_connection.engine
        self.session: Session = db_connection.session
        self.make_session = db_connection.make_session

    def _delete(self, table, del_record_list, batch_size=500):
        """
        Args:
            table: 表
            del_record_list: 是一个字典列表, 每个字典代表一个delete语句, Key是筛选字段, Value是筛选值
                例如del_record_list = [{'match_column1': match_value1, 'match_column2': match_value2}, ...]
                代表`delete from table where match_column1=match_value1 and match_column2=match_value2`
            batch_size: 一批删除内的记录数量
        """
        with self.make_session() as session:
            query = session.query(table)
            for i in range(0, len(del_record_list), batch_size):
                batch = del_record_list[i:i + batch_size]
                for del_record in batch:
                    filter_condition_dict = del_record
                    filter_condition = [getattr(table, col) == v for col, v in filter_condition_dict.items()]
                    single_query = query.filter(*filter_condition)
                    single_query.delete()
                session.commit()

    def _expire(self, table, expire_until_date=None, expire_days=30):
        if expire_until_date is None:
            expire_until_date = (datetime.datetime.now() - datetime.timedelta(days=expire_days)).strftime('%Y%m%d')
        self.session.query(table).filter(table.cal_date <= expire_until_date).delete()
        self.session.commit()


class CombineBaseOperator:

    def __init__(self, jjpg_saver, jjpg_deleter, jjpg_updater, jjpg_reader):
        self.saver: BaseSaver = jjpg_saver
        self.deleter: BaseDeleter = jjpg_deleter
        self.updater: BaseUpdater = jjpg_updater
        self.reader: BaseReader = jjpg_reader

    def _increment_save(self, table, code, dict_list_or_dataframe, code_column: str, filter_columns: List[str],
                        compare_ignore_columns=('id', 'cal_date', 'update_time')):
        """
        增量式更新
        若传入数据不存在与数据库中, 则保存
        若传入数据已存在于数据库中, 但不一致, 则更新. 其中:
        (1) 判断是否存在使用filter_columns
        (2) 判断是否一致使用全部的column-ignore_column

        Args:
            table: 表
            code: 代码
            dict_list_or_dataframe: 传入数据
            code_column: 代码列
            filter_columns:判断数据是否已存使用的列
            compare_ignore_columns: 判断一致性忽略的列, 默认为id

        Returns:

        """
        if len(dict_list_or_dataframe) == 0:
            return
        df = self.saver.transfer_input_to_df(dict_list_or_dataframe)
        df = self.saver.transfer_df_numeric_precision(table, df)
        if len(df) == 0:
            return
        query = self.reader.session.query(table)
        cur_res = self.reader.batch_query(query, getattr(table, code_column), code)
        if isinstance(compare_ignore_columns, str):
            compare_ignore_columns = [compare_ignore_columns]
        update_columns = list(set(df.columns) - set(compare_ignore_columns) - set(filter_columns))
        update_columns = list(set(cur_res.columns) & set(update_columns))  # 应保证列在表定义中
        df['res'] = df[update_columns].apply(tuple, axis=1)
        res_dict = df.set_index(filter_columns)['res'].to_dict()
        res_dict = {tuple([k]) if not isinstance(k, tuple) else k: v for k, v in res_dict.items()}

        cur_res['res'] = cur_res[update_columns].apply(tuple, axis=1)
        cur_res_dict = cur_res.set_index(filter_columns)['res'].to_dict()
        cur_res_dict = {tuple([k]) if not isinstance(k, tuple) else k: v for k, v in cur_res_dict.items()}
        save_list = []
        update_list = []
        for filter_res, update_res in res_dict.items():
            filter_column_dict = {column: clean_res(filter_res[i]) for i, column in enumerate(filter_columns)}
            update_column_dict = {column: clean_res(update_res[i]) for i, column in enumerate(update_columns)}
            if filter_res not in cur_res_dict:
                filter_column_dict.update(update_column_dict)
                record = table(**filter_column_dict)
                save_list.append(record)
            elif cur_res_dict[filter_res] != update_res:
                update_list.append({'filter': filter_column_dict, 'update': update_column_dict})

        if len(save_list) > 0:
            logger.info(f'{table.__tablename__}保存数据量:{len(save_list)}')
            self.saver.session.bulk_save_objects(save_list)
            self.saver.session.commit()
        if len(update_list) > 0:
            logger.info(f'{table.__tablename__}更新数据量:{len(update_list)}')
            self.updater._update(table, update_list)


