# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/8/5 9:24
# @Author  : lisl3
# @File    : get_wind_data.py
# @Project : fund_analysis
# @Function: 获取wind数据接口
# @Version : V0.0.1
# ------------------------------
import datetime
from typing import Dict, List, Optional, Union

import numpy as np
import pandas as pd
from sqlalchemy import or_, func, distinct,and_

from database.connection.connection_base import ConnectionBase
from database.connection.sql_server_con import get_default_wind_connection
from database.data_field.wind_field import *
from database.operator_base import BaseReader
from tools.date_util import TradeDateUtilsTemplate


class WindReader(BaseReader):
    def __init__(self, wind_connection: Optional[ConnectionBase] = None):
        """
        Args:
            wind_connection: 数据库连接。如果为None则使用默认配置连接
        """
        if wind_connection is None:
            wind_connection = get_default_wind_connection()
        super().__init__(db_connection=wind_connection)

    if 'A stock':
        # 股票相关
        def get_a_share_eod_prices(self,
                                   code: Union[None, str, list] = None,
                                   begin_date: Optional[str] = None,
                                   end_date: Optional[str] = None,
                                   trade_date: Optional[str] = None,
                                   columns: Optional[list] = None) -> pd.DataFrame:
            """查询A股行情"""
            table_name = ASHAREEODPRICES
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            if 'TRADE_DT' in df.columns:
                df.sort_values(by='TRADE_DT', inplace=True)
            return df

        def get_valid_stock(self):
            """
            获取有效股票(非IPO失败)
            """
            df = self.get_a_share_description()
            code_list = df[~df["S_INFO_LISTDATE"].isna()]["S_INFO_WINDCODE"].tolist()
            return code_list

        def get_existing_stock_code(self, date=None):
            """获取存续的A股代码"""
            table_name = ASHAREDESCRIPTION
            query = self.query(table_name, ['S_INFO_WINDCODE'])
            if date is None:
                date = datetime.datetime.now().strftime('%Y%m%d')
            query = query.filter(table_name.S_INFO_LISTDATE <= date).filter(
                or_(table_name.S_INFO_DELISTDATE >= date,
                    table_name.S_INFO_DELISTDATE.is_(None)))
            existing_fund_list = self.read_sql(query)["S_INFO_WINDCODE"].tolist()
            return existing_fund_list

        def get_a_share_description(self, code=None, columns=None):
            """中国A股基本资料"""
            table_name = ASHAREDESCRIPTION
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_ipo(self, code=None, begin_date=None, end_date=None, trade_date=None,columns=None):
            """中国A股首次公开发行数据"""
            table_name = ASHAREIPO
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.S_IPO_LISTDATE, begin_date, end_date, trade_date).order_by(table_name.S_IPO_LISTDATE)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_index_eod_prices(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                   columns=None) -> pd.DataFrame:
            """查询指数行情"""
            table_name = AINDEXEODPRICES
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            if 'TRADE_DT' in df.columns:
                df.sort_values(by='TRADE_DT', inplace=True)
            return df

        def get_a_index_members(self, code=None, begin_date=None, end_date=None, columns=None):
            """中国A股指数成份股"""
            table_name = AINDEXMEMBERS
            query = self.query(table_name, columns)
            # 筛选条件
            if begin_date is not None:
                query = query.filter(or_(table_name.S_CON_OUTDATE >= begin_date, table_name.S_CON_OUTDATE.is_(None)))
            if end_date is not None:
                query = query.filter(table_name.S_CON_INDATE <= end_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_sws_index_eod(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """申万指数行情"""
            table_name = ASWSINDEXEOD
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_index_hs300_close_weight(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                           columns=None):
            """沪深300指数成份股当日收盘权重信息"""
            table_name = AINDEXHS300CLOSEWEIGHT
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_financial_indicator(self, code=None, begin_date=None, end_date=None, report_period=None,
                                            columns=None):
            """中国A股财务指标"""
            table_name = ASHAREFINANCIALINDICATOR
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.REPORT_PERIOD, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_eod_derivative_indicator(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                                 columns=None):
            """中国A股日行情估值指标"""
            table_name = ASHAREEODDERIVATIVEINDICATOR
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_sw_industries_class(self, code=None, columns=None, trade_date=None):
            """申万行业分类"""
            table_name = ASHARESWINDUSTRIESCLASS
            query = self.query(table_name, columns)
            if trade_date is not None:
                query = query.filter(table_name.ENTRY_DT <= trade_date).filter(
                    or_(table_name.REMOVE_DT >= trade_date, table_name.REMOVE_DT.is_(None)))
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_swn_industries_class(self, code=None, columns=None, trade_date=None):
            """申万行业分类(2021)"""
            table_name = ASHARESWNINDUSTRIESCLASS
            query = self.query(table_name, columns)
            if trade_date is not None:
                query = query.filter(table_name.ENTRY_DT <= trade_date).filter(
                    or_(table_name.REMOVE_DT >= trade_date, table_name.REMOVE_DT.is_(None)))
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df



        def get_index_code_from_industry_name(self, industry_name='SW', level=1):
            industry_code_list = self.get_industry_code_from_industry_name(industry_name, level)
            index_code_list = self.get_index_code_from_industry_code(industry_code_list)[
                'S_INFO_INDEXCODE'].unique().tolist()
            return index_code_list

        def get_index_code_name_dict_from_industry_name(self, industry_name='SW', level=1):
            industry_code_list = self.get_industry_code_from_industry_name(industry_name, level)
            index_df = self.get_index_code_from_industry_code(industry_code_list)
            index_code_name_dict = index_df.set_index(['S_INFO_INDEXCODE'])['S_INFO_INDUSTRYNAME'].to_dict()
            return index_code_name_dict

        def get_a_index_industries_eod_citics(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                              columns=None):
            """中国A股中信行业指数日行情"""
            table_name = AINDEXINDUSTRIESEODCITICS
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_index_wind_industries_eod(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                            columns=None):
            """中国A股Wind行业指数日行情"""
            table_name = AINDEXWINDINDUSTRIESEOD
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_index_valuation(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """中国A股指数估值数据"""
            table_name = AINDEXVALUATION
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_index_description(self, code=None, columns=None):
            """中国A股指数基本资料"""
            table_name = AINDEXDESCRIPTION
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_industries_code(self, ind_code=None, ind_name=None, ind_code_like=None, level=None,
                                        columns=None):
            """行业代码"""
            table_name = ASHAREINDUSTRIESCODE
            query = self.query(table_name, columns)
            # 筛选条件
            if ind_code is not None:
                if isinstance(ind_code, str):
                    query = query.filter(table_name.INDUSTRIESCODE == ind_code)
                elif isinstance(ind_code, list):
                    query = query.filter(table_name.INDUSTRIESCODE.in_(ind_code))
            if ind_name is not None:
                if isinstance(ind_name, str):
                    query = query.filter(table_name.INDUSTRIESNAME == ind_name)
                elif isinstance(ind_name, list):
                    query = query.filter(table_name.INDUSTRIESNAME.in_(ind_name))
            if ind_code_like is not None:
                query = query.filter(table_name.INDUSTRIESCODE.like(ind_code_like))
            if level is not None:
                query = query.filter(table_name.LEVELNUM == level)
            # 查询数据
            df = self.read_sql(query)
            return df

        def get_a_index_hs300_free_weight(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                          columns=None):
            """沪深300免费指数权重"""
            table_name = AINDEXHS300FREEWEIGHT
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_calendar(self, market='SSE'):
            """中国A股交易日历表"""
            table_name = ASHARECALENDAR
            query = self.query(table_name).filter(
                table_name.S_INFO_EXCHMARKET == market).order_by(table_name.TRADE_DAYS)
            # 查询数据
            df = self.read_sql(query)
            return df



        def get_a_share_conception(self, code=None, date=None, columns=None):
            """中国A股Wind概念板块"""
            table_name = ASHARECONSEPTION
            query = self.query(table_name, columns)
            if date is None:
                date = datetime.datetime.now().strftime('%Y%m%d')
            query = query.filter(table_name.ENTRY_DT <= date).filter(
                or_(table_name.REMOVE_DT >= date,
                    table_name.REMOVE_DT.is_(None)))
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_industries_class_citics(self, code=None, columns=None):
            """中国A股中信行业分类"""
            table_name = ASHAREINDUSTRIESCLASSCITICS
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_a_share_placement_details(self,code=None,fund_code=None,columns=None):
            """中国A股网下配售机构获配明细"""

            table_name = ASHAREPLACEMENTDETAILS
            query = self.query(table_name, columns)
            if code is not None:
                query = query.filter(table_name.S_INFO_WINDCODE == code).filter(table_name.IS_SEOORIPO == 0)

            if fund_code is not None:
                query = query.outerjoin(CHINAMUTUALFUNDDESCRIPTION, ASHAREPLACEMENTDETAILS.S_INFO_COMPCODE == CHINAMUTUALFUNDDESCRIPTION.F_INFO_FUND_ID).filter(
                                                                             CHINAMUTUALFUNDDESCRIPTION.F_INFO_WINDCODE == fund_code
                ).order_by(table_name.ANN_DT)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df


        def get_a_share_ipo_inquiry_details(self,code=None,fund_code=None,columns=None):
            """IPO初步询价明细"""
            table_name = IPOINQUIRYDETAILS
            query = self.query(table_name, columns)
            if code is not None:
                query = query.filter(table_name.S_INFO_WINDCODE == code)
            if fund_code is not None:
                query = query.outerjoin(CHINAMUTUALFUNDDESCRIPTION,
                                        table_name.ISSUETARGETID == CHINAMUTUALFUNDDESCRIPTION.F_INFO_FUND_ID).filter(
                                        CHINAMUTUALFUNDDESCRIPTION.F_INFO_WINDCODE == fund_code
                ).order_by(table_name.ANN_DT)
            # 查询数据
            df = self.batch_query(query)
            return df


    if 'HK stock':
        # 港股
        def get_hk_share_eod_prices(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """香港股票日行情"""
            table_name = HKSHAREEODPRICES
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            if 'TRADE_DT' in df.columns:
                df.sort_values(by='TRADE_DT', inplace=True)
            return df

        def get_hk_share_description(self, code=None, columns=None):
            """香港股票基本资料"""
            table_name = HKSHAREDESCRIPTION
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_hk_index_eod_prices(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """香港股票指数日行情"""
            table_name = HKINDEXEODPRICES
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_global_index_eod(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """全球指数行情"""
            table_name = GLOBALINDEXEOD
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_hk_share_sw_industries_class(self, code=None, columns=None):
            """港股申万行业分类"""
            table_name = HKSHARESWINDUSTRIESCLASS
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_hk_stock_wind_industries_members(self, code=None, columns=None):
            """港股代码wind行业对应表"""
            table_name = HKSTOCKWINDINDUSTRIESMEMBERS
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_hk_stock_index_members(self, code=None, columns=None):
            """香港股票指数成份股"""
            table_name = HKSTOCKINDEXMEMBERS
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_hk_share_eod_derivative_index(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                              columns=None):
            """香港股票日行情估值指标"""
            table_name = HKSHAREEODDERIVATIVEINDEX
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.FINANCIAL_TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

    if 'fund':
        # 基金相关
        def get_china_etf_pch_redem_members(self, fund_code, begin_date=None, end_date=None, trade_date=None):
            table_name = CHINAETFPCHREDMMEMBERS
            query = self.query(table_name)
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, fund_code)
            return df

        def get_company_award(self, comp_code):
            table_name = COMPANYAWARD
            query = self.query(table_name)
            return self.batch_query(query, table_name.S_INFO_COMPCODE, comp_code)

        def get_related_fund_code(self, fund_code):
            table_name = CHINAMUTUALFUNDDESCRIPTION
            query = self.query(table_name).filter(table_name.F_INFO_WINDCODE == fund_code)
            df = self.read_sql(query)
            res = []
            if len(df) > 0:
                full_name = df['F_INFO_FULLNAME'].tolist()[0]
                query_name = self.query(table_name).filter(table_name.F_INFO_FULLNAME == full_name)
                df_related = self.read_sql(query_name)
                if len(df_related) > 0:
                    related_code_list = df_related['F_INFO_WINDCODE'].tolist()
                    res = related_code_list

            return res

        def _get_distinct_date_china_mutual_fund_asset_portfolio(self, code: str, begin_date: Optional[str] = None,
                                                                 end_date: Optional[str] = None,
                                                                 trade_date: Optional[str] = None) -> List[str]:
            """
            查询净值distinct的日期

            Args:
                code: 基金代码
                begin_date: 开始日期
                end_date: 结束日期
                trade_date: 交易日期

            Returns:
                date_list: 根据日期筛选出的Distinct日期
            """
            table_name = CHINAMUTUALFUNDASSETPORTFOLIO
            query = self.session.query(distinct(table_name.F_PRT_ENDDATE))
            query = query.filter(table_name.S_INFO_WINDCODE == code)
            # 筛选日期
            query = self.filter_date(query, table_name.F_PRT_ENDDATE, begin_date, end_date, trade_date)
            df = self.read_sql(query)
            date_list = df.iloc[:, 0].tolist()
            date_list.sort()
            return date_list

        def get_distinct_date_china_mutual_fund_asset_portfolio(self, code: Union[str, List[str]],
                                                                begin_date: Optional[str] = None,
                                                                end_date: Optional[str] = None,
                                                                trade_date: Optional[str] = None) -> Union[
            Dict, List[str]]:
            """
            查询净值distinct的日期

            Args:
                code: 基金代码
                begin_date: 开始日期
                end_date: 结束日期
                trade_date: 交易日期

            Returns:
                code_list: 根据日期筛选出的Distinct日期
            """
            if isinstance(code, str):
                date_list = self._get_distinct_date_china_mutual_fund_asset_portfolio(code, begin_date, end_date,
                                                                                      trade_date)
                return date_list
            if isinstance(code, list):
                res_dict = {}
                for c in code:
                    res_dict[c] = self._get_distinct_date_china_mutual_fund_asset_portfolio(c, begin_date, end_date,
                                                                                            trade_date)
                return res_dict

        def get_cmf_issuing_date_predict(self, fund_code: Union[str, list, None] = None, begin_date=None,
                                         end_date=None):
            table_name = CMFISSUINGDATEPREDICT
            query = self.session.query(table_name)
            if begin_date is not None:
                query = query.filter(table_name.START_DT == begin_date)
            if end_date is not None:
                query = query.filter(table_name.END_DT == end_date)
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, fund_code)
            return df

        def get_existing_china_mutual_fund_code(self, date=None) -> list:
            """
            获取存续的基金列表

            Args:
                date: 日期, 如果传入None, 则为获取最新基金列表

            Returns:
                存续的基金列表
            """
            table_name = CHINAMUTUALFUNDDESCRIPTION
            query = self.query(table_name, ['F_INFO_WINDCODE'])
            if date is None:
                date = datetime.datetime.now().strftime('%Y%m%d')
            query = query.filter(table_name.F_INFO_SETUPDATE <= date).filter(
                or_(table_name.F_INFO_MATURITYDATE >= date,
                    table_name.F_INFO_MATURITYDATE.is_(None)))
            existing_fund_list = self.read_sql(query)["F_INFO_WINDCODE"].tolist()
            existing_fund_list.sort()
            return existing_fund_list

        def get_all_fund_list(self) -> list:
            """
            获取全部的基金列表
            """
            table_name = CHINAMUTUALFUNDDESCRIPTION
            query = self.session.query(table_name.F_INFO_WINDCODE)
            all_fund_list = pd.read_sql(query.statement, self.engine)["F_INFO_WINDCODE"].tolist()
            return all_fund_list

        def get_existing_manager_list(self, date=None):
            """
            获取当前管理存续基金的基金经理
            """
            table_name = CHINAMUTUALFUNDMANAGER
            query = self.session.query(table_name.F_INFO_FUNDMANAGER_ID)
            if date is None:
                date = datetime.datetime.now()
            query = query.filter(table_name.F_INFO_MANAGER_STARTDATE <= date).filter(
                or_(table_name.F_INFO_MANAGER_LEAVEDATE >= date,
                    table_name.F_INFO_MANAGER_LEAVEDATE.is_(None)))
            existing_manager_list = pd.read_sql(query.statement, self.engine)["F_INFO_FUNDMANAGER_ID"].unique().tolist()
            return existing_manager_list

        def get_china_mutual_fund_nav_net_asset_total(self, code=None, begin_date=None, end_date=None, trade_date=None):
            """获取基金总资产"""
            table_name = CHINAMUTUALFUNDNAV
            query = self.query(table_name, ['F_INFO_WINDCODE', 'PRICE_DATE', 'NETASSET_TOTAL'])
            query = query.filter(table_name.NETASSET_TOTAL.isnot(None))
            # 筛选条件
            query = self.filter_date(query, table_name.PRICE_DATE, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_nav_f_prt_net_asset(self, code=None, begin_date=None, end_date=None, trade_date=None):
            """获取基金净资产"""
            table_name = CHINAMUTUALFUNDNAV
            query = self.query(table_name, ['F_INFO_WINDCODE', 'PRICE_DATE', 'F_PRT_NETASSET'])
            query = query.filter(table_name.F_PRT_NETASSET.isnot(None))
            # 筛选条件
            query = self.filter_date(query, table_name.PRICE_DATE, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_share_total(self, code=None, begin_date=None, end_date=None, trade_date=None):
            """基金合计总份额"""
            table_name = CHINAMUTUALFUNDSHARE
            query = self.query(table_name, columns=["F_INFO_WINDCODE", "CHANGE_DATE", "FUNDSHARE_TOTAL"])
            query = query.filter(table_name.FUNDSHARE_TOTAL.isnot(None))
            # 筛选条件
            query = self.filter_date(query, table_name.CHANGE_DATE, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        # def get_compound_fund_benchmark(self, code, begin_date=None, end_date=None, trade_date=None):
        #     """获取基金复合基准收盘价"""
        #     if isinstance(code, str):
        #         code = [code]
        #     df_res = pd.DataFrame()
        #     for c in code:
        #         # 1. 获取基金自身净值
        #         fund_nav_date = self.get_distinct_china_mutual_fund_nav_date(c, begin_date, end_date, trade_date)
        #         # 2. 根据类型获取市场基准， 取市场基准大于自身净值最小日期的部分
        #         fund_sector = self.get_fund_wind_sector_name(c)
        #         stock_fund_type = ['普通股票型基金', '被动指数型基金', '增强指数型基金', '偏股混合型基金', '平衡混合型基金',
        #                            '灵活配置型基金', '国际(QDII)股票型基金', '国际(QDII)混合型基金']
        #         # 市场基准
        #         if fund_sector in stock_fund_type:
        #             index_close_df = self.get_a_index_eod_prices("000300.SH", begin_date, end_date, trade_date)
        #         else:
        #             index_close_df = self.get_cb_index_eod_prices("h11001.CSI", begin_date, end_date, trade_date)
        #         index_close_series = index_close_df.set_index(['TRADE_DT'])['S_DQ_CLOSE']
        #         # 3. 获取基金自身基准
        #         benchmark_df = self.get_china_mutual_fund_benchmark_eod(c, begin_date, end_date, trade_date)
        #         if len(benchmark_df) > 0:
        #             benchmark_series = benchmark_df.set_index(['TRADE_DT'])['S_DQ_CLOSE']
        #         else:
        #             benchmark_series = pd.Series()
        #         # 4. 市场基准与自身基准分别求收益率，二者做连接，以自身基准为准
        #         index_pct_change = index_close_series.pct_change().dropna()
        #         bm_pct_change = benchmark_series.pct_change().dropna()
        #         diff_pct_change = index_pct_change.reindex(index_pct_change.index.difference(bm_pct_change.index))
        #         final_pct_change = pd.concat([diff_pct_change, bm_pct_change], axis=0)
        #         final_pct_change = final_pct_change.reindex(fund_nav_date).fillna(0)
        #         # 5. 收益率还原为指数，初始值为1
        #         final_nav = (final_pct_change + 1).cumprod()
        #         df = pd.DataFrame({"TRADE_DT": final_nav.index, "S_DQ_CLOSE": final_nav.values})
        #         df["S_INFO_WINDCODE"] = c
        #         if begin_date is not None:
        #             df = df[df['TRADE_DT'] >= begin_date]
        #         if end_date is not None:
        #             df = df[df['TRADE_DT'] <= end_date]
        #         if trade_date is not None:
        #             df = df[df['TRADE_DT'] == trade_date]
        #         df_res = df_res.append(df)
        #     return df_res

        def _get_distinct_china_mutual_fund_nav_date(self, code: str, begin_date: Optional[str] = None,
                                                     end_date: Optional[str] = None,
                                                     trade_date: Optional[str] = None) -> List[str]:
            """
            查询净值distinct的日期

            Args:
                code: 基金代码
                begin_date: 开始日期
                end_date: 结束日期
                trade_date: 交易日期

            Returns:
                date_list: 根据日期筛选出的Distinct日期
            """
            table_name = CHINAMUTUALFUNDNAV
            query = self.session.query(distinct(table_name.PRICE_DATE))
            query = query.filter(table_name.F_INFO_WINDCODE == code)
            # 筛选日期
            query = self.filter_date(query, table_name.PRICE_DATE, begin_date, end_date, trade_date)
            df = self.read_sql(query)
            date_list = df.iloc[:, 0].tolist()
            date_list.sort()
            return date_list

        def get_distinct_china_mutual_fund_nav_date(self, code: Union[str, List[str]], begin_date: Optional[str] = None,
                                                    end_date: Optional[str] = None,
                                                    trade_date: Optional[str] = None) -> Union[Dict, List[str]]:
            """
            查询净值distinct的日期

            Args:
                code: 基金代码
                begin_date: 开始日期
                end_date: 结束日期
                trade_date: 交易日期

            Returns:
                code_list: 根据日期筛选出的Distinct日期
            """
            if isinstance(code, str):
                date_list = self._get_distinct_china_mutual_fund_nav_date(code, begin_date, end_date, trade_date)
                return date_list
            if isinstance(code, list):
                res_dict = {}
                for c in code:
                    res_dict[c] = self._get_distinct_china_mutual_fund_nav_date(c, begin_date, end_date, trade_date)
                return res_dict

        def deprecate_get_index_close(self, index='000300.SH', today=None):
            """
            获取指数数据
            :param index: str或list或None, 需要查询的指数代码
            :param today: 截止日期. 当index传入的是str时, today会生效, 否则不生效
            :return: dict, 指数收盘价字典, Key是指数代码, Value是指数收盘价
            """
            if today is None:
                today = datetime.datetime.now().strftime('%Y%m%d')
            if type(index) is str:
                index_close = self.session.query(AINDEXEODPRICES.TRADE_DT, AINDEXEODPRICES.S_DQ_CLOSE) \
                    .filter(AINDEXEODPRICES.S_INFO_WINDCODE == index, AINDEXEODPRICES.TRADE_DT < today).order_by(
                    AINDEXEODPRICES.TRADE_DT)
                index_close_df = pd.read_sql(index_close.statement, self.engine)
                index_close_df.set_index(["TRADE_DT"], inplace=True)
                index_close_df.dropna(inplace=True)
                return np.array(index_close_df["S_DQ_CLOSE"]), np.array(index_close_df.index)
            elif type(index) is list:
                index_close = self.session.query(AINDEXEODPRICES).filter(AINDEXEODPRICES.S_INFO_WINDCODE.in_(index))
            else:
                index_close = self.session.query(AINDEXEODPRICES)
            index_close_df = pd.read_sql(index_close.statement, self.engine)
            grouped = index_close_df.groupby("S_INFO_WINDCODE")
            return {str(i[0]): i[1].sort_values(
                by="TRADE_DT", ascending=True
            ).dropna().reset_index(drop=True) for i in grouped}

        def get_china_mutual_fund_nav(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                      columns=None) -> pd.DataFrame:
            """查询基金行情"""
            table_name = CHINAMUTUALFUNDNAV
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.PRICE_DATE, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            if 'F_INFO_WINDCODE' in df.columns and 'PRICE_DATE' in df.columns:
                df.sort_values(by=['F_INFO_WINDCODE', 'PRICE_DATE'], inplace=True)
            return df

        def get_china_mutual_fund_nav_continuous(self, code: Union[str, List], begin_date=None, end_date=None,
                                                 trade_date=None, columns=None) -> pd.DataFrame:
            """
            查询基金行情, 对于中间缺失按交易日向下填充
            """

            def _fill_nav(df: pd.DataFrame, trade_date_list):
                df = df.set_index("PRICE_DATE").reindex(trade_date_list).fillna(method='pad').reset_index(drop=False)
                return df

            table_name = CHINAMUTUALFUNDNAV
            trade_date_list_all = self.get_a_index_eod_prices('000001.SH')['TRADE_DT'].values
            if isinstance(code, str):
                code = [code]
            df_res = pd.DataFrame()
            for c in code:
                query = self.query(table_name, columns)
                trade_date_list = trade_date_list_all.copy()
                date_list = np.array(self.get_distinct_china_mutual_fund_nav_date(c))
                # 取该基金最小净值以后的交易日
                if len(date_list) == 0:
                    continue
                trade_date_list = trade_date_list[trade_date_list >= date_list[0]]
                if begin_date is not None:
                    begin_date_pre_nav_date = TradeDateUtilsTemplate(date_list).get_previous_trading_date(begin_date)
                    query = query.filter(table_name.PRICE_DATE >= begin_date_pre_nav_date)
                    trade_date_list = trade_date_list[trade_date_list >= begin_date]
                if end_date is not None:
                    query = query.filter(table_name.PRICE_DATE <= end_date)
                    trade_date_list = trade_date_list[trade_date_list <= end_date]
                if trade_date is not None:
                    query = query.filter(table_name.PRICE_DATE == trade_date)
                    trade_date_list = trade_date_list[trade_date_list == trade_date]
                query = query.filter(table_name.F_INFO_WINDCODE == c)
                df = self.read_sql(query)
                df = _fill_nav(df, trade_date_list)
                df.sort_values(by='PRICE_DATE', inplace=True)
                df_res = df_res.append(df)
            return df_res

        def get_china_mutual_fund_nav_pct_chg(self, code: Union[str, List], begin_date=None, end_date=None,
                                              trade_date=None) -> pd.DataFrame:
            """
            查询基金行情, 返回收益率
            """
            table_name = CHINAMUTUALFUNDNAV
            query = self.query(table_name, ['F_INFO_WINDCODE', 'PRICE_DATE', 'F_NAV_ADJUSTED'])
            if isinstance(code, str):
                code = [code]
            df_res = pd.DataFrame()
            for c in code:
                date_list = np.array(self.get_distinct_china_mutual_fund_nav_date(c))
                # 取该基金最小净值以后的交易日
                if begin_date is not None:
                    begin_date_pre_nav_date = TradeDateUtilsTemplate(date_list).get_previous_trading_date(begin_date)
                    query = query.filter(table_name.PRICE_DATE >= begin_date_pre_nav_date)
                if end_date is not None:
                    query = query.filter(table_name.PRICE_DATE <= end_date)
                if trade_date is not None:
                    query = query.filter(table_name.PRICE_DATE == trade_date)
                query = query.filter(table_name.F_INFO_WINDCODE == c)
                df = self.read_sql(query)
                df.sort_values(by='PRICE_DATE', inplace=True)
                df['PCT_CHG'] = df["F_NAV_ADJUSTED"].pct_change()
                df_res = df_res.append(df[['F_INFO_WINDCODE', 'PRICE_DATE', 'PCT_CHG']].iloc[1:])
            return df_res

        def get_china_mutual_fund_nav_max_date(self, code: Union[str, List, None] = None, batch_size=500
                                               ) -> Union[str, Dict[str, str], None]:
            """
            查询公募基金行情最大日期

            Args:
                code: 基金代码
                batch_size: 当code为list时, 单次取数据库时基金代码数

            Returns:
                若code为str, 则返回该基金最大日期, 否则返回字典, Key为基金代码, Value为对应基金的最大日期
            """
            table_name = CHINAMUTUALFUNDNAV
            query = self.session.query(table_name.F_INFO_WINDCODE, func.max(table_name.PRICE_DATE)).group_by(
                table_name.F_INFO_WINDCODE)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code, batch_size=batch_size)
            if isinstance(code, str):
                if len(df) > 0:
                    return df.values[0][1]
                else:
                    return None
            else:
                return df.set_index("F_INFO_WINDCODE").iloc[:, 0].to_dict()

        def get_china_mf_performance(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                     columns=None) -> pd.DataFrame:
            """中国共同基金业绩表现"""
            table_name = CHINAMFPERFORMANCE
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mfm_performance(self, manager_id=None, begin_date=None, end_date=None,
                                      trade_date=None, columns=None) -> pd.DataFrame:
            """中国共同基金基金经理业绩表现"""
            table_name = CHINAMFMPERFORMANCE
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.FUNDMANAGER_ID, manager_id)
            return df

        def get_fund_out_date(self, fund_code: str):
            """
            获取基金的退市时间
            """
            query = self.session.query(CHINAMUTUALFUNDDESCRIPTION.F_INFO_MATURITYDATE).filter(
                CHINAMUTUALFUNDDESCRIPTION.F_INFO_WINDCODE == fund_code)
            date_list = pd.read_sql(query.statement, self.engine)['F_INFO_MATURITYDATE'].tolist()
            if len(date_list) > 0:
                out_date = date_list[0]
            else:
                out_date = None
            return out_date

        def get_china_mutual_fund_description(self, code=None, columns=None):
            """查询中国共同基金基本资料"""
            table_name = CHINAMUTUALFUNDDESCRIPTION
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_main_share(self, code=None, columns=None):
            """查询主份额基金"""
            table_name = CHINAMUTUALFUNDDESCRIPTION
            query = self.query(table_name, columns)
            query = query.filter(table_name.F_INFO_ISINITIAL == 1)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_distinct_china_mutual_fund_description(self):
            """获取所有共同基金代码"""
            table_name = CHINAMUTUALFUNDDESCRIPTION
            query = self.session.query(distinct(table_name.F_INFO_WINDCODE))
            df = self.read_sql(query)
            code_list = list(df.iloc[:, 0])
            return code_list

        def get_china_in_house_fund_description(self, code=None, columns=None):
            """中国券商理财基本资料"""
            table_name = CHINAINHOUSEFUNDDESCRIPTION
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_cmf_index_eod(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """中国共同基金指数行情"""
            table_name = CMFINDEXEOD
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_cmf_financial_indicator(self, code=None, begin_date=None, end_date=None, report_period=None,
                                        columns=None):
            """中国共同基金财务指标(报告期)"""
            table_name = CMFFINANCIALINDICATOR
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.REPORT_PERIOD, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_manager(self, code=None, manager_id=None, columns=None):
            """中国共同基金基金经理"""
            table_name = CHINAMUTUALFUNDMANAGER
            query = self.query(table_name, columns)
            # 筛选条件
            if code is not None:
                if isinstance(code, str):
                    query = query.filter(table_name.F_INFO_WINDCODE == code)
                elif isinstance(code, list):
                    query = query.filter(table_name.F_INFO_WINDCODE.in_(code))
            if manager_id is not None:
                if isinstance(manager_id, str):
                    query = query.filter(table_name.F_INFO_FUNDMANAGER_ID == manager_id)
                elif isinstance(manager_id, list):
                    query = query.filter(table_name.F_INFO_FUNDMANAGER_ID.in_(manager_id))
            # 查询数据
            df = self.read_sql(query)
            return df

        def get_china_mutual_fund_manager_by_fund(self, code=None, columns=None):
            """中国共同基金基金经理"""
            table_name = CHINAMUTUALFUNDMANAGER
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_manager_by_manager(self, manager_id=None, columns=None):
            """中国共同基金基金经理"""
            table_name = CHINAMUTUALFUNDMANAGER
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_FUNDMANAGER_ID, manager_id)
            return df

        def get_china_mutual_fund_sector(self, code=None, cur_sign=None, columns=None):
            """中国Wind基金分类"""
            table_name = CHINAMUTUALFUNDSECTOR
            query = self.query(table_name, columns)
            # 筛选条件
            if cur_sign is not None:
                query = query.filter(table_name.CUR_SIGN == cur_sign)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_sector_by_invest_type(self, code=None, columns=None):
            """中国Wind基金分类"""
            table_name = CHINAMUTUALFUNDSECTOR
            industry_like = '2001010%'
            query = self.query(table_name, columns).filter(table_name.S_INFO_SECTOR.like(industry_like))
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_fund_benchmark_mapping_code_bm(self, fund_code: Union[str, list, None] = None) -> Dict[str, str]:
            """
            获取基金本身代码->基金基准行情代码的映射

            Args:
                fund_code: 基金代码

            Returns:
                映射字典, Key为基金代码, Value为基准的代码

            Examples:
                >>> wind_data_reader.get_fund_benchmark_mapping_code_bm('110011.OF')
                {'110011.OF': '110011BI.WI'}
            """
            table_name = CHINAMUTUALFUNDDESCRIPTION
            query = self.session.query(table_name.F_INFO_WINDCODE)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, fund_code)
            df["bm"] = df['F_INFO_WINDCODE'].apply(lambda x: x.split('.')[0] + 'BI.WI')
            res_dict = df.set_index('F_INFO_WINDCODE')['bm'].to_dict()
            return res_dict

        def get_fund_benchmark_mapping_bm_code(self, fund_code: Union[str, list, None] = None) -> Dict[str, str]:
            """
            获取基金基准行情代码->基金本身代码的映射

            Args:
                fund_code: 基金代码

            Returns:
                映射字典, Key为基准代码, Value为基金代码

            Examples:
                >>> wind_data_reader.get_fund_benchmark_mapping_bm_code('110011.OF')
                {'110011BI.WI': '110011.OF'}
            """
            res_dict = self.get_fund_benchmark_mapping_code_bm(fund_code)
            return {v: k for k, v in res_dict.items()}

        def get_china_mutual_fund_benchmark_eod(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                                columns=None):
            """中国共同基金业绩比较基准行情"""
            table_name = CHINAMUTUALFUNDBENCHMARKEOD
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            code_bm = None
            if isinstance(code, str):
                code_bm = code[:6] + 'BI.WI'
            elif isinstance(code, list):
                code_bm = list(set([i[:6] + 'BI.WI' for i in code]))
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code_bm)
            # 根据基金代码与基准代码的映射表, 将基准代码转换成基金代码
            bm_code_mapping = self.get_fund_benchmark_mapping_bm_code(code)
            df['S_INFO_WINDCODE'] = df['S_INFO_WINDCODE'].map(bm_code_mapping)
            if 'S_INFO_WINDCODE' in df.columns and 'TRADE_DT' in df.columns:
                df.sort_values(by=['S_INFO_WINDCODE', 'TRADE_DT'], inplace=True)
            return df

        def get_china_mutual_fund_benchmark_eod_by_bm_code(self, code=None, begin_date=None, end_date=None,
                                                           trade_date=None,
                                                           columns=None):
            """中国共同基金业绩比较基准行情"""
            table_name = CHINAMUTUALFUNDBENCHMARKEOD
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_fund_benchmark_eod(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                   columns=None):
            """基金自身基准行情"""
            table_name = CHINAMUTUALFUNDBENCHMARKEOD
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_existing_china_mutual_fund_benchmark_code(self, begin_date=None, end_date=None, trade_date=None):
            table_name = CHINAMUTUALFUNDBENCHMARKEOD
            query = self.session.query(distinct(table_name.S_INFO_WINDCODE))
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            benchmark_code_list = pd.read_sql(query.statement, self.engine)["S_INFO_WINDCODE"].unique().tolist()
            existing_fund_list = self.get_existing_china_mutual_fund_code()
            fund_list = set(code[:6] for code in existing_fund_list)
            bm_code_list = set([i[:6] for i in benchmark_code_list])
            existing_benchmark_code_list = [code + "BI.WI" for code in bm_code_list.intersection(fund_list)]
            return existing_benchmark_code_list

        def get_china_mutual_fund_share(self, code=None, begin_date=None, end_date=None, report_period=None,
                                        columns=None):
            """中国共同基金份额"""
            table_name = CHINAMUTUALFUNDSHARE
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.CHANGE_DATE, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_fund_asset(self, fund_code, end_date=None):
            fund_share = self.session.query(CHINAMUTUALFUNDSHARE.FUNDSHARE).filter(
                CHINAMUTUALFUNDSHARE.F_INFO_WINDCODE == fund_code)
            fund_nav = self.session.query(CHINAMUTUALFUNDNAV.F_NAV_UNIT).filter(
                CHINAMUTUALFUNDNAV.F_INFO_WINDCODE == fund_code)
            if end_date is not None:
                fund_share = fund_share.filter(CHINAMUTUALFUNDSHARE.CHANGE_DATE <= end_date)
                fund_nav = fund_nav.filter(CHINAMUTUALFUNDNAV.PRICE_DATE <= end_date)
            fund_share = fund_share.order_by(CHINAMUTUALFUNDSHARE.CHANGE_DATE.desc()).limit(1)
            fund_nav = fund_nav.order_by(CHINAMUTUALFUNDNAV.PRICE_DATE.desc()).limit(1)
            logger.info(f'{fund_code}-{end_date}查询share数据开始')
            fund_share_df = pd.read_sql(fund_share.statement, self.engine)
            logger.info(f'{fund_code}-{end_date}查询nav数据开始')
            fund_nav_df = pd.read_sql(fund_nav.statement, self.engine)
            logger.info(f'{fund_code}-{end_date}查询nav数据结束')
            fund_asset = None
            if (not fund_share_df.empty) and (not fund_nav_df.empty):
                nav_unit = fund_share_df.loc[0, 'FUNDSHARE']
                share = fund_nav_df.loc[0, 'F_NAV_UNIT']
                fund_asset = nav_unit * share * 10000
            return fund_asset

        def get_fund_asset_share_all(self, fund_code, trade_date):
            fund_share = self.session.query(CHINAMUTUALFUNDSHARE.FUNDSHARE, CHINAMUTUALFUNDSHARE.CHANGE_DATE).filter(
                CHINAMUTUALFUNDSHARE.F_INFO_WINDCODE == fund_code, CHINAMUTUALFUNDSHARE.F_UNIT_MERGEDSHARESORNOT == 0) \
                .order_by(CHINAMUTUALFUNDSHARE.CHANGE_DATE.desc())
            fund_share_df = pd.read_sql(fund_share.statement, self.engine).set_index('CHANGE_DATE')

            fund_net_asset = self.session.query(CHINAMUTUALFUNDNAV.F_PRT_NETASSET, CHINAMUTUALFUNDNAV.PRICE_DATE) \
                .filter(CHINAMUTUALFUNDNAV.F_INFO_WINDCODE == fund_code,
                        CHINAMUTUALFUNDNAV.F_ASSET_MERGEDSHARESORNOT == 0) \
                .order_by(CHINAMUTUALFUNDNAV.PRICE_DATE.desc())

            fund_net_asset_df = pd.read_sql(fund_net_asset.statement, self.engine).set_index('PRICE_DATE')
            fund_net_asset_df['product_share'] = fund_share_df['FUNDSHARE'] * 10000
            result = None
            if not fund_net_asset_df.empty or not fund_share_df.empty:
                index_min = min(fund_net_asset_df.index)
                index_max = max(fund_net_asset_df.index)
                trade_date_list = list(trade_date[(trade_date >= index_min) & (trade_date <= index_max)])
                index_list = list(set(trade_date_list).union(set(fund_net_asset_df.index)))
                index_list.sort()

                result = pd.DataFrame(index=index_list)
                result['product_share'] = fund_share_df['FUNDSHARE']
                result['product_asset'] = fund_net_asset_df['F_PRT_NETASSET']
                result['fund_code'] = fund_code
                result = result.fillna(method='ffill')
                result = result.reindex(index=trade_date_list).dropna()
            return result

        def get_cmf_holder_structure(self, code=None, begin_date=None, end_date=None, report_period=None, columns=None):
            """中国共同基金持有人结构"""
            table_name = CMFHOLDERSTRUCTURE
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.END_DT, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def _get_distinct_cmf_holder_structure_date(self, code: str, begin_date: Optional[str] = None,
                                                    end_date: Optional[str] = None,
                                                    trade_date: Optional[str] = None) -> List[str]:
            """
            查询cmf_holder_structure的distinct日期

            Args:
                code: 基金代码
                begin_date: 开始日期
                end_date: 结束日期
                trade_date: 交易日期

            Returns:
                code_list: 根据日期筛选出的Distinct日期
            """
            table_name = CMFHOLDERSTRUCTURE
            query = self.session.query(distinct(table_name.END_DT))
            query = query.filter(table_name.S_INFO_WINDCODE == code)
            query = self.filter_date(query, table_name.END_DT, begin_date, end_date, trade_date)

            df = self.read_sql(query)
            code_list = df.iloc[:, 0].tolist()
            code_list.sort()
            return code_list

        def get_distinct_cmf_holder_structure_date(self, code: Union[str, List[str]], begin_date: Optional[str] = None,
                                                   end_date: Optional[str] = None,
                                                   trade_date: Optional[str] = None) -> Union[Dict, List[str]]:
            """
            查询净值distinct的日期

            Args:
                code: 基金代码
                begin_date: 开始日期
                end_date: 结束日期
                trade_date: 交易日期

            Returns:
                code_list: 根据日期筛选出的Distinct日期
            """
            if isinstance(code, str):
                date_list = self._get_distinct_cmf_holder_structure_date(code, begin_date, end_date, trade_date)
                return date_list
            if isinstance(code, list):
                res_dict = {}
                for c in code:
                    res_dict[c] = self._get_distinct_cmf_holder_structure_date(c, begin_date, end_date, trade_date)
                return res_dict

        def get_cmf_mg_qualifications(self, manager_id, columns=None):
            table_name = CMFMGQUALIFICATIONS
            query = self.query(table_name, columns)
            return self.batch_query(query, table_name.F_INFO_FUNDMANAGER_ID, manager_id)

        def get_c_fund_introduction_by_name(self, company_short_name=None, columns=None):
            """中国基金公司简介-通过short name查询"""
            table_name = CFUNDINTRODUCTION
            query = self.query(table_name, columns)
            return self.batch_query(query, table_name.COMP_SNAME, company_short_name)

        def get_c_fund_introduction_by_id(self, company_id=None, columns=None):
            """中国基金公司简介-通过company id查询"""
            table_name = CFUNDINTRODUCTION
            query = self.query(table_name, columns)
            return self.batch_query(query, table_name.COMP_ID, company_id)

        def get_china_mutual_fund_asset_portfolio(self, code=None, begin_date=None, end_date=None, report_period=None,
                                                  columns=None):
            """中国共同基金投资组合-资产配置"""
            table_name = CHINAMUTUALFUNDASSETPORTFOLIO
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.F_PRT_ENDDATE, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_stock_portfolio(self, code=None, begin_date=None, end_date=None, report_period=None,
                                                  columns=None):
            """中国共同基金投资组合——持股明细"""
            table_name = CHINAMUTUALFUNDSTOCKPORTFOLIO
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.F_PRT_ENDDATE, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_stock_portfolio_by_date_bak(self, report_period, is_top10=False):
            """
            基金的股票投资组合, 控制是否取前十大
            """
            df_portfolio = pd.DataFrame()
            if is_top10:
                table_name = CHINAMUTUALFUNDSTOCKPORTFOLIO
                query = self.query(table_name).filter(table_name.F_PRT_ENDDATE == report_period)
                df_portfolio_all = self.read_sql(query)
                for fund_code, grouped in df_portfolio_all.groupby('S_INFO_WINDCODE'):
                    grouped['rank'] = grouped['F_PRT_STKVALUE'].rank(method='min')
                    df_portfolio = df_portfolio.append(grouped[grouped['rank'] <= 10])  # 排名一致则都取出
            else:
                # 取全部持仓, 则从公告日期表找出已有半年报/年报的基金
                start_date = report_period[:4] + '0101'
                df_issue_date = self.get_cmf_issuing_date_predict(begin_date=start_date, end_date=report_period)
                code_list = df_issue_date['S_INFO_WINDCODE'].tolist()
                df_portfolio = self.get_china_mutual_fund_stock_portfolio(code=code_list,
                                                                          report_period=report_period)
            return df_portfolio

        def get_china_mutual_fund_stock_portfolio_by_date(self, report_period, is_top10=False, fund_code=None):
            """
            基金的股票投资组合
            """
            table_name = CHINAMUTUALFUNDSTOCKPORTFOLIO
            query = self.query(table_name).filter(table_name.F_PRT_ENDDATE == report_period)
            df_portfolio_all = self.batch_query(query, table_name.S_INFO_WINDCODE, fund_code)

            df_portfolio = pd.DataFrame()
            if is_top10:
                for fund_code, grouped in df_portfolio_all.groupby('S_INFO_WINDCODE'):
                    grouped['rank'] = grouped['F_PRT_STKVALUE'].rank(method='min')
                    df_portfolio = df_portfolio.append(grouped[grouped['rank'] <= 10])  # 排名一致则都取出
            else:
                # 取全部持仓, 则从公告日期表找出已有半年报/年报的基金
                start_date = report_period[:4] + '0101'
                df_issue_date = self.get_cmf_issuing_date_predict(begin_date=start_date, end_date=report_period)
                code_list = df_issue_date['S_INFO_WINDCODE'].tolist()
                df_portfolio = df_portfolio_all[df_portfolio_all['S_INFO_WINDCODE'].isin(code_list)]
            return df_portfolio

        def get_china_mutual_fund_stock_portfolio_by_code(self, code, is_top10=False, begin_date=None, end_date=None,
                                                          report_period=None):
            table_name = CHINAMUTUALFUNDSTOCKPORTFOLIO
            query = self.query(table_name)
            query = self.filter_date(query, table_name.F_PRT_ENDDATE, begin_date, end_date, report_period)
            df_portfolio_all = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            if not is_top10:
                df_portfolio = df_portfolio_all
            else:
                df_portfolio = pd.DataFrame()
                for _, grouped in df_portfolio_all.groupby(['F_PRT_ENDDATE', 'S_INFO_WINDCODE']):
                    grouped['rank'] = grouped['F_PRT_STKVALUE'].rank(method='min', ascending=False)
                    df_portfolio = df_portfolio.append(grouped[grouped['rank'] <= 10])  # 排名一致则都取出
            return df_portfolio

        def get_distinct_fund_code_china_mutual_fund_stock_portfolio(self):
            table_name = CHINAMUTUALFUNDSTOCKPORTFOLIO
            query = self.query(distinct(table_name.S_INFO_WINDCODE))
            df = self.read_sql(query)
            code_list = df.iloc[:, 0].tolist()
            code_list.sort()
            return code_list

        def get_distinct_fund_code_china_mutual_fund_asset_portfolio(self):
            table_name = CHINAMUTUALFUNDASSETPORTFOLIO
            query = self.query(distinct(table_name.S_INFO_WINDCODE))
            df = self.read_sql(query)
            code_list = df.iloc[:, 0].tolist()
            code_list.sort()
            return code_list

        def get_china_mutual_fund_asset_portfolio_by_code(self, code, begin_date=None, end_date=None,
                                                          report_period=None):
            table_name = CHINAMUTUALFUNDASSETPORTFOLIO
            query = self.query(table_name)
            query = self.filter_date(query, table_name.F_PRT_ENDDATE, begin_date, end_date, report_period)
            df_portfolio = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df_portfolio

        def get_china_mutual_fund_ind_portfolio(self, code=None, begin_date=None, end_date=None, report_period=None,
                                                columns=None):
            """中国共同基金投资组合——行业配置"""
            table_name = CHINAMUTUALFUNDINDPORTFOLIO
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.F_PRT_ENDDATE, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_distinct_bond_code_china_mutual_fund_bond_portfolio(self) -> List:
            table_name = CHINAMUTUALFUNDBONDPORTFOLIO
            query = self.session.query(distinct(table_name.S_INFO_BONDWINDCODE))
            df = self.read_sql(query)
            code_list = df.iloc[:, 0].tolist()
            code_list.sort()
            return code_list

        def get_china_mutual_fund_bond_portfolio(self, code=None, begin_date=None, end_date=None, report_period=None,
                                                 columns=None):
            """中国共同基金投资组合-持券明细"""
            table_name = CHINAMUTUALFUNDBONDPORTFOLIO
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.F_PRT_ENDDATE, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_bond_portfolio_report_period(self, fund_code=None):
            table_name = CHINAMUTUALFUNDBONDPORTFOLIO
            query = self.query(table_name).filter(or_(CHINAMUTUALFUNDBONDPORTFOLIO.F_PRT_ENDDATE.like('%0331%'),
                                                      CHINAMUTUALFUNDBONDPORTFOLIO.F_PRT_ENDDATE.like('%0630%'),
                                                      CHINAMUTUALFUNDBONDPORTFOLIO.F_PRT_ENDDATE.like('%0930%'),
                                                      CHINAMUTUALFUNDBONDPORTFOLIO.F_PRT_ENDDATE.like('%1231%')))
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, fund_code)
            return df

        def get_cmf_other_portfolio(self, code=None, begin_date=None, end_date=None, report_period=None, columns=None):
            """中国共同基金投资组合——其他证券"""
            table_name = CMFOTHERPORTFOLIO
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.END_DT, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_issue(self, code=None, columns=None):
            """中国共同基金发行"""
            table_name = CHINAMUTUALFUNDISSUE
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_suspend_pch_redm(self, code=None, columns=None):
            """中国共同基金暂停申购赎回"""
            table_name = CHINAMUTUALFUNDSUSPENDPCHREDM
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_pch_redm(self, code=None, columns=None):
            """中国共同基金申购赎回"""
            table_name = CHINAMUTUALFUNDPCHREDM
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_lof_pch_redm(self, code=None, columns=None):
            """中国开放式基金场内申购赎回"""
            table_name = LOFPCHREDM
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_etf_pch_redm(self, code=None, columns=None):
            """中国ETF申购赎回"""
            table_name = ETFPCHREDM
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_closed_fund_pch_redm(self, code=None, columns=None):
            """中国封闭式基金场内申购赎回"""
            table_name = CLOSEDFUNDPCHREDM
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_cmf_subred_fee(self, code=None, columns=None):
            """中国开放式基金费率表"""
            table_name = CMFSUBREDFEE
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mf_dividend(self, code=None, columns=None):
            """中国共同基金分红"""
            table_name = CHINAMFDIVIDEND
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_fund_pch_redm(self, code=None, columns=None):
            """中国共同基金申购赎回天数"""
            table_name = CFUNDPCHREDM
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_cm_fund_split(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """中国共同基金基金份额拆分与折算"""
            table_name = CMFUNDSPLIT
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.F_INFO_SHARETRANSDATE, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_tracking_index(self, code=None, columns=None):
            """中国共同基金被动型基金跟踪指数"""
            table_name = CHINAMUTUALFUNDTRACKINGINDEX
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_fund_rate_sensitive(self, code=None, begin_date=None, end_date=None, report_period=None,
                                      columns=None):
            """中国共同基金利率敏感分析"""
            table_name = CFUNDRATESENSITIVE
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.REPORT_PERIOD, begin_date, end_date, report_period)
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, code)
            return df

        def get_china_mutual_fund_transformation(self, pre_code=None, post_code=None, columns=None):
            """中国共同基金转型"""
            table_name = CHINAMUTUALFUNDTRANSFORMATION
            query = self.query(table_name, columns)
            # 筛选条件
            if pre_code is not None:
                if isinstance(pre_code, str):
                    query = query.filter(table_name.PREWINDCODE == pre_code)
                elif isinstance(pre_code, list):
                    query = query.filter(table_name.PREWINDCODE.in_(pre_code))
            if post_code is not None:
                if isinstance(post_code, str):
                    query = query.filter(table_name.POSTWINDCODE == post_code)
                elif isinstance(post_code, list):
                    query = query.filter(table_name.POSTWINDCODE.in_(post_code))
            # 查询数据
            df = self.read_sql(query)
            return df

        def get_cmf_code_and_s_name(self, code=None, columns=None):
            """中国共同基金业务代码及简称"""
            table_name = CMFCODEANDSNAME
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_money_market_daily_f_income(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                              columns=None):
            """中国货币式基金日收益(拆分)"""
            table_name = CMONEYMARKETDAILYFINCOME
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.F_INFO_ENDDATE, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_cmm_quarterly_data(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """中国货币式基金日收益(拆分)"""
            table_name = CMMQUARTERLYDATA
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.F_INFO_ENDDATE, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_china_closed_fund_eod_price(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                            columns=None):
            """中国上市基金日行情"""
            table_name = CHINACLOSEDFUNDEODPRICE
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def _get_distinct_china_closed_fund_eod_price_date(self, code: str, begin_date: Optional[str] = None,
                                                           end_date: Optional[str] = None,
                                                           trade_date: Optional[str] = None) -> List[str]:
            """
            查询cmf_holder_structure的distinct日期

            Args:
                code: 基金代码
                begin_date: 开始日期
                end_date: 结束日期
                trade_date: 交易日期

            Returns:
                code_list: 根据日期筛选出的Distinct日期
            """
            table_name = CHINACLOSEDFUNDEODPRICE
            query = self.session.query(distinct(table_name.TRADE_DT))
            query = query.filter(table_name.S_INFO_WINDCODE == code)
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            df = self.read_sql(query)
            code_list = df.iloc[:, 0].tolist()
            code_list.sort()
            return code_list

        def get_distinct_china_closed_fund_eod_price_date(self, code: Union[str, List[str]],
                                                          begin_date: Optional[str] = None,
                                                          end_date: Optional[str] = None,
                                                          trade_date: Optional[str] = None) -> Union[Dict, List[str]]:
            """
            查询distinct的日期

            Args:
                code: 基金代码
                begin_date: 开始日期
                end_date: 结束日期
                trade_date: 交易日期

            Returns:
                code_list: 根据日期筛选出的Distinct日期
            """
            if isinstance(code, str):
                date_list = self._get_distinct_china_closed_fund_eod_price_date(code, begin_date, end_date, trade_date)
                return date_list
            if isinstance(code, list):
                res_dict = {}
                for c in code:
                    res_dict[c] = self._get_distinct_china_closed_fund_eod_price_date(c, begin_date, end_date,
                                                                                      trade_date)
                return res_dict

        def get_china_mutual_fund_float_share(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                              columns=None):
            """中国共同基金场内流通份额"""
            table_name = CHINAMUTUALFUNDFLOATSHARE
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_wind_industry_map_code_name(self, level=None):
            """
            获取行业代码与行业名称映射

            Returns
            -------
            """
            if level is not None:
                level = level + 3
            df_industry_code = self.get_a_share_industries_code(ind_code_like="200101%", level=level)
            industry_map = df_industry_code.set_index("INDUSTRIESCODE")["INDUSTRIESNAME"].to_dict()
            if level == 2:
                industry_map["2001010400000000"] = "货币市场型基金"
            return industry_map

        def get_wind_industry_map_name_code(self, level=None) -> Dict[str, str]:
            """
            获取行业名称与行业代码的映射
            """
            res_dict = self.get_wind_industry_map_code_name(level)
            return {v: k for k, v in res_dict.items()}

        def get_fund_wind_sector_name(self, fund_code: Union[str, List[str], None] = None,
                                      date: Optional[str] = None, level=2):
            """获取基金的Wind分类名称"""
            res = self.get_fund_wind_sector_code(fund_code, date, level)
            wind_industry_map = self.get_wind_industry_map_code_name()
            if isinstance(fund_code, str):
                if res not in wind_industry_map:
                    return "其他"
                else:
                    return wind_industry_map[res]
            else:
                return pd.Series(res).map(wind_industry_map).fillna("其他").to_dict()

        def get_fund_wind_sector_code(self, fund_code: Union[str, List[str], None] = None,
                                      date: Optional[str] = None, level=2):
            """
            获取基金的Wind分类

            Args:
                fund_code: 基金代码
                date: 日期, 默认为None, 若为None表示最新日期
                level: 分类层级, 默认二级分类

            Returns:
                若传入的基金代码是str, 则返回基金分类
                若传入的基金代码是None或list, 则返回基金分类字典
            """
            table_name = CHINAMUTUALFUNDSECTOR
            query = self.query(table_name).filter(table_name.S_INFO_SECTOR.like("200101%"))
            if date is not None:
                query = query.filter(table_name.S_INFO_SECTORENTRYDT <= date).filter(
                    or_(table_name.S_INFO_SECTOREXITDT >= date,
                        table_name.S_INFO_SECTOREXITDT.is_(None)))
            else:
                query = query.filter(table_name.S_INFO_SECTOREXITDT.is_(None))
            # 查询数据
            df = self.batch_query(query, table_name.F_INFO_WINDCODE, fund_code)
            if level == 1:
                # Wind一级分类, 8位代码 + 8个0, 如2001010100000000代表股票型基金
                df["S_INFO_SECTOR"] = df["S_INFO_SECTOR"].apply(lambda x: x[:8] + '0' * 8)
            elif level == 2:
                # Wind二级分类, 10位代码 + 6个0, 如2001010101000000代表普通股票型基金
                df["S_INFO_SECTOR"] = df["S_INFO_SECTOR"].apply(lambda x: x[:10] + '0' * 6)
            elif level == 3:
                # Wind三级分类, 12位代码+4个0, 如2001010801010000代表国际(QDII)普通股票型基金
                # 注意只有国际(QDII)基金、FOF基金存在三级分类
                df["S_INFO_SECTOR"] = df["S_INFO_SECTOR"].apply(lambda x: x[:12] + '0' * 4)

            df["S_INFO_SECTOR"] = df["S_INFO_SECTOR"].fillna("其他")
            if fund_code is not None and isinstance(fund_code, str):
                if len(df["S_INFO_SECTOR"]) > 0:
                    return df["S_INFO_SECTOR"].values[0]
                else:
                    return "其他"
            else:
                return df.set_index("F_INFO_WINDCODE")["S_INFO_SECTOR"].to_dict()

        def get_fund_code_by_wind_sector(self, sector_code):
            """
            根据类型获取基金代码列表
            """
            fund_sector = self.session.query(CHINAMUTUALFUNDSECTOR).filter(
                CHINAMUTUALFUNDSECTOR.S_INFO_SECTOR.like(sector_code),
                CHINAMUTUALFUNDSECTOR.S_INFO_SECTORENTRYDT.isnot(None),
                CHINAMUTUALFUNDSECTOR.CUR_SIGN == 1)
            df_fund_sector = pd.read_sql(fund_sector.statement, self.engine)
            code_list = df_fund_sector['F_INFO_WINDCODE'].unique().tolist()
            return code_list

        def get_fund_code_by_wind_sector_code(self, sector_code, level=2):
            """
            根据类型代码获取基金代码列表
            """
            fund_sector = self.session.query(CHINAMUTUALFUNDSECTOR).filter(
                CHINAMUTUALFUNDSECTOR.S_INFO_SECTORENTRYDT.isnot(None),
                CHINAMUTUALFUNDSECTOR.CUR_SIGN == 1)
            if level is None:
                fund_sector = fund_sector.filter(CHINAMUTUALFUNDSECTOR.S_INFO_SECTOR == sector_code)
            elif level == 1:
                fund_sector = fund_sector.filter(CHINAMUTUALFUNDSECTOR.S_INFO_SECTOR.startswith(sector_code[:8]))
            elif level == 2:
                fund_sector = fund_sector.filter(CHINAMUTUALFUNDSECTOR.S_INFO_SECTOR.startswith(sector_code[:10]))
            else:
                fund_sector = fund_sector.filter(CHINAMUTUALFUNDSECTOR.S_INFO_SECTOR.startswith(sector_code[:12]))

            df_fund_sector = pd.read_sql(fund_sector.statement, self.engine)
            code_list = df_fund_sector['F_INFO_WINDCODE'].unique().tolist()
            return code_list

        def get_parent_code(self, fund_code: str):
            """
            查看母基金代码
            """
            table_name = CHINAMUTUALFUNDDESCRIPTION
            query = self.session.query(table_name).filter(table_name.F_INFO_WINDCODE == fund_code)
            df = self.read_sql(query)
            if len(df) > 0:
                full_name = df['F_INFO_FULLNAME'].tolist()[0]
                query = self.session.query(table_name).filter(table_name.F_INFO_FULLNAME == full_name,
                                                              table_name.F_INFO_ISINITIAL == 1)
                df_parent = self.read_sql(query)
                if len(df_parent) > 0:
                    parent_code = df_parent['F_INFO_WINDCODE'].tolist()[0]
                    if parent_code == fund_code:
                        return None
                    else:
                        return parent_code
            return None

        def get_china_mutual_fund_issue_name(self, fund_code: str):
            """获取共同基金发行名称"""
            table_name = CHINAMUTUALFUNDISSUE
            query = self.session.query(table_name.S_INFO_WINDCODE, table_name.F_INFO_SHORTNAME).filter(
                table_name.S_INFO_WINDCODE == fund_code)
            df = self.read_sql(query)
            if len(df) > 0:
                return df['F_INFO_SHORTNAME'].values.tolist()[0]
            else:
                return None

        def get_china_mutual_fund_issue_name_dict(self, fund_list: List) -> Dict[str, str]:
            """
            获取基金名称字典

            Args:
                fund_list: 基金列表, 需要获取的基金列表

            Returns:
                基金名称字典, Key为基金代码, Value为基金名称
            """
            table = CHINAMUTUALFUNDISSUE
            query = self.query(table, ["S_INFO_WINDCODE", "F_INFO_SHORTNAME"])
            fund_name_df = self.batch_query(query, table.S_INFO_WINDCODE, fund_list)
            fund_name_df.set_index("S_INFO_WINDCODE", inplace=True)
            fund_name_df = fund_name_df[~fund_name_df.index.duplicated(keep='first')]
            fund_name_dict = dict(fund_name_df['F_INFO_SHORTNAME'])
            return fund_name_dict

        def get_manager_manage_fund_list(self, manager_id: str, date: Optional[str] = None) -> List:
            """
            获取基金经理管理基金列表

            Args:
                manager_id: 基金经理ID
                date: 日期, 默认为None, 表示最新日期, 若为"all"表示管理的全部基金, 若为日期则表示当时在管的基金

            Returns:
                该基金经理管理的基金列表
            """
            table_name = CHINAMUTUALFUNDMANAGER
            query = self.query(table_name).filter(table_name.F_INFO_FUNDMANAGER_ID == manager_id)
            if date is None:
                query = query.filter(table_name.F_INFO_MANAGER_LEAVEDATE.is_(None))
            elif date.upper() != "ALL":
                query = query.filter(table_name.F_INFO_MANAGER_STARTDATE >= date).filter(
                    or_(table_name.F_INFO_MANAGER_LEAVEDATE <= date,
                        table_name.F_INFO_MANAGER_LEAVEDATE.is_(None)))
            df = self.read_sql(query)
            return df["F_INFO_WINDCODE"].unique().tolist()

        def get_netasset_fundshare_from_list(self, fund_list=None):
            """
            获取基本信息下的资产规模数据
            """
            if fund_list is not None:
                # 资产数据
                fund_asset = self.session.query(CHINAMUTUALFUNDNAV.F_INFO_WINDCODE, CHINAMUTUALFUNDNAV.PRICE_DATE,
                                                CHINAMUTUALFUNDNAV.F_PRT_NETASSET).filter(
                    CHINAMUTUALFUNDNAV.F_INFO_WINDCODE.in_(fund_list), CHINAMUTUALFUNDNAV.F_PRT_NETASSET != None,
                                                                       CHINAMUTUALFUNDNAV.F_ASSET_MERGEDSHARESORNOT == 0)
                # 份额数据
                fund_share = self.session.query(CHINAMUTUALFUNDSHARE.F_INFO_WINDCODE, CHINAMUTUALFUNDSHARE.CHANGE_DATE,
                                                CHINAMUTUALFUNDSHARE.FUNDSHARE).filter(
                    CHINAMUTUALFUNDSHARE.F_INFO_WINDCODE.in_(fund_list), CHINAMUTUALFUNDSHARE.FUNDSHARE != None,
                                                                         CHINAMUTUALFUNDSHARE.F_UNIT_MERGEDSHARESORNOT == 0)
            else:
                fund_asset = self.session.query(CHINAMUTUALFUNDNAV.F_INFO_WINDCODE, CHINAMUTUALFUNDNAV.PRICE_DATE,
                                                CHINAMUTUALFUNDNAV.F_PRT_NETASSET).filter(
                    CHINAMUTUALFUNDNAV.F_PRT_NETASSET != None, CHINAMUTUALFUNDNAV.F_ASSET_MERGEDSHARESORNOT == 0)
                fund_share = self.session.query(CHINAMUTUALFUNDSHARE.F_INFO_WINDCODE, CHINAMUTUALFUNDSHARE.CHANGE_DATE,
                                                CHINAMUTUALFUNDSHARE.FUNDSHARE).filter(
                    CHINAMUTUALFUNDSHARE.FUNDSHARE != None, CHINAMUTUALFUNDSHARE.F_UNIT_MERGEDSHARESORNOT == 0)
            fund_asset_df = pd.read_sql(fund_asset.statement, self.engine)
            # 使用code+时间作为唯一标识合并数据
            fund_asset_df['code_date'] = fund_asset_df.F_INFO_WINDCODE + fund_asset_df.PRICE_DATE

            fund_share_df = pd.read_sql(fund_share.statement, self.engine)
            fund_share_df['FUNDSHARE'] = fund_share_df['FUNDSHARE'] * 1e4
            fund_share_df['code_date'] = fund_share_df.F_INFO_WINDCODE + fund_share_df.CHANGE_DATE
            df_netasset_fundsahre = pd.merge(fund_asset_df[['code_date', 'F_PRT_NETASSET']],
                                             fund_share_df[['code_date', 'FUNDSHARE']],
                                             on='code_date', how='inner')
            return df_netasset_fundsahre.dropna()

    if 'bond':
        # 债券相关
        def get_c_bond_eod_prices(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """沪深交易所债券的行情数据"""
            table_name = CBONDEODPRICES
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_cb_index_eod_prices(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """债券指数的日收盘行情"""
            table_name = CBINDEXEODPRICES
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            if 'TRADE_DT' in df.columns:
                df.sort_values(by='TRADE_DT', inplace=True)
            return df

        def get_c_bond_index_eod_cnbd(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            table_name = CBONDINDEXEODCNBD
            query = self.query(table_name, columns)
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_bond_industry_wind(self, code=None, columns=None):
            """中国债券Wind分类板块"""
            table_name = CBONDINDUSTRYWIND
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_bond_rating(self, code=None, columns=None):
            """中国债券信用评级"""
            table_name = CBONDRATING
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_bond_description(self, code=None, columns=None):
            """中国债券基本资料"""
            table_name = CBONDDESCRIPTION
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_bond_issuer_rating(self, code=None, columns=None):
            """中国债券发行主体信用评级"""
            table_name = CBONDISSUERRATING
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_COMPCODE, code)
            return df

        def get_c_bond_curve_cnbd(self, begin_date=None, end_date=None, trade_date=None,
                                  curve_number: Union[int, str, None] = None, curve_type: Optional[str] = None,
                                  curve_term: Optional[float] = None, columns: Optional[list] = None) -> pd.DataFrame:
            """
            中债登债券收益率曲线

            Args:
                begin_date: str, 开始日期；
                end_date: str, 结束日期；
                trade_date: str, 交易日期；
                curve_number: int, 曲线编号；
                curve_type: str, 曲线类型;
                curve_term: float, 标准期限(年)；
                columns: list, 查询字段。

            Returns:
                pd.DataFrame
            """
            table_name = CBONDCURVECNBD
            query = self.query(table_name, columns)
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            if curve_type is not None:
                query = query.filter(table_name.B_ANAL_CURVETYPE == curve_type)
            if curve_term is not None:
                query = query.filter(table_name.B_ANAL_CURVETERM == curve_term)
            return self.batch_query(query, table_name.B_ANAL_CURVENUMBER, curve_number)

        def get_c_bond_valuation(self, code=None, begin_date=None, end_date=None, trade_date=None, columns=None):
            """中国债券衍生指标"""
            table_name = CBONDVALUATION
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_cc_bond_issuance(self, code=None, columns=None):
            """中国可转债发行"""
            table_name = CCBONDISSUANCE
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

    if 'futures':
        # 期货相关
        def get_c_index_futures_eod_prices(self, code=None, begin_date=None, end_date=None, trade_date=None,
                                           columns=None):
            """查询股指期货行情"""
            table_name = CINDEXFUTURESEODPRICES
            query = self.query(table_name, columns)
            # 筛选条件
            query = self.filter_date(query, table_name.TRADE_DT, begin_date, end_date, trade_date)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            if 'S_INFO_WINDCODE' in df.columns and 'TRADE_DT' in df.columns:
                df.sort_values(by=['S_INFO_WINDCODE', 'TRADE_DT'], inplace=True)
            return df

        def get_c_futures_description(self, code=None, columns=None):
            """
            中国期货基本资料
            """
            table_name = CFUTURESDESCRIPTION
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_futures_description_distinct_code(self):
            table_name = CFUTURESDESCRIPTION
            query = self.session.query(distinct(table_name.S_INFO_WINDCODE))
            df = self.read_sql(query)
            code_list = list(df.iloc[:, 0])
            return code_list

    if 'others':
        # 其他
        def get_related_securities_code(self, code=None, columns=None):
            """证券关系表"""
            table_name = RALATEDSECURITIESCODE
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_wind_custom_code(self, code=None, columns=None):
            """Wind兼容代码"""
            table_name = WINDCUSTOMCODE
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, code)
            return df

        def get_c_gold_spot_description(self, fund_code=None, columns=None):
            """黄金现货基本资料"""
            table_name = CGOLDSPOTDESCRIPTION
            query = self.query(table_name, columns)
            # 查询数据
            df = self.batch_query(query, table_name.S_INFO_WINDCODE, fund_code)
            return df

    if 'licai':
        def get_licai_comp_financial_info(self,comp_name=None):
            """ 获取理财子公司的财务信息 （总资产，总负债，总盈利） """
            query = self.session.query(COMPINTRODUCTION.COMP_NAME,UNLISTEDBANKBALANCESHEET.REPORT_PERIOD,UNLISTEDBANKBALANCESHEET.TOT_ASSETS,
                                       UNLISTEDBANKBALANCESHEET.TOT_LIAB,UNLISTEDBANKBALANCESHEET.TOT_SHRHLDR_EQY_INCL_MIN_INT,
                                       UNLISTEDBANKINCOME.NET_PROFIT_INCL_MIN_INT_INC).outerjoin(COMPINTRODUCTION,UNLISTEDBANKBALANCESHEET.S_INFO_COMPCODE == COMPINTRODUCTION.COMP_ID).\
                                                                                       outerjoin(UNLISTEDBANKINCOME,and_(UNLISTEDBANKBALANCESHEET.S_INFO_COMPCODE == UNLISTEDBANKINCOME.S_INFO_COMPCODE,
                                                                                                                         UNLISTEDBANKBALANCESHEET.REPORT_PERIOD == UNLISTEDBANKINCOME.REPORT_PERIOD ))

            data = self.batch_query(query,COMPINTRODUCTION.COMP_NAME,comp_name)
            data = data.rename(columns={"COMP_NAME":'comp_name',
                                 "REPORT_PERIOD":"report_period",
                                 "TOT_ASSETS":"asset",
                                 "TOT_LIAB":"liability",
                                 "TOT_SHRHLDR_EQY_INCL_MIN_INT":"equity",
                                 "NET_PROFIT_INCL_MIN_INT_INC": "profit"
                                 })

            return data


if __name__ == '__main__':
    # res = WindReader().get_china_mutual_fund_benchmark_eod("000011BI.WI")
    # print(res)

    # res = WindReader().get_a_share_placement_details(fund_code="000006.OF")
    # print(res)

    # res = WindReader().get_a_share_ipo_inquiry_details(fund_code="002601.OF")
    # print(res)
    #
    # res = WindReader().get_a_share_eod_prices(code='300860.SZ')

    comp_name = '建信理财有限责任公司'
    res = WindReader().get_licai_comp_financial_info(comp_name=comp_name)
    print(res)



