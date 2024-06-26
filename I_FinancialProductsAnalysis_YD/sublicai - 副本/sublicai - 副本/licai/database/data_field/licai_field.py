# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/10/25 14:38 
# @Author    : Wangyd5 
# @File      : licai_field
# @Project   : sublicai
# @Function  ：
# --------------------------------

from sqlalchemy import Column, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import VARCHAR, Numeric,String,Integer,DATETIME
from tools.date_util import get_cur_time, get_cur_date
from tools.generate_id import generate_id

Base = declarative_base()


class LicaiFInancialReport(Base):
    __tablename__ = 'licai_financial_report'
    id = Column(String(32), default=generate_id, primary_key=True)
    compname = Column(VARCHAR(200), comment='理财子公司名称')
    report_period = Column(DATETIME, comment='报告期间')
    asset = Column(Numeric(20,2), comment='总资产')
    liability = Column(Numeric(20,2), comment='总负债')
    equity = Column(Numeric(20,2), comment='总权益资产')
    profit = Column(Numeric(20,2), comment='总利润')
    cal_date = Column(VARCHAR(8), default=get_cur_date, comment="计算日期")
    update_time = Column(VARCHAR(20), default=get_cur_time, comment="更新时间")
    __table_args__ = (Index('compname','report_period'),)


class AssetPortfolio(Base):
    __tablename__ = 'asset_portfolio'
    id = Column(String(32), default=generate_id, primary_key=True)
    registration_code = Column(VARCHAR(200), comment='登记编码',index=True)
    end_date = Column(DATETIME, comment='公告日期')
    first_grade_type = Column(VARCHAR(200), comment='一级资产')
    second_grade_type = Column(VARCHAR(200), comment='二级资产')
    asset_before = Column(Numeric(20,4), comment='穿透前规模')
    ratio_before = Column(Numeric(20,4), comment='穿透前规模占比')
    asset_after = Column(Numeric(20,4), comment='穿透前规模')
    ratio_after = Column(Numeric(20,4), comment='穿透前规模占比')
    cal_date = Column(VARCHAR(8), default=get_cur_date, comment="计算日期")
    update_time = Column(VARCHAR(20), default=get_cur_time, comment="更新时间")


class AssetTop10(Base):
    __tablename__ = 'asset_top_10'
    id = Column(String(32), default=generate_id, primary_key=True)
    registration_code = Column(VARCHAR(200), comment='登记编码',index=True)
    end_date = Column(DATETIME, comment='公告日期')
    asset_name = Column(VARCHAR(200), comment='资产名称')
    asset_std_type = Column(VARCHAR(50), comment='是否标准资产')
    primary_type = Column(VARCHAR(200), comment='一级资产类型')
    three_level_type = Column(VARCHAR(200), comment='三级资产类型')
    asset_scale = Column(Numeric(20,4), comment='资产规模，单位 万元')
    actual_proportion = Column(Numeric(20,4), comment='资产规模占比')
    cal_date = Column(VARCHAR(8), default=get_cur_date, comment="计算日期")
    update_time = Column(VARCHAR(20), default=get_cur_time, comment="更新时间")


class BasicInfo(Base):
    __tablename__ = 'basic_info'
    id = Column(String(32), default=generate_id, primary_key=True)
    CompanyName = Column(VARCHAR(200), comment='理财子公司',index=True)
    ParentCompName = Column(VARCHAR(200), comment='理财子母公司')
    ParentCompType = Column(VARCHAR(100), comment='母公司类型')
    EstablishmentDate = Column(VARCHAR(8), comment='母公司成立时间')
    FinProCode = Column(Integer, comment='产品内部代码')
    product_name = Column(VARCHAR(200), comment='产品名称')
    SecuState = Column(VARCHAR(40), comment='存续状态')
    PopularizeStDate = Column(VARCHAR(8), comment='起售日期')
    MinInvestTimeType = Column(VARCHAR(200), comment='期限运作方式')
    RaisingType = Column(VARCHAR(20), comment='募集方式')
    OperationType = Column(VARCHAR(20), comment='运作方式')
    InvestmentType = Column(VARCHAR(20), comment='投资类型')
    EndDate = Column(VARCHAR(8), comment='截止日期')
    AssetValue = Column(Numeric(20,4), comment='规模')
    ProductType = Column(VARCHAR(20), comment='份额类型')
    product_establish_date = Column(VARCHAR(8), comment='产品成立日期')
    CurrencyUnit = Column(VARCHAR(20), comment='产品货币')
    SecuAbbr = Column(VARCHAR(200), comment='产品简称')
    MinInvestTerm = Column(Numeric(20,0), comment='最小持有期限')
    MinInvestTermUnit = Column(VARCHAR(20), comment='最小持有期限单位')
    RiskLevel = Column(VARCHAR(20), comment='风险等级')
    Benchmark = Column(VARCHAR(200), comment='业绩基准')
    BenchmarkMax = Column(Numeric(20,2), comment='业绩基准上限')
    BenchmarkMin = Column(Numeric(20,2), comment='业绩基准下限')
    manage_fee_x = Column(Numeric(20,2), comment='固定管理费_py')
    manage_fee_y = Column(Numeric(20,2), comment='固定管理费_jy')
    manage_fee_unit = Column(VARCHAR(20), comment='固定管理费单位')
    carry_fee_x = Column(Numeric(20,2), comment='超额业绩报酬_py')
    carry_fee_y = Column(Numeric(20,2), comment='超额业绩报酬_jy')
    carry_fee_unit = Column(VARCHAR(20), comment='超额业绩报酬单位')
    MaturityDate = Column(VARCHAR(8), comment='到期期限')
    inv_type = Column(Integer, comment='是否是现金管理')
    RegistrationCode = Column(VARCHAR(40), comment='登记编码')
    MinInvestDay = Column(Numeric(20,0), comment='最小持有天数')
    IfStructure = Column(Integer, comment='是否结构性')
    InvestTerm = Column(Numeric(20,0), comment='投资周期')
    product_series = Column(VARCHAR(200), comment='产品系列')
    IssueObject_x = Column(VARCHAR(100), comment='发行对象_py')   # fixme 有问题 数据中是数字
    IssueObject_y = Column(VARCHAR(100), comment='发行对象_jy')
    open_type = Column(VARCHAR(500), comment='开放类型')
    open_rules = Column(VARCHAR(1000), comment='开放规则')
    fixed_income_upper = Column(Numeric(20,0), comment='固收投资上限')
    fixed_income_lower = Column(Numeric(20,0), comment='固收投资下限')
    equity_upper = Column(Numeric(20,0), comment='权益投资上限')
    equity_lower = Column(Numeric(20,0), comment='权益投资下限')
    derivatives_upper = Column(Numeric(20,0), comment='衍生品投资上限')
    derivatives_lower = Column(Numeric(20,0), comment='衍生品投资下限')
    invest_strategy = Column(VARCHAR(3000), comment='投资策略')
    top_raise_scale = Column(Numeric(20,0), comment='募集规模上限')
    actual_raise_scale = Column(Numeric(20,0), comment='实际募集规模')
    is_index = Column(Integer, comment='是否挂钩指数')
    is_early_redeem = Column(Integer, comment='是否可以提前赎回')
    old_invest_scope = Column(VARCHAR(500), comment='投资范围')
    report_date = Column(VARCHAR(8), comment='产品分类日期')
    product_type_son = Column(VARCHAR(50), comment='产品分类')
    asset_type = Column(VARCHAR(100), comment='可投资资产')
    resource = Column(VARCHAR(20), comment='分类依据')
    interval_ret_three_m = Column(Numeric(20,4), comment='近三个月年化收益')
    interval_ret_annual = Column(Numeric(20,4), comment='资管新规过渡期结束以来收益')
    max_draw_down = Column(Numeric(20,4), comment='最大回撤')
    sharpe = Column(Numeric(20,4), comment='夏普比')
    rank_str = Column(VARCHAR(20), comment='业绩排名')
    tag = Column(VARCHAR(100), comment='产品系列依据')
    set0 = Column(VARCHAR(20), comment='产品系列0')
    set = Column(VARCHAR(20), comment='产品系列1')
    ident_benchmark = Column(VARCHAR(200), comment='业绩基准-整合')
    benchmark_low = Column(Numeric(20,0), comment='业绩基准下限')
    benchmark_high = Column(Numeric(20,0), comment='业绩基准上限')
    cal_date = Column(VARCHAR(8), default=get_cur_date, comment="计算日期")
    update_time = Column(VARCHAR(20), default=get_cur_time, comment="更新时间")
    __table_args__ = (Index("FinProCode",'RegistrationCode'),)


class WeekNav(Base):
    __tablename__ = 'week_nav'
    id = Column(String(32), default=generate_id, primary_key=True)
    FinProCode = Column(Integer, comment='产品编码',index=True)
    trade_dt = Column(DATETIME, comment='公告日期')
    net_value = Column(Numeric(20,4), comment='净值')
    cal_date = Column(VARCHAR(8), default=get_cur_date, comment="计算日期")
    update_time = Column(VARCHAR(20), default=get_cur_time, comment="更新时间")
    __table_args__ = (Index("FinProCode",'trade_dt'),)


