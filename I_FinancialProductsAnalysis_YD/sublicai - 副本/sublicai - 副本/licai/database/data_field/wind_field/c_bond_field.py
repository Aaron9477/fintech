# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/10/20 9:33
# @Author  : lisl3
# @File    : c_bond_field.py
# @Project : cscfist
# @Function: 中国债券
# @Version : V0.0.1
# ------------------------------
from sqlalchemy import Column, VARCHAR, Numeric, DateTime, TEXT, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CBONDACCOUNTSPAYABLE(Base):
    """中国债券公司应付账款"""
    __tablename__ = 'CBONDACCOUNTSPAYABLE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='上游公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='上游公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='上游公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class CBONDACCOUNTSRECEIVABLE(Base):
    """中国债券发行主体应收账款大股东欠款"""
    __tablename__ = 'CBONDACCOUNTSRECEIVABLE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    MEMO = Column(VARCHAR(100), comment='备注')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    DEBTOR_NAME = Column(VARCHAR(60), comment='债务人名称')
    ARREARS = Column(Numeric(20, 4), comment='金额')
    RATE = Column(Numeric(20, 4), comment='比例(%)')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')


class CBONDACCRUEDINTEREST(Base):
    """中国债券应计利息"""
    __tablename__ = 'CBONDACCRUEDINTEREST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_ACCRUEDDAYS = Column(Numeric(20, 4), comment='已计息时间')
    B_ANAL_ACCRUEDINTEREST = Column(Numeric(24, 12), comment='应计利息')


class CBONDACTUALCF(Base):
    """中国债券实际现金流发生表"""
    __tablename__ = 'CBONDACTUALCF'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_CARRYDATE = Column(VARCHAR(8), comment='计息起始日')
    B_INFO_ENDDATE = Column(VARCHAR(8), comment='计息截止日')
    B_INFO_COUPONRATE = Column(Numeric(24, 8), comment='计息期票面利率(%)')
    B_INFO_PAYMENTDATE = Column(VARCHAR(8), comment='现金流发生日')
    B_INFO_PAYMENTINTEREST = Column(Numeric(24, 8), comment='期末每百元面额应计利息(元)')
    B_INFO_PAYMENTPARVALUE = Column(Numeric(24, 8), comment='期末每百元面额应付本金(元)')
    B_INFO_PAYMENTSUM = Column(Numeric(24, 8), comment='期末每百元面额现金流合计(元)')


class CBONDADMINISTRATION(Base):
    """中国债券公司高管成员"""
    __tablename__ = 'CBONDADMINISTRATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='职务')


class CBONDAGENCY(Base):
    """中国债券中介机构"""
    __tablename__ = 'CBONDAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_AGENCY_NAME = Column(VARCHAR(200), comment='机构名称')
    B_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    B_AGENCY_NAMEID = Column(VARCHAR(200), comment='机构名称ID')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')


class CBONDAGENCYQL(Base):
    """None"""
    __tablename__ = 'CBONDAGENCYQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    B_INFO_WINDCODE = Column(VARCHAR(40))
    B_AGENCY_NAME = Column(VARCHAR(200))
    B_RELATION_TYPCODE = Column(VARCHAR(10))
    B_AGENCY_NAMEID = Column(VARCHAR(200))
    START_DT = Column(VARCHAR(8))
    END_DT = Column(VARCHAR(8))


class CBONDAGENCYZL(Base):
    """中国债券中介机构(增量)"""
    __tablename__ = 'CBONDAGENCYZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_AGENCY_NAME = Column(VARCHAR(200), comment='机构名称')
    B_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    B_AGENCY_NAMEID = Column(VARCHAR(200), comment='机构名称ID')


class CBONDAGINGSTRUCTURE(Base):
    """中国债券发行主体应收账款账龄结构"""
    __tablename__ = 'CBONDAGINGSTRUCTURE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    STATEMENT_TYPE_NAME = Column(VARCHAR(40), comment='报表类型名称')
    MEMO = Column(VARCHAR(100), comment='备注')
    AGING = Column(VARCHAR(20), comment='账龄')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    AMOUNT_MONEY = Column(Numeric(20, 4), comment='金额')
    RATE = Column(Numeric(20, 4), comment='比例(%)')
    BAD_DEBT_PREPARATION = Column(Numeric(20, 4), comment='坏账准备')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    MIN_AGING = Column(Numeric(20, 4), comment='最小账龄(年)')
    MAX_AGING = Column(Numeric(20, 4), comment='最大账龄(年)')
    CLASSIFICATION_CRITERIA = Column(VARCHAR(40), comment='分类标准')


class CBONDAMOUNT(Base):
    """中国债券份额变动"""
    __tablename__ = 'CBONDAMOUNT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    B_INFO_CHANGEREASON = Column(Numeric(9, 0), comment='变动原因')
    B_INFO_OUTSTANDINGBALANCE = Column(Numeric(20, 8), comment='债券份额(亿元)')


class CBONDANALYSISCNBD(Base):
    """中债登估值(废弃)"""
    __tablename__ = 'CBONDANALYSISCNBD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD1(Base):
    """中债登估值(国债金融债企债)"""
    __tablename__ = 'CBONDANALYSISCNBD1'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD2(Base):
    """中债登估值(中票短融)"""
    __tablename__ = 'CBONDANALYSISCNBD2'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD3(Base):
    """中债登估值(债务融资工具)"""
    __tablename__ = 'CBONDANALYSISCNBD3'
    __table_args__ = (
        Index('IDX_CBONDANALYSISCNBD3_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD4(Base):
    """中债登估值(同业存单)"""
    __tablename__ = 'CBONDANALYSISCNBD4'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD5(Base):
    """中债登估值(公司债)"""
    __tablename__ = 'CBONDANALYSISCNBD5'
    __table_args__ = (
        Index('IDX_CBONDANALYSISCNBD5_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD6(Base):
    """中债登估值(资产支持证券)"""
    __tablename__ = 'CBONDANALYSISCNBD6'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD7(Base):
    """中债登估值(优先股及其他)"""
    __tablename__ = 'CBONDANALYSISCNBD7'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD8(Base):
    """中债登估值(CRMW)"""
    __tablename__ = 'CBONDANALYSISCNBD8'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNBD9(Base):
    """中债登估值(中资美元债)"""
    __tablename__ = 'CBONDANALYSISCNBD9'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_ACCRINTCLOSE_CNBD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='点差收益率(%)')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')
    B_ANAL_RESIDUALPRI = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXERCISE_RATE = Column(Numeric(20, 6), comment='估算的行权后票面利率')
    B_ANAL_PRIORITY = Column(Numeric(1, 0), comment='优先级')


class CBONDANALYSISCNM(Base):
    """中国货币网债券估值数据"""
    __tablename__ = 'CBONDANALYSISCNM'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    ANAL_DIRTY = Column(Numeric(20, 4), comment='估价全价')
    ANAL_NET = Column(Numeric(20, 4), comment='估价净价')
    ANAL_YIELD = Column(Numeric(20, 4), comment='估价收益率')


class CBONDANALYSISCSI(Base):
    """中证估值"""
    __tablename__ = 'CBONDANALYSISCSI'
    __table_args__ = (
        Index('IDX_CBONDANALYSISCSI_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_INFO_TYPE = Column(VARCHAR(50), comment='信用类型')
    B_INFO_LISTINGMARKETNUMBERS = Column(Numeric(20, 4), comment='发行市场数')
    B_ANAL_DIRTY_CSI = Column(Numeric(20, 4), comment='计算价格')
    B_ANAL_YIELD_CSI = Column(Numeric(20, 4), comment='计算收益率(%)')
    B_ANAL_MODIDURA_CSI = Column(Numeric(20, 4), comment='修正久期')
    B_ANAL_CNVXTY_CSI = Column(Numeric(20, 4), comment='凸性')
    B_ANAL_NET_CSI = Column(Numeric(20, 4), comment='净价')
    B_ANAL_ACCRINT_CSI = Column(Numeric(20, 4), comment='应计利息')
    B_ANAL_FULL_IFEXE = Column(Numeric(20, 4), comment='全价（行权）')
    B_ANAL_NET_IFEXE = Column(Numeric(20, 4), comment='净价（行权）')
    B_ANAL_YTM_IFEXE = Column(Numeric(20, 4), comment='行权收益率')
    B_ANAL_MODIDURA_IFEXE = Column(Numeric(20, 4), comment='修正久期（行权）')
    B_ANAL_CNVXTY_IFEXE = Column(Numeric(20, 4), comment='凸性（行权）')
    RECOMMENDED = Column(Numeric(1, 0), comment='推荐')
    B_ANAL_EST_COUPONRATE = Column(Numeric(20, 4), comment='预期票面利率')


class CBONDANALYSISSHC(Base):
    """上海清算所债券估值"""
    __tablename__ = 'CBONDANALYSISSHC'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_MATU_CNBD = Column(Numeric(20, 4), comment='待偿期(年)')
    B_ANAL_DIRTY_CNBD = Column(Numeric(20, 4), comment='日间估价全价')
    B_ANAL_ACCRINT_CNBD = Column(Numeric(20, 4), comment='日间应计利息')
    B_ANAL_NET_CNBD = Column(Numeric(20, 4), comment='估价净价')
    B_ANAL_YIELD_CNBD = Column(Numeric(20, 4), comment='估价收益率(%)')
    B_ANAL_MODIDURA_CNBD = Column(Numeric(20, 4), comment='估价修正久期')
    B_ANAL_CNVXTY_CNBD = Column(Numeric(20, 4), comment='估价凸性')
    B_ANAL_VOBP_CNBD = Column(Numeric(20, 4), comment='估价基点价值')
    B_ANAL_SPRDURA_CNBD = Column(Numeric(20, 4), comment='估价利差久期')
    B_ANAL_SPRCNXT_CNBD = Column(Numeric(20, 4), comment='估价利差凸性')
    B_ANAL_PRICE = Column(Numeric(20, 4), comment='市场全价')
    B_ANAL_NETPRICE = Column(Numeric(20, 4), comment='市场净价')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='市场收益率(%)')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(20, 4), comment='市场修正久期')
    B_ANAL_CONVEXITY = Column(Numeric(20, 4), comment='市场凸性')
    B_ANAL_BPVALUE = Column(Numeric(20, 4), comment='市场基点价值')
    B_ANAL_SDURATION = Column(Numeric(20, 4), comment='市场利差久期')
    B_ANAL_SCNVXTY = Column(Numeric(20, 4), comment='市场利差凸性')
    B_ANAL_INTERESTDURATION_CNBD = Column(Numeric(20, 4), comment='估价利率久期')
    B_ANAL_INTERESTCNVXTY_CNBD = Column(Numeric(20, 4), comment='估价利率凸性')
    B_ANAL_INTERESTDURATION = Column(Numeric(20, 4), comment='市场利率久期')
    B_ANAL_INTERESTCNVXTY = Column(Numeric(20, 4), comment='市场利率凸性')
    B_ANAL_PRICE_CNBD = Column(Numeric(20, 4), comment='日终估价全价')
    B_ANAL_BPYIELD = Column(Numeric(20, 4), comment='日终应计利息')
    B_ANAL_SURPLUSCAPITAL = Column(Numeric(20, 4), comment='剩余本金')
    B_ANAL_EXCHANGE = Column(VARCHAR(40), comment='流通场所')
    B_ANAL_CREDIBILITY = Column(VARCHAR(40), comment='可信度')


class CBONDAPPROVALINFORMATION(Base):
    """中国债券公司债审批信息"""
    __tablename__ = 'CBONDAPPROVALINFORMATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    ANN_DATE = Column(VARCHAR(8), comment='更新日期')
    B_INFO_FULLNAME = Column(VARCHAR(200), comment='债券名称')
    BONDTYPE = Column(Numeric(3, 0), comment='债券类型')
    AMOUNT = Column(Numeric(24, 8), comment='计划发行金额(亿元)')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='原始权益人名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='发行人公司ID')
    LEADUNDERWRITER = Column(VARCHAR(1000), comment='主承销商/管理人')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所代码')
    FILENUM = Column(VARCHAR(40), comment='交易所确认文件文号')
    PROGRESS_CODE = Column(Numeric(9, 0), comment='项目状态')


class CBONDAUDITOPINION(Base):
    """中国债券发行主体审计意见"""
    __tablename__ = 'CBONDAUDITOPINION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_STMNOTE_AUDIT_CATEGORY = Column(Numeric(9, 0), comment='审计结果类别代码')
    S_STMNOTE_AUDIT_AGENCY = Column(VARCHAR(100), comment='会计师事务所')
    S_STMNOTE_AUDIT_CPA = Column(VARCHAR(100), comment='签字会计师')
    AUDIT_AGENCY = Column(VARCHAR(30), comment='审计机构类别')
    AUDIT_AGENCY_CODE = Column(Numeric(9, 0), comment='审计机构类别代码')


class CBONDBALANCESHEET(Base):
    """中国债券发行主体资产负债表"""
    __tablename__ = 'CBONDBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    MONETARY_CAP = Column(Numeric(20, 4), comment='货币资金')
    TRADABLE_FIN_ASSETS = Column(Numeric(20, 4), comment='交易性金融资产')
    NOTES_RCV = Column(Numeric(20, 4), comment='应收票据')
    ACCT_RCV = Column(Numeric(20, 4), comment='应收账款')
    OTH_RCV = Column(Numeric(20, 4), comment='其他应收款')
    PREPAY = Column(Numeric(20, 4), comment='预付款项')
    DVD_RCV = Column(Numeric(20, 4), comment='应收股利')
    INT_RCV = Column(Numeric(20, 4), comment='应收利息')
    INVENTORIES = Column(Numeric(20, 4), comment='存货')
    CONSUMPTIVE_BIO_ASSETS = Column(Numeric(20, 4), comment='消耗性生物资产')
    DEFERRED_EXP = Column(Numeric(20, 4), comment='待摊费用')
    NON_CUR_ASSETS_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的非流动资产')
    SETTLE_RSRV = Column(Numeric(20, 4), comment='结算备付金')
    LOANS_TO_OTH_BANKS = Column(Numeric(20, 4), comment='拆出资金')
    PREM_RCV = Column(Numeric(20, 4), comment='应收保费')
    RCV_FROM_REINSURER = Column(Numeric(20, 4), comment='应收分保账款')
    RCV_FROM_CEDED_INSUR_CONT_RSRV = Column(Numeric(20, 4), comment='应收分保合同准备金')
    RED_MONETARY_CAP_FOR_SALE = Column(Numeric(20, 4), comment='买入返售金融资产')
    OTH_CUR_ASSETS = Column(Numeric(20, 4), comment='其他流动资产')
    TOT_CUR_ASSETS = Column(Numeric(20, 4), comment='流动资产合计')
    FIN_ASSETS_AVAIL_FOR_SALE = Column(Numeric(20, 4), comment='可供出售金融资产')
    HELD_TO_MTY_INVEST = Column(Numeric(20, 4), comment='持有至到期投资')
    LONG_TERM_EQY_INVEST = Column(Numeric(20, 4), comment='长期股权投资')
    INVEST_REAL_ESTATE = Column(Numeric(20, 4), comment='投资性房地产')
    TIME_DEPOSITS = Column(Numeric(20, 4), comment='定期存款')
    OTH_ASSETS = Column(Numeric(20, 4), comment='其他资产')
    LONG_TERM_REC = Column(Numeric(20, 4), comment='长期应收款')
    FIX_ASSETS = Column(Numeric(20, 4), comment='固定资产')
    CONST_IN_PROG = Column(Numeric(20, 4), comment='在建工程')
    PROJ_MATL = Column(Numeric(20, 4), comment='工程物资')
    FIX_ASSETS_DISP = Column(Numeric(20, 4), comment='固定资产清理')
    PRODUCTIVE_BIO_ASSETS = Column(Numeric(20, 4), comment='生产性生物资产')
    OIL_AND_NATURAL_GAS_ASSETS = Column(Numeric(20, 4), comment='油气资产')
    INTANG_ASSETS = Column(Numeric(20, 4), comment='无形资产')
    R_AND_D_COSTS = Column(Numeric(20, 4), comment='开发支出')
    GOODWILL = Column(Numeric(20, 4), comment='商誉')
    LONG_TERM_DEFERRED_EXP = Column(Numeric(20, 4), comment='长期待摊费用')
    DEFERRED_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产')
    LOANS_AND_ADV_GRANTED = Column(Numeric(20, 4), comment='发放贷款及垫款')
    OTH_NON_CUR_ASSETS = Column(Numeric(20, 4), comment='其他非流动资产')
    TOT_NON_CUR_ASSETS = Column(Numeric(20, 4), comment='非流动资产合计')
    CASH_DEPOSITS_CENTRAL_BANK = Column(Numeric(20, 4), comment='现金及存放中央银行款项')
    ASSET_DEP_OTH_BANKS_FIN_INST = Column(Numeric(20, 4), comment='存放同业和其它金融机构款项')
    PRECIOUS_METALS = Column(Numeric(20, 4), comment='贵金属')
    DERIVATIVE_FIN_ASSETS = Column(Numeric(20, 4), comment='衍生金融资产')
    AGENCY_BUS_ASSETS = Column(Numeric(20, 4), comment='代理业务资产')
    SUBR_REC = Column(Numeric(20, 4), comment='应收代位追偿款')
    RCV_CEDED_UNEARNED_PREM_RSRV = Column(Numeric(20, 4), comment='应收分保未到期责任准备金')
    RCV_CEDED_CLAIM_RSRV = Column(Numeric(20, 4), comment='应收分保未决赔款准备金')
    RCV_CEDED_LIFE_INSUR_RSRV = Column(Numeric(20, 4), comment='应收分保寿险责任准备金')
    RCV_CEDED_LT_HEALTH_INSUR_RSRV = Column(Numeric(20, 4), comment='应收分保长期健康险责任准备金')
    MRGN_PAID = Column(Numeric(20, 4), comment='存出保证金')
    INSURED_PLEDGE_LOAN = Column(Numeric(20, 4), comment='保户质押贷款')
    CAP_MRGN_PAID = Column(Numeric(20, 4), comment='存出资本保证金')
    INDEPENDENT_ACCT_ASSETS = Column(Numeric(20, 4), comment='独立账户资产')
    CLIENTS_CAP_DEPOSIT = Column(Numeric(20, 4), comment='客户资金存款')
    CLIENTS_RSRV_SETTLE = Column(Numeric(20, 4), comment='客户备付金')
    INCL_SEAT_FEES_EXCHANGE = Column(Numeric(20, 4), comment='其中:交易席位费')
    RCV_INVEST = Column(Numeric(20, 4), comment='应收款项类投资')
    TOT_ASSETS = Column(Numeric(20, 4), comment='资产总计')
    ST_BORROW = Column(Numeric(20, 4), comment='短期借款')
    BORROW_CENTRAL_BANK = Column(Numeric(20, 4), comment='向中央银行借款')
    DEPOSIT_RECEIVED_IB_DEPOSITS = Column(Numeric(20, 4), comment='吸收存款及同业存放')
    LOANS_OTH_BANKS = Column(Numeric(20, 4), comment='拆入资金')
    TRADABLE_FIN_LIAB = Column(Numeric(20, 4), comment='交易性金融负债')
    NOTES_PAYABLE = Column(Numeric(20, 4), comment='应付票据')
    ACCT_PAYABLE = Column(Numeric(20, 4), comment='应付账款')
    ADV_FROM_CUST = Column(Numeric(20, 4), comment='预收款项')
    FUND_SALES_FIN_ASSETS_RP = Column(Numeric(20, 4), comment='卖出回购金融资产款')
    HANDLING_CHARGES_COMM_PAYABLE = Column(Numeric(20, 4), comment='应付手续费及佣金')
    EMPL_BEN_PAYABLE = Column(Numeric(20, 4), comment='应付职工薪酬')
    TAXES_SURCHARGES_PAYABLE = Column(Numeric(20, 4), comment='应交税费')
    INT_PAYABLE = Column(Numeric(20, 4), comment='应付利息')
    DVD_PAYABLE = Column(Numeric(20, 4), comment='应付股利')
    OTH_PAYABLE = Column(Numeric(20, 4), comment='其他应付款')
    ACC_EXP = Column(Numeric(20, 4), comment='预提费用')
    DEFERRED_INC = Column(Numeric(20, 4), comment='递延收益')
    ST_BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付短期债券')
    PAYABLE_TO_REINSURER = Column(Numeric(20, 4), comment='应付分保账款')
    RSRV_INSUR_CONT = Column(Numeric(20, 4), comment='保险合同准备金')
    ACTING_TRADING_SEC = Column(Numeric(20, 4), comment='代理买卖证券款')
    ACTING_UW_SEC = Column(Numeric(20, 4), comment='代理承销证券款')
    NON_CUR_LIAB_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的非流动负债')
    OTH_CUR_LIAB = Column(Numeric(20, 4), comment='其他流动负债')
    TOT_CUR_LIAB = Column(Numeric(20, 4), comment='流动负债合计')
    LT_BORROW = Column(Numeric(20, 4), comment='长期借款')
    BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付债券')
    LT_PAYABLE = Column(Numeric(20, 4), comment='长期应付款')
    SPECIFIC_ITEM_PAYABLE = Column(Numeric(20, 4), comment='专项应付款')
    PROVISIONS = Column(Numeric(20, 4), comment='预计负债')
    DEFERRED_TAX_LIAB = Column(Numeric(20, 4), comment='递延所得税负债')
    DEFERRED_INC_NON_CUR_LIAB = Column(Numeric(20, 4), comment='递延收益-非流动负债')
    OTH_NON_CUR_LIAB = Column(Numeric(20, 4), comment='其他非流动负债')
    TOT_NON_CUR_LIAB = Column(Numeric(20, 4), comment='非流动负债合计')
    LIAB_DEP_OTH_BANKS_FIN_INST = Column(Numeric(20, 4), comment='同业和其它金融机构存放款项')
    DERIVATIVE_FIN_LIAB = Column(Numeric(20, 4), comment='衍生金融负债')
    CUST_BANK_DEP = Column(Numeric(20, 4), comment='吸收存款')
    AGENCY_BUS_LIAB = Column(Numeric(20, 4), comment='代理业务负债')
    OTH_LIAB = Column(Numeric(20, 4), comment='其他负债')
    PREM_RECEIVED_ADV = Column(Numeric(20, 4), comment='预收保费')
    DEPOSIT_RECEIVED = Column(Numeric(20, 4), comment='存入保证金')
    INSURED_DEPOSIT_INVEST = Column(Numeric(20, 4), comment='保户储金及投资款')
    UNEARNED_PREM_RSRV = Column(Numeric(20, 4), comment='未到期责任准备金')
    OUT_LOSS_RSRV = Column(Numeric(20, 4), comment='未决赔款准备金')
    LIFE_INSUR_RSRV = Column(Numeric(20, 4), comment='寿险责任准备金')
    LT_HEALTH_INSUR_V = Column(Numeric(20, 4), comment='长期健康险责任准备金')
    INDEPENDENT_ACCT_LIAB = Column(Numeric(20, 4), comment='独立账户负债')
    INCL_PLEDGE_LOAN = Column(Numeric(20, 4), comment='其中:质押借款')
    CLAIMS_PAYABLE = Column(Numeric(20, 4), comment='应付赔付款')
    DVD_PAYABLE_INSURED = Column(Numeric(20, 4), comment='应付保单红利')
    TOT_LIAB = Column(Numeric(20, 4), comment='负债合计')
    CAP_STK = Column(Numeric(20, 4), comment='股本')
    CAP_RSRV = Column(Numeric(20, 4), comment='资本公积金')
    SPECIAL_RSRV = Column(Numeric(20, 4), comment='专项储备')
    SURPLUS_RSRV = Column(Numeric(20, 4), comment='盈余公积金')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='未分配利润')
    LESS_TSY_STK = Column(Numeric(20, 4), comment='减:库存股')
    PROV_NOM_RISKS = Column(Numeric(20, 4), comment='一般风险准备')
    CNVD_DIFF_FOREIGN_CURR_STAT = Column(Numeric(20, 4), comment='外币报表折算差额')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认的投资损失')
    MINORITY_INT = Column(Numeric(20, 4), comment='少数股东权益')
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(不含少数股东权益)')
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(含少数股东权益)')
    TOT_LIAB_SHRHLDR_EQY = Column(Numeric(20, 4), comment='负债及股东权益总计')
    COMP_TYPE_CODE = Column(VARCHAR(2), comment='公司类型代码')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    SPE_CUR_ASSETS_DIFF = Column(Numeric(20, 4), comment='流动资产差额(特殊报表科目)')
    TOT_CUR_ASSETS_DIFF = Column(Numeric(20, 4), comment='流动资产差额(合计平衡项目)')
    SPE_NON_CUR_ASSETS_DIFF = Column(Numeric(20, 4), comment='非流动资产差额(特殊报表科目)')
    TOT_NON_CUR_ASSETS_DIFF = Column(Numeric(20, 4), comment='非流动资产差额(合计平衡项目)')
    SPE_BAL_ASSETS_DIFF = Column(Numeric(20, 4), comment='资产差额(特殊报表科目)')
    TOT_BAL_ASSETS_DIFF = Column(Numeric(20, 4), comment='资产差额(合计平衡项目)')
    SPE_CUR_LIAB_DIFF = Column(Numeric(20, 4), comment='流动负债差额(特殊报表科目)')
    TOT_CUR_LIAB_DIFF = Column(Numeric(20, 4), comment='流动负债差额(合计平衡项目)')
    SPE_NON_CUR_LIAB_DIFF = Column(Numeric(20, 4), comment='非流动负债差额(特殊报表科目)')
    TOT_NON_CUR_LIAB_DIFF = Column(Numeric(20, 4), comment='非流动负债差额(合计平衡项目)')
    SPE_BAL_LIAB_DIFF = Column(Numeric(20, 4), comment='负债差额(特殊报表科目)')
    TOT_BAL_LIAB_DIFF = Column(Numeric(20, 4), comment='负债差额(合计平衡项目)')
    SPE_BAL_SHRHLDR_EQY_DIFF = Column(Numeric(20, 4), comment='股东权益差额(特殊报表科目)')
    TOT_BAL_SHRHLDR_EQY_DIFF = Column(Numeric(20, 4), comment='股东权益差额(合计平衡项目)')
    SPE_BAL_LIAB_EQY_DIFF = Column(Numeric(20, 4), comment='负债及股东权益差额(特殊报表项目)')
    TOT_BAL_LIAB_EQY_DIFF = Column(Numeric(20, 4), comment='负债及股东权益差额(合计平衡项目)')
    AUDIT_AM = Column(Numeric(1, 0), comment='采用会计准则')
    LT_PAYROLL_PAYABLE = Column(Numeric(20, 4), comment='长期应付职工薪酬')
    OTHER_COMP_INCOME = Column(Numeric(20, 4), comment='其他综合收益')
    OTHER_EQUITY_TOOLS = Column(Numeric(20, 4), comment='其他权益工具')
    OTHER_EQUITY_TOOLS_P_SHR = Column(Numeric(20, 4), comment='其他权益工具:优先股')
    LENDING_FUNDS = Column(Numeric(20, 4), comment='融出资金')
    ACCOUNTS_RECEIVABLE = Column(Numeric(20, 4), comment='应收款项')
    ST_FINANCING_PAYABLE = Column(Numeric(20, 4), comment='应付短期融资款')
    PAYABLES = Column(Numeric(20, 4), comment='应付款项')
    TOT_SHR = Column(Numeric(20, 4), comment='期末总股本')
    HFS_ASSETS = Column(Numeric(20, 4), comment='持有待售的资产')
    HFS_SALES = Column(Numeric(20, 4), comment='持有待售的负债')
    ACCOUNTS_RECEIVABLE_BILL = Column(Numeric(20, 4), comment='应收票据及应收账款')
    ACCOUNTS_PAYABLE = Column(Numeric(20, 4), comment='应付票据及应付账款')
    OTH_RCV_TOT = Column(Numeric(20, 4), comment='其他应收款(合计)')
    STM_BS_TOT = Column(Numeric(20, 4), comment='固定资产(合计)')
    CONST_IN_PROG_TOT = Column(Numeric(20, 4), comment='在建工程(合计)')
    OTH_PAYABLE_TOT = Column(Numeric(20, 4), comment='其他应付款(合计)')
    LT_PAYABLE_TOT = Column(Numeric(20, 4), comment='长期应付款(合计)')
    DEBT_INVESTMENT = Column(Numeric(20, 4), comment='债权投资')
    OTHER_DEBT_INVESTMENT = Column(Numeric(20, 4), comment='其他债权投资')
    OTHER_EQUITY_INVESTMENT = Column(Numeric(20, 4), comment='其他权益工具投资')
    OTHER_ILLIQUIDFINANCIAL_ASSETS = Column(Numeric(20, 4), comment='其他非流动金融资产')
    OTHER_SUSTAINABLE_BOND = Column(Numeric(20, 4), comment='其他权益工具:永续债')
    CONTRACTUAL_ASSETS = Column(Numeric(20, 4), comment='合同资产')
    CONTRACT_LIABILITIES = Column(Numeric(20, 4), comment='合同负债')
    FIN_ASSETS_COST_SHARING = Column(Numeric(20, 4), comment='以摊余成本计量的金融资产')
    FIN_ASSETS_FAIR_VALUE = Column(Numeric(20, 4), comment='以公允价值计量且其变动计入其他综合收益的金融资产')
    SPE_NON_CUR_ASSETS_DIFF_MEMO = Column(VARCHAR(200), comment='非流动资产差额说明(特殊报表科目)')
    SPE_BAL_ASSETS_DIFF_MEMO = Column(VARCHAR(500), comment='资产差额说明(特殊报表科目)')
    SPE_CUR_LIAB_DIFF_MEMO = Column(VARCHAR(200), comment='流动负债差额说明(特殊报表科目)')
    SPE_NON_CUR_LIAB_DIFF_MEMO = Column(VARCHAR(200), comment='非流动负债差额说明(特殊报表科目)')
    SPE_BAL_LIAB_DIFF_MEMO = Column(VARCHAR(500), comment='负债差额说明(特殊报表科目)')
    SPE_BAL_SHRHLDR_EQY_DIFF_MEMO = Column(VARCHAR(200), comment='其他股东权益说明(特殊报表科目)')
    SPE_BAL_LIAB_EQY_DIFF_MEMO = Column(VARCHAR(200), comment='负债及股东权益差额说明(特殊报表项目)')
    RECEIVABLES_FINANCING = Column(Numeric(20, 4), comment='应收款项融资')
    RIGHT_USE_ASSETS = Column(Numeric(20, 4), comment='使用权资产')
    LEASE_LIAB = Column(Numeric(20, 4), comment='租赁负债')


class CBONDBEGUARANTEED(Base):
    """中国债券公司被担保"""
    __tablename__ = 'CBONDBEGUARANTEED'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='担保公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='担保公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='担保公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class CBONDBENCHMARK(Base):
    """存贷款利率(央行)"""
    __tablename__ = 'CBONDBENCHMARK'
    __table_args__ = (
        Index('IDX_CBONDBENCHMARK_BENCHMARK_DT', 'B_INFO_BENCHMARK', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_INFO_BENCHMARK = Column(VARCHAR(10), comment='存贷款利率类型')
    B_INFO_RATE = Column(Numeric(20, 4), comment='利率(%)')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')


class CBONDBILLISSUANCE(Base):
    """中国央行票据发行"""
    __tablename__ = 'CBONDBILLISSUANCE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BILL_NAME = Column(VARCHAR(100), comment='票据名称')
    ISSUE_ANN_DATE = Column(VARCHAR(8), comment='发行公告日期')
    LIST_ANN_DATE = Column(VARCHAR(8), comment='上市公告日期')
    ISSUE_DATE = Column(VARCHAR(8), comment='发行日期')
    LIST_DATE = Column(VARCHAR(8), comment='上市日期')
    PTOTAL_NUM_ISSUES = Column(Numeric(20, 4), comment='计划发行总量(万元)')
    TOTAL_NUM_ISSUES = Column(Numeric(20, 4), comment='实际发行总量(万元)')
    ISSUE_TYPE = Column(VARCHAR(100), comment='发行方式')
    S_INFO_PAR = Column(Numeric(20, 4), comment='面额')
    TERM = Column(Numeric(20, 4), comment='期限(月)')
    PAYMENTDATE = Column(VARCHAR(8), comment='缴款日')
    CARRY_DATE = Column(VARCHAR(8), comment='起息日')
    MATURITY_DATE = Column(VARCHAR(8), comment='到期日')
    TENDER_METHOD = Column(VARCHAR(100), comment='招标方式')
    ISSUE_PRICE = Column(Numeric(20, 4), comment='发行价格')
    TENDRST_REFERYIELD = Column(Numeric(20, 4), comment='利率/参考收益率（%）')
    ISSUE_GOBJECT = Column(VARCHAR(200), comment='发行对象')


class CBONDBILLRATE(Base):
    """中国票据利率"""
    __tablename__ = 'CBONDBILLRATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_INFO_RATETYPE = Column(VARCHAR(100), comment='利率类型')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_INFO_RATE = Column(Numeric(20, 6), comment='利率(%)')


class CBONDBLOCKTRADE(Base):
    """中国债券大宗交易"""
    __tablename__ = 'CBONDBLOCKTRADE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券id')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_BLOCK_PRICE = Column(Numeric(20, 4), comment='成交价（元）')
    S_BLOCK_VOLUME = Column(Numeric(20, 4), comment='成交量（万股）')
    S_BLOCK_AMOUNT = Column(Numeric(20, 4), comment='成交金额（万元）')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_BLOCK_BUYERNAME = Column(VARCHAR(200), comment='买方营业部')
    S_BLOCK_SELLERNAME = Column(VARCHAR(200), comment='卖方营业部')
    S_BLOCK_FREQUENCY = Column(Numeric(20, 4), comment='笔数')


class CBONDCALENDAR(Base):
    """中国债券交易日历"""
    __tablename__ = 'CBONDCALENDAR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DAYS = Column(VARCHAR(8), comment='交易日')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class CBONDCALENDARZL(Base):
    """中国债券市场交易日(增量)"""
    __tablename__ = 'CBONDCALENDARZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DAYS = Column(VARCHAR(8), comment='交易日')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class CBONDCALL(Base):
    """中国债券赎回条款执行说明"""
    __tablename__ = 'CBONDCALL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REDEMPTIONDATE = Column(VARCHAR(8), comment='赎回日')
    B_INFO_REDEMPTIONPRICE = Column(Numeric(20, 4), comment='每百元面值赎回价格(元)')
    B_INFO_CALLANNOUNCEMENTDATE = Column(VARCHAR(8), comment='赎回公告日')
    B_INFO_CALLEXDATE = Column(VARCHAR(8), comment='赎回履行结果公告日')
    B_INFO_CALLAMOUNT = Column(Numeric(20, 4), comment='赎回总面额(亿元)')
    B_INFO_CALLOUTSTANDING = Column(Numeric(20, 4), comment='继续托管总面额(亿元)')
    B_REDEMPTIONDATE = Column(VARCHAR(8), comment='赎回日(公布)')
    B_INFO_CALL_REASON = Column(VARCHAR(1000), comment='赎回原因')
    B_INFO_CALL_ARRIVAL_DAY = Column(VARCHAR(8), comment='赎回资金到账日')
    B_INFO_CALL_RECORD_DAY = Column(VARCHAR(8), comment='赎回登记日')


class CBONDCALLQL(Base):
    """None"""
    __tablename__ = 'CBONDCALLQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    B_INFO_REDEMPTIONDATE = Column(VARCHAR(8))
    B_INFO_REDEMPTIONPRICE = Column(Numeric(20, 4))
    B_INFO_CALLANNOUNCEMENTDATE = Column(VARCHAR(8))
    B_INFO_CALLEXDATE = Column(VARCHAR(8))
    B_INFO_CALLAMOUNT = Column(Numeric(20, 4))
    B_INFO_CALLOUTSTANDING = Column(Numeric(20, 4))
    B_REDEMPTIONDATE = Column(VARCHAR(8))
    B_INFO_CALL_REASON = Column(VARCHAR(1000))
    B_INFO_CALL_ARRIVAL_DAY = Column(VARCHAR(8))
    B_INFO_CALL_RECORD_DAY = Column(VARCHAR(8))


class CBONDCALLZL(Base):
    """中国债券赎回条款执行说明(增量)"""
    __tablename__ = 'CBONDCALLZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REDEMPTIONDATE = Column(VARCHAR(8), comment='赎回日')
    B_INFO_REDEMPTIONPRICE = Column(Numeric(20, 4), comment='每百元面值赎回价格(元)')
    B_INFO_CALLANNOUNCEMENTDATE = Column(VARCHAR(8), comment='赎回公告日')
    B_INFO_CALLEXDATE = Column(VARCHAR(8), comment='赎回履行结果公告日')
    B_INFO_CALLAMOUNT = Column(Numeric(20, 4), comment='赎回总面额(亿元)')
    B_INFO_CALLOUTSTANDING = Column(Numeric(20, 4), comment='继续托管总面额(亿元)')
    B_REDEMPTIONDATE = Column(VARCHAR(8), comment='赎回日(公布)')
    B_INFO_CALL_REASON = Column(VARCHAR(1000), comment='赎回原因')
    B_INFO_CALL_ARRIVAL_DAY = Column(VARCHAR(8), comment='赎回资金到账日')
    B_INFO_CALL_RECORD_DAY = Column(VARCHAR(8), comment='赎回登记日')


class CBONDCASHFLOW(Base):
    """中国债券发行主体现金流量表"""
    __tablename__ = 'CBONDCASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    CASH_RECP_SG_AND_RS = Column(Numeric(20, 4), comment='销售商品、提供劳务收到的现金')
    RECP_TAX_RENDS = Column(Numeric(20, 4), comment='收到的税费返还')
    NET_INCR_DEP_COB = Column(Numeric(20, 4), comment='客户存款和同业存放款项净增加额')
    NET_INCR_LOANS_CENTRAL_BANK = Column(Numeric(20, 4), comment='向中央银行借款净增加额')
    NET_INCR_FUND_BORR_OFI = Column(Numeric(20, 4), comment='向其他金融机构拆入资金净增加额')
    CASH_RECP_PREM_ORIG_INCO = Column(Numeric(20, 4), comment='收到原保险合同保费取得的现金')
    NET_INCR_INSURED_DEP = Column(Numeric(20, 4), comment='保户储金净增加额')
    NET_CASH_RECEIVED_REINSU_BUS = Column(Numeric(20, 4), comment='收到再保业务现金净额')
    NET_INCR_DISP_TFA = Column(Numeric(20, 4), comment='处置交易性金融资产净增加额')
    NET_INCR_INT_HANDLING_CHRG = Column(Numeric(20, 4), comment='收取利息和手续费净增加额')
    NET_INCR_DISP_FAAS = Column(Numeric(20, 4), comment='处置可供出售金融资产净增加额')
    NET_INCR_LOANS_OTHER_BANK = Column(Numeric(20, 4), comment='拆入资金净增加额')
    NET_INCR_REPURCH_BUS_FUND = Column(Numeric(20, 4), comment='回购业务资金净增加额')
    OTHER_CASH_RECP_RAL_OPER_ACT = Column(Numeric(20, 4), comment='收到其他与经营活动有关的现金')
    STOT_CASH_INFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流入小计')
    CASH_PAY_GOODS_PURCH_SERV_REC = Column(Numeric(20, 4), comment='购买商品、接受劳务支付的现金')
    CASH_PAY_BEH_EMPL = Column(Numeric(20, 4), comment='支付给职工以及为职工支付的现金')
    PAY_ALL_TYP_TAX = Column(Numeric(20, 4), comment='支付的各项税费')
    NET_INCR_CLIENTS_LOAN_ADV = Column(Numeric(20, 4), comment='客户贷款及垫款净增加额')
    NET_INCR_DEP_CBOB = Column(Numeric(20, 4), comment='存放央行和同业款项净增加额')
    CASH_PAY_CLAIMS_ORIG_INCO = Column(Numeric(20, 4), comment='支付原保险合同赔付款项的现金')
    HANDLING_CHRG_PAID = Column(Numeric(20, 4), comment='支付手续费的现金')
    COMM_INSUR_PLCY_PAID = Column(Numeric(20, 4), comment='支付保单红利的现金')
    OTHER_CASH_PAY_RAL_OPER_ACT = Column(Numeric(20, 4), comment='支付其他与经营活动有关的现金')
    STOT_CASH_OUTFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流出小计')
    NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额')
    CASH_RECP_DISP_WITHDRWL_INVEST = Column(Numeric(20, 4), comment='收回投资收到的现金')
    CASH_RECP_RETURN_INVEST = Column(Numeric(20, 4), comment='取得投资收益收到的现金')
    NET_CASH_RECP_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定资产、无形资产和其他长期资产收回的现金净额')
    NET_CASH_RECP_DISP_SOBU = Column(Numeric(20, 4), comment='处置子公司及其他营业单位收到的现金净额')
    OTHER_CASH_RECP_RAL_INV_ACT = Column(Numeric(20, 4), comment='收到其他与投资活动有关的现金')
    STOT_CASH_INFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流入小计')
    CASH_PAY_ACQ_CONST_FIOLTA = Column(Numeric(20, 4), comment='购建固定资产、无形资产和其他长期资产支付的现金')
    CASH_PAID_INVEST = Column(Numeric(20, 4), comment='投资支付的现金')
    NET_CASH_PAY_AQUIS_SOBU = Column(Numeric(20, 4), comment='取得子公司及其他营业单位支付的现金净额')
    OTHER_CASH_PAY_RAL_INV_ACT = Column(Numeric(20, 4), comment='支付其他与投资活动有关的现金')
    NET_INCR_PLEDGE_LOAN = Column(Numeric(20, 4), comment='质押贷款净增加额')
    STOT_CASH_OUTFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流出小计')
    NET_CASH_FLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额')
    CASH_RECP_CAP_CONTRIB = Column(Numeric(20, 4), comment='吸收投资收到的现金')
    INCL_CASH_REC_SAIMS = Column(Numeric(20, 4), comment='其中:子公司吸收少数股东投资收到的现金')
    CASH_RECP_BORROW = Column(Numeric(20, 4), comment='取得借款收到的现金')
    PROC_ISSUE_BONDS = Column(Numeric(20, 4), comment='发行债券收到的现金')
    OTHER_CASH_RECP_RAL_FNC_ACT = Column(Numeric(20, 4), comment='收到其他与筹资活动有关的现金')
    STOT_CASH_INFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流入小计')
    CASH_PREPAY_AMT_BORR = Column(Numeric(20, 4), comment='偿还债务支付的现金')
    CASH_PAY_DIST_DPCP_INT_EXP = Column(Numeric(20, 4), comment='分配股利、利润或偿付利息支付的现金')
    INCL_DVD_PROFIT_PAID_SC_MS = Column(Numeric(20, 4), comment='其中:子公司支付给少数股东的股利、利润')
    OTHER_CASH_PAY_RAL_FNC_ACT = Column(Numeric(20, 4), comment='支付其他与筹资活动有关的现金')
    STOT_CASH_OUTFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流出小计')
    NET_CASH_FLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额')
    EFF_FX_FLU_CASH = Column(Numeric(20, 4), comment='汇率变动对现金的影响')
    NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物净增加额')
    CASH_CASH_EQU_BEG_PERIOD = Column(Numeric(20, 4), comment='期初现金及现金等价物余额')
    CASH_CASH_EQU_END_PERIOD = Column(Numeric(20, 4), comment='期末现金及现金等价物余额')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认投资损失')
    PLUS_PROV_DEPR_ASSETS = Column(Numeric(20, 4), comment='加:资产减值准备')
    DEPR_FA_COGA_DPBA = Column(Numeric(20, 4), comment='固定资产折旧、油气资产折耗、生产性生物资产折旧')
    AMORT_INTANG_ASSETS = Column(Numeric(20, 4), comment='无形资产摊销')
    AMORT_LT_DEFERRED_EXP = Column(Numeric(20, 4), comment='长期待摊费用摊销')
    DECR_DEFERRED_EXP = Column(Numeric(20, 4), comment='待摊费用减少')
    INCR_ACC_EXP = Column(Numeric(20, 4), comment='预提费用增加')
    LOSS_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定、无形资产和其他长期资产的损失')
    LOSS_SCR_FA = Column(Numeric(20, 4), comment='固定资产报废损失')
    LOSS_FV_CHG = Column(Numeric(20, 4), comment='公允价值变动损失')
    FIN_EXP = Column(Numeric(20, 4), comment='财务费用')
    INVEST_LOSS = Column(Numeric(20, 4), comment='投资损失')
    DECR_DEFERRED_INC_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产减少')
    INCR_DEFERRED_INC_TAX_LIAB = Column(Numeric(20, 4), comment='递延所得税负债增加')
    DECR_INVENTORIES = Column(Numeric(20, 4), comment='存货的减少')
    DECR_OPER_PAYABLE = Column(Numeric(20, 4), comment='经营性应收项目的减少')
    INCR_OPER_PAYABLE = Column(Numeric(20, 4), comment='经营性应付项目的增加')
    OTHERS = Column(Numeric(20, 4), comment='其他')
    IM_NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='间接法-经营活动产生的现金流量净额')
    CONV_DEBT_INTO_CAP = Column(Numeric(20, 4), comment='债务转为资本')
    CONV_CORP_BONDS_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的可转换公司债券')
    FA_FNC_LEASES = Column(Numeric(20, 4), comment='融资租入固定资产')
    END_BAL_CASH = Column(Numeric(20, 4), comment='现金的期末余额')
    LESS_BEG_BAL_CASH = Column(Numeric(20, 4), comment='减:现金的期初余额')
    PLUS_END_BAL_CASH_EQU = Column(Numeric(20, 4), comment='加:现金等价物的期末余额')
    LESS_BEG_BAL_CASH_EQU = Column(Numeric(20, 4), comment='减:现金等价物的期初余额')
    IM_NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='间接法-现金及现金等价物净增加额')
    FREE_CASH_FLOW = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)')
    COMP_TYPE_CODE = Column(VARCHAR(2), comment='公司类型代码')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    SPE_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(合计平衡项目)')
    SPE_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(合计平衡项目)')
    TOT_BAL_NETCASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额差额(合计平衡项目)')
    SPE_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(合计平衡项目)')
    SPE_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(合计平衡项目)')
    TOT_BAL_NETCASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额差额(合计平衡项目)')
    SPE_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(合计平衡项目)')
    SPE_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(合计平衡项目)')
    TOT_BAL_NETCASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额差额(合计平衡项目)')
    SPE_BAL_NETCASH_INC = Column(Numeric(20, 4), comment='现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_INC = Column(Numeric(20, 4), comment='现金净增加额差额(合计平衡项目)')
    SPE_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(合计平衡项目)')
    SPE_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(合计平衡项目)')
    AUDIT_AM = Column(Numeric(1, 0), comment='采用会计准则')
    CHANGE_SECURITIES_NET_CASH = Column(Numeric(20, 4), comment='代理买卖证券收到的现金净额')
    NET_ADD_MELT_OUT_MONEY = Column(Numeric(20, 4), comment='融出资金净增加额')
    S_DISMANTLE_CAPITAL_ADD_NET = Column(Numeric(20, 4), comment='拆出资金净增加额')
    IS_CALCULATION = Column(Numeric(5, 0), comment='是否计算报表')


class CBONDCBISSUEAPPROVE(Base):
    """中国债券企业债发行核准信息"""
    __tablename__ = 'CBONDCBISSUEAPPROVE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='发行人公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    EXPIRYDATE = Column(VARCHAR(8), comment='有效期截止日')
    APPROVEOBJ = Column(VARCHAR(100), comment='核准项目')
    BATCHNUM_NDRC = Column(VARCHAR(50), comment='发改委批号')
    MAX_AMOUNT = Column(Numeric(20, 4), comment='最大发行规模')
    ISSUETERM = Column(Numeric(10, 4), comment='发行期限')
    RATETYPE = Column(Numeric(9, 0), comment='利率类型')
    PAYMENTTYPE = Column(Numeric(9, 0), comment='计息方式')
    PAYMENTCYCLE = Column(Numeric(9, 0), comment='计息周期')
    IS_INSTALL = Column(Numeric(1, 0), comment='是否可分期发行')
    SPECIALCLAUSESTYPE = Column(VARCHAR(100), comment='特殊条款类型')
    CREDITRATING = Column(VARCHAR(10), comment='信用评级')
    CREDITRATINGAGENCY = Column(VARCHAR(40), comment='评估机构')
    GUARINTRODUCTION = Column(VARCHAR(100), comment='担保情况')
    FUNDUSING = Column(VARCHAR, comment='募集资金用途')
    LU_COMPCODE = Column(VARCHAR(500), comment='主承销商公司ID')
    LU_TYPE = Column(Numeric(9, 0), comment='承销方式')
    ALLOWTIME = Column(VARCHAR(8), comment='许可时间')


class CBONDCF(Base):
    """中国债券现金流"""
    __tablename__ = 'CBONDCF'
    __table_args__ = (
        Index('IDX_CBONDCF_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_CARRYDATE = Column(VARCHAR(8), comment='计息起始日')
    B_INFO_ENDDATE = Column(VARCHAR(8), comment='计息截止日')
    B_INFO_COUPONRATE = Column(Numeric(22, 6), comment='票面利率(%)')
    B_INFO_PAYMENTDATE = Column(VARCHAR(8), comment='现金流发放日')
    B_INFO_PAYMENTINTEREST = Column(Numeric(22, 12), comment='期末每百元面额应付利息')
    B_INFO_PAYMENTPARVALUE = Column(Numeric(22, 12), comment='期末每百元面额应付本金')
    B_INFO_PAYMENTSUM = Column(Numeric(22, 12), comment='期末每百元面额现金流合计')


class CBONDCHANGECLAUSE(Base):
    """中国债券调换条款执行说明"""
    __tablename__ = 'CBONDCHANGECLAUSE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='证券ID')
    S_INFO_WINDCODE2 = Column(VARCHAR(40), comment='目标证券ID')
    S_INFO_EXECDATE = Column(VARCHAR(8), comment='行权日期')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_INFO_REPURCHASESTARTDATE = Column(VARCHAR(8), comment='申请起始日')
    S_INFO_REPURCHASEENDDATE = Column(VARCHAR(8), comment='申请截止日')
    S_INFO_MIN_OPERATION_AMOUNT = Column(Numeric(20, 4), comment='最低操作金额')
    S_INFO_CONVERSION_RATIO = Column(VARCHAR(20), comment='调换比例')
    S_INFO_TRUSTEESHIP = Column(Numeric(20, 4), comment='原托管面额')
    S_INFO_POSTRIGHT_TRUSTEESHIP = Column(Numeric(20, 4), comment='行权后托管面额')


class CBONDCIRCULATINGHOLDERS(Base):
    """中国债券公司流通股东持股比例"""
    __tablename__ = 'CBONDCIRCULATINGHOLDERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(200), comment='股东公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='股东公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='股东公司ID')
    S_HOLDER_ENDDATE = Column(VARCHAR(10), comment='报告期')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例')


class CBONDCOLLATERALINFORMATION(Base):
    """中国债券抵押品信息"""
    __tablename__ = 'CBONDCOLLATERALINFORMATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='wind代码')
    B_AGENCY_GRNTTYPECODE = Column(Numeric(9, 0), comment='担保方式代码')
    B_AGENCY_COLLATERALTYPECODE = Column(Numeric(9, 0), comment='担保物类型代码')
    EQY_TARGETCOMP = Column(VARCHAR(10), comment='股权标的')
    B_GUARANTEEOWNER = Column(VARCHAR(400), comment='担保物所有方')
    B_GUARANTEEOWNER_COMPCODE = Column(VARCHAR(10), comment='担保物所有方公司ID')
    B_INFO_COLLATERALNUMBER = Column(Numeric(20, 4), comment='担保物数量')
    B_INFO_COLLATERALPUNIT = Column(VARCHAR(40), comment='担保物单位')
    B_INFO_COLLATERALVALUE = Column(Numeric(20, 4), comment='担保物价值')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    B_INFO_GUARINTRODUCTION = Column(VARCHAR(400), comment='[内部]担保情况')


class CBONDCOMPANYHOLDSHARES(Base):
    """中国债券发行主体控股参股"""
    __tablename__ = 'CBONDCOMPANYHOLDSHARES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_CAPITALOPERATION_COMPANYNAME = Column(VARCHAR(100), comment='被参控公司名称')
    S_CAPITALOPERATION_COMPANYID = Column(VARCHAR(10), comment='被参控公司ID')
    S_CAPITALOPERATION_COMAINBUS = Column(VARCHAR(1300), comment='被参控公司主营业务')
    RELATIONS_CODE = Column(VARCHAR(40), comment='关系代码')
    S_CAPITALOPERATION_PCT = Column(Numeric(20, 4), comment='直接持股比例')
    VOTING_RIGHTS = Column(Numeric(20, 4), comment='表决权比例')
    S_CAPITALOPERATION_AMOUNT = Column(Numeric(20, 4), comment='投资金额(万元)')
    OPERATIONCRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_CAPITALOPERATION_COREGCAP = Column(Numeric(20, 4), comment='被参股公司注册资本(万元)')
    CAPITALCRNCY_CODE = Column(VARCHAR(10), comment='注册资本货币代码')
    IS_CONSOLIDATE = Column(Numeric(5, 0), comment='是否合并报表')
    NOTCONSOLIDATE_REASON = Column(VARCHAR(500), comment='未纳入合并报表原因')


class CBONDCOMPANYILLEGALITY(Base):
    """中国债券发行主体违规事件"""
    __tablename__ = 'CBONDCOMPANYILLEGALITY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ILLEG_TYPE = Column(VARCHAR(100), comment='违规类型')
    SUBJECT_TYPE = Column(Numeric(9, 0), comment='主体类别代码')
    SUBJECT = Column(VARCHAR(100), comment='违规主体')
    RELATION_TYPE = Column(Numeric(9, 0), comment='与上市公司的关系')
    BEHAVIOR = Column(VARCHAR, comment='违规行为')
    DISPOSAL_DT = Column(VARCHAR(8), comment='处罚日期')
    DISPOSAL_TYPE = Column(VARCHAR(100), comment='处分类型')
    METHODD = Column(VARCHAR(2000), comment='处分措施')
    PROCESSOR = Column(VARCHAR(200), comment='处理人')
    AMOUNT = Column(Numeric(20, 4), comment='处罚金额(元)')
    BAN_YEAR = Column(Numeric(20, 4), comment='市场禁入期限(年)')
    REF_RULE = Column(VARCHAR(1000), comment='相关法规')
    ILLEG_TYPE_CODE = Column(VARCHAR(1000), comment='违规类型代码')
    ANN_ID = Column(Numeric(11, 0), comment='公告id')


class CBONDCOMPANYPREVIOUSNAME(Base):
    """中国债券发行主体公司曾用名"""
    __tablename__ = 'CBONDCOMPANYPREVIOUSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')
    COMP_NAME_ENG = Column(VARCHAR(200), comment='公司英文名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    CHANGE_REASON = Column(VARCHAR(100), comment='更名原因')


class CBONDCONCEPTUALPLATE(Base):
    """中国债券公司概念板块"""
    __tablename__ = 'CBONDCONCEPTUALPLATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')


class CBONDCONVERSIONRATIO(Base):
    """回购标准券折算率"""
    __tablename__ = 'CBONDCONVERSIONRATIO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_CVN_STARTDATE = Column(VARCHAR(8), comment='开始适用日')
    B_CVN_ENDDATE = Column(VARCHAR(8), comment='结束适用日')
    B_CVN_RATEOFSTDBND = Column(Numeric(20, 4), comment='折算比例')
    B_CVN_CVNTPERHUNDRED = Column(Numeric(20, 4), comment='折合标准券')
    B_CVN_RATEOFSTDBNDCSI = Column(Numeric(20, 8), comment='报价式回购折算率')


class CBONDCONVERTIBLEPACTERMS(Base):
    """中国债券可转债回售赎回条款"""
    __tablename__ = 'CBONDCONVERTIBLEPACTERMS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    MAND_PUTPERIOD = Column(VARCHAR(40), comment='无条件回售期')
    MAND_PUTPRICE = Column(Numeric(20, 4), comment='无条件回售价')
    MAND_PUTSTARTDT = Column(VARCHAR(8), comment='无条件回售开始日期')
    MAND_PUTENDDT = Column(VARCHAR(8), comment='无条件回售结束日期')
    MANDPUT_TEXT = Column(VARCHAR(800), comment='无条件回售文字条款')
    IS_MUPCONTAININT = Column(Numeric(5, 0), comment='无条件回售价是否含当期利息')
    CON_PUTSTARTDT = Column(VARCHAR(8), comment='有条件回售起始日期')
    CON_PUTENDDT = Column(VARCHAR(8), comment='有条件回售结束日期')
    MAX_PUTTRIPER = Column(Numeric(5, 0), comment='回售触发计算最大时间区间')
    PUTTRIPERIOD = Column(Numeric(5, 0), comment='回售触发计算时间区间')
    ADD_PUTCON = Column(VARCHAR(800), comment='附加回售条件')
    ADD_PUTPRIINS = Column(VARCHAR(200), comment='附加回售价格说明')
    PUTNUMBER_INS = Column(VARCHAR(200), comment='回售次数说明')
    PUTPRO_PERIOD = Column(Numeric(20, 4), comment='相对回售期(月)')
    PUTNO_PERY = Column(Numeric(20, 4), comment='每年回售次数')
    IS_PUTITEM = Column(Numeric(5, 0), comment='是否有回售条款')
    IS_TERMPUTITEM = Column(Numeric(5, 0), comment='是否有到期回售条款')
    IS_MANDPUTITEM = Column(Numeric(5, 0), comment='是否有无条件回售条款')
    IS_TIMEPUTITEM = Column(Numeric(5, 0), comment='是否有时点回售条款')
    TIMEPUT_NO = Column(Numeric(20, 4), comment='时点回售数')
    TIMEPUTITEM = Column(VARCHAR(800), comment='时点回售文字条款')
    TERM_PUTPRICE = Column(Numeric(20, 4), comment='到期回售价')
    CON_CALLSTARTDT = Column(VARCHAR(8), comment='有条件赎回起始日期')
    CON_CALLENDDT = Column(VARCHAR(8), comment='有条件赎回结束日期')
    CALLTRICON_INS = Column(VARCHAR(800), comment='赎回触发条件说明')
    MAX_CALLTRIPER = Column(Numeric(5, 0), comment='赎回触发计算最大时间区间')
    CALLTRIPER = Column(Numeric(5, 0), comment='赎回触发计算时间区间')
    CALLNUMBER_INS = Column(VARCHAR(100), comment='赎回次数说明')
    IS_CALLITEM = Column(Numeric(5, 0), comment='是否有赎回条款')
    CALLPRO_PERIOD = Column(Numeric(20, 4), comment='相对赎回期(月)')
    CALLNO_PERY = Column(Numeric(20, 4), comment='每年赎回次数')
    IS_TIMECALLITEM = Column(Numeric(5, 0), comment='是否有时点赎回条款')
    TIMECALL_NO = Column(Numeric(20, 4), comment='时点赎回数')
    TIMECALL_TEXT = Column(VARCHAR(800), comment='时点赎回文字条款')


class CBONDCONVPRICE(Base):
    """中国可转债转股价格变动"""
    __tablename__ = 'CBONDCONVPRICE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    B_INFO_ANNOUNCEMENTDATE = Column(VARCHAR(8), comment='公告日期')
    CB_ANAL_CONVPRICE = Column(Numeric(20, 4), comment='转股价格')
    B_INFO_CHANGEREASON = Column(VARCHAR(1000), comment='变动原因')


class CBONDCOUNTERPRICE(Base):
    """银行柜台债券行情"""
    __tablename__ = 'CBONDCOUNTERPRICE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    BANK_ID = Column(VARCHAR(10), comment='银行ID')
    BID_CLEAN_PRICE = Column(Numeric(15, 4), comment='买入价(元)')
    ASK_CLEAN_PRICE = Column(Numeric(15, 4), comment='卖出价(元)')
    B_ANAL_PTMYEAR = Column(Numeric(15, 4), comment='剩余期限(年)')
    B_ANAL_YTM = Column(Numeric(15, 4), comment='到期收益率(%)')
    BID_AMOUNT = Column(Numeric(15, 4), comment='买入金额(万元)')
    ASK_AMOUNT = Column(Numeric(15, 4), comment='卖出金额(万元)')
    B_ANAL_ACCRUEDINTEREST = Column(Numeric(15, 4), comment='应计利息(元)')


class CBONDCREDITORRIGHTS(Base):
    """中国债券公司关联方债权"""
    __tablename__ = 'CBONDCREDITORRIGHTS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='债务公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='债务中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='债务公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class CBONDCURVECNBD(Base):
    """中债登债券收益率曲线"""
    __tablename__ = 'CBONDCURVECNBD'
    __table_args__ = (
        Index('INDEX_BAC_TRADE_DT', 'B_ANAL_CURVENUMBER', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_CURVENUMBER = Column(Numeric(10, 0), comment='曲线编号')
    B_ANAL_CURVENAME = Column(VARCHAR(200), comment='曲线名称')
    B_ANAL_CURVETYPE = Column(VARCHAR(80), comment='曲线类型')
    B_ANAL_CURVETERM = Column(Numeric(20, 4), comment='标准期限(年)')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='收益率(%)')
    B_ANAL_BASE_YIELD = Column(Numeric(20, 4), comment='估值日基础利率')
    B_ANAL_YIELD_TOTAL = Column(Numeric(20, 4), comment='收益率曲线数值')


class CBONDCURVECSI(Base):
    """中证收益率曲线"""
    __tablename__ = 'CBONDCURVECSI'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_CURVENUMBER = Column(VARCHAR(5), comment='曲线编号')
    B_ANAL_CURVENAME = Column(VARCHAR(200), comment='曲线名称')
    B_ANAL_CURVETYPE = Column(VARCHAR(20), comment='曲线类型')
    B_ANAL_CURVETERM = Column(Numeric(20, 4), comment='年限')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='收益率(%)')


class CBONDCURVEMEMBERSCNBD(Base):
    """中债登收益率曲线成分样本"""
    __tablename__ = 'CBONDCURVEMEMBERSCNBD'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_CURVENUMBER = Column(Numeric(10, 0), comment='曲线编号')
    B_ANAL_CURVENAME = Column(VARCHAR(200), comment='曲线名称')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='债券代码')
    CNBD_CREDITRATING = Column(VARCHAR(300), comment='中债隐含评级')


class CBONDCURVESHC(Base):
    """上海清算所收益率曲线"""
    __tablename__ = 'CBONDCURVESHC'
    __table_args__ = (
        Index('IDX_CBONDCURVESHC_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_CURVENUMBER = Column(Numeric(10, 0), comment='曲线编号')
    B_ANAL_CURVENAME = Column(VARCHAR(200), comment='曲线名称')
    B_ANAL_CURVETYPE = Column(VARCHAR(20), comment='曲线类型')
    B_ANAL_CURVETERM = Column(Numeric(20, 4), comment='年限')
    B_ANAL_YIELD = Column(Numeric(20, 4), comment='收益率(%)')


class CBONDCUSTOMER(Base):
    """中国债券公司客户"""
    __tablename__ = 'CBONDCUSTOMER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='下游公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='下游公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='下游公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')
    S_INFO_DISCLOSER = Column(VARCHAR(100), comment='披露公司ID')
    PCT = Column(Numeric(20, 4), comment='占比(%)')


class CBONDDEFAULTPAYMENT(Base):
    """中国债券违约兑付表"""
    __tablename__ = 'CBONDDEFAULTPAYMENT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='证券ID')
    B_ANNOUNCEMENTDATE = Column(VARCHAR(8), comment='公告日')
    B_ACTUAL_PAYMENT = Column(VARCHAR(8), comment='实际兑付日')
    B_PAYMENT_CODE = Column(Numeric(9, 0), comment='兑付类型代码')
    B_PAYMENT_FRONT_BALANCE = Column(Numeric(20, 4), comment='兑付前债券余额(元)')
    B_PAYMENT_AMOUNT = Column(Numeric(20, 4), comment='百元付息金额(元)')
    B_PRINCIPAL_AMOUNT = Column(Numeric(20, 4), comment='百元兑付本金金额(元)')
    B_PRINCIPAL_INTEREST_AMOUNT = Column(Numeric(20, 4), comment='百元兑付本息金额(元)')
    B_PRINCIPAL_AMOUNT_TOT = Column(Numeric(20, 4), comment='兑付本金总额(元)')
    B_PRINCIPAL_INT_AMOUNT_TOT = Column(Numeric(20, 4), comment='兑付利息总额(元)')
    B_RESALE_PAYMENT_TOT = Column(Numeric(20, 4), comment='兑付回售款总额(元)')
    B_RESALE_PAYMENT_TOT1 = Column(Numeric(20, 4), comment='兑付本息及回售款总额(元)')
    B_PAYMENT_AFTER_BALANCE = Column(Numeric(20, 4), comment='兑付后债券余额(元)')


class CBONDDEFAULTREPORTFORM(Base):
    """中国债券违约报表"""
    __tablename__ = 'CBONDDEFAULTREPORTFORM'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_ANNOUNCEMENTDATE = Column(VARCHAR(8), comment='公告日')
    B_DEFAULT_DATE = Column(VARCHAR(8), comment='违约发生日')
    B_DEFAULT_CODE = Column(Numeric(9, 0), comment='违约类型代码')
    B_DEFAULT_REASON = Column(VARCHAR(100), comment='违约原因')
    B_DEFAULT_DATE_BALANCE = Column(Numeric(20, 4), comment='违约日债券余额(元)')
    B_DEFAULTDATE_PAYABLECAPITAL = Column(Numeric(20, 4), comment='违约发生日百元应兑付本金(元)')
    B_DEFAULTDATE_PAYABLEINTEREST = Column(Numeric(20, 4), comment='违约发生日百元应兑付利息(元)')
    B_DEFAULTDATE_PAYABLE_CAP_INT = Column(Numeric(20, 4), comment='违约发生日百元应兑付本息(元)')
    B_DEFAULTDATE_PAYMENTCAPITAL = Column(Numeric(20, 4), comment='违约发生日实际百元兑付本金(元)')
    B_DEFAULTDATE_PAYMENTINTEREST = Column(Numeric(20, 4), comment='违约发生日实际百元兑付利息(元)')
    B_DEFAULTDATE_PAYMENT_CAP_INT = Column(Numeric(20, 4), comment='违约发生日实际百元兑付本息(元)')
    B_PRINCIPAL_PAYABLE = Column(Numeric(20, 4), comment='应付本金(元)')
    B_ANAL_ACCRUEDINTEREST = Column(Numeric(20, 4), comment='应付利息(元)')
    B_PAYABLE_RESALE_PAYMENT = Column(Numeric(20, 4), comment='应付回售款(元)')
    B_CAPITAL_RESALEPAYMENT = Column(Numeric(20, 4), comment='应付本息及回售款(元)')
    B_PAYMENT_PAYABLE = Column(Numeric(20, 4), comment='实付本金(元)')
    B_PAYMENT_INTEREST = Column(Numeric(20, 4), comment='实付利息(元)')
    B_PAYMENT_RESALE = Column(Numeric(20, 4), comment='实付回售款(元)')
    B_PAYMENT_CAP_INT_RESALE = Column(Numeric(20, 4), comment='实际兑付本息及回售款(元)')
    B_DEFAULT_DATE_BALANCE1 = Column(Numeric(20, 4), comment='违约日债券余额(日终)(元)')


class CBONDDEFENDANT(Base):
    """中国债券公司诉讼-被告"""
    __tablename__ = 'CBONDDEFENDANT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='诉讼公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='诉讼公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='诉讼公司ID')
    S_INFO_CASE_TYPE = Column(VARCHAR(10), comment='案件类型')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    LITIGATION_EVENTS_ID = Column(VARCHAR(40), comment='诉讼事件ID')


class CBONDDESCRIPTION(Base):
    """中国债券基本资料"""
    __tablename__ = 'CBONDDESCRIPTION'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),
        Index('IDX_CBONDDESCRIPTION_ISSUER', 'B_INFO_ISSUER'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_FULLNAME = Column(VARCHAR(200), comment='债券名称')
    B_INFO_ISSUER = Column(VARCHAR(100), comment='发行人')
    B_ISSUE_ANNOUNCEMENT = Column(VARCHAR(8), comment='发行公告日')
    B_ISSUE_FIRSTISSUE = Column(VARCHAR(8), comment='发行起始日')
    B_ISSUE_LASTISSUE = Column(VARCHAR(8), comment='发行截止日')
    B_ISSUE_AMOUNTPLAN = Column(Numeric(20, 4), comment='计划发行总量(亿元)')
    B_ISSUE_AMOUNTACT = Column(Numeric(20, 4), comment='实际发行总量(亿元)')
    B_INFO_ISSUEPRICE = Column(Numeric(20, 4), comment='发行价格')
    B_INFO_PAR = Column(Numeric(20, 0), comment='面值')
    B_INFO_COUPONRATE = Column(Numeric(20, 4), comment='发行票面利率(%)')
    B_INFO_SPREAD = Column(Numeric(20, 4), comment='利差(%)')
    B_INFO_CARRYDATE = Column(VARCHAR(8), comment='计息起始日')
    B_INFO_ENDDATE = Column(VARCHAR(8), comment='计息截止日')
    B_INFO_MATURITYDATE = Column(VARCHAR(8), comment='到期日')
    B_INFO_TERM_YEAR_ = Column(Numeric(20, 4), comment='债券期限(年)')
    B_INFO_TERM_DAY_ = Column(Numeric(20, 4), comment='债券期限(天)')
    B_INFO_PAYMENTDATE = Column(VARCHAR(8), comment='兑付日')
    B_INFO_PAYMENTTYPE = Column(Numeric(9, 0), comment='计息方式')
    B_INFO_INTERESTFREQUENCY = Column(VARCHAR(20), comment='付息频率')
    B_INFO_FORM = Column(VARCHAR(10), comment='债券形式')
    B_INFO_COUPON = Column(Numeric(9, 0), comment='息票品种')
    B_INFO_INTERESTTYPE = Column(Numeric(9, 0), comment='附息利率品种')
    B_INFO_ACT = Column(Numeric(20, 4), comment='特殊年计息天数')
    B_ISSUE_FEE = Column(Numeric(20, 4), comment='发行手续费率(%)')
    B_REDEMPTION_FEERATION = Column(Numeric(20, 4), comment='兑付手续费率(%)')
    B_INFO_TAXRATE = Column(Numeric(20, 4), comment='所得税率')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='债券简称')
    S_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    B_INFO_GUARANTOR = Column(VARCHAR(100), comment='担保人')
    B_INFO_GUARTYPE = Column(Numeric(9, 0), comment='担保方式')
    B_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    B_INFO_YEARSNUMBER = Column(Numeric(20, 0), comment='年内序号')
    S_DIV_RECORDDATE = Column(VARCHAR(8), comment='兑付登记起始日')
    B_INFO_CODEBYPLACING = Column(VARCHAR(10), comment='上网发行认购代码')
    B_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    B_INFO_ISSUETYPE = Column(Numeric(9, 0), comment='发行方式')
    B_INFO_GUARINTRODUCTION = Column(VARCHAR(500), comment='担保简介')
    B_INFO_BGNDBYPLACING = Column(VARCHAR(8), comment='上网发行起始日期')
    B_INFO_ENDDBYPLACING = Column(VARCHAR(8), comment='上网发行截止日期')
    B_INFO_AMOUNTBYPLACING = Column(Numeric(20, 4), comment='上网发行数量(亿元)')
    B_INFO_UNDERWRITINGCODE = Column(Numeric(9, 0), comment='承销方式代码')
    B_INFO_ISSUERCODE = Column(VARCHAR(100), comment='发行人编号')
    B_INFO_FORMERCODE = Column(VARCHAR(40), comment='原债券代码')
    B_INFO_COUPONTXT = Column(VARCHAR(1000), comment='利率说明')
    IS_FAILURE = Column(Numeric(5, 0), comment='是否发行失败')
    IS_CROSSMARKET = Column(Numeric(5, 0), comment='是否跨市场')
    B_INFO_COUPONDATETXT = Column(VARCHAR(1300), comment='付息日说明')
    B_INFO_SUBORDINATEORNOT = Column(Numeric(5, 0), comment='是否次级债或混合资本债')
    B_TENDRST_REFERYIELD = Column(Numeric(20, 4), comment='参考收益率')
    B_INFO_CURPAR = Column(Numeric(20, 4), comment='最新面值')
    S_INFO_FORMERWINDCODE = Column(VARCHAR(40), comment='原Wind代码')
    IS_CORPORATE_BOND = Column(Numeric(5, 0), comment='是否公司债')
    B_INFO_ISSUERTYPE = Column(VARCHAR(40), comment='发行人类型')
    B_INFO_SPECIALBONDTYPE = Column(VARCHAR(40), comment='特殊债券类型')
    IS_PAYADVANCED = Column(VARCHAR(1), comment='是否可提前兑付')
    IS_CALLABLE = Column(VARCHAR(1), comment='是否可赎回')
    IS_CHOOSERIGHT = Column(VARCHAR(1), comment='是否有选择权')
    IS_NETPRICE = Column(Numeric(1, 0), comment='是否净价')
    IS_ACT_DAYS = Column(Numeric(1, 0), comment='是否按实际天数计息')
    IS_INCBONDS = Column(Numeric(5, 0), comment='是否增发债')
    ISSUE_OBJECT = Column(VARCHAR(100), comment='发行对象')
    B_INFO_ACTUALBENCHMARK = Column(VARCHAR(8), comment='计息基准')
    REGISTER_FILE_TYPE_CODE = Column(Numeric(9, 0), comment='注册文件类型代码')
    REGISTER_FILE_NUMBER = Column(VARCHAR(1000), comment='注册文件号')
    LIST_ANN_DATE = Column(VARCHAR(8), comment='上市公告日')
    REIMBURSEMENT = Column(VARCHAR(20), comment='偿还方式')
    BOND_RATING = Column(VARCHAR(10), comment='发行时债券评级')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    B_ISSUE_AMOUNT_MAX = Column(Numeric(24, 8), comment='发行金额上限')
    B_INFO_GUARANTEE_ID = Column(VARCHAR(100), comment='担保人ID')


class CBONDDESCRIPTIONQL(Base):
    """None"""
    __tablename__ = 'CBONDDESCRIPTIONQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_FULLNAME = Column(VARCHAR(200), comment='债券名称')
    B_INFO_ISSUER = Column(VARCHAR(100), comment='发行人')
    B_ISSUE_ANNOUNCEMENT = Column(VARCHAR(8), comment='发行公告日')
    B_ISSUE_FIRSTISSUE = Column(VARCHAR(8), comment='发行起始日')
    B_ISSUE_LASTISSUE = Column(VARCHAR(8), comment='发行截止日')
    B_ISSUE_AMOUNTPLAN = Column(Numeric(24, 8), comment='计划发行总量(亿元)')
    B_ISSUE_AMOUNTACT = Column(Numeric(24, 8), comment='实际发行总量(亿元)')
    B_INFO_ISSUEPRICE = Column(Numeric(20, 4), comment='发行价格')
    B_INFO_PAR = Column(Numeric(20, 0), comment='面值')
    B_INFO_COUPONRATE = Column(Numeric(20, 4), comment='发行票面利率(%)')
    B_INFO_SPREAD = Column(Numeric(20, 4), comment='利差(%)')
    B_INFO_CARRYDATE = Column(VARCHAR(8), comment='计息起始日')
    B_INFO_ENDDATE = Column(VARCHAR(8), comment='计息截止日')
    B_INFO_MATURITYDATE = Column(VARCHAR(8), comment='到期日')
    B_INFO_TERM_YEAR_ = Column(Numeric(20, 4), comment='债券期限(年)')
    B_INFO_TERM_DAY_ = Column(Numeric(20, 4), comment='债券期限(天)')
    B_INFO_PAYMENTDATE = Column(VARCHAR(8), comment='兑付日')
    B_INFO_PAYMENTTYPE = Column(Numeric(9, 0), comment='计息方式')
    B_INFO_INTERESTFREQUENCY = Column(VARCHAR(20), comment='付息频率')
    B_INFO_FORM = Column(VARCHAR(10), comment='债券形式')
    B_INFO_COUPON = Column(Numeric(9, 0), comment='息票品种')
    B_INFO_INTERESTTYPE = Column(Numeric(9, 0), comment='附息利率品种')
    B_INFO_ACT = Column(Numeric(20, 4), comment='特殊年计息天数')
    B_ISSUE_FEE = Column(Numeric(20, 4), comment='发行手续费率(%)')
    B_REDEMPTION_FEERATION = Column(Numeric(20, 4), comment='兑付手续费率(%)')
    B_INFO_TAXRATE = Column(Numeric(20, 4), comment='所得税率')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='债券简称')
    S_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    B_INFO_GUARANTOR = Column(VARCHAR(100), comment='担保人')
    B_INFO_GUARTYPE = Column(Numeric(9, 0), comment='担保方式')
    B_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    B_INFO_YEARSNUMBER = Column(Numeric(20, 0), comment='年内序号')
    S_DIV_RECORDDATE = Column(VARCHAR(8), comment='兑付登记起始日')
    B_INFO_CODEBYPLACING = Column(VARCHAR(10), comment='上网发行认购代码')
    B_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    B_INFO_ISSUETYPE = Column(Numeric(9, 0), comment='发行方式')
    B_INFO_GUARINTRODUCTION = Column(VARCHAR(400), comment='担保简介')
    B_INFO_BGNDBYPLACING = Column(VARCHAR(8), comment='上网发行起始日期')
    B_INFO_ENDDBYPLACING = Column(VARCHAR(8), comment='上网发行截止日期')
    B_INFO_AMOUNTBYPLACING = Column(Numeric(20, 4), comment='上网发行数量(亿元)')
    B_INFO_UNDERWRITINGCODE = Column(Numeric(9, 0), comment='承销方式代码')
    B_INFO_ISSUERCODE = Column(VARCHAR(100), comment='发行人编号')
    B_INFO_FORMERCODE = Column(VARCHAR(40), comment='原债券代码')
    B_INFO_COUPONTXT = Column(VARCHAR(1000), comment='利率说明')
    IS_FAILURE = Column(Numeric(5, 0), comment='是否发行失败')
    IS_CROSSMARKET = Column(Numeric(5, 0), comment='是否跨市场')
    B_INFO_COUPONDATETXT = Column(VARCHAR(1000), comment='付息日说明')
    B_INFO_SUBORDINATEORNOT = Column(Numeric(5, 0), comment='是否次级债或混合资本债')
    B_TENDRST_REFERYIELD = Column(Numeric(20, 4), comment='参考收益率')
    B_INFO_CURPAR = Column(Numeric(20, 4), comment='最新面值')
    S_INFO_FORMERWINDCODE = Column(VARCHAR(40), comment='原Wind代码')
    IS_CORPORATE_BOND = Column(Numeric(5, 0), comment='是否公司债')
    B_INFO_ISSUERTYPE = Column(VARCHAR(40), comment='发行人类型')
    B_INFO_SPECIALBONDTYPE = Column(VARCHAR(40), comment='特殊债券类型')
    IS_PAYADVANCED = Column(VARCHAR(1), comment='是否可提前兑付')
    IS_CALLABLE = Column(VARCHAR(1), comment='是否可赎回')
    IS_CHOOSERIGHT = Column(VARCHAR(1), comment='是否有选择权')
    IS_NETPRICE = Column(Numeric(1, 0), comment='是否净价')
    IS_ACT_DAYS = Column(Numeric(1, 0), comment='是否按实际天数计息')
    IS_INCBONDS = Column(Numeric(5, 0), comment='是否增发债')
    ISSUE_OBJECT = Column(VARCHAR(100), comment='发行对象')
    B_INFO_ACTUALBENCHMARK = Column(VARCHAR(8), comment='计息基准')
    REGISTER_FILE_TYPE_CODE = Column(Numeric(9, 0), comment='注册文件类型代码')
    REGISTER_FILE_NUMBER = Column(VARCHAR(1000), comment='注册文件号')
    LIST_ANN_DATE = Column(VARCHAR(8), comment='上市公告日')
    REIMBURSEMENT = Column(VARCHAR(20), comment='偿还方式')
    BOND_RATING = Column(VARCHAR(10), comment='发行时债券评级')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    B_ISSUE_AMOUNT_MAX = Column(Numeric(24, 8), comment='发行金额上限')
    B_INFO_GUARANTEE_ID = Column(VARCHAR(100), comment='担保人ID')
    B_INFO_PINYIN = Column(VARCHAR(40), comment='简称拼音')
    TRADE_TYPE_CODE = Column(Numeric(9, 0), comment='交易方式')
    IS_TAXFREE = Column(VARCHAR(4), comment='是否免税')


class CBONDDESCRIPTIONZL(Base):
    """中国债券基本资料(增量)"""
    __tablename__ = 'CBONDDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_FULLNAME = Column(VARCHAR(100), comment='债券名称')
    B_INFO_ISSUER = Column(VARCHAR(100), comment='发行人')
    B_ISSUE_ANNOUNCEMENT = Column(VARCHAR(8), comment='发行公告日')
    B_ISSUE_FIRSTISSUE = Column(VARCHAR(8), comment='发行起始日')
    B_ISSUE_LASTISSUE = Column(VARCHAR(8), comment='发行截止日')
    B_ISSUE_AMOUNTPLAN = Column(Numeric(20, 4), comment='计划发行总量(亿元)')
    B_ISSUE_AMOUNTACT = Column(Numeric(20, 4), comment='实际发行总量(亿元)')
    B_INFO_ISSUEPRICE = Column(Numeric(20, 4), comment='发行价格')
    B_INFO_PAR = Column(Numeric(20, 0), comment='面值')
    B_INFO_COUPONRATE = Column(Numeric(20, 4), comment='发行票面利率(%)')
    B_INFO_SPREAD = Column(Numeric(20, 4), comment='利差(%)')
    B_INFO_CARRYDATE = Column(VARCHAR(8), comment='计息起始日')
    B_INFO_ENDDATE = Column(VARCHAR(8), comment='计息截止日')
    B_INFO_MATURITYDATE = Column(VARCHAR(8), comment='到期日')
    B_INFO_TERM_YEAR_ = Column(Numeric(20, 4), comment='债券期限(年)')
    B_INFO_TERM_DAY_ = Column(Numeric(20, 4), comment='债券期限(天)')
    B_INFO_PAYMENTDATE = Column(VARCHAR(8), comment='兑付日')
    B_INFO_PAYMENTTYPE = Column(Numeric(9, 0), comment='计息方式')
    B_INFO_INTERESTFREQUENCY = Column(VARCHAR(20), comment='付息频率')
    B_INFO_FORM = Column(VARCHAR(10), comment='债券形式')
    B_INFO_COUPON = Column(Numeric(9, 0), comment='息票品种')
    B_INFO_INTERESTTYPE = Column(Numeric(9, 0), comment='附息利率品种')
    B_INFO_ACT = Column(Numeric(20, 4), comment='特殊年计息天数')
    B_ISSUE_FEE = Column(Numeric(20, 4), comment='发行手续费率(%)')
    B_REDEMPTION_FEERATION = Column(Numeric(20, 4), comment='兑付手续费率(%)')
    B_INFO_TAXRATE = Column(Numeric(20, 4), comment='所得税率')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='债券简称')
    S_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    B_INFO_GUARANTOR = Column(VARCHAR(100), comment='担保人')
    B_INFO_GUARTYPE = Column(Numeric(9, 0), comment='担保方式')
    B_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    B_INFO_YEARSNUMBER = Column(Numeric(20, 0), comment='年内序号')
    S_DIV_RECORDDATE = Column(VARCHAR(8), comment='兑付登记起始日')
    B_INFO_CODEBYPLACING = Column(VARCHAR(10), comment='上网发行认购代码')
    B_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    B_INFO_ISSUETYPE = Column(Numeric(9, 0), comment='发行方式')
    B_INFO_GUARINTRODUCTION = Column(VARCHAR(500), comment='担保简介')
    B_INFO_BGNDBYPLACING = Column(VARCHAR(8), comment='上网发行起始日期')
    B_INFO_ENDDBYPLACING = Column(VARCHAR(8), comment='上网发行截止日期')
    B_INFO_AMOUNTBYPLACING = Column(Numeric(20, 4), comment='上网发行数量(亿元)')
    B_INFO_UNDERWRITINGCODE = Column(Numeric(9, 0), comment='承销方式代码')
    B_INFO_ISSUERCODE = Column(VARCHAR(100), comment='发行人编号')
    B_INFO_FORMERCODE = Column(VARCHAR(40), comment='原债券代码')
    B_INFO_COUPONTXT = Column(VARCHAR(1000), comment='利率说明')
    IS_FAILURE = Column(Numeric(5, 0), comment='是否发行失败')
    IS_CROSSMARKET = Column(Numeric(5, 0), comment='是否跨市场')
    B_INFO_COUPONDATETXT = Column(VARCHAR(1000), comment='付息日说明')
    B_INFO_SUBORDINATEORNOT = Column(Numeric(5, 0), comment='是否次级债或混合资本债')
    B_TENDRST_REFERYIELD = Column(Numeric(20, 4), comment='参考收益率')
    B_INFO_CURPAR = Column(Numeric(20, 4), comment='最新面值')
    S_INFO_FORMERWINDCODE = Column(VARCHAR(40), comment='原Wind代码')
    IS_CORPORATE_BOND = Column(Numeric(5, 0), comment='是否公司债')
    B_INFO_ISSUERTYPE = Column(VARCHAR(40), comment='发行人类型')
    B_INFO_SPECIALBONDTYPE = Column(VARCHAR(40), comment='特殊债券类型')
    IS_PAYADVANCED = Column(VARCHAR(1), comment='是否可提前兑付')
    IS_CALLABLE = Column(VARCHAR(1), comment='是否可赎回')
    IS_CHOOSERIGHT = Column(VARCHAR(1), comment='是否有选择权')
    IS_NETPRICE = Column(Numeric(1, 0), comment='是否净价')
    IS_ACT_DAYS = Column(Numeric(1, 0), comment='是否按实际天数计息')
    IS_INCBONDS = Column(Numeric(5, 0), comment='是否增发债')
    ISSUE_OBJECT = Column(VARCHAR(100), comment='发行对象')
    B_INFO_ACTUALBENCHMARK = Column(VARCHAR(8), comment='计息基准')
    REGISTER_FILE_TYPE_CODE = Column(Numeric(9, 0), comment='注册文件类型代码')
    REGISTER_FILE_NUMBER = Column(VARCHAR(1000), comment='注册文件号')
    LIST_ANN_DATE = Column(VARCHAR(8), comment='上市公告日')
    REIMBURSEMENT = Column(VARCHAR(20), comment='偿还方式')
    BOND_RATING = Column(VARCHAR(10), comment='发行时债券评级')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    B_ISSUE_AMOUNT_MAX = Column(Numeric(24, 8), comment='发行金额上限')
    B_INFO_GUARANTEE_ID = Column(VARCHAR(100), comment='担保人ID')


class CBONDDEVALUATIONPREPARATION(Base):
    """中国债券发行主体资产减值准备明细表"""
    __tablename__ = 'CBONDDEVALUATIONPREPARATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_DEVELOPMENT_COST = Column(Numeric(15, 2), comment='开发成本')
    S_LOW_VALUE_CONSUMABLES = Column(Numeric(15, 2), comment='低值易耗品')
    S_FINISHED_PRODUCT = Column(Numeric(15, 2), comment='产成品')
    S_OFFICE_EQUIPMENT = Column(Numeric(15, 2), comment='办公及其他设备')
    S_OTHER_EQUIPMENT = Column(Numeric(15, 2), comment='其他设备')
    S_LAND_USE_RIGHT = Column(Numeric(15, 2), comment='土地使用权')
    S_MATERIALS_IN_TRANSIT = Column(Numeric(15, 2), comment='在途物资')
    S_IN_PRODUCT = Column(Numeric(15, 2), comment='在产品')
    S_DEVELOPING_PRODUCTS = Column(Numeric(15, 2), comment='开发产品')
    S_PART_PREPARED_PRODUCTS = Column(Numeric(15, 2), comment='自制半成品')
    S_RIGHT_USE_HOUSING = Column(Numeric(15, 2), comment='职工住房使用权')
    S_PACKAGING = Column(Numeric(15, 2), comment='包装物')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    STATEMENT_TYPE_CODE = Column(Numeric(9, 0), comment='报表类型代码')
    S_BAD_DEBT_TOT = Column(Numeric(20, 4), comment='坏账准备合计')
    S_ACCT_RCV = Column(Numeric(20, 4), comment='应收账款')
    S_OTH_RCV = Column(Numeric(20, 4), comment='其他应收款')
    S_SHORT_TERM_INV_FALL = Column(Numeric(20, 4), comment='短期投资跌价准备合计')
    S_STOCK_INVESTMENT = Column(Numeric(20, 4), comment='股票投资')
    S_BOND_INVESTMENT = Column(Numeric(20, 4), comment='债券投资')
    S_STOCK_PRICE_DROP1 = Column(Numeric(20, 4), comment='存货跌价准备合计')
    S_INVENTORY_GOODS = Column(Numeric(20, 4), comment='库存商品')
    S_RAW_MATERIAL = Column(Numeric(20, 4), comment='原材料')
    S_LONG_INV_DEPRE_RES_TOT = Column(Numeric(20, 4), comment='长期投资减值准备合计')
    S_EQUITY_INVESTMENT = Column(Numeric(20, 4), comment='长期股权投资减值准备')
    S_LONG_DEBT_INVESTMENTS = Column(Numeric(20, 4), comment='长期债权投资')
    S_FIXED_ASSET_IMPAIRMENT = Column(Numeric(20, 4), comment='固定资产减值准备')
    S_BUILDING1 = Column(Numeric(20, 4), comment='房屋、建筑物')
    S_MACHINERY = Column(Numeric(20, 4), comment='机器设备')
    S_INTANGIBLE_ASSETS_DEVALUE = Column(Numeric(20, 4), comment='无形资产减值准备')
    S_PATENT_RIGHT = Column(Numeric(20, 4), comment='专利权')
    S_TRADEMARK_RIGHT = Column(Numeric(20, 4), comment='商标权')
    S_CON_PROJECT_DEVALUE = Column(Numeric(20, 4), comment='在建工程减值准备')
    S_LOAN_MANDATE_DEVALUE = Column(Numeric(20, 4), comment='委托贷款减值准备')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_SPECIAL_EQUIPMENT = Column(Numeric(20, 4), comment='专用设备')
    S_CONVEYANCE = Column(Numeric(20, 4), comment='运输工具')
    S_COMMUNICATION = Column(Numeric(20, 4), comment='通讯设备')
    S_ELECTRONIC = Column(Numeric(20, 4), comment='电子设备')
    S_STOCK_PRICE_DROP = Column(Numeric(20, 4), comment='自营证券跌价准备')
    S_PRE_BAD_LOANS = Column(Numeric(20, 4), comment='贷款呆账准备')
    S_TURNOVER = Column(Numeric(20, 4), comment='周转材料')
    S_EXPEND_ASSETS = Column(Numeric(20, 4), comment='消耗性生物资产')
    S_SELL_FINANCIAL_ASSETS = Column(Numeric(20, 4), comment='可供出售金融资产减值准备')
    S_HOLD_EXPIRY_INVESTMENT = Column(Numeric(20, 4), comment='持有至到期投资减值准备')
    S_BUILDING = Column(Numeric(20, 4), comment='房屋、建筑物')
    S_INVESTMENT_REAL_ESTATE = Column(Numeric(20, 4), comment='投资性房地产减值准备')
    S_LAND_USE_RIGHT1 = Column(Numeric(20, 4), comment='土地使用权')
    S_MATERIAL_DEVALUE = Column(Numeric(20, 4), comment='工程物资减值准备')
    S_BIOLOGICAL_ASSETS_DEVALUE = Column(Numeric(20, 4), comment='生产性生物资产减值准备')
    S_BIOLOGICAL_ASSETS_DEVALUE1 = Column(Numeric(20, 4), comment='成熟生产性生物资产减值准备')
    S_OIL_GAS_ASSETS_DEVALUE = Column(Numeric(20, 4), comment='油气资产减值准备')
    S_GOODWILL_DEVALUE = Column(Numeric(20, 4), comment='商誉减值准备')
    S_OTHER = Column(Numeric(20, 4), comment='其他')
    S_LOAN_LOSS_PREPARATION = Column(Numeric(20, 4), comment='贷款损失准备')
    S_INTERBANK_PAYMENTS_DEVALUE = Column(Numeric(20, 4), comment='存放同业款项减值准备')
    S_DEMOLITION_CAPITAL_DEVALUE = Column(Numeric(20, 4), comment='拆出资金减值准备')
    S_DEBT_SET_DEVALUE = Column(Numeric(20, 4), comment='抵债资产减值准备')
    S_BACK_SALE_FINANCIAL_ASSETS = Column(Numeric(20, 4), comment='买入返售金融资产减值准备')
    S_NOBLE_METAL_DEPRECIATION = Column(Numeric(20, 4), comment='贵金属跌价准备')
    S_TREATED_ASSETS_DEVALUE = Column(Numeric(20, 4), comment='待处理资产减值准备')
    S_INTEREST_RECEIVABLE_DEVALUE = Column(Numeric(20, 4), comment='应收利息减值准备')
    S_OTHER_ASSETS_DEVALUE = Column(Numeric(20, 4), comment='其他资产减值准备')


class CBONDDIRECTOR(Base):
    """中国债券公司董事成员"""
    __tablename__ = 'CBONDDIRECTOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='职务')


class CBONDEODPRICES(Base):
    """中国债券债券行情(沪深交易所)"""
    __tablename__ = 'CBONDEODPRICES'
    __table_args__ = (
        Index('idx_CBONDEODPRICES_01', 'S_INFO_WINDCODE', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价(元)')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(元)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(元)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(元)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(元)')
    S_DQ_CHANGE = Column(Numeric(20, 4), comment='涨跌(元)')
    S_DQ_PCTCHANGE = Column(Numeric(20, 4), comment='涨跌幅(%)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    S_DQ_AVGPRICE = Column(Numeric(20, 4), comment='均价(VWAP)')
    S_DQ_TRADESTATUS = Column(VARCHAR(10), comment='交易状态')


class CBONDEQUITYRELATIONSHIPS(Base):
    """中国债券发行主体实际控制人"""
    __tablename__ = 'CBONDEQUITYRELATIONSHIPS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    RELATION_TYPE = Column(VARCHAR(40), comment='公司与披露方关系')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    S_HOLDER_CODE = Column(VARCHAR(10), comment='股东ID')
    S_HOLDER_TYPE = Column(Numeric(5, 0), comment='股东类型')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例(%)')
    IS_ACTUALCONTROLLER = Column(Numeric(5, 0), comment='股东是否为实际控制人')
    ACTUALCONTROLLER_TYPE = Column(VARCHAR(80), comment='实际控制人类型')
    ACTUALCONTROLLER_IS_ANN = Column(Numeric(5, 0), comment='股东是否为公布实际控制人')
    ACTUALCONTROLLER_INTRO = Column(VARCHAR(1000), comment='实际控制人简介')


class CBONDEREPAYPRINCIPAL(Base):
    """中国债券本金提前偿还明细"""
    __tablename__ = 'CBONDEREPAYPRINCIPAL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REPAYPRIDT = Column(VARCHAR(8), comment='本金偿还日期')
    B_INFO_REPAYPRIRATE = Column(Numeric(20, 4), comment='本金偿还比例')
    B_INFO_EREPAYTPE = Column(Numeric(1, 0), comment='提前还本方式代码')


class CBONDESTIMATEISSUEAMOUNT(Base):
    """中国银行间债券预计发行总量"""
    __tablename__ = 'CBONDESTIMATEISSUEAMOUNT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    ISSUE_FIRSTISSUE = Column(VARCHAR(8), comment='发行日期')
    BOND_TYPE = Column(VARCHAR(40), comment='债券类型')
    ISSUE_AMOUNTPLAN = Column(Numeric(20, 4), comment='发行数量(亿元)')
    TERM_YEAR = Column(Numeric(20, 4), comment='债券期限(年)')
    INTERESTTYPE = Column(VARCHAR(100), comment='利率类型')
    INTERESTFREQUENCY = Column(VARCHAR(100), comment='付息频率')
    ISSER_INTRODUCE = Column(VARCHAR(200), comment='发行简介')
    SPECIALBONDTYPE = Column(Numeric(9, 0), comment='债券品种代码')
    INTERESTTYPE_CODE = Column(Numeric(9, 0), comment='附息利率品种代码')
    REIMBURSEMENT = Column(Numeric(9, 0), comment='偿还方式代码')


class CBONDEVENTDATEINFORMATION(Base):
    """中国债券事件日期信息"""
    __tablename__ = 'CBONDEVENTDATEINFORMATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EVENT_TYPE = Column(Numeric(8, 0), comment='事件类型编号')
    OCCURRENCE_DATE = Column(VARCHAR(8), comment='发生日期')
    DISCLOSURE_DATE = Column(VARCHAR(8), comment='披露日期')
    MEMO = Column(VARCHAR(2000), comment='内容说明')
    DATE_CREATED = Column(VARCHAR(8), comment='创建日期')
    S_INFO_CODE = Column(VARCHAR(20), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    TYPE_CODE = Column(VARCHAR(10), comment='证券类型代码')
    LANGUAGE1 = Column(VARCHAR(10), comment='语言')
    EQY_RECORD_DT = Column(VARCHAR(8), comment='权益登记日')


class CBONDFCTD(Base):
    """中国国债期货最便宜可交割券"""
    __tablename__ = 'CBONDFCTD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CTD_WINDCODE = Column(VARCHAR(40), comment='CTD证券Wind代码')
    CTD_IRR = Column(Numeric(20, 4), comment='IRR')
    IB_CTD_WINDCODE = Column(VARCHAR(40), comment='银行间CTD证券Wind代码')
    IB_CTD_IRR = Column(Numeric(20, 4), comment='银行间IRR')
    SH_CTD_WINDCODE = Column(VARCHAR(40), comment='沪市CTD证券Wind代码')
    SH_CTD_IRR = Column(Numeric(20, 4), comment='沪市IRR')
    SZ_CTD_WINDCODE = Column(VARCHAR(40), comment='深市CTD证券Wind代码')
    SZ_CTD_IRR = Column(Numeric(20, 4), comment='深市IRR')


class CBONDFINANCIALACCOUNTS(Base):
    """中国债券财务科目与附注对应表"""
    __tablename__ = 'CBONDFINANCIALACCOUNTS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    SUBJECT_CHINESE_NAME = Column(VARCHAR(100), comment='科目中文名')
    CLASSIFICATION_NUMBER = Column(VARCHAR(10), comment='分类序号')
    S_INFO_DATATYPE = Column(VARCHAR(40), comment='数据类型')
    ANN_ITEM = Column(VARCHAR(100), comment='项目公布名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='项目金额')
    ITEM_NAME = Column(VARCHAR(100), comment='项目容错名称')


class CBONDFINANCIALEXPENSE(Base):
    """中国债券发行主体财务费用明细"""
    __tablename__ = 'CBONDFINANCIALEXPENSE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPECODE = Column(Numeric(9, 0), comment='报表类型代码')
    S_STMNOTE_INTEXP = Column(Numeric(20, 4), comment='利息支出')
    S_STMNOTE_INTINC = Column(Numeric(20, 4), comment='减：利息收入')
    S_STMNOTE_EXCH = Column(Numeric(20, 4), comment='汇兑损益')
    S_STMNOTE_FEE = Column(Numeric(20, 4), comment='手续费')
    S_STMNOTE_OTHERS = Column(Numeric(20, 4), comment='其他')
    S_STMNOTE_FINEXP = Column(Numeric(20, 4), comment='合计')
    S_STMNOTE_FINEXP_1 = Column(Numeric(20, 4), comment='利息资本化金额')


class CBONDFINANCIALINDICATOR(Base):
    """中国债券发行主体财务指标"""
    __tablename__ = 'CBONDFINANCIALINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_FA_EXTRAORDINARY = Column(Numeric(20, 4), comment='非经常性损益')
    S_FA_DEDUCTEDPROFIT = Column(Numeric(20, 4), comment='扣除非经常性损益后的净利润')
    S_FA_GROSSMARGIN = Column(Numeric(20, 4), comment='毛利')
    S_FA_OPERATEINCOME = Column(Numeric(20, 4), comment='经营活动净收益')
    S_FA_INVESTINCOME = Column(Numeric(20, 4), comment='价值变动净收益')
    S_STMNOTE_FINEXP = Column(Numeric(20, 4), comment='利息费用')
    S_STM_IS = Column(Numeric(20, 4), comment='折旧与摊销')
    S_FA_EBIT = Column(Numeric(20, 4), comment='息税前利润')
    S_FA_EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    S_FA_FCFF = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)')
    S_FA_FCFE = Column(Numeric(20, 4), comment='股权自由现金流量(FCFE)')
    S_FA_EXINTERESTDEBT_CURRENT = Column(Numeric(20, 4), comment='无息流动负债')
    S_FA_EXINTERESTDEBT_NONCURRENT = Column(Numeric(20, 4), comment='无息非流动负债')
    S_FA_INTERESTDEBT = Column(Numeric(20, 4), comment='带息债务')
    S_FA_NETDEBT = Column(Numeric(20, 4), comment='净债务')
    S_FA_TANGIBLEASSET = Column(Numeric(20, 4), comment='有形资产')
    S_FA_WORKINGCAPITAL = Column(Numeric(20, 4), comment='营运资金')
    S_FA_NETWORKINGCAPITAL = Column(Numeric(20, 4), comment='营运流动资本')
    S_FA_INVESTCAPITAL = Column(Numeric(20, 4), comment='全部投入资本')
    S_FA_RETAINEDEARNINGS = Column(Numeric(20, 4), comment='留存收益')
    S_FA_EPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益')
    S_FA_EPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益')
    S_FA_EPS_DILUTED2 = Column(Numeric(20, 4), comment='期末摊薄每股收益')
    S_FA_BPS = Column(Numeric(20, 4), comment='每股净资产')
    S_FA_OCFPS = Column(Numeric(20, 4), comment='每股经营活动产生的现金流量净额')
    S_FA_GRPS = Column(Numeric(20, 4), comment='每股营业总收入')
    S_FA_ORPS = Column(Numeric(20, 4), comment='每股营业收入')
    S_FA_SURPLUSCAPITALPS = Column(Numeric(20, 4), comment='每股资本公积')
    S_FA_SURPLUSRESERVEPS = Column(Numeric(20, 4), comment='每股盈余公积')
    S_FA_UNDISTRIBUTEDPS = Column(Numeric(20, 4), comment='每股未分配利润')
    S_FA_RETAINEDPS = Column(Numeric(20, 4), comment='每股留存收益')
    S_FA_CFPS = Column(Numeric(20, 4), comment='每股现金流量净额')
    S_FA_EBITPS = Column(Numeric(20, 4), comment='每股息税前利润')
    S_FA_FCFFPS = Column(Numeric(20, 4), comment='每股企业自由现金流量')
    S_FA_FCFEPS = Column(Numeric(20, 4), comment='每股股东自由现金流量')
    S_FA_NETPROFITMARGIN = Column(Numeric(20, 4), comment='销售净利率')
    S_FA_GROSSPROFITMARGIN = Column(Numeric(20, 4), comment='销售毛利率')
    S_FA_COGSTOSALES = Column(Numeric(20, 4), comment='销售成本率')
    S_FA_EXPENSETOSALES = Column(Numeric(20, 4), comment='销售期间费用率')
    S_FA_PROFITTOGR = Column(Numeric(20, 4), comment='净利润/营业总收入')
    S_FA_SALEEXPENSETOGR = Column(Numeric(20, 4), comment='销售费用/营业总收入')
    S_FA_ADMINEXPENSETOGR = Column(Numeric(20, 4), comment='管理费用/营业总收入')
    S_FA_FINAEXPENSETOGR = Column(Numeric(20, 4), comment='财务费用/营业总收入')
    S_FA_IMPAIRTOGR_TTM = Column(Numeric(20, 4), comment='资产减值损失/营业总收入')
    S_FA_GCTOGR = Column(Numeric(20, 4), comment='营业总成本/营业总收入')
    S_FA_OPTOGR = Column(Numeric(20, 4), comment='营业利润/营业总收入')
    S_FA_EBITTOGR = Column(Numeric(20, 4), comment='息税前利润/营业总收入')
    S_FA_ROE = Column(Numeric(20, 4), comment='净资产收益率')
    S_FA_ROE_DEDUCTED = Column(Numeric(20, 4), comment='净资产收益率(扣除非经常损益)')
    S_FA_ROA2 = Column(Numeric(20, 4), comment='总资产报酬率')
    S_FA_ROA = Column(Numeric(20, 4), comment='总资产净利润')
    S_FA_ROIC = Column(Numeric(20, 4), comment='投入资本回报率')
    S_FA_ROE_YEARLY = Column(Numeric(20, 4), comment='年化净资产收益率')
    S_FA_ROA2_YEARLY = Column(Numeric(20, 4), comment='年化总资产报酬率')
    S_FA_ROE_AVG = Column(Numeric(20, 4), comment='平均净资产收益率(增发条件)')
    S_FA_OPERATEINCOMETOEBT = Column(Numeric(20, 4), comment='经营活动净收益/利润总额')
    S_FA_INVESTINCOMETOEBT = Column(Numeric(20, 4), comment='价值变动净收益/利润总额')
    S_FA_NONOPERATEPROFITTOEBT = Column(Numeric(20, 4), comment='营业外收支净额/利润总额')
    S_FA_TAXTOEBT = Column(Numeric(20, 4), comment='所得税/利润总额')
    S_FA_DEDUCTEDPROFITTOPROFIT = Column(Numeric(20, 4), comment='扣除非经常损益后的净利润/净利润')
    S_FA_SALESCASHINTOOR = Column(Numeric(20, 4), comment='销售商品提供劳务收到的现金/营业收入')
    S_FA_OCFTOOR = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/营业收入')
    S_FA_OCFTOOPERATEINCOME = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/经营活动净收益')
    S_FA_CAPITALIZEDTODA = Column(Numeric(20, 4), comment='资本支出/折旧和摊销')
    S_FA_DEBTTOASSETS = Column(Numeric(20, 4), comment='资产负债率')
    S_FA_ASSETSTOEQUITY = Column(Numeric(20, 4), comment='权益乘数')
    S_FA_DUPONT_ASSETSTOEQUITY = Column(Numeric(20, 4), comment='权益乘数(用于杜邦分析)')
    S_FA_CATOASSETS = Column(Numeric(20, 4), comment='流动资产/总资产')
    S_FA_NCATOASSETS = Column(Numeric(20, 4), comment='非流动资产/总资产')
    S_FA_TANGIBLEASSETSTOASSETS = Column(Numeric(20, 4), comment='有形资产/总资产')
    S_FA_INTDEBTTOTOTALCAP = Column(Numeric(20, 4), comment='带息债务/全部投入资本')
    S_FA_EQUITYTOTOTALCAPITAL = Column(Numeric(20, 4), comment='归属于母公司的股东权益/全部投入资本')
    S_FA_CURRENTDEBTTODEBT = Column(Numeric(20, 4), comment='流动负债/负债合计')
    S_FA_LONGDEBTODEBT = Column(Numeric(20, 4), comment='非流动负债/负债合计')
    S_FA_CURRENT = Column(Numeric(20, 4), comment='流动比率')
    S_FA_QUICK = Column(Numeric(20, 4), comment='速动比率')
    S_FA_CASHRATIO = Column(Numeric(20, 4), comment='保守速动比率')
    S_FA_OCFTOSHORTDEBT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/流动负债')
    S_FA_DEBTTOEQUITY = Column(Numeric(20, 4), comment='产权比率')
    S_FA_EQUITYTODEBT = Column(Numeric(20, 4), comment='归属于母公司的股东权益/负债合计')
    S_FA_EQUITYTOINTERESTDEBT = Column(Numeric(20, 4), comment='归属于母公司的股东权益/带息债务')
    S_FA_TANGIBLEASSETTODEBT = Column(Numeric(20, 4), comment='有形资产/负债合计')
    S_FA_TANGASSETTOINTDEBT = Column(Numeric(20, 4), comment='有形资产/带息债务')
    S_FA_TANGIBLEASSETTONETDEBT = Column(Numeric(20, 4), comment='有形资产/净债务')
    S_FA_OCFTODEBT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/负债合计')
    S_FA_OCFTOINTERESTDEBT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/带息债务')
    S_FA_OCFTONETDEBT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/净债务')
    S_FA_EBITTOINTEREST = Column(Numeric(20, 4), comment='已获利息倍数(EBIT/利息费用)')
    S_FA_LONGDEBTTOWORKINGCAPITAL = Column(Numeric(20, 4), comment='长期债务与营运资金比率')
    S_FA_EBITDATODEBT = Column(Numeric(20, 4), comment='息税折旧摊销前利润/负债合计')
    S_FA_TURNDAYS = Column(Numeric(20, 4), comment='营业周期')
    S_FA_INVTURNDAYS = Column(Numeric(20, 4), comment='存货周转天数')
    S_FA_ARTURNDAYS = Column(Numeric(20, 4), comment='应收账款周转天数')
    S_FA_INVTURN = Column(Numeric(20, 4), comment='存货周转率')
    S_FA_ARTURN = Column(Numeric(20, 4), comment='应收账款周转率')
    S_FA_CATURN = Column(Numeric(20, 4), comment='流动资产周转率')
    S_FA_FATURN = Column(Numeric(20, 4), comment='固定资产周转率')
    S_FA_ASSETSTURN = Column(Numeric(20, 4), comment='总资产周转率')
    S_FA_ROA_YEARLY = Column(Numeric(20, 4), comment='年化总资产净利率')
    S_FA_DUPONT_ROA = Column(Numeric(20, 4), comment='总资产净利率(杜邦分析)')
    S_STM_BS = Column(Numeric(20, 4), comment='固定资产合计')
    S_FA_PREFINEXPENSE_OPPROFIT = Column(Numeric(20, 4), comment='扣除财务费用前营业利润')
    S_FA_NONOPPROFIT = Column(Numeric(20, 4), comment='非营业利润')
    S_FA_OPTOEBT = Column(Numeric(20, 4), comment='营业利润／利润总额')
    S_FA_NOPTOEBT = Column(Numeric(20, 4), comment='非营业利润／利润总额')
    S_FA_OCFTOPROFIT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／营业利润')
    S_FA_CASHTOLIQDEBT = Column(Numeric(20, 4), comment='货币资金／流动负债')
    S_FA_CASHTOLIQDEBTWITHINTEREST = Column(Numeric(20, 4), comment='货币资金／带息流动负债')
    S_FA_OPTOLIQDEBT = Column(Numeric(20, 4), comment='营业利润／流动负债')
    S_FA_OPTODEBT = Column(Numeric(20, 4), comment='营业利润／负债合计')
    S_FA_ROIC_YEARLY = Column(Numeric(20, 4), comment='年化投入资本回报率')
    S_FA_TOT_FATURN = Column(Numeric(20, 4), comment='固定资产合计周转率')
    S_FA_PROFITTOOP = Column(Numeric(20, 4), comment='利润总额／营业收入')
    S_QFA_OPERATEINCOME = Column(Numeric(20, 4), comment='单季度.经营活动净收益')
    S_QFA_INVESTINCOME = Column(Numeric(20, 4), comment='单季度.价值变动净收益')
    S_QFA_DEDUCTEDPROFIT = Column(Numeric(20, 4), comment='单季度.扣除非经常损益后的净利润')
    S_QFA_EPS = Column(Numeric(20, 4), comment='单季度.每股收益')
    S_QFA_NETPROFITMARGIN = Column(Numeric(20, 4), comment='单季度.销售净利率')
    S_QFA_GROSSPROFITMARGIN = Column(Numeric(20, 4), comment='单季度.销售毛利率')
    S_QFA_EXPENSETOSALES = Column(Numeric(20, 4), comment='单季度.销售期间费用率')
    S_QFA_PROFITTOGR = Column(Numeric(20, 4), comment='单季度.净利润／营业总收入')
    S_QFA_SALEEXPENSETOGR = Column(Numeric(20, 4), comment='单季度.销售费用／营业总收入')
    S_QFA_ADMINEXPENSETOGR = Column(Numeric(20, 4), comment='单季度.管理费用／营业总收入')
    S_QFA_FINAEXPENSETOGR = Column(Numeric(20, 4), comment='单季度.财务费用／营业总收入')
    S_QFA_IMPAIRTOGR_TTM = Column(Numeric(20, 4), comment='单季度.资产减值损失／营业总收入')
    S_QFA_GCTOGR = Column(Numeric(20, 4), comment='单季度.营业总成本／营业总收入')
    S_QFA_OPTOGR = Column(Numeric(20, 4), comment='单季度.营业利润／营业总收入')
    S_QFA_ROE = Column(Numeric(20, 4), comment='单季度.净资产收益率')
    S_QFA_ROE_DEDUCTED = Column(Numeric(20, 4), comment='单季度.净资产收益率(扣除非经常损益)')
    S_QFA_ROA = Column(Numeric(20, 4), comment='单季度.总资产净利润')
    S_QFA_OPERATEINCOMETOEBT = Column(Numeric(20, 4), comment='单季度.经营活动净收益／利润总额')
    S_QFA_INVESTINCOMETOEBT = Column(Numeric(20, 4), comment='单季度.价值变动净收益／利润总额')
    S_QFA_DEDUCTEDPROFITTOPROFIT = Column(Numeric(20, 4), comment='单季度.扣除非经常损益后的净利润／净利润')
    S_QFA_SALESCASHINTOOR = Column(Numeric(20, 4), comment='单季度.销售商品提供劳务收到的现金／营业收入')
    S_QFA_OCFTOSALES = Column(Numeric(20, 4), comment='单季度.经营活动产生的现金流量净额／营业收入')
    S_QFA_OCFTOOR = Column(Numeric(20, 4), comment='单季度.经营活动产生的现金流量净额／经营活动净收益')
    S_FA_YOYEPS_BASIC = Column(Numeric(20, 4), comment='同比增长率-基本每股收益(%)')
    S_FA_YOYEPS_DILUTED = Column(Numeric(20, 4), comment='同比增长率-稀释每股收益(%)')
    S_FA_YOYOCFPS = Column(Numeric(20, 4), comment='同比增长率-每股经营活动产生的现金流量净额(%)')
    S_FA_YOYOP = Column(Numeric(20, 4), comment='同比增长率-营业利润(%)')
    S_FA_YOYEBT = Column(Numeric(20, 4), comment='同比增长率-利润总额(%)')
    S_FA_YOYNETPROFIT = Column(Numeric(20, 4), comment='同比增长率-归属母公司股东的净利润(%)')
    S_FA_YOYNETPROFIT_DEDUCTED = Column(Numeric(20, 4), comment='同比增长率-归属母公司股东的净利润-扣除非经常损益(%)')
    S_FA_YOYOCF = Column(Numeric(20, 4), comment='同比增长率-经营活动产生的现金流量净额(%)')
    S_FA_YOYROE = Column(Numeric(20, 4), comment='同比增长率-净资产收益率(摊薄)(%)')
    S_FA_YOYBPS = Column(Numeric(20, 4), comment='相对年初增长率-每股净资产(%)')
    S_FA_YOYASSETS = Column(Numeric(20, 4), comment='相对年初增长率-资产总计(%)')
    S_FA_YOYEQUITY = Column(Numeric(20, 4), comment='相对年初增长率-归属母公司的股东权益(%)')
    S_FA_YOY_TR = Column(Numeric(20, 4), comment='营业总收入同比增长率(%)')
    S_FA_YOY_OR = Column(Numeric(20, 4), comment='营业收入同比增长率(%)')
    S_QFA_YOYGR = Column(Numeric(20, 4), comment='单季度.营业总收入同比增长率(%)')
    S_QFA_CGRGR = Column(Numeric(20, 4), comment='单季度.营业总收入环比增长率(%)')
    S_QFA_YOYSALES = Column(Numeric(20, 4), comment='单季度.营业收入同比增长率(%)')
    S_QFA_CGRSALES = Column(Numeric(20, 4), comment='单季度.营业收入环比增长率(%)')
    S_QFA_YOYOP = Column(Numeric(20, 4), comment='单季度.营业利润同比增长率(%)')
    S_QFA_CGROP = Column(Numeric(20, 4), comment='单季度.营业利润环比增长率(%)')
    S_QFA_YOYPROFIT = Column(Numeric(20, 4), comment='单季度.净利润同比增长率(%)')
    S_QFA_CGRPROFIT = Column(Numeric(20, 4), comment='单季度.净利润环比增长率(%)')
    S_QFA_YOYNETPROFIT = Column(Numeric(20, 4), comment='单季度.归属母公司股东的净利润同比增长率(%)')
    S_QFA_CGRNETPROFIT = Column(Numeric(20, 4), comment='单季度.归属母公司股东的净利润环比增长率(%)')
    S_FA_YOY_EQUITY = Column(Numeric(20, 4), comment='净资产(同比增长率)')
    RD_EXPENSE = Column(Numeric(20, 4), comment='研发费用')


class CBONDFINNOTESDETAIL(Base):
    """中国债券发行主体财务附注明细"""
    __tablename__ = 'CBONDFINNOTESDETAIL'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    BD_LOSS = Column(Numeric(20, 4), comment='坏账损失')
    INV_LOSS = Column(Numeric(20, 4), comment='存货跌价损失')
    GI_LOSS = Column(Numeric(20, 4), comment='商誉减值损失')
    GC_LOSS = Column(Numeric(20, 4), comment='发放贷款和垫款减值损失')
    AFA_LOSS = Column(Numeric(20, 4), comment='可供出售金融资产减值损失')
    HI_LOSS = Column(Numeric(20, 4), comment='持有至到期投资减值损失')
    OTH_LOSS = Column(Numeric(20, 4), comment='其他金融资产减值损失')
    LTI_INVINC = Column(Numeric(20, 4), comment='处置长期股权投资产生的投资收益')
    FAT_INVINC = Column(Numeric(20, 4), comment='处置交易性金融资产取得的投资收益')
    AFA_INVINC = Column(Numeric(20, 4), comment='处置可供出售金融资产取得的投资收益')
    PAEI_INVINC = Column(Numeric(20, 4), comment='委托投资损益')
    FEL_INVINC = Column(Numeric(20, 4), comment='对外委托贷款取得的收益')
    CFEO_INVINC = Column(Numeric(20, 4), comment='受托经营取得的托管费收入')
    OTHN_INVINC = Column(Numeric(20, 4), comment='其他非经常性投资收益')
    LTI_COST = Column(Numeric(20, 4), comment='成本法核算的长期股权投资收益')
    LUR_ORIVAL = Column(Numeric(20, 4), comment='土地使用权-原值')
    LUR_ACCA = Column(Numeric(20, 4), comment='土地使用权-累计摊销')
    LUR_IMP = Column(Numeric(20, 4), comment='土地使用权-减值准备')
    LUR_BOOKVAL = Column(Numeric(20, 4), comment='土地使用权-账面价值')
    LTI_EQU = Column(Numeric(20, 4), comment='权益法核算的长期股权投资')
    MONF_RES = Column(Numeric(20, 4), comment='受限制的货币资金')
    SAL_COS = Column(Numeric(20, 4), comment='工资薪酬(销售费用)')
    SAL_GEX = Column(Numeric(20, 4), comment='工资薪酬(管理费用)')
    DA_COS = Column(Numeric(20, 4), comment='折旧摊销(销售费用)')
    DA_GEX = Column(Numeric(20, 4), comment='折旧摊销(管理费用)')
    REN_COS = Column(Numeric(20, 4), comment='租赁费(销售费用)')
    REN_GEX = Column(Numeric(20, 4), comment='租赁费(管理费用)')
    STC_COS = Column(Numeric(20, 4), comment='仓储运输费(销售费用)')
    APE_COS = Column(Numeric(20, 4), comment='广告宣传推广费(销售费用)')
    LTLOAN_1Y = Column(Numeric(20, 4), comment='1年内到期的长期借款')
    BONDPAY_1Y = Column(Numeric(20, 4), comment='1年内到期的应付债券')
    STFINBOND = Column(Numeric(20, 4), comment='短期融资债(其他流动负债)')


class CBONDFLOATINGRATE(Base):
    """中国债券浮息债基础利率属性"""
    __tablename__ = 'CBONDFLOATINGRATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_BENCHMARKCODE = Column(Numeric(9, 0), comment='基准利率代码')
    B_INFO_MARKETRATEORNOT = Column(Numeric(5, 0), comment='基准利率是否是市场化利率')
    B_INFO_INTERESTCODE = Column(VARCHAR(20), comment='市场化利率代码')
    B_INFO_INTERESTFLOOR = Column(Numeric(20, 4), comment='保底利率(%)')
    B_INFO_PAYMENTDAYTYPE = Column(VARCHAR(2), comment='计算基准利率所用付息日类型')
    B_INFO_INTERESTPRECI = Column(Numeric(1, 0), comment='基准利率精度')
    BENCHMARK_DT = Column(VARCHAR(1100), comment='基准利率确定日说明')
    INTEREST_CONTENT = Column(VARCHAR(100), comment='票面利率说明')
    BENCHMARKCODE_PERIOD = Column(VARCHAR(40), comment='基准利率期限 ')
    LIBOR_CRNCY_CODE = Column(VARCHAR(10), comment='LIBOR货币代码 ')
    PRC_DTRMNTN_DATE = Column(VARCHAR(8), comment='首个定价日 ')
    B_INFO_BENCHMARK = Column(VARCHAR(10), comment='存贷款利率代码')


class CBONDFLOWCOEFFICIENTCNBD(Base):
    """中债债券流动性系数"""
    __tablename__ = 'CBONDFLOWCOEFFICIENTCNBD'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='流通场所')
    S_FLOWCOEFFICIENT = Column(Numeric(20, 4), comment='绝对流动性系数')
    S_POSITION_PERCENTAGE = Column(Numeric(20, 4), comment='位置百分比')
    S_FLOWCOEFFICIENT_RELATIVE = Column(Numeric(20, 4), comment='相对流动性系数')
    S_FLOW_VALUE = Column(Numeric(20, 4), comment='相对流动性取值')


class CBONDFORWARDMARKETN(Base):
    """中国债券远期交易行情(银行间)"""
    __tablename__ = 'CBONDFORWARDMARKETN'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TERM_VARIETY = Column(VARCHAR(80), comment='远期期限品种')
    LAST_CP_NET = Column(Numeric(20, 4), comment='前收盘净价')
    LAST_WP_NET = Column(Numeric(20, 4), comment='前加权净价')
    OP_NET = Column(Numeric(20, 4), comment='开盘净价')
    NP_NEW = Column(Numeric(20, 4), comment='最新净价')
    NP_HIGH = Column(Numeric(20, 4), comment='最高净价')
    NP_LOW = Column(Numeric(20, 4), comment='最低净价')
    CP_NET = Column(Numeric(20, 4), comment='收盘净价')
    WP_NET = Column(Numeric(20, 4), comment='加权净价')
    NOMINAL_AMOUNT = Column(Numeric(20, 4), comment='券面总额(万元)')
    RETURN_LC = Column(Numeric(20, 4), comment='前收盘收益率(%)')
    RETURN_LW = Column(Numeric(20, 4), comment='前加权收益率(%)')
    RETURN_OPEN = Column(Numeric(20, 4), comment='开盘收益率(%)')
    RETURN_NEW = Column(Numeric(20, 4), comment='最新收益率(%)')
    RETURN_HIGH = Column(Numeric(20, 4), comment='最高收益率(%)')
    RETURN_LOW = Column(Numeric(20, 4), comment='最低收益率(%)')
    RETURN_CLOSE = Column(Numeric(20, 4), comment='收盘收益率(%)')
    RETURN_WEIGHT = Column(Numeric(20, 4), comment='加权收益率(%)')
    CHG = Column(Numeric(20, 10), comment='涨跌幅')


class CBONDFSUBJECTCVF(Base):
    """中国国债期货标的券"""
    __tablename__ = 'CBONDFSUBJECTCVF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    DLS_WINDCODE = Column(VARCHAR(40), comment='标的券Wind代码')
    B_TBF_CVF = Column(Numeric(20, 8), comment='转换因子')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class CBONDFSUBJECTCVFZL(Base):
    """国债期货标的券(增量)"""
    __tablename__ = 'CBONDFSUBJECTCVFZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    DLS_WINDCODE = Column(VARCHAR(40), comment='标的券Wind代码')
    B_TBF_CVF = Column(Numeric(20, 8), comment='转换因子')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class CBONDFTHIRDPARTYVALUATION(Base):
    """中国国债期货可交割券第三方估值"""
    __tablename__ = 'CBONDFTHIRDPARTYVALUATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    DLS_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    PRICETYPE_CODE = Column(Numeric(9, 0), comment='价格类型代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    DL_INTEREST = Column(Numeric(24, 8), comment='交割利息')
    INTERVALINTEREST = Column(Numeric(24, 8), comment='区间利息')
    DL_COST = Column(Numeric(20, 4), comment='交割成本')
    FS_SPREAD = Column(Numeric(20, 4), comment='期现价差')
    IRR = Column(Numeric(20, 4), comment='IRR')
    RT_SPREAD = Column(Numeric(20, 4), comment='基差')


class CBONDFUNDSTOP5COMPANIES(Base):
    """中国债券发行主体往来资金前五名公司明细"""
    __tablename__ = 'CBONDFUNDSTOP5COMPANIES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='单位名称')
    S_INFO_COMPCODE2 = Column(VARCHAR(40), comment='单位名称ID')
    TYPECODE = Column(Numeric(9, 0), comment='往来资金类别代码')
    CONDITIONCODE = Column(Numeric(9, 0), comment='往来资金条件代码')
    START_DT = Column(VARCHAR(8), comment='起始日')
    END_DT = Column(VARCHAR(8), comment='终止日')
    AMOUNT1 = Column(Numeric(20, 4), comment='金额')
    AMOUNT2 = Column(Numeric(20, 4), comment='原币金额')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    RATE = Column(VARCHAR(80), comment='利率')


class CBONDFUNDUSING(Base):
    """中国债券募集资金用途"""
    __tablename__ = 'CBONDFUNDUSING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券ID')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
    FUNDUSE = Column(TEXT(2147483647), comment='资金用途')


class CBONDFUTURESEODPRICES(Base):
    """中国国债期货交易日行情"""
    __tablename__ = 'CBONDFUTURESEODPRICES'
    __table_args__ = (
        Index('IDX_CBONDFUTURESEODPRICES_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_PRESETTLE = Column(Numeric(20, 4), comment='前结算价(元)')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(元)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(元)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(元)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(元)')
    S_DQ_SETTLE = Column(Numeric(20, 4), comment='结算价(元)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(万元)')
    S_DQ_OI = Column(Numeric(20, 4), comment='持仓量(手)')
    S_DQ_CHANGE = Column(Numeric(20, 4), comment='涨跌(元)')
    S_DQ_CCCODE = Column(VARCHAR(20), comment='连续合约代码')


class CBONDFUTURESPOSITIONS(Base):
    """中国国债期货成交及持仓"""
    __tablename__ = 'CBONDFUTURESPOSITIONS'
    __table_args__ = (
        Index('IDX_CBONDFUTURESPOSITIONS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    FS_INFO_MEMBERNAME = Column(VARCHAR(40), comment='会员简称')
    FS_INFO_TYPE = Column(VARCHAR(40), comment='类型')
    FS_INFO_POSITIONSNUM = Column(Numeric(20, 4), comment='数量')
    FS_INFO_RANK = Column(Numeric(5, 0), comment='名次')
    S_OI_POSITIONSNUMC = Column(Numeric(20, 4), comment='比上交易日增减')


class CBONDFVALUATION(Base):
    """中国国债期货可交割券衍生指标"""
    __tablename__ = 'CBONDFVALUATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    DLS_WINDCODE = Column(VARCHAR(40), comment='可交割券Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    DL_INTEREST = Column(Numeric(20, 8), comment='交割利息')
    INTERVALINTEREST = Column(Numeric(20, 8), comment='区间利息')
    DL_COST = Column(Numeric(20, 4), comment='交割成本')
    FS_SPREAD = Column(Numeric(20, 4), comment='期现价差')
    IRR = Column(Numeric(20, 4), comment='IRR')
    RT_SPREAD = Column(Numeric(20, 4), comment='基差')


class CBONDGOVERNMENTGRANTS(Base):
    """中国债券发行主体政府补助明细"""
    __tablename__ = 'CBONDGOVERNMENTGRANTS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ITEM_NAME = Column(VARCHAR(500), comment='项目')
    AMOUNT_CURRENT_ISSUE = Column(Numeric(20, 4), comment='本期发生额')
    AMOUNT_PREVIOUS_PERIOD = Column(Numeric(20, 4), comment='上期发生额')
    MEMO = Column(VARCHAR(2000), comment='说明')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class CBONDGUARANTEE(Base):
    """中国债券发行主体对外担保明细"""
    __tablename__ = 'CBONDGUARANTEE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    RELATION = Column(VARCHAR(40), comment='担保方与披露方关系')
    GUARANTOR = Column(VARCHAR(100), comment='担保方公司名称')
    RELATION2 = Column(VARCHAR(40), comment='被担保方与披露方关系')
    SECUREDPARTY = Column(VARCHAR(100), comment='被担保方公司名称')
    METHOD1 = Column(VARCHAR(40), comment='担保方式')
    AMOUNT = Column(Numeric(20, 4), comment='担保金额(元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='币种')
    TERM = Column(Numeric(20, 4), comment='担保期限(年)')
    START_DT = Column(VARCHAR(8), comment='担保起始日期')
    END_DT = Column(VARCHAR(8), comment='担保终止日期')
    IS_COMPLETE = Column(Numeric(1, 0), comment='是否履行完毕')
    IS_RELATED = Column(Numeric(1, 0), comment='是否关联交易')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    IS_OVERDUE = Column(Numeric(1, 0), comment='担保是否逾期')
    OVERDUE_AMOUNT = Column(Numeric(20, 4), comment='担保逾期金额(元)')
    IS_COUNTERGUARANTEE = Column(Numeric(1, 0), comment='是否存在反担保')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class CBONDGUARANTEEBALANCESHEET(Base):
    """中国债券担保人资产负债表"""
    __tablename__ = 'CBONDGUARANTEEBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    MONETARY_CAP = Column(Numeric(20, 4), comment='货币资金')
    TRADABLE_FIN_ASSETS = Column(Numeric(20, 4), comment='交易性金融资产')
    NOTES_RCV = Column(Numeric(20, 4), comment='应收票据')
    ACCT_RCV = Column(Numeric(20, 4), comment='应收账款')
    OTH_RCV = Column(Numeric(20, 4), comment='其他应收款')
    PREPAY = Column(Numeric(20, 4), comment='预付款项')
    DVD_RCV = Column(Numeric(20, 4), comment='应收股利')
    INT_RCV = Column(Numeric(20, 4), comment='应收利息')
    INVENTORIES = Column(Numeric(20, 4), comment='存货')
    CONSUMPTIVE_BIO_ASSETS = Column(Numeric(20, 4), comment='消耗性生物资产')
    DEFERRED_EXP = Column(Numeric(20, 4), comment='待摊费用')
    NON_CUR_ASSETS_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的非流动资产')
    SETTLE_RSRV = Column(Numeric(20, 4), comment='结算备付金')
    LOANS_TO_OTH_BANKS = Column(Numeric(20, 4), comment='拆出资金')
    PREM_RCV = Column(Numeric(20, 4), comment='应收保费')
    RCV_FROM_REINSURER = Column(Numeric(20, 4), comment='应收分保账款')
    RCV_FROM_CEDED_INSUR_CONT_RSRV = Column(Numeric(20, 4), comment='应收分保合同准备金')
    RED_MONETARY_CAP_FOR_SALE = Column(Numeric(20, 4), comment='买入返售金融资产')
    OTH_CUR_ASSETS = Column(Numeric(20, 4), comment='其他流动资产')
    TOT_CUR_ASSETS = Column(Numeric(20, 4), comment='流动资产合计')
    FIN_ASSETS_AVAIL_FOR_SALE = Column(Numeric(20, 4), comment='可供出售金融资产')
    HELD_TO_MTY_INVEST = Column(Numeric(20, 4), comment='持有至到期投资')
    LONG_TERM_EQY_INVEST = Column(Numeric(20, 4), comment='长期股权投资')
    INVEST_REAL_ESTATE = Column(Numeric(20, 4), comment='投资性房地产')
    TIME_DEPOSITS = Column(Numeric(20, 4), comment='定期存款')
    OTH_ASSETS = Column(Numeric(20, 4), comment='其他资产')
    LONG_TERM_REC = Column(Numeric(20, 4), comment='长期应收款')
    FIX_ASSETS = Column(Numeric(20, 4), comment='固定资产')
    CONST_IN_PROG = Column(Numeric(20, 4), comment='在建工程')
    PROJ_MATL = Column(Numeric(20, 4), comment='工程物资')
    FIX_ASSETS_DISP = Column(Numeric(20, 4), comment='固定资产清理')
    PRODUCTIVE_BIO_ASSETS = Column(Numeric(20, 4), comment='生产性生物资产')
    OIL_AND_NATURAL_GAS_ASSETS = Column(Numeric(20, 4), comment='油气资产')
    INTANG_ASSETS = Column(Numeric(20, 4), comment='无形资产')
    R_AND_D_COSTS = Column(Numeric(20, 4), comment='开发支出')
    GOODWILL = Column(Numeric(20, 4), comment='商誉')
    LONG_TERM_DEFERRED_EXP = Column(Numeric(20, 4), comment='长期待摊费用')
    DEFERRED_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产')
    LOANS_AND_ADV_GRANTED = Column(Numeric(20, 4), comment='发放贷款及垫款')
    OTH_NON_CUR_ASSETS = Column(Numeric(20, 4), comment='其他非流动资产')
    TOT_NON_CUR_ASSETS = Column(Numeric(20, 4), comment='非流动资产合计')
    CASH_DEPOSITS_CENTRAL_BANK = Column(Numeric(20, 4), comment='现金及存放中央银行款项')
    ASSET_DEP_OTH_BANKS_FIN_INST = Column(Numeric(20, 4), comment='存放同业和其它金融机构款项')
    PRECIOUS_METALS = Column(Numeric(20, 4), comment='贵金属')
    DERIVATIVE_FIN_ASSETS = Column(Numeric(20, 4), comment='衍生金融资产')
    AGENCY_BUS_ASSETS = Column(Numeric(20, 4), comment='代理业务资产')
    SUBR_REC = Column(Numeric(20, 4), comment='应收代位追偿款')
    RCV_CEDED_UNEARNED_PREM_RSRV = Column(Numeric(20, 4), comment='应收分保未到期责任准备金')
    RCV_CEDED_CLAIM_RSRV = Column(Numeric(20, 4), comment='应收分保未决赔款准备金')
    RCV_CEDED_LIFE_INSUR_RSRV = Column(Numeric(20, 4), comment='应收分保寿险责任准备金')
    RCV_CEDED_LT_HEALTH_INSUR_RSRV = Column(Numeric(20, 4), comment='应收分保长期健康险责任准备金')
    MRGN_PAID = Column(Numeric(20, 4), comment='存出保证金')
    INSURED_PLEDGE_LOAN = Column(Numeric(20, 4), comment='保户质押贷款')
    CAP_MRGN_PAID = Column(Numeric(20, 4), comment='存出资本保证金')
    INDEPENDENT_ACCT_ASSETS = Column(Numeric(20, 4), comment='独立账户资产')
    CLIENTS_CAP_DEPOSIT = Column(Numeric(20, 4), comment='客户资金存款')
    CLIENTS_RSRV_SETTLE = Column(Numeric(20, 4), comment='客户备付金')
    INCL_SEAT_FEES_EXCHANGE = Column(Numeric(20, 4), comment='其中：交易席位费')
    RCV_INVEST = Column(Numeric(20, 4), comment='应收款项类投资')
    TOT_ASSETS = Column(Numeric(20, 4), comment='资产总计')
    ST_BORROW = Column(Numeric(20, 4), comment='短期借款')
    BORROW_CENTRAL_BANK = Column(Numeric(20, 4), comment='向中央银行借款')
    DEPOSIT_RECEIVED_IB_DEPOSITS = Column(Numeric(20, 4), comment='吸收存款及同业存放')
    LOANS_OTH_BANKS = Column(Numeric(20, 4), comment='拆入资金')
    TRADABLE_FIN_LIAB = Column(Numeric(20, 4), comment='交易性金融负债')
    NOTES_PAYABLE = Column(Numeric(20, 4), comment='应付票据')
    ACCT_PAYABLE = Column(Numeric(20, 4), comment='应付账款')
    ADV_FROM_CUST = Column(Numeric(20, 4), comment='预收款项')
    FUND_SALES_FIN_ASSETS_RP = Column(Numeric(20, 4), comment='卖出回购金融资产款')
    HANDLING_CHARGES_COMM_PAYABLE = Column(Numeric(20, 4), comment='应付手续费及佣金')
    EMPL_BEN_PAYABLE = Column(Numeric(20, 4), comment='应付职工薪酬')
    TAXES_SURCHARGES_PAYABLE = Column(Numeric(20, 4), comment='应交税费')
    INT_PAYABLE = Column(Numeric(20, 4), comment='应付利息')
    DVD_PAYABLE = Column(Numeric(20, 4), comment='应付股利')
    OTH_PAYABLE = Column(Numeric(20, 4), comment='其他应付款')
    ACC_EXP = Column(Numeric(20, 4), comment='预提费用')
    DEFERRED_INC = Column(Numeric(20, 4), comment='递延收益')
    ST_BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付短期债券')
    PAYABLE_TO_REINSURER = Column(Numeric(20, 4), comment='应付分保账款')
    RSRV_INSUR_CONT = Column(Numeric(20, 4), comment='保险合同准备金')
    ACTING_TRADING_SEC = Column(Numeric(20, 4), comment='代理买卖证券款')
    ACTING_UW_SEC = Column(Numeric(20, 4), comment='代理承销证券款')
    NON_CUR_LIAB_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的非流动负债')
    OTH_CUR_LIAB = Column(Numeric(20, 4), comment='其他流动负债')
    TOT_CUR_LIAB = Column(Numeric(20, 4), comment='流动负债合计')
    LT_BORROW = Column(Numeric(20, 4), comment='长期借款')
    BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付债券')
    LT_PAYABLE = Column(Numeric(20, 4), comment='长期应付款')
    SPECIFIC_ITEM_PAYABLE = Column(Numeric(20, 4), comment='专项应付款')
    PROVISIONS = Column(Numeric(20, 4), comment='预计负债')
    DEFERRED_TAX_LIAB = Column(Numeric(20, 4), comment='递延所得税负债')
    DEFERRED_INC_NON_CUR_LIAB = Column(Numeric(20, 4), comment='递延收益-非流动负债')
    OTH_NON_CUR_LIAB = Column(Numeric(20, 4), comment='其他非流动负债')
    TOT_NON_CUR_LIAB = Column(Numeric(20, 4), comment='非流动负债合计')
    LIAB_DEP_OTH_BANKS_FIN_INST = Column(Numeric(20, 4), comment='同业和其它金融机构存放款项')
    DERIVATIVE_FIN_LIAB = Column(Numeric(20, 4), comment='衍生金融负债')
    CUST_BANK_DEP = Column(Numeric(20, 4), comment='吸收存款')
    AGENCY_BUS_LIAB = Column(Numeric(20, 4), comment='代理业务负债')
    OTH_LIAB = Column(Numeric(20, 4), comment='其他负债')
    PREM_RECEIVED_ADV = Column(Numeric(20, 4), comment='预收保费')
    DEPOSIT_RECEIVED = Column(Numeric(20, 4), comment='存入保证金')
    INSURED_DEPOSIT_INVEST = Column(Numeric(20, 4), comment='保户储金及投资款')
    UNEARNED_PREM_RSRV = Column(Numeric(20, 4), comment='未到期责任准备金')
    OUT_LOSS_RSRV = Column(Numeric(20, 4), comment='未决赔款准备金')
    LIFE_INSUR_RSRV = Column(Numeric(20, 4), comment='寿险责任准备金')
    LT_HEALTH_INSUR_V = Column(Numeric(20, 4), comment='长期健康险责任准备金')
    INDEPENDENT_ACCT_LIAB = Column(Numeric(20, 4), comment='独立账户负债')
    INCL_PLEDGE_LOAN = Column(Numeric(20, 4), comment='其中：质押借款')
    CLAIMS_PAYABLE = Column(Numeric(20, 4), comment='应付赔付款')
    DVD_PAYABLE_INSURED = Column(Numeric(20, 4), comment='应付保单红利')
    TOT_LIAB = Column(Numeric(20, 4), comment='负债合计')
    CAP_STK = Column(Numeric(20, 4), comment='股本')
    CAP_RSRV = Column(Numeric(20, 4), comment='资本公积金')
    SPECIAL_RSRV = Column(Numeric(20, 4), comment='专项储备')
    SURPLUS_RSRV = Column(Numeric(20, 4), comment='盈余公积金')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='未分配利润')
    LESS_TSY_STK = Column(Numeric(20, 4), comment='减：库存股')
    PROV_NOM_RISKS = Column(Numeric(20, 4), comment='一般风险准备')
    CNVD_DIFF_FOREIGN_CURR_STAT = Column(Numeric(20, 4), comment='外币报表折算差额')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认的投资损失')
    MINORITY_INT = Column(Numeric(20, 4), comment='少数股东权益')
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(不含少数股东权益)')
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(含少数股东权益)')
    TOT_LIAB_SHRHLDR_EQY = Column(Numeric(20, 4), comment='负债及股东权益总计')
    COMP_TYPE_CODE = Column(VARCHAR(2), comment='公司类型代码')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='[内部]实际公告日期')
    SPE_CUR_ASSETS_DIFF = Column(Numeric(20, 4), comment='流动资产差额(特殊报表科目)')
    TOT_CUR_ASSETS_DIFF = Column(Numeric(20, 4), comment='流动资产差额(合计平衡项目)')
    SPE_NON_CUR_ASSETS_DIFF = Column(Numeric(20, 4), comment='非流动资产差额(特殊报表科目)')
    TOT_NON_CUR_ASSETS_DIFF = Column(Numeric(20, 4), comment='非流动资产差额(合计平衡项目)')
    SPE_BAL_ASSETS_DIFF = Column(Numeric(20, 4), comment='资产差额(特殊报表科目)')
    TOT_BAL_ASSETS_DIFF = Column(Numeric(20, 4), comment='资产差额(合计平衡项目)')
    SPE_CUR_LIAB_DIFF = Column(Numeric(20, 4), comment='流动负债差额(特殊报表科目)')
    TOT_CUR_LIAB_DIFF = Column(Numeric(20, 4), comment='流动负债差额(合计平衡项目)')
    SPE_NON_CUR_LIAB_DIFF = Column(Numeric(20, 4), comment='非流动负债差额(特殊报表科目)')
    TOT_NON_CUR_LIAB_DIFF = Column(Numeric(20, 4), comment='非流动负债差额(合计平衡项目)')
    SPE_BAL_LIAB_DIFF = Column(Numeric(20, 4), comment='负债差额(特殊报表科目)')
    TOT_BAL_LIAB_DIFF = Column(Numeric(20, 4), comment='负债差额(合计平衡项目)')
    SPE_BAL_SHRHLDR_EQY_DIFF = Column(Numeric(20, 4), comment='股东权益差额(特殊报表科目)')
    TOT_BAL_SHRHLDR_EQY_DIFF = Column(Numeric(20, 4), comment='股东权益差额(合计平衡项目)')
    SPE_BAL_LIAB_EQY_DIFF = Column(Numeric(20, 4), comment='负债及股东权益差额(特殊报表项目)')
    TOT_BAL_LIAB_EQY_DIFF = Column(Numeric(20, 4), comment='负债及股东权益差额(合计平衡项目)')
    HFS_SALES = Column(Numeric(20, 4), comment='持有待售的负债')
    LT_PAYROLL_PAYABLE = Column(Numeric(20, 4), comment='长期应付职工薪酬')
    OTHER_EQUITY_TOOLS = Column(Numeric(20, 4), comment='其他权益工具')
    OTHER_EQUITY_TOOLS_P_SHR = Column(Numeric(20, 4), comment='其他权益工具:优先股')
    OTHER_COMP_INCOME = Column(Numeric(20, 4), comment='其他综合收益')
    HFS_ASSETS = Column(Numeric(20, 4), comment='划分为持有待售的资产')


class CBONDGUARANTEECASHFLOW(Base):
    """中国债券担保人现金流量表"""
    __tablename__ = 'CBONDGUARANTEECASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    CASH_RECP_SG_AND_RS = Column(Numeric(20, 4), comment='销售商品、提供劳务收到的现金')
    RECP_TAX_RENDS = Column(Numeric(20, 4), comment='收到的税费返还')
    NET_INCR_DEP_COB = Column(Numeric(20, 4), comment='客户存款和同业存放款项净增加额')
    NET_INCR_LOANS_CENTRAL_BANK = Column(Numeric(20, 4), comment='向中央银行借款净增加额')
    NET_INCR_FUND_BORR_OFI = Column(Numeric(20, 4), comment='向其他金融机构拆入资金净增加额')
    CASH_RECP_PREM_ORIG_INCO = Column(Numeric(20, 4), comment='收到原保险合同保费取得的现金')
    NET_INCR_INSURED_DEP = Column(Numeric(20, 4), comment='保户储金净增加额')
    NET_CASH_RECEIVED_REINSU_BUS = Column(Numeric(20, 4), comment='收到再保业务现金净额')
    NET_INCR_DISP_TFA = Column(Numeric(20, 4), comment='处置交易性金融资产净增加额')
    NET_INCR_INT_HANDLING_CHRG = Column(Numeric(20, 4), comment='收取利息和手续费净增加额')
    NET_INCR_DISP_FAAS = Column(Numeric(20, 4), comment='处置可供出售金融资产净增加额')
    NET_INCR_LOANS_OTHER_BANK = Column(Numeric(20, 4), comment='拆入资金净增加额')
    NET_INCR_REPURCH_BUS_FUND = Column(Numeric(20, 4), comment='回购业务资金净增加额')
    OTHER_CASH_RECP_RAL_OPER_ACT = Column(Numeric(20, 4), comment='收到其他与经营活动有关的现金')
    STOT_CASH_INFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流入小计')
    CASH_PAY_GOODS_PURCH_SERV_REC = Column(Numeric(20, 4), comment='购买商品、接受劳务支付的现金')
    CASH_PAY_BEH_EMPL = Column(Numeric(20, 4), comment='支付给职工以及为职工支付的现金')
    PAY_ALL_TYP_TAX = Column(Numeric(20, 4), comment='支付的各项税费')
    NET_INCR_CLIENTS_LOAN_ADV = Column(Numeric(20, 4), comment='客户贷款及垫款净增加额')
    NET_INCR_DEP_CBOB = Column(Numeric(20, 4), comment='存放央行和同业款项净增加额')
    CASH_PAY_CLAIMS_ORIG_INCO = Column(Numeric(20, 4), comment='支付原保险合同赔付款项的现金')
    HANDLING_CHRG_PAID = Column(Numeric(20, 4), comment='支付手续费的现金')
    COMM_INSUR_PLCY_PAID = Column(Numeric(20, 4), comment='支付保单红利的现金')
    OTHER_CASH_PAY_RAL_OPER_ACT = Column(Numeric(20, 4), comment='支付其他与经营活动有关的现金')
    STOT_CASH_OUTFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流出小计')
    NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额')
    CASH_RECP_DISP_WITHDRWL_INVEST = Column(Numeric(20, 4), comment='收回投资收到的现金')
    CASH_RECP_RETURN_INVEST = Column(Numeric(20, 4), comment='取得投资收益收到的现金')
    NET_CASH_RECP_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定资产、无形资产和其他长期资产收回的现金净额')
    NET_CASH_RECP_DISP_SOBU = Column(Numeric(20, 4), comment='处置子公司及其他营业单位收到的现金净额')
    OTHER_CASH_RECP_RAL_INV_ACT = Column(Numeric(20, 4), comment='收到其他与投资活动有关的现金')
    STOT_CASH_INFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流入小计')
    CASH_PAY_ACQ_CONST_FIOLTA = Column(Numeric(20, 4), comment='购建固定资产、无形资产和其他长期资产支付的现金')
    CASH_PAID_INVEST = Column(Numeric(20, 4), comment='投资支付的现金')
    NET_CASH_PAY_AQUIS_SOBU = Column(Numeric(20, 4), comment='取得子公司及其他营业单位支付的现金净额')
    OTHER_CASH_PAY_RAL_INV_ACT = Column(Numeric(20, 4), comment='支付其他与投资活动有关的现金')
    NET_INCR_PLEDGE_LOAN = Column(Numeric(20, 4), comment='质押贷款净增加额')
    STOT_CASH_OUTFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流出小计')
    NET_CASH_FLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额')
    CASH_RECP_CAP_CONTRIB = Column(Numeric(20, 4), comment='吸收投资收到的现金')
    INCL_CASH_REC_SAIMS = Column(Numeric(20, 4), comment='其中：子公司吸收少数股东投资收到的现金')
    CASH_RECP_BORROW = Column(Numeric(20, 4), comment='取得借款收到的现金')
    PROC_ISSUE_BONDS = Column(Numeric(20, 4), comment='发行债券收到的现金')
    OTHER_CASH_RECP_RAL_FNC_ACT = Column(Numeric(20, 4), comment='收到其他与筹资活动有关的现金')
    STOT_CASH_INFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流入小计')
    CASH_PREPAY_AMT_BORR = Column(Numeric(20, 4), comment='偿还债务支付的现金')
    CASH_PAY_DIST_DPCP_INT_EXP = Column(Numeric(20, 4), comment='分配股利、利润或偿付利息支付的现金')
    INCL_DVD_PROFIT_PAID_SC_MS = Column(Numeric(20, 4), comment='其中：子公司支付给少数股东的股利、利润')
    OTHER_CASH_PAY_RAL_FNC_ACT = Column(Numeric(20, 4), comment='支付其他与筹资活动有关的现金')
    STOT_CASH_OUTFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流出小计')
    NET_CASH_FLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额')
    EFF_FX_FLU_CASH = Column(Numeric(20, 4), comment='汇率变动对现金的影响')
    NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物净增加额')
    CASH_CASH_EQU_BEG_PERIOD = Column(Numeric(20, 4), comment='期初现金及现金等价物余额')
    CASH_CASH_EQU_END_PERIOD = Column(Numeric(20, 4), comment='期末现金及现金等价物余额')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认投资损失')
    PLUS_PROV_DEPR_ASSETS = Column(Numeric(20, 4), comment='加：资产减值准备')
    DEPR_FA_COGA_DPBA = Column(Numeric(20, 4), comment='固定资产折旧、油气资产折耗、生产性生物资产折旧')
    AMORT_INTANG_ASSETS = Column(Numeric(20, 4), comment='无形资产摊销')
    AMORT_LT_DEFERRED_EXP = Column(Numeric(20, 4), comment='长期待摊费用摊销')
    DECR_DEFERRED_EXP = Column(Numeric(20, 4), comment='待摊费用减少')
    INCR_ACC_EXP = Column(Numeric(20, 4), comment='预提费用增加')
    LOSS_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定、无形资产和其他长期资产的损失')
    LOSS_SCR_FA = Column(Numeric(20, 4), comment='固定资产报废损失')
    LOSS_FV_CHG = Column(Numeric(20, 4), comment='公允价值变动损失')
    FIN_EXP = Column(Numeric(20, 4), comment='财务费用')
    INVEST_LOSS = Column(Numeric(20, 4), comment='投资损失')
    DECR_DEFERRED_INC_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产减少')
    INCR_DEFERRED_INC_TAX_LIAB = Column(Numeric(20, 4), comment='递延所得税负债增加')
    DECR_INVENTORIES = Column(Numeric(20, 4), comment='存货的减少')
    DECR_OPER_PAYABLE = Column(Numeric(20, 4), comment='经营性应收项目的减少')
    INCR_OPER_PAYABLE = Column(Numeric(20, 4), comment='经营性应付项目的增加')
    OTHERS = Column(Numeric(20, 4), comment='其他')
    IM_NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='间接法-经营活动产生的现金流量净额')
    CONV_DEBT_INTO_CAP = Column(Numeric(20, 4), comment='债务转为资本')
    CONV_CORP_BONDS_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的可转换公司债券')
    FA_FNC_LEASES = Column(Numeric(20, 4), comment='融资租入固定资产')
    END_BAL_CASH = Column(Numeric(20, 4), comment='现金的期末余额')
    LESS_BEG_BAL_CASH = Column(Numeric(20, 4), comment='减：现金的期初余额')
    PLUS_END_BAL_CASH_EQU = Column(Numeric(20, 4), comment='加：现金等价物的期末余额')
    LESS_BEG_BAL_CASH_EQU = Column(Numeric(20, 4), comment='减：现金等价物的期初余额')
    IM_NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='间接法-现金及现金等价物净增加额')
    FREE_CASH_FLOW = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)')
    COMP_TYPE_CODE = Column(VARCHAR(2), comment='公司类型代码')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='[内部]实际公告日期')
    SPE_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(合计平衡项目)')
    SPE_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(合计平衡项目)')
    TOT_BAL_NETCASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额差额(合计平衡项目)')
    SPE_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(合计平衡项目)')
    SPE_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(合计平衡项目)')
    TOT_BAL_NETCASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额差额(合计平衡项目)')
    SPE_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(合计平衡项目)')
    SPE_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(合计平衡项目)')
    TOT_BAL_NETCASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额差额(合计平衡项目)')
    SPE_BAL_NETCASH_INC = Column(Numeric(20, 4), comment='现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_INC = Column(Numeric(20, 4), comment='现金净增加额差额(合计平衡项目)')
    SPE_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(合计平衡项目)')
    SPE_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(合计平衡项目)')


class CBONDGUARANTEEDETAIL(Base):
    """中国债券发行主体担保数据(明细)"""
    __tablename__ = 'CBONDGUARANTEEDETAIL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    COMPANY_GUARANTEED = Column(VARCHAR(100), comment='被担保公司名称')
    AMOUNTOFGUARANTEE = Column(Numeric(20, 0), comment='担保金额(万元)')
    GUARANTEECOMPANYTYPE = Column(VARCHAR(20), comment='担保公司类别')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')


class CBONDGUARANTEEINCOME(Base):
    """中国债券担保人利润表"""
    __tablename__ = 'CBONDGUARANTEEINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    TOT_OPER_REV = Column(Numeric(20, 4), comment='营业总收入')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入')
    INT_INC = Column(Numeric(20, 4), comment='利息收入')
    NET_INT_INC = Column(Numeric(20, 4), comment='利息净收入')
    INSUR_PREM_UNEARNED = Column(Numeric(20, 4), comment='已赚保费')
    HANDLING_CHRG_COMM_INC = Column(Numeric(20, 4), comment='手续费及佣金收入')
    NET_HANDLING_CHRG_COMM_INC = Column(Numeric(20, 4), comment='手续费及佣金净收入')
    NET_INC_OTHER_OPS = Column(Numeric(20, 4), comment='其他经营净收益')
    PLUS_NET_INC_OTHER_BUS = Column(Numeric(20, 4), comment='加:其他业务净收益')
    PREM_INC = Column(Numeric(20, 4), comment='保费业务收入')
    LESS_CEDED_OUT_PREM = Column(Numeric(20, 4), comment='减：分出保费')
    CHG_UNEARNED_PREM_RES = Column(Numeric(20, 4), comment='提取未到期责任准备金')
    INCL_REINSURANCE_PREM_INC = Column(Numeric(20, 4), comment='其中：分保费收入')
    NET_INC_SEC_TRADING_BROK_BUS = Column(Numeric(20, 4), comment='代理买卖证券业务净收入')
    NET_INC_SEC_UW_BUS = Column(Numeric(20, 4), comment='证券承销业务净收入')
    NET_INC_EC_ASSET_MGMT_BUS = Column(Numeric(20, 4), comment='受托客户资产管理业务净收入')
    OTHER_BUS_INC = Column(Numeric(20, 4), comment='其他业务收入')
    PLUS_NET_GAIN_CHG_FV = Column(Numeric(20, 4), comment='加:公允价值变动净收益')
    PLUS_NET_INVEST_INC = Column(Numeric(20, 4), comment='加:投资净收益')
    INCL_INC_INVEST_ASSOC_JV_ENTP = Column(Numeric(20, 4), comment='其中：对联营企业和合营企业的投资收益')
    PLUS_NET_GAIN_FX_TRANS = Column(Numeric(20, 4), comment='加:汇兑净收益')
    TOT_OPER_COST = Column(Numeric(20, 4), comment='营业总成本')
    LESS_OPER_COST = Column(Numeric(20, 4), comment='减:营业成本')
    LESS_INT_EXP = Column(Numeric(20, 4), comment='减:利息支出')
    LESS_HANDLING_CHRG_COMM_EXP = Column(Numeric(20, 4), comment='减:手续费及佣金支出')
    LESS_TAXES_SURCHARGES_OPS = Column(Numeric(20, 4), comment='减:营业税金及附加')
    LESS_SELLING_DIST_EXP = Column(Numeric(20, 4), comment='减:销售费用')
    LESS_GERL_ADMIN_EXP = Column(Numeric(20, 4), comment='减:管理费用')
    LESS_FIN_EXP = Column(Numeric(20, 4), comment='减:财务费用')
    LESS_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='减:资产减值损失')
    PREPAY_SURR = Column(Numeric(20, 4), comment='退保金')
    TOT_CLAIM_EXP = Column(Numeric(20, 4), comment='赔付总支出')
    CHG_INSUR_CONT_RSRV = Column(Numeric(20, 4), comment='提取保险责任准备金')
    DVD_EXP_INSURED = Column(Numeric(20, 4), comment='保户红利支出')
    REINSURANCE_EXP = Column(Numeric(20, 4), comment='分保费用')
    OPER_EXP = Column(Numeric(20, 4), comment='营业支出')
    LESS_CLAIM_RECB_REINSURER = Column(Numeric(20, 4), comment='减：摊回赔付支出')
    LESS_INS_RSRV_RECB_REINSURER = Column(Numeric(20, 4), comment='减：摊回保险责任准备金')
    LESS_EXP_RECB_REINSURER = Column(Numeric(20, 4), comment='减：摊回分保费用')
    OTHER_BUS_COST = Column(Numeric(20, 4), comment='其他业务成本')
    OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    PLUS_NON_OPER_REV = Column(Numeric(20, 4), comment='加:营业外收入')
    LESS_NON_OPER_EXP = Column(Numeric(20, 4), comment='减：营业外支出')
    IL_NET_LOSS_DISP_NONCUR_ASSET = Column(Numeric(20, 4), comment='其中：减：非流动资产处置净损失')
    TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    INC_TAX = Column(Numeric(20, 4), comment='所得税')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认投资损失')
    NET_PROFIT_INCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(含少数股东损益)')
    NET_PROFIT_EXCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(不含少数股东损益)')
    MINORITY_INT_INC = Column(Numeric(20, 4), comment='少数股东损益')
    OTHER_COMPREH_INC = Column(Numeric(20, 4), comment='其他综合收益')
    TOT_COMPREH_INC = Column(Numeric(20, 4), comment='综合收益总额')
    TOT_COMPREH_INC_PARENT_COMP = Column(Numeric(20, 4), comment='综合收益总额(母公司)')
    TOT_COMPREH_INC_MIN_SHRHLDR = Column(Numeric(20, 4), comment='综合收益总额(少数股东)')
    EBIT = Column(Numeric(20, 4), comment='项目金额')
    EBITDA = Column(Numeric(20, 4), comment='项目金额')
    NET_PROFIT_AFTER_DED_NR_LP = Column(Numeric(20, 4), comment='扣除非经常性损益后净利润')
    NET_PROFIT_UNDER_INTL_ACC_STA = Column(Numeric(20, 4), comment='国际会计准则净利润')
    COMP_TYPE_CODE = Column(VARCHAR(2), comment='公司类型代码')
    S_FA_EPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益')
    S_FA_EPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='[内部]实际公告日期')
    INSURANCE_EXPENSE = Column(Numeric(20, 4), comment='保险业务支出')
    SPE_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(特殊报表科目)')
    TOT_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(合计平衡项目)')
    SPE_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(特殊报表科目)')
    TOT_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(合计平衡项目)')
    SPE_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(特殊报表科目)')
    TOT_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(合计平衡项目)')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='年初未分配利润')
    ADJLOSSGAIN_PREVYEAR = Column(Numeric(20, 4), comment='调整以前年度损益')
    TRANSFER_FROM_SURPLUSRESERVE = Column(Numeric(20, 4), comment='盈余公积转入')
    TRANSFER_FROM_HOUSINGIMPREST = Column(Numeric(20, 4), comment='住房周转金转入')
    TRANSFER_FROM_OTHERS = Column(Numeric(20, 4), comment='其他转入')
    DISTRIBUTABLE_PROFIT = Column(Numeric(20, 4), comment='可分配利润')
    WITHDR_LEGALSURPLUS = Column(Numeric(20, 4), comment='提取法定盈余公积')
    WITHDR_LEGALPUBWELFUNDS = Column(Numeric(20, 4), comment='提取法定公益金')
    WORKERS_WELFARE = Column(Numeric(20, 4), comment='职工奖金福利')
    WITHDR_BUZEXPWELFARE = Column(Numeric(20, 4), comment='提取企业发展基金')
    WITHDR_RESERVEFUND = Column(Numeric(20, 4), comment='提取储备基金')
    DISTRIBUTABLE_PROFIT_SHRHDER = Column(Numeric(20, 4), comment='可供股东分配的利润')
    PRFSHARE_DVD_PAYABLE = Column(Numeric(20, 4), comment='应付优先股股利')
    WITHDR_OTHERSURPRESERVE = Column(Numeric(20, 4), comment='提取任意盈余公积金')
    COMSHARE_DVD_PAYABLE = Column(Numeric(20, 4), comment='应付普通股股利')
    CAPITALIZED_COMSTOCK_DIV = Column(Numeric(20, 4), comment='转作股本的普通股股利')
    ASSET_DISPOSAL_INCOME = Column(Numeric(20, 4), comment='资产处置收益')
    OTHER_INCOME = Column(Numeric(20, 4), comment='其他收益')
    CONTINUED_NET_PROFIT = Column(Numeric(20, 4), comment='持续经营净利润')
    END_NET_PROFIT = Column(Numeric(20, 4), comment='终止经营净利润')


class CBONDGUARANTEEINFO(Base):
    """中国债券担保人"""
    __tablename__ = 'CBONDGUARANTEEINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='债券Wind代码')
    GUARANTOR = Column(VARCHAR(100), comment='担保人')
    GUARANTOR_ID = Column(VARCHAR(40), comment='担保人ID')
    B_AGENCY_GUARANTORNATURE = Column(VARCHAR(40), comment='担保人公司属性')
    B_AGENCY_GRNTTYPE = Column(VARCHAR(100), comment='担保方式')
    B_AGENCY_GRNTTYPECODE = Column(Numeric(9, 0), comment='担保方式代码')
    B_INFO_GUARTERM = Column(VARCHAR(3000), comment='担保期限')
    B_INFO_GUARRANGE = Column(VARCHAR(3990), comment='担保范围')
    B_AGENCY_REGUARANTOR = Column(VARCHAR(100), comment='再担保人')
    B_AGENCY_REGUARANTORID = Column(VARCHAR(40), comment='再担保人ID')
    B_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    B_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期 ')


class CBONDGUARANTEEINFOQL(Base):
    """None"""
    __tablename__ = 'CBONDGUARANTEEINFOQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='债券Wind代码')
    GUARANTOR = Column(VARCHAR(100), comment='担保人')
    GUARANTOR_ID = Column(VARCHAR(40), comment='担保人ID')
    B_AGENCY_GUARANTORNATURE = Column(VARCHAR(40), comment='担保人公司属性')
    B_AGENCY_GRNTTYPE = Column(VARCHAR(100), comment='担保方式')
    B_AGENCY_GRNTTYPECODE = Column(Numeric(9, 0), comment='担保方式代码')
    B_INFO_GUARTERM = Column(VARCHAR(3000), comment='担保期限')
    B_INFO_GUARRANGE = Column(VARCHAR, comment='担保范围')
    B_AGENCY_REGUARANTOR = Column(VARCHAR(100), comment='再担保人')
    B_AGENCY_REGUARANTORID = Column(VARCHAR(40), comment='再担保人ID')
    B_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    B_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期')


class CBONDGUARANTEEINFOZL(Base):
    """中国债券担保信息(增量)"""
    __tablename__ = 'CBONDGUARANTEEINFOZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='债券Wind代码')
    GUARANTOR = Column(VARCHAR(100), comment='担保人')
    GUARANTOR_ID = Column(VARCHAR(40), comment='担保人ID')
    B_AGENCY_GUARANTORNATURE = Column(VARCHAR(40), comment='担保人公司属性')
    B_AGENCY_GRNTTYPE = Column(VARCHAR(100), comment='担保方式')
    B_AGENCY_GRNTTYPECODE = Column(Numeric(9, 0), comment='担保方式代码')
    B_INFO_GUARTERM = Column(VARCHAR(3000), comment='担保期限')
    B_INFO_GUARRANGE = Column(VARCHAR(3700), comment='担保范围')
    B_AGENCY_REGUARANTOR = Column(VARCHAR(100), comment='再担保人')
    B_AGENCY_REGUARANTORID = Column(VARCHAR(40), comment='再担保人ID')
    B_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    B_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期')


class CBONDGUARANTEERELATIONSHIP(Base):
    """中国债券公司担保"""
    __tablename__ = 'CBONDGUARANTEERELATIONSHIP'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='被担保公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='被担保公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='被担保公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class CBONDGUARANTEESTATISTICS(Base):
    """中国债券发行主体对外担保统计"""
    __tablename__ = 'CBONDGUARANTEESTATISTICS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    TOTAL_AMOUNT_GUARANTEE = Column(Numeric(20, 4), comment='担保发生额合计')
    GUARANTEE_BALANCE_TOTAL = Column(Numeric(20, 4), comment='担保余额合计')
    AMOUNT_OF_GUARANTEE = Column(Numeric(20, 4), comment='担保总额')
    HOLDING_TOTAL_AMOUNT_GUARANTEE = Column(Numeric(20, 4), comment='对控股子公司担保发生额合计')
    VIOLATION_AMOUNT_GUARANTEE = Column(Numeric(20, 4), comment='违规担保总额')
    AMOUNT_OF_GUARANTEE_RATE = Column(Numeric(20, 4), comment='担保总额占净资产比例')
    DEADLINE = Column(VARCHAR(8), comment='截止日期')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    HOLDING_TOTAL = Column(Numeric(20, 4), comment='对控股子公司担保余额合计')
    CONTROLLING_TOTAL = Column(Numeric(20, 4), comment='为控股股东及其他关联方提供担保金额')
    TOTAL_AMOUNT_GUARANTEE1 = Column(Numeric(20, 4), comment='为高负债对象提供担保金额')
    IS_MORE_THAN_NET_ASSETS = Column(Numeric(5, 0), comment='担保总额是否超过净资产50%')
    NET_ASSETS_RATE = Column(Numeric(20, 4), comment='担保总额占净资产比例(%)(计算值)')
    MORE_THAN_NET_ASSETS_AMOUNT = Column(Numeric(20, 4), comment='担保总额超过净资产50%部分的金额')
    HOLDING_AMOUNT_OF_GUARANTEE = Column(Numeric(20, 4), comment='对控股子公司担保额度合计')
    EXTERNAL_GUARANTEE = Column(Numeric(20, 4), comment='对外担保额度合计')
    AMOUNT_OF_GUARANTEE_TOTAL = Column(Numeric(20, 4), comment='担保额度合计')
    NET_ASSETS_RATE2 = Column(Numeric(20, 4), comment='担保额度占净资产比例')


class CBONDGUARANTEETOTAL(Base):
    """中国债券发行主体担保数据(合计)"""
    __tablename__ = 'CBONDGUARANTEETOTAL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    GUAR_BALANCE = Column(Numeric(20, 4), comment='担保余额(万元)')
    GUAR_INWARDS = Column(Numeric(20, 4), comment='对内担保余额(万元)')
    GUAR_OUTWARDS = Column(Numeric(20, 4), comment='对外担保余额(万元)')
    MEMO = Column(VARCHAR(3000), comment='备注')


class CBONDHOLDER(Base):
    """中国债券持有人"""
    __tablename__ = 'CBONDHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_FA_LATELYRD = Column(VARCHAR(8), comment='报告期')
    B_INFO_HOLDER = Column(VARCHAR(100), comment='持有人')
    B_INFO_HOLDAMOUNT = Column(Numeric(20, 4), comment='持有数量(张)')
    B_ISSUER_SHARECATEGORY = Column(VARCHAR(1), comment='持有人类型')
    B_INFO_HOLDER_ID = Column(VARCHAR(10), comment='持有人ID')


class CBONDHOLDERSMEETING(Base):
    """中国债券持有人大会通知"""
    __tablename__ = 'CBONDHOLDERSMEETING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    MEETING_NAME = Column(VARCHAR(40), comment='会议名称')
    IS_NEW = Column(Numeric(5, 0), comment='最新标志')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    MEETING_DT = Column(VARCHAR(8), comment='会议日期')
    MEETING_TYPE = Column(VARCHAR(20), comment='会议类型')
    MEETING_CONTENT = Column(TEXT(2147483647), comment='会议内容')
    IS_INTNET = Column(Numeric(5, 0), comment='是否可以网络投票')
    SMTGRECDATE = Column(VARCHAR(8), comment='A股股权登记日')
    SPOTMTGSTARTDATE = Column(VARCHAR(8), comment='会议登记起始日')
    SPOTMTGENDDATE = Column(VARCHAR(8), comment='会议登记截止日')
    VOTINGCODE = Column(Numeric(9, 0), comment='投票通道代码')
    MEETEVENT_ID = Column(VARCHAR(40), comment='会议事件ID')
    TYPE_CODE = Column(Numeric(9, 0), comment='品种类型代码')
    MEETING_PLACE = Column(VARCHAR(400), comment='会议召开地点')
    IS_NOTARIZATION = Column(Numeric(5, 0), comment='是否经公证')
    RESOLUTION_ANN_DT = Column(VARCHAR(8), comment='决议公告日')
    RESOLUTION_CONTENT = Column(VARCHAR(3000), comment='决议内容')
    COST_TOT = Column(Numeric(20, 4), comment='大会费用合计')
    ATTEND_RATIO = Column(Numeric(20, 4), comment='持有人出席比例')


class CBONDHOLDERZL(Base):
    """中国债券持有人(增量)"""
    __tablename__ = 'CBONDHOLDERZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_FA_LATELYRD = Column(VARCHAR(8), comment='报告期')
    B_INFO_HOLDER = Column(VARCHAR(100), comment='持有人')
    B_INFO_HOLDAMOUNT = Column(Numeric(20, 4), comment='持有数量(张)')
    B_ISSUER_SHARECATEGORY = Column(VARCHAR(1), comment='持有人类型')
    B_INFO_HOLDER_ID = Column(VARCHAR(10), comment='持有人ID')


class CBONDIBRMBMONDMAROVIEW(Base):
    """None"""
    __tablename__ = 'CBONDIBRMBMONDMAROVIEW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_INFO_TYPECODE = Column(VARCHAR(40), comment='交易品种代码')
    B_DQ_TYPE = Column(VARCHAR(80), comment='交易品种')
    B_DQ_NUMBER = Column(Numeric(20, 8), comment='成交笔数')
    B_DQ_NOCHANGE = Column(Numeric(20, 8), comment='成交笔数增减')
    B_DQ_TRADINGVALUE = Column(Numeric(20, 8), comment='成交量(亿元)')
    B_DQ_VCHANGE = Column(Numeric(20, 8), comment='成交额增减（亿元）')
    B_DQ_WAVRATE = Column(Numeric(20, 8), comment='加权平均利率(%)')
    B_DQ_BPCHANGE = Column(Numeric(20, 8), comment='升降基点')
    B_DQ_NOMEMBERSINVO = Column(Numeric(20, 8), comment='参与成员家数')


class CBONDIBRMBMONDMARQUOTATION(Base):
    """银行间本币货币市场日行情"""
    __tablename__ = 'CBONDIBRMBMONDMARQUOTATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_DQ_TYPE = Column(VARCHAR(80), comment='交易品种')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_DQ_OPEN = Column(Numeric(20, 8), comment='开盘利率')
    B_DQ_HIGH = Column(Numeric(20, 8), comment='最高利率')
    B_DQ_LOW = Column(Numeric(20, 8), comment='最低利率')
    B_DQ_ORIGINCLOSE = Column(Numeric(20, 8), comment='收盘利率')
    B_DQ_WAVERAGERATE = Column(Numeric(20, 8), comment='加权平均利率')
    B_DQ_BPCHANGE = Column(Numeric(20, 8), comment='升降(基点)')
    B_DQ_VOLUME = Column(Numeric(20, 8), comment='成交量(手)')
    B_DQ_AMOUNT = Column(Numeric(20, 8), comment='成交金额(亿元)')
    B_DQ_AMOUNTCHANGE = Column(Numeric(20, 8), comment='成交量增减(亿元)')


class CBONDIMPORTANTINDICATORS(Base):
    """中国债券发行主体公布重要指标"""
    __tablename__ = 'CBONDIMPORTANTINDICATORS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    IFLISTED_DATA = Column(Numeric(5, 0), comment='是否上市后数据')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_FA_EPS_DILUTED = Column(Numeric(20, 4), comment='每股收益-摊薄')
    S_FA_BPS_SH = Column(Numeric(20, 4), comment='归属于母公司股东的每股净资产')
    S_FA_BPS_ADJUST = Column(Numeric(20, 4), comment='每股净资产-调整')
    ROE_DILUTED = Column(Numeric(20, 4), comment='净资产收益率-摊薄(%)')
    S_INFO_DIV = Column(VARCHAR(40), comment='分红方案')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_FA_EPS_EX = Column(Numeric(20, 4), comment='每股收益-扣除')
    ROE_WEIGHTED = Column(Numeric(20, 4), comment='净资产收益率-加权(%)')
    ROE_EXWEIGHTED = Column(Numeric(20, 4), comment='净资产收益率-扣除/加权(%)')
    S_FA_EPS_BASIC = Column(Numeric(20, 4), comment='每股收益-基本')
    S_FA_EPS_EXBASIC = Column(Numeric(20, 4), comment='每股收益-扣除/基本')
    ROE_EX = Column(Numeric(20, 4), comment='净资产收益率-扣除(%)')
    S_FA_DEDUCTEDPROFIT = Column(Numeric(20, 4), comment='扣除非经常性损益后的净利润(扣除少数股东损益)')
    S_FA_CURRENT = Column(Numeric(20, 4), comment='流动比')
    S_FA_QUICK = Column(Numeric(20, 4), comment='速动比')
    S_FA_ARTURN = Column(Numeric(20, 4), comment='应收账款周转率')
    S_FA_INVTURN = Column(Numeric(20, 4), comment='存货周转率')
    S_FT_DEBTTOASSETS = Column(Numeric(20, 4), comment='资产负债率(%)')
    S_FA_OCFPS = Column(Numeric(20, 4), comment='每股经营活动产生的现金流量净额')
    NET_PROFIT = Column(Numeric(20, 4), comment='国际会计准则净利润')
    RD_EXPENSE = Column(Numeric(20, 4), comment='研发费用')
    S_FA_EPS_DILUTED2 = Column(Numeric(20, 6), comment='每股收益-稀释')
    S_FA_EPS_EXDILUTED = Column(Numeric(20, 4), comment='每股收益-扣除/稀释')
    S_FA_BPS = Column(Numeric(22, 4), comment='每股净资产')
    S_FA_EXTRAORDINARY = Column(Numeric(22, 4), comment='非经常性损益')
    S_FA_TOT_ASSETS = Column(Numeric(22, 4), comment='比年初增长率.总资产(%)')
    S_FA_YOYEPS_BASIC = Column(Numeric(22, 4), comment='同比增长率.基本每股收益(%)')
    S_FA_YOYEPS_DILUTED = Column(Numeric(22, 4), comment='同比增长率.稀释每股收益(%)')
    S_FA_YOYEQUITY = Column(Numeric(22, 4), comment='比年初增长率.归属母公司的股东权益(%)')
    GROWTH_BPS_SH = Column(Numeric(22, 4), comment='比年初增长率.归属于母公司股东的每股净资产(%)')
    S_FA_YOYOCFPS = Column(Numeric(22, 4), comment='同比增长率.每股经营活动产生的现金流量净额(%)')
    YOY_NET_CASH_FLOWS = Column(Numeric(22, 4), comment='同比增长率.经营活动产生的现金流量净额(%)')
    S_FA_DEDUCTEDPROFIT_YOY = Column(Numeric(22, 4), comment='同比增长率.扣除非经常性损益后的净利润(扣除少数股东损益)(%)')
    YOY_ROE_DILUTED = Column(Numeric(22, 4), comment='同比增长率.净资产收益率(摊薄)(%)')
    S_FA_YOYOP = Column(Numeric(20, 4), comment='同比增长率.营业利润(%)')
    S_FA_YOYEBT = Column(Numeric(20, 4), comment='同比增长率.利润总额(%)')
    NET_PROFIT_YOY = Column(Numeric(20, 4), comment='同比增长率.净利润(%)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    STATEMENT_TYPE_CODE = Column(Numeric(9, 0), comment='报表类型代码')
    CONTRIBUTIONPS = Column(Numeric(20, 4), comment='每股社会贡献值')
    MEMO = Column(VARCHAR(100), comment='备注')


class CBONDINCOME(Base):
    """中国债券发行主体利润表"""
    __tablename__ = 'CBONDINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    TOT_OPER_REV = Column(Numeric(20, 4), comment='营业总收入')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入')
    INT_INC = Column(Numeric(20, 4), comment='利息收入')
    NET_INT_INC = Column(Numeric(20, 4), comment='利息净收入')
    INSUR_PREM_UNEARNED = Column(Numeric(20, 4), comment='已赚保费')
    HANDLING_CHRG_COMM_INC = Column(Numeric(20, 4), comment='手续费及佣金收入')
    NET_HANDLING_CHRG_COMM_INC = Column(Numeric(20, 4), comment='手续费及佣金净收入')
    NET_INC_OTHER_OPS = Column(Numeric(20, 4), comment='其他经营净收益')
    PLUS_NET_INC_OTHER_BUS = Column(Numeric(20, 4), comment='加:其他业务净收益')
    PREM_INC = Column(Numeric(20, 4), comment='保费业务收入')
    LESS_CEDED_OUT_PREM = Column(Numeric(20, 4), comment='减:分出保费')
    CHG_UNEARNED_PREM_RES = Column(Numeric(20, 4), comment='提取未到期责任准备金')
    INCL_REINSURANCE_PREM_INC = Column(Numeric(20, 4), comment='其中:分保费收入')
    NET_INC_SEC_TRADING_BROK_BUS = Column(Numeric(20, 4), comment='代理买卖证券业务净收入')
    NET_INC_SEC_UW_BUS = Column(Numeric(20, 4), comment='证券承销业务净收入')
    NET_INC_EC_ASSET_MGMT_BUS = Column(Numeric(20, 4), comment='受托客户资产管理业务净收入')
    OTHER_BUS_INC = Column(Numeric(20, 4), comment='其他业务收入')
    PLUS_NET_GAIN_CHG_FV = Column(Numeric(20, 4), comment='加:公允价值变动净收益')
    PLUS_NET_INVEST_INC = Column(Numeric(20, 4), comment='加:投资净收益')
    INCL_INC_INVEST_ASSOC_JV_ENTP = Column(Numeric(20, 4), comment='其中:对联营企业和合营企业的投资收益')
    PLUS_NET_GAIN_FX_TRANS = Column(Numeric(20, 4), comment='加:汇兑净收益')
    TOT_OPER_COST = Column(Numeric(20, 4), comment='营业总成本')
    LESS_OPER_COST = Column(Numeric(20, 4), comment='减:营业成本')
    LESS_INT_EXP = Column(Numeric(20, 4), comment='减:利息支出')
    LESS_HANDLING_CHRG_COMM_EXP = Column(Numeric(20, 4), comment='减:手续费及佣金支出')
    LESS_TAXES_SURCHARGES_OPS = Column(Numeric(20, 4), comment='减:营业税金及附加')
    LESS_SELLING_DIST_EXP = Column(Numeric(20, 4), comment='减:销售费用')
    LESS_GERL_ADMIN_EXP = Column(Numeric(20, 4), comment='减:管理费用')
    LESS_FIN_EXP = Column(Numeric(20, 4), comment='减:财务费用')
    LESS_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='减:资产减值损失')
    PREPAY_SURR = Column(Numeric(20, 4), comment='退保金')
    TOT_CLAIM_EXP = Column(Numeric(20, 4), comment='赔付总支出')
    CHG_INSUR_CONT_RSRV = Column(Numeric(20, 4), comment='提取保险责任准备金')
    DVD_EXP_INSURED = Column(Numeric(20, 4), comment='保户红利支出')
    REINSURANCE_EXP = Column(Numeric(20, 4), comment='分保费用')
    OPER_EXP = Column(Numeric(20, 4), comment='营业支出')
    LESS_CLAIM_RECB_REINSURER = Column(Numeric(20, 4), comment='减:摊回赔付支出')
    LESS_INS_RSRV_RECB_REINSURER = Column(Numeric(20, 4), comment='减:摊回保险责任准备金')
    LESS_EXP_RECB_REINSURER = Column(Numeric(20, 4), comment='减:摊回分保费用')
    OTHER_BUS_COST = Column(Numeric(20, 4), comment='其他业务成本')
    OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    PLUS_NON_OPER_REV = Column(Numeric(20, 4), comment='加:营业外收入')
    LESS_NON_OPER_EXP = Column(Numeric(20, 4), comment='减:营业外支出')
    IL_NET_LOSS_DISP_NONCUR_ASSET = Column(Numeric(20, 4), comment='其中:减:非流动资产处置净损失')
    TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    INC_TAX = Column(Numeric(20, 4), comment='所得税')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认投资损失')
    NET_PROFIT_INCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(含少数股东损益)')
    NET_PROFIT_EXCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(不含少数股东损益)')
    MINORITY_INT_INC = Column(Numeric(20, 4), comment='少数股东损益')
    OTHER_COMPREH_INC = Column(Numeric(20, 4), comment='其他综合收益')
    TOT_COMPREH_INC = Column(Numeric(20, 4), comment='综合收益总额')
    TOT_COMPREH_INC_PARENT_COMP = Column(Numeric(20, 4), comment='综合收益总额(母公司)')
    TOT_COMPREH_INC_MIN_SHRHLDR = Column(Numeric(20, 4), comment='综合收益总额(少数股东)')
    S_FA_EPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益')
    S_FA_EPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    INSURANCE_EXPENSE = Column(Numeric(20, 4), comment='保险业务支出')
    SPE_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(特殊报表科目)')
    TOT_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(合计平衡项目)')
    SPE_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(特殊报表科目)')
    TOT_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(合计平衡项目)')
    SPE_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(特殊报表科目)')
    TOT_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(合计平衡项目)')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='年初未分配利润')
    ADJLOSSGAIN_PREVYEAR = Column(Numeric(20, 4), comment='调整以前年度损益')
    TRANSFER_FROM_SURPLUSRESERVE = Column(Numeric(20, 4), comment='盈余公积转入')
    TRANSFER_FROM_HOUSINGIMPREST = Column(Numeric(20, 4), comment='住房周转金转入')
    TRANSFER_FROM_OTHERS = Column(Numeric(20, 4), comment='其他转入')
    DISTRIBUTABLE_PROFIT = Column(Numeric(20, 4), comment='可分配利润')
    WITHDR_LEGALSURPLUS = Column(Numeric(20, 4), comment='提取法定盈余公积')
    WITHDR_LEGALPUBWELFUNDS = Column(Numeric(20, 4), comment='提取法定公益金')
    WORKERS_WELFARE = Column(Numeric(20, 4), comment='职工奖金福利')
    WITHDR_BUZEXPWELFARE = Column(Numeric(20, 4), comment='提取企业发展基金')
    WITHDR_RESERVEFUND = Column(Numeric(20, 4), comment='提取储备基金')
    DISTRIBUTABLE_PROFIT_SHRHDER = Column(Numeric(20, 4), comment='可供股东分配的利润')
    PRFSHARE_DVD_PAYABLE = Column(Numeric(20, 4), comment='应付优先股股利')
    WITHDR_OTHERSURPRESERVE = Column(Numeric(20, 4), comment='提取任意盈余公积金')
    COMSHARE_DVD_PAYABLE = Column(Numeric(20, 4), comment='应付普通股股利')
    CAPITALIZED_COMSTOCK_DIV = Column(Numeric(20, 4), comment='转作股本的普通股股利')
    AUDIT_AM = Column(Numeric(1, 0), comment='采用会计准则')
    OTHER_INCOME = Column(Numeric(20, 4), comment='其他收益')
    MEMO = Column(VARCHAR(1000), comment='备注')
    ASSET_DISPOSAL_INCOME = Column(Numeric(20, 4), comment='资产处置收益')
    CONTINUED_NET_PROFIT = Column(Numeric(20, 4), comment='持续经营净利润')
    END_NET_PROFIT = Column(Numeric(20, 4), comment='终止经营净利润')
    COMP_TYPE_CODE = Column(VARCHAR(2), comment='公司类型代码')
    CREDIT_IMPAIRMENT_LOSS = Column(Numeric(20, 4), comment='信用减值损失')
    NET_EXPOSURE_HEDGING_BENEFITS = Column(Numeric(20, 4), comment='净敞口套期收益')
    RD_EXPENSE = Column(Numeric(20, 4), comment='研发费用')
    STMNOTE_FINEXP = Column(Numeric(20, 4), comment='财务费用:利息费用')
    FIN_EXP_INT_INC = Column(Numeric(20, 4), comment='财务费用:利息收入')
    IS_CALCULATION = Column(Numeric(5, 0), comment='是否计算报表')
    EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    OTHER_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='其他资产减值损失')
    TOT_OPER_COST2 = Column(Numeric(20, 4), comment='营业总成本2')
    AMODCOST_FIN_ASSETS = Column(Numeric(20, 4), comment='以摊余成本计量的金融资产终止确认收益')


class CBONDINDEXEODCNBD(Base):
    """中债登指数行情"""
    __tablename__ = 'CBONDINDEXEODCNBD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='指数值')
    S_VAL_PE = Column(Numeric(20, 6), comment='指数总市值(亿元)')
    AVGMVDURATION = Column(Numeric(20, 4), comment='平均市值法久期')
    AVGCF = Column(Numeric(20, 4), comment='平均现金流法久期')
    AVG_VALUE_CONVEXITY = Column(Numeric(20, 4), comment='平均市值法凸性')
    AVG_CASH_CONVEXITY = Column(Numeric(20, 4), comment='平均现金流法凸性')
    AVG_CASH_YTM = Column(Numeric(20, 4), comment='平均现金流法到期收益率(%)')
    AVG_MATU = Column(Numeric(20, 4), comment='平均待偿期(年)')
    AVG_DIVIDEND_RATE = Column(Numeric(20, 4), comment='平均派息率(%)')
    AVG_VOBP = Column(Numeric(20, 4), comment='平均基点价值(元)')
    PENDING_TERM_CODE = Column(Numeric(9, 0), comment='待偿期限代码')
    SPOT_SETTLEMENT = Column(Numeric(20, 4), comment='现券结算量(亿元)')
    AVG_VALUE_YTM = Column(Numeric(20, 4), comment='平均市值法到期收益率')


class CBONDINDEXPERFORMANCE(Base):
    """中国债券指数业绩表现"""
    __tablename__ = 'CBONDINDEXPERFORMANCE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    PCT_CHG_RECENT1M = Column(Numeric(20, 6), comment='最近1月涨跌幅')
    PCT_CHG_RECENT3M = Column(Numeric(20, 6), comment='最近3月涨跌幅')
    PCT_CHG_RECENT6M = Column(Numeric(20, 6), comment='最近6月涨跌幅')
    PCT_CHG_RECENT1Y = Column(Numeric(20, 6), comment='最近1年涨跌幅')
    PCT_CHG_RECENT2Y = Column(Numeric(20, 6), comment='最近2年涨跌幅')
    PCT_CHG_RECENT3Y = Column(Numeric(20, 6), comment='最近3年涨跌幅')
    PCT_CHG_RECENT4Y = Column(Numeric(20, 6), comment='最近4年涨跌幅')
    PCT_CHG_RECENT5Y = Column(Numeric(20, 6), comment='最近5年涨跌幅')
    PCT_CHG_RECENT6Y = Column(Numeric(20, 6), comment='最近6年涨跌幅')
    PCT_CHG_THISWEEK = Column(Numeric(20, 6), comment='本周以来涨跌幅')
    PCT_CHG_THISMONTH = Column(Numeric(20, 6), comment='本月以来涨跌幅')
    PCT_CHG_THISQUARTER = Column(Numeric(20, 6), comment='本季以来涨跌幅')
    PCT_CHG_THISYEAR = Column(Numeric(20, 6), comment='本年以来涨跌幅')
    SI_PCT_CHG = Column(Numeric(20, 6), comment='发布以来涨跌幅')
    ANNUALYEILD = Column(Numeric(20, 6), comment='年化收益率')
    STD_DEV_6M = Column(Numeric(20, 6), comment='6个月标准差')
    STD_DEV_1Y = Column(Numeric(20, 6), comment='1年标准差')
    STD_DEV_2Y = Column(Numeric(20, 6), comment='2年标准差')
    STD_DEV_3Y = Column(Numeric(20, 6), comment='3年标准差')
    SHARPRATIO_6M = Column(Numeric(20, 6), comment='6个月夏普比率')
    SHARPRATIO_1Y = Column(Numeric(20, 6), comment='1年夏普比率')
    SHARPRATIO_2Y = Column(Numeric(20, 6), comment='2年夏普比率')
    SHARPRATIO_3Y = Column(Numeric(20, 6), comment='3年夏普比率')


class CBONDINDEXSCH(Base):
    """中国债券上海清算所指数行情"""
    __tablename__ = 'CBONDINDEXSCH'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='指数值')
    S_VAL_PE = Column(Numeric(20, 6), comment='指数总市值(亿元)')
    AVGMVDURATION = Column(Numeric(20, 4), comment='平均市值法久期')


class CBONDINDUSTRIESCODE(Base):
    """中国债券板块代码"""
    __tablename__ = 'CBONDINDUSTRIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCODE1 = Column(VARCHAR(38), comment='板块代码(父)')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='板块代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='板块名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')
    USED = Column(Numeric(1, 0), comment='是否有效')
    INDUSTRIESTYPE = Column(VARCHAR(50), comment='板块类型')


class CBONDINDUSTRIESCODEZL(Base):
    """中国债券板块代码(增量)"""
    __tablename__ = 'CBONDINDUSTRIESCODEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCODE1 = Column(VARCHAR(38), comment='板块代码(父)')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='板块代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='板块名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')
    USED = Column(Numeric(1, 0), comment='是否有效')
    INDUSTRIESTYPE = Column(VARCHAR(50), comment='板块类型')


class CBONDINDUSTRYCIRC(Base):
    """None"""
    __tablename__ = 'CBONDINDUSTRYCIRC'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(40), comment='一级板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='一级板块名称')
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(40), comment='二级板块代码')
    S_INFO_INDUSTRYNAME2 = Column(VARCHAR(100), comment='二级板块名称')


class CBONDINDUSTRYCIRCZL(Base):
    """保监会债券分类板块(增量)"""
    __tablename__ = 'CBONDINDUSTRYCIRCZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(40), comment='一级板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='一级板块名称')
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(40), comment='二级板块代码')
    S_INFO_INDUSTRYNAME2 = Column(VARCHAR(100), comment='二级板块名称')


class CBONDINDUSTRYCNBD(Base):
    """中国债券中债登债券分类板块"""
    __tablename__ = 'CBONDINDUSTRYCNBD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')


class CBONDINDUSTRYCNBDZL(Base):
    """中债债券分类板块(增量)"""
    __tablename__ = 'CBONDINDUSTRYCNBDZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')


class CBONDINDUSTRYNAFMII(Base):
    """NAFMII债券分类板块(增量)"""
    __tablename__ = 'CBONDINDUSTRYNAFMII'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(40), comment='一级板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='一级板块名称')
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(40), comment='二级板块代码')
    S_INFO_INDUSTRYNAME2 = Column(VARCHAR(100), comment='二级板块名称')


class CBONDINDUSTRYNAFMIIZL(Base):
    """NAFMII债券分类板块(增量)"""
    __tablename__ = 'CBONDINDUSTRYNAFMIIZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(40), comment='一级板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='一级板块名称')
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(40), comment='二级板块代码')
    S_INFO_INDUSTRYNAME2 = Column(VARCHAR(100), comment='二级板块名称')


class CBONDINDUSTRYSHC(Base):
    """中国债券上清所债券分类板块"""
    __tablename__ = 'CBONDINDUSTRYSHC'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')


class CBONDINDUSTRYSHCQL(Base):
    """None"""
    __tablename__ = 'CBONDINDUSTRYSHCQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20))
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100))


class CBONDINDUSTRYSHCZL(Base):
    """上清所债券分类板块(增量)"""
    __tablename__ = 'CBONDINDUSTRYSHCZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')


class CBONDINDUSTRYWIND(Base):
    """中国债券Wind分类板块"""
    __tablename__ = 'CBONDINDUSTRYWIND'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='一级板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='一级板块名称')
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(20), comment='二级板块代码')
    S_INFO_INDUSTRYNAME2 = Column(VARCHAR(100), comment='二级板块名称')


class CBONDINDUSTRYWINDQL(Base):
    """None"""
    __tablename__ = 'CBONDINDUSTRYWINDQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20))
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100))
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(20))
    S_INFO_INDUSTRYNAME2 = Column(VARCHAR(100))


class CBONDINDUSTRYWINDZL(Base):
    """中国Wind债券分类板块(增量)"""
    __tablename__ = 'CBONDINDUSTRYWINDZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='一级板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='一级板块名称')
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(20), comment='二级板块代码')
    S_INFO_INDUSTRYNAME2 = Column(VARCHAR(100), comment='二级板块名称')


class CBONDINSIDEHOLDER(Base):
    """中国债券发行主体前十大股东"""
    __tablename__ = 'CBONDINSIDEHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    B_HOLDER_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    B_HOLDER_HOLDERCATEGORY = Column(VARCHAR(1), comment='股东类型')
    B_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    B_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='持股数量')
    B_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例')
    B_HOLDER_SHARECATEGORY = Column(VARCHAR(40), comment='持股性质')
    B_HOLDER_ANAME = Column(VARCHAR(100), comment='股东名称')
    HOLDERID = Column(VARCHAR(40), comment='股东ID')


class CBONDINTERBANKMARKETRATECFETS(Base):
    """银行间市场基准利率参考指标"""
    __tablename__ = 'CBONDINTERBANKMARKETRATECFETS'
    __table_args__ = (
        Index('IDX_CBONDINTERBANKMARKETRATECFETS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_INFO_RATE = Column(Numeric(20, 4), comment='收盘利率')


class CBONDINTERESTRATECURVE(Base):
    """中国债券发行利率曲线"""
    __tablename__ = 'CBONDINTERESTRATECURVE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    B_ANAL_CURVENAME = Column(VARCHAR(100), comment='曲线名称')
    B_ANAL_CURVETYPE = Column(VARCHAR(40), comment='曲线类型')
    B_ANAL_CURVETERM = Column(Numeric(20, 4), comment='标准期限')
    B_ANAL_COUPONRATE = Column(Numeric(20, 4), comment='发行利率/利差')


class CBONDINTRODUCTION(Base):
    """中国债券公司简介(增量)"""
    __tablename__ = 'CBONDINTRODUCTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_PROVINCE = Column(VARCHAR(20), comment='省份')
    S_INFO_CITY = Column(VARCHAR(50), comment='城市')
    S_INFO_CHAIRMAN = Column(VARCHAR(50), comment='法人代表')
    S_INFO_PRESIDENT = Column(VARCHAR(38), comment='总经理')
    S_INFO_BDSECRETARY = Column(VARCHAR(500), comment='董事会秘书')
    S_INFO_REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    S_INFO_FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    S_INFO_CHINESEINTRODUCTION = Column(VARCHAR(2000), comment='公司中文简介')
    S_INFO_COMPTYPE = Column(VARCHAR(20), comment='公司类型')
    S_INFO_WEBSITE = Column(VARCHAR(160), comment='主页')
    S_INFO_EMAIL = Column(VARCHAR(160), comment='电子邮箱')
    S_INFO_OFFICE = Column(VARCHAR(800), comment='办公地址')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_COUNTRY = Column(VARCHAR(20), comment='国籍')
    S_INFO_BUSINESSSCOPE = Column(TEXT(2147483647), comment='经营范围')
    S_INFO_COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')


class CBONDINTRODUCTIONZL(Base):
    """中国债券公司简介(增量)"""
    __tablename__ = 'CBONDINTRODUCTIONZL'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_PROVINCE = Column(VARCHAR(20), comment='省份')
    S_INFO_CITY = Column(VARCHAR(50), comment='城市')
    S_INFO_CHAIRMAN = Column(VARCHAR(50), comment='法人代表')
    S_INFO_PRESIDENT = Column(VARCHAR(38), comment='总经理')
    S_INFO_BDSECRETARY = Column(VARCHAR(500), comment='董事会秘书')
    S_INFO_REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    S_INFO_FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    S_INFO_CHINESEINTRODUCTION = Column(VARCHAR(2000), comment='公司中文简介')
    S_INFO_COMPTYPE = Column(VARCHAR(20), comment='公司类型')
    S_INFO_WEBSITE = Column(VARCHAR(160), comment='主页')
    S_INFO_EMAIL = Column(VARCHAR(160), comment='电子邮箱')
    S_INFO_OFFICE = Column(VARCHAR(800), comment='办公地址')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_COUNTRY = Column(VARCHAR(20), comment='国籍')
    S_INFO_BUSINESSSCOPE = Column(TEXT(2147483647), comment='经营范围')
    S_INFO_COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')


class CBONDINVENTORYDETAILS(Base):
    """中国债券发行主体存货明细"""
    __tablename__ = 'CBONDINVENTORYDETAILS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    INV_OBJECT = Column(VARCHAR(100), comment='项目')
    INV_AMT = Column(Numeric(20, 4), comment='金额')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PROVISION = Column(Numeric(20, 4), comment='跌价准备')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报告类型代码')
    NET = Column(Numeric(20, 4), comment='净额')
    SUBJECT_NAME = Column(VARCHAR(20), comment='科目名称')


class CBONDINVESTMENTPEVC(Base):
    """中国债券公司投资PEVC基金"""
    __tablename__ = 'CBONDINVESTMENTPEVC'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='投资公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='投资公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='投资公司ID')
    S_HOLDER_DATE = Column(VARCHAR(10), comment='投资时间')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='股权比例')


class CBONDISSUER(Base):
    """中国债券发行主体"""
    __tablename__ = 'CBONDISSUER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='债券主体公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='债券主体公司id')
    USED = Column(Numeric(1, 0), comment='是否有效')
    S_INFO_COMPIND_CODE1 = Column(VARCHAR(50), comment='债券主体公司所属Wind一级行业代码')
    S_INFO_COMPIND_NAME1 = Column(VARCHAR(100), comment='债券主体公司所属Wind一级行业名称')
    S_INFO_COMPIND_CODE2 = Column(VARCHAR(50), comment='债券主体公司所属Wind二级行业代码')
    S_INFO_COMPIND_NAME2 = Column(VARCHAR(100), comment='债券主体公司所属Wind二级行业名称')
    S_INFO_COMPIND_CODE3 = Column(VARCHAR(50), comment='债券主体公司所属Wind三级行业代码')
    S_INFO_COMPIND_NAME3 = Column(VARCHAR(100), comment='债券主体公司所属Wind三级行业名称')
    S_INFO_COMPIND_CODE4 = Column(VARCHAR(50), comment='债券主体公司所属Wind四级行业代码')
    S_INFO_COMPIND_NAME4 = Column(VARCHAR(100), comment='债券主体公司所属Wind四级行业名称')
    S_INFO_COMPREGADDRESS = Column(VARCHAR(80), comment='债券主体公司国籍(注册地)')
    S_INFO_COMPTYPE = Column(VARCHAR(40), comment='债券主体类型')
    S_INFO_LISTCOMPORNOT = Column(Numeric(1, 0), comment='是否上市公司')
    S_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    S_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期')
    B_AGENCY_GUARANTORNATURE = Column(VARCHAR(40), comment='公司属性')
    IS_FIN_INST = Column(Numeric(1, 0), comment='是否金融机构')
    S_INFO_TYPECODE = Column(Numeric(9, 0), comment='关系类型代码')


class CBONDISSUERMANAGEMENT(Base):
    """中国债券发行主体管理层成员"""
    __tablename__ = 'CBONDISSUERMANAGEMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_GENDER = Column(VARCHAR(10), comment='性别代码')
    S_INFO_MANAGER_EDUCATION = Column(VARCHAR(10), comment='学历')
    S_INFO_MANAGER_NATIONALITY = Column(VARCHAR(40), comment='国籍')
    S_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(8), comment='出生日期')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8), comment='离职日期')
    S_INFO_MANAGER_TYPE = Column(Numeric(5, 0), comment='管理层类别')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='公布职务名称')
    S_INFO_MANAGER_INTRODUCTION = Column(VARCHAR(2000), comment='个人简历')
    MANID = Column(VARCHAR(10), comment='人物id')
    DISPLAY_ORDER = Column(Numeric(4, 0), comment='展示顺序')


class CBONDISSUEROFFICECITY(Base):
    """中国债券主体国内办公城市(海外)"""
    __tablename__ = 'CBONDISSUEROFFICECITY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    WIND_IND_CODE = Column(VARCHAR(50), comment='所属板块代码')
    WIND_IND_NAME = Column(VARCHAR(50), comment='板块名称')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CBONDISSUERQL(Base):
    """None"""
    __tablename__ = 'CBONDISSUERQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_COMPNAME = Column(VARCHAR(100))
    S_INFO_COMPCODE = Column(VARCHAR(10))
    USED = Column(Numeric(1, 0))
    S_INFO_COMPIND_CODE1 = Column(VARCHAR(50))
    S_INFO_COMPIND_NAME1 = Column(VARCHAR(100))
    S_INFO_COMPIND_CODE2 = Column(VARCHAR(50))
    S_INFO_COMPIND_NAME2 = Column(VARCHAR(100))
    S_INFO_COMPIND_CODE3 = Column(VARCHAR(50))
    S_INFO_COMPIND_NAME3 = Column(VARCHAR(100))
    S_INFO_COMPIND_CODE4 = Column(VARCHAR(50))
    S_INFO_COMPIND_NAME4 = Column(VARCHAR(100))
    S_INFO_COMPREGADDRESS = Column(VARCHAR(80))
    S_INFO_COMPTYPE = Column(VARCHAR(40))
    S_INFO_LISTCOMPORNOT = Column(Numeric(1, 0))
    S_INFO_EFFECTIVE_DT = Column(VARCHAR(8))
    S_INFO_INVALID_DT = Column(VARCHAR(8))
    B_AGENCY_GUARANTORNATURE = Column(VARCHAR(40))
    IS_FIN_INST = Column(Numeric(1, 0))
    S_INFO_TYPECODE = Column(Numeric(9, 0))


class CBONDISSUERRATING(Base):
    """中国债券发行主体信用评级"""
    __tablename__ = 'CBONDISSUERRATING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司中文名称')
    ANN_DT = Column(VARCHAR(8), comment='评级日期')
    B_RATE_STYLE = Column(VARCHAR(100), comment='评级类型')
    B_INFO_CREDITRATING = Column(VARCHAR(40), comment='信用评级')
    B_RATE_RATINGOUTLOOK = Column(Numeric(9, 0), comment='评级展望')
    B_INFO_CREDITRATINGAGENCY = Column(VARCHAR(10), comment='评级机构代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='债券主体公司id')
    B_INFO_CREDITRATINGEXPLAIN = Column(VARCHAR(1000), comment='信用评级说明')
    B_INFO_PRECREDITRATING = Column(VARCHAR(40), comment='前次信用评级')
    B_CREDITRATING_CHANGE = Column(VARCHAR(10), comment='评级变动方向')
    B_INFO_ISSUERRATETYPE = Column(Numeric(9, 0), comment='评级对象类型代码')
    ANN_DT2 = Column(VARCHAR(8), comment='公告日期')


class CBONDISSUERRATINGWATCHLIST(Base):
    """中国债券主体信用评级观察名单明细"""
    __tablename__ = 'CBONDISSUERRATINGWATCHLIST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_SUBJECT_ID = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    B_EVENT_HAPDATE = Column(VARCHAR(8), comment='发生日期')
    B_EVENT_CATEGORYCODE = Column(Numeric(9, 0), comment='事件类型代码')
    B_EVENT_CATEGORY = Column(VARCHAR(80), comment='事件类型名称')
    B_EVENT_TITLE = Column(VARCHAR(400), comment='事件标题')
    B_ANN_ABSTRACT = Column(VARCHAR(3000), comment='公告摘要')


class CBONDISSUERZL(Base):
    """中国债券主体(增量)"""
    __tablename__ = 'CBONDISSUERZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='债券主体公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='债券主体公司id')
    USED = Column(Numeric(1, 0), comment='是否有效')
    S_INFO_COMPIND_CODE1 = Column(VARCHAR(50), comment='债券主体公司所属Wind一级行业代码')
    S_INFO_COMPIND_NAME1 = Column(VARCHAR(100), comment='债券主体公司所属Wind一级行业名称')
    S_INFO_COMPIND_CODE2 = Column(VARCHAR(50), comment='债券主体公司所属Wind二级行业代码')
    S_INFO_COMPIND_NAME2 = Column(VARCHAR(100), comment='债券主体公司所属Wind二级行业名称')
    S_INFO_COMPIND_CODE3 = Column(VARCHAR(50), comment='债券主体公司所属Wind三级行业代码')
    S_INFO_COMPIND_NAME3 = Column(VARCHAR(100), comment='债券主体公司所属Wind三级行业名称')
    S_INFO_COMPIND_CODE4 = Column(VARCHAR(50), comment='债券主体公司所属Wind四级行业代码')
    S_INFO_COMPIND_NAME4 = Column(VARCHAR(100), comment='债券主体公司所属Wind四级行业名称')
    S_INFO_COMPREGADDRESS = Column(VARCHAR(80), comment='债券主体公司国籍(注册地)')
    S_INFO_COMPTYPE = Column(VARCHAR(40), comment='债券主体类型')
    S_INFO_LISTCOMPORNOT = Column(Numeric(1, 0), comment='是否上市公司')
    S_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    S_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期')
    B_AGENCY_GUARANTORNATURE = Column(VARCHAR(40), comment='公司属性')
    IS_FIN_INST = Column(Numeric(1, 0), comment='是否金融机构')
    S_INFO_TYPECODE = Column(Numeric(9, 0), comment='关系类型代码')


class CBONDISSUINGDATEPREDICT(Base):
    """中国债券发行主体定期报告披露日期"""
    __tablename__ = 'CBONDISSUINGDATEPREDICT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_STM_PREDICT_ISSUINGDATE = Column(VARCHAR(8), comment='预计披露日期')
    S_STM_ACTUAL_ISSUINGDATE = Column(VARCHAR(8), comment='实际披露日期')


class CBONDLEADUNDERWRITER(Base):
    """中国债券发行主承销商承销金额"""
    __tablename__ = 'CBONDLEADUNDERWRITER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    MEETING_DT = Column(VARCHAR(8), comment='发审委会议日期')
    PASS_DT = Column(VARCHAR(8), comment='发审委通过公告日')
    S_LU_ANNISSUEDATE = Column(VARCHAR(8), comment='发行公告日')
    S_LU_ISSUEDATE = Column(VARCHAR(8), comment='发行日期')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期(债券起息日)')
    S_LU_ISSUETYPE = Column(VARCHAR(30), comment='发行类型')
    BONDTYPE = Column(VARCHAR(40), comment='辅助类型')
    S_LU_TOTALISSUECOLLECTION = Column(Numeric(20, 4), comment='募集资金合计(万元)')
    NETCOLLECTION = Column(Numeric(20, 4), comment='实际募资金额(万元)')
    AVG_TOTALCOLL = Column(Numeric(20, 4), comment='募集资金合计(平均分配)')
    AVG_NETCOLL = Column(Numeric(20, 4), comment='实际募资金额(平均分配)')
    S_LU_TOTALISSUEEXPENSES = Column(Numeric(20, 4), comment='发行费用合计(万元)')
    S_LU_TOTALUDERANDSPONEFEE = Column(Numeric(20, 4), comment='承销与保荐费用(万元)')
    ALL_LU = Column(VARCHAR(1900), comment='参与主承销商名称')
    S_LU_NUMBER = Column(Numeric(5, 0), comment='参与主承销商个数')
    S_LU_NAME = Column(VARCHAR(100), comment='主承销商名称')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='主承销商公司ID')
    S_LU_INSTITYPE = Column(VARCHAR(40), comment='机构类型')
    S_IS_STATISTICS = Column(Numeric(1, 0), comment='是否参与统计')


class CBONDLOANDETAILS(Base):
    """中国债券发行主体贷款明细"""
    __tablename__ = 'CBONDLOANDETAILS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    LOAN_TYPE = Column(VARCHAR(80), comment='贷款类型')
    LOAN_CNY = Column(Numeric(20, 4), comment='人民币贷款')
    LOAN_USD = Column(Numeric(20, 4), comment='美元贷款(折算人民币)')
    LOAN_JPY = Column(Numeric(20, 4), comment='日元贷款(折算人民币)')
    LOAN_EUR = Column(Numeric(20, 4), comment='欧元贷款(折算人民币)')
    LOAN_HKD = Column(Numeric(20, 4), comment='港币贷款(折算人民币)')
    LOAN_GBP = Column(Numeric(20, 4), comment='英镑贷款(折算人民币)')
    LOAN_OTHER = Column(Numeric(20, 4), comment='其他货币贷款(折算人民币)')
    LOAN_TOT = Column(Numeric(20, 4), comment='贷款合计')


class CBONDLONGLOAN(Base):
    """中国债券公司长期借款"""
    __tablename__ = 'CBONDLONGLOAN'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='债务公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='债务公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='债务公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class CBONDMAINANDNOTEITEMS(Base):
    """None"""
    __tablename__ = 'CBONDMAINANDNOTEITEMS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(10), comment='Wind代码')
    SEQUENCE1 = Column(Numeric(6, 0), comment='顺序编号')
    ACCOUNTS_ID = Column(VARCHAR(20), comment='科目ID')
    IS_NOT_NULL = Column(Numeric(1, 0), comment='是否非空')
    IS_SHOW = Column(Numeric(1, 0), comment='是否展示')
    S_INFO_TYPECODE = Column(Numeric(9, 0), comment='报表品种代码')
    SUBJECT_CHINESE_NAME = Column(VARCHAR(100), comment='科目中文名')


class CBONDMAJOREVENT(Base):
    """中国债券重大事件汇总"""
    __tablename__ = 'CBONDMAJOREVENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_EVENT_CATEGORYCODE = Column(Numeric(9, 0), comment='事件类型代码')
    S_EVENT_ANNCEDATE = Column(VARCHAR(8), comment='披露日期')
    S_EVENT_HAPDATE = Column(VARCHAR(8), comment='发生日期')
    S_EVENT_EXPDATE = Column(VARCHAR(8), comment='失效日期')
    S_EVENT_CONTENT = Column(VARCHAR, comment='事件内容')
    S_EVENT_TEMPLATEID = Column(Numeric(12, 0), comment='模板ID')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class CBONDMAJORRECEIVABLES(Base):
    """中国债券发行主体主要其它应收款明细"""
    __tablename__ = 'CBONDMAJORRECEIVABLES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    DEBTOR_NAME = Column(VARCHAR(100), comment='债务人名称')
    ARREARS = Column(Numeric(20, 4), comment='金额')
    DELAYTIME = Column(VARCHAR(40), comment='拖欠时间')
    DELAYREASON = Column(VARCHAR(100), comment='拖欠原因')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')


class CBONDMANAGEMENTHOLDREWARD(Base):
    """中国债券发行主体管理层持股及报酬"""
    __tablename__ = 'CBONDMANAGEMENTHOLDREWARD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    END_DATE = Column(VARCHAR(8), comment='截止日期')
    CRNY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_POST = Column(VARCHAR(300), comment='职务')
    S_MANAGER_RETURN = Column(Numeric(20, 4), comment='报酬')
    S_MANAGER_QUANTITY = Column(Numeric(20, 4), comment='持股数量')
    MANID = Column(VARCHAR(10), comment='人物ID')
    S_MANAGER_RETURN_OTHER = Column(Numeric(5, 0), comment='是否在股东或关联单位领取报酬、津贴')


class CBONDMECHANISMOWNERSHIP(Base):
    """中国债券公司机构持股"""
    __tablename__ = 'CBONDMECHANISMOWNERSHIP'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='股东公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='股东公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='股东公司ID')
    S_HOLDER_ENDDATE = Column(VARCHAR(10), comment='报告期')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例')


class CBONDMERGERSUBJECT(Base):
    """中国债券公司并购标的"""
    __tablename__ = 'CBONDMERGERSUBJECT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='并购公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='并购公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='并购公司ID')
    S_INFO_PROGRESS = Column(VARCHAR(300), comment='方案进度')
    S_UPDATE_DATE = Column(VARCHAR(8), comment='最新披露日期')
    S_MEETEVENT_ID = Column(VARCHAR(20), comment='事件ID')
    S_INFO_COMP_NAME1 = Column(VARCHAR(100), comment='并购目标公司名称')
    S_INFO_COMP_SNAME1 = Column(VARCHAR(40), comment='并购目标公司中文简称')


class CBONDMONETARYFUNDS(Base):
    """中国债券发行主体货币资金明细"""
    __tablename__ = 'CBONDMONETARYFUNDS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_RMB = Column(Numeric(20, 4), comment='人民币')
    S_US = Column(Numeric(20, 4), comment='美元(折算人民币)')
    S_JPY = Column(Numeric(20, 4), comment='日元(折算人民币)')
    S_EUR = Column(Numeric(20, 4), comment='欧元(折算人民币)')
    S_HKD = Column(Numeric(20, 4), comment='港币(折算人民币)')
    S_GBP = Column(Numeric(20, 4), comment='英镑(折算人民币)')
    S_OTHER = Column(Numeric(20, 4), comment='其他货币(折算人民币)')
    CAPITAL_TOT = Column(Numeric(20, 4), comment='货币资金合计')


class CBONDNEGATIVECREDITEVENT(Base):
    """中国债券负面事件"""
    __tablename__ = 'CBONDNEGATIVECREDITEVENT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='wind代码')
    ACU_DATE = Column(VARCHAR(8), comment='[内部]发生日期')
    EVENT_TYPE = Column(Numeric(9, 0), comment='事件类型')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    SUBJECT_TYPE = Column(Numeric(9, 0), comment='主体类型代码')
    EVENT_TITLE = Column(VARCHAR(400), comment='事件标题 ')
    EVENT_MEMO = Column(VARCHAR(3000), comment='事件摘要 ')


class CBONDNEINDUSTRIESCLASS(Base):
    """中国债券国民经济行业分类"""
    __tablename__ = 'CBONDNEINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    NE_IND_CODE = Column(VARCHAR(50), comment='国民经济行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class CBONDNINDUSTRYWIND(Base):
    """中国Wind债券分类板块(新)"""
    __tablename__ = 'CBONDNINDUSTRYWIND'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='所属板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CBONDNONPROFITLOSS(Base):
    """中国债券发行主体非经常性损益"""
    __tablename__ = 'CBONDNONPROFITLOSS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    NON_CURRENT_GAINS_LOSSES = Column(Numeric(20, 4), comment='非流动资产处置损益')
    TAX_RETURN = Column(Numeric(20, 4), comment='税收返还减免')
    GOVERNMENT_SUBSIDY = Column(Numeric(20, 4), comment='政府补助')
    CAPITAL_OCCUPATION_FEE = Column(Numeric(20, 4), comment='资金占用费')
    CONSOLIDATED_GAINS_LOSSES = Column(Numeric(20, 4), comment='企业合并产生的损益')
    NON_ASSETS_GAINS_LOSSES = Column(Numeric(20, 4), comment='非货币性资产交换损益')
    INVESTMENT_GAINS_LOSSES = Column(Numeric(20, 4), comment='委托投资损益')
    IMPAIRMENT_ASSETS = Column(Numeric(20, 4), comment='资产减值准备')
    DEBT_RESTRUCTURING = Column(Numeric(20, 4), comment='债务重组损益')
    ENTERPRISE_RESTRUCTURING = Column(Numeric(20, 4), comment='企业重组费用')
    TRADING_PRICE_UNFAIR = Column(Numeric(20, 4), comment='交易价格显失公允产生的损益')
    NET_PROFIT_LOSS_SUBSIDIARIES = Column(Numeric(20, 4), comment='同一控制下企业合并产生的子公司净损益')
    EXPECTED_LIABILITIES = Column(Numeric(20, 4), comment='预计负债产生的损益')
    ONOIAE = Column(Numeric(20, 4), comment='其他营业外收支净额')
    OTHER_PROJECTS = Column(Numeric(20, 4), comment='其他项目')
    NON_RECURRING_GAINS_LOSSES = Column(Numeric(20, 4), comment='非经常性损益项目小计')
    INCOME_TAX_IMPACT = Column(Numeric(20, 4), comment='所得税影响数')
    PROFIT_LOSS_SHAREHOLDERS = Column(Numeric(20, 4), comment='少数股东损益影响数')
    NON_RECURRING_GAINS_LOSSES1 = Column(Numeric(20, 4), comment='非经常性损益项目合计')
    S_FA_DEDUCTEDPROFITTOPROFIT = Column(Numeric(20, 4), comment='扣除非经常损益后的净利润')
    S_FA_DEDUCTEDPROFITTOPROFIT1 = Column(Numeric(20, 4), comment='扣除非经常损益后的归属公司股东的净利润')
    FAIRVALUE_CHANGE_GAINS_LOSSES = Column(Numeric(20, 4), comment='持有(或处置)交易性金融资产和负债产生的公允价值变动损益')
    PROVISION_IMPAIRMENT_REVERSED = Column(Numeric(20, 4), comment='单独进行监制测试的应收款项减值准备转回')
    PROCEEDS_LOAN = Column(Numeric(20, 4), comment='对外委托贷款取得的收益')
    CHANGES_REAL_ESTATE_VALUE = Column(Numeric(20, 4), comment='公允价值法计量的投资性房地产价值变动损益')
    PROFIT_LOSS_ADJUSTMENT = Column(Numeric(20, 4), comment='法规要求一次性损益调整影响')
    CUSTODY_FEE_INCOME = Column(Numeric(20, 4), comment='受托经营取得的托管费收入')
    IS_PUBLISHED = Column(Numeric(1, 0), comment='是否公布')


class CBONDOLDSECINDUSTRIESCLASS(Base):
    """中国债券证监会行业分类(旧)"""
    __tablename__ = 'CBONDOLDSECINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='证监会行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CBONDOLDSECINDUSTRIESCLASSQL(Base):
    """None"""
    __tablename__ = 'CBONDOLDSECINDUSTRIESCLASSQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    SEC_IND_CODE = Column(VARCHAR(50))
    ENTRY_DT = Column(VARCHAR(8))
    REMOVE_DT = Column(VARCHAR(8))
    CUR_SIGN = Column(Numeric(1, 0))


class CBONDOLDSECINDUSTRIESCLASSZL(Base):
    """中国债券证监会行业分类(旧)(增量)"""
    __tablename__ = 'CBONDOLDSECINDUSTRIESCLASSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='证监会行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CBONDOTHERACCOUNTSRECEIVABLE(Base):
    """中国债券发行主体其它应收款帐龄结构"""
    __tablename__ = 'CBONDOTHERACCOUNTSRECEIVABLE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    AGING = Column(VARCHAR(30), comment='账龄')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    OTH_RCV = Column(Numeric(20, 4), comment='金额')
    OTH_RCV_PCT = Column(Numeric(20, 4), comment='比例')
    EXTRA_AMOUNT = Column(Numeric(20, 4), comment='坏账准备')
    MIN_AGING = Column(Numeric(20, 4), comment='最小账龄')
    MAX_AGING = Column(Numeric(20, 4), comment='最大账龄')


class CBONDOTHERRECEIVABLES(Base):
    """中国债券发行主体其它应收款大股东欠款"""
    __tablename__ = 'CBONDOTHERRECEIVABLES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    DEBTOR_NAME = Column(VARCHAR(100), comment='债务人名称')
    ARREARS = Column(Numeric(20, 4), comment='金额')
    OTH_RCV_PCT = Column(Numeric(20, 4), comment='比例(%)')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')


class CBONDPAYMENT(Base):
    """中国债券付息和兑付"""
    __tablename__ = 'CBONDPAYMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_ANNOUNCEMENTDATE = Column(VARCHAR(8), comment='公告日期')
    S_DIV_RECORDDATE = Column(VARCHAR(8), comment='债权登记日')
    S_DIV_EXDATE = Column(VARCHAR(8), comment='除息日')
    B_INFO_PAYMENTDATE = Column(VARCHAR(8), comment='付息日')
    B_INFO_INTERESTPERTHOUSANDS = Column(Numeric(28, 11), comment='每手付息数')
    B_INFO_PRINCIPALPERTHOUSANDS = Column(Numeric(28, 11), comment='每手兑付本金数')
    B_INFO_PRINCIPALAFTERTAX = Column(Numeric(28, 11), comment='税后每手付息数')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    B_INFO_REDEEM_NET_PRICE = Column(Numeric(28, 12), comment='每百元提前兑付/赎回净价')


class CBONDPEVCINVESTMENT(Base):
    """中国债券公司PEVC投资机构"""
    __tablename__ = 'CBONDPEVCINVESTMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='股东公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='股东公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='股东公司ID')
    S_HOLDER_DATE = Column(VARCHAR(8), comment='融资时间')
    S_HOLDER_PCT = Column(Numeric(12, 4), comment='股权比例')


class CBONDPLACEMENTDETAILS(Base):
    """中国债券配售机构获配明细"""
    __tablename__ = 'CBONDPLACEMENTDETAILS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='证券ID')
    TYPEOFINVESTOR = Column(VARCHAR(20), comment='法人投资者类型')
    INVESTOR_NAME = Column(VARCHAR(1000), comment='法人投资者')
    INVESTOR_ID = Column(VARCHAR(10), comment='法人投资者ID')
    PLACEMENT = Column(Numeric(20, 4), comment='获配数量(万股/万张)')
    LOCKMONTH = Column(Numeric(20, 4), comment='冻结期限(月)')
    ANN_ORDQTY = Column(Numeric(20, 4), comment='实际申购数量')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    TRADE_DT = Column(VARCHAR(8), comment='配售截止日期')
    REFUND_PAYBACK_AMOUNT = Column(Numeric(20, 4), comment='退款或补缴金额')
    SHARE_TYPE = Column(VARCHAR(50), comment='股份类型')
    TRADABLE_DT = Column(VARCHAR(8), comment='可流通日期')
    LATEST_OWN_QTY = Column(Numeric(20, 4), comment='最新持股数量')
    LATEST_OWN_QTY_FINANCING = Column(Numeric(20, 4), comment='最新持股数量(配套融资)')
    INVESTOR_TYPE_CODE = Column(Numeric(9, 0), comment='投资者类型代码')


class CBONDPLAINTIFF(Base):
    """中国债券公司诉讼-原告"""
    __tablename__ = 'CBONDPLAINTIFF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='诉讼公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='诉讼公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='诉讼公司ID')
    S_INFO_CASE_TYPE = Column(VARCHAR(10), comment='案件类型')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    LITIGATION_EVENTS_ID = Column(VARCHAR(40), comment='诉讼事件ID')


class CBONDPLATEWIND(Base):
    """中国债券Wind概念板块"""
    __tablename__ = 'CBONDPLATEWIND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')


class CBONDPLATEWINDQL(Base):
    """None"""
    __tablename__ = 'CBONDPLATEWINDQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20))
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100))


class CBONDPLATEWINDZL(Base):
    """中国Wind债券概念板块(增量)"""
    __tablename__ = 'CBONDPLATEWINDZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')


class CBONDPREPODESCRIPTION(Base):
    """回购基本资料"""
    __tablename__ = 'CBONDPREPODESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SUBJECTWINDCODE = Column(VARCHAR(40), comment='标的债券Wind代码')
    B_INFO_REPO_TYPE = Column(VARCHAR(40), comment='回购类型')
    B_INFO_REPO_DAYS = Column(Numeric(5, 0), comment='回购天数')
    B_INFO_REPO_FIRSTDATE = Column(VARCHAR(8), comment='首次交易日期')
    B_INFO_REPO_PCNTBOND = Column(Numeric(20, 4), comment='履约金比例')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    REPO_DAYS = Column(VARCHAR(40), comment='期限')
    S_INFO_FULLNAME = Column(VARCHAR(200), comment='证券全称')
    S_INFO_TYPE = Column(Numeric(9, 0), comment='品种类别代码')
    S_INFO_TYPENAME = Column(VARCHAR(200), comment='品种类别名称')
    SECURITY_STATUS = Column(Numeric(9, 0), comment='存续状态')
    CRNCY_NAME = Column(VARCHAR(10), comment='交易货币代码')


class CBONDPREPODESCRIPTIONZL(Base):
    """中国债券回购基本资料(增量)"""
    __tablename__ = 'CBONDPREPODESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SUBJECTWINDCODE = Column(VARCHAR(40), comment='标的债券Wind代码')
    B_INFO_REPO_TYPE = Column(VARCHAR(40), comment='回购类型')
    B_INFO_REPO_DAYS = Column(Numeric(5, 0), comment='回购天数')
    B_INFO_REPO_FIRSTDATE = Column(VARCHAR(8), comment='首次交易日期')
    B_INFO_REPO_PCNTBOND = Column(Numeric(20, 4), comment='履约金比例')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    REPO_DAYS = Column(VARCHAR(40), comment='期限')
    S_INFO_FULLNAME = Column(VARCHAR(200), comment='证券全称')
    S_INFO_TYPE = Column(Numeric(9, 0), comment='品种类别代码')
    S_INFO_TYPENAME = Column(VARCHAR(200), comment='品种类别名称')
    SECURITY_STATUS = Column(Numeric(9, 0), comment='存续状态')
    CRNCY_NAME = Column(VARCHAR(10), comment='交易货币代码')


class CBONDPRERELEASE(Base):
    """中国债券国债预发行资料"""
    __tablename__ = 'CBONDPRERELEASE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    PRE_RELEASE_CODE = Column(VARCHAR(10), comment='预发行代码')
    PRE_RELEASE_NAME = Column(VARCHAR(40), comment='预发行简称')
    PRE_RELEASE_BEGINDATE = Column(VARCHAR(8), comment='预发行交易起始日')
    PRE_RELEASE_ENDDATE = Column(VARCHAR(8), comment='预发行交易截止日')
    S_BASE_INFO = Column(Numeric(24, 8), comment='基准价格/收益率')
    B_ANAL_RDURATION = Column(Numeric(24, 8), comment='参考久期')
    PRICE_TYPE_CODE = Column(Numeric(9, 0), comment='价格类型代码')


class CBONDPRERELEASEZL(Base):
    """中国债券预发行资料(增量)"""
    __tablename__ = 'CBONDPRERELEASEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    PRE_RELEASE_CODE = Column(VARCHAR(10), comment='预发行代码')
    PRE_RELEASE_NAME = Column(VARCHAR(40), comment='预发行简称')
    PRE_RELEASE_BEGINDATE = Column(VARCHAR(8), comment='预发行交易起始日')
    PRE_RELEASE_ENDDATE = Column(VARCHAR(8), comment='预发行交易截止日')
    S_BASE_INFO = Column(Numeric(24, 8), comment='基准价格/收益率')
    B_ANAL_RDURATION = Column(Numeric(24, 8), comment='参考久期')
    PRICE_TYPE_CODE = Column(Numeric(9, 0), comment='价格类型代码')


class CBONDPREVIOUSNAME(Base):
    """中国债券曾用名"""
    __tablename__ = 'CBONDPREVIOUSNAME'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截至日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    CHANGEREASON = Column(Numeric(9, 0), comment='变动原因代码')


class CBONDPRICES(Base):
    """中国债券行情-全价"""
    __tablename__ = 'CBONDPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_DQ_OPEN = Column(Numeric(20, 8), comment='开盘价(元)')
    B_DQ_HIGH = Column(Numeric(20, 8), comment='最高价(元)')
    B_DQ_LOW = Column(Numeric(20, 8), comment='最低价(元)')
    B_DQ_ORIGINCLOSE = Column(Numeric(20, 8), comment='收盘价(元)')
    B_DQ_VOLUME = Column(Numeric(20, 8), comment='成交量(手)')
    B_DQ_AMOUNT = Column(Numeric(20, 8), comment='成交金额(千元)')


class CBONDPRICESIRS(Base):
    """利率互换行情"""
    __tablename__ = 'CBONDPRICESIRS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID ')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    B_INFO_IRSTYPE = Column(Numeric(9, 0), comment='利率互换类型')
    B_INFO_REFERENCERATE1 = Column(VARCHAR(90), comment='参考利率1')
    B_INFO_REFERENCERATE2 = Column(VARCHAR(90), comment='参考利率2')
    B_INFO_TERM = Column(VARCHAR(300), comment='期限')
    B_DQ_PRECLOSE = Column(Numeric(20, 10), comment='利率1前收盘价 ')
    B_DQ_PREAVGPRICE = Column(Numeric(20, 10), comment='利率1加权平均前收盘价 ')
    B_DQ_OPEN = Column(Numeric(20, 10), comment='利率1开盘价 ')
    B_DQ_HIGH = Column(Numeric(20, 10), comment='利率1最高价 ')
    B_DQ_LOW = Column(Numeric(20, 10), comment='利率1最低价 ')
    B_DQ_CLOSE = Column(Numeric(20, 10), comment='利率1收盘价 ')
    B_DQ_AVGPRICE = Column(Numeric(20, 10), comment='利率1加权平均收盘价 ')
    B_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额 ')


class CBONDPRICESNET(Base):
    """中国债券行情-净价"""
    __tablename__ = 'CBONDPRICESNET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_DQ_OPEN = Column(Numeric(20, 8), comment='开盘价(元)')
    B_DQ_HIGH = Column(Numeric(20, 8), comment='最高价(元)')
    B_DQ_LOW = Column(Numeric(20, 8), comment='最低价(元)')
    B_DQ_ORIGINCLOSE = Column(Numeric(20, 8), comment='收盘价(元)')
    B_DQ_VOLUME = Column(Numeric(20, 8), comment='成交量(手)')
    B_DQ_AMOUNT = Column(Numeric(20, 8), comment='成交金额(千元)')


class CBONDPRICESREPO(Base):
    """中国债券存款机构间回购行情"""
    __tablename__ = 'CBONDPRICESREPO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='记录ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘(%)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高(%)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低(%)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘(%)')
    S_DQ_AVGPRICE = Column(Numeric(20, 4), comment='加权平均(%)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')


class CBONDPRICINGVALUATION(Base):
    """中国债券评级定价估值(银行间)"""
    __tablename__ = 'CBONDPRICINGVALUATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    VAL_AGENCY = Column(VARCHAR(40), comment='估值机构')
    VAL_AGENCY_ID = Column(VARCHAR(10), comment='估值机构id')
    CREDIT_CODE = Column(Numeric(9, 0), comment='信用评级代码')
    TERM = Column(Numeric(20, 4), comment='期限')
    VALUATION = Column(Numeric(20, 4), comment='定价估值')


class CBONDPRODUCT(Base):
    """中国债券公司产品"""
    __tablename__ = 'CBONDPRODUCT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')
    S_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_PRODUCT_NAME = Column(VARCHAR(100), comment='产品名称')


class CBONDPROVISIONBADDEBTS(Base):
    """中国债券发行主体坏帐准备提取比例"""
    __tablename__ = 'CBONDPROVISIONBADDEBTS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    AGING = Column(VARCHAR(70), comment='账龄')
    EXTRACTION_RATIO = Column(Numeric(20, 4), comment='提取比例')
    MIN_AGING = Column(Numeric(20, 4), comment='最小账龄')
    MAX_AGING = Column(Numeric(20, 4), comment='最大账龄')


class CBONDPUT(Base):
    """中国债券回售条款执行说明"""
    __tablename__ = 'CBONDPUT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REPURCHASEDATE = Column(VARCHAR(8), comment='回售资金到帐日')
    B_INFO_REPURCHASEPRICE = Column(Numeric(20, 4), comment='每百元面值回售价格(元)')
    B_INFO_PUTANNOUNCEMENTDATE = Column(VARCHAR(8), comment='回售公告日')
    B_INFO_PUTEXDATE = Column(VARCHAR(8), comment='回售履行结果公告日')
    B_INFO_PUTAMOUNT = Column(Numeric(20, 4), comment='回售总面额(亿元)')
    B_INFO_PUTOUTSTANDING = Column(Numeric(20, 4), comment='继续托管总面额(亿元)')
    B_INFO_REPURCHASESTARTDATE = Column(VARCHAR(8), comment='回售行使开始日')
    B_INFO_REPURCHASEENDDATE = Column(VARCHAR(8), comment='回售行使截止日')
    B_INFO_FUNDENDDATE = Column(VARCHAR(8), comment='回售日 ')
    B_INFO_REPURCHASECODE = Column(VARCHAR(40), comment='回售代码')


class CBONDPUTQL(Base):
    """None"""
    __tablename__ = 'CBONDPUTQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    B_INFO_REPURCHASEDATE = Column(VARCHAR(8))
    B_INFO_REPURCHASEPRICE = Column(Numeric(20, 4))
    B_INFO_PUTANNOUNCEMENTDATE = Column(VARCHAR(8))
    B_INFO_PUTEXDATE = Column(VARCHAR(8))
    B_INFO_PUTAMOUNT = Column(Numeric(20, 4))
    B_INFO_PUTOUTSTANDING = Column(Numeric(20, 4))
    B_INFO_REPURCHASESTARTDATE = Column(VARCHAR(8))
    B_INFO_REPURCHASEENDDATE = Column(VARCHAR(8))
    B_INFO_FUNDENDDATE = Column(VARCHAR(8))
    B_INFO_REPURCHASECODE = Column(VARCHAR(40))


class CBONDPUTZL(Base):
    """中国债券回售条款执行说明(增量)"""
    __tablename__ = 'CBONDPUTZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REPURCHASEDATE = Column(VARCHAR(8), comment='回售资金到帐日')
    B_INFO_REPURCHASEPRICE = Column(Numeric(20, 4), comment='每百元面值回售价格(元)')
    B_INFO_PUTANNOUNCEMENTDATE = Column(VARCHAR(8), comment='回售公告日')
    B_INFO_PUTEXDATE = Column(VARCHAR(8), comment='回售履行结果公告日')
    B_INFO_PUTAMOUNT = Column(Numeric(20, 4), comment='回售总面额(亿元)')
    B_INFO_PUTOUTSTANDING = Column(Numeric(20, 4), comment='继续托管总面额(亿元)')
    B_INFO_REPURCHASESTARTDATE = Column(VARCHAR(8), comment='回售行使开始日')
    B_INFO_REPURCHASEENDDATE = Column(VARCHAR(8), comment='回售行使截止日')
    B_INFO_FUNDENDDATE = Column(VARCHAR(8), comment='回售日')
    B_INFO_REPURCHASECODE = Column(VARCHAR(40), comment='回售代码')


class CBONDRATEADJUSTMENT(Base):
    """中国债券票面利率调整幅度"""
    __tablename__ = 'CBONDRATEADJUSTMENT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_CARRYDATE = Column(VARCHAR(8), comment='起始日期')
    B_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    B_INFO_PROVISIONTYPE = Column(VARCHAR(400), comment='条款类型')
    B_INFO_COUPONRATE = Column(Numeric(22, 6), comment='当期票面利率')
    B_INFO_COUPONADJ_MIN = Column(Numeric(20, 4), comment='调整下限')
    B_INFO_COUPONADJ_MAX = Column(Numeric(20, 4), comment='调整上限')


class CBONDRATING(Base):
    """中国债券信用评级"""
    __tablename__ = 'CBONDRATING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='评级日期')
    B_RATE_STYLE = Column(VARCHAR(100), comment='评级类型')
    B_INFO_CREDITRATING = Column(VARCHAR(40), comment='信用评级')
    B_INFO_CREDITRATINGAGENCY = Column(VARCHAR(10), comment='评级机构代码')
    B_INFO_CREDITRATINGEXPLAIN = Column(VARCHAR(1000), comment='评级说明')
    B_INFO_PRECREDITRATING = Column(VARCHAR(40), comment='前次信用评级')
    B_CREDITRATING_CHANGE = Column(VARCHAR(10), comment='评级变动方向')
    ANN_DT2 = Column(VARCHAR(8), comment='公告日期')


class CBONDRATINGCICC(Base):
    """中国债券短融投资评级(中金)"""
    __tablename__ = 'CBONDRATINGCICC'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(10), comment='评级日期')
    ANALYST = Column(VARCHAR(100), comment='分析师')
    B_INFO_RATING = Column(VARCHAR(20), comment='公布评级')
    S_INFO_NAME = Column(VARCHAR(200), comment='公布证券简称')
    B_INFO_RATINGAGENCY = Column(VARCHAR(40), comment='机构')
    STARLEVEL = Column(Numeric(5, 0), comment='星级')
    MEMO = Column(VARCHAR(1000), comment='评级内容摘要')


class CBONDRATINGDEFINITION(Base):
    """中国债券信用评估机构名单"""
    __tablename__ = 'CBONDRATINGDEFINITION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    B_INFO_CREDITRATINGAGENCY = Column(VARCHAR(10), comment='评估机构代码')
    B_INFO_CREDITRATING_NAME = Column(VARCHAR(100), comment='评估机构名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')


class CBONDRATINGWATCHLIST(Base):
    """中国债券信用评级观察名单明细"""
    __tablename__ = 'CBONDRATINGWATCHLIST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    B_EVENT_HAPDATE = Column(VARCHAR(8), comment='发生日期')
    B_EVENT_CATEGORYCODE = Column(Numeric(9, 0), comment='事件类型代码')
    B_EVENT_CATEGORY = Column(VARCHAR(80), comment='事件类型名称')
    B_EVENT_TITLE = Column(VARCHAR(400), comment='事件标题')
    B_ANN_ABSTRACT = Column(VARCHAR(3000), comment='公告摘要')


class CBONDRECEIVABLES(Base):
    """中国债券公司应收账款"""
    __tablename__ = 'CBONDRECEIVABLES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='下游公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='下游公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='下游公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class CBONDREGIONAL(Base):
    """中国债券主体地域板块"""
    __tablename__ = 'CBONDREGIONAL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    WIND_SEC_CODE = Column(VARCHAR(10), comment='板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CBONDRELATEDPARTYDEBT(Base):
    """中国债券公司关联方债务"""
    __tablename__ = 'CBONDRELATEDPARTYDEBT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='债权公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='债权公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='债权公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class CBONDREPO(Base):
    """央行公开市场操作"""
    __tablename__ = 'CBONDREPO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_INFO_TERM = Column(Numeric(20, 4), comment='期限(天)')
    B_TENDER_INTERESTRATE = Column(Numeric(20, 4), comment='招标利率(%)')
    B_TENDER_AMOUNT = Column(Numeric(20, 4), comment='招标数量(亿元)')
    B_TENDER_METHOD = Column(Numeric(9, 0), comment='招标方式')
    B_INFO_REPO_TYPE = Column(Numeric(9, 0), comment='操作类型代码')
    B_INFO_TERM_WORDS = Column(VARCHAR(40), comment='期限(文字）')


class CBONDREPOANDIBLEODPRICES(Base):
    """中国债券同业拆借日行情"""
    __tablename__ = 'CBONDREPOANDIBLEODPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(%)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(%)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(%)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(%)')
    B_DQ_WAVERAGERATE = Column(Numeric(20, 8), comment='加权价(%)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交笔数')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(元)')


class CBONDRESERVERATE(Base):
    """存款准备金率(央行)"""
    __tablename__ = 'CBONDRESERVERATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_INFO_RESERVERATETYPE = Column(VARCHAR(80), comment='准备金率品种')
    B_INFO_RATE = Column(Numeric(20, 4), comment='准备金率(%)')


class CBONDSALESSEGMENT(Base):
    """中国债券发行主体主营业务构成"""
    __tablename__ = 'CBONDSALESSEGMENT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_SEGMENT_ITEM = Column(VARCHAR(100), comment='主营业务项目')
    S_SEGMENT_COST_RATIO = Column(Numeric(20, 4), comment='主营业务成本比例(%)')
    S_SEGMENT_PROFIT_RATIO = Column(Numeric(20, 4), comment='主营业务利润比例(%)')
    S_SEGMENT_SALES_RATIO = Column(Numeric(20, 4), comment='主营业务收入比例(%)')
    S_REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_SEGMENT_SALES = Column(Numeric(20, 4), comment='主营业务收入')
    S_SEGMENT_PROFIT = Column(Numeric(20, 4), comment='主营业务利润')
    S_SEGMENT_ITEMCODE = Column(VARCHAR(50), comment='项目类别')
    S_SEGMENT_COST = Column(Numeric(20, 4), comment='主营业务成本')
    S_GROSSPROFITMARGIN = Column(Numeric(20, 4), comment='毛利率(%)')
    S_PRIME_OPER_REV_YOY = Column(Numeric(20, 4), comment='主营业务收入比上年增减(%)')
    S_PRIME_OPER_COST_YOY = Column(Numeric(20, 4), comment='主营业务成本比上年增减(%)')
    S_GROSS_PROFIT_MARGIN_YOY = Column(Numeric(20, 4), comment='毛利率比上年增减(%)')
    S_SEGMENT_ITEM_CODE = Column(VARCHAR(100), comment='容错后主营业务项目')
    S_SEGMENT_SALES_CODE = Column(Numeric(9, 0), comment='主营业务收入项目代码')
    S_ACCOUNTS_ID = Column(VARCHAR(20), comment='科目ID')
    S_IS_PUBLISHVALUE = Column(Numeric(1, 0), comment='[内部]是否公布值')
    S_GROSS_PROFIT_YOY = Column(Numeric(20, 4), comment='毛利同比增长率')


class CBONDSECINDUSTRIESCLASS(Base):
    """中国债券证监会行业分类"""
    __tablename__ = 'CBONDSECINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    SEC_IND_CODE = Column(VARCHAR(50))
    ENTRY_DT = Column(VARCHAR(8))
    REMOVE_DT = Column(VARCHAR(8))
    CUR_SIGN = Column(Numeric(1, 0))
    COMP_ID = Column(VARCHAR(10))


class CBONDSECINDUSTRIESCLASSQL(Base):
    """None"""
    __tablename__ = 'CBONDSECINDUSTRIESCLASSQL'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='所属板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
    COMP_ID = Column(VARCHAR(10), comment='公司ID')


class CBONDSECINDUSTRIESCLASSZL(Base):
    """中国债券证监会行业分类(增量)"""
    __tablename__ = 'CBONDSECINDUSTRIESCLASSZL'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='所属板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')

    COMP_ID = Column(VARCHAR(10))


class CBONDSELLSUBJECT(Base):
    """中国债券公司并购出售标的"""
    __tablename__ = 'CBONDSELLSUBJECT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='并购公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='并购公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='并购公司ID')
    S_INFO_PROGRESS = Column(VARCHAR(300), comment='方案进度')
    S_UPDATE_DATE = Column(VARCHAR(8), comment='最新披露日期')
    S_MEETEVENT_ID = Column(VARCHAR(20), comment='事件ID')
    S_INFO_COMP_NAME1 = Column(VARCHAR(200), comment='并购出售目标公司名称')
    S_INFO_COMP_SNAME1 = Column(VARCHAR(40), comment='并购出售目标公司中文简称')


class CBONDSPECIALCONDITIONS(Base):
    """中国债券特殊条款"""
    __tablename__ = 'CBONDSPECIALCONDITIONS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_PROVISIONTYPE = Column(VARCHAR(100), comment='条款类型')
    B_INFO_CALLBKORPUTBKPRICE = Column(Numeric(20, 4), comment='赎回价/回售价')
    B_INFO_CALLBKORPUTBKDATE = Column(VARCHAR(8), comment='赎回/回售日期')
    B_INFO_REDEMPORREPURCDATE = Column(VARCHAR(8), comment='赎回/回售告知截止日期')
    B_INFO_MATURITYEMBEDDED = Column(VARCHAR(40), comment='含权期限说明')
    B_INFO_EXECMATURITYEMBEDDED = Column(Numeric(20, 4), comment='行权期限')
    B_INFO_COUPONADJ_MAX = Column(Numeric(20, 4), comment='票面利率调整上限')
    B_INFO_COUPONADJ_MIN = Column(Numeric(20, 4), comment='票面利率调整下限')
    B_INFO_CONTENT = Column(VARCHAR(4000), comment='条款内容')


class CBONDSPECIALCONDITIONSQL(Base):
    """None"""
    __tablename__ = 'CBONDSPECIALCONDITIONSQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    B_INFO_PROVISIONTYPE = Column(VARCHAR(100))
    B_INFO_CALLBKORPUTBKPRICE = Column(Numeric(20, 4))
    B_INFO_CALLBKORPUTBKDATE = Column(VARCHAR(8))
    B_INFO_REDEMPORREPURCDATE = Column(VARCHAR(8))
    B_INFO_MATURITYEMBEDDED = Column(VARCHAR(40))
    B_INFO_EXECMATURITYEMBEDDED = Column(Numeric(20, 4))
    B_INFO_COUPONADJ_MAX = Column(Numeric(20, 4))
    B_INFO_COUPONADJ_MIN = Column(Numeric(20, 4))
    B_INFO_CONTENT = Column(VARCHAR(4000))


class CBONDSPECIALCONDITIONSZL(Base):
    """中国债券特殊条款(增量)"""
    __tablename__ = 'CBONDSPECIALCONDITIONSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_PROVISIONTYPE = Column(VARCHAR(100), comment='条款类型')
    B_INFO_CALLBKORPUTBKPRICE = Column(Numeric(20, 4), comment='赎回价/回售价')
    B_INFO_CALLBKORPUTBKDATE = Column(VARCHAR(8), comment='赎回/回售日期')
    B_INFO_REDEMPORREPURCDATE = Column(VARCHAR(8), comment='赎回/回售告知截止日期')
    B_INFO_MATURITYEMBEDDED = Column(VARCHAR(40), comment='含权期限说明')
    B_INFO_EXECMATURITYEMBEDDED = Column(Numeric(20, 4), comment='行权期限')
    B_INFO_COUPONADJ_MAX = Column(Numeric(20, 4), comment='票面利率调整上限')
    B_INFO_COUPONADJ_MIN = Column(Numeric(20, 4), comment='票面利率调整下限')
    B_INFO_CONTENT = Column(VARCHAR(3000), comment='条款内容')


class CBONDSPECIALCURVECNBD(Base):
    """中债登特殊收益率曲线"""
    __tablename__ = 'CBONDSPECIALCURVECNBD'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    B_ANAL_CURVENAME = Column(VARCHAR(200), comment='曲线名称')
    B_ANAL_CURVENUMBER = Column(Numeric(10, 0), comment='曲线编号')
    B_ANAL_CURVETYPE = Column(VARCHAR(200), comment='曲线类型')
    B_ANAL_CURVETERM = Column(Numeric(24, 8), comment='标准期限(年)')
    B_ANAL_YIELD = Column(Numeric(24, 8), comment='收益率(%)')


class CBONDST(Base):
    """中国债券特别处理"""
    __tablename__ = 'CBONDST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_TYPE_ST = Column(VARCHAR(8), comment='特别处理类型代码')
    ENTRY_DT = Column(VARCHAR(8), comment='实施日期')
    REMOVE_DT = Column(VARCHAR(8), comment='撤消日期')
    REASON = Column(VARCHAR(100), comment='实施原因')


class CBONDSUPERVISOR(Base):
    """中国债券公司监事成员"""
    __tablename__ = 'CBONDSUPERVISOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='职务')


class CBONDSUPPLIER(Base):
    """中国债券公司供应商"""
    __tablename__ = 'CBONDSUPPLIER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='上游公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='上游公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='上游公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')
    S_INFO_DISCLOSER = Column(VARCHAR(100), comment='披露公司ID')
    PCT = Column(Numeric(20, 4), comment='占比(%)')


class CBONDSWINDUSTRIESCLASS(Base):
    """None"""
    __tablename__ = 'CBONDSWINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SW_IND_NAME = Column(VARCHAR(50), comment='申万子行业')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    SW_IND_NAME1 = Column(VARCHAR(50), comment='申万父行业')
    SW_IND_CODE = Column(VARCHAR(16), comment='申万子行业代码')
    SW_IND_CODE1 = Column(VARCHAR(16), comment='申万父行业代码')


class CBONDTAXESPAYABLE(Base):
    """中国债券发行主体应交税费明细"""
    __tablename__ = 'CBONDTAXESPAYABLE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    VAT = Column(Numeric(20, 4), comment='增值税')
    BUSINESS_TAX = Column(Numeric(20, 4), comment='营业税')
    CORPORATE_INCOME_TAX = Column(Numeric(20, 4), comment='企业所得税')
    URBAN_MAINTENANCE_TAX = Column(Numeric(20, 4), comment='城市维护建设税')
    PROPERTY_TAX = Column(Numeric(20, 4), comment='房产税')
    PERSONAL_INCOME_TAX = Column(Numeric(20, 4), comment='个人所得税')
    SALE_TAX = Column(Numeric(20, 4), comment='消费税')
    LAND_HOLDING_TAX = Column(Numeric(20, 4), comment='土地使用税')
    STAMP_DUTY = Column(Numeric(20, 4), comment='印花税')
    VEHICLE_USAGE_TAX = Column(Numeric(20, 4), comment='车船使用税')
    LAND_VALUE_ADDED_TAX = Column(Numeric(20, 4), comment='土地增值税')
    RESOURCE_TAX = Column(Numeric(20, 4), comment='资源税')
    OTHER = Column(Numeric(20, 4), comment='其他')
    TOTAL = Column(Numeric(20, 4), comment='合计')
    MEMO = Column(VARCHAR(500), comment='备注')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    EDUCATION_SURCHARGE = Column(Numeric(20, 4), comment='教育费附加')
    FLOOD_CONTROL_FUND = Column(Numeric(20, 4), comment='防洪基金')
    COMPENSATION_MINERAL_RESOURCES = Column(Numeric(20, 4), comment='矿产资源补偿费')
    VEHICLE_PURCHASE_SURCHARGE = Column(Numeric(20, 4), comment='车辆购置附加费')
    AGRICULTURE_FORESTRY_TAX = Column(Numeric(20, 4), comment='农林特产税')
    LOCAL_EDUCATION_FEE = Column(Numeric(20, 4), comment='地方教育费附加')
    PRICE_CONTROL_FUND = Column(Numeric(20, 4), comment='价格调控基金')
    STATEMENT_TYPE_CODE = Column(Numeric(9, 0), comment='报表类型代码')


class CBONDTENDER(Base):
    """中国债券招标"""
    __tablename__ = 'CBONDTENDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    B_TENDER_TENDERDATE = Column(VARCHAR(8), comment='招投标日期')
    B_TENDER_METHOD = Column(Numeric(9, 0), comment='招标方式')
    B_TENDER_OBJECT = Column(Numeric(9, 0), comment='招标标的')
    B_TENDER_AMOUNTPLAN = Column(Numeric(20, 4), comment='计划招标总额')
    B_TENDER_CMPTAMNT = Column(Numeric(20, 4), comment='竞争性招标总额')
    B_TENDER_UNDERWRITING = Column(Numeric(20, 4), comment='基本承销额度')
    B_TENDER_ADDITIVERIGHTS = Column(VARCHAR(200), comment='基本承销额增加权利')
    B_TENDER_ADDRATIO = Column(Numeric(20, 4), comment='基本承销额追加比例(%)')
    B_TENDER_THRESHOLD = Column(Numeric(20, 4), comment='投标价位下限')
    B_TENDER_CEILING = Column(Numeric(20, 4), comment='投标价位上限')
    B_TENDER_TENDERUNIT = Column(Numeric(20, 4), comment='基本投标单位')
    B_TENDER_LOWESTAMNT = Column(Numeric(20, 4), comment='每标位最低投标量')
    B_TENDER_HIGHESTAMNT = Column(Numeric(20, 4), comment='每标位最高投标量')
    B_TENDER_PAYMENTDATE = Column(VARCHAR(40), comment='缴款日期')
    B_TENDER_CONFIRMDATE = Column(VARCHAR(8), comment='资金到账确认时间')
    B_TENDER_TRANSFERDATE = Column(VARCHAR(8), comment='债券过户时间')
    B_TENDER_DISTRIBBEGIN = Column(VARCHAR(8), comment='分销起始日期')
    B_TENDER_DISTRIBEND = Column(VARCHAR(8), comment='分销截止日期')
    B_TENDER_UNDERWRITINGCOST = Column(Numeric(20, 4), comment='承揽费率(%)')
    B_TENDER_SPREAD = Column(VARCHAR(20), comment='标位步长')
    B_TENDER_CONCATENATIONORNOT = Column(Numeric(1, 0), comment='是否要求标位连续')
    B_TENDER_TIME = Column(VARCHAR(80), comment='招标时间')
    B_TENDER_PAYMENT_ENDDATE = Column(VARCHAR(8), comment='缴款截止日')


class CBONDTENDERRESULT(Base):
    """中国债券招标结果"""
    __tablename__ = 'CBONDTENDERRESULT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_TENDER_OBJECT = Column(Numeric(9, 0), comment='招标标的')
    B_TENDRST_DOCUMTNUMBER = Column(VARCHAR(80), comment='招标书编号')
    B_TENDRST_PAYAMOUNT = Column(Numeric(20, 4), comment='缴款总金额(元)')
    B_TENDRST_AMOUNTAD = Column(Numeric(20, 4), comment='追加发行总量(万元)')
    B_TENDRST_UNDERWRITING = Column(Numeric(20, 4), comment='基本承购总额(万元)')
    B_TENDRST_AMOUNTACT = Column(Numeric(20, 4), comment='实际发行总额(万元)')
    B_TENDRST_AMNT = Column(Numeric(20, 4), comment='招标总量(万元)')
    B_TENDRST_OUGHTTENDER = Column(Numeric(20, 4), comment='应投家数')
    B_TENDRST_INVESTORTENDERED = Column(Numeric(20, 4), comment='投标家数')
    B_TENDRST_TENDERS = Column(Numeric(20, 4), comment='投标笔数')
    B_TENDRST_EFFECTTENDER = Column(Numeric(20, 4), comment='有效笔数')
    B_TENDRST_INEFFECTTENDER = Column(Numeric(20, 4), comment='无效笔数')
    B_TENDRST_EFFECTAMNT = Column(Numeric(20, 4), comment='有效投标总量(万元)')
    B_TENDRST_HIGHTEST = Column(Numeric(20, 4), comment='最高投标价位')
    B_TENDRST_LOWEST = Column(Numeric(20, 4), comment='最低投标价位')
    B_TENDRST_WINNINGAMNT = Column(Numeric(20, 4), comment='中标总量(万元)')
    B_TENDRST_WINNERBIDDER = Column(Numeric(20, 4), comment='中标家数')
    B_TENDRST_WINNINGBIDDER = Column(Numeric(20, 4), comment='中标笔数')
    B_TENDRST_PRIVATETRADE = Column(Numeric(20, 4), comment='自营中标总量(万元)')
    B_TENDRST_HIGHTPRICE = Column(Numeric(20, 4), comment='最高中标价位')
    B_TENDRST_LOWPRICE = Column(Numeric(20, 4), comment='最低中标价位')
    B_TENDRST_MARGAMNT = Column(Numeric(20, 4), comment='边际中标价位投标总量(万元)')
    B_TENDRST_MARGWINBIDDER = Column(Numeric(20, 4), comment='边际中标价位中标总量(万元)')
    B_TENDRST_FINALPRICE = Column(Numeric(20, 4), comment='最终发行价格')
    B_TENDRST_REFERYIELD = Column(Numeric(20, 4), comment='参考收益率(%)')
    B_TENDRST_FINANCOUPON = Column(Numeric(20, 4), comment='最终票面利率(%)')
    B_TENDRST_BIDRATE = Column(Numeric(20, 4), comment='全场中标利率(%)')
    B_TENDRST_BIDPRICE = Column(Numeric(20, 4), comment='全场中标价格(元)')
    B_TENDRST_BIDSPREAD = Column(Numeric(20, 4), comment='全场中标利差(%)')
    S_IPO_OVRSUBRATIO = Column(Numeric(20, 4), comment='超额认购倍数')
    B_BID_AMNT = Column(Numeric(20, 4), comment='投标总量')
    B_TENDRST_EFFECTIVE_NUMBER = Column(Numeric(20, 4), comment='有效家数')
    B_TENDRST_MARGINAL_MULTIPLIER = Column(Numeric(20, 4), comment='边际倍数')
    B_MARGINAL_INTEREST_RATE = Column(Numeric(20, 4), comment='边际利率')


class CBONDTENDERRESULTQL(Base):
    """None"""
    __tablename__ = 'CBONDTENDERRESULTQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    B_TENDER_OBJECT = Column(Numeric(9, 0))
    B_TENDRST_DOCUMTNUMBER = Column(VARCHAR(80))
    B_TENDRST_PAYAMOUNT = Column(Numeric(20, 4))
    B_TENDRST_AMOUNTAD = Column(Numeric(20, 4))
    B_TENDRST_UNDERWRITING = Column(Numeric(20, 4))
    B_TENDRST_AMOUNTACT = Column(Numeric(20, 4))
    B_TENDRST_AMNT = Column(Numeric(20, 4))
    B_TENDRST_OUGHTTENDER = Column(Numeric(20, 4))
    B_TENDRST_INVESTORTENDERED = Column(Numeric(20, 4))
    B_TENDRST_TENDERS = Column(Numeric(20, 4))
    B_TENDRST_EFFECTTENDER = Column(Numeric(20, 4))
    B_TENDRST_INEFFECTTENDER = Column(Numeric(20, 4))
    B_TENDRST_EFFECTAMNT = Column(Numeric(20, 4))
    B_TENDRST_HIGHTEST = Column(Numeric(20, 4))
    B_TENDRST_LOWEST = Column(Numeric(20, 4))
    B_TENDRST_WINNINGAMNT = Column(Numeric(20, 4))
    B_TENDRST_WINNERBIDDER = Column(Numeric(20, 4))
    B_TENDRST_WINNINGBIDDER = Column(Numeric(20, 4))
    B_TENDRST_PRIVATETRADE = Column(Numeric(20, 4))
    B_TENDRST_HIGHTPRICE = Column(Numeric(20, 4))
    B_TENDRST_LOWPRICE = Column(Numeric(20, 4))
    B_TENDRST_MARGAMNT = Column(Numeric(20, 4))
    B_TENDRST_MARGWINBIDDER = Column(Numeric(20, 4))
    B_TENDRST_FINALPRICE = Column(Numeric(20, 4))
    B_TENDRST_REFERYIELD = Column(Numeric(20, 4))
    B_TENDRST_FINANCOUPON = Column(Numeric(20, 4))
    B_TENDRST_BIDRATE = Column(Numeric(20, 4))
    B_TENDRST_BIDPRICE = Column(Numeric(20, 4))
    B_TENDRST_BIDSPREAD = Column(Numeric(20, 4))
    S_IPO_OVRSUBRATIO = Column(Numeric(20, 4))
    B_BID_AMNT = Column(Numeric(20, 4))
    B_TENDRST_EFFECTIVE_NUMBER = Column(Numeric(20, 4))
    B_TENDRST_MARGINAL_MULTIPLIER = Column(Numeric(20, 4))
    B_MARGINAL_INTEREST_RATE = Column(Numeric(20, 4))


class CBONDTENDERRESULTZL(Base):
    """中国债券招标结果(增量)"""
    __tablename__ = 'CBONDTENDERRESULTZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_TENDER_OBJECT = Column(Numeric(9, 0), comment='招标标的')
    B_TENDRST_DOCUMTNUMBER = Column(VARCHAR(80), comment='招标书编号')
    B_TENDRST_PAYAMOUNT = Column(Numeric(20, 4), comment='缴款总金额(元)')
    B_TENDRST_AMOUNTAD = Column(Numeric(20, 4), comment='追加发行总量(万元)')
    B_TENDRST_UNDERWRITING = Column(Numeric(20, 4), comment='基本承购总额(万元)')
    B_TENDRST_AMOUNTACT = Column(Numeric(20, 4), comment='实际发行总额(万元)')
    B_TENDRST_AMNT = Column(Numeric(20, 4), comment='招标总量(万元)')
    B_TENDRST_OUGHTTENDER = Column(Numeric(20, 4), comment='应投家数')
    B_TENDRST_INVESTORTENDERED = Column(Numeric(20, 4), comment='投标家数')
    B_TENDRST_TENDERS = Column(Numeric(20, 4), comment='投标笔数')
    B_TENDRST_EFFECTTENDER = Column(Numeric(20, 4), comment='有效笔数')
    B_TENDRST_INEFFECTTENDER = Column(Numeric(20, 4), comment='无效笔数')
    B_TENDRST_EFFECTAMNT = Column(Numeric(20, 4), comment='有效投标总量(万元)')
    B_TENDRST_HIGHTEST = Column(Numeric(20, 4), comment='最高投标价位')
    B_TENDRST_LOWEST = Column(Numeric(20, 4), comment='最低投标价位')
    B_TENDRST_WINNINGAMNT = Column(Numeric(20, 4), comment='中标总量(万元)')
    B_TENDRST_WINNERBIDDER = Column(Numeric(20, 4), comment='中标家数')
    B_TENDRST_WINNINGBIDDER = Column(Numeric(20, 4), comment='中标笔数')
    B_TENDRST_PRIVATETRADE = Column(Numeric(20, 4), comment='自营中标总量(万元)')
    B_TENDRST_HIGHTPRICE = Column(Numeric(20, 4), comment='最高中标价位')
    B_TENDRST_LOWPRICE = Column(Numeric(20, 4), comment='最低中标价位')
    B_TENDRST_MARGAMNT = Column(Numeric(20, 4), comment='边际中标价位投标总量(万元)')
    B_TENDRST_MARGWINBIDDER = Column(Numeric(20, 4), comment='边际中标价位中标总量(万元)')
    B_TENDRST_FINALPRICE = Column(Numeric(20, 4), comment='最终发行价格')
    B_TENDRST_REFERYIELD = Column(Numeric(20, 4), comment='参考收益率(%)')
    B_TENDRST_FINANCOUPON = Column(Numeric(20, 4), comment='最终票面利率(%)')
    B_TENDRST_BIDRATE = Column(Numeric(20, 4), comment='全场中标利率(%)')
    B_TENDRST_BIDPRICE = Column(Numeric(20, 4), comment='全场中标价格(元)')
    B_TENDRST_BIDSPREAD = Column(Numeric(20, 4), comment='全场中标利差(%)')
    S_IPO_OVRSUBRATIO = Column(Numeric(20, 4), comment='超额认购倍数')


class CBONDTHIRDEODPRICES(Base):
    """中国债券行情(第三方)"""
    __tablename__ = 'CBONDTHIRDEODPRICES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    SOURCE_CODE = Column(Numeric(9, 0), comment='来源代码')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    S_DQ_AVGPRICE = Column(Numeric(20, 4), comment='均价')
    S_DQ_BUY_AVGPRICE = Column(Numeric(20, 4), comment='买入平均价')
    S_DQ_SELL_AVGPRICE = Column(Numeric(20, 4), comment='卖出平均价')
    S_ANAL_OPEN = Column(Numeric(20, 4), comment='开盘价收益率')
    S_ANAL_HIGH = Column(Numeric(20, 4), comment='最高价收益率')
    S_ANAL_LOW = Column(Numeric(20, 4), comment='最低价收益率')
    S_ANAL_CLOSE = Column(Numeric(20, 4), comment='收盘价收益率')
    S_ANAL_AVGPRICE = Column(Numeric(20, 4), comment='均价收益率')
    S_ANAL_BUY_AVGPRICE = Column(Numeric(20, 4), comment='买入平均价收益率')
    S_ANAL_SELL_AVGPRICE = Column(Numeric(20, 4), comment='卖出平均价收益率')
    S_BLOCK_FREQUENCY = Column(Numeric(20, 4), comment='成交笔数')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额')


class CBONDTHIRDPARTYRATING(Base):
    """中国债券第三方信用评级(中债资信)"""
    __tablename__ = 'CBONDTHIRDPARTYRATING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='品种ID')
    B_RATE_STYLE = Column(Numeric(9, 0), comment='品种类别代码')
    B_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    B_TYPCODE = Column(Numeric(9, 0), comment='评级类型代码')
    B_EST_RATING_INST = Column(VARCHAR(40), comment='信用等级')
    B_EST_INSTITUTE = Column(VARCHAR(100), comment='评估机构公司')
    B_RATE_RATINGOUTLOOK = Column(VARCHAR(300), comment='评级展望')
    B_EST_PRERATING_INST = Column(VARCHAR(40), comment='前次评级')
    B_RATE_PRERATINGOUTLOOK = Column(VARCHAR(300), comment='前次评级展望')
    B_EST_RATING_CHANGE = Column(VARCHAR(10), comment='评级变动方向')
    B_RATE_RATINGOUTLOOK_CODE = Column(Numeric(9, 0), comment='评级展望代码')
    B_RATE_PRERATINGOUTLOOK_CODE = Column(Numeric(9, 0), comment='前次评级展望代码')


class CBONDTOP5BYACCOUNTSRECEIVABLE(Base):
    """中国债券发行主体应收账款余额前五名"""
    __tablename__ = 'CBONDTOP5BYACCOUNTSRECEIVABLE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='债务人名称')
    AMOUNT = Column(Numeric(20, 4), comment='金额')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PERIOD = Column(VARCHAR(50), comment='拖欠时间')
    REASON = Column(VARCHAR(30), comment='拖欠原因')


class CBONDTRADINGSUSPENSION(Base):
    """中国债券停复牌信息"""
    __tablename__ = 'CBONDTRADINGSUSPENSION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DQ_SUSPENDDATE = Column(VARCHAR(8), comment='停牌日期')
    S_DQ_SUSPENDTYPE = Column(Numeric(9, 0), comment='停牌类型代码')
    S_DQ_RESUMPDATE = Column(VARCHAR(8), comment='复牌日期')
    S_DQ_CHANGEREASON = Column(VARCHAR(400), comment='停牌原因')
    S_DQ_CHANGEREASON_CODE = Column(Numeric(9, 0), comment='停牌原因代码')
    S_DQ_RESUMPTIME = Column(VARCHAR(200), comment='停复牌时间')


class CBONDTTMHIS(Base):
    """中国债券发行主体TTM财务指标"""
    __tablename__ = 'CBONDTTMHIS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='截止日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    TOT_OPER_REV_TTM = Column(Numeric(20, 4), comment='营业总收入(TTM)')
    OPER_REV_TTM = Column(Numeric(20, 4), comment='营业收入(TTM)')
    NET_PROFIT_TTM = Column(Numeric(20, 4), comment='净利润(TTM)')
    NET_PROFIT_PARENT_COMP_TTM = Column(Numeric(20, 4), comment='归属于母公司的净利润(TTM)')
    NET_CASH_FLOWS_OPER_ACT_TTM = Column(Numeric(20, 4), comment='经营活动现金净流量(TTM)')
    NET_INCR_CASH_CASH_EQU_TTM = Column(Numeric(20, 4), comment='现金净流量(TTM)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_FA_COST_TTM = Column(Numeric(20, 4), comment='营业成本-非金融类(TTM)')
    S_FA_EXPENSE_TTM = Column(Numeric(20, 4), comment='营业支出-金融类(TTM)')
    S_FA_GROSSMARGIN_TTM = Column(Numeric(20, 4), comment='毛利(TTM)')
    S_FA_OPERATEINCOME_TTM = Column(Numeric(20, 4), comment='经营活动净收益(TTM)')
    S_FA_INVESTINCOME_TTM = Column(Numeric(20, 4), comment='价值变动净收益(TTM)')
    S_FA_OP_TTM = Column(Numeric(20, 4), comment='营业利润(TTM)')
    S_FA_EBT_TTM = Column(Numeric(20, 4), comment='利润总额(TTM)')
    S_FA_GR_TTM = Column(Numeric(20, 4), comment='营业总收入(TTM)')
    S_FA_GC_TTM = Column(Numeric(20, 4), comment='营业总成本(TTM)')
    S_FA_INVESTCASHFLOW_TTM = Column(Numeric(20, 4), comment='投资活动现金净流量(TTM)')
    S_FA_FINANCECASHFLOW_TTM = Column(Numeric(20, 4), comment='筹资活动现金净流量(TTM)')
    S_FA_ASSET_MRQ = Column(Numeric(20, 4), comment='资产总计(MRQ)')
    S_FA_DEBT_MRQ = Column(Numeric(20, 4), comment='负债合计(MRQ)')
    S_FA_TOTALEQUITY_MRQ = Column(Numeric(20, 4), comment='股东权益(MRQ)')
    S_FA_EQUITY_MRQ = Column(Numeric(20, 4), comment='归属于母公司的股东权益(MRQ)')
    S_FA_NETPROFITMARGIN_TTM = Column(Numeric(20, 4), comment='销售净利率(TTM)')
    S_FA_GROSSPROFITMARGIN_TTM = Column(Numeric(20, 4), comment='销售毛利率(TTM)')
    S_FA_EXPENSETOSALES_TTM = Column(Numeric(20, 4), comment='销售期间费用率(TTM)')
    S_FA_PROFITTOGR_TTM = Column(Numeric(20, 4), comment='净利润/营业总收入(TTM)')
    S_FA_OPERATEEXPENSETOGR_TTM = Column(Numeric(20, 4), comment='销售费用/营业总收入(TTM)')
    S_FA_ADMINEXPENSETOGR_TTM = Column(Numeric(20, 4), comment='管理费用/营业总收入(TTM)')
    S_FA_FINAEXPENSETOGR_TTM = Column(Numeric(20, 4), comment='财务费用/营业总收入(TTM)')
    S_FA_IMPAIRTOGR_TTM = Column(Numeric(20, 4), comment='资产减值损失/营业总收入(TTM)')
    S_FA_GCTOGR_TTM = Column(Numeric(20, 4), comment='营业总成本/营业总收入(TTM)')
    S_FA_OPTOGR_TTM = Column(Numeric(20, 4), comment='营业利润/营业总收入(TTM)')
    S_FA_ROA_TTM = Column(Numeric(20, 4), comment='总资产净利率(TTM)')
    S_FA_ROA2_TTM = Column(Numeric(20, 4), comment='总资产报酬率(TTM)')
    S_FA_ROE_TTM = Column(Numeric(20, 4), comment='净资产收益率(TTM)')
    S_FA_OPERATEINCOMETOEBT_TTM = Column(Numeric(20, 4), comment='经营活动净收益/利润总额(TTM)')
    S_FA_INVESTINCOMETOEBT_TTM = Column(Numeric(20, 4), comment='价值变动净收益/利润总额(TTM)')
    S_FA_NONOPERATEPROFITTOEBT_TTM = Column(Numeric(20, 4), comment='营业外收支净额/利润总额(TTM)')
    S_FA_SALESCASHINTOOR_TTM = Column(Numeric(20, 4), comment='销售商品提供劳务收到的现金/营业收入(TTM)')
    S_FA_OCFTOOR_TTM = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/营业收入(TTM)')
    S_FA_OCFTOOPERATEINCOME_TTM = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/经营活动净收益(TTM)')
    S_FA_DEDUCTEDPROFIT_TTM = Column(Numeric(20, 4), comment='扣除非经常性损益后的净利润(TTM)')
    S_FA_EBITDA_TTM_INVERSE = Column(Numeric(20, 4), comment='EBITDA(TTM反推法)')
    S_FA_EBITDA_TTM = Column(Numeric(20, 4), comment='EBITDA(TTM)')
    S_FA_EBIT_TTM = Column(Numeric(20, 4), comment='EBIT(TTM)')
    FA_ROIC_TTM = Column(Numeric(20, 4), comment='投入资本回报率(TTM)')
    S_FA_SALESCASHIN_TTM = Column(Numeric(20, 4), comment='销售商品提供劳务收到的现金(TTM)')
    S_FA_OPERATEEXPENSE_TTM = Column(Numeric(20, 4), comment='销售费用(TTM)')
    S_FA_ADMINEXPENSE_TTM = Column(Numeric(20, 4), comment='管理费用(TTM)')
    S_FA_FINAEXPENSE_TTM = Column(Numeric(20, 4), comment='财务费用(TTM)')
    S_FA_EXPENSE = Column(Numeric(20, 4), comment='期间费用(TTM)')
    S_FA_NONOPERATEPROFIT_TTM = Column(Numeric(20, 4), comment='营业外收支净额(TTM)')
    S_FA_IMPAIRMENT_TTM = Column(Numeric(20, 4), comment='资产减值损失(TTM)')
    S_FA_EBIT_TTM_INVERSE = Column(Numeric(20, 4), comment='EBIT(TTM反推法)')
    S_FA_INVESTCAPITAL_MRQ = Column(Numeric(20, 4), comment='全部投入资本(MRQ)')
    FA_ROIC_TTM2 = Column(Numeric(20, 4), comment='投入资本回报率ROIC(TTM)')
    S_STM_BSMRQ = Column(Numeric(20, 4), comment='固定资产合计(MRQ)')
    S_FA_NONOPPROFIT_TTM = Column(Numeric(20, 4), comment='非营业利润(TTM)')
    S_FA_PREFINEXP_OP_TTM = Column(Numeric(20, 4), comment='扣除财务费用前营业利润(TTM)')
    S_FA_OPTOEBT_TTM = Column(Numeric(20, 4), comment='营业利润/利润总额(TTM)')
    S_FA_NOPTOEBT_TTM = Column(Numeric(20, 4), comment='非营业利润/利润总额(TTM)')
    S_FA_TAXTOEBT_TTM = Column(Numeric(20, 4), comment='税项/利润总额(TTM)')
    S_FA_OPTOOR_TTM = Column(Numeric(20, 4), comment='营业利润/营业收入(TTM)')
    S_FA_EBTTOOR_TTM = Column(Numeric(20, 4), comment='利润总额/营业收入(TTM)')
    S_FA_PREFINEXPOPTOOR_TTM = Column(Numeric(20, 4), comment='扣除融资费用前营业利润/营业收入(TTM)')
    S_FA_NETPROFITTOOR_TTM = Column(Numeric(20, 4), comment='归属母公司股东的净利润/营业收入(TTM)')
    S_FA_PREFINEXPOPTOEBT_TTM = Column(Numeric(20, 4), comment='扣除融资费用前营业利润/利润总额(TTM)')
    S_FA_OCFTOOP_TTM = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额/营业利润(TTM)')
    ROA_EXCLMININTINC_TTM = Column(Numeric(20, 4), comment='总资产净利率-不含少数股东损益(TTM)')
    S_FA_DEBTTOASSETS_MRQ = Column(Numeric(20, 4), comment='资产负债率(MRQ)')
    INT_EXP_TTM = Column(Numeric(20, 4), comment='利息支出(TTM)')
    INC_TAX_TTM = Column(Numeric(20, 4), comment='所得税(TTM)')
    MINORITY_INT_TTM = Column(Numeric(20, 4), comment='少数股东权益(TTM)')
    CONTINUOUS_NET_OP_TTM = Column(Numeric(20, 4), comment='持续经营净利润(TTM)')
    NONCONTINUOUS_NET_OP_TTM = Column(Numeric(20, 4), comment='非持续经营净利润(TTM)')
    NONNETOPTOTAXPROFIT = Column(Numeric(20, 4), comment='非持续经营净利润/税后利润(TTM)')
    NETOPTOTAXPROFIT = Column(Numeric(20, 4), comment='持续经营净利润/税后利润(TTM)')


class CBONDTYPECODE(Base):
    """None"""
    __tablename__ = 'CBONDTYPECODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_TYPNAME = Column(VARCHAR(300), comment='类型名称')
    S_TYPCODE = Column(VARCHAR(40), comment='类型代码')
    S_ORIGIN_TYPCODE = Column(Numeric(9, 0), comment='类型代码')
    S_CLASSIFICATION = Column(VARCHAR(100), comment='分类')


class CBONDUNDERWRITINGMEMBER(Base):
    """中国债券市场承销团成员明细"""
    __tablename__ = 'CBONDUNDERWRITINGMEMBER'
    MEMBER_NAME = Column(VARCHAR(200), comment='成员名称')
    UNDERWRITING_GROUP_TYPE = Column(VARCHAR(100), comment='承销团类型')
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    B_YEAR = Column(VARCHAR(8), comment='年度')
    MEMBER_ID = Column(VARCHAR(50), comment='成员ID')
    MEMBER_TYPE = Column(VARCHAR(100), comment='成员类型')
    MEMBER_TYPE_NUM = Column(Numeric(9, 0), comment='成员类型代码')
    UNDERWRITING_GROUP_NUM = Column(Numeric(9, 0), comment='承销团类型代码')


class CBONDVALUATION(Base):
    """中国债券衍生指标"""
    __tablename__ = 'CBONDVALUATION'
    __table_args__ = (
        Index('IDX_CBONDVALUATION_CODE_DT', 'S_INFO_WINDCODE', 'TRADE_DT'),
        Index('IDX_CBONDVALUATION_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_DURATION = Column(Numeric(24, 8), comment='久期')
    B_ANAL_MODIFIEDDURATION = Column(Numeric(24, 8), comment='修正久期')
    B_ANAL_BDURATION = Column(Numeric(24, 8), comment='基准久期')
    B_ANAL_SDURATION = Column(Numeric(24, 8), comment='利差久期')
    B_ANAL_CONVEXITY = Column(Numeric(24, 8), comment='凸性')
    B_ANAL_ACCRUEDDAYS = Column(Numeric(20, 4), comment='已计息时间')
    B_ANAL_ACCRUEDINTEREST = Column(Numeric(24, 8), comment='应计利息')
    B_ANAL_YTC = Column(Numeric(24, 8), comment='赎回收益率(%)')
    B_ANAL_YTP = Column(Numeric(24, 8), comment='回售收益率(%)')
    B_ANAL_PTMYEAR = Column(Numeric(20, 4), comment='剩余期限(年)')
    B_ANAL_YTM = Column(Numeric(24, 8), comment='到期收益率(%)')
    B_INFO_WEIGHTEDRT = Column(Numeric(20, 8), comment='加权剩余期限(年)')
    B_ANAL_YTM_INTEREST = Column(Numeric(24, 8), comment='收盘价到期收益率(单利)(%)')
    B_ANAL_YTM_COMPOUND = Column(Numeric(24, 8), comment='收盘价到期收益率(复利)(%)')
    B_ANAL_YTM_COMPOUND_BE = Column(Numeric(24, 8), comment='收盘价到期收益率(复利BE)(%)')
    B_ANAL_YTM_OPEN = Column(Numeric(24, 8), comment='开盘价到期收益率(%)')
    B_ANAL_YTM_HIGH = Column(Numeric(24, 8), comment='最高价到期收益率(%)')
    B_ANAL_YTM_LOW = Column(Numeric(24, 8), comment='最低价到期收益率(%)')


class CBONDWINDCUSTOMCODE(Base):
    """None"""
    __tablename__ = 'CBONDWINDCUSTOMCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_ASHARECODE = Column(VARCHAR(10), comment='证券id')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    S_INFO_SECURITIESTYPES = Column(VARCHAR(10), comment='品种类型(兼容)')
    S_INFO_SECTYPENAME = Column(VARCHAR(40), comment='品种类型(兼容)')
    S_INFO_COUNTRYNAME = Column(VARCHAR(100), comment='国家及地区代码')
    S_INFO_COUNTRYCODE = Column(VARCHAR(10), comment='国家及地区代码')
    S_INFO_EXCHMARKETNAME = Column(VARCHAR(40), comment='交易所名称(兼容)')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')
    CRNCY_NAME = Column(VARCHAR(40), comment='交易币种')
    CRNCY_CODE = Column(VARCHAR(10), comment='交易币种')
    S_INFO_ISINCODE = Column(VARCHAR(40), comment='[内部]ISIN代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券中文简称')
    EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')
    SECURITY_STATUS = Column(Numeric(9, 0), comment='存续状态')
    S_INFO_ORG_CODE = Column(VARCHAR(20), comment='组织机构代码')
    S_INFO_TYPECODE = Column(Numeric(9, 0), comment='[内部]产品用分类代码')
    S_INFO_MIN_PRICE_CHG_UNIT = Column(Numeric(24, 8), comment='最小价格变动单位')
    S_INFO_LOT_SIZE = Column(Numeric(20, 4), comment='每手数量')
    S_INFO_ENAME = Column(VARCHAR(200), comment='[内部]证券英文简称')
    S_SECURITIESTYPE_CODE = Column(Numeric(9, 0), comment='品种细类代码')
    S_ABBREVIATION = Column(VARCHAR(40), comment='简称拼音')


class BONDANNCOLUMN(Base):
    """债券公告栏目"""
    __tablename__ = 'BONDANNCOLUMN'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    N_INFO_CODE = Column(VARCHAR(38), comment='Wind栏目代码')
    N_INFO_PCODE = Column(VARCHAR(38), comment='父节点栏目代码')
    N_INFO_FCODE = Column(VARCHAR(38), comment='本节栏目代码')
    N_INFO_NAME = Column(VARCHAR(200), comment='栏目名称')
    N_INFO_ISVALID = Column(Numeric(2, 0), comment='是否有效')
    N_INFO_LEVELNUM = Column(Numeric(2, 0), comment='栏目级别')


class BONDANNCOLUMNZL(Base):
    """债券公告栏目(增量)"""
    __tablename__ = 'BONDANNCOLUMNZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    N_INFO_CODE = Column(VARCHAR(38), comment='Wind栏目代码')
    N_INFO_PCODE = Column(VARCHAR(38), comment='父节点栏目代码')
    N_INFO_FCODE = Column(VARCHAR(38), comment='本节栏目代码')
    N_INFO_NAME = Column(VARCHAR(200), comment='栏目名称')
    N_INFO_ISVALID = Column(Numeric(2, 0), comment='是否有效')
    N_INFO_LEVELNUM = Column(Numeric(2, 0), comment='栏目级别')


class BONDANNINF(Base):
    """债券公告信息"""
    __tablename__ = 'BONDANNINF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    N_INFO_STOCKID = Column(VARCHAR(10), comment='证券ID')
    N_INFO_COMPANYID = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(DateTime, comment='公告日期')
    N_INFO_TITLE = Column(VARCHAR(1024), comment='标题')
    N_INFO_FCODE = Column(VARCHAR(200), comment='栏目代码')
    N_INFO_FTXT = Column(TEXT(2147483647), comment='摘要')
    N_INFO_ANNLINK = Column(TEXT(2147483647), comment='公告链接')


class BONDISSUANCEPLAN(Base):
    """中国债券公司债发行预案"""
    __tablename__ = 'BONDISSUANCEPLAN'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    PROGRESS_CODE = Column(Numeric(5, 0), comment='方案进度代码')
    BONDTYPE = Column(VARCHAR(40), comment='拟发行债券类型')
    AMOUNT = Column(Numeric(24, 8), comment='发行数量(亿元)')
    DESCRIPTION = Column(VARCHAR(200), comment='发行数量说明')
    IS_MAX_AMOUNT = Column(Numeric(1, 0), comment='是否是最大发行数量')
    DURATION = Column(VARCHAR(200), comment='期限说明')
    RATE = Column(VARCHAR(800), comment='利率说明')
    LEADUNDERWRITER = Column(VARCHAR(200), comment='主承销商')
    IS_APPROVED = Column(Numeric(5, 0), comment='是否需股东大会批准')
    IS_ISSUE_SHAREHOLDER = Column(Numeric(5, 0), comment='是否向股东配售')
    ARRANGEMENT = Column(VARCHAR(100), comment='向股东配售安排')
    S_INFO_USAGE = Column(VARCHAR(1000), comment='募集资金的用途')
    EFFECTIVEPERIOD = Column(VARCHAR(80), comment='决议的有效期')
    ANN_DATE_BOARD = Column(VARCHAR(8), comment='董事会预案公告日')
    ANN_DATE_SHAREHOLDER = Column(VARCHAR(8), comment='股东大会公告日')
    ANN_DATE_NDRC = Column(VARCHAR(8), comment='发改委获准公告日')
    ANN_DATE_CSIEC = Column(VARCHAR(8), comment='发审委通过公告日')
    ANN_DATE_SFC = Column(VARCHAR(8), comment='证监会核准公告日')
    ANN_DATE_IMPLEMENT = Column(VARCHAR(8), comment='实施公告日')


class BONDISSUEAUDITPROCESS(Base):
    """[废弃]中国债券发行行政许可审核进度"""
    __tablename__ = 'BONDISSUEAUDITPROCESS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(300), comment='公司名称(申请企业)')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    TYPE_CODE = Column(Numeric(9, 0), comment='审核类型代码')
    TYPE_NAME = Column(VARCHAR(300), comment='申请事项')
    S_INFO_PROCESS = Column(VARCHAR(1000), comment='说明')


class BONDISSUEREGISTRATION(Base):
    """中国债券发行注册额度"""
    __tablename__ = 'BONDISSUEREGISTRATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='[内部]公告日期')
    MEETING_DT = Column(VARCHAR(8), comment='注册会议日期')
    INT_AMOUNT = Column(Numeric(20, 4), comment='初始注册金额(亿元)')
    CHANGE_AMOUNT = Column(Numeric(20, 4), comment='变更后注册金额(亿元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    FILELOCATION = Column(VARCHAR(40), comment='备案场所')
    FILENUM = Column(VARCHAR(80), comment='文件号')
    END_DT_EFFECTIVE = Column(VARCHAR(8), comment='有效期截止日')
    END_DT_FIRSTISSUE = Column(VARCHAR(8), comment='首期发行截止日')
    IS_INSTALL = Column(Numeric(1, 0), comment='是否可分期发行')
    LEADUNDERWRITER = Column(VARCHAR(500), comment='主承销商名称')
    TYPE_CODE = Column(Numeric(9, 0), comment='注册债券类型代码')
    ABS_MANAGERID = Column(VARCHAR(100), comment='ABS产品管理人公司ID')
    ABS_MANAGER = Column(VARCHAR(10), comment='ABS产品管理人/SPV')
    ABS_NAME = Column(VARCHAR(200), comment='ABS产品名称')
    NUM = Column(Numeric(1, 0), comment='[内部]序号')


class BONDISSUEREGISTUNDERWRITERS(Base):
    """中国债券发行注册承销商"""
    __tablename__ = 'BONDISSUEREGISTUNDERWRITERS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    UNDERWRITER = Column(VARCHAR(200), comment='承销商名称')
    UNDERWRITERID = Column(VARCHAR(10), comment='承销商公司ID')
    B_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(5, 0), comment='最新标志')
    BONDTYPE_CODE = Column(Numeric(9, 0), comment='债券类型代码')
    BONDTYPE = Column(VARCHAR(40), comment='债券类型')


class BONDKEYTERMDURATION(Base):
    """中国债券关键年期久期"""
    __tablename__ = 'BONDKEYTERMDURATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='债券Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    DURA1M = Column(Numeric(20, 8), comment='1月久期')
    DURA3M = Column(Numeric(20, 8), comment='3月久期')
    DURA6M = Column(Numeric(20, 8), comment='6月久期')
    DURA1Y = Column(Numeric(20, 8), comment='1年久期')
    DURA2Y = Column(Numeric(20, 8), comment='2年久期')
    DURA3Y = Column(Numeric(20, 8), comment='3年久期')
    DURA4Y = Column(Numeric(20, 8), comment='4年久期')
    DURA5Y = Column(Numeric(20, 8), comment='5年久期')
    DURA7Y = Column(Numeric(20, 8), comment='7年久期')
    DURA9Y = Column(Numeric(20, 8), comment='9年久期')
    DURA10Y = Column(Numeric(20, 8), comment='10年久期')
    DURA15Y = Column(Numeric(20, 8), comment='15年久期')
    DURA20Y = Column(Numeric(20, 8), comment='20年久期')
    DURA30Y = Column(Numeric(20, 8), comment='30年久期')
    DURAST = Column(Numeric(20, 8), comment='短边久期')
    DURALG = Column(Numeric(20, 8), comment='长边久期')


class BONDMARKETNEWS(Base):
    """债券市场"""
    __tablename__ = 'BONDMARKETNEWS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='唯一性标识')
    PUBLISHDATE = Column(DateTime, comment='Wind发布时间')
    TITLE = Column(VARCHAR(1200), comment='新闻标题')
    CONTENT = Column(TEXT(2147483647), comment='新闻内容')
    SOURCE = Column(VARCHAR(200), comment='新闻来源')
    URL = Column(VARCHAR(1200), comment='新闻链接')
    SECTIONS = Column(VARCHAR(3000), comment='新闻栏目')
    AREACODES = Column(TEXT(2147483647), comment='相关地区')
    WINDCODES = Column(TEXT(2147483647), comment='相关公司')
    INDUSTRYCODES = Column(TEXT(2147483647), comment='相关行业')
    SECTERCODES = Column(TEXT(2147483647), comment='概念板块')
    KEYWORDS = Column(VARCHAR(3000), comment='新闻关键字')
    OPDATE = Column(DateTime, comment='入库时间')
    OPMODE = Column(VARCHAR(1), comment='操作类型')
    MKTSENTIMENTS = Column(TEXT(2147483647), comment='市场情绪')


class BONDNEGATIVENEWS(Base):
    """债券负面新闻"""
    __tablename__ = 'BONDNEGATIVENEWS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='唯一性标识')
    PUBLISHDATE = Column(DateTime, comment='Wind发布时间')
    TITLE = Column(VARCHAR(1200), comment='新闻标题')
    CONTENT = Column(TEXT(2147483647), comment='新闻内容')
    SOURCE = Column(VARCHAR(200), comment='新闻来源')
    URL = Column(VARCHAR(1200), comment='新闻链接')
    SECTIONS = Column(VARCHAR(3000), comment='新闻栏目')
    AREACODES = Column(TEXT(2147483647), comment='相关地区')
    WINDCODES = Column(TEXT(2147483647), comment='相关公司')
    INDUSTRYCODES = Column(TEXT(2147483647), comment='相关行业')
    SECTERCODES = Column(TEXT(2147483647), comment='概念板块')
    KEYWORDS = Column(VARCHAR(3000), comment='新闻关键字')
    OPDATE = Column(DateTime, comment='入库时间')
    OPMODE = Column(VARCHAR(1), comment='操作类型')
    MKTSENTIMENTS = Column(TEXT(2147483647), comment='市场情绪')


class BONDPOSITIVENEWS(Base):
    """债券正面"""
    __tablename__ = 'BONDPOSITIVENEWS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='唯一性标识')
    PUBLISHDATE = Column(DateTime, comment='Wind发布时间')
    TITLE = Column(VARCHAR(1200), comment='新闻标题')
    CONTENT = Column(TEXT(2147483647), comment='新闻内容')
    SOURCE = Column(VARCHAR(200), comment='新闻来源')
    URL = Column(VARCHAR(1200), comment='新闻链接')
    SECTIONS = Column(VARCHAR(3000), comment='新闻栏目')
    AREACODES = Column(TEXT(2147483647), comment='相关地区')
    WINDCODES = Column(TEXT(2147483647), comment='相关公司')
    INDUSTRYCODES = Column(TEXT(2147483647), comment='相关行业')
    SECTERCODES = Column(TEXT(2147483647), comment='概念板块')
    KEYWORDS = Column(VARCHAR(3000), comment='新闻关键字')
    OPDATE = Column(DateTime, comment='入库时间')
    OPMODE = Column(VARCHAR(1), comment='操作类型')
    MKTSENTIMENTS = Column(TEXT(2147483647), comment='市场情绪')


class CBINDEXDESCRIPTION(Base):
    """中国债券指数基本资料"""
    __tablename__ = 'CBINDEXDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(80), comment='证券简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='指数名称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8), comment='基期')
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4), comment='基点')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    S_INFO_INDEX_WEIGHTSRULE = Column(VARCHAR(10), comment='加权方式')
    INCOME_PROCESSING_METHOD = Column(VARCHAR(20), comment='收益处理方式')
    S_INFO_INDEXSTYLE = Column(VARCHAR(40), comment='指数风格')
    S_INFO_INDEX_ENAME = Column(VARCHAR(200), comment='指数英文名称')
    WEIGHT_TYPE = Column(VARCHAR(100), comment='权重类型')
    WEIGHTING_METHOD_START_DATE = Column(VARCHAR(8), comment='加权方式起始日期')
    WEIGHTING_METHOD_END_DATE = Column(VARCHAR(8), comment='加权方式终止日期')
    COMPONENT_STOCKS_NUM = Column(Numeric(5, 0), comment='成份股数量')
    INDEX_REGION_CODE = Column(Numeric(9, 0), comment='指数区域代码')
    INDEX_CATEGORY_CODE = Column(Numeric(9, 0), comment='指数类别代码')
    EXPONENTIAL_SCALE_CODE = Column(Numeric(9, 0), comment='指数规模代码')
    WEIGHT_TYPE_CODE = Column(Numeric(9, 0), comment='权重类型代码')
    MARKET_OWN_CODE = Column(Numeric(9, 0), comment='所属市场代码')
    INCOME_PROCESSING_METHOD_CODE = Column(Numeric(9, 0), comment='收益处理方式代码')
    EXPIRE_DATE = Column(VARCHAR(8), comment='终止发布日期')


class CBINDEXDESCRIPTIONWIND(Base):
    """万得中国债券指数基本资料"""
    __tablename__ = 'CBINDEXDESCRIPTIONWIND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='指数名称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8), comment='基期')
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4), comment='基点')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    S_INFO_INDEX_WEIGHTSRULE = Column(VARCHAR(10), comment='加权方式')
    INCOME_PROCESSING_METHOD = Column(VARCHAR(20), comment='收益处理方式')
    S_INFO_INDEXSTYLE = Column(VARCHAR(40), comment='指数风格')
    S_INFO_INDEX_ENAME = Column(VARCHAR(200), comment='指数英文名称')
    WEIGHT_TYPE = Column(VARCHAR(100), comment='权重类型')
    COMPONENT_STOCKS_NUM = Column(Numeric(5, 0), comment='成份股数量')
    INDEX_REGION_CODE = Column(Numeric(9, 0), comment='指数区域代码')
    INDEX_CATEGORY_CODE = Column(Numeric(9, 0), comment='指数类别代码')
    EXPONENTIAL_SCALE_CODE = Column(Numeric(9, 0), comment='指数规模代码')
    WEIGHT_TYPE_CODE = Column(Numeric(9, 0), comment='权重类型代码')
    MARKET_OWN_CODE = Column(Numeric(9, 0), comment='所属市场代码')
    INCOME_PROCESSING_METHOD_CODE = Column(Numeric(9, 0), comment='收益处理方式代码')
    EXPIRE_DATE = Column(VARCHAR(8), comment='终止发布日期')
    INDEX_CATEGORY_TYPE = Column(VARCHAR(40), comment='指数类别')
    INDEX_INTRO = Column(VARCHAR, comment='指数简介')


class CBINDEXDESCRIPTIONZL(Base):
    """中国债券指数基本资料(增量)"""
    __tablename__ = 'CBINDEXDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(80), comment='证券简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='指数名称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8), comment='基期')
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4), comment='基点')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    S_INFO_INDEX_WEIGHTSRULE = Column(VARCHAR(10), comment='加权方式')
    INCOME_PROCESSING_METHOD = Column(VARCHAR(20), comment='收益处理方式')
    S_INFO_INDEXSTYLE = Column(VARCHAR(40), comment='指数风格')
    S_INFO_INDEX_ENAME = Column(VARCHAR(200), comment='指数英文名称')
    WEIGHT_TYPE = Column(VARCHAR(100), comment='权重类型')
    WEIGHTING_METHOD_START_DATE = Column(VARCHAR(8), comment='加权方式起始日期')
    WEIGHTING_METHOD_END_DATE = Column(VARCHAR(8), comment='加权方式终止日期')
    COMPONENT_STOCKS_NUM = Column(Numeric(5, 0), comment='成份股数量')
    INDEX_REGION_CODE = Column(Numeric(9, 0), comment='指数区域代码')
    INDEX_CATEGORY_CODE = Column(Numeric(9, 0), comment='指数类别代码')
    EXPONENTIAL_SCALE_CODE = Column(Numeric(9, 0), comment='指数规模代码')
    WEIGHT_TYPE_CODE = Column(Numeric(9, 0), comment='权重类型代码')
    MARKET_OWN_CODE = Column(Numeric(9, 0), comment='所属市场代码')
    INCOME_PROCESSING_METHOD_CODE = Column(Numeric(9, 0), comment='收益处理方式代码')
    EXPIRE_DATE = Column(VARCHAR(8), comment='终止发布日期')


class CBINDEXEODPRICES(Base):
    """中国债券指数日行情"""
    __tablename__ = 'CBINDEXEODPRICES'
    __table_args__ = (
        Index('IDX_CBINDEXEODPRICES_CODE_DT', 'S_INFO_WINDCODE', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价(点)')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(点)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(点)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(点)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(点)')
    S_DQ_CHANGE = Column(Numeric(20, 4), comment='涨跌(点)')
    S_DQ_PCTCHANGE = Column(Numeric(20, 4), comment='涨跌幅(%)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class CBINDEXEODPRICESWIND(Base):
    """万得中国债券指数日行情"""
    __tablename__ = 'CBINDEXEODPRICESWIND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价(点)')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(点)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(点)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(点)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(点)')
    S_DQ_CHANGE = Column(Numeric(20, 4), comment='涨跌(点)')
    S_DQ_PCTCHANGE = Column(Numeric(20, 4), comment='涨跌幅(%)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class CBINDEXMEMBERS(Base):
    """中国债券指数成分"""
    __tablename__ = 'CBINDEXMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CBINDEXMEMBERSQL(Base):
    """None"""
    __tablename__ = 'CBINDEXMEMBERSQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_CON_WINDCODE = Column(VARCHAR(40))
    S_CON_INDATE = Column(VARCHAR(8))
    S_CON_OUTDATE = Column(VARCHAR(8))
    CUR_SIGN = Column(Numeric(1, 0))


class CBINDEXMEMBERSWIND(Base):
    """万得中国债券指数成份"""
    __tablename__ = 'CBINDEXMEMBERSWIND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CBINDEXMEMBERSZL(Base):
    """中国债券指数成分(增量)"""
    __tablename__ = 'CBINDEXMEMBERSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CBINDEXWEIGHT(Base):
    """中国债券指数权重"""
    __tablename__ = 'CBINDEXWEIGHT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份债Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    I_WEIGHT = Column(Numeric(20, 8), comment='权重')


class CCBONDAMOUNT(Base):
    """中国可转换债券份额变动"""
    __tablename__ = 'CCBONDAMOUNT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_CHANGEDATE = Column(VARCHAR(8), comment='变动日期')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CHANGEREASON = Column(VARCHAR(4), comment='变动原因代码')
    B_INFO_OUTSTANDINGBALANCE = Column(Numeric(15, 2), comment='债券份额(万元)')
    TURN_INTO_SHARE = Column(Numeric(20, 4), comment='已转成股份数')


class CCBONDCONVERSION(Base):
    """中国可转债转股"""
    __tablename__ = 'CCBONDCONVERSION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CONV_CODE = Column(VARCHAR(10), comment='转股申报代码')
    CONV_NAME = Column(VARCHAR(10), comment='转股简称')
    CONV_PRICE = Column(Numeric(20, 4), comment='转股价格')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    CONV_STARTDATE = Column(VARCHAR(8), comment='自愿转换期起始日')
    CONV_ENDDATE = Column(VARCHAR(8), comment='自愿转换期截止日')
    TRADE_DT_LAST = Column(VARCHAR(8), comment='可转债停止交易日')
    FORCED_CONV_DATE = Column(VARCHAR(8), comment='强制转换日')
    FORCED_CONV_PRICE = Column(Numeric(20, 4), comment='强制转换价格')
    REL_CONV_MONTH = Column(Numeric(20, 4), comment='相对转股期(月)')
    ISFORCED = Column(Numeric(5, 0), comment='是否强制转股')
    FORCED_CONV_REASON = Column(VARCHAR(500), comment='强制转换原因')


class CCBONDCONVERSIONRESET(Base):
    """中国可转债修正条款"""
    __tablename__ = 'CCBONDCONVERSIONRESET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    START_DT = Column(VARCHAR(8), comment='特别修正起始时间')
    END_DT = Column(VARCHAR(8), comment='特别修正结束时间')
    MAX_PERIOD = Column(Numeric(5, 0), comment='修正触发计算最大时间区间(天)')
    PERIOD = Column(Numeric(5, 0), comment='修正触发计算时间区间(天)')
    TRIGGERRATIO = Column(Numeric(20, 4), comment='特别修正触发比例(%)')
    MIN_PRICE = Column(VARCHAR(800), comment='修正后转股价格底线说明')
    IS_AVG = Column(Numeric(5, 0), comment='参考价格是否为算术平均价')
    TIMESLIMIT = Column(VARCHAR(40), comment='修正次数限制')
    IS_TIMES = Column(Numeric(5, 0), comment='是否有时点修正条款')
    TIMES = Column(Numeric(20, 4), comment='时点数')
    TIMES_ITEM = Column(VARCHAR(800), comment='时点修正文字条款')
    EXITRESET_PCT = Column(Numeric(20, 4), comment='特别修正幅度(%)')
    IS_EXITRESET = Column(Numeric(1, 0), comment='是否有特别向下修正条款')


class CCBONDISSUANCE(Base):
    """中国可转债发行"""
    __tablename__ = 'CCBONDISSUANCE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CB_INFO_PREPLANDATE = Column(VARCHAR(8), comment='预案公告日')
    CB_INFO_SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    CB_ISSUE_ANNCELSTDATE = Column(VARCHAR(8), comment='上市公告日')
    CB_INFO_LISTEDDATE = Column(VARCHAR(8), comment='上市日期')
    CB_INFO_LISTDATE = Column(VARCHAR(20), comment='方案进度')
    CB_INFO_ISSEPARATION = Column(Numeric(7, 3), comment='是否分离交易可转债')
    CB_INFO_DISTRIBUTO = Column(VARCHAR(1000), comment='分销商ID')
    CB_INFO_RECOMMENDER = Column(VARCHAR(200), comment='上市推荐人')
    CB_CLAUSE_ISCHAINTEREST = Column(Numeric(5, 0), comment='利率是否随存款利率调整')
    CB_CLAUSE_ISCOMINTEREST = Column(Numeric(5, 0), comment='是否有利息补偿条款')
    CB_CLAUSE_COMINTEREST = Column(Numeric(20, 4), comment='补偿利率(%)')
    CB_CLAUSE_COMINTERESTITEM = Column(VARCHAR(500), comment='利率补偿说明')
    CB_CLAUSE_CONVERSIONITEM = Column(VARCHAR(1000), comment='初始转股价条款')
    CB_CLAUSE_CONVCHANGEITEM = Column(VARCHAR(1000), comment='转股价格调整条款')
    CB_CLAUSE_CONVMONTH = Column(VARCHAR(1000), comment='转换期条款')
    CB_CLAUSE_INICONVPRICE = Column(Numeric(20, 4), comment='初始转股价格')
    CB_CLAUSE_INICONVPROPORTION = Column(Numeric(20, 4), comment='初始转股价溢价比例(%)')
    CB_CLAUSE_CALLITEM = Column(VARCHAR(1000), comment='回售条款')
    CB_CLAUSE_RESET_ITEM = Column(VARCHAR(1000), comment='赎回条款')
    CB_CLAUSE_RESETITEM = Column(VARCHAR(1000), comment='特别向下修正条款')
    CB_CLAUSE_RATIONITEM = Column(VARCHAR(2000), comment='向原股东配售安排条款')
    CB_LIST_PASSDATE = Column(VARCHAR(8), comment='发审委通过公告日')
    CB_LIST_PERMITDATE = Column(VARCHAR(8), comment='证监会核准公告日')
    CB_LIST_ANNOUNCEDATE = Column(VARCHAR(8), comment='发行公告日')
    CB_LIST_ANNOCEDATE = Column(VARCHAR(8), comment='发行结果公告日')
    CB_LIST_TYPE = Column(VARCHAR(40), comment='发行方式')
    CB_LIST_FEE = Column(Numeric(20, 4), comment='发行费用')
    CB_LIST_RATIONDATE = Column(VARCHAR(8), comment='老股东配售日期')
    CB_LIST_RATIONCHKINDATE = Column(VARCHAR(8), comment='老股东配售股权登记日')
    CB_LIST_RATIONPAYMTDATE = Column(VARCHAR(8), comment='老股东配售缴款日')
    CB_LIST_RATIONCODE = Column(VARCHAR(10), comment='老股东配售代码')
    CB_LIST_RATIONNAME = Column(VARCHAR(40), comment='老股东配售简称')
    CB_LIST_RATIONPRICE = Column(Numeric(20, 4), comment='老股东配售价格')
    CB_LIST_RATIONRATIODE = Column(Numeric(20, 4), comment='老股东配售比例分母')
    CB_LIST_RATIONRATIOMO = Column(Numeric(20, 4), comment='老股东配售比例分子')
    CB_LIST_RATIONVOL = Column(Numeric(20, 4), comment='向老股东配售数量(张)')
    CB_LIST_ORIGINALS = Column(Numeric(20, 4), comment='老股东配售户数')
    CB_LIST_DTONL = Column(VARCHAR(8), comment='上网发行日期')
    CB_LIST_PCHASECODEONL = Column(VARCHAR(10), comment='上网发行申购代码')
    CB_LIST_PCHNAMEONL = Column(VARCHAR(40), comment='上网发行申购名称')
    CB_LIST_PCHPRICEONL = Column(Numeric(20, 4), comment='上网发行申购价格')
    CB_LIST_ISSUEVOLONL = Column(Numeric(20, 4), comment='上网发行数量(不含优先配售)(张)')
    CB_LIST_CODEONL = Column(Numeric(20, 4), comment='上网发行配号总数')
    CB_LIST_EXCESSPCHONL = Column(Numeric(20, 4), comment='上网发行超额认购倍数(不含优先配售)')
    CB_RESULT_EFSUBSCRPOFF = Column(Numeric(20, 4), comment='网上有效申购户数(不含优先配售)')
    CB_RESULT_SUCRATEOFF = Column(Numeric(20, 4), comment='网上有效申购手数(不含优先配售)')
    CB_LIST_DATEINSTOFF = Column(VARCHAR(8), comment='网下向机构投资者发行日期')
    CB_LIST_VOLINSTOFF = Column(Numeric(20, 4), comment='网下向机构投资者发行数量(不含优先配售)(张)')
    CB_RESULT_SUCRATEON = Column(Numeric(20, 10), comment='网上中签率(不含优先配售)(%)')
    CB_LIST_EFFECTPCHVOLOFF = Column(Numeric(20, 4), comment='网下有效申购手数(不含优先配售)')
    CB_LIST_EFFPCHOF = Column(Numeric(20, 4), comment='网下有效申购户数(不含优先配售)')
    CB_LIST_SUCRATEOFF = Column(Numeric(20, 4), comment='网下中签率(不含优先配售)(%)')
    CB_LIST_PRERATIONVOL = Column(Numeric(20, 4), comment='网下优先配售数量（张）')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='转股公司ID')
    CB_LIST_ISSUESIZE = Column(Numeric(20, 4), comment='发行规模(万元)')
    CB_LIST_ISSUEQUANTITY = Column(Numeric(20, 4), comment='发行数量(万张)')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')
    MINUNLINE_NO = Column(Numeric(20, 4), comment='网下最小申购数量(机构)')
    DEPUNLINE_RATIO = Column(VARCHAR(8), comment='网下定金比例(机构)')
    MAXUNLINE_NO = Column(Numeric(20, 4), comment='网下最大申购数量(机构)')
    UNLINE_UD = Column(VARCHAR(40), comment='网下申购累进单位说明')
    IS_CONVERTIBLE_BONDS = Column(Numeric(1, 0), comment='是否可转债')
    MINUNLINE_PUBLIC = Column(Numeric(20, 4), comment='网上最小申购数量(公众)(元)')
    MAXUNLINE_PUBLIC = Column(Numeric(20, 4), comment='网上最大申购数量(公众)(万元)')
    B_INFO_TERM_YEAR_ = Column(Numeric(10, 0), comment='债券期限(年)')
    B_INFO_INTERESTTYPE = Column(VARCHAR(20), comment='利率类型')
    B_INFO_COUPONRATE = Column(Numeric(20, 4), comment='利率(%)')
    B_INFO_INTERESTFREQUENCY = Column(VARCHAR(20), comment='付息频率')
    CB_RESULT_SUCRATEON2 = Column(Numeric(24, 8), comment='[内部]网上中签率(不含优先配售)(%)')
    B_INFO_COUPONTXT = Column(VARCHAR(1000), comment='利率说明')
    S_RATIOANNCEDATE = Column(VARCHAR(8), comment='网上中签率公告日')
    S_RATIODATE = Column(VARCHAR(8), comment='网上中签结果公告日')


class CCBONDREDEMPTIONPRICERATE(Base):
    """中国可转债有条件赎回价格和触发比例"""
    __tablename__ = 'CCBONDREDEMPTIONPRICERATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REDEMPTIONPRICE = Column(Numeric(20, 4), comment='赎回价')
    B_INFO_BGNDT = Column(VARCHAR(8), comment='起始日期')
    B_INFO_ENDDT = Column(VARCHAR(8), comment='截止日期')
    B_INFO_TRNSRT = Column(Numeric(20, 4), comment='触发比例(%)')


class CCBONDREDEMPTIONPRICERATEQL(Base):
    """None"""
    __tablename__ = 'CCBONDREDEMPTIONPRICERATEQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    B_INFO_WINDCODE = Column(VARCHAR(40))
    B_INFO_REDEMPTIONPRICE = Column(Numeric(20, 4))
    B_INFO_BGNDT = Column(VARCHAR(8))
    B_INFO_ENDDT = Column(VARCHAR(8))
    B_INFO_TRNSRT = Column(Numeric(20, 4))


class CCBONDREDEMPTIONPRICERATEZL(Base):
    """中国可转债有条件赎回价格和触发比例(增量)"""
    __tablename__ = 'CCBONDREDEMPTIONPRICERATEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REDEMPTIONPRICE = Column(Numeric(20, 4), comment='赎回价')
    B_INFO_BGNDT = Column(VARCHAR(8), comment='起始日期')
    B_INFO_ENDDT = Column(VARCHAR(8), comment='截止日期')
    B_INFO_TRNSRT = Column(Numeric(20, 4), comment='触发比例(%)')


class CCBONDREPURCHASEPRICERATE(Base):
    """中国可转债有条件回售价格和触发比例"""
    __tablename__ = 'CCBONDREPURCHASEPRICERATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REPURCHASEPRICE = Column(Numeric(20, 4), comment='回售价')
    B_INFO_BGNDT = Column(VARCHAR(8), comment='起始日期')
    B_INFO_ENDDT = Column(VARCHAR(8), comment='截止日期')
    B_INFO_TRNSRT = Column(Numeric(20, 4), comment='触发比例(%)')


class CCBONDREPURCHASEPRICERATEZL(Base):
    """中国可转债有条件回售价格和触发比例(增量)"""
    __tablename__ = 'CCBONDREPURCHASEPRICERATEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_INFO_REPURCHASEPRICE = Column(Numeric(20, 4), comment='回售价')
    B_INFO_BGNDT = Column(VARCHAR(8), comment='起始日期')
    B_INFO_ENDDT = Column(VARCHAR(8), comment='截止日期')
    B_INFO_TRNSRT = Column(Numeric(20, 4), comment='触发比例(%)')


class CCBONDVALUATION(Base):
    """中国可转债衍生指标"""
    __tablename__ = 'CCBONDVALUATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CB_ANAL_ACCRUEDDAYS = Column(Numeric(20, 4), comment='已计息天数')
    CB_ANAL_ACCRUEDINTEREST = Column(Numeric(20, 4), comment='应计利息')
    CB_ANAL_PTM = Column(Numeric(20, 4), comment='剩余期限（年）')
    CB_ANAL_CURYIELD = Column(Numeric(20, 4), comment='当期收益率')
    CB_ANAL_YTM = Column(Numeric(20, 4), comment='纯债到期收益率')
    CB_ANAL_STRBVALUE = Column(Numeric(20, 4), comment='纯债价值')
    CB_ANAL_STRBPREMIUM = Column(Numeric(20, 4), comment='纯债溢价')
    CB_ANAL_STRBPREMIUMRATIO = Column(Numeric(20, 4), comment='纯债溢价率')
    CB_ANAL_CONVPRICE = Column(Numeric(20, 4), comment='转股价')
    CB_ANAL_CONVRATIO = Column(Numeric(20, 6), comment='转股比例')
    CB_ANAL_CONVVALUE = Column(Numeric(20, 4), comment='转股价值')
    CB_ANAL_CONVPREMIUM = Column(Numeric(20, 4), comment='转股溢价')
    CB_ANAL_CONVPREMIUMRATIO = Column(Numeric(20, 4), comment='转股溢价率')


class CGBBENCHMARK(Base):
    """中国国债基准收益率"""
    __tablename__ = 'CGBBENCHMARK'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='利率(%)')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘利率(%)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高利率(%)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低利率(%)')


class CLIENTOFCREDITRATINGAGENCY(Base):
    """中国债券评级机构客户名单"""
    __tablename__ = 'CLIENTOFCREDITRATINGAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='评级机构ID')
    S_INFO_CREDITRATINGAGENCY = Column(VARCHAR(10), comment='评级机构代码')
    CLIENT_COMPNAME = Column(VARCHAR(200), comment='公司(客户)名称')
    CLIENT_COMPCODE = Column(VARCHAR(10), comment='公司(客户)ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class CNBDINVESTORSTATISTICS(Base):
    """中债登债券投资者统计"""
    __tablename__ = 'CNBDINVESTORSTATISTICS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    MONTHS = Column(VARCHAR(8), comment='月份')
    INVESTORTYPE = Column(VARCHAR(80), comment='投资者类型')
    TRUSTTYPE = Column(VARCHAR(80), comment='托管类型')
    NUM_ENDMONTHS = Column(Numeric(20, 4), comment='月末数量')
    NUM_INCYEAR = Column(Numeric(20, 4), comment='年增数量')
    NUM_ENDYEAR = Column(Numeric(20, 4), comment='上年末数量')


class COMPANYLINEOFCREDIT(Base):
    """中国债券发行主体银行授信额度"""
    __tablename__ = 'COMPANYLINEOFCREDIT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    CREDIT_NO = Column(Numeric(24, 8), comment='授信额度(亿元)')
    CREDIT_USED = Column(Numeric(24, 8), comment='已使用授信额度(亿元)')
    CREDIT_UNUSED = Column(Numeric(24, 8), comment='未使用授信额度(亿元)')
    CREDIT_COMPNAME = Column(VARCHAR(200), comment='授信机构名称')
    CREDIT_COMPID = Column(VARCHAR(10), comment='授信机构公司ID（废弃）')
    CRNCY_CODE = Column(VARCHAR(20), comment='货币代码')


class CREDITRATINGDESCRIPTION(Base):
    """中国债券信用等级定义"""
    __tablename__ = 'CREDITRATINGDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_EST_RATING_INST = Column(VARCHAR(40), comment='信用等级')
    B_EST_INSTITUTE = Column(VARCHAR(10), comment='评估机构代码')
    B_TYPCODE = Column(VARCHAR(40), comment='评级类型')
    INVEST_GRADE = Column(VARCHAR(100), comment='投资等级')
    GRADE_DEFINITION = Column(VARCHAR(1000), comment='含义')
    GRADE_NUM = Column(Numeric(20, 4), comment='等级序号')
    COMMON_GRADE = Column(Numeric(3, 0), comment='通用等级')


class CREDITRATINGDESCRIPTIONZL(Base):
    """信用等级定义(增量)"""
    __tablename__ = 'CREDITRATINGDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    B_EST_RATING_INST = Column(VARCHAR(40), comment='信用等级')
    B_EST_INSTITUTE = Column(VARCHAR(10), comment='评估机构代码')
    B_TYPCODE = Column(VARCHAR(40), comment='评级类型')
    INVEST_GRADE = Column(VARCHAR(100), comment='投资等级')
    GRADE_DEFINITION = Column(VARCHAR(1000), comment='含义')
    GRADE_NUM = Column(Numeric(20, 4), comment='等级序号')
    COMMON_GRADE = Column(Numeric(3, 0), comment='通用等级')


class INTERESTRATEINTRODUCTION(Base):
    """中国债券利率品种简介条款"""
    __tablename__ = 'INTERESTRATEINTRODUCTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='品种ID')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    MEMO = Column(TEXT(2147483647), comment='条款')
    CUR_SIGN = Column(Numeric(1, 0), comment='是否最新')
