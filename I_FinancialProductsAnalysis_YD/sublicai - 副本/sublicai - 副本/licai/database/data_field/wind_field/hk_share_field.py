# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/10/21 11:07
# @Author  : lisl3
# @File    : hk_share_field.py
# @Project : cscfist
# @Function: 中国港股
# @Version : V0.0.1
# ------------------------------
from sqlalchemy import Column, VARCHAR, Numeric, TEXT, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class HKBALANCESHEETSIMPLE(Base):
    """香港股票资产负债表（简表）"""
    __tablename__ = 'HKBALANCESHEETSIMPLE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    REPORT_TYPE = Column(VARCHAR(100), comment='报告类型代码')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='截至日期')
    TOT_CUR_ASSETS = Column(Numeric(20, 4), comment='流动资产合计')
    TOT_NON_CUR_ASSETS = Column(Numeric(20, 4), comment='非流动资产合计')
    TOT_ASSETS = Column(Numeric(20, 4), comment='总资产')
    TOT_CUR_LIAB = Column(Numeric(20, 4), comment='流动负债合计')
    TOT_NON_CUR_LIAB = Column(Numeric(20, 4), comment='非流动负债合计')
    TOTAL_LIABILITIES = Column(Numeric(20, 4), comment='总负债')
    PARSH_INT = Column(Numeric(20, 4), comment='股东权益')
    MINORITY_INT = Column(Numeric(20, 4), comment='少数股东权益')
    TOT_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益合计')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ACC_STA_CODE = Column(Numeric(9, 0), comment='会计准则类型代码')


class HKCASHFLOWSIMPLE(Base):
    """香港股票现金流量表（简表）"""
    __tablename__ = 'HKCASHFLOWSIMPLE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    REPORT_TYPE = Column(VARCHAR(100), comment='报告类型代码')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额')
    NET_CASH_FLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额')
    NET_CASH_FLOWS_FUND_ACT = Column(Numeric(20, 4), comment='筹资活动产生现金流量净额(融资活动产生的现金流量净额)')
    NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物净增加额')
    CRNCY_CODE = Column(VARCHAR(20), comment='货币代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ACC_STA_CODE = Column(Numeric(9, 0), comment='会计准则类型代码')


class HKCHANGECOMPANYNAME(Base):
    """香港股票公司名称变更"""
    __tablename__ = 'HKCHANGECOMPANYNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    COMP_NAME_ENG = Column(VARCHAR(200), comment='公司英文名称')


class HKCOMPANYINFO(Base):
    """香港股票上市公司基本资料"""
    __tablename__ = 'HKCOMPANYINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')
    COMP_NAME_ENG = Column(VARCHAR(100), comment='英文名称')
    FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    LEGALREPRESENTATIVE = Column(VARCHAR(38), comment='法人代表')
    REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    BRIEFING = Column(VARCHAR(1000), comment='公司简介')
    BUSINESSSCOPE = Column(VARCHAR(2000), comment='经营范围')
    BUSINESSSCOPE_ENG = Column(VARCHAR(2000), comment='经营范围(英文)')
    TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    DISCLOSERID = Column(VARCHAR(500), comment='信息披露人ID')
    CRNY_CODE = Column(VARCHAR(10), comment='货币代码')
    ADDRESS = Column(VARCHAR(200), comment='注册地址')
    OFFICE = Column(VARCHAR(200), comment='办公地址')
    PHONE = Column(VARCHAR(50), comment='电话')
    FAX = Column(VARCHAR(50), comment='传真')
    COUNTRY = Column(VARCHAR(20), comment='国家及地区')
    WEBSITE = Column(VARCHAR(80), comment='主页')
    EMAIL = Column(VARCHAR(80), comment='电子邮箱')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ACCOUNT_CURRENCY = Column(VARCHAR(10), comment='记账币种')


class HKCOMPTYPEOFREPORTPERIOD(Base):
    """香港股票报告期公司类型"""
    __tablename__ = 'HKCOMPTYPEOFREPORTPERIOD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    ENDDATE = Column(VARCHAR(8), comment='截止日期(报告期)')
    S_INFO_COMPTYPE = Column(VARCHAR(10), comment='公司类型代码')


class HKCONCEPTUALPLATE(Base):
    """香港股票概念板块"""
    __tablename__ = 'HKCONCEPTUALPLATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(40), comment='板块代码')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')


class HKEQUITYSTRUC(Base):
    """香港股票股本结构"""
    __tablename__ = 'HKEQUITYSTRUC'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DATE = Column(VARCHAR(8), comment='变动日期1(除权日或上市日)')
    ISSUED_SHARES = Column(Numeric(20, 4), comment='已发行股本(万股)')
    MAINLAND_OUTSTD_SHR = Column(Numeric(20, 4), comment='内地流通股(万股)')
    HK_OUTSTD_SHR = Column(Numeric(20, 4), comment='香港流通股(万股)')
    OVERSEAS_OUTSTD_SHR = Column(Numeric(20, 4), comment='境外流通股(万股)')
    NON_TRADABLE_SHR = Column(Numeric(20, 4), comment='非流通股(万股)')
    PREFERREDSHARE = Column(Numeric(20, 4), comment='优先股(万股)')
    OUTSTANDINGSHARES = Column(Numeric(20, 4), comment='流通优先股(万股)')
    TREASURYSTOCK = Column(Numeric(20, 4), comment='库存股(万股)')
    SHARE_CHANGEREASON = Column(VARCHAR(40), comment='股本变动原因')
    OVERSEAS_SHR_CNTRYCODE = Column(VARCHAR(10), comment='境外上市国家或地区代码')


class HKETFDESCRIPTION(Base):
    """香港ETF基本资料"""
    __tablename__ = 'HKETFDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象 ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_NAME = Column(VARCHAR(400), comment='基金名称')
    F_INFO_FUNDCODE = Column(VARCHAR(10), comment='公司id')
    F_INFO_FULLNAME = Column(VARCHAR(400), comment='基金名称')
    F_INFO_SETUPDATE = Column(VARCHAR(8), comment='成立日')
    F_INFO_MATURITYDATE = Column(VARCHAR(8), comment='到期日')
    F_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    F_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')
    S_INFO_TRADEUNIT = Column(Numeric(20, 0), comment='交易单位')
    CRNCY_CODE = Column(VARCHAR(10), comment='交易币种')
    F_INFO_STATUS = Column(Numeric(9, 0), comment='存续状态')
    F_INFO_MGRCOMP = Column(VARCHAR(100), comment='公司名称')


class HKETFEODPRICE(Base):
    """香港ETF日行情"""
    __tablename__ = 'HKETFEODPRICE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额')
    S_DQ_ADJPRECLOSE = Column(Numeric(20, 4), comment='复权昨收盘价(元)')
    S_DQ_ADJOPEN = Column(Numeric(20, 4), comment='复权开盘价(元)')
    S_DQ_ADJHIGH = Column(Numeric(20, 4), comment='复权最高价(元)')
    S_DQ_ADJLOW = Column(Numeric(20, 4), comment='复权最低价(元)')
    S_DQ_ADJCLOSE = Column(Numeric(20, 4), comment='复权收盘价(元)')
    S_DQ_ADJFACTOR = Column(Numeric(24, 8), comment='复权因子')
    S_PCT_CHG = Column(Numeric(20, 4), comment='涨跌幅(%)')


class HKETFNAV(Base):
    """香港ETF净值"""
    __tablename__ = 'HKETFNAV'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    PRICE_DATE = Column(VARCHAR(8), comment='日期')
    F_NAV_UNIT = Column(Numeric(24, 8), comment='份额净值')
    F_NAV_ACCUMULATED = Column(Numeric(24, 8), comment='公布份额累计净值')
    F_NAV_DIVACCUMULATED = Column(Numeric(20, 4), comment='份额累计分红')
    F_NAV_ADJFACTOR = Column(Numeric(20, 8), comment='复权因子')
    CRNCY_CODE = Column(VARCHAR(10), comment='净值货币代码')


class HKEXCALENDAR(Base):
    """香港交易所交易日历"""
    __tablename__ = 'HKEXCALENDAR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DAYS = Column(VARCHAR(8), comment='日期')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class HKFINANCIALINDICATOR(Base):
    """香港股票财务指标"""
    __tablename__ = 'HKFINANCIALINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    REPORT_TYPE = Column(VARCHAR(100), comment='报告类型')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    EPS_BASIC = Column(Numeric(20, 8), comment='每股收益-基本')
    EPS_DILUTED = Column(Numeric(20, 8), comment='每股收益-稀释')
    BPS = Column(Numeric(20, 8), comment='每股净资产')
    GRPS = Column(Numeric(22, 4), comment='每股总营业收入')
    CASH_FLOWS_OPERA_ACTIV_PER = Column(Numeric(20, 8), comment='每股经营性现金流量')
    NET_PROFIT_RATE = Column(Numeric(22, 4), comment='净利润率')
    GROSSPROFITMARGIN = Column(Numeric(22, 4), comment='销售毛利率')
    OPPROFIT_RATE = Column(Numeric(22, 4), comment='营业利润率')
    PROFIT_BEF_TAX_RATE = Column(Numeric(20, 4), comment='税前利润率(%)')
    ROE = Column(Numeric(20, 4), comment='平均净资产收益率')
    ROA = Column(Numeric(20, 4), comment='平均总资产报酬率')
    ROIC = Column(Numeric(22, 4), comment='投入资本回报率ROIC')
    EFFE_INCOME_TAX_RATE = Column(Numeric(22, 4), comment='有效所得税率')
    OCFTOOR = Column(Numeric(22, 4), comment='经营活动产生的现金流量净额/总营业收入')
    DEBTTOEQUITY = Column(Numeric(22, 4), comment='产权比率')
    ASSETSTOEQUITY = Column(Numeric(22, 4), comment='权益乘数')
    DEBTTOASSETS = Column(Numeric(22, 4), comment='资产负债率')
    TOT_LIAB_INVESTCAPITAL = Column(Numeric(20, 4), comment='总负债/投入资本(%)')
    PARSH_INT_INVESTCAPITAL = Column(Numeric(22, 4), comment='归属母公司股东权益/投入资本')
    QUICK_RATIO = Column(Numeric(20, 4), comment='速动比率(倍)')
    CURRENT_RATIO = Column(Numeric(20, 4), comment='流动比率(倍)')
    CASHTOLIQDEBT = Column(Numeric(20, 4), comment='货币资金／流动负债 ')
    NON_CUR_ASSETS_TO_EQUITY = Column(Numeric(20, 4), comment='非流动负债合计/股东权益(%)')
    FFO_TO_TOT_LIAB = Column(Numeric(22, 4), comment='经营活动产生的现金流量净额/总负债')
    FFO_TO_TOT_CUR_LIAB = Column(Numeric(22, 4), comment='经营活动产生的现金流量净额/流动负债合计')
    INVTURN = Column(Numeric(20, 4), comment='存货周转率(倍)')
    CATURN = Column(Numeric(22, 4), comment='流动资产周转率')
    FATURN = Column(Numeric(22, 4), comment='固定资产周转率')
    ASSETSTURN = Column(Numeric(22, 4), comment='总资产周转率')
    INPUT_COSTS = Column(Numeric(22, 4), comment='投入资本')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class HKFUTURESDESCRIPTIONZL(Base):
    """香港期货基本资料(增量)"""
    __tablename__ = 'HKFUTURESDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券中文简称')
    S_INFO_ENAME = Column(VARCHAR(200), comment='证券英文简称')
    FS_INFO_SCCODE = Column(VARCHAR(20), comment='标准合约代码')
    FS_INFO_TYPE = Column(Numeric(1, 0), comment='合约类型')
    S_INFO_EXCHMARKET = Column(VARCHAR(20), comment='交易所')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='最后交易日期')
    FS_INFO_DLMONTH = Column(VARCHAR(10), comment='交割月份')


class HKGSDBALANCESHEET(Base):
    """香港股票资产负债表(GSD)"""
    __tablename__ = 'HKGSDBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='截至日期')
    REPORT_TYPE = Column(Numeric(9, 0), comment='报告类型代码')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    TOT_CUR_ASSETS = Column(Numeric(20, 4), comment='流动资产合计')
    CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物')
    TRADABLE_FIN_ASSETS = Column(Numeric(20, 4), comment='短期投资(交易性金融资产)')
    OTH_SHORT_INV = Column(Numeric(20, 4), comment='其他短期投资')
    AR_TOTAL = Column(Numeric(20, 4), comment='应收款项合计')
    STM_BS = Column(Numeric(20, 4), comment='应收账款及票据')
    OTH_RCV = Column(Numeric(20, 4), comment='其他应收款')
    INVENTORIES = Column(Numeric(20, 4), comment='存货')
    OTH_CUR_ASSETS = Column(Numeric(20, 4), comment='其他流动资产合计')
    NON_CUR_ASSETS = Column(Numeric(20, 4), comment='非流动资产合计')
    NET_OTH_FIX_ASSETS = Column(Numeric(20, 4), comment='固定资产净值')
    EQUITY_INV = Column(Numeric(20, 4), comment='权益性投资')
    HELD_TO_MTY_INVEST = Column(Numeric(20, 4), comment='持有至到期投资')
    AVAIL_FOR_SALE_INV = Column(Numeric(20, 4), comment='可供出售投资')
    OTH_LONG_INV = Column(Numeric(20, 4), comment='其他长期投资')
    GOODWILL_INTANG_ASSETS = Column(Numeric(20, 4), comment='商誉及无形资产')
    GOODWILL = Column(Numeric(20, 4), comment='其中:商誉')
    RIGHT_LAND_USAGE = Column(Numeric(20, 4), comment='[内部]租赁土地')
    OTH_NONCURRENT_ASSETS = Column(Numeric(20, 4), comment='其他非流动资产合计')
    TOT_ASSETS = Column(Numeric(20, 4), comment='总资产')
    CUR_LIAB = Column(Numeric(20, 4), comment='流动负债合计')
    AP_NOTE = Column(Numeric(20, 4), comment='应付账款及票据')
    TAXES_SURCHARGES_PAYABLE = Column(Numeric(20, 4), comment='应交税金')
    TRADABLE_FIN_LIAB = Column(Numeric(20, 4), comment='交易性金融负债')
    STLOANS_LTLOANS_CURDUE = Column(Numeric(20, 4), comment='短期借贷及长期借贷当期到期部分')
    OTH_CUR_LIAB = Column(Numeric(20, 4), comment='其他流动负债')
    NON_CUR_LIAB = Column(Numeric(20, 4), comment='非流动负债合计')
    LT_BORROW = Column(Numeric(20, 4), comment='长期借贷')
    OTH_NON_CUR_LIAB = Column(Numeric(20, 4), comment='其他非流动负债合计')
    TOTAL_LIABILITIES = Column(Numeric(20, 4), comment='总负债')
    PRFSHARE = Column(Numeric(20, 4), comment='优先股')
    COMSHARE = Column(Numeric(20, 4), comment='普通股股本(股本)')
    RESERVE = Column(Numeric(20, 4), comment='储备')
    PREMIUM_STOCK = Column(Numeric(20, 4), comment='股本溢价')
    RETAINED_EARN = Column(Numeric(20, 4), comment='留存收益')
    OTH_RESERVE = Column(Numeric(20, 4), comment='其他储备')
    TREASURYSHARE = Column(Numeric(20, 4), comment='库存股')
    OTH_COM_INCOME = Column(Numeric(20, 4), comment='其他综合性收益')
    TOT_COM_EQUITY = Column(Numeric(20, 4), comment='普通股权益总额')
    PARSH_INT = Column(Numeric(20, 4), comment='股东权益')
    MINORITY_INT = Column(Numeric(20, 4), comment='少数股东权益')
    TOT_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益合计')
    TOT_LIAB_EQY = Column(Numeric(20, 4), comment='总负债及总权益')
    CASH_INTER_BAL = Column(Numeric(20, 4), comment='现金及同业结存')
    DUE_BANK = Column(Numeric(20, 4), comment='存放同业')
    NET_LOANS = Column(Numeric(20, 4), comment='客户贷款及垫款净额')
    DEPOSIT_BANK = Column(Numeric(20, 4), comment='银行同业存款')
    FUNDS_LENT = Column(Numeric(20, 4), comment='拆出资金')
    MORT_SEC = Column(Numeric(20, 4), comment='抵押担保证券')
    SALE_LOAN = Column(Numeric(20, 4), comment='可供出售贷款')
    TOT_DEPOSITS = Column(Numeric(20, 4), comment='总存款')
    LOANS_OTH_BANKS = Column(Numeric(20, 4), comment='拆入资金')
    SECURED_FIN = Column(Numeric(20, 4), comment='抵押担保融资')
    REINSUR_PAY = Column(Numeric(20, 4), comment='应付再保')
    REINSUR_RECE = Column(Numeric(20, 4), comment='应收再保')
    INSUR_PRE_REC = Column(Numeric(20, 4), comment='应收保费')
    DEFER_COST = Column(Numeric(20, 4), comment='递延保单获得成本')
    INSUR_LIAB = Column(Numeric(20, 4), comment='保险合同负债')
    INVEST_LIAB = Column(Numeric(20, 4), comment='投资合同负债')
    OTH_INV = Column(Numeric(20, 4), comment='其他投资')
    OTH_ASSETS = Column(Numeric(20, 4), comment='其他资产')
    OTH_LIAB = Column(Numeric(20, 4), comment='其他负债')
    S_INFO_COMPTYPE = Column(VARCHAR(1), comment='报告期公司类型代码')
    S_MEMO = Column(VARCHAR(2000), comment='备注')


class HKGSDCASHFLOW(Base):
    """香港股票现金流量表(GSD)"""
    __tablename__ = 'HKGSDCASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    BEGIN_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    REPORT_TYPE = Column(Numeric(9, 0), comment='报告类型代码')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    IS_CALC = Column(Numeric(1, 0), comment='是否计算值')
    CRNCY_CODE = Column(VARCHAR(20), comment='货币代码')
    NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额')
    NET_PROFIT_CS = Column(Numeric(20, 4), comment='净利润')
    PLUS_NET_DA = Column(Numeric(20, 4), comment='折旧与摊销')
    OP_CAP_CHANGE = Column(Numeric(20, 4), comment='营运资本变动')
    OTH_NONCASH_CHANGE = Column(Numeric(20, 4), comment='其他非现金调整')
    NET_CASH_FLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额')
    CASH_RECP_FIXASSET_SELL = Column(Numeric(20, 4), comment='出售固定资产收到的现金')
    LESS_CAP_EXPENSE = Column(Numeric(20, 4), comment='资本性支出')
    LESS_INV_INCR = Column(Numeric(20, 4), comment='投资增加')
    INV_DECR = Column(Numeric(20, 4), comment='投资减少')
    NET_OTH_ICF = Column(Numeric(20, 4), comment='其他投资活动产生的现金流量净额')
    NET_CASH_FLOWS_FUND_ACT = Column(Numeric(20, 4), comment='筹资活动产生现金流量净额(融资活动产生的现金流量净额)')
    DEBT_INCR = Column(Numeric(20, 4), comment='债务增加')
    LESS_DEBT_DECR = Column(Numeric(20, 4), comment='债务减少')
    CAP_INCR = Column(Numeric(20, 4), comment='股本增加')
    PLUS_NET_CAP_DECR = Column(Numeric(20, 4), comment='股本减少')
    TOT_DIV_PAID = Column(Numeric(20, 4), comment='支付的股利合计')
    NET_OTH_FCF = Column(Numeric(20, 4), comment='其他筹资活动产生的现金流量净额')
    E_CHANGE_EFFECT = Column(Numeric(20, 4), comment='汇率变动影响')
    OTH_CF_ADJUST = Column(Numeric(20, 4), comment='其他现金流量调整')
    NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物净增加额')
    CASH_CASH_EQU_BEG_PERIOD = Column(Numeric(20, 4), comment='现金及现金等价物期初余额')
    CASH_CASH_EQU_END_PERIOD = Column(Numeric(20, 4), comment='现金及现金等价物期末余额')
    S_MENO = Column(VARCHAR(2000), comment='备注')
    S_INFO_COMPTYPE = Column(VARCHAR(1), comment='报告期公司类型代码')


class HKGSDINCOME(Base):
    """香港股票损益表(GSD)"""
    __tablename__ = 'HKGSDINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    BEGIN_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    REPORT_TYPE = Column(Numeric(9, 0), comment='报告类型代码')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    IS_CALC = Column(Numeric(1, 0), comment='是否计算值')
    CRNCY_CODE = Column(VARCHAR(20), comment='货币代码')
    TOT_OPER_REV = Column(Numeric(20, 4), comment='总营业收入')
    BUS_INC = Column(Numeric(20, 4), comment='主营收入')
    OTH_BUS_INC = Column(Numeric(20, 4), comment='其他营业收入')
    REV_COMM_INC = Column(Numeric(20, 4), comment='扣除贷款损失准备前收入')
    PROV_LOAN_LOSS = Column(Numeric(20, 4), comment='贷款损失准备')
    PREMIUMS_EARNED = Column(Numeric(20, 4), comment='净已赚保费')
    TRADE_INC_NET = Column(Numeric(20, 4), comment='交易账户净收入')
    INT_INVERST_INC = Column(Numeric(20, 4), comment='利息及股息收入')
    REV_RENT = Column(Numeric(20, 4), comment='租金收入')
    TENANT_REIM_EXP = Column(Numeric(20, 4), comment='租户认缴物业维护综合费')
    GAIN_SALE_REAL_ESTATE = Column(Numeric(20, 4), comment='房地产销售收入')
    MTG_INC = Column(Numeric(20, 4), comment='抵押贷款相关收入')
    NET_INT_INC = Column(Numeric(20, 4), comment='利息净收入')
    BROKER_COMM_INC = Column(Numeric(20, 4), comment='经纪佣金收入')
    UW_IB_INC = Column(Numeric(20, 4), comment='承销与投资银行费收入')
    AUM_INC = Column(Numeric(20, 4), comment='资产管理费收入')
    TRADE_INC = Column(Numeric(20, 4), comment='自营业务收入')
    NET_FEE_INC = Column(Numeric(20, 4), comment='手续费及佣金净收入')
    FEE_INC = Column(Numeric(20, 4), comment='手续费及佣金收入')
    FEE_EXP = Column(Numeric(20, 4), comment='减：手续费及佣金开支')
    PREMIUMS_INC = Column(Numeric(20, 4), comment='毛承保保费及保单费收入')
    RESERVE_CHG = Column(Numeric(20, 4), comment='减:未到期责任准备金变动')
    PREMIUM_CEDED = Column(Numeric(20, 4), comment='减:分出保费')
    TOT_OPER_COST = Column(Numeric(20, 4), comment='总营业支出')
    BUS_COST = Column(Numeric(20, 4), comment='营业成本')
    OPER_EXP = Column(Numeric(20, 4), comment='营业开支')
    POLICY_INT = Column(Numeric(20, 4), comment='保单持有人利益')
    SGA_EXP = Column(Numeric(20, 4), comment='销售、行政及一般费用')
    DIST_EXP = Column(Numeric(20, 4), comment='营销费用')
    ADMIN_EXP = Column(Numeric(20, 4), comment='行政(管理)费用')
    RD_EXP = Column(Numeric(20, 4), comment='研发费用')
    OTH_BUS_EXP = Column(Numeric(20, 4), comment='其他营业费用合计')
    OPPROFIT = Column(Numeric(20, 4), comment='营业利润')
    GROSSMARGIN = Column(Numeric(20, 4), comment='毛利')
    INT_INC = Column(Numeric(20, 4), comment='利息收入')
    INT_EXP = Column(Numeric(20, 4), comment='利息支出')
    INVEST_GAIN = Column(Numeric(20, 4), comment='权益性投资损益')
    OTH_NONPO_INC = Column(Numeric(20, 4), comment='其他非经营性损益')
    NONRECURITEM_BEF_PROFITS = Column(Numeric(20, 4), comment='非经常项目前利润')
    UNUSUAL_ITEMS = Column(Numeric(20, 4), comment='非经常项目损益')
    INC_PRETAX = Column(Numeric(20, 4), comment='除税前利润(除税前盈利)')
    TAX = Column(Numeric(20, 4), comment='所得税')
    MINORITY_INT_INC = Column(Numeric(20, 4), comment='少数股东损益')
    NONCONTINUOUS_NET_OP = Column(Numeric(20, 4), comment='持续经营净利润')
    DISC_OPER = Column(Numeric(20, 4), comment='非持续经营净利润')
    OTH_SPEC_ITEM = Column(Numeric(20, 4), comment='其他特殊项')
    NET_PROFIT_CS = Column(Numeric(20, 4), comment='净利润')
    DVD_PFD_ADJ = Column(Numeric(20, 4), comment='优先股利及其他调整项')
    NP_BELONGTO_COMMONSH = Column(Numeric(20, 4), comment='归属普通股东净利润')
    CI_BELONGTO_COMMONSH = Column(Numeric(20, 4), comment='归属普通股东综合收益')
    TOT_CI = Column(Numeric(20, 4), comment='综合收益总值')
    INC_AFTTAX = Column(Numeric(20, 4), comment='除税后利润(除税后但未计少数股东权益之盈利)')
    FAIRVALUE_CHG = Column(Numeric(20, 4), comment='公平值变动损益')
    S_INFO_COMPTYPE = Column(VARCHAR(1), comment='报告期公司类型代码')
    S_MEMO = Column(VARCHAR(1000), comment='备注')
    FISCAL_YEAR = Column(VARCHAR(8), comment='会计年度')
    EBITDA = Column(Numeric(20, 4), comment='EBITDA')
    EMPLOYEE_REMUNERATION = Column(Numeric(20, 4), comment='其中:员工薪酬')
    DEPRECIATION_AMORTIZATION = Column(Numeric(20, 4), comment='其中:折旧及摊销')


class HKINCOMESIMPLE(Base):
    """香港股票利润表（简表）"""
    __tablename__ = 'HKINCOMESIMPLE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    REPORT_TYPE = Column(VARCHAR(100), comment='报告类型')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型代码')
    FISCALYEAR = Column(VARCHAR(8), comment='会计年度')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    TOT_OPER_REV = Column(Numeric(20, 4), comment='总营业收入')
    TOT_OPER_COST = Column(Numeric(20, 4), comment='总营业支出')
    OPPROFIT = Column(Numeric(20, 4), comment='营业利润')
    PROFIT_BEF_TAX = Column(Numeric(20, 4), comment='除税前利润(除税前盈利)')
    LESS_TAX = Column(Numeric(20, 4), comment='所得税')
    MINORITY_INT_INC = Column(Numeric(20, 4), comment='少数股东损益')
    NET_PROFIT_CS = Column(Numeric(20, 4), comment='净利润')
    NP_BELONGTO_COMMONSH = Column(Numeric(20, 4), comment='归属普通股东净利润')
    CRNCY_CODE = Column(VARCHAR(20), comment='货币代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ACC_STA_CODE = Column(Numeric(9, 0), comment='会计准则类型代码')


class HKINDEXDESCRIPTION(Base):
    """香港股票指数基本资料"""
    __tablename__ = 'HKINDEXDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40))
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='指数名称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8), comment='基期')
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4), comment='基点')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    S_INFO_INDEX_STYLE = Column(VARCHAR(40), comment='指数风格')
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
    INCOME_PROCESSING_METHOD = Column(Numeric(9, 0), comment='收益处理方式代码')
    EXPIRE_DATE = Column(VARCHAR(8), comment='终止发布日期')


class HKINDEXDESCRIPTIONZL(Base):
    """香港股票指数基本资料(增量)"""
    __tablename__ = 'HKINDEXDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='证券代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='指数名称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8), comment='基期')
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4), comment='基点')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    S_INFO_INDEX_STYLE = Column(VARCHAR(40), comment='指数风格')
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
    INCOME_PROCESSING_METHOD = Column(Numeric(9, 0), comment='收益处理方式代码')
    EXPIRE_DATE = Column(VARCHAR(8), comment='终止发布日期')


class HKINDEXEODPRICES(Base):
    """香港股票指数日行情"""
    __tablename__ = 'HKINDEXEODPRICES'
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


class HKSCMEMBERS(Base):
    """香港港股通成分股"""
    __tablename__ = 'HKSCMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_SECTOR = Column(VARCHAR(10), comment='所属板块代码')


class HKSHAREAGENCY(Base):
    """香港股票中介机构"""
    __tablename__ = 'HKSHAREAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券id')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    AGENCYNAME = Column(VARCHAR(200), comment='机构名称')
    AGENCYCODE = Column(VARCHAR(10), comment='机构公司ID')
    TYPE_CODE = Column(VARCHAR(10), comment='关系类型代码')
    SCP = Column(VARCHAR(50), comment='业务范围')
    START_DT = Column(VARCHAR(8), comment='起使日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
    OP_DATE = Column(VARCHAR(8), comment='操作日期')


class HKSHAREAGENCYHOLDINGS(Base):
    """港股市场中介持股统计"""
    __tablename__ = 'HKSHAREAGENCYHOLDINGS'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='持股日期')
    HKSC_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='港股通持股数量(万股)')
    SHHKSC_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='沪市港股通持股数量(万股)')
    SZHKSC_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='深市港股通持股数量(万股)')
    HKAGENCY_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='香港本地中介机构持股数量(万股)')
    CAGENCY_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='中资中介机构持股数量(万股)')
    IAGENCYT_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='国际中介机构持股数量(万股)')
    HKSC_HOLDER_QUANTITY_PCT = Column(Numeric(20, 4), comment='港股通持股占比')
    SHHKSC_HOLDER_QUANTITY_PCT = Column(Numeric(20, 4), comment='沪市港股通持股占比')
    SZHKSC_HOLDER_QUANTITY_PCT = Column(Numeric(20, 4), comment='深市港股通持股占比')
    HKAGENCY_HOLDER_QUANTITY_PCT = Column(Numeric(20, 4), comment='香港本地中介机构持股占比')
    CAGENCY_HOLDER_QUANTITY_PCT = Column(Numeric(20, 4), comment='中资中介机构持股占比')
    IAGENCY_HOLDER_QUANTITY_PCT = Column(Numeric(20, 4), comment='国际中介机构持股占比')
    TOP5_HOLDER_CONCENTRATION = Column(Numeric(20, 4), comment='Top5持股集中度')
    TOP10_HOLDER_CONCENTRATION = Column(Numeric(20, 4), comment='Top10持股集中度')


class HKSHAREAUDITOPINION(Base):
    """香港股票财报审计意见"""
    __tablename__ = 'HKSHAREAUDITOPINION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    BEGIN_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    AUDIT_STD = Column(Numeric(9, 0), comment='会计准则类型代码')
    S_STMNOTE_AUDIT_AGENCY = Column(VARCHAR(300), comment='审计机构名称')
    S_STMNOTE_AUDIT_CATEGORY = Column(VARCHAR(40), comment='审计意见类型')
    AUDIT_CTNT = Column(TEXT(2147483647), comment='非标审计意见内容')


class HKSHAREBANKINDICATOR(Base):
    """香港股票银行专用指标"""
    __tablename__ = 'HKSHAREBANKINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='资本充足率(%)')
    CORE_CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='核心资本充足率(%)')
    NPL_RATIO = Column(Numeric(20, 4), comment='不良贷款比例-5级分类(%)')
    LOAN_DEPO_RATIO = Column(Numeric(20, 4), comment='存贷款比例(%)')
    TOTAL_LOAN = Column(Numeric(20, 4), comment='贷款总额')
    TOTAL_DEPOSIT = Column(Numeric(20, 4), comment='存款总额')
    LOAN_LOSS_PROVISION = Column(Numeric(20, 4), comment='贷款呆帐准备金')
    BAD_LOAD_FIVE_CLASS = Column(Numeric(20, 4), comment='不良贷款余额-5级分类')
    NPL_PROVISION_COVERAGE = Column(Numeric(20, 4), comment='不良贷款拨备覆盖率-5级分类(%)')
    COST_INCOME_RATIO = Column(Numeric(20, 4), comment='成本收入比(%)')
    NET_CAPITAL = Column(Numeric(20, 4), comment='资本净额')
    CORE_CAPI_NET_AMOUNT = Column(Numeric(20, 4), comment='核心资本净额')
    RISK_WEIGHT_ASSET = Column(Numeric(20, 4), comment='加权风险资产净额')
    INTEREST_BEARING_ASSET = Column(Numeric(20, 4), comment='生息资产')
    NET_INTEREST_MARGIN = Column(Numeric(20, 4), comment='净息差(%)')
    NET_INTEREST_SPREAD = Column(Numeric(20, 4), comment='净利差(%)')
    LOANRESERVESRATIO = Column(Numeric(20, 4), comment='贷款减值准备对贷款总额比率(%)')
    CORETIER1_NET_CAPI = Column(Numeric(20, 4), comment='核心一级资本净额')
    TIER1_NET_CAPI = Column(Numeric(20, 4), comment='一级资本净额')
    NET_CAPITAL_2013 = Column(Numeric(20, 4), comment='资本净额(资本管理办法)')
    CORETIER1CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='核心一级资本充足率')
    TIER1CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='一级资本充足率')
    CAPI_ADE_RATIO_2013 = Column(Numeric(20, 4), comment='资本充足率(资本管理办法)')
    RISK_WEIGHT_NET_ASSET_2013 = Column(Numeric(20, 4), comment='加权风险资产净额(资本管理办法)')


class HKSHAREBUSINESSDATA(Base):
    """None"""
    __tablename__ = 'HKSHAREBUSINESSDATA'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='日期')
    S_INFO_WINDCODE = Column(VARCHAR(20), comment='上市代码')
    INDICATOR_NAME = Column(VARCHAR(80), comment='指标名称')
    INDICATOR_VALUE = Column(Numeric(20, 4), comment='指标数据')
    YOY = Column(Numeric(20, 4), comment='同比(%)')
    INDICATOR_UNIT = Column(VARCHAR(40), comment='[内部]指标单位')
    MOM = Column(Numeric(20, 4), comment='环比(%)')
    PROJECT_ID = Column(VARCHAR(10), comment='项目ID')
    FREQUENCY_CODE = Column(Numeric(9, 0), comment='频率代码')
    NUMBER_TYPECODE = Column(Numeric(9, 0), comment='数量类型代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class HKSHARECAPITALIZATION(Base):
    """香港股票发行数量"""
    __tablename__ = 'HKSHARECAPITALIZATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日')
    ANN_DT = Column(VARCHAR(8), comment='公告日')
    S_ISSUEAMOUNT = Column(Numeric(20, 4), comment='发行股份数')
    RESTRICTED_SHR = Column(Numeric(20, 4), comment='限售股数')
    FLOAT_SHR = Column(Numeric(20, 4), comment='无限售股份数')
    LIST_NON_TRADABLE_SHR = Column(Numeric(20, 4), comment='其中:待上市流通股数')
    NON_TRADABLE_SHR = Column(Numeric(20, 4), comment='非流通股份数')
    S_SHARE_CHANGEREASON = Column(VARCHAR(100), comment='[内部]股本变动原因')


class HKSHARECHANGENAME(Base):
    """香港股票名称变更"""
    __tablename__ = 'HKSHARECHANGENAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券名称')
    S_INFO_NAME_ENG = Column(VARCHAR(200), comment='证券英文名称')


class HKSHARECOMPANYHOLDSHARES(Base):
    """香港股票控股参股"""
    __tablename__ = 'HKSHARECOMPANYHOLDSHARES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    RELATIONS_CODE = Column(VARCHAR(40), comment='关联关系代码')
    S_CAPITALOPERATION_COMAINBUS = Column(VARCHAR(700), comment='被参控公司主营业务')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_CAPITALOPERATION_COMPANYID = Column(VARCHAR(10), comment='被参控公司ID')
    S_CAPITALOPERATION_AMOUNT = Column(Numeric(24, 8), comment='投资金额(万元)')
    OPERATIONCRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    VOTING_RIGHTS = Column(Numeric(20, 4), comment='表决权比例')
    IS_CONSOLIDATE = Column(Numeric(5, 0), comment='是否纳入报表合并范围')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_CAPITALOPERATION_COREGCAP = Column(Numeric(24, 8), comment='被参股公司注册资本(万元)')
    OPERATIONCRNCY_CODE2 = Column(VARCHAR(10), comment='货币代码2')
    S_CAPITALOPERATION_COMPANYNAME = Column(VARCHAR(100), comment='被参控公司名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class HKSHARECONSEPTION(Base):
    """香港股票概念板块分类"""
    __tablename__ = 'HKSHARECONSEPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券id')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    HS_IND_CODE = Column(VARCHAR(50), comment='行业或类别代码')
    ENTRY_DT = Column(VARCHAR(8), comment='起始日期')
    REMOVE_DT = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
    OP_DATE = Column(VARCHAR(8), comment='操作日期')


class HKSHAREDATEOFBOARDMEETING(Base):
    """香港股票董事会会议日期"""
    __tablename__ = 'HKSHAREDATEOFBOARDMEETING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    MEET_DT = Column(VARCHAR(8), comment='会议日期')
    FST_MEET_DT = Column(VARCHAR(8), comment='首次披露会议日期')
    MEET_CTNT = Column(VARCHAR(200), comment='事项')
    PERIOD = Column(VARCHAR(200), comment='期间说明')
    END_DT = Column(VARCHAR(8), comment='截止日')
    S_MONTHS = Column(VARCHAR(200), comment='期间间隔')
    TEL_MEET = Column(TEXT(2147483647), comment='电话会议概要')


class HKSHAREDESCRIPTION(Base):
    """香港股票基本资料"""
    __tablename__ = 'HKSHAREDESCRIPTION'
    __table_args__ = (
        Index('INDEX_SECURITYTYPE', 'SECURITYTYPE'),
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_ISINCODE = Column(VARCHAR(40), comment='[内部]ISIN代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券中文简称')
    S_INFO_NAME_ENG = Column(VARCHAR(200), comment='[内部]证券英文简称')
    S_INFO_FULLNAME = Column(VARCHAR(100), comment='[内部]证券中文全称')
    S_INFO_FULLNAME_ENG = Column(VARCHAR(200), comment='[内部]证券英文全称')
    SECURITYCLASS = Column(Numeric(9, 0), comment='品种大类代码')
    SECURITYSUBCLASS = Column(Numeric(9, 0), comment='品种细类代码')
    SECURITYTYPE = Column(VARCHAR(10), comment='品种类型(兼容)')
    S_INFO_COUNTRYCODE = Column(VARCHAR(10), comment='国家及地区代码')
    S_INFO_EXCHANGE_ENG = Column(VARCHAR(40), comment='交易所英文简称')
    S_INFO_EXCHANGE = Column(VARCHAR(40), comment='交易所名称(兼容)')
    S_INFO_LISTBOARD = Column(VARCHAR(10), comment='上市板')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    S_INFO_STATUS = Column(Numeric(9, 0), comment='存续状态')
    CRNCY_CODE = Column(VARCHAR(10), comment='交易币种')
    S_INFO_PAR = Column(Numeric(24, 8), comment='面值')
    MIN_PRC_CHG_UNIT = Column(Numeric(24, 8), comment='最小价格变动单位')
    S_INFO_UNITPERLOT = Column(Numeric(20, 4), comment='每手数量')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='开始交易日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='最后交易日期')
    S_INFO_LISTPRICE = Column(Numeric(24, 8), comment='挂牌价')
    IS_HKSC = Column(Numeric(5, 0), comment='是否在港股通范围内')
    ISTEMPORARYSYMBOL = Column(Numeric(5, 0), comment='是否并行临时代码')
    IS_H = Column(Numeric(1, 0), comment='是否是H股')


class HKSHAREENDLIST(Base):
    """香港股票终止上市"""
    __tablename__ = 'HKSHAREENDLIST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_DELISTDT = Column(VARCHAR(8))
    S_DELISTTYPE = Column(VARCHAR(40))


class HKSHAREENDLISTZL(Base):
    """香港股票终止上市(增量)"""
    __tablename__ = 'HKSHAREENDLISTZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DELISTDT = Column(VARCHAR(8), comment='退市日期')
    S_DELISTTYPE = Column(VARCHAR(40), comment='退市原因类型')


class HKSHAREEODDERIVATIVEINDEX(Base):
    """香港股票日行情估值指标"""
    __tablename__ = 'HKSHAREEODDERIVATIVEINDEX'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    FINANCIAL_TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    TRADE_CRNCY_CODE = Column(VARCHAR(10), comment='交易币种代码')
    TOT_SHR_TODAY = Column(Numeric(20, 4), comment='当日总股本')
    FLOAT_A_SHR_TODAY = Column(Numeric(20, 4), comment='当日流通股本')
    S_VAL_MV = Column(Numeric(20, 4), comment='当日总市值')
    S_DQ_MV = Column(Numeric(20, 4), comment='当日流通市值')
    S_DQ_CLOSE_TODAY = Column(Numeric(20, 4), comment='当日收盘价')
    S_PQ_HIGH_52W = Column(Numeric(20, 4), comment='52周最高价')
    S_PQ_LOW_52W = Column(Numeric(20, 4), comment='52周最低价')
    S_VAL_PB_NEW = Column(Numeric(20, 4), comment='市净率(PB)')
    S_VAL_PE_LYR = Column(Numeric(20, 4), comment='市盈率(PE,LYR)')
    S_VAL_PE_TTM = Column(Numeric(20, 4), comment='市盈率(PE,TTM)')
    S_VAL_PCF_OCFLYR = Column(Numeric(20, 4), comment='市现率(经营现金流LYR)')
    S_VAL_PCF_OCFTTM = Column(Numeric(20, 4), comment='市现率(经营现金流TTM)')
    S_VAL_PCF_NCFLYR = Column(Numeric(20, 4), comment='市现率(现金净流量LYR)')
    S_VAL_PCF_NCFTTM = Column(Numeric(20, 4), comment='市现率(现金净流量TTM)')
    S_VAL_PS_LYR = Column(Numeric(20, 4), comment='市销率(PS,LYR)')
    S_VAL_PS_TTM = Column(Numeric(20, 4), comment='市销率(PS,TTM)')
    S_DQ_TURN = Column(Numeric(20, 4), comment='换手率')
    CRNCY_CODE = Column(VARCHAR(10), comment='财务币种代码')
    NET_ASSETS_TODAY = Column(Numeric(20, 4), comment='当日净资产')
    NET_PROFIT_PARENT_COMP_LYR = Column(Numeric(20, 4), comment='归属母公司净利润(LYR)')
    NET_PROFIT_PARENT_COMP_TTM = Column(Numeric(20, 4), comment='归属母公司净利润(TTM)')
    NET_CASH_FLOWS_OPER_ACT_LYR = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额(LYR)')
    NET_CASH_FLOWS_OPER_ACT_TTM = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额(TTM)')
    OPER_REV_LYR = Column(Numeric(20, 4), comment='营业收入(LYR)')
    OPER_REV_TTM = Column(Numeric(20, 4), comment='营业收入(TTM)')
    NET_INCR_CASH_CASH_EQU_LYR = Column(Numeric(20, 4), comment='现金及现金等价物净增加额(LYR)')
    NET_INCR_CASH_CASH_EQU_TTM = Column(Numeric(20, 4), comment='现金及现金等价物净增加额(TTM)')


class HKSHAREEODPRICES(Base):
    """香港股票日行情"""
    __tablename__ = 'HKSHAREEODPRICES'
    __table_args__ = (
        Index('S_INFO_WINDCODE_Index', 'S_INFO_WINDCODE', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(元)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(元)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(元)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(元)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(股)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='前收盘价(元)')
    S_DQ_ADJPRECLOSE = Column(Numeric(20, 4), comment='复权昨收盘价(元)')
    S_DQ_ADJOPEN = Column(Numeric(20, 4), comment='复权开盘价(元)')
    S_DQ_ADJHIGH = Column(Numeric(20, 4), comment='复权最高价(元)')
    S_DQ_ADJLOW = Column(Numeric(20, 4), comment='复权最低价(元)')
    S_DQ_ADJCLOSE = Column(Numeric(20, 4), comment='复权收盘价(元)')
    S_DQ_ADJFACTOR = Column(Numeric(20, 8), comment='复权因子')
    S_DQ_AVGPRICE = Column(Numeric(20, 4), comment='均价(VWAP)')
    DIVIDEND_YIELD = Column(Numeric(20, 4), comment='股息率(废弃)')


class HKSHAREEQUITYRELATIONSHIPS(Base):
    """香港股票实际控制人"""
    __tablename__ = 'HKSHAREEQUITYRELATIONSHIPS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    RELATION_TYPE = Column(VARCHAR(40), comment='公司与披露方关系')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    S_HOLDER_CODE = Column(VARCHAR(10), comment='股东ID')
    S_HOLDER_TYPE = Column(Numeric(5, 0), comment='股东类型')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例(%)')
    IS_ACTUALCONTROLLER = Column(Numeric(5, 0), comment='股东是否为实际控制人')
    ACTUALCONTROLLER_TYPE = Column(VARCHAR(80), comment='实际控制人类型')
    ACTUALCONTROLLER_IS_ANN = Column(Numeric(5, 0), comment='股东是否为公布实际控制人')
    ACTUALCONTROLLER_INTRO = Column(VARCHAR(1000), comment='实际控制人简介')


class HKSHAREEVENT(Base):
    """香港股票权益事件"""
    __tablename__ = 'HKSHAREEVENT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='证券id')
    EVENT_TYPE = Column(VARCHAR(200), comment='事件类型')
    EX_DATE = Column(VARCHAR(8), comment='除权日')
    START_DATE = Column(VARCHAR(8), comment='截止过户起始日')
    END_DATE = Column(VARCHAR(8), comment='截止过户截止日')
    GM_DATE = Column(VARCHAR(8), comment='股东大会会议日期')
    PAYMENT_DATE = Column(VARCHAR(8), comment='现金发放日')
    BONUS_SHARE_D_DATE = Column(VARCHAR(8), comment='红股发送日')
    CASH_DIV_RATIO = Column(Numeric(20, 8), comment='派息比例(元)')
    BONUS_SHARE_RATIO = Column(Numeric(20, 8), comment='红股送转比例(股)')
    IN_SPECIE_RATIO = Column(Numeric(20, 8), comment='实物派送比例')
    BONUS_WARRANT_RATIO = Column(Numeric(20, 8), comment='红利认股权证派送比例(股)')
    RIGHT_ISSUE_RATIO = Column(Numeric(20, 8), comment='供股、公开发售比例(股)')
    RIGHT_ISSUE_PRICE = Column(Numeric(20, 4), comment='每股供股股份、发售股份价格(元)')
    CONSOLIDATION_RATIO = Column(Numeric(20, 8), comment='合并比例')
    SPLIT_RATIO = Column(Numeric(20, 8), comment='拆分比例')
    EXCHANGE_RATIO = Column(Numeric(20, 8), comment='换股比例')
    CANCELLATION_RATIO = Column(Numeric(20, 8), comment='削减比例')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    FANN_DATE = Column(VARCHAR(8), comment='首次公告日期')
    NANN_DATE = Column(VARCHAR(8), comment='最新公告日期')
    RSTART_DATE = Column(VARCHAR(8), comment='报告起始日')
    REND_DATE = Column(VARCHAR(8), comment='报告截止日')
    RE_TYPE = Column(Numeric(9, 0), comment='报告类型代码')
    BONUS_WARRANT_DATE = Column(VARCHAR(8), comment='认股权证发送日')
    IN_SPECIE_DATE = Column(VARCHAR(8), comment='实物股票发送日')
    RIGHT_ISSUE_D_DATE = Column(VARCHAR(8), comment='供股、公开发售股份发送日')
    BONUS_SHARE_L_DATE = Column(VARCHAR(8), comment='红股上市日')
    RIGHT_ISSUE_L_DATE = Column(VARCHAR(8), comment='供股股份、发售股份上市日')
    TRANSFER_RATIO = Column(Numeric(20, 8), comment='转增比例')
    PRESENT_RATIO = Column(Numeric(20, 8), comment='送股比例')
    MEMO = Column(VARCHAR(1000), comment='备注')
    S_INFO_WINDCODE1 = Column(VARCHAR(40), comment='辅助证券ID')
    DIVIDEND_CURRENCY = Column(VARCHAR(10), comment='派息原始币种')
    CASH_DIV_RATIO1 = Column(Numeric(20, 6), comment='派息比例(原始币种)')


class HKSHAREFINANCIALDERIVATIVE(Base):
    """香港股票财务衍生指标表"""
    __tablename__ = 'HKSHAREFINANCIALDERIVATIVE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    INTERVAL_LENGTH = Column(Numeric(20, 4), comment='区间长度(月)')
    FISCALYEAR = Column(VARCHAR(8), comment='会计年度(Wind判定)')
    REPORT_TYPE = Column(VARCHAR(20), comment='报告类型')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    TOT_SHR = Column(Numeric(20, 4), comment='期末总股本')
    OPPROFIT1 = Column(Numeric(20, 4), comment='营业利润(含价值变动损益)')
    OPERATEINCOME = Column(Numeric(20, 4), comment='经营活动净收益')
    INVESTINCOME = Column(Numeric(20, 4), comment='价值变动净收益')
    S_STM_IS = Column(Numeric(20, 4), comment='折旧与摊销')
    EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    FCFF = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)')
    FCFE = Column(Numeric(20, 4), comment='股权自由现金流量(FCFE)')
    EXINTERESTDEBT_CURRENT = Column(Numeric(20, 4), comment='无息流动负债')
    EXINTERESTDEBT_NONCURRENT = Column(Numeric(20, 4), comment='无息非流动负债')
    INTERESTDEBT = Column(Numeric(20, 4), comment='带息债务')
    NETDEBT = Column(Numeric(20, 4), comment='净债务')
    TANGIBLEASSET = Column(Numeric(20, 4), comment='有形资产')
    WORKINGCAPITAL = Column(Numeric(20, 4), comment='营运资金')
    NETWORKINGCAPITAL = Column(Numeric(20, 4), comment='营运流动资本')
    INVESTCAPITAL = Column(Numeric(20, 4), comment='全部投入资本')
    RETAINEDEARNINGS = Column(Numeric(20, 4), comment='留存收益')
    EPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益')
    EPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益')
    EPS_DILUTED2 = Column(Numeric(20, 4), comment='每股收益(期末摊薄)')
    EPS_DILUTED3 = Column(Numeric(20, 4), comment='每股收益(扣除／期末股本摊薄)')
    BPS = Column(Numeric(20, 4), comment='每股净资产')
    OCFPS = Column(Numeric(20, 4), comment='每股经营活动产生的现金流量净额')
    GRPS = Column(Numeric(20, 4), comment='每股营业总收入')
    ORPS = Column(Numeric(20, 4), comment='每股营业收入')
    SURPLUSCAPITALPS = Column(Numeric(20, 4), comment='每股资本公积')
    RETAINEDPS = Column(Numeric(20, 4), comment='每股留存收益')
    CFPS = Column(Numeric(20, 4), comment='每股现金流量净额')
    EBITPS = Column(Numeric(20, 4), comment='每股息税前利润')
    FCFFPS = Column(Numeric(20, 4), comment='每股企业自由现金流量')
    FCFEPS = Column(Numeric(20, 4), comment='每股股东自由现金流量')
    NETPROFITMARGIN = Column(Numeric(20, 4), comment='销售净利率')
    GROSSPROFITMARGIN = Column(Numeric(20, 4), comment='销售毛利率')
    COGSTOSALES = Column(Numeric(20, 4), comment='销售成本率')
    PROFITTOGR = Column(Numeric(20, 4), comment='净利润／营业总收入')
    SALEEXPENSETOGR = Column(Numeric(20, 4), comment='销售费用／营业总收入')
    ADMINEXPENSETOGR = Column(Numeric(20, 4), comment='行政(管理)费用／营业总收入')
    FINAEXPENSETOGR = Column(Numeric(20, 4), comment='财务费用／营业总收入')
    GCTOGR = Column(Numeric(20, 4), comment='营业总成本／营业总收入')
    OPTOGR = Column(Numeric(20, 4), comment='营业利润(含价值变动损益)／营业总收入')
    EBITTOGR = Column(Numeric(20, 4), comment='息税前利润／营业总收入')
    ROE = Column(Numeric(20, 4), comment='净资产收益率(平均)')
    ROE_DEDUCTED = Column(Numeric(20, 4), comment='净资产收益率(扣除平均)')
    ROA2 = Column(Numeric(20, 4), comment='总资产报酬率(平均)')
    ROA = Column(Numeric(20, 4), comment='总资产净利润(平均)')
    ROIC = Column(Numeric(20, 4), comment='投入资本回报率(平均)')
    ROE_YEARLY = Column(Numeric(20, 4), comment='年化净资产收益率')
    ROA2_YEARLY = Column(Numeric(20, 4), comment='年化总资产报酬率')
    ROA_YEARLY = Column(Numeric(20, 4), comment='年化总资产净利率')
    ROIC_YEARLY = Column(Numeric(20, 4), comment='年化投入资本回报率')
    OPERATEINCOMETOEBT = Column(Numeric(20, 4), comment='经营活动净收益／除税前利润')
    INVESTINCOMETOEBT = Column(Numeric(20, 4), comment='价值变动净收益／除税前利润')
    NONOPERATEPROFITTOEBT = Column(Numeric(20, 4), comment='营业外收支净额／除税前利润')
    TAXTOEBT = Column(Numeric(20, 4), comment='所得税／利润总额')
    CONTINUED_NET_PROFIT = Column(Numeric(20, 4), comment='持续经营净利润／除税后利润')
    NONNETOPTOTAXPROFIT = Column(Numeric(20, 4), comment='非持续经营净利润/除税后利润')
    OCFTOOR = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／营业收入')
    OCFTOOR1 = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／经营活动净收益')
    CAPITALIZEDTODA = Column(Numeric(20, 4), comment='资本支出／折旧和摊销')
    DEBTTOASSETS = Column(Numeric(20, 4), comment='资产负债率')
    ASSETSTOEQUITY = Column(Numeric(20, 4), comment='权益乘数')
    DUPONT_ASSETSTOEQUITY = Column(Numeric(20, 4), comment='权益乘数(用于杜邦分析)')
    CATOASSETS = Column(Numeric(20, 4), comment='流动资产／总资产')
    NCATOASSETS = Column(Numeric(20, 4), comment='非流动资产／总资产')
    TANGIBLEASSETSTOASSETS = Column(Numeric(20, 4), comment='有形资产／总资产')
    INTDEBTTOTOTALCAP = Column(Numeric(20, 4), comment='带息债务／全部投入资本')
    EQUITYTOTOTALCAPITAL = Column(Numeric(20, 4), comment='归属于母公司的股东权益／全部投入资本')
    CURRENTDEBTTODEBT = Column(Numeric(20, 4), comment='流动负债／负债合计')
    LONGDEBTODEBT = Column(Numeric(20, 4), comment='非流动负债／负债合计')
    CURRENT1 = Column(Numeric(20, 4), comment='流动比率')
    QUICK = Column(Numeric(20, 4), comment='速动比率')
    CASHRATIO = Column(Numeric(20, 4), comment='保守速动比率')
    OCFTOSHORTDEBT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／流动负债')
    DEBTTOEQUITY = Column(Numeric(20, 4), comment='产权比率')
    EQUITYTODEBT = Column(Numeric(20, 4), comment='归属于母公司的股东权益／负债合计')
    EQUITYTOINTERESTDEBT = Column(Numeric(20, 4), comment='归属于母公司的股东权益／带息债务')
    TANGIBLEASSETTODEBT = Column(Numeric(20, 4), comment='有形资产／负债合计')
    TANGASSETTOINTDEBT = Column(Numeric(20, 4), comment='有形资产／带息债务')
    TANGIBLEASSETTONETDEBT1 = Column(Numeric(20, 4), comment='有形资产／净债务')
    OCFTODEBT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／负债合计')
    OCFTOINTERESTDEBT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／带息债务')
    TANGIBLEASSETTONETDEBT2 = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／净债务')
    EBITTOINTEREST = Column(Numeric(20, 4), comment='已获利息倍数(EBIT／利息费用)')
    LONGDEBTTOWORKINGCAPITAL = Column(Numeric(20, 4), comment='长期债务与营运资金比率')
    EBITDATODEBT = Column(Numeric(20, 4), comment='息税折旧摊销前利润／负债合计')
    TURNDAYS = Column(Numeric(20, 4), comment='营业周期')
    INVTURNDAYS = Column(Numeric(20, 4), comment='存货周转天数')
    ARTURNDAYS = Column(Numeric(20, 4), comment='应收账款周转天数')
    INVTURN = Column(Numeric(20, 4), comment='存货周转率')
    ARTURN = Column(Numeric(20, 4), comment='应收账款周转率')
    CATURN = Column(Numeric(20, 4), comment='流动资产周转率')
    FATURN = Column(Numeric(20, 4), comment='固定资产周转率')
    ASSETSTURN = Column(Numeric(20, 4), comment='总资产周转率')
    OCFTOPROFIT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／营业利润(含)')
    CASHTOLIQDEBT = Column(Numeric(20, 4), comment='货币资金／流动负债')
    CASHTOLIQDEBTWITHINTEREST = Column(Numeric(20, 4), comment='货币资金／带息流动负债')
    OPTOLIQDEBT = Column(Numeric(20, 4), comment='营业利润／流动负债')
    OPTODEBT = Column(Numeric(20, 4), comment='营业利润／负债合计')
    PROFITTOOP = Column(Numeric(20, 4), comment='利润总额／营业总收入')
    NET_PROFIT5 = Column(Numeric(20, 4), comment='归属母公司的净利润／净利润')
    NET_TOTAL_PROFIT = Column(Numeric(20, 4), comment='净利润／利润总额')
    TOTAL_PROFIT_EBIT = Column(Numeric(20, 4), comment='利润总额／EBIT')
    YOYEPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益同比增长率')
    YOYEPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益同比增长率')
    YOYOCFPS = Column(Numeric(20, 4), comment='每股经营活动产生的现金流量净额同比增长率')
    YOY_TR = Column(Numeric(20, 4), comment='营业总收入同比增长率')
    YOY_OR = Column(Numeric(20, 4), comment='营业收入同比增长率')
    YOYOP = Column(Numeric(20, 4), comment='营业利润同比增长率(含)')
    YOYEBT = Column(Numeric(20, 4), comment='利润总额同比增长率')
    YOYNETPROFIT = Column(Numeric(20, 4), comment='归属母公司股东的净利润同比增长率')
    YOYNETPROFIT_DEDUCTED = Column(Numeric(20, 4), comment='归属母公司股东的净利润-扣除非经常损益同比增长率')
    YOYOCF = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额同比增长率')
    YOYROE = Column(Numeric(20, 4), comment='净资产收益率(平均) 同比增长率')
    YOYBPS = Column(Numeric(20, 4), comment='每股净资产同比增长率')
    YOYASSETS = Column(Numeric(20, 4), comment='资产总计同比增长率')
    YOYEQUITY = Column(Numeric(20, 4), comment='归属母公司的股东权益同比增长率')


class HKSHAREFREEFLOAT(Base):
    """香港股票自由流通股本"""
    __tablename__ = 'HKSHAREFREEFLOAT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期(除权日)')
    CHANGE_DT1 = Column(VARCHAR(8), comment='变动日期(上市日)')
    FREESHARES = Column(Numeric(20, 4), comment='自由流通股本(万股)')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class HKSHAREFREEFLOATCALENDAR(Base):
    """港股限售股流通日历"""
    __tablename__ = 'HKSHAREFREEFLOATCALENDAR'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(10), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='可流通日期')
    S_SHARE_LSTTYPECODE = Column(Numeric(9, 0), comment='上市股份类型代码')
    LOCKDAY = Column(Numeric(20, 4), comment='冻结期限(天)')
    RESTRICTED_STOCK = Column(Numeric(20, 4), comment='限售股数量(股)')
    RESTRICTED_DATE_START = Column(VARCHAR(8), comment='限售起始日期')


class HKSHAREHOLDERSMEETING(Base):
    """香港股票股东大会通知"""
    __tablename__ = 'HKSHAREHOLDERSMEETING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='品种ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    MEETING_DT = Column(VARCHAR(8), comment='会议日期')
    MEETING_TYPE = Column(VARCHAR(20), comment='会议类型')
    VOTINGCODE = Column(Numeric(9, 0), comment='投票通道代码')
    SMTGRECDATE = Column(VARCHAR(8), comment='A股股权登记日')
    SPOTMTGSTARTDATE = Column(VARCHAR(8), comment='会议登记起始日')
    SPOTMTGENDDATE = Column(VARCHAR(8), comment='会议登记截止日')
    IS_INTNET = Column(Numeric(5, 0), comment='是否可以网络投票')
    MEETEVENT_ID = Column(VARCHAR(40), comment='会议事件ID')
    IS_NEW = Column(Numeric(5, 0), comment='最新标志')
    MEETING_NAME = Column(VARCHAR(100), comment='会议名称')
    VOTING_TYPE = Column(VARCHAR(100), comment='投票类型')
    IS_NOTARIZATION = Column(Numeric(5, 0), comment='是否经公证')
    START_DATE = Column(VARCHAR(8), comment='过户起始日')
    END_DATE = Column(VARCHAR(8), comment='过户截止日')
    HSHARE_RECORDDATE = Column(VARCHAR(8), comment='H股股权登记日')
    MEETING_PLACE = Column(VARCHAR(400), comment='会议召开地点')
    MEETING_CONTENT = Column(TEXT(2147483647), comment='会议内容')


class HKSHAREHOLDERTRADE(Base):
    """香港股票大股东增减持"""
    __tablename__ = 'HKSHAREHOLDERTRADE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    END_DT = Column(VARCHAR(8), comment='事件日期')
    CHG_REAN = Column(VARCHAR(10), comment='披露原因')
    HOLDER_NAME = Column(VARCHAR(200), comment='最终持有人名称')
    SHRNUM = Column(Numeric(20, 4), comment='增/减或涉及的股份数量')
    SHRTYPE = Column(Numeric(9, 0), comment='[内部]股份类别')
    SHROP = Column(VARCHAR(10), comment='持有权益类型')
    TYPE_CODE = Column(VARCHAR(10), comment='持有股份的身份')
    SHRNUM201 = Column(Numeric(20, 4), comment='201持有权益的股份数目')
    SHRNUM202 = Column(Numeric(20, 4), comment='202持有权益的股份数目')
    SHRNUM203 = Column(Numeric(20, 4), comment='203持有权益的股份数目')
    SHRNUM204 = Column(Numeric(20, 4), comment='204持有权益的股份数目')
    SHRNUM205 = Column(Numeric(20, 4), comment='205持有权益的股份数目')
    SHRNUM206 = Column(Numeric(20, 4), comment='206持有权益的股份数目')
    SHRNUM207 = Column(Numeric(20, 4), comment='207持有权益的股份数目')
    SHRNUM208 = Column(Numeric(20, 4), comment='208持有权益的股份数目')
    SHRNUM209 = Column(Numeric(20, 4), comment='209持有权益的股份数目')
    SHRNUM210 = Column(Numeric(20, 4), comment='210持有权益的股份数目')
    SHRNUM211 = Column(Numeric(20, 4), comment='211持有权益的股份数目')
    SHRNUM212 = Column(Numeric(20, 4), comment='212持有权益的股份数目')
    SHRNUM213 = Column(Numeric(20, 4), comment='213持有权益的股份数目')
    SHRNUM214 = Column(Numeric(20, 4), comment='214持有权益的股份数目')
    CRNCY_CODE = Column(VARCHAR(10), comment='交易货币代码')
    EXHP = Column(Numeric(20, 4), comment='场内每股最高价(元)')
    EXAP = Column(Numeric(20, 4), comment='场内每股平均价(元)')
    OTCAP = Column(Numeric(20, 4), comment='场外每股平均代价(元)')
    OTCP_TYPE = Column(VARCHAR(10), comment='场外代价代号')
    PRESHRNUM = Column(Numeric(20, 4), comment='变动前股份总数(股)')
    PRESHRPCT = Column(Numeric(20, 4), comment='变动前占已发行H股或优先股比例(%)')
    AFTSHRNUM = Column(Numeric(20, 4), comment='变动后股份总数(股)')
    AFTSHRPCT = Column(Numeric(20, 4), comment='变动后占已发行H股或优先股比例(%)')
    COMPNAME = Column(VARCHAR(400), comment='披露人名称')
    COMPTYPE = Column(Numeric(9, 0), comment='股东类型代码')
    HOLDER_TYPE = Column(Numeric(9, 0), comment='内部人类型代码')
    IS_MNG = Column(Numeric(5, 0), comment='是否董事')
    IS_ACTCTRL = Column(Numeric(5, 0), comment='是否实际控制人')
    DRVT_TYPE = Column(Numeric(9, 0), comment='衍生工具类别')
    DRVT_NUM = Column(Numeric(20, 4), comment='衍生权益数量(股)')


class HKSHAREILLEGALITY(Base):
    """香港股票违规事件"""
    __tablename__ = 'HKSHAREILLEGALITY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ILLEG_TYPE = Column(VARCHAR(100), comment='违规类型')
    SUBJECT_TYPE = Column(Numeric(9, 0), comment='主体类别代码')
    SUBJECT = Column(VARCHAR(100), comment='违规主体')
    RELATION_TYPE = Column(Numeric(9, 0), comment='与上市公司的关系')
    BEHAVIOR = Column(VARCHAR, comment='违规行为')
    DISPOSAL_DT = Column(VARCHAR(8), comment='处罚日期')
    DISPOSAL_TYPE = Column(VARCHAR(100), comment='处分类型')
    METHODI = Column(VARCHAR(2000), comment='处分措施')
    PROCESSOR = Column(VARCHAR(200), comment='处理人')
    AMOUNT = Column(Numeric(20, 4), comment='处罚金额(元)')
    BAN_YEAR = Column(Numeric(20, 4), comment='市场禁入期限(年)')
    REF_RULE = Column(VARCHAR(1000), comment='相关法规')
    ILLEG_TYPE_CODE = Column(VARCHAR(1000), comment='违规类型代码')
    ANN_ID = Column(Numeric(11, 0), comment='公告id')


class HKSHAREINSIDEHOLDER(Base):
    """香港股票大股东"""
    __tablename__ = 'HKSHAREINSIDEHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    END_DT = Column(VARCHAR(8), comment='截至日期')
    REPORT_TYPE = Column(Numeric(9, 0), comment='报告类型代码')
    HOLDER_TYPE = Column(Numeric(9, 0), comment='股东类型代码')
    HOLDERNAME = Column(VARCHAR(500), comment='股东名称')
    HOLDERID = Column(VARCHAR(40), comment='股东ID')
    HOLDERID_TYPE = Column(Numeric(9, 0), comment='股东类别代码')
    DIRHOLDNUM = Column(Numeric(20, 4), comment='直接持有数量')
    INDIRHOLDNUM = Column(Numeric(20, 4), comment='间接持有数量')
    SHARETYPE = Column(VARCHAR(100), comment='股份性质')
    PCT_TOT = Column(Numeric(20, 4), comment='占股份总数比例(%)')
    PCT_STYPE = Column(Numeric(20, 4), comment='占同类型股份比例')
    S_CTNT = Column(VARCHAR(3000), comment='备注')


class HKSHAREINTERNETVOTING(Base):
    """香港股票股东大会议案网络投票表决明细"""
    __tablename__ = 'HKSHAREINTERNETVOTING'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_EVENT_ID = Column(VARCHAR(40), comment='会议事件ID')
    S_EVENT_NUM = Column(VARCHAR(20), comment='议案序号')
    S_EVENT_NAME = Column(VARCHAR(2000), comment='议案名称')
    S_INFO_TYPE = Column(VARCHAR(300), comment='表决方式类型')
    S_INFO_PRICE = Column(Numeric(20, 4), comment='申报价格')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class HKSHAREISSUANCE(Base):
    """香港股票发行数据"""
    __tablename__ = 'HKSHAREISSUANCE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='发行公告日')
    ISIPO = Column(Numeric(5, 0), comment='是否IPO')
    S_ISSUE_TYPE = Column(VARCHAR(200), comment='发行方式')
    BOARDLOTUNIT = Column(Numeric(20, 4), comment='发行时交易单位(股)')
    S_ISSUE_PAR = Column(Numeric(26, 10), comment='发行时面值(元)')
    PAR_CRNCY_CODE = Column(VARCHAR(10), comment='面值货币代码')
    S_ISSUE_PRICE = Column(Numeric(20, 4), comment='发行价格(元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    FUNDRAISING_NET = Column(Numeric(20, 4), comment='发售募资净额(元)')
    PTOTAL_NUM_SHARES = Column(Numeric(20, 4), comment='计划发行总数(股)')
    PNUM_HKSHARES = Column(Numeric(20, 4), comment='计划香港发行数量(股)')
    PNUM_INTRNL_SHARES = Column(Numeric(20, 4), comment='计划国际发行数量(股)')
    TOTAL_NUM_SHARES = Column(Numeric(20, 4), comment='实际发行总数(股)')
    NUM_HK_SHARES = Column(Numeric(20, 4), comment='实际香港发行数量(股)')
    NUM_INTRNL_SHARES = Column(Numeric(20, 4), comment='实际国际发行数量(股)')
    OVERALLOTMENTAMOUNT = Column(Numeric(20, 4), comment='超额配售数量(股)')
    HKVALIDSHARES = Column(Numeric(20, 4), comment='香港发行有效申购股数(股)')
    HKVALIDMULTIPLE = Column(Numeric(20, 4), comment='香港发行有效申购倍数(倍)')
    PRICERANGE_UP = Column(Numeric(20, 4), comment='招股价区间下限(元)')
    PRICERANGE_DOWN = Column(Numeric(20, 4), comment='招股价区间上限(元)')
    HEARINGDATE = Column(VARCHAR(8), comment='聆讯日期')
    PRC_DTRMNTN_DATE = Column(VARCHAR(8), comment='定价日')
    PAYMENTDATE = Column(VARCHAR(8), comment='缴款日期')
    LISTDATE = Column(VARCHAR(8), comment='上市日期')
    SBSCRPT_STARTDATE = Column(VARCHAR(8), comment='申购起始日')
    SBSCRPT_ENDDATE = Column(VARCHAR(10), comment='申购截止日')
    INTRNL_VALIDSHARES = Column(Numeric(20, 4), comment='国际发行有效申购股数（股）')
    INTRNL_VALIDMULTIPLE = Column(Numeric(20, 4), comment='国际发行有效申购倍数(倍)')
    PN_SELLING_SHRHLDR = Column(Numeric(20, 4), comment='其中：售股股东计划发售数(股)')
    OAN_SELLING_SHRHLDR = Column(Numeric(20, 4), comment='其中：售股股东超额发售数(股)')
    OVERALLOTMENT_FUNDRAISING = Column(Numeric(20, 4), comment='超额配售募资净额(元)')
    TOTALFUNDRAISING = Column(Numeric(20, 4), comment='募资总额(元)')
    LOTWINNINGRATE = Column(Numeric(20, 4), comment='申购1手中签率(%)')
    MINPURCHASE_1HAND = Column(Numeric(20, 4), comment='稳购1手最低申购股数(股)')
    RESULT_ANN_DATE = Column(VARCHAR(8), comment='发行结果公布日期')
    FUNDUSE = Column(VARCHAR(1200), comment='募资用途说明')
    WEB_INFO_ANN_DATE = Column(VARCHAR(8), comment='网上预览资料公布日')
    INITIAL_ISSUE_PRICE = Column(Numeric(20, 4), comment='初始发行价')


class HKSHAREMAINANDNOTEITEMS(Base):
    """None"""
    __tablename__ = 'HKSHAREMAINANDNOTEITEMS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEQUENCE1 = Column(Numeric(6, 0), comment='顺序编号')
    ACCOUNTS_ID = Column(VARCHAR(20), comment='科目ID')
    IS_NOT_NULL = Column(Numeric(1, 0), comment='是否非空')
    IS_SHOW = Column(Numeric(1, 0), comment='是否展示')
    S_INFO_TYPECODE = Column(Numeric(9, 0), comment='报表品种代码')
    SUBJECT_CHINESE_NAME = Column(VARCHAR(100), comment='科目中文名')


class HKSHAREMAJOREVENT(Base):
    """香港股票重大事件表"""
    __tablename__ = 'HKSHAREMAJOREVENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_EVENT_CATEGORYCODE = Column(Numeric(9, 0), comment='事件类型代码')
    S_EVENT_ANNCEDATE = Column(VARCHAR(8), comment='披露日期')
    S_EVENT_HAPDATE = Column(VARCHAR(8), comment='发生日期')
    S_EVENT_EXPDATE = Column(VARCHAR(8), comment='失效日期')
    S_EVENT_CONTENT = Column(TEXT(2147483647), comment='[内部]事件内容参数')
    S_EVENT_TEMPLATEID = Column(Numeric(12, 0), comment='[内部]模板ID')


class HKSHAREMANAGEMENT(Base):
    """香港股票管理层信息"""
    __tablename__ = 'HKSHAREMANAGEMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_INFO_MANAGER_NAME = Column(VARCHAR(100), comment='姓名')
    S_INFO_MANAGER_ENNAME = Column(VARCHAR(200), comment='英文名')
    S_INFO_MANAGER_GENDER = Column(VARCHAR(10), comment='性别')
    S_INFO_MANAGER_NATIONALITY = Column(VARCHAR(20), comment='国籍')
    S_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(8), comment='出生年份')
    S_INFO_MANAGER_TYPECODE = Column(Numeric(9, 0), comment='管理层类别代码')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='职务')
    S_INFO_MANAGER_ENPOST = Column(VARCHAR(200), comment='职务(英文)')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8), comment='离职日期')
    S_INFO_MANAGER_INTRODUCTION = Column(TEXT(2147483647), comment='个人简历')
    S_INFO_MANAGER_ENINTRODUCTION = Column(TEXT(2147483647), comment='个人简历(英文)')
    MANID = Column(VARCHAR(10), comment='人物ID')
    OP_DATE = Column(VARCHAR(8), comment='操作日期')
    IS_IN_OFFICE = Column(Numeric(1, 0), comment='是否在任')


class HKSHAREMANAGEMENTHOLDREWARD(Base):
    """香港股票管理层持股及报酬"""
    __tablename__ = 'HKSHAREMANAGEMENTHOLDREWARD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    END_DATE = Column(VARCHAR(8), comment='截止日期')
    CRNY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_POST = Column(VARCHAR(200), comment='职务')
    S_MANAGER_RETURN = Column(Numeric(20, 4), comment='报酬')
    S_MANAGER_QUANTITY = Column(Numeric(20, 4), comment='持股数量')


class HKSHAREPARVALUELOTSIZE(Base):
    """香港股票面值及交易单位"""
    __tablename__ = 'HKSHAREPARVALUELOTSIZE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='变动日期')
    S_INFO_PARVALUE = Column(Numeric(26, 10), comment='面值')
    S_INFO_TRADEUNIT = Column(Numeric(20, 4), comment='交易单位')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')


class HKSHAREPROSECUTION(Base):
    """香港股票诉讼事件"""
    __tablename__ = 'HKSHAREPROSECUTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    TITLE = Column(VARCHAR(40), comment='案件名称')
    ACCUSER = Column(VARCHAR(3000), comment='原告方')
    DEFENDANT = Column(VARCHAR(3000), comment='被告方')
    PRO_TYPE = Column(VARCHAR(10), comment='诉讼类型')
    AMOUNT = Column(Numeric(20, 4), comment='涉案金额')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PROSECUTE_DT = Column(VARCHAR(8), comment='起诉日期')
    COURT = Column(VARCHAR(200), comment='一审受理法院')
    JUDGE_DT = Column(VARCHAR(8), comment='判决日期')
    RESULT9 = Column(TEXT(2147483647), comment='判决内容')
    IS_APPEAL = Column(Numeric(5, 0), comment='是否上诉')
    APPELLANT = Column(VARCHAR(1), comment='二审上诉方(是否原告)')
    COURT2 = Column(VARCHAR(200), comment='二审受理法院')
    JUDGE_DT2 = Column(VARCHAR(8), comment='二审判决日期')
    RESULT2 = Column(VARCHAR(2000), comment='二审判决内容')
    RESULTAMOUNT = Column(Numeric(20, 4), comment='判决金额')
    BRIEFRESULT = Column(VARCHAR(100), comment='诉讼结果')
    EXECUTION = Column(TEXT(2147483647), comment='执行情况')
    INTRODUCTION = Column(TEXT(2147483647), comment='案件描述')


class HKSHARESHORTSELLINGTURNOVER(Base):
    """香港股票卖空成交量"""
    __tablename__ = 'HKSHARESHORTSELLINGTURNOVER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_INFO_DATATYPE = Column(Numeric(9, 0), comment='数据类型')
    S_SS_VOLUME = Column(Numeric(20, 4), comment='成交股数')
    S_SS_TURNOVER = Column(Numeric(20, 4), comment='成交金额')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')


class HKSHAREST(Base):
    """香港股票特别处理"""
    __tablename__ = 'HKSHAREST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_TYPE_ST = Column(VARCHAR(8), comment='特别处理类型')
    ENTRY_DT = Column(VARCHAR(8), comment='实施日期')
    REMOVE_DT = Column(VARCHAR(8), comment='撤销日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REASON = Column(VARCHAR(100), comment='实施原因')


class HKSHARESTAFF(Base):
    """香港股票员工人数变更"""
    __tablename__ = 'HKSHARESTAFF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 4), comment='员工人数(人)')
    S_INFO_TOTALEMPLOYEES2 = Column(Numeric(20, 0), comment='母公司员工人数(人)')
    MEMO = Column(VARCHAR(1000), comment='特殊情况说明')


class HKSHARESWINDUSTRIESCLASS(Base):
    """港股通申万行业分类（一年更新一次）"""
    __tablename__ = 'HKSHARESWINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SW_IND_CODE = Column(VARCHAR(50), comment='申万行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class HKSHARETTMANDMRQ(Base):
    """香港股票TTM与MRQ"""
    __tablename__ = 'HKSHARETTMANDMRQ'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    TRADE_DT = Column(VARCHAR(8), comment='截止日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_FA_OR_TTM = Column(Numeric(20, 4), comment='营业收入(TTM)')
    S_FA_GROSSMARGIN_TTM = Column(Numeric(22, 4), comment='毛利(TTM)')
    S_FA_PREFINEXPOP_TTM = Column(Numeric(22, 4), comment='扣除融资费用前营业利润(TTM)')
    S_FA_NONOPPROFIT_TTM = Column(Numeric(22, 4), comment='非营业利润(TTM)')
    S_FA_PCTJVPROFIT_TTM = Column(Numeric(22, 4), comment='所占联营公司业绩(TTM)')
    S_FA_PROFIT_BEF_TAX_TTM = Column(Numeric(22, 4), comment='除税前利润(TTM)')
    S_FA_PROFIT_AFT_TAX_TTM = Column(Numeric(22, 4), comment='除税后利润(TTM)')
    MINORITY_INT_TTM = Column(Numeric(22, 4), comment='少数股东权益(TTM)')
    S_FA_PCTJVCPROFIT_TTM = Column(Numeric(22, 4), comment='所占共同控制实体业绩(TTM)')
    S_FA_NETPROFIT_TTM = Column(Numeric(22, 4), comment='归属母公司股东净利润(TTM)')
    S_FA_FINAEXPENSE_TTM = Column(Numeric(22, 4), comment='财务费用(TTM)')
    NET_INCR_CASH_CASH_EQU_TTM = Column(Numeric(22, 4), comment='现金及现金等价物净增加额(TTM)')
    NET_CASH_FLOWS_OPER_ACT_TTM = Column(Numeric(22, 4), comment='经营活动产生的现金流量净额(TTM)')
    S_FA_INVESTCASHFLOW_TTM = Column(Numeric(22, 4), comment='投资活动产生的现金流量净额(TTM)')
    S_FA_FINANCECASHFLOW_TTM = Column(Numeric(22, 4), comment='筹资活动产生的现金流量净额(TTM)')
    S_FA_ASSET_MRQ = Column(Numeric(22, 4), comment='资产总计(MRQ)')
    S_FA_DEBT_MRQ = Column(Numeric(22, 4), comment='负债合计(MRQ)')
    S_STM_BSMRQ = Column(Numeric(22, 4), comment='固定资产合计(MRQ)')
    S_FA_TOTALEQUITY_MRQ = Column(Numeric(22, 4), comment='股东权益(MRQ)')
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(Numeric(22, 4), comment='股东权益(含少数股东权益)(MRQ)')
    S_FA_INVESTCAPITAL_MRQ = Column(Numeric(22, 4), comment='投入资本(MRQ)')
    S_FA_NETPROFITMARGIN_TTM = Column(Numeric(22, 4), comment='销售净利率(TTM)')
    S_FA_MARGINALPROFITRATE_TTM = Column(Numeric(22, 4), comment='边际利润率(TTM)')
    S_FA_GROSSPROFITMARGIN_TTM = Column(Numeric(22, 4), comment='销售毛利率(TTM)')
    S_FA_OPPROFIT_RATE = Column(Numeric(22, 4), comment='经营利润率(TTM)')
    S_FA_OPTOOR_TTM = Column(Numeric(22, 4), comment='营业利润/营业收入(TTM)')
    S_FA_PROFIT_BEF_TAX_RATE = Column(Numeric(22, 4), comment='税前利润率(TTM)')
    S_FA_ROE_TTM = Column(Numeric(22, 4), comment='净资产收益率(ROE)(TTM)')
    S_FA_ROA_TTM = Column(Numeric(22, 4), comment='总资产净利率(TTM)')
    ROA_EXCLMININTINC_TTM = Column(Numeric(22, 4), comment='总资产净利率-不含少数股东损益(TTM)')
    FA_ROIC_TTM = Column(Numeric(22, 4), comment='投入资本回报率ROIC(TTM)')
    S_FA_PREFINEXPOPTOEBT_TTM = Column(Numeric(22, 4), comment='扣除融资费用前营业利润/利润总额(TTM)')
    S_FA_NOPTOEBT_TTM = Column(Numeric(22, 4), comment='非营业利润/利润总额(TTM)')
    S_FA_TAXTOEBT_TTM = Column(Numeric(22, 4), comment='税项/利润总额(TTM)')
    S_FA_OCFTOOR_TTM = Column(Numeric(22, 4), comment='经营活动产生的现金流量净额／营业收入(TTM)')
    S_FA_DEBTTOASSETS_MRQ = Column(Numeric(22, 4), comment='资产负债率(MRQ)')
    S_FA_OCFTOOP_TTM = Column(Numeric(22, 4), comment='经营活动产生的现金流量净额／营业利润(TTM)?(含)')
    CONTINUOUS_NET_OP_TTM = Column(Numeric(22, 4), comment='持续经营净利润(TTM)')
    NONCONTINUOUS_NET_OP_TTM = Column(Numeric(22, 4), comment='非持续经营净利润(TTM)')
    S_FA_COST_TTM = Column(Numeric(22, 4), comment='营业成本(TTM)')
    S_FA_OPERATEINCOME_TTM = Column(Numeric(22, 4), comment='经营活动净收益(TTM)')
    S_FA_INVESTINCOME_TTM = Column(Numeric(22, 4), comment='价值变动净收益(TTM)')
    S_FA_OP_TTM = Column(Numeric(22, 4), comment='营业利润(TTM)')
    S_FA_GR_TTM = Column(Numeric(22, 4), comment='营业总收入(TTM)')
    S_FA_GC_TTM = Column(Numeric(22, 4), comment='营业总成本(TTM)')
    S_FA_PROFITTOGR_TTM = Column(Numeric(22, 4), comment='净利润／营业总收入(TTM)')
    S_FA_GCTOGR_TTM = Column(Numeric(22, 4), comment='营业总成本／营业总收入(TTM)')
    S_FA_ROA2_TTM = Column(Numeric(22, 4), comment='总资产报酬率(TTM)')
    S_FA_OPERATEINCOMETOEBT_TTM = Column(Numeric(22, 4), comment='经营活动净收益／利润总额(TTM)')
    S_FA_INVESTINCOMETOEBT_TTM = Column(Numeric(22, 4), comment='价值变动净收益／利润总额(TTM)')
    S_FA_OCFTOOPERATEINCOME_TTM = Column(Numeric(22, 4), comment='经营活动产生的现金流量净额／经营活动净收益(TTM)')
    S_FA_EPS_TTM = Column(Numeric(22, 4), comment='每股收益(TTM)')
    S_FA_ORPS_TTM = Column(Numeric(22, 4), comment='每股营业收入(TTM)')
    S_FA_OCFPS_TTM = Column(Numeric(22, 4), comment='每股经营活动产生的现金流量净额(TTM)')
    S_FA_CFPS_TTM = Column(Numeric(22, 4), comment='每股现金流量净额(TTM)')
    S_FA_OPERATEEXPENSETOGR_TTM = Column(Numeric(22, 4), comment='销售费用／营业总收入(TTM)')
    S_FA_ADMINEXPENSETOGR_TTM = Column(Numeric(22, 4), comment='管理费用／营业总收入(TTM)')
    S_FA_FINAEXPENSETOGR_TTM = Column(Numeric(22, 4), comment='财务费用／营业总收入(TTM)')
    S_FA_OPERATEEXPENSE_TTM = Column(Numeric(22, 4), comment='销售费用(TTM)')
    S_FA_ADMINEXPENSE_TTM = Column(Numeric(22, 4), comment='管理费用(TTM)')
    S_FA_EBIT_TTM = Column(Numeric(22, 4), comment='息税前利润(TTM)')
    S_FA_TOTINVESTCAPITAL_MRQ = Column(Numeric(22, 4), comment='全部投入资本(MRQ)')
    S_FA_OPTOEBT_TTM = Column(Numeric(22, 4), comment='营业利润(含)／利润总额(TTM)')
    S_FA_OPTOGR_TTM = Column(Numeric(22, 4), comment='营业利润(含)／营业总收入(TTM)')
    S_FA_EBTTOGR_TTM = Column(Numeric(22, 4), comment='利润总额／营业总收入(TTM)')
    NONNETOPTOTAXPROFIT = Column(Numeric(22, 4), comment='非持续经营净利润／税后利润(TTM)')
    NETOPTOTAXPROFIT = Column(Numeric(22, 4), comment='持续经营净利润／税后利润(TTM)')
    TOT_SHR_NEW = Column(Numeric(22, 4), comment='最新总股本')
    INT_EXP_TTM = Column(Numeric(22, 4), comment='利息支出(TTM)')
    INC_TAX_TTM = Column(Numeric(22, 4), comment='所得税(TTM)')
    S_FA_GRPS_TTM = Column(Numeric(22, 4), comment='每股营业总收入(TTM)')
    S_FA_BPS_MRQ = Column(Numeric(22, 4), comment='每股净资产(MRQ)')


class HKSHARETTMHIS(Base):
    """香港股票TTM指标历史数据"""
    __tablename__ = 'HKSHARETTMHIS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    TRADE_DT = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    TOT_OPER_REV_TTM = Column(Numeric(20, 4), comment='营业总收入(TTM)')
    OPER_REV_TTM = Column(Numeric(20, 4), comment='营业收入(TTM)')
    NET_PROFIT_TTM = Column(Numeric(20, 4), comment='净利润(TTM)')
    NET_PROFIT_PARENT_COMP_TTM = Column(Numeric(20, 4), comment='归属母公司净利润(TTM)')
    NET_CASH_FLOWS_OPER_ACT_TTM = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额(TTM)')
    NET_INCR_CASH_CASH_EQU_TTM = Column(Numeric(20, 4), comment='现金及现金等价物净增加额(TTM)')


class HKSHAREUNSOLDSHORTSALE(Base):
    """香港股票证券未平仓卖空量"""
    __tablename__ = 'HKSHAREUNSOLDSHORTSALE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码1')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    UNFLAT_SHORT_INTEREST = Column(Numeric(20, 4), comment='未平仓卖空股数')
    UNFLAT_SHORT_SELLING_AMOUNT = Column(Numeric(20, 4), comment='未平仓卖空金额')


class HKSHAREYIELD(Base):
    """香港股票行情日收益率"""
    __tablename__ = 'HKSHAREYIELD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    PCT_CHANGE_D = Column(Numeric(22, 4), comment='日涨跌幅')
    PCT_CHANGE_W = Column(Numeric(22, 4), comment='周涨跌幅')
    PCT_CHANGE_M = Column(Numeric(22, 4), comment='月涨跌幅')
    VOLUME_W = Column(Numeric(22, 4), comment='周成交量')
    VOLUME_M = Column(Numeric(22, 4), comment='月成交量')
    AMOUNT_W = Column(Numeric(22, 4), comment='周成交额')
    AMOUNT_M = Column(Numeric(22, 4), comment='月成交额')
    TURNOVER_D = Column(Numeric(22, 4), comment='日换手率')
    TURNOVER_D_FLOAT = Column(Numeric(22, 4), comment='日换手率(自由流通股本)')
    TURNOVER_W = Column(Numeric(22, 4), comment='周换手率')
    TURNOVER_W_FLOAT = Column(Numeric(22, 4), comment='周换手率(自由流通股本)')
    TURNOVER_W_AVE = Column(Numeric(22, 4), comment='周平均换手率')
    TURNOVER_W_AVE_FLOAT = Column(Numeric(22, 4), comment='周平均换手率(自由流通股本)')
    TURNOVER_M = Column(Numeric(22, 4), comment='月换手率')
    TURNOVER_M_FLOAT = Column(Numeric(22, 4), comment='月换手率(自由流通股本)')
    TURNOVER_M_AVE = Column(Numeric(22, 4), comment='月平均换手率')
    TURNOVER_M_AVE_FLOAT = Column(Numeric(22, 4), comment='月平均换手率(自由流通股本)')
    PCT_CHANGE_AVE_100W = Column(Numeric(22, 4), comment='周平均涨跌幅(100周)')
    STD_DEVIATION_100W = Column(Numeric(22, 4), comment='周标准差(100周)')
    VARIANCE_100W = Column(Numeric(22, 4), comment='周方差(100周)')
    PCT_CHANGE_AVE_24M = Column(Numeric(22, 4), comment='月平均涨跌幅(24月)')
    STD_DEVIATION_24M = Column(Numeric(22, 4), comment='月标准差(24月)')
    VARIANCE_24M = Column(Numeric(22, 4), comment='月方差(24月)')
    PCT_CHANGE_AVE_60M = Column(Numeric(22, 4), comment='月平均涨跌幅(60月)')
    STD_DEVIATION_60M = Column(Numeric(22, 4), comment='月标准差(60月)')
    VARIANCE_60M = Column(Numeric(22, 4), comment='月方差(60月)')
    BETA_DAY_1Y = Column(Numeric(22, 8), comment='日BETA(1年)')
    BETA_DAY_2Y = Column(Numeric(22, 8), comment='日BETA(2年)')
    ALPHA_DAY_1Y = Column(Numeric(22, 8), comment='日ALPHA(1年)')
    ALPHA_DAY_2Y = Column(Numeric(22, 8), comment='日ALPHA(2年)')
    BETA_100W = Column(Numeric(22, 8), comment='周BETA(100周)')
    ALPHA_100W = Column(Numeric(22, 8), comment='周ALPHA(100周)')
    BETA_24M = Column(Numeric(22, 8), comment='月BETA(24月)')
    BETA_60M = Column(Numeric(22, 8), comment='月BETA(60月)')
    ALPHA_24M = Column(Numeric(22, 8), comment='月ALPHA(24月)')
    ALPHA_60M = Column(Numeric(22, 8), comment='月ALPHA(60月)')


class HKSTOCKCHANGECODE(Base):
    """香港股票代码变更表"""
    __tablename__ = 'HKSTOCKCHANGECODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前Wind代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后Wind代码')
    CHANGE_DATE = Column(VARCHAR(8), comment='Wind代码变更日期')


class HKSTOCKCHANGECODEQL(Base):
    """None"""
    __tablename__ = 'HKSTOCKCHANGECODEQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_OLDWINDCODE = Column(VARCHAR(40))
    S_INFO_NEWWINDCODE = Column(VARCHAR(40))
    CHANGE_DATE = Column(VARCHAR(8))


class HKSTOCKCHANGECODEZL(Base):
    """港股代码变更表(增量)"""
    __tablename__ = 'HKSTOCKCHANGECODEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前Wind代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后Wind代码')
    CHANGE_DATE = Column(VARCHAR(8), comment='Wind代码变更日期')


class HKSTOCKGICSINDUSTRIESMEMBERS(Base):
    """香港股票GICS行业成份(废弃)"""
    __tablename__ = 'HKSTOCKGICSINDUSTRIESMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司ID')
    GICS_IND_CODE = Column(VARCHAR(50), comment='GICS行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='起始日期')
    REMOVE_DT = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(5, 0), comment='最新标志')


class HKSTOCKHSINDEXWEIGHT(Base):
    """None"""
    __tablename__ = 'HKSTOCKHSINDEXWEIGHT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    IXDEX_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    COMPON_STOCK_WINDCODE = Column(VARCHAR(40), comment='成分股Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_WEIGHT = Column(Numeric(20, 4), comment='权重')


class HKSTOCKHSINDUSTRIESMEMBERS(Base):
    """香港股票恒生行业分类"""
    __tablename__ = 'HKSTOCKHSINDUSTRIESMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    HS_IND_CODE = Column(VARCHAR(50), comment='恒生行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class HKSTOCKHSINDUSTRIESMEMBERSZL(Base):
    """香港股票恒生行业成份(增量)"""
    __tablename__ = 'HKSTOCKHSINDUSTRIESMEMBERSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    HS_IND_CODE = Column(VARCHAR(50), comment='恒生行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class HKSTOCKINDEXCODE(Base):
    """香港股票指数板块代码"""
    __tablename__ = 'HKSTOCKINDEXCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_INDEXWINDCODE = Column(VARCHAR(40))
    S_INFO_NAME = Column(VARCHAR(50), comment='指数简称')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(40), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')
    MK = Column(VARCHAR(40), comment='交易所')


class HKSTOCKINDEXCODEZL(Base):
    """香港指数板块代码(增量)"""
    __tablename__ = 'HKSTOCKINDEXCODEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_INDEXWINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='指数简称')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(40), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')
    MK = Column(VARCHAR(40), comment='交易所')


class HKSTOCKINDEXMEMBERS(Base):
    """香港股票指数成份股"""
    __tablename__ = 'HKSTOCKINDEXMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class HKSTOCKINDEXMEMBERSZL(Base):
    """香港股票指数成份股(增量)"""
    __tablename__ = 'HKSTOCKINDEXMEMBERSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class HKSTOCKINDUSTRIESCODE(Base):
    """香港股票行业分类编码"""
    __tablename__ = 'HKSTOCKINDUSTRIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCLASS = Column(VARCHAR(38), comment='行业分类')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='行业代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='行业名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')


class HKSTOCKINDUSTRIESCODEZL(Base):
    """香港行业代码(增量)(废弃)"""
    __tablename__ = 'HKSTOCKINDUSTRIESCODEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCLASS = Column(VARCHAR(38), comment='行业分类')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='行业代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='行业名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')


class HKSTOCKREPO(Base):
    """香港证券回购信息"""
    __tablename__ = 'HKSTOCKREPO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(10), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(元)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(元)')
    REPO_VOLUME = Column(Numeric(20, 4), comment='回购数量(股)')
    REPO_AMOUNT = Column(Numeric(20, 4), comment='回购金额(元)')
    CRNCY_CODE = Column(VARCHAR(20), comment='货币代码')
    REPO_TYPECODE = Column(Numeric(9, 0), comment='回购方式类型代码')


class HKSTOCKSHORTSELLINGLIST(Base):
    """香港股票可卖空证券明细"""
    __tablename__ = 'HKSTOCKSHORTSELLINGLIST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(VARCHAR(8), comment='最新标志')


class HKSTOCKWINDINDUSTRIESMEMBERS(Base):
    """香港股票Wind行业分类"""
    __tablename__ = 'HKSTOCKWINDINDUSTRIESMEMBERS'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_IND_CODE = Column(VARCHAR(50), comment='Wind行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class HKSTOCKWINDINDUSTRIESMEMBERSQL(Base):
    """None"""
    __tablename__ = 'HKSTOCKWINDINDUSTRIESMEMBERSQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    WIND_IND_CODE = Column(VARCHAR(50))
    ENTRY_DT = Column(VARCHAR(8))
    REMOVE_DT = Column(VARCHAR(8))
    CUR_SIGN = Column(Numeric(1, 0))


class HKSTOCKWINDINDUSTRIESMEMBERSZL(Base):
    """香港股票万得行业成份(增量)"""
    __tablename__ = 'HKSTOCKWINDINDUSTRIESMEMBERSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_IND_CODE = Column(VARCHAR(50), comment='Wind行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class HKTRANSACTIONSTATUS(Base):
    """香港股票停复牌信息"""
    __tablename__ = 'HKTRANSACTIONSTATUS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SUSPENDDATE = Column(VARCHAR(8), comment='停牌日期')
    SUSPENDTYPE = Column(VARCHAR(100), comment='停牌类型')
    SUSPENDREASON = Column(VARCHAR(400), comment='停牌原因')
    SUSPENDTYPECODE = Column(Numeric(9, 0), comment='停牌类型代码')
    SUSPENDREASONCODE = Column(Numeric(9, 0), comment='停牌原因代码')
    RESUMPDATE = Column(VARCHAR(8), comment='复牌日期')
    RESUMPTIME = Column(VARCHAR(200), comment='停复牌时间')


class HSHARESALESSEGMENT(Base):
    """香港股票主营业务构成"""
    __tablename__ = 'HSHARESALESSEGMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='[内部]公告日期')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    STATEMENT_TYPECODE = Column(Numeric(9, 0), comment='报表类型代码')
    REPORT_TYPECODE = Column(Numeric(9, 0), comment='报告类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    SEGMENT_ITEMCODE = Column(Numeric(9, 0), comment='项目类别代码')
    RESOURCECODE = Column(Numeric(9, 0), comment='[内部]文件类型代码')
    SEGMENT_ITEM = Column(VARCHAR(100), comment='主营业务项目')
    SEGMENT_SALES = Column(Numeric(20, 4), comment='主营业务收入')
    SEGMENT_COST = Column(Numeric(20, 4), comment='主营业务成本')
    GROSSPROFIT = Column(Numeric(20, 4), comment='毛利')
    SEGMENT_SALES_RATIO = Column(Numeric(20, 4), comment='主营业务收入比例')
    SEGMENT_COST_RATIO = Column(Numeric(20, 4), comment='主营业务成本比例')
    GROSSPROFITMARGIN = Column(Numeric(20, 4), comment='毛利率')
    PRIME_OPER_REV_YOY = Column(Numeric(20, 4), comment='主营业务收入同比增长率')
    PRIME_OPER_COST_YOY = Column(Numeric(20, 4), comment='主营业务成本同比增长率')
    GROSS_PROFIT_MARGIN_YOY = Column(Numeric(20, 4), comment='毛利率同比增长率')
    GROSS_PROFIT_YOY = Column(Numeric(20, 4), comment='毛利同比增长率')
    PRIME_OPER_PROFIT_RATIO = Column(Numeric(20, 4), comment='主营业务利润比例')
    ACCOUNTS_ID = Column(VARCHAR(20), comment='科目ID')
    ISPUBLISHVALUE = Column(Numeric(1, 0), comment='[内部]是否公布值')
