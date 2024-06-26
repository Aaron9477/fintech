# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/8/5 8:48
# @Author  : lisl3
# @File    : wind_data_field.py
# @Project : cscfist
# @Function: 定义wind数据字段类型
# @Version : V0.0.1
# ------------------------------
from sqlalchemy import Column, VARCHAR, Numeric, DateTime, TEXT, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ABSDESCRIPTION(Base):
    """资产支持证券基本资料"""
    __tablename__ = 'ABSDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    ABS_NAME = Column(VARCHAR(200), comment='项目名称')
    ABS_SHORTNAME = Column(VARCHAR(200), comment='项目简称')
    SPONOR = Column(VARCHAR(200), comment='发起机构')
    SPONORID = Column(VARCHAR(40), comment='发起机构id')
    ISSUER = Column(VARCHAR(200), comment='发行人')
    ISSUERID = Column(VARCHAR(40), comment='发行人ID')
    ISSUEAMOUNT = Column(Numeric(24, 8), comment='发行总额(万)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    POOL_NAME = Column(VARCHAR(200), comment='资产池名称')
    START_DT = Column(VARCHAR(8), comment='初始起算日')
    ASSET_TYPE = Column(Numeric(9, 0), comment='基础资产类型代码')
    DELIVERY_DT = Column(VARCHAR(8), comment='交割日')
    SETUP_DT = Column(VARCHAR(8), comment='信托成立日')
    FIRST_PAY_DT = Column(VARCHAR(8), comment='首个本息兑付日')
    MATURITY_DT = Column(VARCHAR(8), comment='法定到期日')
    ANN_DT = Column(VARCHAR(8), comment='发行公告日')
    ABS_ASSET = Column(VARCHAR(2000), comment='基础资产')
    ABS_BLOCK_CODE = Column(Numeric(9, 0), comment='资产支持证券分档代码')
    IS_INTERNAL_CREDIT = Column(Numeric(1, 0), comment='是否有内部信用增级')
    IS_EXTERNAL_CREDIT = Column(Numeric(1, 0), comment='是否有外部信用增级')
    ASSETS_IS_TABLE = Column(Numeric(1, 0), comment='资产是否出表')
    ABS_ID = Column(VARCHAR(10), comment='项目ID')


class ABSINDUSTRIESCLASS(Base):
    """资产支持证券原始权益人Wind行业分类"""
    __tablename__ = 'ABSINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    WIND_IND_CODE = Column(VARCHAR(50), comment='Wind行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ABSINSIDEHOLDER(Base):
    """资产支持证券原始权益人持股变动"""
    __tablename__ = 'ABSINSIDEHOLDER'
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


class ABSPAYMENT(Base):
    """资产支持证券本息兑付"""
    __tablename__ = 'ABSPAYMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='报告日期')
    CLASSIFICATION_CODE = Column(Numeric(9, 0), comment='资产支持证券分档代码')
    INT_ACC_START_DT = Column(VARCHAR(8), comment='计息起始日')
    INT_ACC_END_DT = Column(VARCHAR(8), comment='计息截止日')
    PAYMENT_DT = Column(VARCHAR(8), comment='支付日')
    PRINCIPAL_BEGIN = Column(Numeric(24, 8), comment='本金期初金额')
    PRINCIPAL_BALANCE = Column(Numeric(24, 8), comment='本金期末余额')
    COUPON_RATE = Column(Numeric(20, 4), comment='票面利率')
    PRINCIPAL_AMOUNT = Column(Numeric(24, 8), comment='实付本金额')
    PRINCIPAL_PAYABLE = Column(Numeric(24, 8), comment='应付本金额')
    PRINCIPAL_TRANS_TO_NP = Column(Numeric(24, 8), comment='转存下期本金还款额')
    PRINCIPAL_LOSS = Column(Numeric(24, 8), comment='本金损失金额')
    INTEREST_PAYABLE = Column(Numeric(24, 8), comment='应付利息额')
    INTEREST_AMOUNT = Column(Numeric(24, 8), comment='实付利息额')


class ABSSENSITANALYSIS(Base):
    """资产支持证券敏感性分析"""
    __tablename__ = 'ABSSENSITANALYSIS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANAL_TYPE = Column(VARCHAR(40), comment='敏感性分析类型')
    ANAL_RATIO = Column(Numeric(20, 4), comment='早偿率/违约率')
    WEIGH_AVG_TERM = Column(Numeric(20, 4), comment='加权平均期限')
    EST_MATURITYDATE = Column(VARCHAR(8), comment='预期到期日')


class ABSSUBFILEDATA(Base):
    """资产支持证券分档基本资料"""
    __tablename__ = 'ABSSUBFILEDATA'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    YIELD_MIN = Column(Numeric(20, 4), comment='预期最低年收益率(%)')
    YIELD_MAX = Column(Numeric(20, 4), comment='预期最高年收益率(%)')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='资产所有方公司id')
    B_ANAL_PTMYEAR = Column(Numeric(20, 4), comment='存续期')
    BASIC_ASSETS = Column(VARCHAR(2000), comment='基础资产')
    MOBILE_PLACES = Column(VARCHAR(800), comment='流动场所')
    PRODUCT_COMPNAME = Column(VARCHAR(200), comment='产品设立人')
    START_DATE = Column(VARCHAR(8), comment='转让起始日期')
    END_DATE = Column(VARCHAR(8), comment='转让截止日期')
    PRODUCT_MANAGER = Column(VARCHAR(200), comment='产品管理人')
    BOOKKEEPING_MANAGER = Column(VARCHAR(200), comment='薄记管理人')
    SUBDIVIDE_CODE = Column(Numeric(9, 0), comment='资产支持证券分档代码')
    INTEX_NAME = Column(VARCHAR(20), comment='Intex项目名称')
    INTEX_CODE = Column(VARCHAR(20), comment='Intex分档代码')
    INTEX_RATE = Column(VARCHAR(50), comment='Intex利率基准')


class ABSTRANSACTION(Base):
    """资产支持证券交易数据"""
    __tablename__ = 'ABSTRANSACTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='转让日期')
    S_INC_INITEXECPRI = Column(Numeric(20, 4), comment='转让价格')
    TRANSFERRED = Column(Numeric(20, 4), comment='转让数量(手)')


class ACCOUNTRELATEDWITHBONDISSUE(Base):
    """中国债券发行涉及银行账号"""
    __tablename__ = 'ACCOUNTRELATEDWITHBONDISSUE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TYPE_CODE = Column(Numeric(9, 0), comment='发行类型代码')
    ACCOUNT_NUM = Column(VARCHAR(40), comment='账号')
    ACCOUNT_TITLE = Column(VARCHAR(100), comment='账户名称')
    BANK_NAME = Column(VARCHAR(100), comment='开户行名称')
    BANK_NUM = Column(VARCHAR(40), comment='清算行行号')


class AEQUFROPLEINFOREPPEREND(Base):
    """中国A股股权冻结质押情况(报告期)"""
    __tablename__ = 'AEQUFROPLEINFOREPPEREND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    PRICE_DATE = Column(VARCHAR(8), comment='报告期')
    F_NAV_UNIT = Column(VARCHAR(8), comment='公告日期')
    F_NAV_ACCUMULATED = Column(VARCHAR(200), comment='股东名称')
    F_NAV_DIVACCUMULATED = Column(Numeric(20, 4), comment='质押或冻结数量(股)')
    F_NAV_ADJFACTOR = Column(Numeric(20, 4), comment='持股数量(股)')
    CRNCY_CODE = Column(Numeric(20, 4), comment='质押冻结比例(%)')
    F_NAV_ADJUSTED = Column(VARCHAR(400), comment='备注')


class AMACCHFDESCRIPTION(Base):
    """中国私募基金基本资料(基金业协会)"""
    __tablename__ = 'AMACCHFDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_FULLNAME = Column(VARCHAR(200), comment='基金名称')
    F_INFO_NUMBER = Column(VARCHAR(100), comment='基金编号')
    F_ESTABLISHMENT_TIME = Column(VARCHAR(8), comment='成立时间')
    F_RECORD_TIME = Column(VARCHAR(8), comment='备案时间')
    F_FUND_FILING_STAGE = Column(VARCHAR(40), comment='基金备案阶段')
    F_FUND_TYPE = Column(VARCHAR(40), comment='基金类型')
    F_CURRENCY = Column(VARCHAR(10), comment='币种')
    F_INFO_FUNDMANAGEMENTCOMP = Column(VARCHAR(100), comment='基金管理人名称')
    F_INFO_FIRSTINVESTTYPE = Column(VARCHAR(20), comment='管理类型')
    F_INFO_CUSTODIANBANK = Column(VARCHAR(500), comment='托管人名称')
    F_INFO_INVESTSCOPE = Column(VARCHAR(2000), comment='主要投资领域')
    F_INFO_STATUS = Column(VARCHAR(20), comment='运作状态')
    F_INFO_LAST_REPORTTIME = Column(VARCHAR(8), comment='基金信息最后报告时间')
    F_INFO_HOT_TIP = Column(VARCHAR(300), comment='基金协会特别提示')
    F_DISCLOSUR_WEBSITES = Column(VARCHAR(200), comment='产品信息披露网址')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_PRODUCT_ID = Column(VARCHAR(10), comment='产品证券ID')
    F_INFO_FUNDMANAGEMENTID = Column(VARCHAR(10), comment='管理人公司ID')
    F_INFO_CUSTODIANBANKID = Column(VARCHAR(200), comment='托管人公司ID')
    F_CONTRACT_PERIOD = Column(Numeric(20, 4), comment='合同期限')
    F_INITIAL_SCALE = Column(Numeric(22, 6), comment='起始规模')
    IS_CLASSIFICATION = Column(VARCHAR(10), comment='是否分级')
    F_INVESTORS_NUMBER = Column(Numeric(5, 0), comment='成立时投资者数量')
    F_PRODUCT_TYPE = Column(VARCHAR(50), comment='非专户资产管理计划产品类型')


class ASAREPLANTRADE(Base):
    """中国A股股东拟增减持计划"""
    __tablename__ = 'ASAREPLANTRADE'
    __table_args__ = (
        Index('IDX_ASAREPLANTRADE_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='首次披露公告日')
    ANN_DT_NEW = Column(VARCHAR(8), comment='最新公告日')
    IS_ADJUSTMENT = Column(Numeric(1, 0), comment='方案是否有过调整')
    PROGRAMME_PROGRESS = Column(Numeric(9, 0), comment='方案进度代码')
    HOLDER_NAME = Column(VARCHAR(100), comment='持有方名称')
    HOLDER_ID = Column(VARCHAR(10), comment='持有方id')
    HOLDER_STATUS = Column(VARCHAR(80), comment='股东身份类别')
    HOLDER_TYPE = Column(VARCHAR(1), comment='股东类型')
    HOLD_NUMBER = Column(Numeric(20, 4), comment='持有证券数量(股/张)')
    HOLD_PROPORTION = Column(Numeric(20, 4), comment='持股数量占比(%)')
    HOLD_RESTRICTED_STOCK = Column(Numeric(20, 4), comment='持有限售股数量(股)')
    HOLD_UNLIMITED_SALE_SHARES = Column(Numeric(20, 4), comment='持有无限售股数量(股)')
    TRANSACT_TYPE = Column(VARCHAR(4), comment='变动方向')
    TRANSACT_OBJECTIVE = Column(VARCHAR(400), comment='变动目的')
    TRANSACT_STOCK_SOURCE = Column(VARCHAR(100), comment='变动股份来源')
    TRANSACT_SOURCE_FUNDS = Column(VARCHAR(100), comment='变动资金来源')
    TRANSACT_PERIOD_DESCRIPTION = Column(VARCHAR(100), comment='变动期间说明')
    TRANSACTION_MODE = Column(VARCHAR(100), comment='交易方式')
    PLAN_TRANSACT_MAX_NUM = Column(Numeric(20, 4), comment='拟变动数量上限(股/张)')
    PLAN_TRANSACT_MAX_RATIO = Column(Numeric(20, 4), comment='拟变动数量上限占比(%)')
    PLAN_TRANSACT_MIN_NUM = Column(Numeric(20, 4), comment='拟变动数量下限(股/张)')
    PLAN_TRANSACT_MIN_RATIO = Column(Numeric(20, 4), comment='拟变动数量下限占比(%)')
    PLAN_MAX_HOLD_RATIO = Column(Numeric(20, 4), comment='拟最大变动数量占持有公司股份的比例(%)')
    TOT_ACTUAL_TRANSACT_NUM = Column(Numeric(20, 4), comment='实际累计变动证券数量(股/张)')
    TOTAL_CAPITAL_STOCK = Column(Numeric(20, 4), comment='公司总股本(股)')
    PLAN_TRANSACT_MIN = Column(Numeric(20, 4), comment='拟变动金额下限(元)')
    PLAN_TRANSACT_MAX = Column(Numeric(20, 4), comment='拟变动金额上限(元)')
    VARIABLE_PRICE_MEMO = Column(VARCHAR(100), comment='变动价格说明')
    CHANGE_START_DATE = Column(VARCHAR(8), comment='变动起始日期')
    CHANGE_END_DATE = Column(VARCHAR(8), comment='变动截止日期')
    IS_CHANGE_CONTROL = Column(Numeric(1, 0), comment='是否导致公司控制权变更')
    SPECIAL_CHANGES_MEMO = Column(VARCHAR(1000), comment='特殊变动说明')
    PROGRAM_ADJUSTMENT_MEMO = Column(VARCHAR(1000), comment='方案调整说明')


class ASPCITICINDEXEOD(Base):
    """中信标普指数行情"""
    __tablename__ = 'ASPCITICINDEXEOD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')


class ASPCITICINDEXWEIGHT(Base):
    """None"""
    __tablename__ = 'ASPCITICINDEXWEIGHT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CLOSEVALUE = Column(Numeric(20, 4), comment='收盘价')
    FREE_SHRARE = Column(Numeric(20, 4), comment='自由流通股本(股)')
    FREE_MARKETVAL = Column(Numeric(20, 4), comment='自由流通市值(元)')
    WEIGHT = Column(Numeric(20, 8), comment='权重(%)')


class ASSETMANAGEMENTBALANCESHEET(Base):
    """非上市资产管理公司资产负债表"""
    __tablename__ = 'ASSETMANAGEMENTBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    MONETARY_CAP = Column(Numeric(20, 4), comment='货币资金')
    CLIENTS_CAP_DEPOSIT = Column(Numeric(20, 4), comment='客户资金存款')
    SETTLE_RSRV = Column(Numeric(20, 4), comment='结算备付金')
    CLIENTS_RSRV_SETTLE = Column(Numeric(20, 4), comment='客户备付金')
    LOANS_TO_OTH_BANKS = Column(Numeric(20, 4), comment='拆出资金')
    TRADABLE_FIN_ASSETS = Column(Numeric(20, 4), comment='交易性金融资产')
    DERIVATIVE_FIN_ASSETS = Column(Numeric(20, 4), comment='衍生金融资产')
    RED_MONETARY_CAP_FOR_SALE = Column(Numeric(20, 4), comment='买入返售金融资产')
    INT_RCV = Column(Numeric(20, 4), comment='应收利息')
    MRGN_PAID = Column(Numeric(20, 4), comment='存出保证金')
    AGENCY_BUS_ASSETS = Column(Numeric(20, 4), comment='代理业务资产')
    FIN_ASSETS_AVAIL_FOR_SALE = Column(Numeric(20, 4), comment='可供出售金融资产')
    HELD_TO_MTY_INVEST = Column(Numeric(20, 4), comment='持有至到期投资')
    LONG_TERM_EQY_INVEST = Column(Numeric(20, 4), comment='长期股权投资')
    FIX_ASSETS = Column(Numeric(20, 4), comment='固定资产')
    INTANG_ASSETS = Column(Numeric(20, 4), comment='无形资产')
    INCL_SEAT_FEES_EXCHANGE = Column(Numeric(20, 4), comment='其中：交易席位费')
    GOODWILL = Column(Numeric(20, 4), comment='商誉')
    DEFERRED_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产')
    INVEST_REAL_ESTATE = Column(Numeric(20, 4), comment='投资性房地产')
    OTH_ASSETS = Column(Numeric(20, 4), comment='其他资产')
    SPE_BAL_ASSETS = Column(Numeric(20, 4), comment='资产差额(特殊报表科目)')
    TOT_BAL_ASSETS = Column(Numeric(20, 4), comment='资产差额(合计平衡项目)')
    TOT_ASSETS = Column(Numeric(20, 4), comment='资产总计')
    ST_BORROW = Column(Numeric(20, 4), comment='短期借款')
    INCL_PLEDGE_LOAN = Column(Numeric(20, 4), comment='其中：质押借款')
    LOANS_OTH_BANKS = Column(Numeric(20, 4), comment='拆入资金')
    TRADABLE_FIN_LIAB = Column(Numeric(20, 4), comment='交易性金融负债')
    DERIVATIVE_FIN_LIAB = Column(Numeric(20, 4), comment='衍生金融负债')
    FUND_SALES_FIN_ASSETS_RP = Column(Numeric(20, 4), comment='卖出回购金融资产款')
    ACTING_TRADING_SEC = Column(Numeric(20, 4), comment='代理买卖证券款')
    ACTING_UW_SEC = Column(Numeric(20, 4), comment='代理承销证券款')
    EMPL_BEN_PAYABLE = Column(Numeric(20, 4), comment='应付职工薪酬')
    TAXES_SURCHARGES_PAYABLE = Column(Numeric(20, 4), comment='应交税费')
    INT_PAYABLE = Column(Numeric(20, 4), comment='应付利息')
    AGENCY_BUS_LIAB = Column(Numeric(20, 4), comment='代理业务负债')
    LT_BORROW = Column(Numeric(20, 4), comment='长期借款')
    BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付债券')
    DEFERRED_TAX_LIAB = Column(Numeric(20, 4), comment='延所得税负债')
    PROVISIONS = Column(Numeric(20, 4), comment='预计负债')
    OTH_LIAB = Column(Numeric(20, 4), comment='其他负债')
    SPE_BAL_LIAB = Column(Numeric(20, 4), comment='负债差额(特殊报表科目)')
    TOT_BAL_LIAB = Column(Numeric(20, 4), comment='负债差额(合计平衡项目)')
    TOT_LIAB = Column(Numeric(20, 4), comment='负债合计')
    CAP_STK = Column(Numeric(20, 4), comment='股本')
    CAP_RSRV = Column(Numeric(20, 4), comment='资本公积金')
    LESS_TSY_STK = Column(Numeric(20, 4), comment='减：库存股')
    SURPLUS_RSRV = Column(Numeric(20, 4), comment='盈余公积金')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='未分配利润')
    PROV_NOM_RISKS = Column(Numeric(20, 4), comment='一般风险准备')
    CNVD_DIFF_FOREIGN_CURR_STAT = Column(Numeric(20, 4), comment='外币报表折算差额')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认的投资损失')
    SPE_BAL_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益差额(特殊报表科目)')
    TOT_BAL_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益差额(合计平衡项目)')
    MINORITY_INT = Column(Numeric(20, 4), comment='少数股东权益')
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(不含少数股东权益)')
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(含少数股东权益)')
    SPE_BAL_LIAB_EQY = Column(Numeric(20, 4), comment='负债及股东权益差额(特殊报表项目)')
    TOT_BAL_LIAB_EQY = Column(Numeric(20, 4), comment='负债及股东权益差额(合计平衡项目)')
    TOT_LIAB_SHRHLDR_EQY = Column(Numeric(20, 4), comment='负债及股东权益总计')
    OTHER_COMP_INCOME = Column(Numeric(20, 4), comment='其他综合收益')
    OTHER_EQUITY_TOOLS = Column(Numeric(20, 4), comment='其他权益工具')
    OTHER_EQUITY_TOOLS_P_SHR = Column(Numeric(20, 4), comment='其他权益工具:优先股')
    MELT_MONEY = Column(Numeric(20, 4), comment='融出资金')
    RECEIVABLES = Column(Numeric(20, 4), comment='应收款项')
    SHORT_TERM_FINANCING = Column(Numeric(20, 4), comment='应付短期融资款')
    PAYABLES = Column(Numeric(20, 4), comment='应付款项')


class ASSETMANAGEMENTCASHFLOW(Base):
    """非上市资产管理公司现金流量表"""
    __tablename__ = 'ASSETMANAGEMENTCASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    FREE_CASH_FLOW = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    NET_INCR_DISP_TFA = Column(Numeric(20, 4), comment='处置交易性金融资产净增加额')
    NET_INCR_DISP_FAAS = Column(Numeric(20, 4), comment='处置可供出售金融资产净增加额')
    NET_INCR_INT_HANDLING_CHRG = Column(Numeric(20, 4), comment='收取利息和手续费净增加额')
    NET_INCR_LOANS_OTHER_BANK = Column(Numeric(20, 4), comment='拆入资金净增加额')
    NET_INCR_REPURCH_BUS_FUND = Column(Numeric(20, 4), comment='回购业务资金净增加额')
    OTHER_CASH_RECP_RAL_OPER_ACT = Column(Numeric(20, 4), comment='收到其他与经营活动有关的现金')
    SPE_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流入小计')
    CASH_PAY_BEH_EMPL = Column(Numeric(20, 4), comment='支付给职工以及为职工支付的现金')
    PAY_ALL_TYP_TAX = Column(Numeric(20, 4), comment='支付的各项税费')
    OTHER_CASH_PAY_RAL_OPER_ACT = Column(Numeric(20, 4), comment='支付其他与经营活动有关的现金')
    HANDLING_CHRG_PAID = Column(Numeric(20, 4), comment='支付手续费的现金')
    SPE_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额')
    CASH_RECP_DISP_WITHDRWL_INVEST = Column(Numeric(20, 4), comment='收回投资收到的现金')
    CASH_RECP_RETURN_INVEST = Column(Numeric(20, 4), comment='取得投资收益收到的现金')
    NET_CASH_RECP_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定资产、无形资产和其他长期资产收回的现金净额')
    OTHER_CASH_RECP_RAL_INV_ACT = Column(Numeric(20, 4), comment='收到其他与投资活动有关的现金')
    SPE_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流入小计')
    CASH_PAID_INVEST = Column(Numeric(20, 4), comment='投资支付的现金')
    CASH_PAY_ACQ_CONST_FIOLTA = Column(Numeric(20, 4), comment='购建固定资产、无形资产和其他长期资产支付的现金')
    OTHER_CASH_PAY_RAL_INV_ACT = Column(Numeric(20, 4), comment='支付其他与投资活动有关的现金')
    SPE_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额')
    CASH_RECP_CAP_CONTRIB = Column(Numeric(20, 4), comment='吸收投资收到的现金')
    CASH_RECP_BORROW = Column(Numeric(20, 4), comment='取得借款收到的现金')
    PROC_ISSUE_BONDS = Column(Numeric(20, 4), comment='发行债券收到的现金')
    OTHER_CASH_RECP_RAL_FNC_ACT = Column(Numeric(20, 4), comment='收到其他与筹资活动有关的现金')
    SPE_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流入小计')
    CASH_PREPAY_AMT_BORR = Column(Numeric(20, 4), comment='偿还债务支付的现金')
    CASH_PAY_DIST_DPCP_INT_EXP = Column(Numeric(20, 4), comment='分配股利、利润或偿付利息支付的现金')
    OTHER_CASH_PAY_RAL_FNC_ACT = Column(Numeric(20, 4), comment='支付其他与筹资活动有关的现金')
    SPE_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额')
    EFF_FX_FLU_CASH = Column(Numeric(20, 4), comment='汇率变动对现金的影响')
    SPE_BAL_NETCASH_EQU_DIR = Column(Numeric(20, 4), comment='现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_DIR = Column(Numeric(20, 4), comment='现金净增加额差额(合计平衡项目)')
    NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物净增加额')
    CASH_CASH_EQU_BEG_PERIOD = Column(Numeric(20, 4), comment='期初现金及现金等价物余额')
    CASH_CASH_EQU_END_PERIOD = Column(Numeric(20, 4), comment='期末现金及现金等价物余额')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
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
    SPE_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(合计平衡项目)')
    IM_NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='间接法-经营活动产生的现金流量净额')
    CONV_DEBT_INTO_CAP = Column(Numeric(20, 4), comment='债务转为资本')
    CONV_CORP_BONDS_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的可转换公司债券')
    FA_FNC_LEASES = Column(Numeric(20, 4), comment='融资租入固定资产')
    END_BAL_CASH = Column(Numeric(20, 4), comment='现金的期末余额')
    LESS_BEG_BAL_CASH = Column(Numeric(20, 4), comment='减：现金的期初余额')
    PLUS_END_BAL_CASH_EQU = Column(Numeric(20, 4), comment='加：现金等价物的期末余额')
    LESS_BEG_BAL_CASH_EQU = Column(Numeric(20, 4), comment='减：现金等价物的期初余额')
    SPE_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(合计平衡项目)')
    IM_NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='间接法-现金及现金等价物净增加额')
    AGENT_TRADING_SC_NET_CASH = Column(Numeric(20, 4), comment='代理买卖证券收到的现金净额')
    MELT_MONEY_NET_INCREASE = Column(Numeric(20, 4), comment='融出资金净增加额')


class ASSETMANAGEMENTFICLASS(Base):
    """国内资管业金融机构分类"""
    __tablename__ = 'ASSETMANAGEMENTFICLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_TYPECODE = Column(VARCHAR(50), comment='分类代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASWSINDEXCLOSEWEIGHT(Base):
    """申万指数成份日收盘权重"""
    __tablename__ = 'ASWSINDEXCLOSEWEIGHT'
    __table_args__ = (
        Index('IDX_ASWSINDEXCLOSEWEIGHT_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    I_WEIGHT = Column(Numeric(20, 4), comment='权重(%)')


class ASWSINDEXEOD(Base):
    """申万指数行情"""
    __tablename__ = 'ASWSINDEXEOD'
    __table_args__ = (
        Index('IDX_ASWSINDEXEOD_TRADE_DT', 'TRADE_DT'),
        Index('INDEX_S_INFO_WINDCODE_TRADE_DT', 'S_INFO_WINDCODE', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(百股)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    S_VAL_PE = Column(Numeric(20, 4), comment='指数市盈率')
    S_VAL_PB = Column(Numeric(20, 4), comment='指数市净率')
    S_DQ_MV = Column(Numeric(20, 4), comment='A股流通市值(万元)')
    S_VAL_MV = Column(Numeric(20, 4), comment='总市值(万元)')


class BANKBRANCHINFORMATION(Base):
    """银行分支机构基本资料"""
    __tablename__ = 'BANKBRANCHINFORMATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='OBJECT_ID')
    BRANCH_ID = Column(VARCHAR(10), comment='机构ID')
    BRANCH_NAME = Column(VARCHAR(200), comment='机构名称')
    BRANCH_CODE = Column(VARCHAR(20), comment='机构编码')
    BELONG_COMPANY_ID = Column(VARCHAR(20), comment='所属机构公司ID')
    BELONG_COMPANY_NAME = Column(VARCHAR(200), comment='所属机构公司名称')
    ORGANIZATION_TYPECODE = Column(Numeric(9, 0), comment='机构类型代码')
    PROVINCE = Column(VARCHAR(30), comment='省份')
    CITY = Column(VARCHAR(100), comment='城市')
    REGION = Column(VARCHAR(100), comment='区域')
    ADDRESS = Column(VARCHAR(200), comment='地址')
    POSTCODE = Column(VARCHAR(20), comment='邮编')
    TELEPHONE = Column(VARCHAR(100), comment='电话')
    FAX = Column(VARCHAR(50), comment='传真')
    BRANCH_LEVEL_CODE = Column(Numeric(9, 0), comment='机构层级代码')
    BRANCH_SURVIVAL_STATUS = Column(Numeric(9, 0), comment='机构存续状态代码')
    DATE_ISSUE = Column(VARCHAR(8), comment='发证日期')
    DATE_ESTABLISHMENT = Column(VARCHAR(8), comment='批准成立日期')
    DATE_EXIT = Column(VARCHAR(8), comment='退出日期')
    BUSINESS_TIME = Column(VARCHAR(1000), comment='营业时间')
    BRANCH_TYPE_CODE = Column(Numeric(9, 0), comment='网点类型代码')
    SERVICE_FUNCTION = Column(VARCHAR(1000), comment='服务功能')
    PARENT_ORGANIZATION_ID = Column(VARCHAR(10), comment='上级机构ID')
    IS_DISCLOSED = Column(Numeric(1, 0), comment='是否公司披露')


class BANKINGFICLASSCBRC(Base):
    """国内银行业金融机构分类(银监会)"""
    __tablename__ = 'BANKINGFICLASSCBRC'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_TYPECODE = Column(VARCHAR(50), comment='分类代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class BANKLOAN5LCLASSIFICATION(Base):
    """银行五级分类贷款明细"""
    __tablename__ = 'BANKLOAN5LCLASSIFICATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    LOAN_TYPE = Column(VARCHAR(40), comment='贷款类型')
    TOTAL_AMOUNT = Column(Numeric(20, 4), comment='合计金额')
    LOANS_EXCL_DISCOUNT = Column(Numeric(20, 4), comment='贷款(不含贴现)')
    DISCOUNT = Column(Numeric(20, 4), comment='贴现')
    PASTDUEITEMS = Column(Numeric(20, 4), comment='逾期拆放同业及金融类公司')
    OTHERCREDITASSET = Column(Numeric(20, 4), comment='其他信贷资产')
    PROPORTION_OF_TA = Column(Numeric(20, 4), comment='贷款占贷款总额比例(%)')
    LLIMIT_OF_LLR_ACCRUALRATIO = Column(Numeric(20, 4), comment='贷款损失准备金计提比例下限(%)')
    ULIMIT_OF_LLR_ACCRUALRATIO = Column(Numeric(20, 4), comment='贷款损失准备金计提比例上限(%)')
    PROPORTION_OF_SLL = Column(Numeric(20, 4), comment='标准贷款损失计提比例(%)')
    MIGRATION_RATE = Column(Numeric(20, 4), comment='迁徙率(%)')


class BOINDEXWEIGHTSWIND(Base):
    """None"""
    __tablename__ = 'BOINDEXWEIGHTSWIND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    S_INFO_WEIGHTS = Column(Numeric(20, 4), comment='权数')
    S_INFO_INDEX_WEIGHTSRULE = Column(VARCHAR(10), comment='加权方式代码')


class BREAKINGNEWS(Base):
    """财经要闻"""
    __tablename__ = 'BREAKINGNEWS'
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


class BROKERAUDITOPINION(Base):
    """非上市券商审计意见"""
    __tablename__ = 'BROKERAUDITOPINION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_STMNOTE_AUDIT_CATEGORY = Column(Numeric(9, 0), comment='审计结果类别代码')
    S_STMNOTE_AUDIT_AGENCY = Column(VARCHAR(100), comment='会计师事务所')
    S_STMNOTE_AUDIT_CPA = Column(VARCHAR(100), comment='签字会计师')


class BROKERSALESSEGMENT(Base):
    """非上市券商主营业务构成"""
    __tablename__ = 'BROKERSALESSEGMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_SEGMENT_ITEMCODE = Column(Numeric(9, 0), comment='项目类别')
    S_SEGMENT_ITEM = Column(VARCHAR(100), comment='主营业务项目')
    S_SEGMENT_SALES = Column(Numeric(20, 4), comment='主营业务收入(元)')
    S_SEGMENT_PROFIT = Column(Numeric(20, 4), comment='主营业务利润(元)')
    S_SEGMENT_COST = Column(Numeric(20, 4), comment='主营业务成本(元)')


class CBANKDEPOSITSTRUCTURE(Base):
    """银行业存款结构"""
    __tablename__ = 'CBANKDEPOSITSTRUCTURE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    CRNCY_TYPE_CODE = Column(Numeric(9, 0), comment='币种类型代码')
    LOAN_TYPE_CODE = Column(Numeric(9, 0), comment='项目类别代码')
    DEPOSIT_ITEM_CODE = Column(Numeric(9, 0), comment='存款项目代码')
    ANN_ITEM = Column(VARCHAR(100), comment='存款项目公布名称')
    TOTAL_DEPOSIT = Column(Numeric(20, 4), comment='存款余额')
    AVE_DEPOSIT = Column(Numeric(20, 4), comment='存款平均余额')
    INTEREST_COST = Column(Numeric(20, 4), comment='存款利息支出')
    AVERAGE_YIELD = Column(Numeric(20, 4), comment='存款平均成本率')
    MEMO = Column(VARCHAR(200), comment='备注')


class CBANKFINNOTES(Base):
    """None"""
    __tablename__ = 'CBANKFINNOTES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    ITEM_DATA = Column(VARCHAR(40), comment='数据内容')
    ITEM_TYPE_CODE = Column(VARCHAR(4), comment='项目类别代码')
    ANN_ITEM = Column(VARCHAR(400), comment='项目公布名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='项目金额')
    ITEM_NAME = Column(VARCHAR(100), comment='项目容错名称')


class CBANKLOANSTRUCTURE(Base):
    """银行业贷款结构"""
    __tablename__ = 'CBANKLOANSTRUCTURE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    CRNCY_TYPE_CODE = Column(Numeric(9, 0), comment='币种类型代码')
    LOAN_TYPE_CODE = Column(Numeric(9, 0), comment='项目类别代码')
    ANN_ITEM = Column(VARCHAR(100), comment='[内部]公布名称')
    LOAN_ITEM_CODE = Column(Numeric(9, 0), comment='贷款项目代码')
    TOTAL_LOANS = Column(Numeric(20, 4), comment='贷款余额')
    AVE_LOANS = Column(Numeric(20, 4), comment='贷款平均余额')
    INTEREST_INCOME = Column(Numeric(20, 4), comment='贷款利息收入')
    AVERAGE_YIELD = Column(Numeric(20, 4), comment='贷款平均收益率')
    NON_PERFORMING_LOANS = Column(Numeric(20, 4), comment='不良贷款余额')
    NON_PERFORMING_LOANS_RATIO = Column(Numeric(20, 4), comment='不良贷款率(%)')
    MEMO = Column(VARCHAR(200), comment='备注')


class CBATAPBBINDEXWEIGHT(Base):
    """中债-国债及政策性银行债财富(总值)指数权重"""
    __tablename__ = 'CBATAPBBINDEXWEIGHT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份债Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    I_WEIGHT = Column(Numeric(20, 8), comment='权重')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='流通场所')


class CBILLBTRANSDISCOUNTQUOTE(Base):
    """中国银行间票据转贴现报价"""
    __tablename__ = 'CBILLBTRANSDISCOUNTQUOTE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    TRADE_TM = Column(VARCHAR(20), comment='时间')
    B_INFO_TRADETYPCODE = Column(Numeric(9, 0), comment='业务类型代码')
    B_INFO_TRADESIDE = Column(Numeric(1, 0), comment='交易方向')
    B_INFO_AMOUNTMN = Column(Numeric(20, 4), comment='报价金额')
    B_INFO_INTEREST = Column(Numeric(20, 8), comment='利率')
    B_ANAL_PTM = Column(VARCHAR(100), comment='剩余期限')
    B_INFO_ACCEPTTYPE = Column(Numeric(9, 0), comment='承兑行类型代码')
    B_INFO_BILLTYPE = Column(Numeric(9, 0), comment='票据类型代码')


class CBILLPUBSUMMON(Base):
    """中国票据催告公示"""
    __tablename__ = 'CBILLPUBSUMMON'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    B_INFO_BILLNO = Column(VARCHAR(100), comment='票号')
    B_INFO_BILLTYPE = Column(Numeric(9, 0), comment='票据类型代码')
    B_INFO_FACEVALUE = Column(Numeric(20, 4), comment='票面金额')
    ISSUE_DT = Column(VARCHAR(8), comment='出票日期')
    MATURITY_DT = Column(VARCHAR(8), comment='到期日')
    B_INFO_DRAWER = Column(VARCHAR(200), comment='出票人')
    B_INFO_ACCEPTBANK = Column(VARCHAR(200), comment='付款银行/付款人')
    B_INFO_SUMMONTYPE = Column(VARCHAR(40), comment='状态类别')
    B_INFO_APPLICANT = Column(VARCHAR(200), comment='申请人')
    B_INFO_NOTICERELEASER = Column(VARCHAR(200), comment='发布机构')


class CBRCNEWS(Base):
    """银监会"""
    __tablename__ = 'CBRCNEWS'
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


class CCOMMODITYFUTURESEODPRICES(Base):
    """中国商品期货日行情"""
    __tablename__ = 'CCOMMODITYFUTURESEODPRICES'
    __table_args__ = (
        Index('IDX_CCOMMODITYFUTURESEODPRICES_TRADE_DT', 'TRADE_DT'),)
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
    S_DQ_OICHANGE = Column(Numeric(20, 4), comment='持仓量变化')
    FS_INFO_TYPE = Column(VARCHAR(10), comment='合约类型')


class CCOMMODITYFUTURESPOSITIONS(Base):
    """中国商品期货成交及持仓"""
    __tablename__ = 'CCOMMODITYFUTURESPOSITIONS'
    __table_args__ = (
        Index('IDX_CCOMMODITYFUTURESPOSITIONS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    FS_INFO_MEMBERNAME = Column(VARCHAR(40), comment='会员简称')
    FS_INFO_TYPE = Column(VARCHAR(1), comment='类型')
    FS_INFO_POSITIONSNUM = Column(Numeric(20, 4), comment='数量')
    FS_INFO_RANK = Column(Numeric(5, 0), comment='名次')
    S_OI_POSITIONSNUMC = Column(Numeric(20, 4), comment='比上交易日增减')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='会员ID ')
    SEC_ID = Column(VARCHAR(10), comment='证券ID ')


class CDRAGENCY(Base):
    """中国存托凭证发行中介机构"""
    __tablename__ = 'CDRAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_AGENCY_NAME = Column(VARCHAR(200), comment='机构名称')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    S_BUSINESS_TYPCODE = Column(Numeric(9, 0), comment='业务类型代码')
    S_AGENCY_NAMEID = Column(VARCHAR(200), comment='机构名称ID')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    SEQUENCE1 = Column(VARCHAR(6), comment='序号')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class CDRBALANCESHEET(Base):
    """中国存托凭证资产负债表"""
    __tablename__ = 'CDRBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
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
    FIN_ASSETS_COST_SHARING = Column(Numeric(20, 4), comment='以摊余成本计量的金融资产')
    FIN_ASSETS_FAIR_VALUE = Column(Numeric(20, 4), comment='以公允价值计量且其变动计入其他综合收益的金融资产')


class CDRCASHFLOW(Base):
    """中国存托凭证现金流量表"""
    __tablename__ = 'CDRCASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
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


class CDRCOMPANYHOLDSHARES(Base):
    """中国存托凭证控股参股"""
    __tablename__ = 'CDRCOMPANYHOLDSHARES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_CAPITALOPERATION_COMPANYNAME = Column(VARCHAR(100), comment='被参控公司名称')
    S_CAPITALOPERATION_COMPANYID = Column(VARCHAR(10), comment='被参控公司ID')
    S_CAPITALOPERATION_COMAINBUS = Column(VARCHAR(150), comment='被参控公司主营业务')
    RELATIONS_CODE = Column(VARCHAR(40), comment='关系代码')
    S_CAPITALOPERATION_PCT = Column(Numeric(20, 4), comment='直接持股比例')
    VOTING_RIGHTS = Column(Numeric(20, 4), comment='表决权比例')
    S_CAPITALOPERATION_AMOUNT = Column(Numeric(20, 4), comment='投资金额(万元)')
    OPERATIONCRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_CAPITALOPERATION_COREGCAP = Column(Numeric(20, 4), comment='被参股公司注册资本(万元)')
    CAPITALCRNCY_CODE = Column(VARCHAR(10), comment='注册资本货币代码')
    IS_CONSOLIDATE = Column(Numeric(5, 0), comment='是否合并报表')
    NOTCONSOLIDATE_REASON = Column(VARCHAR(500), comment='未纳入合并报表原因')


class CDRCOMPRFA(Base):
    """中国存托凭证审核申报企业情况"""
    __tablename__ = 'CDRCOMPRFA'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPANYID = Column(VARCHAR(40), comment='公司ID')
    REGADDR = Column(VARCHAR(20), comment='注册地')
    SECTORS = Column(VARCHAR(100), comment='所属行业')
    SPONSOR = Column(VARCHAR(200), comment='保荐机构')
    SPON_REP = Column(VARCHAR(100), comment='保荐代表人')
    ACC_FIRM = Column(VARCHAR(200), comment='会计师事务所')
    CPA = Column(VARCHAR(100), comment='签字会计师')
    LAW_FIRM = Column(VARCHAR(200), comment='律师事务所')
    SOL_SIG = Column(VARCHAR(100), comment='签字律师')
    APP_CODE = Column(Numeric(9, 0), comment='申请事项代码')
    SCH_CODE = Column(Numeric(9, 0), comment='进度类型代码')
    TBLISTED = Column(Numeric(9, 0), comment='拟上市板块代码')
    ST_DATE = Column(VARCHAR(8), comment='状态起始日期')
    END_DATE = Column(VARCHAR(8), comment='状态终止日期')
    EST_ISSUENO = Column(Numeric(20, 4), comment='预计发行股数（万股）')
    EST_ISSUESHARES = Column(Numeric(20, 4), comment='预计发行后总股本（万股）')
    PRO_TOLALINV = Column(Numeric(20, 4), comment='募投项目投资总额')


class CDRDESCRIPTION(Base):
    """中国存托凭证基本资料"""
    __tablename__ = 'CDRDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司中文名称')
    S_INFO_COMPNAMEENG = Column(VARCHAR(100), comment='公司英文名称')
    S_INFO_ISINCODE = Column(VARCHAR(40), comment='ISIN代码')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_LISTBOARD = Column(VARCHAR(10), comment='上市板类型')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_PINYIN = Column(VARCHAR(40), comment='简称拼音')
    S_INFO_LISTBOARDNAME = Column(VARCHAR(10), comment='上市板')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class CDRDIVIDEND(Base):
    """中国存托凭证分红条款"""
    __tablename__ = 'CDRDIVIDEND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TYPE_CODE = Column(Numeric(9, 0), comment='品种类别代码')
    CLAUSE_TYPE_CODE = Column(Numeric(9, 0), comment='条款属性类型代码')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    CLAUSE_CONTENT = Column(VARCHAR(3000), comment='条款')
    ANN_ITEM = Column(Numeric(1, 0), comment='是否最新')


class CDRHOLDINGOPERATE(Base):
    """中国存托凭证主要控股参股公司经营情况"""
    __tablename__ = 'CDRHOLDINGOPERATE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='截止日期')
    S_CAPITALOPERATION_COMPANYNAME = Column(VARCHAR(80), comment='被参控公司名称')
    S_TOT_ASSETS = Column(Numeric(24, 8), comment='资产规模')
    S_NET_PROFIT = Column(Numeric(24, 8), comment='净利润')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_NET_ASSETS = Column(Numeric(24, 8), comment='净资产')
    S_TOT_LIAB = Column(Numeric(24, 8), comment='负债总额')
    S_OPER_REV = Column(Numeric(24, 8), comment='营业收入')
    S_TOT_PROFIT = Column(Numeric(24, 8), comment='利润总额')


class CDRINCOME(Base):
    """中国存托凭证利润表"""
    __tablename__ = 'CDRINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
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
    EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    NET_PROFIT_AFTER_DED_NR_LP = Column(Numeric(20, 4), comment='扣除非经常性损益后净利润')
    NET_PROFIT_UNDER_INTL_ACC_STA = Column(Numeric(20, 4), comment='国际会计准则净利润')
    COMP_TYPE_CODE = Column(VARCHAR(2), comment='公司类型代码')
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
    NET_AFTER_DED_NR_LP_CORRECT = Column(Numeric(20, 4), comment='扣除非经常性损益后的净利润(财务重要指标(更正前))')
    OTHER_INCOME = Column(Numeric(20, 4), comment='其他收益')
    MEMO = Column(VARCHAR(1000), comment='备注')
    ASSET_DISPOSAL_INCOME = Column(Numeric(20, 4), comment='资产处置收益')
    CONTINUED_NET_PROFIT = Column(Numeric(20, 4), comment='持续经营净利润')
    END_NET_PROFIT = Column(Numeric(20, 4), comment='终止经营净利润')


class CDRINDUSTRIESCLASS(Base):
    """中国存托凭证Wind行业分类"""
    __tablename__ = 'CDRINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    WIND_IND_CODE = Column(VARCHAR(50), comment='Wind行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class CDRINTRODUCTION(Base):
    """中国存托凭证公司简介"""
    __tablename__ = 'CDRINTRODUCTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_PROVINCE = Column(VARCHAR(20), comment='省份')
    S_INFO_CITY = Column(VARCHAR(20), comment='城市')
    S_INFO_CHAIRMAN = Column(VARCHAR(38), comment='法人代表')
    S_INFO_PRESIDENT = Column(VARCHAR(38), comment='总经理')
    S_INFO_BDSECRETARY = Column(VARCHAR(500), comment='董事会秘书')
    S_INFO_REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    S_INFO_FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    S_INFO_CHINESEINTRODUCTION = Column(VARCHAR(2000), comment='公司中文简介')
    S_INFO_COMPTYPE = Column(VARCHAR(20), comment='公司类型')
    S_INFO_WEBSITE = Column(VARCHAR(80), comment='主页')
    S_INFO_EMAIL = Column(VARCHAR(80), comment='电子邮箱')
    S_INFO_OFFICE = Column(VARCHAR(200), comment='办公地址')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_COUNTRY = Column(VARCHAR(20), comment='国籍')
    S_INFO_BUSINESSSCOPE = Column(VARCHAR(2000), comment='经营范围')
    S_INFO_COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')


class CDRISSUECOMMAUDIT(Base):
    """中国存托凭证发行审核一览"""
    __tablename__ = 'CDRISSUECOMMAUDIT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPANYNAME = Column(VARCHAR(100), comment='公司名称')
    S_IC_YEAR = Column(VARCHAR(4), comment='年度')
    S_IC_SESSIONTIMES = Column(VARCHAR(3), comment='会议届次')
    S_IC_AUDITTYPE = Column(VARCHAR(40), comment='审核类型')
    S_IC_TYPE = Column(Numeric(9, 0), comment='发审委类型')
    S_IC_ANNOUNCEMENTDATE = Column(VARCHAR(8), comment='会议公告日期')
    S_IC_DATE = Column(VARCHAR(8), comment='会议日期')
    S_IC_AUDITOCETYPE = Column(VARCHAR(100), comment='审核结果类型')
    S_IC_AUDITANNOCEDATE = Column(VARCHAR(8), comment='审核结果公告日期')
    S_INFO_EXPECTEDISSUESHARES = Column(Numeric(20, 4), comment='预计发行股数(万股)')
    S_INFO_EXPECTEDCOLLECTION = Column(Numeric(20, 4), comment='预计募集资金(万元)')
    S_INFO_VETO_REASON = Column(TEXT(2147483647), comment='被否原因')


class CDRMANAGEMENT(Base):
    """中国存托凭证管理层成员"""
    __tablename__ = 'CDRMANAGEMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_CODECODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_GENDER = Column(VARCHAR(10), comment='性别')
    S_INFO_MANAGER_EDUCATION = Column(VARCHAR(10), comment='学历')
    S_INFO_MANAGER_NATIONALITY = Column(VARCHAR(40), comment='国籍')
    S_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(8), comment='出生年份')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8), comment='离职日期')
    S_INFO_MANAGER_TYPE = Column(Numeric(5, 0), comment='管理层类别')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='职务')
    S_INFO_MANAGER_INTRODUCTION = Column(VARCHAR(2000), comment='个人简历')
    MANID = Column(VARCHAR(10), comment='人物ID')
    DISPLAY_ORDER = Column(Numeric(4, 0), comment='展示顺序')


class CDRSECNINDUSTRIESCLASS(Base):
    """中国存托凭证证监会新版行业分类"""
    __tablename__ = 'CDRSECNINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    SEC_IND_CODE = Column(VARCHAR(50), comment='证监会行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class CDRSTAFF(Base):
    """中国存托凭证员工人数变更"""
    __tablename__ = 'CDRSTAFF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 4), comment='员工人数(人)')
    S_INFO_TOTALEMPLOYEES2 = Column(Numeric(20, 0), comment='母公司员工人数(人)')
    MEMO = Column(VARCHAR(1000), comment='特殊情况说明')


class CDRSTAFFSTRUCTURE(Base):
    """中国存托凭证员工构成"""
    __tablename__ = 'CDRSTAFFSTRUCTURE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='交易代码')
    STAFF_TYPE_CODE = Column(Numeric(9, 0), comment='人数类别代码')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    REPORT_TYPE_CODE = Column(Numeric(9, 0), comment='报告类型代码')
    ITEM_TYPE_CODE = Column(Numeric(9, 0), comment='项目分类代码')
    ITEM_NAME = Column(VARCHAR(100), comment='项目')
    ITEM_CODE = Column(Numeric(9, 0), comment='项目代码')
    STAFF_NUMBER = Column(Numeric(20, 0), comment='人数')
    PROPORTION = Column(Numeric(20, 4), comment='所占比例')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class CFETSEODPRICE(Base):
    """银行间债券市场现券行情"""
    __tablename__ = 'CFETSEODPRICE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    TYPE = Column(VARCHAR(10), comment='交易方式')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    S_DQ_PRECLOSE = Column(Numeric(20, 10), comment='前收盘净价')
    WA_NETPRICE = Column(Numeric(20, 4), comment='均价')
    WA_PRENETPRICE = Column(Numeric(20, 10), comment='前加权平均净价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(万元)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(万元)')
    S_DQ_PCTCHANGE = Column(Numeric(20, 10), comment='涨跌幅')
    S_DQ_OPENYIELD = Column(Numeric(20, 10), comment='开盘收益率')
    S_DQ_HIGHYIELD = Column(Numeric(20, 10), comment='最高收益率')
    S_DQ_LOWYIELD = Column(Numeric(20, 10), comment='最低收益率')
    S_DQ_CLOSEYIELD = Column(Numeric(20, 10), comment='收盘收益率')
    S_DQ_PRECLOSEYIELD = Column(Numeric(20, 10), comment='前收盘收益率')
    WA_YIELD = Column(Numeric(20, 10), comment='加权平均收益率')
    WA_PREYIELD = Column(Numeric(20, 10), comment='前加权平均收益率')


class CGOLDSPOTDESCRIPTION(Base):
    """中国黄金现货基本资料"""
    __tablename__ = 'CGOLDSPOTDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券中文简称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_PUNIT = Column(VARCHAR(40), comment='交易单位')


class CGOLDSPOTDESCRIPTIONZL(Base):
    """中国黄金现货基本资料(增量)"""
    __tablename__ = 'CGOLDSPOTDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券中文简称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_PUNIT = Column(VARCHAR(40), comment='交易单位')


class CGOLDSPOTEODPRICES(Base):
    """中国黄金现货日行情"""
    __tablename__ = 'CGOLDSPOTEODPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(元)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(元)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(元)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(元)')
    S_DQ_AVGPRICE = Column(Numeric(20, 4), comment='均价(元)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(千克)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(元)')
    S_DQ_OI = Column(Numeric(20, 4), comment='持仓量(手)')
    DEL_AMT = Column(Numeric(20, 4), comment='交收量(手)')
    S_DQ_SETTLE = Column(Numeric(20, 4), comment='结算价(元) ')
    DELAY_PAY_TYPECODE = Column(Numeric(9, 0), comment='延期补偿费支付方式向类别代码 ')
    S_PCT_CHG = Column(Numeric(20, 4), comment='涨跌幅(%)')


class CHANGEWINDCODE(Base):
    """Wind代码变更表"""
    __tablename__ = 'CHANGEWINDCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前Wind代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后Wind代码')
    CHANGE_DATE = Column(VARCHAR(8), comment='Wind代码变更日期')
    S_INFO_CHANGE_REASON = Column(Numeric(9, 0), comment='变更原因代码')


class CHANGEWINDCODEQL(Base):
    """None"""
    __tablename__ = 'CHANGEWINDCODEQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_OLDWINDCODE = Column(VARCHAR(40))
    S_INFO_NEWWINDCODE = Column(VARCHAR(40))
    CHANGE_DATE = Column(VARCHAR(8))
    S_INFO_CHANGE_REASON = Column(Numeric(9, 0))


class CHANGEWINDCODEZL(Base):
    """Wind代码变更表(增量)"""
    __tablename__ = 'CHANGEWINDCODEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前Wind代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后Wind代码')
    CHANGE_DATE = Column(VARCHAR(8), comment='Wind代码变更日期')
    S_INFO_CHANGE_REASON = Column(Numeric(9, 0), comment='变更原因代码')


class CHFINDEXDESCRIPTION(Base):
    """中国私募基金指数基本资料"""
    __tablename__ = 'CHFINDEXDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='指数名称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_PUBLISHER = Column(VARCHAR(100), comment='发布方')
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8), comment='基期')
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4), comment='基点')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    S_INFO_INDEX_WEIGHTSRULE = Column(VARCHAR(40), comment='加权方式')
    S_INFO_INDEXSTYLE = Column(VARCHAR(40), comment='指数风格')
    INDEX_INTRO = Column(TEXT(2147483647), comment='指数简介')
    EXPIRE_DATE = Column(VARCHAR(8), comment='终止发布日期')


class CHFINDEXEOD(Base):
    """中国私募基金指数行情"""
    __tablename__ = 'CHFINDEXEOD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='指数简称')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='最新价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class CHFMANAGERINFORMATION(Base):
    """中国私募基金管理人资料"""
    __tablename__ = 'CHFMANAGERINFORMATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_CORP_FUNDMANAGEMENTCOMP = Column(VARCHAR(100), comment='基金管理人全称(中文)')
    F_INFO_FUNDMANAGEMENTCOMP_E = Column(VARCHAR(100), comment='基金管理人全称(英文)')
    F_INFO_SEQUENCE = Column(VARCHAR(20), comment='登记编号')
    F_INFO_ORG_CODE = Column(VARCHAR(20), comment='组织机构代码')
    F_INFO_REGISTRATION_TIME = Column(VARCHAR(8), comment='登记时间')
    F_INFO_ESTABLISH_TIME = Column(VARCHAR(8), comment='成立时间')
    F_INFO_ADDRESS = Column(VARCHAR(200), comment='注册地址')
    F_INFO_OFFICE = Column(VARCHAR(200), comment='办公地址')
    F_INFO_REGCAPITAL = Column(Numeric(20, 4), comment='注册资本')
    F_INFO_PAIDCAPITAL = Column(Numeric(20, 4), comment='实缴资本')
    F_INFO_COMP_PROPERTY = Column(VARCHAR(20), comment='企业性质')
    F_INFO_RATIO = Column(Numeric(20, 4), comment='注册资本实缴比例')
    F_INFO_MANAGED_FUND_TYPE = Column(VARCHAR(100), comment='管理基金主要类别')
    F_INFO_APPLY_OTHER_BUSINESS = Column(VARCHAR(100), comment='申请的其他业务类型')
    F_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工人数')
    F_INFO_WEBSITE = Column(VARCHAR(200), comment='机构网址')
    F_INFO_DISCLOSUREWEBSITE = Column(VARCHAR(200), comment='协会披露网址')
    F_INFO_MANAGEMENT_SCALE = Column(Numeric(20, 4), comment='公司管理规模')
    F_INFO_SINCERITY = Column(TEXT(2147483647), comment='机构诚信信息')
    F_INFO_REPORTING_TIME = Column(VARCHAR(8), comment='机构信息最后报告时间')
    F_SPECIAL_HINT_INFORMATION = Column(VARCHAR(200), comment='特别提示信息')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_INFO_LEGAL_OPINION = Column(VARCHAR(50), comment='法律意见书状态')
    F_INFO_LAW_FIRM = Column(VARCHAR(100), comment='律师事务所名称')
    F_INFO_SOL_SIG = Column(VARCHAR(50), comment='律师姓名')
    F_INFO_COMPANYID = Column(VARCHAR(10), comment='管理人公司ID')
    F_MANAGEMENT_SCALE_INTERVAL = Column(VARCHAR(200), comment='管理规模区间')
    IS_NEW = Column(Numeric(1, 0), comment='是否最新')
    IS_MEMBER = Column(Numeric(1, 0), comment='是否为会员')
    F_INFO_MEMBER_TYPE = Column(VARCHAR(40), comment='当前会员类型')
    F_INFO_TIME_ADMISSION = Column(VARCHAR(8), comment='入会时间')
    F_INFO_CRNCY_CODE = Column(VARCHAR(10), comment='币种')


class CHFUNDDESCRIPTIONZL(Base):
    """中港互认基金基本资料(增量)"""
    __tablename__ = 'CHFUNDDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_COMPCODE = Column(VARCHAR(40), comment='基金ID')
    F_INFO_FULLNAME = Column(VARCHAR(400), comment='基金名称')
    SEC_ID = Column(VARCHAR(40), comment='子基金ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='子基金Wind代码')
    F_INFO_NAME = Column(VARCHAR(100), comment='子基金简称')
    F_INFO_PINYIN = Column(VARCHAR(50), comment='子基金简称拼音')
    IS_CH = Column(Numeric(1, 0), comment='是否互认子基金')
    F_INFO_CORP_FUNDMANAGEMENTID = Column(VARCHAR(40), comment='管理人公司ID')
    F_INFO_CORP_FUNDMANAGEMENTCOMP = Column(VARCHAR(200), comment='管理人')
    F_INFO_FIRSTINVESTTYPE = Column(VARCHAR(40), comment='投资类型')
    F_INFO_SETUPDATE = Column(VARCHAR(8), comment='成立日期')
    F_INFO_MATURITYDATE = Column(VARCHAR(8), comment='到期日期')
    F_PCHREDM_PCHSTARTDATE = Column(VARCHAR(8), comment='上市日期')
    F_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    F_INFO_ISINITIAL = Column(Numeric(1, 0), comment='是否为初始基金')
    F_INFO_INVESTSCOPE = Column(TEXT(2147483647), comment='投资范围')
    F_INFO_INVESTOBJECT = Column(TEXT(2147483647), comment='投资目标')
    F_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    REGISTRATION = Column(VARCHAR(10), comment='注册地代码')
    CRNY_CODE = Column(VARCHAR(10), comment='交易币种代码')
    CHCODE = Column(VARCHAR(10), comment='代码(证监会)')
    CHNAME = Column(VARCHAR(100), comment='简称(证监会)')


class CHFUNDLISTZL(Base):
    """中港互认基金名单(增量)"""
    __tablename__ = 'CHFUNDLISTZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_COMPCODE = Column(VARCHAR(40), comment='基金ID')
    F_INFO_FULLNAME = Column(VARCHAR(400), comment='基金名称')
    F_INFO_CORP_FUNDMANAGEMENTID = Column(VARCHAR(40), comment='管理人公司ID')
    F_INFO_CORP_FUNDMANAGEMENTCOMP = Column(VARCHAR(300), comment='基金管理人')
    REGISTRATION = Column(VARCHAR(10), comment='注册地代码')
    FUNDTYPE = Column(VARCHAR(20), comment='类别')
    START_DT = Column(VARCHAR(8), comment='纳入日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CHGFINYEARENDDT(Base):
    """香港股票财报年结日变更"""
    __tablename__ = 'CHGFINYEARENDDT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='品种ID')
    ID_TYPECODE = Column(Numeric(9, 0), comment='品种类别代码')
    CHG_TYPECODE = Column(Numeric(9, 0), comment='条款属性类型代码')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    FINYEARENDDT = Column(TEXT(2147483647), comment='条款')
    CUR_SIGN = Column(Numeric(1, 0), comment='是否最新')


class CHINABONDDELIVERYSTATISTICS(Base):
    """金融机构债券交割量月度统计(中债)"""
    __tablename__ = 'CHINABONDDELIVERYSTATISTICS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    ANN_DATE = Column(VARCHAR(8), comment='日期')
    ORGANIZATION_NAME = Column(VARCHAR(100), comment='机构名称')
    MECHANISM_TYPE = Column(VARCHAR(40), comment='机构类型')
    BOND_DELIVERY_VOLUME = Column(Numeric(20, 4), comment='债券交割量(万元)')
    BOND_PROPORTION = Column(Numeric(20, 4), comment='占同类机构比重(%)')
    DATA_TYPE = Column(VARCHAR(40), comment='数据类型')


class CHINABWMCURVE(Base):
    """中国银行理财产品收益率曲线"""
    __tablename__ = 'CHINABWMCURVE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CODE = Column(Numeric(9, 0), comment='理财产品收益率曲线代码')
    NAME = Column(VARCHAR(80), comment='曲线名称')
    TERM = Column(VARCHAR(20), comment='曲线期限')
    YIELD = Column(Numeric(20, 4), comment='预期平均年收益率(%)')
    ISSUERNAME = Column(VARCHAR(80), comment='发行银行')
    CRNCY_CODE = Column(VARCHAR(10), comment='币种')


class CHINABWMDESC(Base):
    """中国银行理财产品基本资料"""
    __tablename__ = 'CHINABWMDESC'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    FULLNAME = Column(VARCHAR(200), comment='产品名称')
    ISSUERNAME = Column(VARCHAR(80), comment='发行人')
    MANAGEMENTCOMP = Column(VARCHAR(200), comment='管理人')
    CUSTODIANBANK = Column(VARCHAR(100), comment='托管人')
    ISSUINGPLACE = Column(VARCHAR(400), comment='发售地区')
    ISSUEOBJECT = Column(VARCHAR(100), comment='发行对象')
    PURCHASECHANNELS = Column(VARCHAR(200), comment='购买渠道')
    PAYMENTTYPE = Column(VARCHAR(80), comment='付息方式')
    RETURNTYPE = Column(VARCHAR(40), comment='收益类型')
    INVESTFIELD = Column(VARCHAR(100), comment='基础资产')
    BUSINESSMODEL = Column(VARCHAR(40), comment='业务模式')
    UNDERLYING = Column(VARCHAR(400), comment='挂钩标的')
    PURCHASERNUM = Column(Numeric(20, 4), comment='购买人数')
    STRUCTURE = Column(VARCHAR(40), comment='产品结构')
    PRINCIPALRATIO = Column(Numeric(5, 0), comment='保本比例')
    PLEDGEISNOT = Column(Numeric(1, 0), comment='是否可质押')
    CRNCY_CODE = Column(VARCHAR(10), comment='币种')
    PLAN_AMT_MIN = Column(Numeric(20, 4), comment='计划募资金额下限(亿元)')
    PLAN_AMT_MAX = Column(Numeric(20, 4), comment='计划募资金额上限(亿元)')
    ENTSTART_AMT = Column(Numeric(20, 4), comment='委托起始金额')
    ACT_AMT = Column(Numeric(20, 4), comment='销售规模(亿元)')
    SALESTARTDATE = Column(VARCHAR(8), comment='销售起始日')
    SALEENDDATE = Column(VARCHAR(8), comment='销售截止日')
    INCOMESTARTDATE = Column(VARCHAR(8), comment='收益起始日')
    INCOMEENDDATE = Column(VARCHAR(8), comment='收益到期日')
    EFFINCOMEENDDATE = Column(VARCHAR(8), comment='收益实际到期日')
    COMMISSION = Column(Numeric(20, 4), comment='委托期(天)')
    EFFCOMMISSION = Column(Numeric(20, 4), comment='实际委托期(天)')
    EXPYIELD_MAX = Column(Numeric(20, 4), comment='预期收益率上限')
    EXPYIDLD_MIN = Column(Numeric(20, 4), comment='预期收益率下限')
    EXPYEARYIELD_MAX = Column(Numeric(20, 4), comment='预期年化收益率上限')
    EXPYEARYIELD_MIN = Column(Numeric(20, 4), comment='预期年化收益率下限')
    EFFYIELD = Column(Numeric(20, 4), comment='实际收益率')
    EFFYEARYIELD = Column(Numeric(20, 4), comment='实际年化收益率')
    CAPYIELD = Column(Numeric(20, 4), comment='封顶收益率')
    YIELDDESCRIPTION = Column(VARCHAR(4000), comment='收益率说明')
    DEPEDESCRIPTION = Column(VARCHAR(2800), comment='委托期说明')
    FEEDESCRIPTION = Column(VARCHAR(2000), comment='费用说明')
    PRODUCTINTRODUCTION = Column(TEXT(2147483647), comment='产品简介')
    MANAGEMENTFEE = Column(Numeric(20, 4), comment='管理费率')
    CUSTODIANFEE = Column(Numeric(20, 4), comment='托管费率')
    SUBSCRIPTIONFEE = Column(Numeric(20, 4), comment='认购费率')
    REDEMPTIONFEE = Column(Numeric(20, 4), comment='赎回费率')
    PURCHASECHANNEL = Column(VARCHAR(200), comment='购买渠道')
    F_INFO_OPERATION_CODE = Column(VARCHAR(100), comment='业务代码')
    INVESTSCOPE = Column(VARCHAR(800), comment='投资范围')
    ISSUERID = Column(VARCHAR(40), comment='发行人公司ID')
    ISSUERNAME_TYPE = Column(VARCHAR(50), comment='发行人类型')


class CHINABWMNAV(Base):
    """中国银行理财产品净值"""
    __tablename__ = 'CHINABWMNAV'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    PRICE_DATE = Column(VARCHAR(8), comment='截止日期')
    F_NAV_UNIT = Column(Numeric(20, 6), comment='单位净值')
    F_NAV_ACCUMULATED = Column(Numeric(20, 7), comment='累计净值')
    F_NAV_DIVACCUMULATED = Column(Numeric(20, 8), comment='累计分红')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')


class CHINABWMSTAGEINCOME(Base):
    """中国银行理财产品阶段收益"""
    __tablename__ = 'CHINABWMSTAGEINCOME'
    PRODUCT_ID = Column(VARCHAR(10), comment='产品证券ID')
    INCOMESTARTDATE = Column(VARCHAR(8), comment='收益起始日')
    INCOMEENDDATE = Column(VARCHAR(8), comment='收益截止日')
    INTERVAL_YIELD = Column(Numeric(24, 6), comment='区间收益率')
    IS_PUBLISHED_VALUE = Column(Numeric(5, 0), comment='是否公布值')
    IS_ROE = Column(Numeric(5, 0), comment='是否年化收益率')
    CRNCY_CODE = Column(VARCHAR(10), comment='币种')
    F_NAV_ADJUSTED = Column(Numeric(20, 8), comment='复权单位净值(计算)')
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')


class CHINAINHOUSEFUNDDESCRIPTION(Base):
    """中国券商理财基本资料"""
    __tablename__ = 'CHINAINHOUSEFUNDDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_OPERATION_CODE = Column(VARCHAR(40), comment='业务代码')
    F_INFO_FULLNAME = Column(VARCHAR(100), comment='名称')
    F_INFO_NAME = Column(VARCHAR(100), comment='简称')
    F_INFO_CORP_FUNDMANAGEMENTCOMP = Column(VARCHAR(100), comment='管理人')
    F_INFO_CUSTODIANBANK = Column(VARCHAR(100), comment='托管人')
    F_INFO_FIRSTINVESTTYPE = Column(VARCHAR(40), comment='投资类型')
    F_INFO_SETUPDATE = Column(VARCHAR(8), comment='成立日期')
    F_INFO_MATURITYDATE = Column(VARCHAR(8), comment='到期日期')
    F_ISSUE_TOTALUNIT = Column(Numeric(20, 4), comment='发行份额')
    F_INFO_MANAGEMENTFEERATIO = Column(Numeric(20, 4), comment='管理费')
    F_INFO_CUSTODIANFEERATIO = Column(Numeric(20, 4), comment='托管费')
    CRNY_CODE = Column(VARCHAR(10))
    F_INFO_PTMYEAR = Column(Numeric(20, 4), comment='存续期')
    F_ISSUE_OEF_STARTDATEINST = Column(VARCHAR(8), comment='推广起始日期')
    F_ISSUE_OEF_DNDDATEINST = Column(VARCHAR(8), comment='推广截止日期')
    F_INFO_PARVALUE = Column(Numeric(20, 4), comment='面值')
    F_INFO_TRUSTTYPE = Column(VARCHAR(40), comment='信托类别')
    F_INFO_TRUSTEE = Column(VARCHAR(100), comment='受托人')
    F_PCHREDM_PCHSTARTDATE = Column(VARCHAR(8), comment='上市日期/申购首日')
    F_INFO_REDMSTARTDATE = Column(VARCHAR(8), comment='日常赎回起始日')
    F_INFO_MINBUYAMOUNT = Column(Numeric(20, 4), comment='起点金额')
    F_INFO_EXPECTEDRATEOFRETURN = Column(Numeric(20, 4), comment='预期收益率')
    F_INFO_ISSUINGPLACE = Column(VARCHAR(100), comment='发行地')
    F_INFO_BENCHMARK = Column(VARCHAR(500), comment='业绩比较基准')
    F_INFO_STATUS = Column(Numeric(9, 0), comment='存续状态')
    F_INFO_RESTRICTEDORNOT = Column(VARCHAR(20), comment='限定类型')
    F_INFO_STRUCTUREDORNOT = Column(Numeric(1, 0), comment='是否结构化产品')
    F_INFO_SETUPSCALE = Column(Numeric(20, 4), comment='成立规模')
    F_INFO_EFFSUBSCRHOLEDERNO = Column(Numeric(20, 4), comment='有效认购户数')
    F_INFO_ANNOUNCEWEB = Column(VARCHAR(200), comment='信息披露网址')
    F_INFO_TARGETSCALE = Column(Numeric(20, 4), comment='目标规模(亿元)')
    F_INFO_MGR_PARTAKE = Column(Numeric(20, 4), comment='管理人参与金额(万元)')
    F_INFO_REWARDTAG = Column(Numeric(5, 0), comment='是否提取业绩报酬')
    F_INFO_INVESTOBJECT = Column(VARCHAR(600), comment='投资目标')
    F_INFO_CORP_FUNDMANAGEMENTID = Column(VARCHAR(10), comment='管理人ID')
    TYPECODE = Column(Numeric(9, 0), comment='产品类型代码')
    MIN_AMOUNT = Column(Numeric(20, 4), comment='追加认购最低金额(万元)')
    OPENDAY_INFO = Column(VARCHAR(1000), comment='开放日说明')
    F_INFO_INITIAL_FUND = Column(Numeric(1, 0), comment='是否初始基金')


class CHINAINHOUSEFUNDDIVIDEND(Base):
    """中国券商集合理财分红"""
    __tablename__ = 'CHINAINHOUSEFUNDDIVIDEND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EQY_RECORD_DT = Column(VARCHAR(8), comment='权益登记日')
    EX_DT = Column(VARCHAR(8), comment='除息日')
    DVD_PAYOUT_DT = Column(VARCHAR(8), comment='红利发放日')
    F_TEN_SP_DIV = Column(Numeric(20, 4), comment='每10份集合计划分红额')
    F_INFO_SPLITDATE = Column(VARCHAR(8), comment='份额拆分日')
    F_INFO_SPLITINC = Column(Numeric(20, 8), comment='份额拆分比例')


class CHINAINHOUSEFUNDMANAGER(Base):
    """中国券商理财基金经理"""
    __tablename__ = 'CHINAINHOUSEFUNDMANAGER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_INFO_FUNDMANAGER = Column(VARCHAR(160), comment='姓名')
    F_INFO_MANAGER_GENDER = Column(VARCHAR(10), comment='性别')
    F_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(10), comment='出身年份')
    F_INFO_MANAGER_EDUCATION = Column(VARCHAR(20), comment='学历')
    F_INFO_MANAGER_NATIONALITY = Column(VARCHAR(10), comment='国籍')
    F_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    F_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8), comment='离职日期')
    F_INFO_POSITION = Column(VARCHAR(20), comment='职务')
    F_INFO_MANAGER_RESUME = Column(VARCHAR(2000), comment='简历')
    F_INFO_FUNDMANAGER_ID = Column(VARCHAR(10), comment='基金经理ID')


class CHINAINHOUSEFUNDMANAGERQL(Base):
    """None"""
    __tablename__ = 'CHINAINHOUSEFUNDMANAGERQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    F_INFO_WINDCODE = Column(VARCHAR(40))
    ANN_DATE = Column(VARCHAR(8))
    F_INFO_FUNDMANAGER = Column(VARCHAR(160))
    F_INFO_MANAGER_GENDER = Column(VARCHAR(10))
    F_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(10))
    F_INFO_MANAGER_EDUCATION = Column(VARCHAR(20))
    F_INFO_MANAGER_NATIONALITY = Column(VARCHAR(10))
    F_INFO_MANAGER_STARTDATE = Column(VARCHAR(8))
    F_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8))
    F_INFO_POSITION = Column(VARCHAR(20))
    F_INFO_MANAGER_RESUME = Column(VARCHAR(2000))
    F_INFO_FUNDMANAGER_ID = Column(VARCHAR(10))


class CHINAINHOUSEFUNDMANAGERZL(Base):
    """中国券商理财基金经理(增量)"""
    __tablename__ = 'CHINAINHOUSEFUNDMANAGERZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_INFO_FUNDMANAGER = Column(VARCHAR(160), comment='姓名')
    F_INFO_MANAGER_GENDER = Column(VARCHAR(10), comment='性别')
    F_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(10), comment='出身年份')
    F_INFO_MANAGER_EDUCATION = Column(VARCHAR(20), comment='学历')
    F_INFO_MANAGER_NATIONALITY = Column(VARCHAR(10), comment='国籍')
    F_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    F_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8), comment='离职日期')
    F_INFO_POSITION = Column(VARCHAR(20), comment='职务')
    F_INFO_MANAGER_RESUME = Column(VARCHAR(2000), comment='简历')
    F_INFO_FUNDMANAGER_ID = Column(VARCHAR(10), comment='基金经理ID')


class CHINAINHOUSEFUNDMARKETFINCOME(Base):
    """中国券商理财(货币式)收益率"""
    __tablename__ = 'CHINAINHOUSEFUNDMARKETFINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_BGNDATE = Column(VARCHAR(8), comment='起始日期')
    F_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    F_INFO_UNITYIELD = Column(Numeric(20, 5), comment='每万份基金单位收益')
    F_INFO_YEARLYROE = Column(Numeric(20, 5), comment='七日年化收益率(%)')
    EST_YEARLYROE = Column(Numeric(20, 5), comment='预估年化收益率(%)')


class CHINAINHOUSEFUNDNAV(Base):
    """中国券商理财净值"""
    __tablename__ = 'CHINAINHOUSEFUNDNAV'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    PRICE_DATE = Column(VARCHAR(8), comment='截止日期')
    F_NAV_UNIT = Column(Numeric(24, 8), comment='单位净值')
    F_NAV_ACCUMULATED = Column(Numeric(24, 8), comment='累计净值')
    F_NAV_DIVACCUMULATED = Column(Numeric(20, 4), comment='累计分红')
    F_NAV_ADJFACTOR = Column(Numeric(20, 6), comment='复权因子')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    F_NAV_ADJUSTED = Column(Numeric(24, 8), comment='复权单位净值')


class CHINAINHOUSEFUNDSECTOR(Base):
    """中国券商理财板块"""
    __tablename__ = 'CHINAINHOUSEFUNDSECTOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SECTOR = Column(VARCHAR(40), comment='所属板块')
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_SECTOREXITDT = Column(VARCHAR(8), comment='截止日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class CHINAINHOUSEFUNDSECTORQL(Base):
    """None"""
    __tablename__ = 'CHINAINHOUSEFUNDSECTORQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    F_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_SECTOR = Column(VARCHAR(40))
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8))
    S_INFO_SECTOREXITDT = Column(VARCHAR(8))
    CUR_SIGN = Column(VARCHAR(10))


class CHINAINHOUSEFUNDSECTORZL(Base):
    """中国券商理财板块(增量)"""
    __tablename__ = 'CHINAINHOUSEFUNDSECTORZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SECTOR = Column(VARCHAR(40), comment='所属板块')
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_SECTOREXITDT = Column(VARCHAR(8), comment='截止日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class CHINAINHOUSEFUNDSHARE(Base):
    """中国券商理财份额"""
    __tablename__ = 'CHINAINHOUSEFUNDSHARE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DATE = Column(VARCHAR(8), comment='变动日期')
    F_UNIT_TOTAL = Column(Numeric(20, 4), comment='基金总份额')
    F_UNIT_TOTALPURCHASE = Column(Numeric(20, 4), comment='总申购份额(含红利再投资)')
    F_UNIT_TOTALREDEMPTION = Column(Numeric(20, 4), comment='总赎回份额')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    F_UNIT_BEGIN = Column(Numeric(20, 4), comment='期初份额')
    F_IS_TOTAL = Column(Numeric(1, 0), comment='是否为合计值')
    F_UNIT_BEGIN_TOTAL = Column(Numeric(20, 4), comment='期初份额(合计)')
    F_UNIT_TOTALPURCHASE_TOTAL = Column(Numeric(20, 4), comment='总申购份额(合计)')
    F_UNIT_TOTALREDEMPTION_TOTAL = Column(Numeric(20, 4), comment='总赎回份额(合计)')
    F_UNIT_END = Column(Numeric(20, 4), comment='期末份额(合计)')


class CHINAOPTIONCALENDAR(Base):
    """中国期权交易日历"""
    __tablename__ = 'CHINAOPTIONCALENDAR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID ')
    TRADE_DAYS = Column(VARCHAR(40), comment='交易日')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class CHINAOPTIONCALENDARZL(Base):
    """中国期权交易日历(增量)"""
    __tablename__ = 'CHINAOPTIONCALENDARZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DAYS = Column(VARCHAR(40), comment='交易日')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class CHINAOPTIONCONTPRO(Base):
    """中国期权标准合约属性"""
    __tablename__ = 'CHINAOPTIONCONTPRO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='标的Wind代码')
    S_INFO_CODE = Column(VARCHAR(20), comment='期权Wind代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='期权名称')
    S_INFO_ENAME = Column(VARCHAR(100), comment='期权英文名称')
    S_INFO_EXNAME = Column(VARCHAR(20), comment='交易所名称')
    S_INFO_TYPE = Column(VARCHAR(20), comment='期权类型')
    S_INFO_EUROAMERICANBERMUDA = Column(VARCHAR(10), comment='行权方式')
    S_INFO_SETTLEMENTMETHOD = Column(VARCHAR(10), comment='交割方式')
    S_INFO_LISTEDDATE = Column(VARCHAR(8), comment='上市日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    S_INFO_STRIKERATIO = Column(Numeric(20, 4), comment='合约乘数')
    S_INFO_CEVALUE = Column(Numeric(20, 4), comment='合约价值')
    S_INFO_COVALUE = Column(VARCHAR(80), comment='立约价值')
    S_INFO_LSMONTH = Column(VARCHAR(200), comment='合约结算月份')
    S_INFO_MINPRICEFLUCT = Column(VARCHAR(40), comment='最小报价单位')
    S_INFO_THOURS = Column(VARCHAR(200), comment='交易时间')
    S_INFO_LASTTRADINGDATE = Column(VARCHAR(200), comment='最后交易日')
    S_INFO_LSDATE = Column(VARCHAR(200), comment='最后结算日')
    S_INFO_LASTSETTLE = Column(VARCHAR(200), comment='最后结算价')
    S_INFO_TRADEFEE = Column(VARCHAR(200), comment='交易费用')
    S_INFO_POSLIMIT = Column(VARCHAR(800), comment='头寸限制')
    S_INFO_MINPOSLIMIT = Column(VARCHAR(800), comment='头寸申报下限')
    S_INFO_OPTIONPRICE = Column(VARCHAR(20), comment='期权金')
    S_INFO_EXERCISINGEND = Column(VARCHAR(80), comment='期权行权日')
    S_INFO_STRIKEPRICE = Column(VARCHAR(800), comment='期权行权价')
    S_INFO_SIMULATION = Column(VARCHAR(1), comment='是否仿真交易')
    S_INFO_QUOTEUNIT = Column(VARCHAR(40), comment='报价货币单位')
    S_INFO_COUNIT = Column(Numeric(20, 4), comment='合约单位')
    S_INFO_COUNITDIMENSION = Column(VARCHAR(40), comment='合约单位量纲')
    S_INFO_ID = Column(VARCHAR(40), comment='期权ID')


class CHINAOPTIONCONTPROZL(Base):
    """中国期权标准合约属性(增量)"""
    __tablename__ = 'CHINAOPTIONCONTPROZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='标的Wind代码')
    S_INFO_CODE = Column(VARCHAR(20), comment='期权Wind代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='期权名称')
    S_INFO_ENAME = Column(VARCHAR(100), comment='期权英文名称')
    S_INFO_EXNAME = Column(VARCHAR(20), comment='交易所名称')
    S_INFO_TYPE = Column(VARCHAR(20), comment='期权类型')
    S_INFO_EUROAMERICANBERMUDA = Column(VARCHAR(10), comment='行权方式')
    S_INFO_SETTLEMENTMETHOD = Column(VARCHAR(10), comment='交割方式')
    S_INFO_LISTEDDATE = Column(VARCHAR(8), comment='上市日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    S_INFO_STRIKERATIO = Column(Numeric(20, 4), comment='合约乘数')
    S_INFO_CEVALUE = Column(Numeric(20, 4), comment='合约价值')
    S_INFO_COVALUE = Column(VARCHAR(80), comment='立约价值')
    S_INFO_LSMONTH = Column(VARCHAR(200), comment='合约结算月份')
    S_INFO_MINPRICEFLUCT = Column(VARCHAR(40), comment='最小报价单位')
    S_INFO_THOURS = Column(VARCHAR(200), comment='交易时间')
    S_INFO_LASTTRADINGDATE = Column(VARCHAR(200), comment='最后交易日')
    S_INFO_LSDATE = Column(VARCHAR(200), comment='最后结算日')
    S_INFO_LASTSETTLE = Column(VARCHAR(200), comment='最后结算价')
    S_INFO_TRADEFEE = Column(VARCHAR(200), comment='交易费用')
    S_INFO_POSLIMIT = Column(VARCHAR(800), comment='头寸限制')
    S_INFO_MINPOSLIMIT = Column(VARCHAR(800), comment='头寸申报下限')
    S_INFO_OPTIONPRICE = Column(VARCHAR(20), comment='期权金')
    S_INFO_EXERCISINGEND = Column(VARCHAR(80), comment='期权行权日')
    S_INFO_STRIKEPRICE = Column(VARCHAR(800), comment='期权行权价')
    S_INFO_SIMULATION = Column(VARCHAR(1), comment='是否仿真交易')
    S_INFO_QUOTEUNIT = Column(VARCHAR(40), comment='报价货币单位')
    S_INFO_COUNIT = Column(Numeric(20, 4), comment='合约单位')
    S_INFO_COUNITDIMENSION = Column(VARCHAR(40), comment='合约单位量纲')
    S_INFO_ID = Column(VARCHAR(40), comment='期权ID')


class CHINAOPTIONDAILYSTATISTICS(Base):
    """中国期权日交易统计"""
    __tablename__ = 'CHINAOPTIONDAILYSTATISTICS'
    __table_args__ = (
        Index('IDX_CHINAOPTIONDAILYSTATISTICS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_CODE = Column(VARCHAR(20), comment='期权Wind代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='期权名称')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    ITEM_CODE = Column(Numeric(9, 0), comment='类型')
    VALUE = Column(Numeric(20, 4), comment='数量')


class CHINAOPTIONDESCRIPTION(Base):
    """中国期权基本资料"""
    __tablename__ = 'CHINAOPTIONDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='月合约交易所编码')
    S_INFO_NAME = Column(VARCHAR(100), comment='月合约全称')
    S_INFO_SCCODE = Column(VARCHAR(50), comment='期权Wind代码')
    S_INFO_CALLPUT = Column(Numeric(9, 0), comment='月合约类别')
    S_INFO_STRIKEPRICE = Column(Numeric(20, 4), comment='行权价格')
    S_INFO_MONTH = Column(VARCHAR(6), comment='交割月份')
    S_INFO_MATURITYDATE = Column(VARCHAR(8), comment='到期日')
    S_INFO_FTDATE = Column(VARCHAR(8), comment='开始交易日')
    S_INFO_LASTTRADINGDATE = Column(VARCHAR(8), comment='最后交易日')
    S_INFO_EXERCISINGEND = Column(VARCHAR(8), comment='最后行权日')
    S_INFO_LDDATE = Column(VARCHAR(8), comment='最后交割日')
    S_INFO_LPRICE = Column(Numeric(20, 4), comment='挂牌基准价')
    S_INFO_TRADE = Column(VARCHAR(1), comment='是否交易')
    S_INFO_EXCODE = Column(VARCHAR(20), comment='月合约交易所代码')
    S_INFO_EXNAME = Column(VARCHAR(100), comment='月合约交易所简称')
    S_INFO_COUNIT = Column(Numeric(20, 4), comment='合约单位')


class CHINAOPTIONDESCRIPTIONQL(Base):
    """None"""
    __tablename__ = 'CHINAOPTIONDESCRIPTIONQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_CODE = Column(VARCHAR(40))
    S_INFO_NAME = Column(VARCHAR(100))
    S_INFO_SCCODE = Column(VARCHAR(50))
    S_INFO_CALLPUT = Column(Numeric(9, 0))
    S_INFO_STRIKEPRICE = Column(Numeric(20, 4))
    S_INFO_MONTH = Column(VARCHAR(6))
    S_INFO_MATURITYDATE = Column(VARCHAR(8))
    S_INFO_FTDATE = Column(VARCHAR(8))
    S_INFO_LASTTRADINGDATE = Column(VARCHAR(8))
    S_INFO_EXERCISINGEND = Column(VARCHAR(8))
    S_INFO_LDDATE = Column(VARCHAR(8))
    S_INFO_LPRICE = Column(Numeric(20, 4))
    S_INFO_TRADE = Column(VARCHAR(1))
    S_INFO_EXCODE = Column(VARCHAR(20))
    S_INFO_EXNAME = Column(VARCHAR(100))
    S_INFO_COUNIT = Column(Numeric(20, 4))


class CHINAOPTIONDESCRIPTIONZL(Base):
    """中国期权基本资料(增量)"""
    __tablename__ = 'CHINAOPTIONDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='月合约交易所编码')
    S_INFO_NAME = Column(VARCHAR(100), comment='月合约全称')
    S_INFO_SCCODE = Column(VARCHAR(50), comment='期权Wind代码')
    S_INFO_CALLPUT = Column(Numeric(9, 0), comment='月合约类别')
    S_INFO_STRIKEPRICE = Column(Numeric(20, 4), comment='行权价格')
    S_INFO_MONTH = Column(VARCHAR(6), comment='交割月份')
    S_INFO_MATURITYDATE = Column(VARCHAR(8), comment='到期日')
    S_INFO_FTDATE = Column(VARCHAR(8), comment='开始交易日')
    S_INFO_LASTTRADINGDATE = Column(VARCHAR(8), comment='最后交易日')
    S_INFO_EXERCISINGEND = Column(VARCHAR(8), comment='最后行权日')
    S_INFO_LDDATE = Column(VARCHAR(8), comment='最后交割日')
    S_INFO_LPRICE = Column(Numeric(20, 4), comment='挂牌基准价')
    S_INFO_TRADE = Column(VARCHAR(1), comment='是否交易')
    S_INFO_EXCODE = Column(VARCHAR(20), comment='月合约交易所代码')
    S_INFO_EXNAME = Column(VARCHAR(100), comment='月合约交易所简称')
    S_INFO_COUNIT = Column(Numeric(20, 4), comment='合约单位')


class CHINAOPTIONEODPRICES(Base):
    """中国期权日行情"""
    __tablename__ = 'CHINAOPTIONEODPRICES'
    __table_args__ = (
        Index('IDX_S_INFO_WINDCODE_TRADE_DT', 'S_INFO_WINDCODE', 'TRADE_DT'),
        Index('IDX_CHINAOPTIONEODPRICES_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID ')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(元)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(元)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(元)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(元)')
    S_DQ_SETTLE = Column(Numeric(20, 4), comment='结算价(元)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(万元)')
    S_DQ_OI = Column(Numeric(20, 4), comment='持仓量(手)')
    S_DQ_OICHANGE = Column(Numeric(20, 4), comment='持仓量变化(手)')
    S_DQ_PRESETTLE = Column(Numeric(20, 4), comment='前结算价')
    S_DQ_CHANGE1 = Column(Numeric(20, 4), comment='涨跌1')
    S_DQ_CHANGE2 = Column(Numeric(20, 4), comment='涨跌2')


class CHINAOPTIONINDEXEODPRICES(Base):
    """中国期权指数日行情"""
    __tablename__ = 'CHINAOPTIONINDEXEODPRICES'
    __table_args__ = (
        Index('IDX_CHINAOPTIONINDEXEODPRICES_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='指数简称')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='最新价')
    S_DQ_CHANGE = Column(Numeric(20, 4), comment='涨跌(点)')
    S_DQ_PCTCHANGE = Column(Numeric(20, 4), comment='涨跌幅(%)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class CHINAOPTIONMEMBERSTATISTICS(Base):
    """中国期权会员交易统计"""
    __tablename__ = 'CHINAOPTIONMEMBERSTATISTICS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_CODE = Column(VARCHAR(20), comment='期权Wind代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='期权名称')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    ITEM_CODE = Column(Numeric(9, 0), comment='类型')
    VALUE = Column(Numeric(20, 4), comment='数量')
    RANK = Column(Numeric(5, 0), comment='名次')
    S_INFO_MEMBERNAME = Column(VARCHAR(40), comment='会员简称')


class CHINAOPTIONPREVIOUSNAME(Base):
    """中国期权曾用名"""
    __tablename__ = 'CHINAOPTIONPREVIOUSNAME'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截至日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券简称')
    CHANGEREASON = Column(Numeric(9, 0), comment='变动原因代码')


class CHINAOPTIONVALUATION(Base):
    """中国期权衍生指标"""
    __tablename__ = 'CHINAOPTIONVALUATION'
    __table_args__ = (
        Index('IDX_CHINAOPTIONVALUATION_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    W_ANAL_UNDERLYINGIMPLIEDVOL = Column(Numeric(24, 8), comment='隐含波动率(%)')
    W_ANAL_DELTA = Column(Numeric(24, 8), comment='Delta')
    W_ANAL_THETA = Column(Numeric(24, 8), comment='Theta')
    W_ANAL_GAMMA = Column(Numeric(24, 8), comment='Gamma')
    W_ANAL_VEGA = Column(Numeric(24, 8), comment='Vega')
    W_ANAL_RHO = Column(Numeric(24, 8), comment='Rho')
    SURGED_LIMIT = Column(Numeric(24, 8), comment='涨停价格')
    DECLINE_LIMIT = Column(Numeric(24, 8), comment='跌停价格')


class CINDEXFUTURESEODPRICES(Base):
    """中国股指期货日行情"""
    __tablename__ = 'CINDEXFUTURESEODPRICES'
    __table_args__ = (
        Index('IDX_CINDEXFUTURESEODPRICES_TRADE_DT', 'TRADE_DT'),
        Index('NonClusteredIndex-20200806-190651', 'S_INFO_WINDCODE', 'TRADE_DT'),)
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
    FS_INFO_TYPE = Column(VARCHAR(10), comment='合约类型')


class CINDEXFUTURESPOSITIONS(Base):
    """中国股指期货成交及持仓"""
    __tablename__ = 'CINDEXFUTURESPOSITIONS'
    __table_args__ = (
        Index('IDX_CINDEXFUTURESPOSITIONS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    FS_INFO_MEMBERNAME = Column(VARCHAR(40), comment='会员简称')
    FS_INFO_TYPE = Column(Numeric(1, 0), comment='类型')
    FS_INFO_POSITIONSNUM = Column(Numeric(20, 4), comment='持仓数量')
    FS_INFO_RANK = Column(Numeric(5, 0), comment='名次')
    S_OI_POSITIONSNUMC = Column(Numeric(20, 4), comment='比上交易日增减')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='会员ID')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class CNUSBONDISSUER(Base):
    """中资美元债发行主体"""
    __tablename__ = 'CNUSBONDISSUER'
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


class CNUSDBONDDESC(Base):
    """中资美元债基本资料"""
    __tablename__ = 'CNUSDBONDDESC'
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
    B_INFO_GUARINTRODUCTION = Column(VARCHAR(200), comment='担保简介')
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


class CODEANDSNAME(Base):
    """业务代码及简称"""
    __tablename__ = 'CODEANDSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券ID')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务类型代码')
    S_CODE = Column(VARCHAR(40), comment='业务代码')
    S_SNAME = Column(VARCHAR(100), comment='业务简称')
    IS_COMMON = Column(Numeric(1, 0), comment='是否通用代码')
    MEMO = Column(VARCHAR(800), comment='备注')


class COMPANYBUSINESSDATA(Base):
    """None"""
    __tablename__ = 'COMPANYBUSINESSDATA'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    COMP_NAME = Column(VARCHAR(300), comment='公司名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    ITEM_NAME = Column(VARCHAR(80), comment='业务(产品)名称')
    ITEM_TYPE = Column(VARCHAR(20), comment='数据类型')
    NUM_TYPE = Column(VARCHAR(10), comment='数量类型')
    NUM = Column(Numeric(20, 4), comment='数量')
    UNIT = Column(VARCHAR(20), comment='单位')
    NUM_LEVEL = Column(VARCHAR(40), comment='数量级别')
    NUM_CALCULATE = Column(Numeric(20, 4), comment='换算后数量')
    FREQUENCY = Column(Numeric(9, 0), comment='频率代码')
    YOY = Column(Numeric(20, 4), comment='同比')
    MOM = Column(Numeric(20, 4), comment='环比')
    IS_CALCULATE = Column(Numeric(1, 0), comment='是否计算同环比')
    SOURCE = Column(VARCHAR(40), comment='数据来源')


class COMPANYNEWS(Base):
    """公司新闻"""
    __tablename__ = 'COMPANYNEWS'
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


class COMPANYPREVIOUSNAME(Base):
    """中国A股公司曾用名"""
    __tablename__ = 'COMPANYPREVIOUSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')
    COMP_NAME_ENG = Column(VARCHAR(200), comment='公司英文名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    CHANGE_REASON = Column(VARCHAR(100), comment='更名原因')


class COMPANYPREVIOUSNAMES(Base):
    """公司曾用名"""
    __tablename__ = 'COMPANYPREVIOUSNAMES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')
    COMP_NAME_ENG = Column(VARCHAR(200), comment='公司英文名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    CHANGE_REASON = Column(VARCHAR(500), comment='更名原因')


class COMPINTRODUCTION(Base):
    """公司简介"""
    __tablename__ = 'COMPINTRODUCTION'
    __table_args__ = (
        Index('IDX_COMP_ID', 'COMP_ID'),
        Index('IDX_COMP_NAME', 'COMP_NAME'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(40), comment='公司ID')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')
    COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')
    COMP_NAME_ENG = Column(VARCHAR(100), comment='英文名称')
    COMP_SNAMEENG = Column(VARCHAR(100), comment='英文名称缩写')
    PROVINCE = Column(VARCHAR(20), comment='省份')
    CITY = Column(VARCHAR(50), comment='城市')
    ADDRESS = Column(VARCHAR(200), comment='注册地址')
    OFFICE = Column(VARCHAR(400), comment='办公地址')
    ZIPCODE = Column(VARCHAR(10), comment='邮编')
    PHONE = Column(VARCHAR(80), comment='电话')
    FAX = Column(VARCHAR(50), comment='传真')
    EMAIL = Column(VARCHAR(200), comment='电子邮件')
    WEBSITE = Column(VARCHAR(200), comment='公司网址')
    REGISTERNUMBER = Column(VARCHAR(20), comment='统一社会信用代码')
    CHAIRMAN = Column(VARCHAR(100), comment='法人代表')
    PRESIDENT = Column(VARCHAR(100), comment='总经理')
    DISCLOSER = Column(VARCHAR(500), comment='信息披露人')
    REGCAPITAL = Column(Numeric(20, 4), comment='注册资本')
    CURRENCYCODE = Column(VARCHAR(10), comment='货币代码')
    FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    ENDDATE = Column(VARCHAR(8), comment='公司终止日期')
    BRIEFING = Column(VARCHAR(2000), comment='公司简介')
    COMP_TYPE = Column(VARCHAR(100), comment='公司类型')
    COMP_PROPERTY = Column(VARCHAR(100), comment='企业性质')
    COUNTRY = Column(VARCHAR(20), comment='国籍')
    BUSINESSSCOPE = Column(TEXT(2147483647), comment='经营范围')
    COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    SOCIAL_CREDIT_CODE = Column(VARCHAR(30), comment='统一社会信用编码(废弃)')
    S_INFO_ORG_CODE = Column(VARCHAR(30), comment='组织机构代码')
    IS_LISTED = Column(Numeric(1, 0), comment='是否上市公司')
    S_INFO_COMPTYPE = Column(VARCHAR(10), comment='公司类型')


class COMPORGANIZATIONCODE(Base):
    """公司机构代码表"""
    __tablename__ = 'COMPORGANIZATIONCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(40), comment='公司ID')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务类型代码')
    S_CODE = Column(VARCHAR(40), comment='业务代码')
    S_SNAME = Column(VARCHAR(100), comment='业务名称')
    IS_COMMON = Column(Numeric(1, 0), comment='是否通用代码')
    MEMO = Column(VARCHAR(800), comment='备注')


class COPTIONCONTPROCHANGE(Base):
    """中国期权标准合约属性变更"""
    __tablename__ = 'COPTIONCONTPROCHANGE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    CONTRACT_ID = Column(VARCHAR(40), comment='合约代码')
    ITEM = Column(VARCHAR(50), comment='变更字段名称')
    CHANGE_DT = Column(VARCHAR(8), comment='变更日期')
    S_INFO_OLD = Column(VARCHAR(1000), comment='变更前')
    S_INFO_NEW = Column(VARCHAR(1000), comment='变更后')


class COPTIONDESCRIPTIONCHANGE(Base):
    """中国期权月合约属性变动表"""
    __tablename__ = 'COPTIONDESCRIPTIONCHANGE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='期权月合约代码')
    S_CHANGE_DATE = Column(VARCHAR(8), comment='调整日期')
    S_INFO_CODE_OLD = Column(VARCHAR(20), comment='原交易代码')
    S_INFO_NAME_OLD = Column(VARCHAR(40), comment='原合约简称')
    S_EXERCISE_PRICE_OLD = Column(Numeric(20, 4), comment='原行权价（元）')
    S_UNIT_OLD = Column(Numeric(20, 4), comment='原合约单位（股）')
    S_INFO_CODE_NEW = Column(VARCHAR(20), comment='新交易代码')
    S_INFO_NAME_NEW = Column(VARCHAR(40), comment='新合约简称')
    S_EXERCISE_PRICE_NEW = Column(Numeric(20, 4), comment='新行权价（元）')
    S_UNIT_NEW = Column(Numeric(20, 4), comment='新合约单位（股）')
    S_CHANGE_REASON = Column(VARCHAR(300), comment='调整原因')


class COPTIONEMBEDDEDBONDVALUATION(Base):
    """中国含权债行权衍生指标"""
    __tablename__ = 'COPTIONEMBEDDEDBONDVALUATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    PRICE_TYPE_CODE = Column(Numeric(9, 0), comment='价格类型代码')
    PRICE_TYPE = Column(VARCHAR(20), comment='价格类型')
    B_ANAL_NXOPTIONDATE = Column(VARCHAR(8), comment='最近行权日')
    B_ANAL_TERMIFEXERCISE = Column(Numeric(22, 4), comment='行权剩余期限')
    B_ANAL_YTM_IFEXE = Column(Numeric(24, 8), comment='行权收益率')
    B_ANAL_DURATIONIFEXERCISE = Column(Numeric(24, 8), comment='行权久期')
    B_ANAL_MODIDURATION_IFEXE = Column(Numeric(24, 8), comment='行权修正久期')
    B_ANAL_CONVEXITY_IFEXE = Column(Numeric(24, 8), comment='行权凸性')
    B_ANAL_BASEVALUE_IFEXE = Column(Numeric(24, 8), comment='行权基点价值')
    B_ANAL_BDURATION_IFEXE = Column(Numeric(24, 8), comment='行权基准久期')
    B_ANAL_BCONVEXITY_IFEXE = Column(Numeric(24, 8), comment='行权基准凸性')
    B_ANAL_SDURATION_IFEXE = Column(Numeric(24, 8), comment='行权利差久期')
    B_ANAL_SCONVEXITY_IFEXE = Column(Numeric(24, 8), comment='行权利差凸性')


class COPTIONIMPLIEDVOLATILITY(Base):
    """中国期权隐含波动率"""
    __tablename__ = 'COPTIONIMPLIEDVOLATILITY'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    CONTRACT_ID = Column(VARCHAR(10), comment='合约ID')
    S_INFO_SCCODE = Column(VARCHAR(20), comment='标准合约代码')
    VOLATILITY_TYPE = Column(Numeric(9, 0), comment='波动率类型')
    TERM = Column(VARCHAR(20), comment='期限')
    W_ANAL_UNDERLYINGIMPLIEDVOL = Column(Numeric(20, 4), comment='隐含波动率')
    APPLY_MODEL = Column(VARCHAR(100), comment='模型')
    SOURCE1 = Column(VARCHAR(100), comment='来源')
    TRADE_DT = Column(VARCHAR(8), comment='日期')


class COUNTRYANDAREACODE(Base):
    """国家及地区代码表"""
    __tablename__ = 'COUNTRYANDAREACODE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    IS_VALID = Column(Numeric(5, 0), comment='是否有效')
    RELEASE_DATE = Column(DateTime, comment='发布日期')
    COUNTRY_CODE_3 = Column(VARCHAR(10), comment='国家代码(3位)')
    CONTINENT = Column(VARCHAR(20), comment='所属洲')
    COUNTRY_CODE_2 = Column(VARCHAR(10), comment='国家代码(2位)')
    NAME = Column(VARCHAR(40), comment='名称')


class COUNTRYANDAREACODEZL(Base):
    """None"""
    __tablename__ = 'COUNTRYANDAREACODEZL'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    IS_VALID = Column(Numeric(5, 0), comment='是否有效')
    RELEASE_DATE = Column(DateTime, comment='发布日期')
    COUNTRY_CODE_3 = Column(VARCHAR(10), comment='国家及地区代码(3位)')
    CONTINENT = Column(VARCHAR(20), comment='所属洲')
    COUNTRY_CODE_2 = Column(VARCHAR(10), comment='国家及地区代码(2位)')
    NAME1 = Column(VARCHAR(40), comment='国家及地区名称')


class CPFUNDDESCRIPTION(Base):
    """中国保本基金基本资料"""
    __tablename__ = 'CPFUNDDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CP_PERIOD = Column(Numeric(20, 4), comment='保本周期(年)')
    START_DT = Column(VARCHAR(8), comment='保本周期起始日期')
    END_DT = Column(VARCHAR(8), comment='保本周期终止日期')
    GUARANT_FEE = Column(Numeric(20, 4), comment='保证费率(%)')
    TRIGGER_YIELD = Column(Numeric(20, 4), comment='触发收益率(%)')
    TRIGGER_INFO = Column(VARCHAR(2000), comment='触发机制说明')
    GUARANTOR = Column(VARCHAR(200), comment='保证人名称')
    GUARANTOR_INFO = Column(VARCHAR(800), comment='保证人简介')


class CPSAGENCY(Base):
    """中国优先股发行中介机构"""
    __tablename__ = 'CPSAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_AGENCY_NAME = Column(VARCHAR(200), comment='机构名称')
    S_AGENCY_NAMEID = Column(VARCHAR(200), comment='中介机构公司ID')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CPSCAPITALIZATION(Base):
    """中国优先股股本"""
    __tablename__ = 'CPSCAPITALIZATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日')
    ANN_DT = Column(VARCHAR(8), comment='公告日')
    S_ISSUEAMOUNT = Column(Numeric(20, 4), comment='发行股份数')


class CPSDESCRIPTION(Base):
    """中国优先股基本资料"""
    __tablename__ = 'CPSDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    DIV_FACERATE = Column(Numeric(20, 4), comment='票面股息率')
    DIV_RATETYPE = Column(Numeric(9, 0), comment='股息率类型代码')
    DIV_CONTENT = Column(VARCHAR(800), comment='股息率说明')
    REDEMP_CONDITION = Column(VARCHAR(500), comment='赎回条件说明')
    REDEMP_PRICE = Column(VARCHAR(400), comment='赎回价格说明')
    CONV_PRICE = Column(Numeric(20, 4), comment='转股价 ')
    CONV_CONDITION = Column(VARCHAR(400), comment='转股触发条件 ')
    CONV_PRICEBASIS = Column(VARCHAR(400), comment='转股价设定依据 ')
    TYPE_CODE = Column(VARCHAR(30), comment='属性代码 ')
    S_INFO_NAME = Column(VARCHAR(40), comment='优先股名称 ')


class CPSDESCRIPTIONZL(Base):
    """中国优先股基本资料(增量)"""
    __tablename__ = 'CPSDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    DIV_FACERATE = Column(Numeric(20, 4), comment='票面股息率')
    DIV_RATETYPE = Column(Numeric(9, 0), comment='股息率类型代码')
    DIV_CONTENT = Column(VARCHAR(800), comment='股息率说明')
    REDEMP_CONDITION = Column(VARCHAR(500), comment='赎回条件说明')
    REDEMP_PRICE = Column(VARCHAR(400), comment='赎回价格说明')
    CONV_PRICE = Column(Numeric(20, 4), comment='转股价')
    CONV_CONDITION = Column(VARCHAR(400), comment='转股触发条件')
    CONV_PRICEBASIS = Column(VARCHAR(400), comment='转股价设定依据')
    TYPE_CODE = Column(VARCHAR(30), comment='属性代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='优先股名称')


class CPSDIVIDEND(Base):
    """中国优先股分红"""
    __tablename__ = 'CPSDIVIDEND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DIV_PROGRESS = Column(VARCHAR(10), comment='方案进度')
    STK_DVD_PER_SH = Column(Numeric(24, 8), comment='转增比例分子')
    CASH_DVD_PER_SH_PRE_TAX = Column(Numeric(24, 8), comment='派息比例分子(税前)')
    CASH_DVD_PER_SH_AFTER_TAX = Column(Numeric(24, 8), comment='派息比例分子(税后)')
    EQY_RECORD_DT = Column(VARCHAR(8), comment='股权登记日/B股最后交易日')
    EX_DT = Column(VARCHAR(8), comment='除权除息日')
    DVD_PAYOUT_DT = Column(VARCHAR(8), comment='派息日')
    LISTING_DT_OF_DVD_SHR = Column(VARCHAR(8), comment='红股上市日期')
    S_DIV_PRELANDATE = Column(VARCHAR(8), comment='预案公告日')
    S_DIV_SMTGDATE = Column(VARCHAR(8), comment='股东大会公告日')
    DVD_ANN_DT = Column(VARCHAR(8), comment='分红实施公告日')
    S_DIV_BASEDATE = Column(VARCHAR(8), comment='股本基准日期')
    S_DIV_BASESHARE = Column(Numeric(20, 4), comment='基准股本(万股)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    IS_CHANGED = Column(Numeric(5, 0), comment='方案曾经变更')
    REPORT_PERIOD = Column(VARCHAR(8), comment='分红年度')
    S_DIV_CHANGE = Column(VARCHAR(500), comment='方案变更说明')
    S_DIV_BONUSRATE = Column(Numeric(24, 8), comment='每股送股比例')
    S_DIV_CONVERSEDRATE = Column(Numeric(24, 8), comment='每股转增比例')
    MEMO = Column(VARCHAR(200), comment='[内部]备注')
    S_DIV_PREANNDT = Column(VARCHAR(8), comment='预案预披露公告日')
    S_DIV_OBJECT = Column(VARCHAR(100), comment='分红对象')
    BONUSRATE_DENOMINATOR = Column(Numeric(20, 4), comment='送股比例分母')
    CASH_DVD_PER_DENOMINATOR = Column(Numeric(20, 4), comment='派息比例分母')


class CPSEODPRICES(Base):
    """中国优先股日行情"""
    __tablename__ = 'CPSEODPRICES'
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
    S_DQ_ADJPRECLOSE = Column(Numeric(20, 4), comment='复权昨收盘价(元)')
    S_DQ_ADJOPEN = Column(Numeric(20, 4), comment='复权开盘价(元)')
    S_DQ_ADJHIGH = Column(Numeric(20, 4), comment='复权最高价(元)')
    S_DQ_ADJLOW = Column(Numeric(20, 4), comment='复权最低价(元)')
    S_DQ_ADJCLOSE = Column(Numeric(20, 4), comment='复权收盘价(元)')
    S_DQ_ADJFACTOR = Column(Numeric(20, 6), comment='复权因子')
    S_DQ_AVGPRICE = Column(Numeric(20, 4), comment='均价(VWAP)')
    S_DQ_TRADESTATUS = Column(VARCHAR(10), comment='交易状态')
    S_DQ_TRADESTATUSCODE = Column(Numeric(5, 0), comment='交易状态代码')


class CPSISSUERRATING(Base):
    """中国优先股主体信用评级"""
    __tablename__ = 'CPSISSUERRATING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司中文名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_RATE_STYLE = Column(VARCHAR(100), comment='评级类型')
    S_INFO_CREDITRATING = Column(VARCHAR(40), comment='信用评级')
    S_RATE_RATINGOUTLOOK = Column(Numeric(9, 0), comment='评级展望')
    S_INFO_CREDITRATINGAGENCY = Column(VARCHAR(10), comment='评级机构代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    S_INFO_CREDITRATINGEXPLAIN = Column(VARCHAR(1000), comment='信用评级说明')
    S_INFO_PRECREDITRATING = Column(VARCHAR(40), comment='前次信用评级')
    S_CREDITRATING_CHANGE = Column(VARCHAR(10), comment='评级变动方向')
    S_INFO_ISSUERRATETYPE = Column(Numeric(9, 0), comment='评级对象类型代码')


class CPSPLACEMENTDETAILS(Base):
    """中国优先股发行获配明细"""
    __tablename__ = 'CPSPLACEMENTDETAILS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='[内部]获配公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='法人投资者ID')
    TYPEOFINVESTOR = Column(VARCHAR(20), comment='法人投资者类型')
    PLACEMENT = Column(Numeric(20, 4), comment='获配数量(万股/万张)')
    TRADE_DT = Column(VARCHAR(8), comment='配售截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class CPSRATING(Base):
    """中国优先股信用评级"""
    __tablename__ = 'CPSRATING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_RATE_STYLE = Column(VARCHAR(100), comment='评级类型')
    S_INFO_CREDITRATING = Column(VARCHAR(40), comment='信用评级')
    S_INFO_CREDITRATINGAGENCY = Column(VARCHAR(10), comment='评级机构代码')
    S_INFO_CREDITRATINGEXPLAIN = Column(VARCHAR(1000), comment='信用评级说明')
    S_INFO_PRECREDITRATING = Column(VARCHAR(40), comment='前次信用评级')
    S_CREDITRATING_CHANGE = Column(VARCHAR(10), comment='评级变动方向')


class CPSSEO(Base):
    """中国优先股发行"""
    __tablename__ = 'CPSSEO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_FELLOW_ISSUETYPE = Column(Numeric(9, 0), comment='发行方式代码')
    S_FELLOW_OFFERINGOBJECT = Column(VARCHAR(200), comment='发行对象')
    S_FELLOW_PRICE = Column(Numeric(20, 4), comment='发行价格')
    S_FELLOW_AMOUNT = Column(Numeric(20, 4), comment='发行数量(万股)')
    S_FELLOW_ESTICOLLECTION = Column(Numeric(20, 4), comment='预计募集资金(元)')
    S_FELLOW_COLLECTION = Column(Numeric(20, 4), comment='募集资金合计')
    S_FELLOW_COST = Column(Numeric(20, 4), comment='发行费用')
    S_FELLOW_PROGRESS = Column(Numeric(5, 0), comment='方案进度')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_FELLOW_YEAR = Column(VARCHAR(8), comment='增发年度')
    S_FELLOW_PREPLANDATE = Column(VARCHAR(8), comment='预案公告日')
    S_FELLOW_SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    S_FELLOW_PASSDATE = Column(VARCHAR(8), comment='发审委通过公告日')
    S_FELLOW_APPROVEDDATE = Column(VARCHAR(10), comment='证监会核准公告日')
    S_FELLOW_OFFERINGDATE = Column(VARCHAR(8), comment='增发公告日')
    S_FELLOW_SUBINVITATIONDT = Column(VARCHAR(8), comment='认购邀请书日')
    S_FELLOW_DATE = Column(VARCHAR(8), comment='定增发行日期')
    S_FELLOW_OTCDATE = Column(VARCHAR(8), comment='网下发行日期')


class CRMWDESCRIPTION(Base):
    """中国债券信用风险缓释工具基本资料"""
    __tablename__ = 'CRMWDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    B_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    B_CREATE_FULLNAME = Column(VARCHAR(100), comment='凭证全称')
    B_CREATE_NAME = Column(VARCHAR(80), comment='创设机构名称')
    B_CREATE_NAMEID = Column(VARCHAR(10), comment='创设机构ID')
    FILENUM = Column(VARCHAR(80), comment='创设批准文件编号')
    B_CREATE_ANN_DATE = Column(VARCHAR(10), comment='创设公告日')
    B_CREATE_OBJECT = Column(Numeric(9, 0), comment='发行对象代码')
    B_CREATE_PRICE = Column(Numeric(20, 4), comment='凭证创设价格')
    B_CREATE_AMOUNTPLAN = Column(Numeric(20, 6), comment='计划创设总额')
    B_CREATE_AMOUNTACT = Column(Numeric(20, 6), comment='实际创设总额')
    B_CREATE_FIRSTISSUE = Column(VARCHAR(8), comment='簿记建档日')
    B_REGISTRATION_DATE = Column(VARCHAR(8), comment='凭证登记日')
    B_CREATE_START_DAY = Column(VARCHAR(8), comment='凭证起始日')
    B_CREATE_END_DAY = Column(VARCHAR(8), comment='凭证到期日')
    B_CREATE_TERM_DAY = Column(Numeric(20, 4), comment='凭证期限')
    B_CREATE_PAYMENT_CODE = Column(Numeric(9, 0), comment='付费方式代码')
    B_CGROSS_PRINCIPAL_AMOUNT = Column(Numeric(20, 6), comment='名义本金总额')
    IS_GUARANTEE = Column(Numeric(1, 0), comment='是否担保')
    B_CGROSS_SETTLEMENT_CODE = Column(Numeric(9, 0), comment='结算方式代码')
    B_VOUCHER_CODE = Column(Numeric(9, 0), comment='凭证类别代码')
    B_SECURITY_CODE = Column(Numeric(9, 0), comment='履约保障机制代码')
    B_UNIT_NOMINAL_CAPITAL = Column(Numeric(20, 4), comment='单位名义本金')
    B_CREATE_CANCELLATION_DAY = Column(VARCHAR(8), comment='凭证注销日')
    B_INFO_COMPCODE = Column(VARCHAR(10), comment='参考实体公司id')
    B_CREATE_DEBT_TYPE = Column(VARCHAR(200), comment='债务种类')
    B_CREATE_DEBT_FEATURES = Column(VARCHAR(200), comment='债务特征')
    B_INFO_CODE = Column(VARCHAR(100), comment='可交付债务证券id')


class CSRCNEWS(Base):
    """None"""
    __tablename__ = 'CSRCNEWS'
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


class CTREASURYCASHDEPOSITCOMBANK(Base):
    """商业银行定期存款利率(国库现金管理)"""
    __tablename__ = 'CTREASURYCASHDEPOSITCOMBANK'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TENDER_DATE = Column(VARCHAR(8), comment='招标日')
    TENDER_ANN_DT = Column(VARCHAR(8), comment='招标公告日')
    TENDER_TIME = Column(VARCHAR(40), comment='招标时间')
    TENDER_RESULT_ANN_DT = Column(VARCHAR(8), comment='招标结果公告日')
    CARRY_DATE = Column(VARCHAR(8), comment='起息日')
    MATURITY_DATE = Column(VARCHAR(8), comment='到期日')
    TERM_DAY = Column(Numeric(20, 4), comment='期限(天)')
    TENDER_TYPE = Column(VARCHAR(40), comment='招标方式')
    TENDER_AMOUNT = Column(Numeric(20, 4), comment='招标总量(亿元)')
    BID_AMOUNT = Column(Numeric(20, 4), comment='中标总量(亿元)')
    BID_RATE = Column(Numeric(20, 6), comment='中标利率(%)')
    TERM_WORD = Column(VARCHAR(40), comment='期限(文字)')
    TENDER_NAME = Column(VARCHAR(100), comment='名称')


class CURRENCYCODE(Base):
    """货币代码表"""
    __tablename__ = 'CURRENCYCODE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    CRNCY_NAME = Column(VARCHAR(40), comment='货币名称')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    MAIN_CURRENCY_CODE = Column(VARCHAR(10), comment='主币货币代码')
    PIP_VALUE = Column(Numeric(20, 4), comment='pip value')
    MAIN_CURRENCY_RATIO = Column(Numeric(20, 0), comment='主辅币比例')
    LATEST_LOGO = Column(Numeric(1, 0), comment='最新标志')
    MEMO = Column(VARCHAR(100), comment='备注')


class CWARRANTDESCRIPTION(Base):
    """中国权证基本资料"""
    __tablename__ = 'CWARRANTDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    WINDCODE = Column(VARCHAR(40), comment='权证证券id')
    UNDERLYINGWINDCODE = Column(VARCHAR(10), comment='标的证券id')
    CALLPUT = Column(VARCHAR(40), comment='行权方式')
    EQUITYCOVERED = Column(VARCHAR(40), comment='权证类型(按买卖方向分类)')
    ISSUER = Column(VARCHAR(200), comment='发行人')
    ISSUER_TYPE = Column(VARCHAR(200), comment='发行方式')
    ISSUER_IPONUM = Column(Numeric(20, 4), comment='发行数量(万份)')
    ISSUERNUM = Column(Numeric(20, 4), comment='上市数量(万份)')
    INISTRIKEPRICE = Column(Numeric(20, 4), comment='初始行权价')
    INISTRIKERATIO = Column(Numeric(24, 8), comment='初始行权比例')
    DURATION_DAYS = Column(Numeric(20, 4), comment='存续期限(天)')
    DURATION_STARTDATE = Column(VARCHAR(8), comment='存续起始日期')
    DURATION_ENDDATE = Column(VARCHAR(8), comment='存续截止日期')
    ISSUEDATE = Column(VARCHAR(8), comment='发行日期')
    ISSUEPRICE = Column(Numeric(20, 4), comment='发行价格')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    LISTEDDATE = Column(VARCHAR(8), comment='上市日期')
    ANNISSUEDATE = Column(VARCHAR(8), comment='发行公告日')
    ANNLISTEDDATE = Column(VARCHAR(8), comment='上市公告日')
    SETTLEMENTMETHOD = Column(VARCHAR(40), comment='结算方式')
    EXERCISINGEND = Column(VARCHAR(8), comment='最后行权日')
    EXERCODE = Column(VARCHAR(20), comment='行权代码')
    EXERNAME = Column(VARCHAR(40), comment='行权简称')
    ISRATIOADJUST = Column(Numeric(5, 0), comment='行权价及行权比例是否调整')
    ADJUSTRATIO = Column(VARCHAR(800), comment='行权价及比例调整公式')
    PROGRESS = Column(VARCHAR(8), comment='方案进度')
    PRELAN_DATE = Column(VARCHAR(8), comment='预案公告日')
    SMTG_DATE = Column(VARCHAR(8), comment='股东大会公告日')
    TYPEBYISSUER = Column(VARCHAR(40), comment='权证类型(按发行人分类)')
    OLD_SHRHLDR_RATIO = Column(Numeric(20, 4), comment='原股东配售比例')
    PLACINGRECORDDATE = Column(VARCHAR(8), comment='权证配售股权登记日')
    OFFERINGOBJECT = Column(VARCHAR(40), comment='发行对象')
    GUARTYPE = Column(VARCHAR(40), comment='担保方式')
    EXERCISESTARTDATE = Column(VARCHAR(8), comment='行权起始日期')
    REF_PRICE = Column(Numeric(20, 4), comment='上市首日参考价')
    ISCALLCLAUSE = Column(Numeric(5, 0), comment='是否有约购条款')
    CALLPRICE = Column(Numeric(20, 4), comment='回购价格')
    CALLDESCRIPTION = Column(VARCHAR(500), comment='回购说明')
    GUARANTOR = Column(VARCHAR(300), comment='担保人')
    GUARDESCRIPTION = Column(VARCHAR(400), comment='担保说明')
    WARRANTSOURCE = Column(VARCHAR(40), comment='权证来源')
    WARRANT_NUM_PER_BOND = Column(Numeric(20, 4), comment='每张债券附认股权证数量')
    BONDWINDCODE = Column(VARCHAR(10), comment='债券交易代码(证券id)')
    LASTTRADEDATE = Column(VARCHAR(8), comment='最后交易日')
    EXPIREDATE = Column(VARCHAR(8), comment='停止交易日')
    RECORDDATE_PUTWARRANT = Column(VARCHAR(8), comment='认沽权利股权登记日')
    S_INFO_LISTBOARD = Column(VARCHAR(10), comment='上市板')


class CWARRANTDESCRIPTIONZL(Base):
    """中国权证基本资料(增量)"""
    __tablename__ = 'CWARRANTDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    WINDCODE = Column(VARCHAR(40), comment='权证证券id')
    UNDERLYINGWINDCODE = Column(VARCHAR(10), comment='标的证券id')
    CALLPUT = Column(VARCHAR(40), comment='行权方式')
    EQUITYCOVERED = Column(VARCHAR(40), comment='权证类型(按买卖方向分类)')
    ISSUER = Column(VARCHAR(200), comment='发行人')
    ISSUER_TYPE = Column(VARCHAR(200), comment='发行方式')
    ISSUER_IPONUM = Column(Numeric(20, 4), comment='发行数量(万份)')
    ISSUERNUM = Column(Numeric(20, 4), comment='上市数量(万份)')
    INISTRIKEPRICE = Column(Numeric(20, 4), comment='初始行权价')
    INISTRIKERATIO = Column(Numeric(24, 8), comment='初始行权比例')
    DURATION_DAYS = Column(Numeric(20, 4), comment='存续期限(天)')
    DURATION_STARTDATE = Column(VARCHAR(8), comment='存续起始日期')
    DURATION_ENDDATE = Column(VARCHAR(8), comment='存续截止日期')
    ISSUEDATE = Column(VARCHAR(8), comment='发行日期')
    ISSUEPRICE = Column(Numeric(20, 4), comment='发行价格')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    LISTEDDATE = Column(VARCHAR(8), comment='上市日期')
    ANNISSUEDATE = Column(VARCHAR(8), comment='发行公告日')
    ANNLISTEDDATE = Column(VARCHAR(8), comment='上市公告日')
    SETTLEMENTMETHOD = Column(VARCHAR(40), comment='结算方式')
    EXERCISINGEND = Column(VARCHAR(8), comment='最后行权日')
    EXERCODE = Column(VARCHAR(20), comment='行权代码')
    EXERNAME = Column(VARCHAR(40), comment='行权简称')
    ISRATIOADJUST = Column(Numeric(5, 0), comment='行权价及行权比例是否调整')
    ADJUSTRATIO = Column(VARCHAR(800), comment='行权价及比例调整公式')
    PROGRESS = Column(VARCHAR(8), comment='方案进度')
    PRELAN_DATE = Column(VARCHAR(8), comment='预案公告日')
    SMTG_DATE = Column(VARCHAR(8), comment='股东大会公告日')
    TYPEBYISSUER = Column(VARCHAR(40), comment='权证类型(按发行人分类)')
    OLD_SHRHLDR_RATIO = Column(Numeric(20, 4), comment='原股东配售比例')
    PLACINGRECORDDATE = Column(VARCHAR(8), comment='权证配售股权登记日')
    OFFERINGOBJECT = Column(VARCHAR(40), comment='发行对象')
    GUARTYPE = Column(VARCHAR(40), comment='担保方式')
    EXERCISESTARTDATE = Column(VARCHAR(8), comment='行权起始日期')
    REF_PRICE = Column(Numeric(20, 4), comment='上市首日参考价')
    ISCALLCLAUSE = Column(Numeric(5, 0), comment='是否有约购条款')
    CALLPRICE = Column(Numeric(20, 4), comment='回购价格')
    CALLDESCRIPTION = Column(VARCHAR(500), comment='回购说明')
    GUARANTOR = Column(VARCHAR(300), comment='担保人')
    GUARDESCRIPTION = Column(VARCHAR(400), comment='担保说明')
    WARRANTSOURCE = Column(VARCHAR(40), comment='权证来源')
    WARRANT_NUM_PER_BOND = Column(Numeric(20, 4), comment='每张债券附认股权证数量')
    BONDWINDCODE = Column(VARCHAR(10), comment='债券交易代码(证券id)')
    LASTTRADEDATE = Column(VARCHAR(8), comment='最后交易日')
    EXPIREDATE = Column(VARCHAR(8), comment='停止交易日')
    RECORDDATE_PUTWARRANT = Column(VARCHAR(8), comment='认沽权利股权登记日')
    S_INFO_LISTBOARD = Column(VARCHAR(10), comment='上市板')


class CWARRANTHOLDER(Base):
    """中国权证持有人"""
    __tablename__ = 'CWARRANTHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    END_DATE = Column(VARCHAR(8), comment='日期')
    HOLDER = Column(VARCHAR(200), comment='持有人')


class CWARRANTHOLDERZL(Base):
    """中国权证持有人(增量)"""
    __tablename__ = 'CWARRANTHOLDERZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    END_DATE = Column(VARCHAR(8), comment='日期')
    HOLDER = Column(VARCHAR(200), comment='持有人')


class ECBNEWS(Base):
    """None"""
    __tablename__ = 'ECBNEWS'
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


class ECONOMICINDICATORS(Base):
    """None"""
    __tablename__ = 'ECONOMICINDICATORS'
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


class EURIBORPRICE(Base):
    """EURIBOR行情"""
    __tablename__ = 'EURIBORPRICE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券ID')
    TRADE_DT = Column(VARCHAR(20), comment='利率代码')
    B_INFO_RATE = Column(Numeric(20, 4), comment='收盘利率')


class EXMEMBERSTATISTICS(Base):
    """交易所会员每月交易量明细"""
    __tablename__ = 'EXMEMBERSTATISTICS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    ENN_DATE = Column(VARCHAR(8), comment='月份')
    S_INFO_EXCHMAR = Column(VARCHAR(20), comment='交易所')
    COMP_NAME = Column(VARCHAR(100), comment='会员名称')
    COMP_SNAME = Column(VARCHAR(60), comment='会员简称')
    TYPE_CODE = Column(VARCHAR(5), comment='会员类型')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='会员公司id')
    TOTAL_VOL = Column(Numeric(15, 4), comment='总计(万元)')
    SHARES = Column(Numeric(15, 4), comment='股票(万元)')
    ASHARES = Column(Numeric(15, 4), comment='A股(万元)')
    BSHARES = Column(Numeric(15, 4), comment='B股(万元)')
    WARRANT = Column(Numeric(20, 4), comment='权证(万元)')
    CPS = Column(Numeric(20, 4), comment='优先股(万元)')
    OPTIONS = Column(Numeric(20, 4), comment='期权(万元)')
    SEC_INV_FUND = Column(Numeric(15, 4), comment='证券投资基金(万元)')
    ETF = Column(Numeric(20, 4), comment='ETF(万元)')
    OTHER_FUND = Column(Numeric(15, 4), comment='其他基金(万元)')
    BONDSPOT = Column(Numeric(20, 4), comment='债券现货(万元)')
    GOVBOND = Column(Numeric(15, 4), comment='国债现货(万元)')
    TBOND = Column(Numeric(15, 4), comment='可转债(万元)')
    FIN_COMP_BOND = Column(Numeric(15, 4), comment='金融债、企业债(万元)')
    BONDREPO = Column(Numeric(20, 4), comment='债券回购(万元)')
    GOVBONDREPO = Column(Numeric(15, 4), comment='国债回购(万元)')
    S_MARGIN_PURCHWITHBORROWMONEY = Column(Numeric(20, 4), comment='融资买入(万元)')
    S_MARGIN_TRADINGBALANCE = Column(Numeric(20, 4), comment='融资余额(万元)')
    S_MARGIN_SALESOFBORROWEDSEC = Column(Numeric(20, 4), comment='融券卖出')
    S_MARGIN_SECLENDINGBALANCEVOL = Column(Numeric(20, 4), comment='融券余量(万股)')
    S_MARGIN_SECLENDINGBALANCE = Column(Numeric(20, 4), comment='融券余额(万元)')
    S_MARGIN_MARGINTRADEBALANCE = Column(Numeric(20, 4), comment='融资融券余额(万元)')
    REPAYMENT = Column(Numeric(20, 4), comment='卖券还款')
    RETURNSTOCK = Column(Numeric(20, 4), comment='买券还券')


class FEDNEWS(Base):
    """None"""
    __tablename__ = 'FEDNEWS'
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


class FILESYNCTIMESCHEDULE(Base):
    """FileSync转档时间"""
    __tablename__ = 'FILESYNCTIMESCHEDULE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    PRODUCT_NAME = Column(VARCHAR(100), comment='产品包名')
    FREQUENCY = Column(VARCHAR(10), comment='频率')
    RUNTIME = Column(VARCHAR(100), comment='时间')
    WEEKLY_PARAMETER = Column(VARCHAR(50), comment='周(参数)')


class FINANCIALBALANCESHEETDETAILS(Base):
    """金融机构资产负债明细表"""
    __tablename__ = 'FINANCIALBALANCESHEETDETAILS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    SUBJECT_NAME = Column(VARCHAR(200), comment='科目名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='科目金额')
    CLASSIFICATION_NUMBER = Column(Numeric(4, 0), comment='序号')
    PUBLISH_VALUE = Column(VARCHAR(40), comment='公布值')
    PUBLISH_COUNITDIMENSION = Column(VARCHAR(20), comment='公布量纲')
    IS_LISTING_DATA = Column(Numeric(1, 0), comment='是否上市后数据')
    ACC_STA_CODE = Column(VARCHAR(40), comment='会计准则类型')


class FINANCIALCONCEPTPLATE(Base):
    """中国金融机构概念板块"""
    __tablename__ = 'FINANCIALCONCEPTPLATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_TYPECODE = Column(VARCHAR(50), comment='分类代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class FINANCIALFINANCIALDETAILS(Base):
    """金融机构现金流量明细表"""
    __tablename__ = 'FINANCIALFINANCIALDETAILS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    SUBJECT_NAME = Column(VARCHAR(200), comment='科目名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='科目金额')
    CLASSIFICATION_NUMBER = Column(Numeric(4, 0), comment='序号')
    PUBLISH_VALUE = Column(VARCHAR(40), comment='公布值')
    PUBLISH_COUNITDIMENSION = Column(VARCHAR(20), comment='公布量纲')
    IS_LISTING_DATA = Column(Numeric(1, 0), comment='是否上市后数据')
    ACC_STA_CODE = Column(VARCHAR(40), comment='会计准则类型')


class FINANCIALINCOMEDETAILS(Base):
    """金融机构利润明细表"""
    __tablename__ = 'FINANCIALINCOMEDETAILS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    SUBJECT_NAME = Column(VARCHAR(200), comment='科目名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='科目金额')
    CLASSIFICATION_NUMBER = Column(Numeric(4, 0), comment='序号')
    PUBLISH_VALUE = Column(VARCHAR(40), comment='公布值')
    PUBLISH_COUNITDIMENSION = Column(VARCHAR(20), comment='公布量纲')
    IS_LISTING_DATA = Column(Numeric(1, 0), comment='是否上市后数据')
    ACC_STA_CODE = Column(VARCHAR(40), comment='会计准则类型')


class FINANCIALNEWS(Base):
    """互联网财经舆情"""
    __tablename__ = 'FINANCIALNEWS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='唯一性标识')
    PUBLISHDATE = Column(DateTime, comment='Wind发布时间')
    TITLE = Column(VARCHAR(1200), comment='新闻标题')
    CONTENT = Column(TEXT(2147483647), comment='新闻内容')
    SOURCE = Column(VARCHAR(200), comment='新闻来源')
    URL = Column(VARCHAR(1800), comment='新闻链接')
    SECTIONS = Column(VARCHAR(3000), comment='新闻栏目')
    AREACODES = Column(TEXT(2147483647), comment='相关地区')
    WINDCODES = Column(TEXT(2147483647), comment='相关公司')
    INDUSTRYCODES = Column(TEXT(2147483647), comment='相关行业')
    SECTERCODES = Column(TEXT(2147483647), comment='概念板块')
    KEYWORDS = Column(VARCHAR(3000), comment='新闻关键字')
    OPDATE = Column(DateTime, comment='入库时间')
    OPMODE = Column(VARCHAR(1), comment='操作类型')
    MKTSENTIMENTS = Column(TEXT(2147483647), comment='市场情绪')


class FINANCIALNOTECATEGORY(Base):
    """财务附注项目类别配置表"""
    __tablename__ = 'FINANCIALNOTECATEGORY'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_SEGMENT_ITEMCODE = Column(VARCHAR(4), comment='项目类别代码')
    S_SEGMENT_ITEMNAME = Column(VARCHAR(40), comment='项目类别名称')
    S_CORRESPONDING_CONTENT = Column(VARCHAR(40), comment='对应的数据内容')


class FINANCIALQUALIFICATION(Base):
    """中国共同基金金融机构资格"""
    __tablename__ = 'FINANCIALQUALIFICATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    ORGANIZATION_NAME = Column(VARCHAR(100), comment='机构公布名称')
    FINANCIAL_TYPE = Column(VARCHAR(100), comment='金融机构资格类型')
    ACQUISITION_DATE = Column(VARCHAR(8), comment='获得日期')
    REVOKE_DATE = Column(VARCHAR(8), comment='撤销日期')
    IS_EFFECTIVE = Column(Numeric(5, 0), comment='是否有效')
    S_INFO_NAME = Column(VARCHAR(200), comment='公司简称')
    AGENCY_TYPCODE = Column(VARCHAR(80), comment='机构类型')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    FINANCIAL_TYPE_NUM = Column(Numeric(9, 0), comment='金融机构资格类型代码')
    QUALIFICATION_CODE = Column(VARCHAR(100), comment='资格编码')


class FINANCIALREGIONAL(Base):
    """中国金融机构地域板块"""
    __tablename__ = 'FINANCIALREGIONAL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    WIND_SEC_CODE = Column(VARCHAR(10), comment='板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class FINDEXPERFORMANCE(Base):
    """中国共同基金指数业绩表现"""
    __tablename__ = 'FINDEXPERFORMANCE'
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
    PCT_CHG_RECENT1W = Column(Numeric(20, 6), comment='最近1周涨跌幅')


class FINDEXRISKANALYSIS(Base):
    """中国共同基金指数风险分析指标"""
    __tablename__ = 'FINDEXRISKANALYSIS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    RISKANALYSIS_CODE = Column(Numeric(9, 0), comment='指标类型代码')
    RISKANALYSIS_NAME = Column(VARCHAR(100), comment='指标名称')
    RISKANALYSIS_VALUE = Column(Numeric(20, 8), comment='指标数值')


class FINNOTESACCOUNTSPAYABLE(Base):
    """中国A股财务附注--应付账款"""
    __tablename__ = 'FINNOTESACCOUNTSPAYABLE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    ITEM_DATA = Column(VARCHAR(40), comment='数据内容')
    ITEM_TYPE_CODE = Column(VARCHAR(4), comment='项目类别代码')
    ANN_ITEM = Column(VARCHAR(400), comment='项目公布名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='项目金额')
    ITEM_NAME = Column(VARCHAR(100), comment='项目容错名称')


class FINNOTESDETAIL(Base):
    """中国A股财务附注明细"""
    __tablename__ = 'FINNOTESDETAIL'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
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


class FINSEGMENTINFO(Base):
    """金融机构经营分部业务数据"""
    __tablename__ = 'FINSEGMENTINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    CLASS_CODE = Column(Numeric(9, 0), comment='分部类别代码')
    SUBJECT_CODE = Column(Numeric(9, 0), comment='科目代码')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='项目金额')
    UNIT = Column(VARCHAR(40), comment='单位')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    SUBJECT_NAME_ANN = Column(VARCHAR(100), comment='[内部]公布名称')


class FIPARTICIPANTCODE(Base):
    """金融机构参与方编码"""
    __tablename__ = 'FIPARTICIPANTCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务类型代码')
    S_CODE = Column(VARCHAR(20), comment='业务代码')


class FIXEDINCOMENEWS(Base):
    """None"""
    __tablename__ = 'FIXEDINCOMENEWS'
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


class FLOATINGCOUPONSRATE(Base):
    """中国浮息债票面利率变动"""
    __tablename__ = 'FLOATINGCOUPONSRATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    RATE = Column(Numeric(22, 6), comment='利率(%)')


class FOREIGNEXCHANGENEWS(Base):
    """None"""
    __tablename__ = 'FOREIGNEXCHANGENEWS'
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


class FOREXOPTIONDELTA(Base):
    """外汇期权Delta计量参数"""
    __tablename__ = 'FOREXOPTIONDELTA'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    CRNCY_CODE = Column(VARCHAR(6), comment='外汇品种代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    ANAL_CURVETERM = Column(VARCHAR(8), comment='标准期限')
    MATURITYDATE = Column(VARCHAR(8), comment='到期日')
    MATURITY_DAY = Column(Numeric(6, 0), comment='到期天数')
    SPOT_PRICE_TYPE_CODE = Column(Numeric(3, 0), comment='即期价格类型代码')
    SPOT_PRICE = Column(Numeric(20, 4), comment='即期价格')
    RMB_RATE_TYPE_CODE = Column(Numeric(3, 0), comment='人民币利率类型代码')
    INTEREST_RATE = Column(Numeric(20, 4), comment='本币利率')
    VOLATILITY_TYPE_CODE = Column(Numeric(3, 0), comment='波动率类型代码')
    FOREIGN_CURRENCY_RATE = Column(Numeric(20, 4), comment='外币利率')
    IMPLIED_VOLATILITY = Column(Numeric(20, 4), comment='隐含波动率')
    FOREIGN_SWAP_POINT = Column(Numeric(20, 4), comment='外汇掉期点')
    EXECUTIVE_PRICE = Column(Numeric(20, 4), comment='执行价格')
    CALL_OPTION_DELTA = Column(Numeric(20, 4), comment='看涨期权delta')
    PUT_OPTION_DELTA = Column(Numeric(20, 4), comment='看跌期权delta')


class FUNDACASHFLOW(Base):
    """中国基金公司现金流量表"""
    __tablename__ = 'FUNDACASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='Wind代码')
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
    OTHER_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='其他资产减值损失')
    CREDIT_IMPAIRMENT_LOSS = Column(Numeric(20, 4), comment='信用减值损失')
    RIGHT_USE_ASSETS_DEP = Column(Numeric(20, 4), comment='使用权资产折旧')


class FUNDANNCOLUMN(Base):
    """基金公告栏目"""
    __tablename__ = 'FUNDANNCOLUMN'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    N_INFO_CODE = Column(VARCHAR(38), comment='Wind栏目代码')
    N_INFO_PCODE = Column(VARCHAR(38), comment='父节点栏目代码')
    N_INFO_FCODE = Column(VARCHAR(38), comment='本节栏目代码')
    N_INFO_NAME = Column(VARCHAR(200), comment='栏目名称')
    N_INFO_ISVALID = Column(Numeric(2, 0), comment='是否有效')
    N_INFO_LEVELNUM = Column(Numeric(2, 0), comment='栏目级别')


class FUNDANNCOLUMNZL(Base):
    """基金公告栏目增量"""
    __tablename__ = 'FUNDANNCOLUMNZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    N_INFO_CODE = Column(VARCHAR(38), comment='Wind栏目代码')
    N_INFO_PCODE = Column(VARCHAR(38), comment='父节点栏目代码')
    N_INFO_FCODE = Column(VARCHAR(38), comment='本节栏目代码')
    N_INFO_NAME = Column(VARCHAR(200), comment='栏目名称')
    N_INFO_ISVALID = Column(Numeric(2, 0), comment='是否有效')
    N_INFO_LEVELNUM = Column(Numeric(2, 0), comment='栏目级别')


class FUNDANNINF(Base):
    """基金公告信息"""
    __tablename__ = 'FUNDANNINF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    N_INFO_STOCKID = Column(VARCHAR(10), comment='证券ID')
    N_INFO_COMPANYID = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(DateTime, comment='公告日期')
    N_INFO_TITLE = Column(VARCHAR(1024), comment='标题')
    N_INFO_FCODE = Column(VARCHAR(200), comment='栏目代码')
    N_INFO_FTXT = Column(TEXT(2147483647), comment='摘要')
    N_INFO_ANNLINK = Column(VARCHAR(1024), comment='公告链接')


class FUNDANNINFTEXT(Base):
    """基金公告文本"""
    __tablename__ = 'FUNDANNINFTEXT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    ANN_OBJECT_ID = Column(VARCHAR(100), comment='公告主表对象ID')
    ANN_TEXT = Column(VARCHAR, comment='公告正文')


class FUNDBALANCESHEET(Base):
    """中国基金公司资产负债表"""
    __tablename__ = 'FUNDBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='Wind代码')
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
    FIN_ASSETS_COST_SHARING = Column(Numeric(20, 4), comment='以摊余成本计量的金融资产')
    FIN_ASSETS_FAIR_VALUE = Column(Numeric(20, 4), comment='以公允价值计量且其变动计入其他综合收益的金融资产')
    CONTRACTUAL_ASSETS = Column(Numeric(20, 4), comment='合同资产')
    CONTRACT_LIABILITIES = Column(Numeric(20, 4), comment='合同负债')
    RECEIVABLES_FINANCING = Column(Numeric(20, 4), comment='应收款项融资')
    RIGHT_USE_ASSETS = Column(Numeric(20, 4), comment='使用权资产')
    LEASE_LIAB = Column(Numeric(20, 4), comment='租赁负债')


class FUNDBONDPORTFOLIO(Base):
    """全球基金债券组合(分评级)"""
    __tablename__ = 'FUNDBONDPORTFOLIO'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True, comment='对象ID')
    S_INFO_CODE = Column(VARCHAR(40), comment='基金代码')
    DEADLINE = Column(VARCHAR(8), comment='截止日期')
    B_INFO_CREDITRATING = Column(Numeric(9, 0), comment='债券评级代码')
    RATING_VALUE_TYPE = Column(Numeric(9, 0), comment='评级取值类型')
    MARKET_VALUE = Column(Numeric(20, 4), comment='市值')
    NET_ASSETS_RATIO = Column(Numeric(20, 4), comment='占净资产比例')
    CURRENCY_CODE = Column(VARCHAR(10), comment='市值货币代码')
    POSITION_TYPE_CODE = Column(Numeric(9, 0), comment='持仓类型代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    ANNOUNCE_RATING_CODE = Column(VARCHAR(20), comment='公布评级代码')
    COMP_ID = Column(VARCHAR(40), comment='公司ID')
    RATING_TYPE_CODE = Column(Numeric(9, 0), comment='评级品种类别代码')


class FUNDCOMPANYINSIDEHOLDER(Base):
    """中国基金公司十大股东"""
    __tablename__ = 'FUNDCOMPANYINSIDEHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    COMP_SNAME = Column(VARCHAR(200), comment='公司名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_HOLDER_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_HOLDER_HOLDERCATEGORY = Column(VARCHAR(1), comment='股东类型')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    S_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='持股数量（股）')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例（%）')
    S_HOLDER_SHARECATEGORY = Column(VARCHAR(40), comment='持股性质代码')
    S_HOLDER_RESTRICTEDQUANTITY = Column(Numeric(20, 4), comment='持有限售股份（非流通股）数量')
    S_HOLDER_ANAME = Column(VARCHAR(100), comment='股东名称')
    S_HOLDER_SEQUENCE = Column(VARCHAR(10), comment='关联方序号')
    S_HOLDER_SHARECATEGORYNAME = Column(VARCHAR(40), comment='持股性质')
    S_HOLDER_MEMO = Column(VARCHAR(1500), comment='股东说明')


class FUNDCREDITRECORD(Base):
    """中国基金公司诚信记录"""
    __tablename__ = 'FUNDCREDITRECORD'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    EVENT_ID = Column(VARCHAR(20), comment='事件ID')
    REGULATORS_ID = Column(VARCHAR(10), comment='监管机构ID')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    EFFECTIVE_DATE = Column(VARCHAR(8), comment='生效日期')
    REGULATORY_OBJECT_NAME = Column(VARCHAR(100), comment='监管对象名称')
    REGULATORY_OBJECT_ID = Column(VARCHAR(10), comment='监管对象ID')
    REGULATORY_OBJECT_CODE = Column(Numeric(9, 0), comment='监管对象类别代码')
    REGULATORY_OBJECT_TYPE = Column(Numeric(9, 0), comment='监管对象类型代码')
    MEASURES_DISPOSITION = Column(VARCHAR(1000), comment='处分措施')
    MEASURES_DISPOSITION_CODE = Column(Numeric(9, 0), comment='处分措施代码')
    PUNISHMENT_MEASURES_CODE = Column(Numeric(9, 0), comment='处罚措施代码')
    PENALTY_AMOUNT = Column(Numeric(24, 8), comment='处罚金额')
    BUSINESS_RESTRICTIVE_MEASURES = Column(Numeric(9, 0), comment='业务资格限制措施代码')
    PUNISHMENT_TIME_CODE = Column(Numeric(9, 0), comment='处分期限代码')
    DEBAR_MEASURES_CODE = Column(Numeric(9, 0), comment='市场禁入措施代码')
    INSTITUTION_ID = Column(VARCHAR(10), comment='处罚时所在机构ID')
    IRREGULARITIES = Column(VARCHAR(1000), comment='违规事项')
    LEGAL_BASIS = Column(VARCHAR(1000), comment='法律依据')
    DETAILED_CONTENT = Column(TEXT(2147483647), comment='详细内容')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务类型代码')
    INVOLVING_COMP_ID = Column(VARCHAR(10), comment='涉及公司ID')
    IS_EFFECTIVE = Column(Numeric(1, 0), comment='是否生效')


class FUNDINCOME(Base):
    """中国基金公司利润表"""
    __tablename__ = 'FUNDINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
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
    EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    NET_PROFIT_AFTER_DED_NR_LP = Column(Numeric(20, 4), comment='扣除非经常性损益后净利润')
    NET_PROFIT_UNDER_INTL_ACC_STA = Column(Numeric(20, 4), comment='国际会计准则净利润')
    COMP_TYPE_CODE = Column(VARCHAR(2), comment='公司类型代码')
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
    NET_AFTER_DED_NR_LP_CORRECT = Column(Numeric(20, 4), comment='扣除非经常性损益后的净利润(财务重要指标(更正前))')
    OTHER_INCOME = Column(Numeric(20, 4), comment='其他收益')
    MEMO = Column(VARCHAR(1000), comment='备注')
    ASSET_DISPOSAL_INCOME = Column(Numeric(20, 4), comment='资产处置收益')
    CONTINUED_NET_PROFIT = Column(Numeric(20, 4), comment='持续经营净利润')
    END_NET_PROFIT = Column(Numeric(20, 4), comment='终止经营净利润')
    OTHER_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='其他资产减值损失')
    TOT_OPER_COST2 = Column(Numeric(20, 4), comment='营业总成本2')


class FUNDMOVENEWS(Base):
    """None"""
    __tablename__ = 'FUNDMOVENEWS'
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


class FUNDNEGATIVENEWS(Base):
    """None"""
    __tablename__ = 'FUNDNEGATIVENEWS'
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


class FUNDNEWS(Base):
    """None"""
    __tablename__ = 'FUNDNEWS'
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


class FUNDPOSITIVENEWS(Base):
    """None"""
    __tablename__ = 'FUNDPOSITIVENEWS'
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


class FUNDSAMFEE(Base):
    """中国券商理财费率"""
    __tablename__ = 'FUNDSAMFEE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券ID')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    FEETYPECODE = Column(Numeric(9, 0), comment='费率类型代码')
    CHARGEWAY = Column(VARCHAR(20), comment='收费类型')
    AMOUNTDOWNLIMIT = Column(Numeric(20, 4), comment='金额下限(元)')
    AMOUNTUPLIMIT = Column(Numeric(20, 4), comment='金额上限(元)')
    RETURNDOWNLIMIT = Column(Numeric(20, 4), comment='收益率下限(%)')
    RETURNUPLIMIT = Column(Numeric(20, 4), comment='收益率上限(%)')
    NAVDOWNLIMIT = Column(Numeric(20, 4), comment='净值下限(元)')
    NAVUPLIMIT = Column(Numeric(20, 4), comment='净值上限(元)')
    HOLDINGPERIOD_DOWNLIMIT = Column(Numeric(20, 4), comment='持有年限下限(年)')
    HOLDINGPERIOD_UPLIMIT = Column(Numeric(20, 4), comment='持有年限上限(年)')
    FEERATIO = Column(Numeric(20, 4), comment='费率(%)')
    CUR_SIGN = Column(Numeric(1, 0), comment='[内部]最新标志')
    SUPPLEMENTARY = Column(VARCHAR(800), comment='费率补充说明')


class FUNDSAMPERFORMANCE(Base):
    """中国券商理财业绩表现"""
    __tablename__ = 'FUNDSAMPERFORMANCE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    F_AVGRETURN_THISWEEK = Column(Numeric(20, 6), comment='收益率(本周以来)')
    F_AVGRETURN_THISMONTH = Column(Numeric(20, 6), comment='收益率(本月以来)')
    F_AVGRETURN_THISQUARTER = Column(Numeric(20, 6), comment='收益率(本季以来)')
    F_AVGRETURN_WEEK = Column(Numeric(20, 6), comment='收益率(一周)')
    F_AVGRETURN_MONTH = Column(Numeric(20, 6), comment='收益率(一个月)')
    F_AVGRETURN_QUARTER = Column(Numeric(20, 6), comment='收益率(三个月)')
    F_AVGRETURN_HALFYEAR = Column(Numeric(20, 6), comment='收益率(六个月)')
    F_AVGRETURN_THISYEAR = Column(Numeric(20, 6), comment='收益率(本年以来)')
    F_AVGRETURN_YEAR = Column(Numeric(20, 6), comment='收益率(一年)')
    F_AVGRETURN_TWOYEA = Column(Numeric(20, 6), comment='收益率(两年)')
    F_AVGRETURN_THREEYEAR = Column(Numeric(20, 6), comment='收益率(三年)')
    F_AVGRETURN_FOURYEAR = Column(Numeric(20, 6), comment='收益率(四年)')
    F_AVGRETURN_FIVEYEAR = Column(Numeric(20, 6), comment='收益率(五年)')
    F_AVGRETURN_SIXYEAR = Column(Numeric(20, 6), comment='收益率(六年)')
    F_AVGRETURN_SINCEFOUND = Column(Numeric(20, 6), comment='收益率(成立以来)')
    F_ANNUALYEILD = Column(Numeric(20, 6), comment='年化收益率')
    F_TRACKDEV_THISDAY = Column(Numeric(20, 6), comment='当天跟踪偏离度')
    F_SFRETURN_THISYEAR = Column(Numeric(20, 6), comment='今年以来同类基金收益率')
    F_SFRANK_THISYEAR = Column(Numeric(20, 0), comment='今年以来同类排名')
    F_SFRETURN_RECENTQUARTER = Column(Numeric(20, 6), comment='最近三月同类基金收益率')
    F_SFRANK_RECENTQUARTER = Column(Numeric(20, 0), comment='最近三月同类排名')
    F_SFRETURN_RECENTHALFYEAR = Column(Numeric(20, 6), comment='最近六月同类基金收益率')
    F_SFRANK_RECENTHALFYEAR = Column(Numeric(20, 0), comment='最近六月同类排名')
    F_SFRETURN_RECENTYEAR = Column(Numeric(20, 6), comment='最近一年同类基金收益率')
    F_SFRANK_RECENTYEAR = Column(Numeric(20, 0), comment='最近一年同类排名')
    F_SFRETURN_RECENTTWOYEAR = Column(Numeric(20, 6), comment='最近两年同类基金收益率')
    F_SFRANK_RECENTTWOYEAR = Column(Numeric(20, 0), comment='最近两年同类排名')
    F_SFRETURN_RECENTTHREEYEAR = Column(Numeric(20, 6), comment='最近三年同类基金收益率')
    F_SFRANK_RECENTTHREEYEAR = Column(Numeric(20, 0), comment='最近三年同类排名')
    F_SFRETURN_RECENTFIVEYEAR = Column(Numeric(20, 6), comment='最近五年同类基金收益率')
    F_SFRANK_RECENTFIVEYEAR = Column(Numeric(20, 0), comment='最近五年同类排名')
    F_SFRETURN_SINCEFOUND = Column(Numeric(20, 6), comment='成立以来同类基金收益率')
    F_SFRANK_SINCEFOUND = Column(Numeric(20, 0), comment='成立以来同类排名')
    F_SFANNUALYEILD = Column(Numeric(20, 6), comment='同类基金年化收益率')
    F_SFRANK_ANNUALYEILD = Column(Numeric(20, 0), comment='年化收益率同类排名')
    F_STDARDDEV_HALFYEAR = Column(Numeric(20, 6), comment='标准差(六个月)')
    F_STDARDDEV_YEAR = Column(Numeric(20, 6), comment='标准差(一年)')
    F_STDARDDEV_TWOYEAR = Column(Numeric(20, 6), comment='标准差(两年)')
    F_STDARDDEV_THREEYEAR = Column(Numeric(20, 6), comment='标准差(三年)')
    F_STDARDDEV_FIVEYEAR = Column(Numeric(20, 6), comment='标准差(五年)')
    F_STDARDDEV_SINCEFOUND = Column(Numeric(20, 6), comment='标准差(成立以来)')
    F_SHARPRATIO_HALFYEAR = Column(Numeric(20, 6), comment='夏普比率(六个月)')
    F_SHARPRATIO_YEAR = Column(Numeric(20, 6), comment='夏普比率(一年)')
    F_SHARPRATIO_TWOYEAR = Column(Numeric(20, 6), comment='夏普比率(两年)')
    F_SHARPRATIO_THREEYEAR = Column(Numeric(20, 6), comment='夏普比率(三年)')
    F_SFRETURN_RECENTWEEK = Column(Numeric(20, 6), comment='最近一周同类基金收益率')
    F_SFRANK_RECENTWEEK = Column(Numeric(20, 0), comment='最近一周同类排名')
    F_SFRETURN_RECENTMONTH = Column(Numeric(20, 6), comment='最近一月同类基金收益率')
    F_SFRANK_RECENTMONTH = Column(Numeric(20, 0), comment='最近一月同类排名')
    F_AVGRETURN_DAY = Column(Numeric(20, 6), comment='收益率(当天)')
    F_SFRANK_THISYEART = Column(VARCHAR(50), comment='今年以来同类排名')
    F_SFRANK_RECENTQUARTERT = Column(VARCHAR(50), comment='最近三月同类排名')
    F_SFRANK_RECENTHALFYEART = Column(VARCHAR(50), comment='最近六月同类排名')
    F_SFRANK_RECENTYEART = Column(VARCHAR(50), comment='最近一年同类排名')
    F_SFRANK_RECENTTWOYEART = Column(VARCHAR(50), comment='最近两年同类排名')
    F_SFRANK_RECENTTHREEYEART = Column(VARCHAR(50), comment='最近三年同类排名')
    F_SFRANK_RECENTFIVEYEART = Column(VARCHAR(50), comment='最近五年同类排名')
    F_SFRANK_SINCEFOUNDT = Column(VARCHAR(50), comment='成立以来同类排名')
    F_SFRANK_ANNUALYEILDT = Column(VARCHAR(50), comment='年化收益率同类排名')
    F_SFRANK_RECENTWEEKT = Column(VARCHAR(50), comment='最近一周同类排名')
    F_SFRANK_RECENTMONTHT = Column(VARCHAR(50), comment='最近一月同类排名')


class FUNDSAMRISKANALYSISINDEX(Base):
    """中国券商理财风险分析指标"""
    __tablename__ = 'FUNDSAMRISKANALYSISINDEX'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    RISKANALYSIS_CODE = Column(Numeric(9, 0), comment='指标类型代码')
    RISKANALYSIS_NAME = Column(VARCHAR(100), comment='指标名称')
    RISKANALYSIS_VALUE = Column(Numeric(20, 8), comment='指标数值')


class FUNDTENDENCY(Base):
    """None"""
    __tablename__ = 'FUNDTENDENCY'
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


class FUNDVIEWNEWS(Base):
    """None"""
    __tablename__ = 'FUNDVIEWNEWS'
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


class FUTURESEXCHANGEPRODUCTCODE(Base):
    """中国期货交易所标准产品代码"""
    __tablename__ = 'FUTURESEXCHANGEPRODUCTCODE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BUSINESS_TYPE_CODE = Column(Numeric(9, 0), comment='业务代码类型')
    BUSINESS_CODE = Column(VARCHAR(40), comment='业务代码')
    BUSINESS_ABBREVIATION = Column(VARCHAR(100), comment='业务简称')


class FUTURESNEGATIVENEWS(Base):
    """None"""
    __tablename__ = 'FUTURESNEGATIVENEWS'
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


class FUTURESNEWS(Base):
    """None"""
    __tablename__ = 'FUTURESNEWS'
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


class FUTURESPOSITIVENEWS(Base):
    """None"""
    __tablename__ = 'FUTURESPOSITIVENEWS'
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


class FXEODPRICES(Base):
    """中国外汇交易行情"""
    __tablename__ = 'FXEODPRICES'
    __table_args__ = (
        Index('IDX_FXEODPRICES_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='外汇交易代码')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DQ_BUY = Column(Numeric(20, 8), comment='买入价')
    S_DQ_SELL = Column(Numeric(20, 8), comment='卖出价')


class FXRAMOUNT(Base):
    """发行人债券余额"""
    __tablename__ = 'FXRAMOUNT'
    OBJECT_ID = Column(VARCHAR(50), primary_key=True, comment='OBJECT_ID')
    CO_NAME = Column(VARCHAR(80), comment='公司名称')
    AMOUNT = Column(Numeric(20, 6), comment='发行人债券余额')


class FXREMARKS(Base):
    """None"""
    __tablename__ = 'FXREMARKS'
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


class FXRMBMIDRATE(Base):
    """中国外汇牌价"""
    __tablename__ = 'FXRMBMIDRATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    CRNCY_CODE = Column(VARCHAR(40), comment='货币代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CRNCY_MIDRATE = Column(Numeric(20, 6), comment='中间价')


class GICSCODE(Base):
    """全球行业板块(废弃)"""
    __tablename__ = 'GICSCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCODE = Column(VARCHAR(40), comment='GICS代码')
    INDUSTRIESNAME = Column(VARCHAR(200), comment='GICS行业名称')
    INDUSTRIESENAME = Column(VARCHAR(200), comment='GICS行业英文名称')
    LEVELNUM = Column(Numeric(5, 0), comment='级数')


class GICSCODEZL(Base):
    """全球行业板块(增量)(废弃)"""
    __tablename__ = 'GICSCODEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCODE = Column(VARCHAR(40), comment='GICS代码')
    INDUSTRIESNAME = Column(VARCHAR(200), comment='GICS行业名称')
    INDUSTRIESENAME = Column(VARCHAR(200), comment='GICS行业英文名称')
    LEVELNUM = Column(Numeric(5, 0), comment='级数')


class GLOBALBONDNEWS(Base):
    """None"""
    __tablename__ = 'GLOBALBONDNEWS'
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


class GLOBALINDEXEOD(Base):
    """全球指数行情"""
    __tablename__ = 'GLOBALINDEXEOD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额')
    S_DQ_MV = Column(Numeric(20, 4), comment='市值')
    S_DQ_PCTCHANGE = Column(Numeric(20, 4), comment='涨跌幅(%)')


class GLOBALMARKETTRADINGTIME(Base):
    """全球市场交易时间"""
    __tablename__ = 'GLOBALMARKETTRADINGTIME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    EXCHANGE_SNAME_ENG = Column(VARCHAR(40), comment='交易所英文简称')
    EXCHANGE_NAME = Column(VARCHAR(40), comment='交易所中文名称')
    SECURITIES_TYPE = Column(VARCHAR(1000), comment='交易品种描述')
    TRADING_HOURS_CODE = Column(VARCHAR(5), comment='交易时段编码')
    TRADING_HOURS = Column(VARCHAR(500), comment='交易时段')
    TRADING_HOURS_2 = Column(VARCHAR(1000), comment='交易时段(新)')
    EXCHANGE_ENG_NAME = Column(VARCHAR(200), comment='交易所英文名称')


class GLOBALWORKINGDAY(Base):
    """全球工作日安排"""
    __tablename__ = 'GLOBALWORKINGDAY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    WORKING_DATE = Column(VARCHAR(8), comment='日期')
    COUNTRY_CODE = Column(VARCHAR(10), comment='国家或地区代码')


class GOLDMKTNEWS(Base):
    """None"""
    __tablename__ = 'GOLDMKTNEWS'
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


class HDRINFO(Base):
    """香港股票存托凭证份额"""
    __tablename__ = 'HDRINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    END_DATE = Column(VARCHAR(8), comment='截止日期')
    ISSUED_SHARES = Column(Numeric(20, 4), comment='基础证券股份数(万股)')
    SHARE_CODE = Column(VARCHAR(10), comment='基础证券id')
    HDR_STAND_FOR_SHARES = Column(Numeric(20, 4), comment='R:O比率')
    ISSUED_HDRS = Column(Numeric(20, 4), comment='已发行凭证份额数(万份)')


class HIBORPRICES(Base):
    """HiBor行情"""
    __tablename__ = 'HIBORPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_INFO_RATE = Column(Numeric(20, 8), comment='利率(%)')


class HOTTOPICNEWS(Base):
    """None"""
    __tablename__ = 'HOTTOPICNEWS'
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


class IAMFUNDDIVIDEND(Base):
    """保险资管产品分红"""
    __tablename__ = 'IAMFUNDDIVIDEND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EQY_RECORD_DT = Column(VARCHAR(8), comment='权益登记日')
    EX_DT = Column(VARCHAR(8), comment='除息日')
    DVD_PAYOUT_DT = Column(VARCHAR(8), comment='红利发放日')
    F_TEN_SP_DIV = Column(Numeric(24, 8), comment='每10份集合计划分红额')
    F_INFO_SPLITDATE = Column(VARCHAR(8), comment='份额拆分日')
    F_INFO_SPLITINC = Column(Numeric(20, 8), comment='份额拆分比例')


class IAMFUNDNAV(Base):
    """保险资管产品净值"""
    __tablename__ = 'IAMFUNDNAV'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    PRICE_DATE = Column(VARCHAR(8), comment='日期')
    F_NAV_UNIT = Column(Numeric(24, 8), comment='份额净值')
    F_NAV_ACCUMULATED = Column(Numeric(24, 8), comment='公布份额累计净值')
    F_NAV_DIVACCUMULATED = Column(Numeric(24, 8), comment='份额累计分红')
    F_NAV_ADJFACTOR = Column(Numeric(20, 8), comment='复权因子')
    CRNCY_CODE = Column(VARCHAR(10), comment='净值货币代码')
    F_NAV_ADJUSTED = Column(Numeric(24, 8), comment='复权单位净值(计算)')


class IBBONDTRADINGSTATS(Base):
    """None"""
    __tablename__ = 'IBBONDTRADINGSTATS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    STATS_TYPE = Column(VARCHAR(40), comment='统计分类')
    BOND_TYPE = Column(VARCHAR(40), comment='债券类型')
    TRANS_LOTS = Column(Numeric(20, 4), comment='成交笔数(笔)')
    CHANGE_LOTS = Column(Numeric(20, 4), comment='增减(笔)')
    AMOUNT = Column(Numeric(20, 4), comment='成交量(亿元)')
    CHANGE_AMOUNT = Column(Numeric(20, 4), comment='增减(亿元)')
    CHANGE_PCT = Column(Numeric(20, 4), comment='占总成交的比例(%)')


class IBFXEODPRICES(Base):
    """银行间外汇市场行情"""
    __tablename__ = 'IBFXEODPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    FX_INFO_WINDCODE = Column(VARCHAR(40), comment='外汇交易代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    FX_DQ_OPEN = Column(Numeric(20, 6), comment='开盘价')
    FX_DQ_HIGH = Column(Numeric(20, 6), comment='最高价')
    FX_DQ_LOW = Column(Numeric(20, 6), comment='最低价')
    FX_DQ_CLOSE = Column(Numeric(20, 6), comment='收盘价')
    FX_DQ_CLOSE2 = Column(Numeric(20, 6), comment='收盘价2')
    FX_DQ_PRECLOSE = Column(Numeric(20, 6), comment='昨收盘价')
    FX_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量')


class IECMEMBERLIST(Base):
    """发审委员基本资料"""
    __tablename__ = 'IECMEMBERLIST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TERM = Column(VARCHAR(3), comment='发审委届次')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    STATUS = Column(VARCHAR(10), comment='专职/兼职')
    NAME = Column(VARCHAR(40), comment='姓名')
    AGE = Column(Numeric(3, 0), comment='年龄')
    GENDER = Column(VARCHAR(2), comment='性别')
    PROFESSIONAL = Column(VARCHAR(40), comment='专业')
    DEGREE = Column(VARCHAR(40), comment='学历/学位')
    UNIT = Column(VARCHAR(100), comment='工作单位')
    POST = Column(VARCHAR(70), comment='职务')
    TITLE = Column(VARCHAR(40), comment='职称')
    TYPECODE = Column(Numeric(9, 0), comment='委员会类型代码')
    VALID_DT = Column(VARCHAR(8), comment='有效截止日期')


class IMPLIEDRATESCURVE(Base):
    """外汇隐含利率曲线"""
    __tablename__ = 'IMPLIEDRATESCURVE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TRADE_DATE = Column(VARCHAR(8), comment='日期')
    FOREIGN_EXCHANGE_CODE = Column(VARCHAR(6), comment='外汇品种代码')
    TERM = Column(VARCHAR(40), comment='期限')
    IMPLIED_RATES = Column(Numeric(20, 4), comment='隐含利率')
    MONETARY_INTEREST_RATE = Column(Numeric(20, 4), comment='标价货币利率')
    TYPE_CODE = Column(Numeric(1, 0), comment='标价货币利率类型代码')
    DISTANT_DROP_POINT = Column(Numeric(20, 4), comment='远/掉期点')
    RATE_TYPE_CODE = Column(Numeric(1, 0), comment='即期汇率类型代码')
    SPOT_EXCHANGE_RATE = Column(Numeric(20, 4), comment='即期汇率')


class INDEXCONTRASTSECTOR(Base):
    """指数板块对照"""
    __tablename__ = 'INDEXCONTRASTSECTOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_INDEXCODE = Column(VARCHAR(40), comment='指数万得代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='指数简称')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(16), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(50), comment='板块名称')
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(16), comment='板块代码2')
    S_INFO_INDUSTRYNAME_ENG = Column(VARCHAR(200), comment='板块英文名称')


class INDEXCONTRASTSECTORZL(Base):
    """指数板块对照(增量)"""
    __tablename__ = 'INDEXCONTRASTSECTORZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_INDEXCODE = Column(VARCHAR(40), comment='指数万得代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='指数简称')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(16), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(50), comment='板块名称')
    S_INFO_INDUSTRYCODE2 = Column(VARCHAR(16), comment='板块代码2')
    S_INFO_INDUSTRYNAME_ENG = Column(VARCHAR(200), comment='板块英文名称')


class INDUSTRYNEGATIVENEWS(Base):
    """None"""
    __tablename__ = 'INDUSTRYNEGATIVENEWS'
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


class INDUSTRYNEWS(Base):
    """None"""
    __tablename__ = 'INDUSTRYNEWS'
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


class INSURANCEFICLASS(Base):
    """国内保险业金融机构分类"""
    __tablename__ = 'INSURANCEFICLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_TYPECODE = Column(VARCHAR(50), comment='分类代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class INSURANCENEWS(Base):
    """None"""
    __tablename__ = 'INSURANCENEWS'
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


class INSURERPREMIUMINCOME(Base):
    """保险公司保费收入"""
    __tablename__ = 'INSURERPREMIUMINCOME'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    MONTHLY = Column(VARCHAR(6), comment='月度')
    INSURANCE_COMPANY = Column(VARCHAR(40), comment='保险公司')
    PREMIUM_CATEGORY = Column(VARCHAR(10), comment='保费类别')
    COMPANY_CATEGORY = Column(VARCHAR(10), comment='[内部]公司类别')
    INCOME = Column(Numeric(20, 4), comment='收入(万元)')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='保险公司id')
    ENTERPRISE_ANNUITY = Column(Numeric(20, 4), comment='企业年金缴费')
    ENTRUSTED_ASSETS = Column(Numeric(20, 4), comment='受托管理资产')
    INVESTMENT_ASSETS = Column(Numeric(20, 4), comment='投资管理资产')
    INSURED_INV_NEWLY_ADDED = Column(Numeric(20, 4), comment='保户投资款新增缴费')
    INV_LINKED_INSURANCE_ADDED = Column(Numeric(20, 4), comment='投连险独立账户新增增缴费')


class INSURERSOLVENCYINX(Base):
    """非上市保险公司偿付能力指标"""
    __tablename__ = 'INSURERSOLVENCYINX'
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    F_INFO_BGNDATE = Column(VARCHAR(8), comment='报告期起始日期')
    F_INFO_ENDDATE = Column(VARCHAR(8), comment='报告期截止日期')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    CORE_SLVCY_SURP = Column(Numeric(20, 4), comment='核心偿付能力溢额')
    ADEQUACY_RATIO = Column(Numeric(20, 4), comment='核心偿付能力充足率')
    COMPHSV_SLVCY_SURP = Column(Numeric(20, 4), comment='综合偿付能力溢额')
    COMPHSV_SLVCY_RATIO = Column(Numeric(20, 4), comment='综合偿付能力充足率')
    INSUANCE_OP_INCOME = Column(Numeric(20, 4), comment='保险业务收入')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    ASSETS_TODAY = Column(Numeric(20, 4), comment='净资产')
    ADMSB_ASSET = Column(Numeric(20, 4), comment='认可资产')
    ADMSB_DEBT = Column(Numeric(20, 4), comment='认可负债')
    ACTUAL_CAPITAL = Column(Numeric(20, 4), comment='实际资本')
    CORETIER1_CAPI = Column(Numeric(20, 4), comment='其中:核心一级资本')
    CORETIER2_CAPI = Column(Numeric(20, 4), comment='其中:核心二级资本')
    TIER_2_CAPITAL = Column(Numeric(20, 4), comment='其中:附属一级资本')
    OTHER_TIER_2_CAPITAL = Column(Numeric(20, 4), comment='其中:附属二级资本')
    MINIMUN_CAPITAL = Column(Numeric(20, 4), comment='最低资本')
    QUAN_RISK_MINIM_CPITAL = Column(Numeric(20, 4), comment='量化风险最低资本')
    MINIMUN_CAPITAL_IRFLIO = Column(Numeric(20, 4), comment='其中:寿险业务保险风险最低资本合计')
    MINIMUN_CAPITAL_NIO = Column(Numeric(20, 4), comment='其中:非寿险业务保险风险最低资本合计')
    MINIMUN_CAPITAL_MR = Column(Numeric(20, 4), comment='其中:市场风险最低资本合计')
    MINIMUN_CAPITAL_CRER = Column(Numeric(20, 4), comment='其中:信用风险最低资本合计')
    QUAN_EFFECT_RD = Column(Numeric(20, 4), comment='其中:量化风险分散效应')
    LAEO_SPECIFIC_NSURECON = Column(Numeric(20, 4), comment='其中:特定类别保险合同损失吸收效应')
    MINIMUN_CAPITAL_CONR = Column(Numeric(20, 4), comment='控制风险最低资本')
    ADDITIONAL_PCAPITAL = Column(Numeric(20, 4), comment='附加资本')
    THE_LATEST_RR = Column(VARCHAR(10), comment='最近一次风险综合评级类别')
    NET_CASH_FLOW = Column(Numeric(20, 4), comment='净现金流')
    NET_CASH_FLOW_1Y = Column(Numeric(20, 4), comment='净现金流:报告日后第1年')
    NET_CASH_FLOW_2Y = Column(Numeric(20, 4), comment='净现金流:报告日后第2年')
    NET_CASH_FLOW_3Y = Column(Numeric(20, 4), comment='净现金流:报告日后第3年')
    COMPREHSIVE_LR_3M = Column(Numeric(20, 4), comment='综合流动比率:3个月内')
    COMPREHSIVE_LR_W1Y = Column(Numeric(20, 4), comment='综合流动比率:1年内')
    COMPREHSIVE_LR_O1Y = Column(Numeric(20, 4), comment='综合流动比率:1年以上')
    COMPREHSIVE_LR_1TO3Y = Column(Numeric(20, 4), comment='综合流动比率:1-3年内')
    COMPREHSIVE_LR_3TO5Y = Column(Numeric(20, 4), comment='综合流动比率:3-5年内')
    COMPREHSIVE_LR_O5Y = Column(Numeric(20, 4), comment='综合流动比率:5年以上')
    THE_LIQT_BASIC_SCRIO = Column(Numeric(20, 4), comment='流动性覆盖率:基本情景')
    THE_LIQT_COMP_S1 = Column(Numeric(20, 4), comment='流动性覆盖率:公司整体:压力情景1')
    THE_LIQT_COMP_S2 = Column(Numeric(20, 4), comment='流动性覆盖率:公司整体:压力情景2')
    THE_LIQT_SACT_S1 = Column(Numeric(20, 4), comment='流动性覆盖率:独立账户:压力情景1')
    THE_LIQT_SACT_S2 = Column(Numeric(20, 4), comment='流动性覆盖率:独立账户:压力情景2')
    MINCAP_INSURE_RISK = Column(Numeric(20, 4), comment='其中:保险风险最低资本合计')
    NET_CASH_FLOW_1ST_QUARTER = Column(Numeric(20, 4), comment='其中:未来1季度')
    NET_CASH_FLOW_2ND_QUARTER = Column(Numeric(20, 4), comment='其中:未来2季度')
    NET_CASH_FLOW_3RD_QUARTER = Column(Numeric(20, 4), comment='其中:未来3季度')
    NET_CASH_FLOW_4TH_QUARTER = Column(Numeric(20, 4), comment='其中:未来4季度')
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')


class IPOCOMPRFA(Base):
    """IPO审核申报企业情况"""
    __tablename__ = 'IPOCOMPRFA'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPANYNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMPANYID = Column(VARCHAR(40), comment='公司ID')
    REGADDR = Column(VARCHAR(20), comment='注册地')
    SECTORS = Column(VARCHAR(100), comment='所属行业')
    SPONSOR = Column(VARCHAR(200), comment='保荐机构')
    SPON_REP = Column(VARCHAR(100), comment='保荐代表人')
    ACC_FIRM = Column(VARCHAR(200), comment='会计师事务所')
    CPA = Column(VARCHAR(100), comment='签字会计师')
    LAW_FIRM = Column(VARCHAR(200), comment='律师事务所')
    SOL_SIG = Column(VARCHAR(100), comment='签字律师')
    APP_CODE = Column(Numeric(9, 0), comment='申请事项代码')
    SCH_CODE = Column(Numeric(9, 0), comment='进度类型代码')
    TBLISTED = Column(Numeric(9, 0), comment='拟上市板块代码')
    ST_DATE = Column(VARCHAR(8), comment='状态起始日期')
    END_DATE = Column(VARCHAR(8), comment='状态终止日期')
    EST_ISSUENO = Column(Numeric(20, 4), comment='预计发行股数（万股）')
    EST_ISSUESHARES = Column(Numeric(20, 4), comment='预计发行后总股本（万股）')
    PRO_TOLALINV = Column(Numeric(20, 4), comment='募投项目投资总额')


class IPODECLAREDISCLOSUREDATE(Base):
    """IPO申报预披露日"""
    __tablename__ = 'IPODECLAREDISCLOSUREDATE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    PER_DISCLOSUREDATE = Column(VARCHAR(8), comment='纳入日期')


class IRSRATEYIELD(Base):
    """利率互换收益率曲线"""
    __tablename__ = 'IRSRATEYIELD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='OBJECT_ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_ANAL_CURVETYPE = Column(VARCHAR(40), comment='曲线类型')
    B_ANAL_CURVETYPECODE = Column(Numeric(9, 0), comment='曲线类型代码')
    B_ANAL_CURVETERM = Column(Numeric(20, 4), comment='期限(年)')
    B_ANAL_YTM = Column(Numeric(20, 4), comment='到期收益率(%)')
    B_TBF_SYTM = Column(Numeric(20, 4), comment='即期利率(%)')
    B_TBF_FYTM = Column(Numeric(20, 4), comment='远期利率(%)')


class LIBORPRICES(Base):
    """Libor行情"""
    __tablename__ = 'LIBORPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_INFO_RATE = Column(Numeric(20, 8), comment='利率(%)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')


class LTDBANKKINDSOVELOANSTERM(Base):
    """非上市银行财务附注--期限划分下的各类逾期贷款"""
    __tablename__ = 'LTDBANKKINDSOVELOANSTERM'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    ITEM_DATA = Column(VARCHAR(40), comment='数据内容')
    ITEM_TYPE_CODE = Column(VARCHAR(4), comment='项目类别代码')
    ANN_ITEM = Column(VARCHAR(400), comment='项目公布名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='项目金额')
    ITEM_NAME = Column(VARCHAR(100), comment='项目容错名称')
    ITEM_TYPE_NAME = Column(VARCHAR(100), comment='项目类别名称')


class MACRONEGATIVENEWS(Base):
    """None"""
    __tablename__ = 'MACRONEGATIVENEWS'
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


class MACROPOSITIVENEWS(Base):
    """None"""
    __tablename__ = 'MACROPOSITIVENEWS'
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


class MEDIASUMMARY(Base):
    """None"""
    __tablename__ = 'MEDIASUMMARY'
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


class MOFCOMNEWS(Base):
    """None"""
    __tablename__ = 'MOFCOMNEWS'
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


class NEEQADMPERMITSCHEDULE(Base):
    """股转系统公司行政许可事项进度表"""
    __tablename__ = 'NEEQADMPERMITSCHEDULE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司ID')
    ANNDATE = Column(VARCHAR(8), comment='公告日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    TYPE_NAME = Column(VARCHAR(300), comment='申请事项')
    TYPE_CODE = Column(Numeric(9, 0), comment='审核类型代码')
    APPLY_PICKUP_DATE = Column(VARCHAR(8), comment='申请材料接收日')
    NOTICE_CORRECTION_DATE = Column(VARCHAR(8), comment='通知补正日')
    RECEIVE_CORRECTION_MATERIAL = Column(VARCHAR(8), comment='接收补正材料日')
    ADMISSIBILITY_DATE = Column(VARCHAR(8), comment='受理决定日')
    NO_ADMISSIBILITY_DATE = Column(VARCHAR(8), comment='不予受理决定日')
    FEEDBACK_DATE1 = Column(VARCHAR(8), comment='第一次反馈意见日')
    RECEIVE_FEEDBACK_DATE1 = Column(VARCHAR(8), comment='接收第一次反馈材料日')
    FEEDBACK_DATE2 = Column(VARCHAR(8), comment='第二次反馈意见日')
    RECEIVE_FEEDBACK_DATE2 = Column(VARCHAR(8), comment='接收第二次反馈材料日')
    REVIEW_DATE = Column(VARCHAR(8), comment='审查决定日')
    MEMO = Column(VARCHAR(1000), comment='说明')
    COMP_NAME = Column(VARCHAR(300), comment='申请人名称')
    PROGRESS_CODE = Column(Numeric(9, 0), comment='审核进度代码')
    ANN_DATE_NDRC = Column(VARCHAR(8), comment='审结日期')
    AUDIT_EVENT_ID = Column(VARCHAR(40), comment='审核事件ID')
    AUDIT_CHANNEL_CODE = Column(Numeric(9, 0), comment='审核通道代码')
    FEEDBACK_DATE = Column(VARCHAR(8), comment='反馈回复日期')
    OTHER_COMP_ID = Column(VARCHAR(10), comment='其他公司ID')
    OTHER_COMP_TYPE_CODE = Column(Numeric(9, 0), comment='其他公司类型代码')


class NEEQEEQUITYPLEDGE(Base):
    """股转系统公司股权质押"""
    __tablename__ = 'NEEQEEQUITYPLEDGE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_PLEDGE_BGDATE = Column(VARCHAR(8), comment='质押起始时间')
    S_PLEDGE_ENDDATE = Column(VARCHAR(8), comment='质押结束时间')
    S_HOLDER_NAME = Column(VARCHAR(100), comment='股东名称')
    S_PLEDGE_SHARES = Column(Numeric(20, 4), comment='质押数量(万股)')
    S_PLEDGOR = Column(VARCHAR(200), comment='质押方')
    S_DISCHARGE_DATE = Column(VARCHAR(8), comment='解押日期')
    S_REMARK = Column(VARCHAR(1000), comment='备注')
    IS_DISCHARGE = Column(Numeric(1, 0), comment='是否解押')
    S_HOLDER_TYPE_CODE = Column(Numeric(9, 0), comment='股东类型代码')
    S_HOLDER_ID = Column(VARCHAR(10), comment='股东ID')
    S_PLEDGOR_TYPE_CODE = Column(Numeric(9, 0), comment='质押方类型代码')
    S_PLEDGOR_ID = Column(VARCHAR(10), comment='质押方ID')
    S_SHR_CATEGORY_CODE = Column(Numeric(9, 0), comment='股份性质类别代码')
    S_TOTAL_HOLDING_SHR = Column(Numeric(20, 4), comment='持股总数')
    S_TOTAL_PLEDGE_SHR = Column(Numeric(20, 4), comment='累计质押股数')
    S_PLEDGE_SHR_RATIO = Column(Numeric(20, 4), comment='本次质押股数占公司总股本比例')
    S_TOTAL_HOLDING_SHR_RATIO = Column(Numeric(20, 4), comment='持股总数占公司总股本比例')
    IS_EQUITY_PLEDGE_REPO = Column(Numeric(1, 0), comment='是否股权质押回购')


class NEEQEODDERIVATIVEINDICATOR(Base):
    """股转系统日行情估值指标"""
    __tablename__ = 'NEEQEODDERIVATIVEINDICATOR'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_TURN = Column(Numeric(20, 4), comment='换手率(%)')
    S_VAL_MV = Column(Numeric(20, 4), comment='当日总市值')
    S_DQ_MV = Column(Numeric(20, 4), comment='当日流通市值')
    S_PQ_HIGH_52W_ = Column(Numeric(20, 4), comment='52周最高价')
    S_PQ_LOW_52W_ = Column(Numeric(20, 4), comment='52周最低价')
    S_VAL_PE = Column(Numeric(20, 4), comment='市盈率(PE)')
    S_VAL_PB_NEW = Column(Numeric(20, 4), comment='市净率(PB)')
    S_VAL_PE_TTM = Column(Numeric(20, 4), comment='市盈率(PE,TTM)')
    S_VAL_PCF_OCF = Column(Numeric(20, 4), comment='市现率(PCF,经营现金流)')
    S_VAL_PCF_OCFTTM = Column(Numeric(20, 4), comment='市现率(PCF,经营现金流TTM)')
    S_VAL_PS = Column(Numeric(20, 4), comment='市销率(PS)')
    S_VAL_PS_TTM = Column(Numeric(20, 4), comment='市销率(PS,TTM)')
    S_DQ_FREETURNOVER = Column(Numeric(20, 4), comment='换手率(基准.自由流通股本)')
    TOT_SHR_TODAY = Column(Numeric(24, 8), comment='当日总股本')
    FLOAT_A_SHR_TODAY = Column(Numeric(24, 8), comment='当日流通股本')
    FREE_SHARES_TODAY = Column(Numeric(24, 8), comment='当日自由流通股本')
    NET_PROFIT_PARENT_COMP_TTM = Column(Numeric(20, 4), comment='归属母公司净利润(TTM)')
    NET_PROFIT_PARENT_COMP_LYR = Column(Numeric(20, 4), comment='归属母公司净利润(LYR)')
    NET_ASSETS_TODAY = Column(Numeric(20, 4), comment='当日净资产')
    NET_CASH_FLOWS_OPER_ACT_TTM = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额(TTM)')
    NET_CASH_FLOWS_OPER_ACT_LYR = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额(LYR)')
    S_DQ_CLOSE_TODAY = Column(Numeric(20, 4), comment='收盘价')
    OPER_REV_TTM = Column(Numeric(20, 4), comment='营业收入(TTM)')
    OPER_REV_LYR = Column(Numeric(20, 4), comment='营业收入(LYR)')
    NET_INCR_CASH_CASH_EQU_TTM = Column(Numeric(20, 4), comment='现金及现金等价物净增加额(TTM)')
    NET_INCR_CASH_CASH_EQU_LYR = Column(Numeric(20, 4), comment='现金及现金等价物净增加额(LYR)')
    S_VAL_PCF_NCF = Column(Numeric(20, 4), comment='市现率(PCF,现金净流量)')
    S_VAL_PCF_NCFTTM = Column(Numeric(20, 4), comment='市现率(PCF,现金净流量TTM)')
    CRNCY_CODE2 = Column(VARCHAR(10), comment='货币代码2')


class NEEQGRADATION(Base):
    """股转系统股票分层分类"""
    __tablename__ = 'NEEQGRADATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码')
    WIND_SEC_CODE = Column(VARCHAR(50), comment='板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class NEEQILLEGALITY(Base):
    """股转系统违规事件"""
    __tablename__ = 'NEEQILLEGALITY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ILLEG_TYPE = Column(VARCHAR(100), comment='违规类型')
    SUBJECT_TYPE = Column(Numeric(9, 0), comment='违规主体类别代码')
    SUBJECT = Column(VARCHAR(200), comment='违规主体名称')
    RELATION_TYPE = Column(Numeric(9, 0), comment='与公告公司的关系类型代码')
    BEHAVIOR = Column(TEXT(2147483647), comment='违规行为')
    DISPOSAL_DT = Column(VARCHAR(8), comment='处罚日期')
    DISPOSAL_TYPE = Column(VARCHAR(100), comment='处分类型')
    S_INFO_METHOD = Column(VARCHAR(2000), comment='处分措施')
    PROCESSOR = Column(VARCHAR(200), comment='处理人')
    AMOUNT = Column(Numeric(20, 4), comment='处罚金额(元)')
    BAN_YEAR = Column(Numeric(20, 4), comment='市场禁入期限(年)')
    REF_RULE = Column(VARCHAR(1000), comment='相关法规')


class NEEQINDEXDESCRIPTION(Base):
    """股转系统指数基本资料"""
    __tablename__ = 'NEEQINDEXDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象id')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(100), comment='指数简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='指数全称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_PUBLISHER = Column(VARCHAR(100), comment='发布方')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    EXPIRE_DATE = Column(VARCHAR(8), comment='终止发布日期')
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8), comment='基期')
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4), comment='基点')
    S_INFO_INDEXCODE = Column(Numeric(9, 0), comment='指数类别代码')
    S_INFO_INDEXSTYLE = Column(VARCHAR(40), comment='指数风格')
    INDEX_INTRO = Column(VARCHAR, comment='指数简介')
    INCOME_PROCESSING_METHOD = Column(VARCHAR(20), comment='收益处理方式')
    S_INFO_INDEXTYPE = Column(VARCHAR(40), comment='指数类别')


class NEEQINDEXEODPRICES(Base):
    """股转系统指数日行情"""
    __tablename__ = 'NEEQINDEXEODPRICES'
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


class NEEQINSIDEHOLDER(Base):
    """股转系统公司前十大股东"""
    __tablename__ = 'NEEQINSIDEHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_HOLDER_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_HOLDER_HOLDERCATEGORY = Column(VARCHAR(1), comment='[内部]股东类型')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='公司名称')
    S_HOLDER_ANAME = Column(VARCHAR(200), comment='股东名称')
    S_INFO_COMPCODE2 = Column(VARCHAR(40), comment='股东ID(容错)')
    S_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='持股数量')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例(%)')
    S_HOLDER_SHARECATEGORY = Column(VARCHAR(40), comment='股本性质代码')
    S_HOLDER_SHARECATEGORYNAME = Column(VARCHAR(40), comment='持股性质')
    S_HOLDER_RESTRICTEDQUANTITY = Column(Numeric(20, 4), comment='持有限售股份(非流通股)数量')
    S_HOLDER_MEMO = Column(VARCHAR(2000), comment='股东说明')
    S_HOLDER_SEQUENCE = Column(VARCHAR(200), comment='关联方序号')


class NEEQREGINV(Base):
    """股转系统立案调查"""
    __tablename__ = 'NEEQREGINV'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SUR_INSTITUTE = Column(VARCHAR(100), comment='调查机构')
    SUR_REASONS = Column(VARCHAR(500), comment='调查原因')
    STR_ANNDATE = Column(VARCHAR(8), comment='开始公告日期')
    END_ANNDATE = Column(VARCHAR(8), comment='结束公告日期')
    STR_DATE = Column(VARCHAR(8), comment='开始日期')


class NEEQSAGENCY(Base):
    """股转系统股票发行中介机构"""
    __tablename__ = 'NEEQSAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_AGENCY_NAME = Column(VARCHAR(200), comment='机构名称')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    S_BUSINESS_TYPCODE = Column(Numeric(9, 0), comment='业务类型代码')
    S_AGENCY_NAMEID = Column(VARCHAR(200), comment='中介机构公司ID')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class NEEQSCAPITALIZATION(Base):
    """股转系统公司股本"""
    __tablename__ = 'NEEQSCAPITALIZATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期(上市日)')
    S_SHARE_CHANGEREASON = Column(VARCHAR(30), comment='变动原因代码')
    TOT_SHR = Column(Numeric(20, 4), comment='总股本(普通股)')
    S_SHARE_OTCA = Column(Numeric(20, 4), comment='流通三板股(万股)')
    S_SHARE_OTCB = Column(Numeric(20, 4), comment='三板B股(万股)')
    S_SHARE_NTRD_STATE_PCT = Column(Numeric(20, 4), comment='非流通股(国有股)')
    S_SHARE_NTRD_STATE = Column(Numeric(20, 4), comment='非流通股(国家股)')
    S_SHARE_NTRD_STATJUR = Column(Numeric(20, 4), comment='非流通股(国有法人股)')
    S_SHARE_NTRD_SUBDOMESJUR = Column(Numeric(20, 4), comment='非流通股(境内法人股)')
    S_SHARE_NTRD_DOMESINITOR = Column(Numeric(20, 4), comment='非流通股(境内法人股:境内发起人股)')
    S_SHARE_NTRD_GENJURIS = Column(Numeric(20, 4), comment='非流通股(境内法人股:一般法人股)')
    S_SHARE_NTRD_STRTINVESTOR = Column(Numeric(20, 4), comment='非流通股(境内法人股:战略投资者持股)')
    S_SHARE_NTRD_IPOINIP = Column(Numeric(20, 4), comment='非流通股(自然人股)')
    S_SHARE_NTRD_NONLSTFRGN = Column(Numeric(20, 4), comment='非流通股(非上市外资股)')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DT1 = Column(VARCHAR(8), comment='变动日期(除权日)')
    USED = Column(Numeric(5, 0), comment='[内部]是否有效')
    CUR_SIGN = Column(Numeric(5, 0), comment='最新标志')
    CHANGE_ORDER = Column(Numeric(20, 4), comment='变动次序')
    S_OTC_CIRCULATION_HOLDER = Column(Numeric(20, 4), comment='三板流通股(控股股东或实际控制人)(万股)')
    S_SHARE_NTRD_SNORMNGER = Column(Numeric(20, 4), comment='流通股(高管持股)(万股)')
    S_OTC_CIRCULATION_CORESTAFF = Column(Numeric(20, 4), comment='三板流通股(核心员工)(万股)')
    S_OTC_CIRCULATION_OTHER = Column(Numeric(20, 4), comment='三板流通股(其他)(万股)')
    S_OTC_RESTRICTED = Column(Numeric(20, 4), comment='三板限售股(万股)')
    S_OTC_RESTRICTED_HOLDER = Column(Numeric(20, 4), comment='三板限售股(控股股东或实际控制人)(万股)')
    S_SHARE_RTD_SENMANAGER = Column(Numeric(20, 4), comment='限售股份(高管持股)(万股)')
    S_OTC_RESTRICTED_CORESTAFF = Column(Numeric(20, 4), comment='三板限售股(核心员工)(万股)')
    S_OTC_RESTRICTED_OTHER = Column(Numeric(20, 4), comment='三板限售股(其他)(万股)')
    S_SHARE_NTRD_PRFSHARE = Column(Numeric(20, 4), comment='优先股(万股)')


class NEEQSCHANGEWINDCODE(Base):
    """中国股转系统Wind代码变更表"""
    __tablename__ = 'NEEQSCHANGEWINDCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后代码')
    CHANGE_DATE = Column(VARCHAR(10), comment='代码变更日期')


class NEEQSCODEANDSNAME(Base):
    """中国股转系统业务代码及简称"""
    __tablename__ = 'NEEQSCODEANDSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='品种ID')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务代码类型')
    S_CODE = Column(VARCHAR(40), comment='业务代码')
    S_SNAME = Column(VARCHAR(100), comment='业务简称')
    IS_COMMON = Column(Numeric(1, 0), comment='是否通用代码')
    MEMO = Column(VARCHAR(800), comment='业务说明')


class NEEQSCOMPRESTRICTED(Base):
    """股转系统限售股解禁公司明细"""
    __tablename__ = 'NEEQSCOMPRESTRICTED'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='可流通日期')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    S_SHARE_LSTTYPECODE = Column(Numeric(9, 0), comment='股份类型代码')
    S_SHARE_LSTTYPENAME = Column(VARCHAR(200), comment='股份类型')
    S_SHARE_LST = Column(Numeric(20, 4), comment='可流通数量(股)')
    S_SHARE_RATIO = Column(Numeric(20, 4), comment='可流通数量占总股本比例(%)')
    S_SHARE_PLACEMENT_ENDDT = Column(VARCHAR(8), comment='配售截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class NEEQSDESCRIPTION(Base):
    """股转系统股票基本资料"""
    __tablename__ = 'NEEQSDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_PINYIN = Column(VARCHAR(40), comment='简称拼音')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所代码')
    S_INFO_LISTBOARD = Column(VARCHAR(10), comment='上市板代码')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市时间')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='摘牌日期')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')


class NEEQSDESCRIPTIONZL(Base):
    """股转系统股票基本资料(增量)"""
    __tablename__ = 'NEEQSDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券简称')
    S_INFO_PINYIN = Column(VARCHAR(40), comment='简称拼音')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所代码')
    S_INFO_LISTBOARD = Column(VARCHAR(10), comment='上市板代码')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市时间')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='摘牌日期')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')


class NEEQSDIVIDEND(Base):
    """股转系统股票分红"""
    __tablename__ = 'NEEQSDIVIDEND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DIV_PROGRESS = Column(VARCHAR(10), comment='方案进度')
    STK_DVD_PER_SH = Column(Numeric(20, 4), comment='每股送转')
    CASH_DVD_PER_SH_PRE_TAX = Column(Numeric(20, 8), comment='每股派息(税前)(元)')
    CASH_DVD_PER_SH_AFTER_TAX = Column(Numeric(20, 8), comment='每股派息(税后)(元)')
    EQY_RECORD_DT = Column(VARCHAR(8), comment='股权登记日/B股最后交易日')
    EX_DT = Column(VARCHAR(8), comment='除权除息日')
    DVD_PAYOUT_DT = Column(VARCHAR(8), comment='派息日')
    LISTING_DT_OF_DVD_SHR = Column(VARCHAR(8), comment='红股上市日期')
    S_DIV_PRELANDATE = Column(VARCHAR(8), comment='预案公告日')
    S_DIV_SMTGDATE = Column(VARCHAR(8), comment='股东大会公告日')
    DVD_ANN_DT = Column(VARCHAR(8), comment='分红实施公告日')
    S_DIV_BASEDATE = Column(VARCHAR(8), comment='股本基准日期')
    S_DIV_BASESHARE = Column(Numeric(20, 4), comment='基准股本(万股)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    IS_CHANGED = Column(Numeric(5, 0), comment='方案曾经变更')
    REPORT_PERIOD = Column(VARCHAR(8), comment='分红年度')
    S_DIV_CHANGE = Column(VARCHAR(500), comment='方案变更说明')
    S_DIV_BONUSRATE = Column(Numeric(20, 8), comment='每股送股比例')
    S_DIV_CONVERSEDRATE = Column(Numeric(20, 8), comment='每股转增比例')


class NEEQSEODPRICES(Base):
    """股转系统股票日行情"""
    __tablename__ = 'NEEQSEODPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='最新价')
    S_DQ_CHANGE = Column(Numeric(20, 4), comment='涨跌(元)')
    S_DQ_PCTCHANGE = Column(Numeric(20, 4), comment='涨跌幅(%)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    S_DQ_ADJPRECLOSE = Column(Numeric(20, 4), comment='复权昨收盘价')
    S_DQ_ADJOPEN = Column(Numeric(20, 4), comment='复权开盘价')
    S_DQ_ADJHIGH = Column(Numeric(20, 4), comment='复权最高价')
    S_DQ_ADJLOW = Column(Numeric(20, 4), comment='复权最低价')
    S_DQ_ADJCLOSE = Column(Numeric(20, 4), comment='复权收盘价')
    S_DQ_ADJFACTOR = Column(Numeric(20, 6), comment='复权因子')
    S_DQ_AVGPRICE = Column(Numeric(20, 4), comment='平均价')
    S_DQ_TRADESTATUS = Column(VARCHAR(10), comment='[内部]交易状态代码')
    S_DQ_TURN = Column(Numeric(20, 4), comment='换手率')


class NEEQSEVENTDATEINFORMATION(Base):
    """股转系统事件日期信息"""
    __tablename__ = 'NEEQSEVENTDATEINFORMATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EVENT_TYPE = Column(Numeric(8, 0), comment='事件类型编号')
    OCCURRENCE_DATE = Column(VARCHAR(8), comment='发生日期')
    DISCLOSURE_DATE = Column(VARCHAR(8), comment='披露日期')
    MEMO = Column(VARCHAR(2000), comment='内容说明')
    DATE_CREATED = Column(VARCHAR(8), comment='创建日期')
    S_INFO_CODE = Column(VARCHAR(10), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券简称')
    TYPE_CODE = Column(VARCHAR(10), comment='证券类型代码')
    LANGUAGE1 = Column(VARCHAR(10), comment='语言')
    EQY_RECORD_DT = Column(VARCHAR(8), comment='权益登记日')


class NEEQSGUARANTEE(Base):
    """股转系统担保事件"""
    __tablename__ = 'NEEQSGUARANTEE'
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


class NEEQSINDUSTRIESCODE(Base):
    """股转系统行业代码"""
    __tablename__ = 'NEEQSINDUSTRIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='板块代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='板块名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')
    USED = Column(Numeric(1, 0), comment='是否使用')
    INDUSTRIESALIAS = Column(VARCHAR(12), comment='板块别名')
    SEQUENCE1 = Column(Numeric(4, 0), comment='展示序号')
    MEMO = Column(VARCHAR(100), comment='[内部]备注')
    CHINESEDEFINITION = Column(VARCHAR(600), comment='板块中文定义')


class NEEQSINTRODUCTION(Base):
    """股转系统公司简介"""
    __tablename__ = 'NEEQSINTRODUCTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    S_INFO_COMPNAMEENG = Column(VARCHAR(200), comment='英文名称')
    S_INFO_COUNTRY = Column(VARCHAR(20), comment='国家及地区')
    S_INFO_PROVINCE = Column(VARCHAR(20), comment='省份')
    S_INFO_CITY = Column(VARCHAR(30), comment='城市')
    S_INFO_CHAIRMAN = Column(VARCHAR(40), comment='法人代表')
    S_INFO_PRESIDENT = Column(VARCHAR(40), comment='总经理')
    S_INFO_BDSECRETARY = Column(VARCHAR(500), comment='董事会秘书')
    S_INFO_REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    S_INFO_FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    S_INFO_WEBSITE = Column(VARCHAR(160), comment='主页')
    S_INFO_EMAIL = Column(VARCHAR(160), comment='电子邮箱')
    S_INFO_OFFICE = Column(VARCHAR(800), comment='办公地址')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_BUSINESSSCOPE = Column(TEXT(2147483647), comment='经营范围')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    S_INFO_CHINESEINTRODUCTION = Column(VARCHAR(2000), comment='公司简介')


class NEEQSINTRODUCTIONZL(Base):
    """股转系统公司简介(增量)"""
    __tablename__ = 'NEEQSINTRODUCTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMPNAMEENG = Column(VARCHAR(100), comment='英文名称')
    S_INFO_COUNTRY = Column(VARCHAR(20), comment='国家及地区')
    S_INFO_PROVINCE = Column(VARCHAR(20), comment='省份')
    S_INFO_CITY = Column(VARCHAR(30), comment='城市')
    S_INFO_CHAIRMAN = Column(VARCHAR(40), comment='法人代表')
    S_INFO_PRESIDENT = Column(VARCHAR(40), comment='总经理')
    S_INFO_BDSECRETARY = Column(VARCHAR(500), comment='董事会秘书')
    S_INFO_REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    S_INFO_FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    S_INFO_WEBSITE = Column(VARCHAR(80), comment='主页')
    S_INFO_EMAIL = Column(VARCHAR(80), comment='电子邮箱')
    S_INFO_OFFICE = Column(VARCHAR(200), comment='办公地址')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_BUSINESSSCOPE = Column(VARCHAR(3400), comment='经营范围')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    S_INFO_CHINESEINTRODUCTION = Column(VARCHAR(2000), comment='公司简介')


class NEEQSIPO(Base):
    """股转系统首次公开发行数据"""
    __tablename__ = 'NEEQSIPO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_IPO_PRICE = Column(Numeric(20, 4), comment='发行价格(元)')
    S_IPO_PRE_DILUTEDPE = Column(Numeric(20, 4), comment='发行市盈率(发行前股本)')
    S_IPO_DILUTEDPE = Column(Numeric(20, 4), comment='发行市盈率(发行后股本)')
    S_IPO_AMOUNT = Column(Numeric(20, 4), comment='公开及老股发行数量合计(万股)')
    S_IPO_AMTBYPLACING = Column(Numeric(20, 4), comment='网上发行数量(万股)')
    S_IPO_AMTTOJUR = Column(Numeric(20, 4), comment='网下发行数量(万股)')
    S_IPO_COLLECTION = Column(Numeric(20, 4), comment='募集资金(万元)')
    S_IPO_CASHRATIO = Column(Numeric(20, 8), comment='网上发行中签率(%)')
    S_IPO_PURCHASECODE = Column(VARCHAR(10), comment='网上申购代码')
    S_IPO_SUBDATE = Column(VARCHAR(8), comment='申购日')
    S_IPO_JURISDATE = Column(VARCHAR(8), comment='向一般法人配售上市日期')
    S_IPO_INSTISDATE = Column(VARCHAR(8), comment='向战略投资者配售部分上市日期')
    S_IPO_EXPECTLISTDATE = Column(VARCHAR(8), comment='预计上市日期')
    S_IPO_FUNDVERIFICATIONDATE = Column(VARCHAR(8), comment='申购资金验资日')
    S_IPO_RATIODATE = Column(VARCHAR(8), comment='中签率公布日')
    S_FELLOW_UNFROZEDATE = Column(VARCHAR(8), comment='申购资金解冻日')
    S_IPO_LISTDATE = Column(VARCHAR(8), comment='上市日')
    S_IPO_PUBOFFRDATE = Column(VARCHAR(8), comment='招股公告日')
    S_IPO_ANNCEDATE = Column(VARCHAR(8), comment='发行公告日')
    S_IPO_ANNCELSTDATE = Column(VARCHAR(8), comment='上市公告日')
    S_IPO_ROADSHOWSTARTDATE = Column(VARCHAR(8), comment='初步询价(预路演)起始日期')
    S_IPO_ROADSHOWENDDATE = Column(VARCHAR(8), comment='初步询价(预路演)终止日期')
    S_IPO_PLACINGDATE = Column(VARCHAR(8), comment='网下配售发行公告日')
    S_IPO_APPLYSTARTDATE = Column(VARCHAR(8), comment='网下申购起始日期')
    S_IPO_APPLYENDDATE = Column(VARCHAR(8), comment='网下申购截止日期')
    S_IPO_PRICEANNOUNCEDATE = Column(VARCHAR(8), comment='网下定价公告日')
    S_IPO_PLACINGRESULTDATE = Column(VARCHAR(8), comment='网下配售结果公告日')
    S_IPO_FUNDENDDATE = Column(VARCHAR(8), comment='网下申购资金到帐截止日')
    S_IPO_CAPVERIFICATIONDATE = Column(VARCHAR(8), comment='网下验资日')
    S_IPO_REFUNDDATE = Column(VARCHAR(8), comment='网下多余款项退还日')
    S_IPO_EXPECTEDCOLLECTION = Column(Numeric(20, 4), comment='预计募集资金(万元)')
    S_IPO_LIST_FEE = Column(Numeric(20, 4), comment='发行费用(万元)')
    S_IPO_CASHAMTUPLIMIT = Column(Numeric(10, 0), comment='申购上限(机构)')
    S_IPO_CASHMONEYUPLIMIT = Column(Numeric(20, 4), comment='申购金额上限(机构)')
    S_IPO_NAMEBYPLACING = Column(VARCHAR(20), comment='网上发行简称')
    S_IPO_SHOWPRICEDOWNLIMIT = Column(Numeric(20, 4), comment='投标询价申购价格下限')
    S_IPO_PAR = Column(Numeric(24, 8), comment='面值')
    S_IPO_PURCHASEUPLIMIT = Column(Numeric(20, 4), comment='网上申购上限(个人)（股）')
    S_IPO_OP_UPLIMIT = Column(Numeric(20, 4), comment='网下申购上限（万股）')
    S_IPO_OP_DOWNLIMIT = Column(Numeric(20, 4), comment='网下申购下限（万股）')
    S_IPO_PURCHASEMV_DT = Column(VARCHAR(8), comment='网上市值申购登记日')
    S_IPO_PUBOSDTOTISSCOLL = Column(Numeric(20, 4), comment='公开及原股东募集资金总额')
    S_IPO_OSDEXPOFFAMOUNT = Column(Numeric(20, 4), comment='新股发行数量')
    S_IPO_OSDEXPOFFAMOUNTUP = Column(Numeric(20, 4), comment='原股东预计售股数量上限')
    S_IPO_OSDACTOFFAMOUNT = Column(Numeric(20, 4), comment='原股东实际售股数量')
    S_IPO_OSDACTOFFPRICE = Column(Numeric(20, 4), comment='原股东实际售股金额')
    S_IPO_OSDUNDERWRITINGFEES = Column(Numeric(20, 4), comment='原股东应摊承销费用')
    S_IPO_PUREFFSUBRATIO = Column(Numeric(20, 4), comment='网上投资者有效认购倍数')
    S_IPO_REPORATE = Column(Numeric(20, 4), comment='回拨比例')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日期')
    IS_FAILURE = Column(Numeric(5, 0), comment='是否发行失败')
    S_IPO_OTC_CASH_PCT = Column(Numeric(24, 8), comment='网下申购配售比例')
    MIN_APPLYUNIT = Column(Numeric(20, 4), comment='最低累进申购数量(万股)')
    MV_CALCULATION_DATE = Column(VARCHAR(8), comment='市值计算参考日')
    S_IPO_MV_THRESHOLD = Column(Numeric(20, 4), comment='网下询价市值门槛')
    S_IPO_PAYMENTDATE = Column(VARCHAR(8), comment='网上申购缴款日')
    S_FELLOW_ISSUETYPE = Column(VARCHAR(40), comment='发行方式')
    S_VAL_PE = Column(Numeric(20, 4), comment='行业PE')
    S_IPO_NEW_FACEVALUE = Column(Numeric(24, 8), comment='最新每股面值')
    S_IPO_MV_THRESHOLD_A = Column(Numeric(20, 4), comment='网下询价市值门槛(A类)(万元)')
    S_INFO_UNDERWRITING = Column(VARCHAR(30), comment='承销方式')
    ONLINE_EFFECTIVE_NUMBER = Column(Numeric(10, 0), comment='网上发行有效申购户数')
    ONLINE_EFFECTIVE_QUANTITY = Column(Numeric(20, 4), comment='网上发行有效申购数量')
    S_INFO_OVRSUBRATIO = Column(Numeric(20, 4), comment='超额认购倍数')
    EFFECTIVE_QUOTE_OVRSUBRATIO = Column(Numeric(20, 4), comment='初步询价有效报价对应的超额认购倍数')
    UNDER_SUBSCRIPTION = Column(Numeric(20, 4), comment='网下超额认购倍数')
    APPLICATIONDEADLINE = Column(VARCHAR(8), comment='网下报备截止日')
    APPLICATIONDEADLINE_TIME = Column(VARCHAR(20), comment='网下报备截止时间')
    STRATEGY_PLACING_QUANTITY = Column(Numeric(20, 4), comment='向战略投资者配售数量(万股)')
    OFFLINE_RELEASES_NUM = Column(Numeric(20, 4), comment='网下发行数量')
    S_IPO_MV_THRESHOLD_STIB = Column(Numeric(20, 4), comment='网下询价市值门槛(科创主题与战略)(万元)')
    S_IPO_COMMISSION_RATE = Column(Numeric(20, 4), comment='新股配售经纪佣金费率')
    S_PLACING_RESULT_ANN_DAY = Column(VARCHAR(8), comment='初步配售结果公告日')
    BALANCE_SUB_QUANTITY = Column(Numeric(20, 4), comment='承销商余额认购数量(万股)')
    PRELIMINARY_INQUIRY_LOWER = Column(Numeric(20, 4), comment='初步询价报价结果下限')
    PRELIMINARY_INQUIRY_UPPER = Column(Numeric(20, 4), comment='初步询价报价结果上限')
    EXCLUDE_HIGHEST_BID_LIMIT = Column(Numeric(20, 4), comment='剔除的最高报价下限(含)')
    EXCLUDE_HIGHEST_BID_OFFER = Column(Numeric(20, 4), comment='剔除的最高报价的申购量')
    PREL_INQ_ANN_DT = Column(VARCHAR(8), comment='初步询价公告日')
    PREL_INQ_RESULT_ANN_DT = Column(VARCHAR(8), comment='初步询价结果公告日')
    IS_ADDUP_SHOWPRICE = Column(Numeric(5, 0), comment='是否进行累计投标询价')


class NEEQSIPOINQUIRYDETAILS(Base):
    """股转系统IPO初步询价明细"""
    __tablename__ = 'NEEQSIPOINQUIRYDETAILS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    INQUIRER = Column(VARCHAR(100), comment='询价对象名称')
    INQUIRERID = Column(VARCHAR(40), comment='询价对象名称ID')
    INQUIRER_TYPECODE = Column(Numeric(9, 0), comment='投资者类别代码')
    ISSUETARGET = Column(VARCHAR(100), comment='配售对象名称')
    DEDAREDPRICE = Column(Numeric(20, 4), comment='申报价格(元/股)')
    DEDAREDSHARES = Column(Numeric(20, 4), comment='申购数量(万股)')
    IS_VALID = Column(Numeric(1, 0), comment='是否有效报价投资者')
    ISSUETARGET1 = Column(VARCHAR(100), comment='配售对象名称')
    PCT_CHANGE_1M = Column(Numeric(20, 4), comment='配售数量')
    ISSUETARGETID = Column(VARCHAR(10), comment='配售对象名称ID')
    REJECT_DEDAREDSHARES = Column(Numeric(20, 4), comment='被剔除申购股数(万股)')
    ACT_DEDAREDSHARES = Column(Numeric(20, 4), comment='实际申购数量(万股)')


class NEEQSLEADUNDERWRITER(Base):
    """股转系统发行主承销商"""
    __tablename__ = 'NEEQSLEADUNDERWRITER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_LU_ANNISSUEDATE = Column(VARCHAR(8), comment='发行公告日')
    S_LU_ISSUEDATE = Column(VARCHAR(8), comment='发行日期')
    S_LU_ISSUETYPE = Column(VARCHAR(1), comment='发行类型')
    S_LU_TOTALISSUECOLLECTION = Column(Numeric(20, 4), comment='募集资金合计(万元)')
    S_LU_TOTALISSUEEXPENSES = Column(Numeric(20, 4), comment='发行费用合计(万元)')
    S_LU_TOTALUDERANDSPONEFEE = Column(Numeric(20, 4), comment='承销与保荐费用(万元)')
    S_LU_NUMBER = Column(VARCHAR(1), comment='参与主承销商个数')
    S_LU_NAME_ANN = Column(VARCHAR(100), comment='参与主承销商公布名称')
    S_LU_NAME = Column(VARCHAR(100), comment='参与主承销商名称')
    S_LU_INSTITYPE = Column(VARCHAR(40), comment='主承销商类型')
    S_LU_AUX_TYPE = Column(VARCHAR(40), comment='辅助类型')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='主承销商id')
    ALL_LU = Column(VARCHAR, comment='全部参与主承销商名称')
    MEETING_DT = Column(VARCHAR(8), comment='发审委会议日期')
    PASS_DT = Column(VARCHAR(8), comment='发审委通过公告日')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    TYPE = Column(VARCHAR(40), comment='发行类型')
    NETCOLLECTION = Column(Numeric(20, 4), comment='募资净额合计(万元)')
    AVG_TOTALCOLL = Column(Numeric(20, 4), comment='募集总额算术平均 (万元)')
    AVG_NETCOLL = Column(Numeric(20, 4), comment='募资净额算术平均 (万元)')


class NEEQSMAJOREVENT(Base):
    """股转系统重大事件表"""
    __tablename__ = 'NEEQSMAJOREVENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_EVENT_CATEGORYCODE = Column(Numeric(9, 0), comment='事件类型代码')
    S_EVENT_ANNCEDATE = Column(VARCHAR(8), comment='披露日期')
    S_EVENT_HAPDATE = Column(VARCHAR(8), comment='发生日期')
    S_EVENT_EXPDATE = Column(VARCHAR(8), comment='失效日期')
    S_EVENT_CONTENT = Column(TEXT(2147483647), comment='事件内容')
    S_EVENT_TEMPLATEID = Column(Numeric(12, 0), comment='模板ID')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class NEEQSPLACEDETAILSADDOFF(Base):
    """股转系统增发配售明细"""
    __tablename__ = 'NEEQSPLACEDETAILSADDOFF'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    END_DATE = Column(VARCHAR(8), comment='配售截止日期')
    INS_ALLOCATION = Column(VARCHAR(100), comment='[内部]获配公司名称')
    INS_TYPE = Column(VARCHAR(20), comment='法人投资者类型')
    PLACEMENT = Column(Numeric(20, 4), comment='获配数量(万股/万张)')
    ISSUE_PRICE = Column(Numeric(20, 4), comment='发行价格')
    LOCKUP_PERIOD = Column(Numeric(20, 4), comment='冻结期限(月)')
    PRICING_RULE = Column(VARCHAR(2000), comment='定价规则')
    AMOUNT_REFUND = Column(Numeric(20, 4), comment='退款或补缴金额')


class NEEQSPLACEMENTDETAILS(Base):
    """股转系统网下配售机构获配明细"""
    __tablename__ = 'NEEQSPLACEMENTDETAILS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    TYPEOFINVESTOR = Column(VARCHAR(20), comment='法人投资者类型')
    PLACEMENT = Column(Numeric(20, 4), comment='获配数量(股)')
    TRADE_DT = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    LOCKMONTH = Column(Numeric(20, 4), comment='锁定期(月)')
    TRADABLE_DT = Column(VARCHAR(8), comment='可流通日期')
    IS_SEOORIPO = Column(Numeric(1, 0), comment='是否增发或首发')
    LATEST_OWN_QTY = Column(Numeric(20, 4), comment='最新持股数量(万股/万张)')
    PLACEMENT_FINANCING = Column(Numeric(20, 4), comment='获配数量(配套融资)')
    MEETEVENT_ID = Column(VARCHAR(40), comment='融资事件ID')
    S_SHARE_LSTTYPENAME = Column(VARCHAR(50), comment='股份类型')


class NEEQSPREVIOUSNAME(Base):
    """股转系统证券曾用名"""
    __tablename__ = 'NEEQSPREVIOUSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券简称')
    CHANGEREASON = Column(Numeric(9, 0), comment='变动原因代码')


class NEEQSPREVIOUSNAMEZL(Base):
    """股转系统证券曾用名(增量)"""
    __tablename__ = 'NEEQSPREVIOUSNAMEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券简称')
    CHANGEREASON = Column(Numeric(9, 0), comment='变动原因代码')


class NEEQSPROSECUTION(Base):
    """股转系统诉讼事件"""
    __tablename__ = 'NEEQSPROSECUTION'
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
    RESULT1 = Column(TEXT(2147483647), comment='判决内容')
    IS_APPEAL = Column(Numeric(5, 0), comment='是否上诉')
    APPELLANT = Column(VARCHAR(1), comment='二审上诉方(是否原告)')
    COURT2 = Column(VARCHAR(200), comment='二审受理法院')
    JUDGE_DT2 = Column(VARCHAR(8), comment='二审判决日期')
    RESULT2 = Column(VARCHAR(2000), comment='二审判决内容')
    RESULTAMOUNT = Column(Numeric(20, 4), comment='判决金额')
    BRIEFRESULT = Column(VARCHAR(100), comment='诉讼结果')
    EXECUTION = Column(TEXT(2147483647), comment='执行情况')
    INTRODUCTION = Column(TEXT(2147483647), comment='案件描述')
    LITIGATION_EVENTS_ID = Column(VARCHAR(40), comment='诉讼事件ID')


class NEEQSSECINDUSTRIESCLASS(Base):
    """股转系统股票证监会行业分类"""
    __tablename__ = 'NEEQSSECINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    WIND_IND_CODE = Column(VARCHAR(50), comment='板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class NEEQSSEO(Base):
    """股转系统股票发行"""
    __tablename__ = 'NEEQSSEO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_FELLOW_PROGRESS = Column(VARCHAR(8), comment='方案进度')
    S_FELLOW_ISSUETYPE = Column(VARCHAR(10), comment='发行方式代码')
    S_FELLOW_OFFERINGOBJECT = Column(VARCHAR(200), comment='发行对象')
    S_SEO_SUBSMODE = Column(Numeric(9, 0), comment='定增认购方式代码')
    S_SEO_HOLDERSUBSMODE = Column(VARCHAR(30), comment='大股东认购方式')
    S_SEO_HOLDERSUBSRATE = Column(Numeric(20, 4), comment='大股东认购比例(%)')
    S_FELLOW_OBJECTIVE_CODE = Column(Numeric(9, 0), comment='定向增发目的代码')
    S_FELLOW_PRICEUPLIMIT = Column(Numeric(20, 4), comment='增发预案价上限(元)')
    S_FELLOW_PRICEDOWNLIMIT = Column(Numeric(20, 4), comment='增发预案价下限(元)')
    S_FELLOW_PRICE = Column(Numeric(20, 4), comment='发行价格(元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_FELLOW_DISCNTRATIO = Column(Numeric(20, 4), comment='折扣率(%)')
    S_FELLOW_AMOUNT = Column(Numeric(20, 4), comment='发行数量(万股)')
    S_FELLOW_ESTICOLLECTION = Column(Numeric(20, 4), comment='预计募集资金(元)')
    S_FELLOW_COLLECTION = Column(Numeric(20, 4), comment='募集资金合计(元)')
    S_FELLOW_YEAR = Column(VARCHAR(8), comment='增发年度')
    S_FELLOW_PREPLANDATE = Column(VARCHAR(8), comment='预案公告日')
    S_FELLOW_SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    S_FELLOW_OFFERINGDATE = Column(VARCHAR(8), comment='增发公告日')
    S_FELLOW_LISTANNDATE = Column(VARCHAR(8), comment='上市公告日')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_FELLOW_DATE = Column(VARCHAR(8), comment='定增发行日期')
    S_FELLOW_INITIAL_PLAN = Column(VARCHAR(8), comment='初始预案公告日')


class NEEQSSHARETRANSFER(Base):
    """股转系统代办股份转让券商"""
    __tablename__ = 'NEEQSSHARETRANSFER'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_RIGHT_ANN_DATE = Column(VARCHAR(8), comment='股份确权公告日')
    S_TRANSFER_ANN_DATE = Column(VARCHAR(8), comment='代办股份转让公告日')
    S_RIGHT_START_DATE = Column(VARCHAR(8), comment='股份确权起始日')
    S_TRANSFER_START_DATE = Column(VARCHAR(8), comment='代办股份开始转让日 ')
    S_HOST_BROKER = Column(VARCHAR(80), comment='主办(报价)券商')
    S_DEPUTY_HOST_BROKER = Column(VARCHAR(200), comment='副主办(报价)券商')
    S_CUSTODIAN = Column(VARCHAR(60), comment='股份登记机构')
    S_TYPE = Column(VARCHAR(60), comment='公司类别')
    S_TRANSFER_A_NUM = Column(Numeric(20, 4), comment='可转让A股数量(万股)')
    S_TRANSFER_B_NUM = Column(Numeric(20, 4), comment='可转让B股数量(万股)')
    S_VALUE = Column(Numeric(20, 4), comment='面值')
    S_LIST_PRICE = Column(Numeric(20, 4), comment='挂牌价')
    S_HOST_BROKER_ID = Column(VARCHAR(10), comment='主办券商ID')


class NEEQST(Base):
    """股转系统特别处理"""
    __tablename__ = 'NEEQST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_TYPE_ST = Column(VARCHAR(8), comment='特别处理类型')
    ENTRY_DT = Column(VARCHAR(8), comment='实施日期')
    REMOVE_DT = Column(VARCHAR(8), comment='撤销日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REASON = Column(VARCHAR(100), comment='实施原因')


class NEEQSTRADETYPEZL(Base):
    """股转系统股票转让方式(增量)"""
    __tablename__ = 'NEEQSTRADETYPEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADETYPECODE = Column(Numeric(9, 0), comment='转让方式代码')
    TRADETYPE = Column(VARCHAR(20), comment='转让方式')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='是否最新')


class NEEQSTYPECODE(Base):
    """股转系统类型编码表"""
    __tablename__ = 'NEEQSTYPECODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_TYPNAME = Column(VARCHAR(300), comment='类型名称')
    S_TYPCODE = Column(VARCHAR(40), comment='类型代码')
    S_ORIGIN_TYPCODE = Column(Numeric(9, 0), comment='类型代码')
    S_CLASSIFICATION = Column(VARCHAR(100), comment='分类')


class NEEQSWINDCUSTOMCODE(Base):
    """股转系统Wind兼容代码"""
    __tablename__ = 'NEEQSWINDCUSTOMCODE'
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


class NEEQWEEKREPORTSOFBROKERS(Base):
    """股转系统券商做市与督导情况统计(周)"""
    __tablename__ = 'NEEQWEEKREPORTSOFBROKERS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    BROKER_ID = Column(VARCHAR(10), comment='券商ID')
    TYPECODE = Column(Numeric(2, 0), comment='周报类型')
    START_DATE = Column(VARCHAR(8), comment='起始日期')
    CLOSING_DATE = Column(VARCHAR(8), comment='截止日期')
    MAKE_MARKET_NUM = Column(Numeric(20, 4), comment='做市企业数量')
    LISTED_COMPANIES_NUM = Column(Numeric(20, 4), comment='累计推荐挂牌企业数量')
    MARKET_MAKING_ENTERPRISE_RATIO = Column(Numeric(20, 4), comment='当周做市企业数量占比')
    TRADING_VOLUME = Column(Numeric(20, 4), comment='当周做市成交量')
    TRADING_VOLUME_RATIO = Column(Numeric(20, 4), comment='当周做市成交量市场占比')
    MARKET_TURNOVER = Column(Numeric(20, 4), comment='当周做市成交额')
    MARKET_TURNOVER_RATIO = Column(Numeric(20, 4), comment='当周做市成交额市场占比')
    REPORT_PERIOD = Column(VARCHAR(8), comment='披露定期报告报告期')
    SUPERVISION_COMPANY_NUM = Column(Numeric(20, 0), comment='持续督导公司家数')
    THIS_PERIOD_DISCLOSURE_NUM = Column(Numeric(20, 0), comment='本期披露定期报告的公司家数')
    ACCUMULATIVE_DISCLOSURE_NUM = Column(Numeric(20, 0), comment='累计披露定期报告的公司家数')
    NOT_YET_DISCLOSURE_NUM = Column(Numeric(20, 0), comment='尚未披露定期报告的公司家数')
    CORRECTIONS_NUM = Column(Numeric(20, 0), comment='定期报告披露后进行更正的公司家数')
    DELAYED_DISCLOSURE_NUM = Column(Numeric(20, 0), comment='延迟披露定期报告的公司家数')
    EXISTING_PROBLEMS_NUM = Column(Numeric(20, 0), comment='定期报告披露督导中存在其他问题的公司家数')


class NOPUBLICSTOCKCOMPRFA(Base):
    """非公开发行股票审核申报企业情况"""
    __tablename__ = 'NOPUBLICSTOCKCOMPRFA'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPANYNAME = Column(VARCHAR(100), comment='公司名称')
    REGADDR = Column(VARCHAR(30), comment='注册地')
    SECTORS = Column(VARCHAR(100), comment='所属行业')
    SPONSOR = Column(VARCHAR(200), comment='保荐机构')
    SPON_REP = Column(VARCHAR(100), comment='保荐代表人')
    ACC_FIRM = Column(VARCHAR(200), comment='会计师事务所')
    CPA = Column(VARCHAR(200), comment='签字会计师')
    LAW_FIRM = Column(VARCHAR(200), comment='律师事务所')
    SOL_SIG = Column(VARCHAR(100), comment='签字律师')
    APP_CODE = Column(Numeric(9, 0), comment='申请事项代码')
    SCH_CODE = Column(Numeric(9, 0), comment='进度类型代码')
    TBLISTED = Column(Numeric(9, 0), comment='拟上市板块代码')
    ST_DATE = Column(VARCHAR(8), comment='状态起始日期')
    END_DATE = Column(VARCHAR(8), comment='状态终止日期')
    EST_ISSUENO = Column(Numeric(24, 8), comment='预计发行股数（万股）')
    EST_ISSUESHARES = Column(Numeric(24, 8), comment='预计发行后总股本（万股）')
    PRO_TOLALINV = Column(Numeric(20, 4), comment='募投项目投资总额')


class OPTIONEMBEDDEDBONDRATE(Base):
    """中国含权债票面利率变动"""
    __tablename__ = 'OPTIONEMBEDDEDBONDRATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    B_INFO_PAYMENTDATE = Column(VARCHAR(8), comment='付息日')
    RATE = Column(Numeric(22, 6), comment='利率(%)')
    CHANGE_DT = Column(VARCHAR(8), comment='基准利率变动日')
    ADD_POINT_NUM = Column(Numeric(20, 4), comment='利率/利差加点数')


class PBCNEWS(Base):
    """None"""
    __tablename__ = 'PBCNEWS'
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


class PLEDGECODE(Base):
    """中国债券质押券代码"""
    __tablename__ = 'PLEDGECODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务类型代码')
    PLEDGE_CODE = Column(VARCHAR(20), comment='质押券代码')
    PLEDGE_NAME = Column(VARCHAR(100), comment='质押券名称')
    IS_VALID = Column(Numeric(1, 0), comment='是否有效')


class POOLINITIALSTATISTICS(Base):
    """资产池初始统计数据"""
    __tablename__ = 'POOLINITIALSTATISTICS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    POOL_NAME = Column(VARCHAR(200), comment='资产池名称')
    DT = Column(VARCHAR(8), comment='日期')
    ITEM_CODE = Column(Numeric(9, 0), comment='统计项目代码')
    TYPE = Column(VARCHAR(200), comment='统计类别')
    TYPE_CODE = Column(Numeric(9, 0), comment='统计指标代码')
    VALUE = Column(Numeric(24, 8), comment='指标数据')
    UNIT = Column(VARCHAR(40), comment='指标单位')


class POOLSTATISTICS(Base):
    """资产池收款期统计特征"""
    __tablename__ = 'POOLSTATISTICS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    POOL_NAME = Column(VARCHAR(200), comment='资产池名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    START_DT = Column(VARCHAR(8), comment='收款期间起始日')
    END_DR = Column(VARCHAR(8), comment='收款期间截止日')
    LAON_BALANCE = Column(Numeric(24, 8), comment='贷款余额(万元)')
    LAON_NUM = Column(Numeric(24, 4), comment='贷款笔数')
    WA_LOANRATE = Column(Numeric(24, 4), comment='加权平均贷款利率')
    WA_REMTM = Column(Numeric(24, 4), comment='加权平均贷款剩余期限（年）')
    CREDIT_NUM = Column(Numeric(24, 4), comment='信用贷款笔数')
    GUARANTEE_NUM = Column(Numeric(24, 4), comment='保证担保贷款笔数')
    CREDIT_PCT = Column(Numeric(24, 4), comment='信用贷款金额占比')
    GUARANTEE_PCT = Column(Numeric(24, 4), comment='保证担保贷款金额占比')
    DEFAUT_VALUE = Column(Numeric(24, 8), comment='累计违约金额（万元）')
    DEFAULT_BACKVALUE = Column(Numeric(24, 8), comment='累计回收违约本金（万元）')
    DEFAULT_RATE = Column(Numeric(24, 4), comment='累计违约率')
    ARREARS_RATE = Column(Numeric(24, 4), comment='严重拖欠率')


class QDIIINDPORTFOLIO(Base):
    """QDII投资组合-行业配置"""
    __tablename__ = 'QDIIINDPORTFOLIO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    IND = Column(VARCHAR(100), comment='行业类别')
    VALUE = Column(Numeric(20, 4), comment='持仓市值(元)')
    PCT_NAV = Column(Numeric(20, 4), comment='占基金资产净值比例(%)')
    GICS_CODE = Column(VARCHAR(10), comment='行业代码')


class QDIISCOPEPORTFOLIO(Base):
    """QDII投资组合-地区配置"""
    __tablename__ = 'QDIISCOPEPORTFOLIO'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象id')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    SCOPE = Column(VARCHAR(10), comment='国家（地区)代码')
    VALUE = Column(Numeric(20, 4), comment='市值(元)')
    POSSTKTONAV = Column(Numeric(20, 4), comment='占净资产的比例(%)')


class QDIISECURITIESPORTFOLIO(Base):
    """QDII投资组合-持券配置"""
    __tablename__ = 'QDIISECURITIESPORTFOLIO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    TYPE = Column(VARCHAR(20), comment='投资证券类型')
    INVESTCODE = Column(VARCHAR(20), comment='投资证券代码')
    NAME = Column(VARCHAR(100), comment='投资证券名称')
    COMP_NAME = Column(VARCHAR(100), comment='投资证券公司名称')
    LISTSCOPE = Column(VARCHAR(20), comment='投资证券上市地代码')
    S_INFO_INVESTWINDCODE = Column(VARCHAR(40), comment='投资证券Wind代码')
    QUANTITY = Column(Numeric(20, 4), comment='数量(股/份)')
    VALUE = Column(Numeric(20, 4), comment='市值(元)')
    POSSTKTONAV = Column(Numeric(20, 4), comment='占净资产的比例')
    INVESTFUNDCODE = Column(VARCHAR(20), comment='投资基金的类型')
    INVESTFUNDTYPE = Column(VARCHAR(20), comment='投资基金的运作方式')
    FUNDMANAGEMENTCOMP = Column(VARCHAR(100), comment='投资基金的管理人')


class QFIIDESCRIPTION(Base):
    """QFII基本资料"""
    __tablename__ = 'QFIIDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象id')
    F_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    F_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    TRUSTEE_NAME = Column(VARCHAR(100), comment='公司名称')
    TRUSTEE_ID = Column(VARCHAR(100), comment='托管行ID')
    CUSTODY_SECUR_COMPNAME = Column(VARCHAR(200), comment='券商名称')
    CUSTODY_SECUR_COMPID = Column(VARCHAR(200), comment='托管券商ID')
    APPROVAL_DATE = Column(VARCHAR(8), comment='资格获准日期')
    APPROVAL_ENDDATE = Column(VARCHAR(8), comment='资格终止日期')
    APPROVAL_DATE_FIRST = Column(VARCHAR(8), comment='首次额度获准日期')
    APPROVAL_DATE_ACCOUNT = Column(VARCHAR(8), comment='帐户获准日期')
    ANN_DATE = Column(VARCHAR(8), comment='信息披露日期')


class QFIIDESCRIPTIONZL(Base):
    """QFII基本资料增量"""
    __tablename__ = 'QFIIDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象id')
    F_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    F_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    TRUSTEE_NAME = Column(VARCHAR(100), comment='公司名称')
    TRUSTEE_ID = Column(VARCHAR(100), comment='托管行ID')
    CUSTODY_SECUR_COMPNAME = Column(VARCHAR(200), comment='券商名称')
    CUSTODY_SECUR_COMPID = Column(VARCHAR(200), comment='托管券商ID')
    APPROVAL_DATE = Column(VARCHAR(8), comment='资格获准日期')
    APPROVAL_ENDDATE = Column(VARCHAR(8), comment='资格终止日期')
    APPROVAL_DATE_FIRST = Column(VARCHAR(8), comment='首次额度获准日期')
    APPROVAL_DATE_ACCOUNT = Column(VARCHAR(8), comment='帐户获准日期')
    ANN_DATE = Column(VARCHAR(8), comment='信息披露日期')


class QFIIQUOTACHANGE(Base):
    """QFII额度变动"""
    __tablename__ = 'QFIIQUOTACHANGE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象id')
    F_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    F_INFO_COMPCODE = Column(VARCHAR(20), comment='公司ID')
    INVEST_AMOUNT = Column(Numeric(20, 4), comment='投资额度(亿)')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    TYPE = Column(Numeric(9, 0), comment='类型代码')


class QFIIQUOTACHANGEZL(Base):
    """QFII额度变动增量"""
    __tablename__ = 'QFIIQUOTACHANGEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象id')
    F_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    F_INFO_COMPCODE = Column(VARCHAR(20), comment='公司ID')
    INVEST_AMOUNT = Column(Numeric(20, 4), comment='投资额度(亿)')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    TYPE = Column(Numeric(9, 0), comment='类型代码')


class RALATEDSECURITIESCODE(Base):
    """证券关系表"""
    __tablename__ = 'RALATEDSECURITIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_RALATEDCODE = Column(VARCHAR(40), comment='关联证券Wind代码')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    S_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    S_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期')


class RALATEDSECURITIESCODEZL(Base):
    """证券关系表(增量)"""
    __tablename__ = 'RALATEDSECURITIESCODEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_RALATEDCODE = Column(VARCHAR(40), comment='关联证券Wind代码')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    S_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    S_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期')


class RCLOANOFTHEPOOL(Base):
    """资产池贷款回收情况"""
    __tablename__ = 'RCLOANOFTHEPOOL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    POOL_NAME = Column(VARCHAR(200), comment='资产池名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    START_DT = Column(VARCHAR(8), comment='收款期间起始日')
    END_DR = Column(VARCHAR(8), comment='收款期间截止日')
    RCLOAN_NUM = Column(Numeric(24, 4), comment='回收贷款笔数(笔)')
    RC = Column(Numeric(24, 8), comment='收入回收款(万元)')
    RCPRINCIPAL = Column(Numeric(24, 8), comment='本金回收款(万元)')
    RCINTEREST = Column(Numeric(24, 8), comment='利息回收款(万元)')
    RCPENALTY = Column(Numeric(24, 8), comment='违约金回收款(万元)')
    RCOTHER = Column(Numeric(24, 8), comment='其他回收款(万元)')
    PAYIP_NUM = Column(Numeric(24, 4), comment='计划内还款笔数')
    PAYIP = Column(Numeric(24, 8), comment='计划内还款本金(万元)')
    PREPAY_NUM = Column(Numeric(24, 4), comment='提前还款笔数')
    PREPAY = Column(Numeric(24, 8), comment='提前还款本金(万元)')
    ARREARS_RCNUM = Column(Numeric(24, 4), comment='拖欠回收笔数')
    ARREARS_RC = Column(Numeric(24, 8), comment='拖欠回收本金(万元)')
    DEFAULT_RCNUM = Column(Numeric(24, 4), comment='违约回收笔数')
    DEFAULT_RC = Column(Numeric(24, 8), comment='违约回收本金(万元)')
    TAXES = Column(Numeric(24, 8), comment='税费支出(万元)')


class REALESTATENEWS(Base):
    """None"""
    __tablename__ = 'REALESTATENEWS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='唯一性标识')
    PUBLISHDATE = Column(DateTime, comment='Wind发布时间')
    TITLE = Column(VARCHAR(1200), comment='新闻标题')
    CONTENT = Column(TEXT(2147483647), comment='新闻内容')
    SOURCE = Column(VARCHAR(200), comment='新闻来源')
    URL = Column(VARCHAR(1800), comment='新闻链接')
    SECTIONS = Column(VARCHAR(3000), comment='新闻栏目')
    AREACODES = Column(TEXT(2147483647), comment='相关地区')
    WINDCODES = Column(TEXT(2147483647), comment='相关公司')
    INDUSTRYCODES = Column(TEXT(2147483647), comment='相关行业')
    SECTERCODES = Column(TEXT(2147483647), comment='概念板块')
    KEYWORDS = Column(VARCHAR(3000), comment='新闻关键字')
    OPDATE = Column(DateTime, comment='入库时间')
    OPMODE = Column(VARCHAR(1), comment='操作类型')
    MKTSENTIMENTS = Column(TEXT(2147483647), comment='市场情绪')


class RELATEDEVENT(Base):
    """中国A股关联事件"""
    __tablename__ = 'RELATEDEVENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    EVENT_ID = Column(VARCHAR(40), comment='事件ID')
    RELATED_ID = Column(VARCHAR(40), comment='关联事件ID')


class RISKINFOSOURCE1(Base):
    """None"""
    __tablename__ = 'RISKINFOSOURCE1'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='唯一性标识')
    PUBLISHDATE = Column(DateTime, comment='资讯发布时间')
    TITLE = Column(VARCHAR(1200), comment='新闻标题')
    SOURCE = Column(VARCHAR(400), comment='资讯来源')
    URL = Column(VARCHAR(1200), comment='资讯链接')
    WINDCODES = Column(TEXT(2147483647), comment='相关公司(Wind)')
    MKTSENTIMENTS = Column(TEXT(2147483647), comment='风险分类(Wind)')
    CONTENT = Column(TEXT(2147483647), comment='资讯正文')


class RISKWARNINGEVENTS(Base):
    """None"""
    __tablename__ = 'RISKWARNINGEVENTS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    COMPNAME = Column(VARCHAR(800), comment='公司名称')
    COMPCODE = Column(VARCHAR(10), comment='公司ID(Wind)')
    SECID = Column(VARCHAR(10), comment='证券ID(Wind)')
    EVTTYPECODE1 = Column(VARCHAR(10), comment='风险分类编码(Wind)')
    EVTTYPE1 = Column(VARCHAR(100), comment='风险分类名称(Wind)')
    EVTTYPECODE2 = Column(VARCHAR(10), comment='事件分类编码(Wind)')
    EVTTYPE2 = Column(VARCHAR(100), comment='事件分类名称(Wind)')
    HAPDATE = Column(VARCHAR(8), comment='事件发生日期')
    PUBLISHDATE = Column(VARCHAR(8), comment='事件公布日期')
    CONTENT = Column(TEXT(2147483647), comment='事件内容')


class SACCOUNTTRUSTVALSTATISTICS(Base):
    """SAccountTrustValStatistics"""
    __tablename__ = 'SACCOUNTTRUSTVALSTATISTICS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_MONTH = Column(VARCHAR(8), comment='月份')
    ACCOUNT_TYPE = Column(VARCHAR(20), comment='账户类型')
    S_INFO_EXCHMARKET = Column(VARCHAR(20), comment='交易所')
    ACCOUNT_NAME = Column(VARCHAR(100), comment='账户名称')
    TOTAL_TRUST = Column(Numeric(20, 4), comment='托管总额')
    S_INFO_UNIT = Column(VARCHAR(80), comment='单位')
    S_INFO_RATIO = Column(Numeric(20, 4), comment='比例（%）')
    FININST_TYPE = Column(VARCHAR(40), comment='金融机构类型')


class SAMFUNDAGENCY(Base):
    """中国券商理财中介机构"""
    __tablename__ = 'SAMFUNDAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_AGENCY_NAME = Column(VARCHAR(200), comment='中介机构名称')
    S_AGENCY_FNAME = Column(VARCHAR(100), comment='中介机构名称(容错后)')
    S_AGENCY_ID = Column(VARCHAR(40), comment='中介机构ID')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(6, 0), comment='最新标志')


class SAMFUNDASSOCIATIONCODE(Base):
    """中国券商理财基金业协会编码"""
    __tablename__ = 'SAMFUNDASSOCIATIONCODE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务代码类型')
    S_CODE = Column(VARCHAR(40), comment='业务代码')
    S_SNAME = Column(VARCHAR(100), comment='业务简称')
    IS_COMMON = Column(Numeric(1, 0), comment='是否通用代码')
    MEMO = Column(VARCHAR(800), comment='业务说明')
    COMP_TYPE_CODE = Column(Numeric(9, 0), comment='主体类别代码')


class SAMFUNDOPERATEPERIOD(Base):
    """中国券商理财滚动运作周期"""
    __tablename__ = 'SAMFUNDOPERATEPERIOD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    OPR_PERIOD = Column(Numeric(10, 0), comment='期数')
    PCH_STARTDT = Column(VARCHAR(8), comment='开放申购起始日')
    PCH_ENDDT = Column(VARCHAR(8), comment='开放申购截止日')
    OPR_STARTDT = Column(VARCHAR(8), comment='运作起始日')
    OPR_ENDDT = Column(VARCHAR(8), comment='运作结束日')
    REDM_STARTDT = Column(VARCHAR(8), comment='开放赎回起始日')
    REDM_ENDDT = Column(VARCHAR(8), comment='开放赎回截止日')
    ANTICIPATE_ANNUALYEILD = Column(Numeric(20, 4), comment='预期年化收益率')
    ANNUALYEILD = Column(Numeric(20, 4), comment='实际年化收益率')


class SAMFUNDOPERATEPERIODZL(Base):
    """券商理财滚动运作周期增量"""
    __tablename__ = 'SAMFUNDOPERATEPERIODZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    OPR_PERIOD = Column(Numeric(10, 0), comment='期数')
    PCH_STARTDT = Column(VARCHAR(8), comment='开放申购起始日')
    PCH_ENDDT = Column(VARCHAR(8), comment='开放申购截止日')
    OPR_STARTDT = Column(VARCHAR(8), comment='运作起始日')
    OPR_ENDDT = Column(VARCHAR(8), comment='运作结束日')
    REDM_STARTDT = Column(VARCHAR(8), comment='开放赎回起始日')
    REDM_ENDDT = Column(VARCHAR(8), comment='开放赎回截止日')
    ANTICIPATE_ANNUALYEILD = Column(Numeric(20, 4), comment='预期年化收益率')
    ANNUALYEILD = Column(Numeric(20, 4), comment='实际年化收益率')


class SAMGRADINGFUND(Base):
    """中国券商理财分级基金基本资料"""
    __tablename__ = 'SAMGRADINGFUND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='母基金Wind代码')
    F_INFO_FEEDER_WINDCODE = Column(VARCHAR(40), comment='子基金Wind代码')
    F_INFO_FEEDER_TYPECODE = Column(Numeric(9, 0), comment='子基金类型代码')
    F_INFO_FEEDER_SHARERATIO = Column(Numeric(20, 4), comment='子基金份额占比')
    F_INFO_TERM_TYPECODE = Column(Numeric(9, 0), comment='存续期类型代码')
    F_INFO_PERIOD_IFDIV = Column(Numeric(1, 0), comment='运作期内是否分红')
    F_INFO_TERM_IFTRANS = Column(Numeric(1, 0), comment='存续期内是否有份额配对转换')
    F_INFO_TRANS_BGNDATE = Column(VARCHAR(8), comment='份额配对转换起始日期')
    F_INFO_TRANS_ENDDATE = Column(VARCHAR(8), comment='份额配对转换截止日期')
    F_INFO_PREFER_IFDIS = Column(Numeric(1, 0), comment='优先份额是否参与超额收益分配')
    F_INFO_PREFER_IFADD = Column(Numeric(1, 0), comment='优先份额约定收益是否得到累计')
    F_INFO_PREFER_FORMULA = Column(VARCHAR(200), comment='优先份额约定年收益表达式')


class SCFCLAUSE(Base):
    """中国分级基金条款"""
    __tablename__ = 'SCFCLAUSE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TYPE_CODE = Column(Numeric(9, 0), comment='条款属性类型代码')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='是否最新')
    CONTENT = Column(TEXT(2147483647), comment='条款')


class SCFCONVERT(Base):
    """中国分级基金折算"""
    __tablename__ = 'SCFCONVERT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    CONVERT_REASON = Column(Numeric(9, 0), comment='折算原因代码')
    PERIOD = Column(Numeric(20, 4), comment='折算周期(年)')
    CONVERT_DT = Column(VARCHAR(8), comment='折算基准日')
    NAV_TYPECODE = Column(Numeric(9, 0), comment='基金净值类型代码')
    NAV_MIN = Column(Numeric(20, 4), comment='基金净值下限(元)')
    NAV_MAX = Column(Numeric(20, 4), comment='基金净值上限(元)')
    CONVERT_TYPECODE = Column(Numeric(9, 0), comment='折算方式代码')
    CONVERT_FUND_TYPECODE = Column(Numeric(9, 0), comment='折算母基金份额的方式代码')
    CONVERT_FEEDER_TYPECODE = Column(Numeric(9, 0), comment='折算子基金份额的方式代码')


class SCFRETURNDISTRIBUTION(Base):
    """中国分级基金收益分配"""
    __tablename__ = 'SCFRETURNDISTRIBUTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='母基金Wind代码')
    F_INFO_FEEDER_WINDCODE = Column(VARCHAR(40), comment='子基金Wind代码')
    RULE_STARETDT = Column(VARCHAR(8), comment='收益分配条约起始日期')
    RULE_ENDDT = Column(VARCHAR(8), comment='收益分配条约截止日期')
    PRI_BENCHRETURN = Column(Numeric(20, 4), comment='优先份额基准收益率(%)')
    TYPE_CODE = Column(Numeric(9, 0), comment='优先份额基准收益率获取方式代码')
    RETURNDIST_CODE = Column(Numeric(9, 0), comment='子基金收益方式代码')
    EXRETURN_SHARE = Column(Numeric(20, 4), comment='子基金超额收益分成占比(%)')


class SCLOANOFTHEPOOL(Base):
    """资产池贷款状态特征"""
    __tablename__ = 'SCLOANOFTHEPOOL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    POOL_NAME = Column(VARCHAR(200), comment='资产池名称')
    ANN_DT = Column(VARCHAR(8), comment='报告日期')
    START_DT = Column(VARCHAR(8), comment='收款起始日')
    END_DR = Column(VARCHAR(8), comment='收款截止日')
    LAON_NUM = Column(Numeric(20, 4), comment='正常贷款笔数')
    LAON_BALANCE = Column(Numeric(24, 8), comment='正常贷款本金余额')
    OVELOANS1_30D_NUM = Column(Numeric(20, 4), comment='逾期1-30天贷款笔数')
    OVELOANS1_30D__BALANCE = Column(Numeric(24, 8), comment='逾期1-30天贷款本金余额')
    OVELOANS31_60D_NUM = Column(Numeric(24, 4), comment='逾期31-60天贷款笔数')
    OVELOANS31_60D__BALANCE = Column(Numeric(20, 8), comment='逾期31-60天贷款本金余额')
    OVELOANS61_90D_NUM = Column(Numeric(20, 4), comment='逾期61-90天贷款笔数')
    OVELOANS61_90D__BALANCE = Column(Numeric(24, 8), comment='逾期61-90天贷款本金余额')
    SERI_ARR_LAON_NUM = Column(Numeric(20, 4), comment='严重拖欠贷款笔数')
    SERI_ARR_LAON_BALANCE = Column(Numeric(24, 8), comment='严重拖欠贷款本金余额')
    DEF_LAON_NUM = Column(Numeric(20, 4), comment='违约贷款数目')
    DEF_LAON_BALANCE = Column(Numeric(24, 8), comment='违约贷款本金余额')
    NEW_DEF_LAON_NUM = Column(Numeric(20, 4), comment='新增违约贷款笔数')
    NEW_DEF_LAON_BALANCE = Column(Numeric(24, 8), comment='新增违约贷款本金余额')
    PROC_NOARR_LAON_NUM = Column(Numeric(20, 4), comment='经处置无拖欠贷款笔数')
    PROC_NOARR_LAON_BALANCE = Column(Numeric(24, 8), comment='经处置无拖欠贷款本金余额')
    NONPROSE_PROC_LAON_NUM = Column(Numeric(20, 4), comment='非诉讼类处置贷款笔数')
    NONPROSE_PROC_LAON_BALANCE = Column(Numeric(24, 8), comment='非诉讼类处置贷款本金余额')
    READYPROSE_LAON_NUM = Column(Numeric(20, 4), comment='进入诉讼准备程序贷款笔数')
    READYPROSE_LAON_BALANCE = Column(Numeric(24, 8), comment='进入诉讼准备程序贷款本金余额')
    ACCEPTPROSE_LAON_NUM = Column(Numeric(20, 4), comment='进入法庭受理程序贷款笔数')
    ACCEPTPROSE_LAON_BALANCE = Column(Numeric(24, 8), comment='进入法庭受理程序贷款本金余额')
    EXECAUCTION_LAON_NUM = Column(Numeric(20, 4), comment='进入执行拍卖程序贷款笔数')
    EXECAUCTION_LAON_BALANCE = Column(Numeric(24, 8), comment='进入执行拍卖程序贷款本金余额')
    SETTLE_PROC_LAON_NUM = Column(Numeric(20, 4), comment='经处置已结清贷款笔数')
    SETTLE_PROC_LAON_BALANCE = Column(Numeric(24, 8), comment='经处置已结清贷款本金余额')
    CANCEL_PROC_LAON_NUM = Column(Numeric(20, 4), comment='经处置已核销贷款笔数')
    CANCEL_PROC_LAON_BALANCE = Column(Numeric(24, 8), comment='经处置已核销贷款本金余额')
    REDM_BB_REP_LAON_NUM = Column(Numeric(20, 4), comment='赎回、回购或替换贷款笔数')
    REDM_BB_REP_LAON_BALANCE = Column(Numeric(24, 8), comment='赎回、回购或替换贷款金额')


class SECREGIONVOLUMETOT(Base):
    """证券地区交易量合计(月)"""
    __tablename__ = 'SECREGIONVOLUMETOT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TRADE_MONTH = Column(VARCHAR(8), comment='月份')
    PROVINCE = Column(VARCHAR(20), comment='省份')
    S_TYPE = Column(Numeric(1, 0), comment='数据类型(当月;累计)')
    S_VOLUME_TOT = Column(Numeric(20, 4), comment='总交易量(亿元)')
    S_VOLUME_STOCK = Column(Numeric(20, 4), comment='股票交易量(亿元)')
    S_VOLUME_FUND = Column(Numeric(20, 4), comment='基金交易量(亿元)')
    S_VOLUME_BOND = Column(Numeric(20, 4), comment='债券交易量(亿元)')
    S_VOLUME_WARRANT = Column(Numeric(20, 4), comment='权证交易量(亿元)')
    S_EXCHMARKET = Column(Numeric(1, 0), comment='交易所')


class SECURITIESTYPECODE(Base):
    """证券类型代码配置表"""
    __tablename__ = 'SECURITIESTYPECODE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TYPE_CODE = Column(VARCHAR(10), comment='证券类型代码')
    TYPE = Column(VARCHAR(40), comment='证券类型')


class SHIBORPRICES(Base):
    """Shibor行情"""
    __tablename__ = 'SHIBORPRICES'
    __table_args__ = (
        Index('IDX_SHIBORPRICES_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    B_INFO_RATE = Column(Numeric(20, 4), comment='利率(%)')
    B_INFO_TERM = Column(VARCHAR(40), comment='期限')
    PCT_CHG = Column(Numeric(20, 4), comment='涨跌(BP)')


class SHSCCHANNELHOLDINGS(Base):
    """陆港通通道持股数量统计(中央结算系统)"""
    __tablename__ = 'SHSCCHANNELHOLDINGS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码')
    TRADE_DT = Column(VARCHAR(8), comment='持股日期')
    S_INFO_EXCHMARKETNAME = Column(VARCHAR(40), comment='交易所英文简称')
    S_QUANTITY = Column(Numeric(20, 4), comment='中央结算系统持股量')
    S_RATIO = Column(Numeric(20, 4), comment='[内部]中央结算系统持股量占比')
    S_INFO_CODE = Column(VARCHAR(40), comment='[内部]股份代码')


class SHSCDAILYSTATISTICS(Base):
    """陆港通日交易统计"""
    __tablename__ = 'SHSCDAILYSTATISTICS'
    __table_args__ = (
        Index('IDX_SHSCDAILYSTATISTICS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(100), comment='日期')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')
    VALUE = Column(Numeric(20, 4), comment='数据')
    ITEM_CODE = Column(Numeric(9, 0), comment='项目代码')
    UNIT = Column(VARCHAR(20), comment='单位')


class SHSCMECHANISMOWNERSHIP(Base):
    """陆港通机构持股"""
    __tablename__ = 'SHSCMECHANISMOWNERSHIP'
    __table_args__ = (
        Index('INDEX_ENDDATE', 'S_HOLDER_ENDDATE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_HOLDER_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_HOLDER_NAME = Column(VARCHAR(100), comment='机构名称')
    S_HOLDER_NUM = Column(VARCHAR(10), comment='机构编号')
    S_HOLDER_COMPID = Column(VARCHAR(40), comment='机构公司ID')
    S_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='持股数量')
    S_HOLDER_ISSUED_TRADABLE_SHR = Column(Numeric(20, 4), comment='已发行股本或流通股份占比')


class SHSCMEMBERS(Base):
    """沪股通成分股"""
    __tablename__ = 'SHSCMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class SHSCSELLMEMBERS(Base):
    """沪股通只可卖出证券"""
    __tablename__ = 'SHSCSELLMEMBERS'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='所属板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class SHSCSHORTSELLING(Base):
    """陆港通卖空数据"""
    __tablename__ = 'SHSCSHORTSELLING'
    __table_args__ = (
        Index('IDX_SHSCSHORTSELLING_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    SHORT_SELL_STOCKS_MAX = Column(Numeric(20, 4), comment='最多可供卖空的股数(股)')
    SHORT_SELL_STOCKS_BALANCE = Column(Numeric(20, 4), comment='可供卖空的股数余额(股)')
    SHORT_SALE_NUM = Column(Numeric(20, 4), comment='卖空成交股数(股)')
    SHORT_SALE_AMOUNT = Column(Numeric(20, 4), comment='卖空成交金额(元)')
    SHORT_SELL_PROPORTION = Column(Numeric(20, 4), comment='当天卖空比例(%)')
    SHORT_SELL_PROPORTION_TOTAL = Column(Numeric(20, 4), comment='累计十天卖空比例(%)')


class SHSCTOP10ACTIVESTOCKS(Base):
    """陆港通日十大成交活跃股统计"""
    __tablename__ = 'SHSCTOP10ACTIVESTOCKS'
    __table_args__ = (
        Index('IDX_SHSCTOP10ACTIVESTOCKS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    MARKET = Column(VARCHAR(100), comment='市场')
    BUYTRADEVALUE = Column(Numeric(20, 4), comment='买入金额')
    SELLTRADEVALUE = Column(Numeric(20, 4), comment='卖出金额')
    TOTALTRADEVALUE = Column(Numeric(20, 4), comment='成交金额')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_EXCHMARKETNAME = Column(VARCHAR(40), comment='交易所英文简称')


class SHSZRELATEDSECURITIES(Base):
    """AH股关联证券"""
    __tablename__ = 'SHSZRELATEDSECURITIES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    EXCHANGE_A = Column(VARCHAR(40), comment='交易所1')
    SECURITIES_TYPE_A = Column(VARCHAR(10), comment='证券类型1')
    S_INFO_WINDCODE = Column(VARCHAR(10), comment='WIND代码1')
    EXCHANGE_B = Column(VARCHAR(40), comment='交易所2')
    SECURITIES_TYPE_B = Column(VARCHAR(10), comment='证券类型2')
    S_INFO_WINDCOD2 = Column(VARCHAR(10), comment='WIND代码2')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券简称2')
    IS_EFFECTIVE = Column(Numeric(1, 0), comment='是否有效')


class SINDEXPERFORMANCE(Base):
    """中国A股指数行情衍生指标"""
    __tablename__ = 'SINDEXPERFORMANCE'
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


class SRLEADERREMARKS(Base):
    """None"""
    __tablename__ = 'SRLEADERREMARKS'
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


class SSEBONDSTATISTICS(Base):
    """上证所债券统计(分券种)"""
    __tablename__ = 'SSEBONDSTATISTICS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    BOND_TYPE = Column(VARCHAR(20), comment='债券种类')
    INDEX_CODE = Column(Numeric(9, 0), comment='统计指标代码')
    INDEX_DATA = Column(Numeric(20, 4), comment='指标数据')
    UNIT = Column(VARCHAR(10), comment='单位')


class STOCKNEGATIVENEWS(Base):
    """None"""
    __tablename__ = 'STOCKNEGATIVENEWS'
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


class STOCKPOSITIVENEWS(Base):
    """None"""
    __tablename__ = 'STOCKPOSITIVENEWS'
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


class SZSCMEMBERS(Base):
    """深股通成分股"""
    __tablename__ = 'SZSCMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class SZSCQFIIRQFIIINVESTORINFO(Base):
    """深股通/QFII/RQFII投资者信息"""
    __tablename__ = 'SZSCQFIIRQFIIINVESTORINFO'
    SEC_ID = Column(VARCHAR(10), comment='证券id')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    FORINS_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='境外投资者持股数量')
    FORINS_HOLDER_PCT = Column(Numeric(20, 4), comment='境外投资者持股占比')
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')


class SZSCSELLMEMBERS(Base):
    """深股通只可卖出证券"""
    __tablename__ = 'SZSCSELLMEMBERS'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='所属板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class TBOBJECT4124(Base):
    """[中信证券]定制EDB数据"""
    __tablename__ = 'TBOBJECT4124'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    F1_4124 = Column(VARCHAR(10))
    F2_4124 = Column(VARCHAR(8))
    F3_4124 = Column(Numeric(20, 6))
    F4_4124 = Column(VARCHAR(8))


class TEJCREDITRATINGDESCRIPTION(Base):
    """CCRQM财务信用评级说明表"""
    __tablename__ = 'TEJCREDITRATINGDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='年月日')
    S_NUM = Column(Numeric(4, 0), comment='序号')
    S_RISK_LEVEL = Column(VARCHAR(2), comment='风险等级')
    S_DESCRIPTION = Column(VARCHAR(2000), comment='说明')


class TEJCREDITRATINGMASTER(Base):
    """CCRQM财务信用评级主表"""
    __tablename__ = 'TEJCREDITRATINGMASTER'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型')
    S_RISK_LEVEL = Column(VARCHAR(2), comment='风险等级')
    S_TOTAL_SCORE = Column(Numeric(5, 0), comment='总分')
    S_CORPORATE_GOVERNANCE = Column(Numeric(4, 0), comment='公司治理')
    S_PROFIT = Column(Numeric(4, 0), comment='获利')
    S_SAFETY = Column(Numeric(4, 0), comment='安全')
    S_EFFECTIVENESS = Column(Numeric(4, 0), comment='效率')
    S_NET_RATE_RETURN = Column(Numeric(20, 4), comment='净值报酬率')
    S_ROA = Column(Numeric(20, 4), comment='资产报酬率')
    S_OPERATING_PROFIT_RATE = Column(Numeric(20, 4), comment='营业利益率')
    S_GROSS_PROFIT_MARGIN = Column(Numeric(20, 4), comment='毛利率')
    S_A_BORROWING_DEPENDENCY = Column(Numeric(20, 4), comment='调整后借款依存度%')
    S_BORROWING_DEPENDENCY = Column(Numeric(20, 4), comment='借款依存度%')
    S_QUICK_RATIO = Column(Numeric(20, 4), comment='速动比率%')
    S_CONSERVA_QUICK_RATIO = Column(Numeric(20, 4), comment='保守速动比率%')
    S_INTEREST_RATE = Column(Numeric(20, 4), comment='利息支出率%')
    S_COLLECTION_DAYS = Column(Numeric(20, 4), comment='收款天数')
    S_SALES_DAYS = Column(Numeric(20, 4), comment='售货天数')
    S_OTHER_RECEIVABLES = Column(Numeric(20, 4), comment='其他应收款%')
    S_QUALITY_RATIO = Column(Numeric(20, 4), comment='股东设质比%')
    S_REVENUE_GROWTH = Column(Numeric(20, 4), comment='营收成长%')
    S_CFO = Column(Numeric(20, 4), comment='CFO')
    S_OPERATING_PROFIT = Column(Numeric(20, 4), comment='营业利益')
    S_AVERAGE_LOAN_INTEREST = Column(Numeric(20, 4), comment='平均借款利息%')
    S_EXISTING_FUNDS = Column(Numeric(20, 4), comment='现有资金')
    S_LOAN = Column(Numeric(20, 4), comment='借款')
    S_SHAREHOLDERS_EQUITY = Column(Numeric(20, 4), comment='股东权益')
    S_BASIC_LEVEL = Column(VARCHAR(4), comment='数量模式基本等级')
    S_FORMULA_LEVEL = Column(VARCHAR(4), comment='数量模式公式等级')
    S_CONSTANT_NET_RETURN = Column(Numeric(20, 4), comment='常续净值报酬率分数')
    S_ANNUAL_NET_RETURN = Column(Numeric(20, 4), comment='年常续净值报酬率')
    S_OPERATING_RATE = Column(Numeric(20, 4), comment='营业率分数')
    S_CONSERVATIVE_QUICK_RATIO = Column(Numeric(20, 4), comment='保守速动比分数')
    S_COLLECTION_DAYS_SCORE = Column(Numeric(20, 4), comment='收款天数分数')
    S_SALES_DAYS_SCORE = Column(Numeric(20, 4), comment='售货天数分数')
    S_OTHER_RECEIVABLES_RATIO = Column(Numeric(20, 4), comment='其他应收款比率分数')
    S_SHAREHOLDERS_PROPORTION = Column(Numeric(20, 4), comment='大股东设质比分数')
    S_ANNUAL_CONTINUING_BENEFITS = Column(Numeric(20, 4), comment='年化常续利益')
    S_ANNUAL_NONBUSINESS_INTERESTS = Column(Numeric(20, 4), comment='年化常续业外利益')
    S_DE_SCORE = Column(Numeric(20, 4), comment='DE分数')
    S_DE_RATIO = Column(Numeric(20, 4), comment='DE比率')
    S_COMPREHENSIVE_SCORE = Column(Numeric(20, 4), comment='综合评分')
    CURRENCY_CODE = Column(VARCHAR(10), comment='币种单位代码')


class TEJDAILYNEWS(Base):
    """CCRQM财务风险每日快讯"""
    __tablename__ = 'TEJDAILYNEWS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='日期')
    S_NUM = Column(VARCHAR(10), comment='序号')
    S_NEWS_CONTENT = Column(VARCHAR(2000), comment='新闻内容')
    S_EVENT_CLASSIFICATION = Column(VARCHAR(14), comment='事件大分类')
    S_EVENT_SMALL_CLASSNAME = Column(VARCHAR(34), comment='事件小分类名')


class TEJRISKINDICATOR(Base):
    """CCRQM股票财务风险指标"""
    __tablename__ = 'TEJRISKINDICATOR'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_CLOSE = Column(Numeric(20, 8), comment='收盘价元)')
    S_VAR_99 = Column(Numeric(20, 8), comment='VaR-99(%)')
    S_VAR_95 = Column(Numeric(20, 8), comment='VaR-95(%)')
    S_RATE_RETURN = Column(Numeric(20, 8), comment='报酬率(%)')
    S_RAROC_99 = Column(Numeric(20, 8), comment='RAROC-99(%)')
    S_RAROC_95 = Column(Numeric(20, 8), comment='RAROC-95(%)')
    S_FREQUENCY = Column(Numeric(9, 0), comment='频率')


class THIRDPARTYINDEXEOD(Base):
    """其他第三方商品期货指数行情"""
    __tablename__ = 'THIRDPARTYINDEXEOD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额')
    S_DQ_OI = Column(Numeric(20, 4), comment='持仓量')
    S_DQ_SETTLE = Column(Numeric(20, 4), comment='结算价')


class THIRDPARTYSTOCKINDEXEOD(Base):
    """其他第三方股票指数行情"""
    __tablename__ = 'THIRDPARTYSTOCKINDEXEOD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额')
    S_DQ_OI = Column(Numeric(20, 4), comment='持仓量')
    S_DQ_SETTLE = Column(Numeric(20, 4), comment='结算价')


class TIBORPRICE(Base):
    """Tibor行情"""
    __tablename__ = 'TIBORPRICE'
    __table_args__ = (
        Index('IDX_TIBORPRICE_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(Numeric(8, 0), comment='指标日期')
    B_INFO_RATE = Column(Numeric(20, 6), comment='数据')


class TOP5BYACCOUNTSRECEIVABLE(Base):
    """中国A股应收账款余额前五名"""
    __tablename__ = 'TOP5BYACCOUNTSRECEIVABLE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='债务人名称')
    AMOUNT = Column(Numeric(20, 4), comment='金额（元）')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PERIOD = Column(VARCHAR(70), comment='拖欠时间')
    REASON = Column(VARCHAR(30), comment='拖欠原因')


class TOP5BYLONGTERMBORROWING(Base):
    """中国A股长期借款前五名"""
    __tablename__ = 'TOP5BYLONGTERMBORROWING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='单位名称')
    S_INFO_COMPCODE2 = Column(VARCHAR(40), comment='单位名称ID')
    TYPECODE = Column(Numeric(9, 0), comment='往来资金类别代码')
    CONDITIONCODE = Column(Numeric(9, 0), comment='往来资金条件代码')
    START_DT = Column(VARCHAR(8), comment='起始日')
    END_DT = Column(VARCHAR(8), comment='终止日')
    AMOUNT1 = Column(Numeric(20, 4), comment='金额（元）')
    AMOUNT2 = Column(Numeric(20, 4), comment='原币金额（元）')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    RATE = Column(VARCHAR(80), comment='利率(%)')


class TOP5BYOPERATINGINCOME(Base):
    """中国A股营业收入前五名"""
    __tablename__ = 'TOP5BYOPERATINGINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='单位名称')
    S_INFO_COMPCODE2 = Column(VARCHAR(40), comment='单位名称ID')
    SALESAMOUNT = Column(Numeric(20, 4), comment='金额(元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PCT = Column(Numeric(20, 4), comment='占比(%)')
    INTERCHANGE_CODE = Column(Numeric(9, 0), comment='往来资金类别代码')


class TRUSTCOIMPORTANTINDEX(Base):
    """信托公司重要指标"""
    __tablename__ = 'TRUSTCOIMPORTANTINDEX'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    TOT_ASSETS = Column(Numeric(20, 4), comment='资产总计')
    TOT_LIAB = Column(Numeric(20, 4), comment='负债合计')
    NET_ASSETS = Column(Numeric(20, 4), comment='净资产')
    NET_CAPITAL = Column(Numeric(20, 4), comment='净资本')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入')
    TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    NET_CAPITAL_RATIO = Column(Numeric(20, 4), comment='净资本比率(%)')
    FLOW_RATIO = Column(Numeric(20, 4), comment='流动比率(%)')
    LONG_TERM_ASSETS = Column(Numeric(20, 4), comment='长期资产合计')
    ASSETS_LIABILITIES = Column(Numeric(20, 4), comment='资产负债率(%)')
    ASSET_TURNOVER = Column(Numeric(20, 4), comment='资产周转率(%)-证券')
    ROE = Column(Numeric(20, 4), comment='净资产收益率(%)')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')
    IS_AUDITED = Column(Numeric(5, 0), comment='是否审计')
    SELF_OWNED_SECURITIES = Column(Numeric(20, 4), comment='自营证券(原值)-证券')
    TREASURY_BONDS = Column(Numeric(20, 4), comment='国债-证券')
    INVESTMENT_FUNDS = Column(Numeric(20, 4), comment='投资基金-证券')
    STOCK = Column(Numeric(20, 4), comment='股票-证券')
    CONVERTIBLE_BONDS = Column(Numeric(20, 4), comment='可转债-证券')
    TOT_CUR_ASSETS = Column(Numeric(20, 4), comment='流动资产合计')
    LONG_TERM_INVESTMENT = Column(Numeric(20, 4), comment='长期投资合计')
    TOTAL_FIXED_ASSETS = Column(Numeric(20, 4), comment='固定资产合计')
    INTANGIBLE_OTHER_ASSETS = Column(Numeric(20, 4), comment='无形资产及其他资产合计')
    TOT_CUR_LIAB = Column(Numeric(20, 4), comment='流动负债合计')
    LONG_TERM_LIABILITIES = Column(Numeric(20, 4), comment='长期负债合计')
    PAID_UP_CAPITAL = Column(Numeric(20, 4), comment='实收资本')
    FEE_INCOME = Column(Numeric(20, 4), comment='手续费收入-证券')
    SELF_SC_DIFFERENCE_INCOME = Column(Numeric(20, 4), comment='自营证券差价收入-证券')
    ENTRUSTED_INVESTMENT_INCOME = Column(Numeric(20, 4), comment='受托投资管理收益-证券')
    UNDERWRITING_INCOME = Column(Numeric(20, 4), comment='证券承销收入-证券')
    NET_SELF_OWNED_SECURITIES = Column(Numeric(20, 4), comment='自营证券(净额)-证券')
    INVESTMENT_INCOME = Column(Numeric(20, 4), comment='投资收益')
    OPER_EXP = Column(Numeric(20, 4), comment='营业支出')
    OPER_COST = Column(Numeric(20, 4), comment='营业费用')
    DEDUCT_TOTAL_PROFIT_LOSS = Column(Numeric(20, 4), comment='扣除资产损失后利润总额')
    NET_INCREASE_CASH = Column(Numeric(20, 4), comment='现金净增加额')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型')
    COMP_TYPE = Column(VARCHAR(40), comment='公司类型')
    CAPITAL_YIELD = Column(Numeric(20, 4), comment='资本收益率(%)-信托')
    TRUST_RATE_RETURN = Column(Numeric(20, 4), comment='信托报酬率(%)-信托')
    PER_CAPITA_PROFIT = Column(Numeric(20, 4), comment='人均利润')
    TRUST_ASSETS_TOT = Column(Numeric(20, 4), comment='信托资产运用合计-信托')
    TOTAL_TRUST_INCOME = Column(Numeric(20, 4), comment='信托收入合计-信托')
    TOTAL_TRUST_COSTS = Column(Numeric(20, 4), comment='信托费用合计-信托')
    TRUST_GAINS_LOSSES = Column(Numeric(20, 4), comment='信托损益-信托')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 4), comment='员工人数')
    ACC_STA_CODE = Column(VARCHAR(2), comment='原始报表采用会计准则代码')


class UNLISTEDBANKBALANCESHEET(Base):
    """非上市银行资产负债表"""
    __tablename__ = 'UNLISTEDBANKBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    CASH_DEPOSITS_CENTRAL_BANK = Column(Numeric(20, 4), comment='现金及存放中央银行款项')
    ASSET_DEP_OTH_BANKS_FIN_INST = Column(Numeric(20, 4), comment='存放同业和其它金融机构款项')
    PRECIOUS_METALS = Column(Numeric(20, 4), comment='贵金属')
    LOANS_TO_OTH_BANKS = Column(Numeric(20, 4), comment='拆出资金')
    TRADABLE_FIN_ASSETS = Column(Numeric(20, 4), comment='交易性金融资产')
    DERIVATIVE_FIN_ASSETS = Column(Numeric(20, 4), comment='衍生金融资产')
    RED_MONETARY_CAP_FOR_SALE = Column(Numeric(20, 4), comment='买入返售金融资产')
    INT_RCV = Column(Numeric(20, 4), comment='应收利息')
    LOANS_AND_ADV_GRANTED = Column(Numeric(20, 4), comment='发放贷款及垫款')
    AGENCY_BUS_ASSETS = Column(Numeric(20, 4), comment='代理业务资产')
    FIN_ASSETS_AVAIL_FOR_SALE = Column(Numeric(20, 4), comment='可供出售金融资产')
    HELD_TO_MTY_INVEST = Column(Numeric(20, 4), comment='持有至到期投资')
    LONG_TERM_EQY_INVEST = Column(Numeric(20, 4), comment='长期股权投资')
    RCV_INVEST = Column(Numeric(20, 4), comment='应收款项类投资')
    FIX_ASSETS = Column(Numeric(20, 4), comment='固定资产')
    INTANG_ASSETS = Column(Numeric(20, 4), comment='无形资产')
    GOODWILL = Column(Numeric(20, 4), comment='商誉')
    DEFERRED_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产')
    INVEST_REAL_ESTATE = Column(Numeric(20, 4), comment='投资性房地产')
    OTH_ASSETS = Column(Numeric(20, 4), comment='其他资产')
    SPE_BAL_ASSETS = Column(Numeric(20, 4), comment='资产差额(特殊报表科目)')
    TOT_BAL_ASSETS = Column(Numeric(20, 4), comment='资产差额(合计平衡项目)')
    TOT_ASSETS = Column(Numeric(20, 4), comment='资产总计')
    LIAB_DEP_OTH_BANKS_FIN_INST = Column(Numeric(20, 4), comment='同业和其它金融机构存放款项')
    BORROW_CENTRAL_BANK = Column(Numeric(20, 4), comment='向中央银行借款')
    LOANS_OTH_BANKS = Column(Numeric(20, 4), comment='拆入资金')
    TRADABLE_FIN_LIAB = Column(Numeric(20, 4), comment='交易性金融负债')
    DERIVATIVE_FIN_LIAB = Column(Numeric(20, 4), comment='衍生金融负债')
    FUND_SALES_FIN_ASSETS_RP = Column(Numeric(20, 4), comment='卖出回购金融资产款')
    CUST_BANK_DEP = Column(Numeric(20, 4), comment='吸收存款')
    EMPL_BEN_PAYABLE = Column(Numeric(20, 4), comment='应付职工薪酬')
    TAXES_SURCHARGES_PAYABLE = Column(Numeric(20, 4), comment='应交税费')
    INT_PAYABLE = Column(Numeric(20, 4), comment='应付利息')
    AGENCY_BUS_LIAB = Column(Numeric(20, 4), comment='代理业务负债')
    BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付债券')
    DEFERRED_TAX_LIAB = Column(Numeric(20, 4), comment='递延所得税负债')
    PROVISIONS = Column(Numeric(20, 4), comment='预计负债')
    OTH_LIAB = Column(Numeric(20, 4), comment='其他负债')
    SPE_BAL_LIAB = Column(Numeric(20, 4), comment='负债差额(特殊报表科目)')
    TOT_BAL_LIAB = Column(Numeric(20, 4), comment='负债差额(合计平衡项目)')
    TOT_LIAB = Column(Numeric(20, 4), comment='负债合计')
    CAP_STK = Column(Numeric(20, 4), comment='股本')
    CAP_RSRV = Column(Numeric(20, 4), comment='资本公积金')
    LESS_TSY_STK = Column(Numeric(20, 4), comment='减：库存股')
    SURPLUS_RSRV = Column(Numeric(20, 4), comment='盈余公积金')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='未分配利润')
    PROV_NOM_RISKS = Column(Numeric(20, 4), comment='一般风险准备')
    CNVD_DIFF_FOREIGN_CURR_STAT = Column(Numeric(20, 4), comment='外币报表折算差额')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认的投资损失')
    SPE_BAL_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益差额(特殊报表科目)')
    TOT_BAL_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益差额(合计平衡项目)')
    MINORITY_INT = Column(Numeric(20, 4), comment='少数股东权益')
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(不含少数股东权益)')
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(含少数股东权益)')
    SPE_BAL_LIAB_EQY = Column(Numeric(20, 4), comment='负债及股东权益差额(特殊报表项目)')
    TOT_BAL_LIAB_EQY = Column(Numeric(20, 4), comment='负债及股东权益差额(合计平衡项目)')
    TOT_LIAB_SHRHLDR_EQY = Column(Numeric(20, 4), comment='负债及股东权益总计')
    OTHER_COMP_INCOME = Column(Numeric(20, 4), comment='其他综合收益')
    OTHER_EQUITY_TOOLS = Column(Numeric(20, 4), comment='其他权益工具')
    OTHER_EQUITY_TOOLS_P_SHR = Column(Numeric(20, 4), comment='其他权益工具:优先股')
    SETTLE_RSRV = Column(Numeric(20, 4), comment='结算备付金')


class UNLISTEDBANKCASHFLOW(Base):
    """非上市银行现金流量表"""
    __tablename__ = 'UNLISTEDBANKCASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    FREE_CASH_FLOW = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    NET_INCR_DEP_COB = Column(Numeric(20, 4), comment='客户存款和同业存放款项净增加额')
    NET_INCR_LOANS_CENTRAL_BANK = Column(Numeric(20, 4), comment='向中央银行借款净增加额')
    NET_INCR_FUND_BORR_OFI = Column(Numeric(20, 4), comment='向其他金融机构拆入资金净增加额')
    NET_INCR_INT_HANDLING_CHRG = Column(Numeric(20, 4), comment='收取利息和手续费净增加额')
    OTHER_CASH_RECP_RAL_OPER_ACT = Column(Numeric(20, 4), comment='收到其他与经营活动有关的现金')
    SPE_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流入小计')
    NET_INCR_CLIENTS_LOAN_ADV = Column(Numeric(20, 4), comment='客户贷款及垫款净增加额')
    NET_INCR_DEP_CBOB = Column(Numeric(20, 4), comment='存放央行和同业款项净增加额')
    CASH_PAY_BEH_EMPL = Column(Numeric(20, 4), comment='支付给职工以及为职工支付的现金')
    PAY_ALL_TYP_TAX = Column(Numeric(20, 4), comment='支付的各项税费')
    OTHER_CASH_PAY_RAL_OPER_ACT = Column(Numeric(20, 4), comment='支付其他与经营活动有关的现金')
    HANDLING_CHRG_PAID = Column(Numeric(20, 4), comment='支付手续费的现金')
    SPE_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额')
    CASH_RECP_DISP_WITHDRWL_INVEST = Column(Numeric(20, 4), comment='收回投资收到的现金')
    CASH_RECP_RETURN_INVEST = Column(Numeric(20, 4), comment='取得投资收益收到的现金')
    NET_CASH_RECP_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定资产、无形资产和其他长期资产收回的现金净额')
    OTHER_CASH_RECP_RAL_INV_ACT = Column(Numeric(20, 4), comment='收到其他与投资活动有关的现金')
    SPE_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流入小计')
    CASH_PAID_INVEST = Column(Numeric(20, 4), comment='投资支付的现金')
    CASH_PAY_ACQ_CONST_FIOLTA = Column(Numeric(20, 4), comment='购建固定资产、无形资产和其他长期资产支付的现金')
    OTHER_CASH_PAY_RAL_INV_ACT = Column(Numeric(20, 4), comment='支付其他与投资活动有关的现金')
    SPE_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额')
    CASH_RECP_CAP_CONTRIB = Column(Numeric(20, 4), comment='吸收投资收到的现金')
    CASH_RECP_BORROW = Column(Numeric(20, 4), comment='取得借款收到的现金')
    PROC_ISSUE_BONDS = Column(Numeric(20, 4), comment='发行债券收到的现金')
    OTHER_CASH_RECP_RAL_FNC_ACT = Column(Numeric(20, 4), comment='收到其他与筹资活动有关的现金')
    STOT_CASH_INFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流入小计')
    CASH_PREPAY_AMT_BORR = Column(Numeric(20, 4), comment='偿还债务支付的现金')
    CASH_PAY_DIST_DPCP_INT_EXP = Column(Numeric(20, 4), comment='分配股利、利润或偿付利息支付的现金')
    OTHER_CASH_PAY_RAL_FNC_ACT = Column(Numeric(20, 4), comment='支付其他与筹资活动有关的现金')
    SPE_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额')
    EFF_FX_FLU_CASH = Column(Numeric(20, 4), comment='汇率变动对现金的影响')
    SPE_BAL_NETCASH_EQU_DIR = Column(Numeric(20, 4), comment='现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_DIR = Column(Numeric(20, 4), comment='现金净增加额差额(合计平衡项目)')
    NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物净增加额')
    CASH_CASH_EQU_BEG_PERIOD = Column(Numeric(20, 4), comment='期初现金及现金等价物余额')
    CASH_CASH_EQU_END_PERIOD = Column(Numeric(20, 4), comment='期末现金及现金等价物余额')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
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
    SPE_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(合计平衡项目)')
    IM_NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='间接法-经营活动产生的现金流量净额')
    CONV_DEBT_INTO_CAP = Column(Numeric(20, 4), comment='债务转为资本')
    CONV_CORP_BONDS_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的可转换公司债券')
    FA_FNC_LEASES = Column(Numeric(20, 4), comment='融资租入固定资产')
    END_BAL_CASH = Column(Numeric(20, 4), comment='现金的期末余额')
    LESS_BEG_BAL_CASH = Column(Numeric(20, 4), comment='减：现金的期初余额')
    PLUS_END_BAL_CASH_EQU = Column(Numeric(20, 4), comment='加：现金等价物的期末余额')
    LESS_BEG_BAL_CASH_EQU = Column(Numeric(20, 4), comment='减：现金等价物的期初余额')
    SPE_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(合计平衡项目)')
    IM_NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='间接法-现金及现金等价物净增加额')
    SPE_OUT_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(特殊报表科目)')
    TOT_OUT_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(合计平衡项目)')


class UNLISTEDBANKINCOME(Base):
    """非上市银行利润表"""
    __tablename__ = 'UNLISTEDBANKINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    NET_PROFIT_AFTER_DED_NR_LP = Column(Numeric(20, 4), comment='扣除非经常性损益后净利润')
    NET_PROFIT_UNDER_INTL_ACC_STA = Column(Numeric(20, 4), comment='国际会计准则净利润')
    S_FA_EPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益')
    S_FA_EPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入')
    NET_INT_INC = Column(Numeric(20, 4), comment='利息净收入')
    INT_INC = Column(Numeric(20, 4), comment='利息收入')
    LESS_INT_EXP = Column(Numeric(20, 4), comment='减:利息支出')
    NET_HANDLING_CHRG_COMM_INC = Column(Numeric(20, 4), comment='手续费及佣金净收入')
    HANDLING_CHRG_COMM_INC = Column(Numeric(20, 4), comment='手续费及佣金收入')
    LESS_HANDLING_CHRG_COMM_EXP = Column(Numeric(20, 4), comment='减:手续费及佣金支出')
    PLUS_NET_INVEST_INC = Column(Numeric(20, 4), comment='加:投资净收益')
    INCL_INC_INVEST_ASSOC_JV_ENTP = Column(Numeric(20, 4), comment='其中：对联营企业和合营企业的投资收益')
    PLUS_NET_GAIN_CHG_FV = Column(Numeric(20, 4), comment='加:公允价值变动净收益')
    NET_INC_OTHER_OPS = Column(Numeric(20, 4), comment='其他经营净收益')
    PLUS_NET_GAIN_FX_TRANS = Column(Numeric(20, 4), comment='加:汇兑净收益')
    PLUS_NET_INC_OTHER_BUS = Column(Numeric(20, 4), comment='加:其他业务净收益')
    OTHER_BUS_INC = Column(Numeric(20, 4), comment='其他业务收入')
    OTHER_BUS_COST = Column(Numeric(20, 4), comment='其他业务成本')
    OPER_EXP = Column(Numeric(20, 4), comment='营业支出')
    LESS_TAXES_SURCHARGES_OPS = Column(Numeric(20, 4), comment='减:营业税金及附加')
    LESS_GERL_ADMIN_EXP = Column(Numeric(20, 4), comment='减:管理费用')
    LESS_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='减:资产减值损失')
    SPE_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(特殊报表科目)')
    TOT_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(合计平衡项目)')
    OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    PLUS_NON_OPER_REV = Column(Numeric(20, 4), comment='加:营业外收入')
    LESS_NON_OPER_EXP = Column(Numeric(20, 4), comment='减：营业外支出')
    IL_NET_LOSS_DISP_NONCUR_ASSET = Column(Numeric(20, 4), comment='其中：减：非流动资产处置净损失')
    SPE_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(特殊报表科目)')
    TOT_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(合计平衡项目)')
    TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    INC_TAX = Column(Numeric(20, 4), comment='所得税')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认投资损失')
    SPE_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(特殊报表科目)')
    TOT_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(合计平衡项目)')
    NET_PROFIT_INCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(含少数股东损益)')
    NET_PROFIT_EXCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(不含少数股东损益)')
    OTHER_COMPREH_INC = Column(Numeric(20, 4), comment='其他综合收益')
    TOT_COMPREH_INC = Column(Numeric(20, 4), comment='综合收益总额')
    TOT_COMPREH_INC_MIN_SHRHLDR = Column(Numeric(20, 4), comment='综合收益总额(少数股东)')
    TOT_COMPREH_INC_PARENT_COMP = Column(Numeric(20, 4), comment='综合收益总额(母公司)')
    MINORITY_INT_INC = Column(Numeric(20, 4), comment='少数股东损益')
    OTHER_INCOME = Column(Numeric(20, 4), comment='其他收益')
    MEMO = Column(VARCHAR(1000), comment='备注')


class UNLISTEDBANKINDICATOR(Base):
    """非上市银行专用指标"""
    __tablename__ = 'UNLISTEDBANKINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='资本充足率')
    CORE_CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='核心资本充足率')
    NPL_RATIO = Column(Numeric(20, 4), comment='不良贷款比例')
    LOAN_DEPO_RATIO = Column(Numeric(20, 4), comment='存贷款比例')
    LOAN_DEPO_RATIO_RMB = Column(Numeric(20, 4), comment='存贷款比例(人民币)')
    LOAN_DEPO_RATIO_NORMB = Column(Numeric(20, 4), comment='存贷款比例(外币)')
    ST_ASSET_LIQ_RATIO_RMB = Column(Numeric(20, 4), comment='短期资产流动性比例(人民币)')
    ST_ASSET_LIQ_RATIO_NORMB = Column(Numeric(20, 4), comment='短期资产流动性比例(外币)')
    LOAN_FROM_BANKS_RATIO = Column(Numeric(20, 4), comment='拆入资金比例')
    LEND_TO_BANKS_RATIO = Column(Numeric(20, 4), comment='拆出资金比例')
    LARGEST_CUSTOMER_LOAN = Column(Numeric(20, 4), comment='单一客户贷款比例')
    TOP_TEN_CUSTOMER_LOAN = Column(Numeric(20, 4), comment='最大十家客户贷款比例')
    TOTAL_LOAN = Column(Numeric(20, 4), comment='贷款总额')
    TOTAL_DEPOSIT = Column(Numeric(20, 4), comment='存款总额')
    LOAN_LOSS_PROVISION = Column(Numeric(20, 4), comment='贷款呆账准备金')
    BAD_LOAD_FIVE_CLASS = Column(Numeric(20, 4), comment='不良贷款余额（5级分类）')
    NPL_PROVISION_COVERAGE = Column(Numeric(20, 4), comment='不良贷款拨备覆盖率')
    COST_INCOME_RATIO = Column(Numeric(20, 4), comment='成本收入比')
    NON_INTEREST_MARGIN = Column(Numeric(20, 4), comment='非利息收入占比')
    NET_CAPITAL = Column(Numeric(20, 4), comment='资本净额')
    CORE_CAPI_NET_AMOUNT = Column(Numeric(20, 4), comment='核心资本净额')
    RISK_WEIGHT_ASSET = Column(Numeric(20, 4), comment='加权风险资本净额')
    INTEREST_BEARING_ASSET = Column(Numeric(20, 4), comment='生息资产')
    INTEREST_BEARING_ASSET_COMP = Column(Numeric(20, 4), comment='生息资产(计算值)')
    INTEREST_BEARING_LIA = Column(Numeric(20, 4), comment='计息负债')
    INTEREST_BEARING_LIA_COMP = Column(Numeric(20, 4), comment='计息负债(计算值)')
    NON_INTEREST_INCOME = Column(Numeric(20, 4), comment='非利息收入')
    NONEANING_ASSET = Column(Numeric(20, 4), comment='非生息资产')
    NONEANING_LIA = Column(Numeric(20, 4), comment='非计息负债')
    NET_INTEREST_MARGIN = Column(Numeric(20, 4), comment='净息差')
    NET_INTEREST_MARGIN_IS_ANN = Column(Numeric(20, 4), comment='净息差是否公布值')
    NET_INTEREST_SPREAD = Column(Numeric(20, 4), comment='净利差')
    NET_INTEREST_SPREAD_IS_ANN = Column(Numeric(20, 4), comment='净利差是否公布值')
    OVERDUE_LOAN = Column(Numeric(20, 4), comment='逾期贷款')
    TOTAL_INTEREST_INCOME = Column(Numeric(20, 4), comment='总利息收入')
    TOTAL_INTEREST_EXP = Column(Numeric(20, 4), comment='总利息支出')
    CASH_ON_HAND = Column(Numeric(20, 4), comment='库存现金')
    LONGTERM_LOANS_RATIO_CNY = Column(Numeric(20, 4), comment='中长期贷款比例（人民币）')
    LONGTERM_LOANS_RATIO_FC = Column(Numeric(20, 4), comment='中长期贷款比例（外币）')
    IBUSINESS_LOAN_RATIO = Column(Numeric(20, 4), comment='国际商业借款比例')
    INTERECT_COLLECTION_RATIO = Column(Numeric(20, 4), comment='利息回收率')
    CASH_RESERVE_RATIO_CNY = Column(Numeric(20, 4), comment='备付金比例（人民币）')
    CASH_RESERVE_RATIO_FC = Column(Numeric(20, 4), comment='备付金比例（外币）')
    OVERSEAS_FUNDS_APP_RATIO = Column(Numeric(20, 4), comment='境外资金运用比例')
    MARKET_RISK_CAPITAL = Column(Numeric(20, 4), comment='市场风险资本')
    INTEREST_BEARING_ASSET_IFPUB = Column(Numeric(1, 0), comment='生息资产是否是发布值')
    INTEREST_BEARING_LIA_IFPUB = Column(Numeric(1, 0), comment='计息负债是否是发布值')
    NET_INTEREST_MARGIN_IFPUB = Column(Numeric(1, 0), comment='净利差是否是发布值')
    CORETIER1CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='核心一级资本充足率')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    TIER1CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='一级资本充足率')
    CAPI_ADE_RATIO_2013 = Column(Numeric(20, 4), comment='资本充足率(资本管理办法)')
    NET_CAPITAL_2013 = Column(Numeric(20, 4), comment='资本净额(资本管理办法)')
    TIER1_NET_CAPI = Column(Numeric(20, 4), comment='一级资本净额')
    CORETIER1_NET_CAPI = Column(Numeric(20, 4), comment='核心一级资本净额')


class UNLISTEDBROKERBALANCESHEET(Base):
    """非上市券商资产负债表"""
    __tablename__ = 'UNLISTEDBROKERBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    MONETARY_CAP = Column(Numeric(20, 4), comment='货币资金')
    CLIENTS_CAP_DEPOSIT = Column(Numeric(20, 4), comment='客户资金存款')
    SETTLE_RSRV = Column(Numeric(20, 4), comment='结算备付金')
    CLIENTS_RSRV_SETTLE = Column(Numeric(20, 4), comment='客户备付金')
    LOANS_TO_OTH_BANKS = Column(Numeric(20, 4), comment='拆出资金')
    TRADABLE_FIN_ASSETS = Column(Numeric(20, 4), comment='交易性金融资产')
    DERIVATIVE_FIN_ASSETS = Column(Numeric(20, 4), comment='衍生金融资产')
    RED_MONETARY_CAP_FOR_SALE = Column(Numeric(20, 4), comment='买入返售金融资产')
    INT_RCV = Column(Numeric(20, 4), comment='应收利息')
    MRGN_PAID = Column(Numeric(20, 4), comment='存出保证金')
    AGENCY_BUS_ASSETS = Column(Numeric(20, 4), comment='代理业务资产')
    FIN_ASSETS_AVAIL_FOR_SALE = Column(Numeric(20, 4), comment='可供出售金融资产')
    HELD_TO_MTY_INVEST = Column(Numeric(20, 4), comment='持有至到期投资')
    LONG_TERM_EQY_INVEST = Column(Numeric(20, 4), comment='长期股权投资')
    FIX_ASSETS = Column(Numeric(20, 4), comment='固定资产')
    INTANG_ASSETS = Column(Numeric(20, 4), comment='无形资产')
    INCL_SEAT_FEES_EXCHANGE = Column(Numeric(20, 4), comment='其中：交易席位费')
    GOODWILL = Column(Numeric(20, 4), comment='商誉')
    DEFERRED_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产')
    INVEST_REAL_ESTATE = Column(Numeric(20, 4), comment='投资性房地产')
    OTH_ASSETS = Column(Numeric(20, 4), comment='其他资产')
    SPE_BAL_ASSETS = Column(Numeric(20, 4), comment='资产差额(特殊报表科目)')
    TOT_BAL_ASSETS = Column(Numeric(20, 4), comment='资产差额(合计平衡项目)')
    TOT_ASSETS = Column(Numeric(20, 4), comment='资产总计')
    ST_BORROW = Column(Numeric(20, 4), comment='短期借款')
    INCL_PLEDGE_LOAN = Column(Numeric(20, 4), comment='其中：质押借款')
    LOANS_OTH_BANKS = Column(Numeric(20, 4), comment='拆入资金')
    TRADABLE_FIN_LIAB = Column(Numeric(20, 4), comment='交易性金融负债')
    DERIVATIVE_FIN_LIAB = Column(Numeric(20, 4), comment='衍生金融负债')
    FUND_SALES_FIN_ASSETS_RP = Column(Numeric(20, 4), comment='卖出回购金融资产款')
    ACTING_TRADING_SEC = Column(Numeric(20, 4), comment='代理买卖证券款')
    ACTING_UW_SEC = Column(Numeric(20, 4), comment='代理承销证券款')
    EMPL_BEN_PAYABLE = Column(Numeric(20, 4), comment='应付职工薪酬')
    TAXES_SURCHARGES_PAYABLE = Column(Numeric(20, 4), comment='应交税费')
    INT_PAYABLE = Column(Numeric(20, 4), comment='应付利息')
    AGENCY_BUS_LIAB = Column(Numeric(20, 4), comment='代理业务负债')
    LT_BORROW = Column(Numeric(20, 4), comment='长期借款')
    BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付债券')
    DEFERRED_TAX_LIAB = Column(Numeric(20, 4), comment='延所得税负债')
    PROVISIONS = Column(Numeric(20, 4), comment='预计负债')
    OTH_LIAB = Column(Numeric(20, 4), comment='其他负债')
    SPE_BAL_LIAB = Column(Numeric(20, 4), comment='负债差额(特殊报表科目)')
    TOT_BAL_LIAB = Column(Numeric(20, 4), comment='负债差额(合计平衡项目)')
    TOT_LIAB = Column(Numeric(20, 4), comment='负债合计')
    CAP_STK = Column(Numeric(20, 4), comment='股本')
    CAP_RSRV = Column(Numeric(20, 4), comment='资本公积金')
    LESS_TSY_STK = Column(Numeric(20, 4), comment='减：库存股')
    SURPLUS_RSRV = Column(Numeric(20, 4), comment='盈余公积金')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='未分配利润')
    PROV_NOM_RISKS = Column(Numeric(20, 4), comment='一般风险准备')
    CNVD_DIFF_FOREIGN_CURR_STAT = Column(Numeric(20, 4), comment='外币报表折算差额')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认的投资损失')
    SPE_BAL_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益差额(特殊报表科目)')
    TOT_BAL_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益差额(合计平衡项目)')
    MINORITY_INT = Column(Numeric(20, 4), comment='少数股东权益')
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(不含少数股东权益)')
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(含少数股东权益)')
    SPE_BAL_LIAB_EQY = Column(Numeric(20, 4), comment='负债及股东权益差额(特殊报表项目)')
    TOT_BAL_LIAB_EQY = Column(Numeric(20, 4), comment='负债及股东权益差额(合计平衡项目)')
    TOT_LIAB_SHRHLDR_EQY = Column(Numeric(20, 4), comment='负债及股东权益总计')
    OTHER_COMP_INCOME = Column(Numeric(20, 4), comment='其他综合收益')
    OTHER_EQUITY_TOOLS = Column(Numeric(20, 4), comment='其他权益工具')
    OTHER_EQUITY_TOOLS_P_SHR = Column(Numeric(20, 4), comment='其他权益工具:优先股')
    MELT_MONEY = Column(Numeric(20, 4), comment='融出资金')
    RECEIVABLES = Column(Numeric(20, 4), comment='应收款项')
    SHORT_TERM_FINANCING = Column(Numeric(20, 4), comment='应付短期融资款')
    PAYABLES = Column(Numeric(20, 4), comment='应付款项')


class UNLISTEDBROKERCASHFLOW(Base):
    """非上市券商现金流量表"""
    __tablename__ = 'UNLISTEDBROKERCASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    FREE_CASH_FLOW = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    NET_INCR_DISP_TFA = Column(Numeric(20, 4), comment='处置交易性金融资产净增加额')
    NET_INCR_DISP_FAAS = Column(Numeric(20, 4), comment='处置可供出售金融资产净增加额')
    NET_INCR_INT_HANDLING_CHRG = Column(Numeric(20, 4), comment='收取利息和手续费净增加额')
    NET_INCR_LOANS_OTHER_BANK = Column(Numeric(20, 4), comment='拆入资金净增加额')
    NET_INCR_REPURCH_BUS_FUND = Column(Numeric(20, 4), comment='回购业务资金净增加额')
    OTHER_CASH_RECP_RAL_OPER_ACT = Column(Numeric(20, 4), comment='收到其他与经营活动有关的现金')
    SPE_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流入小计')
    CASH_PAY_BEH_EMPL = Column(Numeric(20, 4), comment='支付给职工以及为职工支付的现金')
    PAY_ALL_TYP_TAX = Column(Numeric(20, 4), comment='支付的各项税费')
    OTHER_CASH_PAY_RAL_OPER_ACT = Column(Numeric(20, 4), comment='支付其他与经营活动有关的现金')
    HANDLING_CHRG_PAID = Column(Numeric(20, 4), comment='支付手续费的现金')
    SPE_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额')
    CASH_RECP_DISP_WITHDRWL_INVEST = Column(Numeric(20, 4), comment='收回投资收到的现金')
    CASH_RECP_RETURN_INVEST = Column(Numeric(20, 4), comment='取得投资收益收到的现金')
    NET_CASH_RECP_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定资产、无形资产和其他长期资产收回的现金净额')
    OTHER_CASH_RECP_RAL_INV_ACT = Column(Numeric(20, 4), comment='收到其他与投资活动有关的现金')
    SPE_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流入小计')
    CASH_PAID_INVEST = Column(Numeric(20, 4), comment='投资支付的现金')
    CASH_PAY_ACQ_CONST_FIOLTA = Column(Numeric(20, 4), comment='购建固定资产、无形资产和其他长期资产支付的现金')
    OTHER_CASH_PAY_RAL_INV_ACT = Column(Numeric(20, 4), comment='支付其他与投资活动有关的现金')
    SPE_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额')
    CASH_RECP_CAP_CONTRIB = Column(Numeric(20, 4), comment='吸收投资收到的现金')
    CASH_RECP_BORROW = Column(Numeric(20, 4), comment='取得借款收到的现金')
    PROC_ISSUE_BONDS = Column(Numeric(20, 4), comment='发行债券收到的现金')
    OTHER_CASH_RECP_RAL_FNC_ACT = Column(Numeric(20, 4), comment='收到其他与筹资活动有关的现金')
    SPE_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流入小计')
    CASH_PREPAY_AMT_BORR = Column(Numeric(20, 4), comment='偿还债务支付的现金')
    CASH_PAY_DIST_DPCP_INT_EXP = Column(Numeric(20, 4), comment='分配股利、利润或偿付利息支付的现金')
    OTHER_CASH_PAY_RAL_FNC_ACT = Column(Numeric(20, 4), comment='支付其他与筹资活动有关的现金')
    SPE_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额')
    EFF_FX_FLU_CASH = Column(Numeric(20, 4), comment='汇率变动对现金的影响')
    SPE_BAL_NETCASH_EQU_DIR = Column(Numeric(20, 4), comment='现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_DIR = Column(Numeric(20, 4), comment='现金净增加额差额(合计平衡项目)')
    NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物净增加额')
    CASH_CASH_EQU_BEG_PERIOD = Column(Numeric(20, 4), comment='期初现金及现金等价物余额')
    CASH_CASH_EQU_END_PERIOD = Column(Numeric(20, 4), comment='期末现金及现金等价物余额')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
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
    SPE_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(合计平衡项目)')
    IM_NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='间接法-经营活动产生的现金流量净额')
    CONV_DEBT_INTO_CAP = Column(Numeric(20, 4), comment='债务转为资本')
    CONV_CORP_BONDS_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的可转换公司债券')
    FA_FNC_LEASES = Column(Numeric(20, 4), comment='融资租入固定资产')
    END_BAL_CASH = Column(Numeric(20, 4), comment='现金的期末余额')
    LESS_BEG_BAL_CASH = Column(Numeric(20, 4), comment='减：现金的期初余额')
    PLUS_END_BAL_CASH_EQU = Column(Numeric(20, 4), comment='加：现金等价物的期末余额')
    LESS_BEG_BAL_CASH_EQU = Column(Numeric(20, 4), comment='减：现金等价物的期初余额')
    SPE_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(合计平衡项目)')
    IM_NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='间接法-现金及现金等价物净增加额')
    AGENT_TRADING_SC_NET_CASH = Column(Numeric(20, 4), comment='代理买卖证券收到的现金净额')
    MELT_MONEY_NET_INCREASE = Column(Numeric(20, 4), comment='融出资金净增加额')


class UNLISTEDBROKERINCOME(Base):
    """非上市券商利润表"""
    __tablename__ = 'UNLISTEDBROKERINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    NET_PROFIT_AFTER_DED_NR_LP = Column(Numeric(20, 4), comment='扣除非经常性损益后净利润')
    NET_PROFIT_UNDER_INTL_ACC_STA = Column(Numeric(20, 4), comment='国际会计准则净利润')
    S_FA_EPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益')
    S_FA_EPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入')
    HANDLING_CHRG_COMM_INC = Column(Numeric(20, 4), comment='手续费及佣金收入')
    NET_INC_SEC_TRADING_BROK_BUS = Column(Numeric(20, 4), comment='代理买卖证券业务净收入')
    NET_INC_SEC_UW_BUS = Column(Numeric(20, 4), comment='证券承销业务净收入')
    NET_INC_EC_ASSET_MGMT_BUS = Column(Numeric(20, 4), comment='受托客户资产管理业务净收入')
    NET_INT_INC = Column(Numeric(20, 4), comment='利息净收入')
    PLUS_NET_INVEST_INC = Column(Numeric(20, 4), comment='加:投资净收益')
    INCL_INC_INVEST_ASSOC_JV_ENTP = Column(Numeric(20, 4), comment='其中：对联营企业和合营企业的投资收益')
    PLUS_NET_GAIN_CHG_FV = Column(Numeric(20, 4), comment='加:公允价值变动净收益')
    PLUS_NET_GAIN_FX_TRANS = Column(Numeric(20, 4), comment='加:汇兑净收益')
    OTHER_BUS_INC = Column(Numeric(20, 4), comment='其他业务收入')
    OPER_EXP = Column(Numeric(20, 4), comment='营业支出')
    LESS_TAXES_SURCHARGES_OPS = Column(Numeric(20, 4), comment='减:营业税金及附加')
    LESS_GERL_ADMIN_EXP = Column(Numeric(20, 4), comment='减:管理费用')
    LESS_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='减:资产减值损失')
    OTHER_BUS_COST = Column(Numeric(20, 4), comment='其他业务成本')
    SPE_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(特殊报表科目)')
    TOT_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(合计平衡项目)')
    OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    PLUS_NON_OPER_REV = Column(Numeric(20, 4), comment='加:营业外收入')
    LESS_NON_OPER_EXP = Column(Numeric(20, 4), comment='减：营业外支出')
    IL_NET_LOSS_DISP_NONCUR_ASSET = Column(Numeric(20, 4), comment='其中：减：非流动资产处置净损失')
    SPE_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(特殊报表科目)')
    TOT_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(合计平衡项目)')
    TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    INC_TAX = Column(Numeric(20, 4), comment='所得税')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认投资损失')
    SPE_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(特殊报表科目)')
    TOT_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(合计平衡项目)')
    NET_PROFIT_INCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(含少数股东损益)')
    NET_PROFIT_EXCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(不含少数股东损益)')
    MINORITY_INT_INC = Column(Numeric(20, 4), comment='少数股东损益')
    OTHER_COMPREH_INC = Column(Numeric(20, 4), comment='其他综合收益')
    TOT_COMPREH_INC = Column(Numeric(20, 4), comment='综合收益总额')
    TOT_COMPREH_INC_MIN_SHRHLDR = Column(Numeric(20, 4), comment='综合收益总额(少数股东)')
    TOT_COMPREH_INC_PARENT_COMP = Column(Numeric(20, 4), comment='综合收益总额(母公司)')
    FEEANDCOMINC = Column(Numeric(20, 4), comment='手续费及佣金净收入')
    OTHER_INCOME = Column(Numeric(20, 4), comment='其他收益')
    MEMO = Column(VARCHAR(1000), comment='备注')


class UNLISTEDIBROKERINDICATOR(Base):
    """非上市券商专用指标"""
    __tablename__ = 'UNLISTEDIBROKERINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    ANN_DT = Column(VARCHAR(8), comment='报告期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='公告日期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    IFLISTED_DATA = Column(Numeric(5, 0), comment='是否上市后数据')
    NET_CAPITAL = Column(Numeric(20, 4), comment='净资本')
    TRUSTED_CAPITAL = Column(Numeric(20, 4), comment='受托资金')
    NET_GEARING_RATIO = Column(Numeric(20, 4), comment='净资本负债率(%)')
    PROP_EQUITY_RATIO = Column(Numeric(20, 4), comment='自营权益类证券比例')
    LONGTERM_INVEST_RATIO = Column(Numeric(20, 4), comment='长期投资比例')
    FIXED_CAPITAL_RATIO = Column(Numeric(20, 4), comment='固定资本比例')
    FEE_BUSINESS_RATIO = Column(Numeric(20, 4), comment='营业费用率')
    TOTAL_CAPITAL_RETURN = Column(Numeric(20, 4), comment='总资产收益率')
    NET_CAPITAL_YIELD = Column(Numeric(20, 4), comment='净资本收益率')
    CURRENT_RATIO = Column(Numeric(20, 4), comment='流动比率')
    ASSET_LIABILITY_RATIO = Column(Numeric(20, 4), comment='资产负债率')
    ASSET_TURNOVER_RATIO = Column(Numeric(20, 4), comment='资产周转率')
    NET_CAPITAL_RETURN = Column(Numeric(20, 4), comment='净资产收益率')
    CONTINGENT_LIABILITY_RATIO = Column(Numeric(20, 4), comment='或有负债(担保）比率')
    PROP_SECURITIES = Column(Numeric(20, 4), comment='自营证券')
    TREASURY_BOND = Column(Numeric(20, 4), comment='国债')
    INVESTMENT_FUNDS = Column(Numeric(20, 4), comment='投资基金')
    STOCKS = Column(Numeric(20, 4), comment='股票')
    CONVERTIBLE_BOND = Column(Numeric(20, 4), comment='可转债')
    PER_CAPITA_PROFITS = Column(Numeric(20, 4), comment='人均利润')
    NET_CAP_TOTAL_RISKPROV = Column(Numeric(20, 4), comment='风险覆盖率')
    NET_CAP_NET_ASSETS = Column(Numeric(20, 4), comment='净资本/净资产')
    PROP_EQU_DER_NETCAP = Column(Numeric(20, 4), comment='自营权益类证券及证券衍生品/净资本')
    PROP_FIXEDINCOME_NETCAP = Column(Numeric(20, 4), comment='自营固定收益类证券/净资本')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    CAPITAL_LEVERAGE_RATIO = Column(Numeric(20, 4), comment='资本杠杆率')
    LIQUIDITY_COVERAGE = Column(Numeric(20, 4), comment='流动性覆盖率')
    NET_STABLE_CAPITAL_RATIO = Column(Numeric(20, 4), comment='净稳定资金率')
    NET_ASSETS_LIABILITIES_RATIO = Column(Numeric(20, 4), comment='净资产/负债')


class UNLISTEDINSURANCEBALANCESHEET(Base):
    """非上市保险资产负债表"""
    __tablename__ = 'UNLISTEDINSURANCEBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    MONETARY_CAP = Column(Numeric(20, 4), comment='货币资金')
    LOANS_TO_OTH_BANKS = Column(Numeric(20, 4), comment='拆出资金')
    TRADABLE_FIN_ASSETS = Column(Numeric(20, 4), comment='交易性金融资产')
    DERIVATIVE_FIN_ASSETS = Column(Numeric(20, 4), comment='衍生金融资产')
    RED_MONETARY_CAP_FOR_SALE = Column(Numeric(20, 4), comment='买入返售金融资产')
    PREM_RCV = Column(Numeric(20, 4), comment='应收保费')
    INT_RCV = Column(Numeric(20, 4), comment='应收利息')
    SUBR_REC = Column(Numeric(20, 4), comment='应收代位追偿款')
    PAYABLE_TO_REINSURER = Column(Numeric(20, 4), comment='应付分保账款')
    RCV_CEDED_UNEARNED_PREM_RSRV = Column(Numeric(20, 4), comment='应收分保未到期责任准备金')
    RCV_CEDED_CLAIM_RSRV = Column(Numeric(20, 4), comment='应收分保未决赔款准备金')
    RCV_CEDED_LIFE_INSUR_RSRV = Column(Numeric(20, 4), comment='应收分保寿险责任准备金')
    RCV_CEDED_LT_HEALTH_INSUR_RSRV = Column(Numeric(20, 4), comment='应收分保长期健康险责任准备金')
    INSURED_PLEDGE_LOAN = Column(Numeric(20, 4), comment='保户质押贷款')
    FIN_ASSETS_AVAIL_FOR_SALE = Column(Numeric(20, 4), comment='可供出售金融资产')
    HELD_TO_MTY_INVEST = Column(Numeric(20, 4), comment='持有至到期投资')
    LONG_TERM_EQY_INVEST = Column(Numeric(20, 4), comment='长期股权投资')
    CAP_MRGN_PAID = Column(Numeric(20, 4), comment='存出资本保证金')
    RCV_INVEST = Column(Numeric(20, 4), comment='应收款项类投资')
    FIX_ASSETS = Column(Numeric(20, 4), comment='固定资产')
    INTANG_ASSETS = Column(Numeric(20, 4), comment='无形资产')
    GOODWILL = Column(Numeric(20, 4), comment='商誉')
    INDEPENDENT_ACCT_ASSETS = Column(Numeric(20, 4), comment='独立账户资产')
    DEFERRED_TAX_LIAB = Column(Numeric(20, 4), comment='递延所得税负债')
    INVEST_REAL_ESTATE = Column(Numeric(20, 4), comment='投资性房地产')
    TIME_DEPOSITS = Column(Numeric(20, 4), comment='定期存款')
    OTH_ASSETS = Column(Numeric(20, 4), comment='其他资产')
    SPE_BAL_ASSETS = Column(Numeric(20, 4), comment='资产差额(特殊报表科目)')
    TOT_BAL_ASSETS = Column(Numeric(20, 4), comment='资产差额(合计平衡项目)')
    TOT_ASSETS = Column(Numeric(20, 4), comment='资产总计')
    ST_BORROW = Column(Numeric(20, 4), comment='短期借款')
    LOANS_OTH_BANKS = Column(Numeric(20, 4), comment='拆入资金')
    TRADABLE_FIN_LIAB = Column(Numeric(20, 4), comment='交易性金融负债')
    FUND_SALES_FIN_ASSETS_RP = Column(Numeric(20, 4), comment='卖出回购金融资产款')
    PREM_RECEIVED_ADV = Column(Numeric(20, 4), comment='预收保费')
    HANDLING_CHARGES_COMM_PAYABLE = Column(Numeric(20, 4), comment='应付手续费及佣金')
    EMPL_BEN_PAYABLE = Column(Numeric(20, 4), comment='应付职工薪酬')
    TAXES_SURCHARGES_PAYABLE = Column(Numeric(20, 4), comment='应交税费')
    INT_PAYABLE = Column(Numeric(20, 4), comment='应付利息')
    CLAIMS_PAYABLE = Column(Numeric(20, 4), comment='应付赔付款')
    DVD_PAYABLE_INSURED = Column(Numeric(20, 4), comment='应付保单红利')
    DEPOSIT_RECEIVED = Column(Numeric(20, 4), comment='存入保证金')
    INSURED_DEPOSIT_INVEST = Column(Numeric(20, 4), comment='保户储金及投资款')
    UNEARNED_PREM_RSRV = Column(Numeric(20, 4), comment='未到期责任准备金')
    OUT_LOSS_RSRV = Column(Numeric(20, 4), comment='未决赔款准备金')
    LIFE_INSUR_RSRV = Column(Numeric(20, 4), comment='寿险责任准备金')
    LT_HEALTH_INSUR_V = Column(Numeric(20, 4), comment='长期健康险责任准备金')
    LT_BORROW = Column(Numeric(20, 4), comment='长期借款')
    BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付债券')
    INDEPENDENT_ACCT_LIAB = Column(Numeric(20, 4), comment='独立账户负债')
    DEFERRED_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产')
    PROVISIONS = Column(Numeric(20, 4), comment='预计负债')
    OTH_LIAB = Column(Numeric(20, 4), comment='其他负债')
    SPE_BAL_LIAB = Column(Numeric(20, 4), comment='负债差额(特殊报表科目)')
    TOT_BAL_LIAB = Column(Numeric(20, 4), comment='负债差额(合计平衡项目)')
    TOT_LIAB = Column(Numeric(20, 4), comment='负债合计')
    CAP_STK = Column(Numeric(20, 4), comment='股本')
    CAP_RSRV = Column(Numeric(20, 4), comment='资本公积金')
    LESS_TSY_STK = Column(Numeric(20, 4), comment='减：库存股')
    SURPLUS_RSRV = Column(Numeric(20, 4), comment='盈余公积金')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='未分配利润')
    PROV_NOM_RISKS = Column(Numeric(20, 4), comment='一般风险准备')
    CNVD_DIFF_FOREIGN_CURR_STAT = Column(Numeric(20, 4), comment='外币报表折算差额')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认的投资损失')
    SPE_BAL_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益差额(特殊报表科目)')
    TOT_BAL_SHRHLDR_EQY = Column(Numeric(20, 4), comment='股东权益差额(合计平衡项目)')
    MINORITY_INT = Column(Numeric(20, 4), comment='少数股东权益')
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(不含少数股东权益)')
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(含少数股东权益)')
    SPE_BAL_LIAB_EQY = Column(Numeric(20, 4), comment='负债及股东权益差额(特殊报表项目)')
    TOT_BAL_LIAB_EQY = Column(Numeric(20, 4), comment='负债及股东权益差额(合计平衡项目)')
    TOT_LIAB_SHRHLDR_EQY = Column(Numeric(20, 4), comment='负债及股东权益总计')
    OTHER_COMP_INCOME = Column(Numeric(20, 4), comment='其他综合收益')
    OTHER_EQUITY_TOOLS = Column(Numeric(20, 4), comment='其他权益工具')
    OTHER_EQUITY_TOOLS_P_SHR = Column(Numeric(20, 4), comment='其他权益工具:优先股')
    DERIVATIVE_FINANCE_DEBT = Column(Numeric(20, 4), comment='衍生金融负债')
    DIVIDEND = Column(Numeric(20, 4), comment='应收分保账款')


class UNLISTEDINSURANCECASHFLOW(Base):
    """非上市保险现金流量表"""
    __tablename__ = 'UNLISTEDINSURANCECASHFLOW'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    FREE_CASH_FLOW = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    CASH_RECP_PREM_ORIG_INCO = Column(Numeric(20, 4), comment='收到原保险合同保费取得的现金')
    NET_CASH_RECEIVED_REINSU_BUS = Column(Numeric(20, 4), comment='收到再保业务现金净额')
    OTHER_CASH_RECP_RAL_OPER_ACT = Column(Numeric(20, 4), comment='收到其他与经营活动有关的现金')
    NET_INCR_INSURED_DEP = Column(Numeric(20, 4), comment='保户储金净增加额')
    SPE_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流入小计')
    CASH_PAY_CLAIMS_ORIG_INCO = Column(Numeric(20, 4), comment='支付原保险合同赔付款项的现金')
    CASH_PAY_BEH_EMPL = Column(Numeric(20, 4), comment='支付给职工以及为职工支付的现金')
    HANDLING_CHRG_PAID = Column(Numeric(20, 4), comment='支付手续费的现金')
    PAY_ALL_TYP_TAX = Column(Numeric(20, 4), comment='支付的各项税费')
    OTHER_CASH_PAY_RAL_OPER_ACT = Column(Numeric(20, 4), comment='支付其他与经营活动有关的现金')
    COMM_INSUR_PLCY_PAID = Column(Numeric(20, 4), comment='支付保单红利的现金')
    SPE_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_OPER = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额')
    CASH_RECP_DISP_WITHDRWL_INVEST = Column(Numeric(20, 4), comment='收回投资收到的现金')
    CASH_RECP_RETURN_INVEST = Column(Numeric(20, 4), comment='取得投资收益收到的现金')
    NET_CASH_RECP_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定资产、无形资产和其他长期资产收回的现金净额')
    OTHER_CASH_RECP_RAL_INV_ACT = Column(Numeric(20, 4), comment='收到其他与投资活动有关的现金')
    SPE_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流入小计')
    CASH_PAID_INVEST = Column(Numeric(20, 4), comment='投资支付的现金')
    NET_INCR_PLEDGE_LOAN = Column(Numeric(20, 4), comment='质押贷款净增加额')
    CASH_PAY_ACQ_CONST_FIOLTA = Column(Numeric(20, 4), comment='购建固定资产、无形资产和其他长期资产支付的现金')
    OTHER_CASH_PAY_RAL_INV_ACT = Column(Numeric(20, 4), comment='支付其他与投资活动有关的现金')
    SPE_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_INV = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_INV_ACT = Column(Numeric(20, 4), comment='投资活动产生的现金流量净额')
    CASH_RECP_CAP_CONTRIB = Column(Numeric(20, 4), comment='吸收投资收到的现金')
    CASH_RECP_BORROW = Column(Numeric(20, 4), comment='取得借款收到的现金')
    PROC_ISSUE_BONDS = Column(Numeric(20, 4), comment='发行债券收到的现金')
    OTHER_CASH_RECP_RAL_FNC_ACT = Column(Numeric(20, 4), comment='收到其他与筹资活动有关的现金')
    SPE_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(特殊报表科目)')
    TOT_BAL_CASH_INFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流入差额(合计平衡项目)')
    STOT_CASH_INFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流入小计')
    CASH_PREPAY_AMT_BORR = Column(Numeric(20, 4), comment='偿还债务支付的现金')
    CASH_PAY_DIST_DPCP_INT_EXP = Column(Numeric(20, 4), comment='分配股利、利润或偿付利息支付的现金')
    OTHER_CASH_PAY_RAL_FNC_ACT = Column(Numeric(20, 4), comment='支付其他与筹资活动有关的现金')
    SPE_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(特殊报表科目)')
    TOT_BAL_CASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动现金流出差额(合计平衡项目)')
    STOT_CASH_OUTFLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动现金流出小计')
    TOT_BAL_NETCASH_OUTFLOWS_FNC = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额差额(合计平衡项目)')
    NET_CASH_FLOWS_FNC_ACT = Column(Numeric(20, 4), comment='筹资活动产生的现金流量净额')
    EFF_FX_FLU_CASH = Column(Numeric(20, 4), comment='汇率变动对现金的影响')
    SPE_BAL_NETCASH_EQU_DIR = Column(Numeric(20, 4), comment='现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_DIR = Column(Numeric(20, 4), comment='现金净增加额差额(合计平衡项目)')
    NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='现金及现金等价物净增加额')
    CASH_CASH_EQU_BEG_PERIOD = Column(Numeric(20, 4), comment='期初现金及现金等价物余额')
    CASH_CASH_EQU_END_PERIOD = Column(Numeric(20, 4), comment='期末现金及现金等价物余额')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
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
    SPE_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(特殊报表科目)')
    TOT_BAL_NETCASH_EQU_UNDIR = Column(Numeric(20, 4), comment='间接法-经营活动现金流量净额差额(合计平衡项目)')
    IM_NET_CASH_FLOWS_OPER_ACT = Column(Numeric(20, 4), comment='间接法-经营活动产生的现金流量净额')
    CONV_DEBT_INTO_CAP = Column(Numeric(20, 4), comment='债务转为资本')
    CONV_CORP_BONDS_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的可转换公司债券')
    FA_FNC_LEASES = Column(Numeric(20, 4), comment='融资租入固定资产')
    END_BAL_CASH = Column(Numeric(20, 4), comment='现金的期末余额')
    LESS_BEG_BAL_CASH = Column(Numeric(20, 4), comment='减：现金的期初余额')
    PLUS_END_BAL_CASH_EQU = Column(Numeric(20, 4), comment='加：现金等价物的期末余额')
    LESS_BEG_BAL_CASH_EQU = Column(Numeric(20, 4), comment='减：现金等价物的期初余额')
    SPE_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(特殊报表科目)')
    TOT_BAL_NETCASH_INC_UNDIR = Column(Numeric(20, 4), comment='间接法-现金净增加额差额(合计平衡项目)')
    IM_NET_INCR_CASH_CASH_EQU = Column(Numeric(20, 4), comment='间接法-现金及现金等价物净增加额')


class UNLISTEDINSURANCEINCOME(Base):
    """非上市保险利润表"""
    __tablename__ = 'UNLISTEDINSURANCEINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(10), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    NET_PROFIT_AFTER_DED_NR_LP = Column(Numeric(20, 4), comment='扣除非经常性损益后净利润')
    NET_PROFIT_UNDER_INTL_ACC_STA = Column(Numeric(20, 4), comment='国际会计准则净利润')
    S_FA_EPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益')
    S_FA_EPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入')
    INSUR_PREM_UNEARNED = Column(Numeric(20, 4), comment='已赚保费')
    PREM_INC = Column(Numeric(20, 4), comment='保费业务收入')
    INCL_REINSURANCE_PREM_INC = Column(Numeric(20, 4), comment='其中：分保费收入')
    LESS_CEDED_OUT_PREM = Column(Numeric(20, 4), comment='减：分出保费')
    CHG_UNEARNED_PREM_RES = Column(Numeric(20, 4), comment='提取未到期责任准备金')
    PLUS_NET_INVEST_INC = Column(Numeric(20, 4), comment='加:投资净收益')
    INCL_INC_INVEST_ASSOC_JV_ENTP = Column(Numeric(20, 4), comment='其中：对联营企业和合营企业的投资收益')
    PLUS_NET_GAIN_CHG_FV = Column(Numeric(20, 4), comment='加:公允价值变动净收益')
    PLUS_NET_GAIN_FX_TRANS = Column(Numeric(20, 4), comment='加:汇兑净收益')
    OPER_EXP = Column(Numeric(20, 4), comment='营业支出')
    PREPAY_SURR = Column(Numeric(20, 4), comment='退保金')
    TOT_CLAIM_EXP = Column(Numeric(20, 4), comment='赔付总支出')
    LESS_CLAIM_RECB_REINSURER = Column(Numeric(20, 4), comment='减：摊回赔付支出')
    LESS_INS_RSRV_RECB_REINSURER = Column(Numeric(20, 4), comment='减：摊回保险责任准备金')
    DVD_EXP_INSURED = Column(Numeric(20, 4), comment='保户红利支出')
    REINSURANCE_EXP = Column(Numeric(20, 4), comment='分保费用')
    LESS_TAXES_SURCHARGES_OPS = Column(Numeric(20, 4), comment='减:营业税金及附加')
    LESS_HANDLING_CHRG_COMM_EXP = Column(Numeric(20, 4), comment='减:手续费及佣金支出')
    LESS_GERL_ADMIN_EXP = Column(Numeric(20, 4), comment='减:管理费用')
    LESS_EXP_RECB_REINSURER = Column(Numeric(20, 4), comment='减：摊回分保费用')
    OTHER_BUS_COST = Column(Numeric(20, 4), comment='其他业务成本')
    LESS_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='减:资产减值损失')
    SPE_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(特殊报表科目)')
    TOT_BAL_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润差额(合计平衡项目)')
    OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    PLUS_NON_OPER_REV = Column(Numeric(20, 4), comment='加:营业外收入')
    LESS_NON_OPER_EXP = Column(Numeric(20, 4), comment='减：营业外支出')
    IL_NET_LOSS_DISP_NONCUR_ASSET = Column(Numeric(20, 4), comment='其中：减：非流动资产处置净损失')
    SPE_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(特殊报表科目)')
    TOT_BAL_TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额差额(合计平衡项目)')
    TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    INC_TAX = Column(Numeric(20, 4), comment='所得税')
    UNCONFIRMED_INVEST_LOSS = Column(Numeric(20, 4), comment='未确认投资损失')
    SPE_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(特殊报表科目)')
    TOT_BAL_NET_PROFIT = Column(Numeric(20, 4), comment='净利润差额(合计平衡项目)')
    NET_PROFIT_INCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(含少数股东损益)')
    NET_PROFIT_EXCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(不含少数股东损益)')
    MINORITY_INT_INC = Column(Numeric(20, 4), comment='少数股东损益')
    OTHER_OPERATING_INCOME = Column(Numeric(20, 4), comment='其他业务收入')
    INSURANCE_LIABILITY_RESERVE = Column(Numeric(20, 4), comment='提取保险责任准备金')
    OTHER_COMPREHENSIVE_INCOME = Column(Numeric(20, 4), comment='其他综合收益')
    TOTAL_COMPREHENSIVE_INCOME = Column(Numeric(20, 4), comment='综合收益总额')
    TOTAL_COMPREHENSIVE_INCOME1 = Column(Numeric(20, 4), comment='综合收益总额(母公司)')
    TOTAL_COMPREHENSIVE_INCOME2 = Column(Numeric(20, 4), comment='综合收益总额(少数股东)')
    OTHER_INCOME = Column(Numeric(20, 4), comment='其他收益')
    MEMO = Column(VARCHAR(1000), comment='备注')


class UNLISTEDINSURANCEINDICATOR(Base):
    """非上市保险专用指标"""
    __tablename__ = 'UNLISTEDINSURANCEINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型')
    CAP_ADEQUACY_RATIO_LIFE = Column(Numeric(20, 4), comment='寿险：偿付能力充足率')
    CAP_ADEQUACY_RATIO_PROPERTY = Column(Numeric(20, 4), comment='产险：偿付能力充足率')
    SURRENDER_RATE = Column(Numeric(20, 4), comment='退保率')
    POLICY_PERSISTENCY_RATE_13M = Column(Numeric(20, 4), comment='保单继续率-13个月')
    POLICY_PERSISTENCY_RATE_25M = Column(Numeric(20, 4), comment='保单继续率-25个月')
    POLICY_PERSISTENCY_RATE_14M = Column(Numeric(20, 4), comment='保单继续率-14个月')
    POLICY_PERSISTENCY_RATE_26M = Column(Numeric(20, 4), comment='保单继续率-26个月')
    NET_INVESTMENT_YIELD = Column(Numeric(20, 4), comment='净投资收益率')
    TOTAL_INVESTMENT_YIELD = Column(Numeric(20, 4), comment='总投资收益率')
    RISK_DISCOUNT_RATE = Column(Numeric(20, 4), comment='评估利率假设：风险贴现率')
    COMBINED_COST_PROPERTY = Column(Numeric(20, 4), comment='产险：综合成本率')
    LOSS_RATIO_PROPERTY = Column(Numeric(20, 4), comment='产险：赔付率')
    FEE_RATIO_PROPERTY = Column(Numeric(20, 4), comment='产险：费用率')
    INTRINSIC_VALUE_LIFE = Column(Numeric(20, 4), comment='寿险：内含价值')
    VALUE_NEW_BUSINESS_LIFE = Column(Numeric(20, 4), comment='寿险：新业务价值')
    VALUE_EFFECTIVE_BUSINESS_LIFE = Column(Numeric(20, 4), comment='寿险：有效业务价值')
    ACTUAL_CAPITAL_LIFE = Column(Numeric(20, 4), comment='寿险：实际资本')
    MINIMUN_CAPITAL_LIFE = Column(Numeric(20, 4), comment='寿险：最低资本')
    ACTUAL_CAPITAL_PROPERTY = Column(Numeric(20, 4), comment='产险：实际资本')
    MINIMUN_CAPITAL_PROPERTY = Column(Numeric(20, 4), comment='产险：最低资本')
    ACTUAL_CAPITAL_GROUP = Column(Numeric(20, 4), comment='集团：实际资本')
    MINIMUN_CAPITAL_GROUP = Column(Numeric(20, 4), comment='集团：最低资本')
    CAPITAL_ADEQUACY_RATIO_GROUP = Column(Numeric(20, 4), comment='集团：偿付能力充足率')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    REPORT_TYPE = Column(Numeric(9, 0), comment='报告类型代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')


class USASTOCKNEWS(Base):
    """美国股市"""
    __tablename__ = 'USASTOCKNEWS'
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


class USSHARECHANGECODE(Base):
    """美股代码变更表"""
    __tablename__ = 'USSHARECHANGECODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDCODE = Column(VARCHAR(10), comment='变更前代码')
    S_INFO_NEWCODE = Column(VARCHAR(10), comment='变更后代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前Wind代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后Wind代码')
    CHANGE_DATE = Column(VARCHAR(10), comment='代码变更日期')


class USSHAREINDUSTRIESCODE(Base):
    """美股行业代码表"""
    __tablename__ = 'USSHAREINDUSTRIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCLASS = Column(VARCHAR(100), comment='行业分类')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='板块代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='板块名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')


class USSHAREINFO(Base):
    """美股基本资料"""
    __tablename__ = 'USSHAREINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券中文简称')
    S_INFO_NAME_ENG = Column(VARCHAR(200), comment='[内部]证券英文简称')
    S_INFO_ISINCODE = Column(VARCHAR(40), comment='[内部]ISIN代码')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所名称(兼容)')
    SECURITYCLASS = Column(Numeric(9, 0), comment='品种大类代码')
    SECURITYSUBCLASS = Column(Numeric(9, 0), comment='品种细类代码')
    SECURITYTYPE = Column(VARCHAR(10), comment='品种类型(兼容)')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='开始交易日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='最后交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='交易币种')
    SECURITY_STATUS = Column(Numeric(9, 0), comment='存续状态')


class USSHAREINTRODUCTION(Base):
    """美股上市公司简介"""
    __tablename__ = 'USSHAREINTRODUCTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')
    COMP_NAME_ENG = Column(VARCHAR(100), comment='英文名称')
    COMP_SNAME_ENG = Column(VARCHAR(100), comment='英文名称缩写')
    FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    LEGALREPRESENTATIVE = Column(VARCHAR(38), comment='法定代表人')
    REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    CRNY_CODE = Column(VARCHAR(10), comment='货币代码')
    BRIEFING = Column(VARCHAR(1000), comment='公司简介')
    BUSINESSSCOPE = Column(VARCHAR(2000), comment='经营范围')
    BUSINESSSCOPE_ENG = Column(VARCHAR(2000), comment='经营范围(英文)')
    TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    DISCLOSERID = Column(VARCHAR(500), comment='信息披露人ID')
    ADDRESS = Column(VARCHAR(200), comment='注册地址')
    OFFICE = Column(VARCHAR(200), comment='办公地址')
    PHONE = Column(VARCHAR(50), comment='电话')
    FAX = Column(VARCHAR(50), comment='传真')
    COUNTRY = Column(VARCHAR(20), comment='国家及地区')
    WEBSITE = Column(VARCHAR(80), comment='主页')
    EMAIL = Column(VARCHAR(80), comment='电子邮箱')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class USSHAREPARVALUELOTSIZE(Base):
    """美股面值及交易单位"""
    __tablename__ = 'USSHAREPARVALUELOTSIZE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='变动日期')
    S_INFO_PAR = Column(Numeric(24, 8), comment='面值')
    S_INFO_TRADEUNIT = Column(Numeric(20, 4), comment='交易单位')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')


class USSHARESECTOR(Base):
    """美股板块分类"""
    __tablename__ = 'USSHARESECTOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_SECTORCODE = Column(VARCHAR(8), comment='板块类别代码')
    S_INFO_SECTOR = Column(VARCHAR(50), comment='板块类别名称')
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_SECTOREXITDT = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class USSHAREWINDCUSTOMCODE(Base):
    """美股Wind兼容代码"""
    __tablename__ = 'USSHAREWINDCUSTOMCODE'
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


class USSHAREWINDINDUSTRIESMEMBERS(Base):
    """美股万得行业成份"""
    __tablename__ = 'USSHAREWINDINDUSTRIESMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    WIND_IND_CODE = Column(VARCHAR(50), comment='所属板块代码')
    WIND_IND_NAME = Column(VARCHAR(50), comment='板块名称')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class VALUEMININGNEWS(Base):
    """价值挖掘"""
    __tablename__ = 'VALUEMININGNEWS'
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


class WINDBENCHMARKINTERESTRATE(Base):
    """WIND计算基准利率"""
    __tablename__ = 'WINDBENCHMARKINTERESTRATE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    B_INFO_BENCHMARKCODE = Column(VARCHAR(20), comment='利率代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    B_INFO_RATE = Column(Numeric(20, 4), comment='利率(%)')


class WINDCHINAOPTIONVALUATION(Base):
    """Wind中国期权衍生指标"""
    __tablename__ = 'WINDCHINAOPTIONVALUATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    W_ANAL_UNDERLYINGIMPLIEDVOL = Column(Numeric(24, 8), comment='隐含波动率')
    THEORE_PRICE = Column(Numeric(24, 8), comment='理论价格')
    W_ANAL_DELTA = Column(Numeric(24, 8), comment='Delta')
    W_ANAL_THETA = Column(Numeric(24, 8), comment='Theta')
    W_ANAL_GAMMA = Column(Numeric(24, 8), comment='Gamma')
    W_ANAL_VEGA = Column(Numeric(24, 8), comment='Vega')
    W_ANAL_RHO = Column(Numeric(24, 8), comment='Rho')


class WINDCUSTOMCODE(Base):
    """Wind兼容代码"""
    __tablename__ = 'WINDCUSTOMCODE'
    __table_args__ = (
        Index('IDX_S_INFO_CODE', 'S_INFO_CODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_ASHARECODE = Column(VARCHAR(10), comment='证券ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_INFO_SECURITIESTYPES = Column(VARCHAR(10), comment='证券类型')
    S_INFO_SECTYPENAME = Column(VARCHAR(40), comment='类型名称')
    S_INFO_COUNTRYNAME = Column(VARCHAR(100), comment='国别')
    S_INFO_COUNTRYCODE = Column(VARCHAR(10), comment='国别编号')
    S_INFO_EXCHMARKETNAME = Column(VARCHAR(40), comment='交易所')
    S_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所编号')
    CRNCY_NAME = Column(VARCHAR(40), comment='币种')
    CRNCY_CODE = Column(VARCHAR(10), comment='币种编号')
    S_INFO_ISINCODE = Column(VARCHAR(40), comment='ISIN代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(80), comment='证券中文简称')
    EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    SECURITY_STATUS = Column(Numeric(9, 0), comment='存续状态')
    S_INFO_ORG_CODE = Column(VARCHAR(20), comment='组织机构代码')
    S_INFO_TYPECODE = Column(Numeric(9, 0), comment='分类代码')
    S_INFO_MIN_PRICE_CHG_UNIT = Column(Numeric(24, 8), comment='最小价格变动单位')
    S_INFO_LOT_SIZE = Column(Numeric(20, 4), comment='每手数量')
    S_INFO_ENAME = Column(VARCHAR(200), comment='证券英文简称')
    TRADING_HOURS_CODE = Column(VARCHAR(10), comment='交易时段编码')
    S_INFO_SECTYPEBCODE = Column(Numeric(9, 0), comment='品种大类代码')
    S_INFO_SECTYPESCODE = Column(Numeric(9, 0), comment='品种细类代码')
    S_INFO_PINYIN = Column(VARCHAR(40), comment='简称拼音')


class XQSTATISTICALINDICATORS(Base):
    """雪球财经股票统计指标"""
    __tablename__ = 'XQSTATISTICALINDICATORS'
    __table_args__ = (
        Index('IDX_XQSTATISTICALINDICATORS_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='日期')
    CUM_CONCERN_NUM = Column(Numeric(20, 4), comment='累计关注人数')
    CUM_DISCUSSION_NUM = Column(Numeric(20, 4), comment='累计讨论次数')
    CUM_SHARE_NUM = Column(Numeric(20, 4), comment='累计交易分享数')
    WEEKLYNEW_CONCERN_NUM = Column(Numeric(20, 4), comment='一周新增关注')
    WEEKLYNEW_DISCUSSION_NUM = Column(Numeric(20, 4), comment='一周新增讨论数')
    WEEKLYNEW_SHARE_NUM = Column(Numeric(20, 4), comment='一周新增交易分享数')
    WEEKLYNEW_CONCERN_RATE = Column(Numeric(20, 4), comment='一周关注增长率')
    WEEKLYNEW_DISCUSSION_RATE = Column(Numeric(20, 4), comment='一周讨论增长率')
    WEEKLYNEW_SHARE_RATE = Column(Numeric(20, 4), comment='一周交易分享增长率')


class IPOINQUIRYDETAILS(Base):
        """ IPO初步询价明细 """
        __tablename__ = 'IPOINQUIRYDETAILS'
        __table_args__ = (
            Index('IDX_IPOINQUIRYDETAILS_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
        OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
        S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
        ANN_DT = Column(VARCHAR(8), comment='公告日期')
        INQUIRER = Column(VARCHAR(300), comment='询价对象名称')
        INQUIRERID = Column(VARCHAR(300), comment='询价对象名称ID')
        INQUIRER_TYPECODE = Column(Numeric(9,0), comment='投资者类别代码')
        ISSUETARGET = Column(VARCHAR(300), comment='')
        DEDAREDPRICE = Column(Numeric(20, 4), comment='申报价格(元/股)')
        DEDAREDSHARES = Column(Numeric(20, 4), comment='申购数量(万股)')
        IS_VALID = Column(Numeric(1, 0), comment='是否有效报价投资者')
        ISSUETARGET1 = Column(VARCHAR(300), comment='公布配售对象名称')
        PCT_CHANGE_1M = Column(Numeric(20, 4), comment='配售数量')
        ISSUETARGETID = Column(VARCHAR(10), comment='配售对象名称ID')
        REJECT_DEDAREDSHARES = Column(Numeric(20, 4), comment='被剔除申购股数(万股)')
        ACT_DEDAREDSHARES = Column(Numeric(20, 4), comment='实际申购数量(万股)')
        ACT_DEDAREDSHARES = Column(Numeric(20, 4), comment='实际申购数量(万股)')
        SECURITY_ACCOUNT = Column(VARCHAR(20), comment='证券账户')
        QUOTE_TYPE_CODE = Column(Numeric(9, 0), comment='报价结果类型代码')









