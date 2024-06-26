# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/10/20 9:09
# @Author  : lisl3
# @File    : a_share_field.py
# @Project : cscfist
# @Function: 中国A股
# @Version : V0.0.1
# ------------------------------
from sqlalchemy import Column, VARCHAR, Numeric, DateTime, TEXT, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ASHAREACCOUNTINGCHANGE(Base):
    """中国A股公司会计变更"""
    __tablename__ = 'ASHAREACCOUNTINGCHANGE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_CHANGE_ITEMCODE = Column(Numeric(9, 0), comment='变更项目代码')
    S_CHANGE_REASON = Column(VARCHAR(2000), comment='变更的内容和原因')
    S_APPROVAL_PROGRAM = Column(VARCHAR(200), comment='审批程序')
    BE_AFFECTED_ITEMCODE = Column(VARCHAR(200), comment='受影响的报表项目名称')
    INFLUENCE_MONEY = Column(Numeric(20, 4), comment='影响金额(元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    BE_AFFECTED_REPORT_PERIOD = Column(VARCHAR(8), comment='受影响的报告期')
    BE_AFFECTED_REPORT_TYPE = Column(Numeric(9, 0), comment='受影响的报表类型')
    BE_AFFECTED_SUBJECT = Column(VARCHAR(80), comment='受影响的报表科目名称(容错)')
    PROCESSING_RESULT = Column(VARCHAR(2000), comment='董事会对责任人采取的问责措施及处理结果')


class ASHAREACCOUNTSPAYABLE(Base):
    """中国A股公司应付账款"""
    __tablename__ = 'ASHAREACCOUNTSPAYABLE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='上游公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='上游公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='上游公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class ASHAREACCOUNTSRECEIVABLE(Base):
    """中国A股应收账款大股东欠款"""
    __tablename__ = 'ASHAREACCOUNTSRECEIVABLE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    MEMO = Column(VARCHAR(100), comment='备注')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    DEBTOR_NAME = Column(VARCHAR(60), comment='债务人名称')
    ARREARS = Column(Numeric(20, 4), comment='金额')
    RATE = Column(Numeric(20, 4), comment='比例(%)')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')


class ASHAREADMINISTRATION(Base):
    """中国A股公司高管成员"""
    __tablename__ = 'ASHAREADMINISTRATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='职务')
    S_INFO_MANID = Column(VARCHAR(10), comment='人物id')


class ASHAREADMPERMITSCHEDULE(Base):
    """中国A股行政许可事项进度表"""
    __tablename__ = 'ASHAREADMPERMITSCHEDULE'
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


class ASHAREADVANCEPAYMENT(Base):
    """中国A股财务附注--预付账款"""
    __tablename__ = 'ASHAREADVANCEPAYMENT'
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


class ASHAREADVANCERECEIPT(Base):
    """中国A股财务附注--预收款项"""
    __tablename__ = 'ASHAREADVANCERECEIPT'
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


class ASHAREAFTEREODPINDICATORS(Base):
    """中国A股盘后盘口指标"""
    __tablename__ = 'ASHAREAFTEREODPINDICATORS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_STOCKID = Column(VARCHAR(10), comment='证券ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    INDICATOR_CODE = Column(Numeric(9, 0), comment='指标代码')
    INDICATOR_VALUE = Column(Numeric(24, 8), comment='指标值')
    INDICATOR_UNIT = Column(VARCHAR(10), comment='指标单位')


class ASHAREAFTEREODPRICES(Base):
    """中国A股沪深交易所盘后行情"""
    __tablename__ = 'ASHAREAFTEREODPRICES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_AFTER_PRICE = Column(Numeric(20, 4), comment='盘后固定价格(元)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')


class ASHAREAGENCY(Base):
    """中国A股发行中介机构"""
    __tablename__ = 'ASHAREAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_AGENCY_NAME = Column(VARCHAR(200), comment='机构名称')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    S_BUSINESS_TYPCODE = Column(Numeric(9, 0), comment='业务类型代码')
    S_AGENCY_NAMEID = Column(VARCHAR(200), comment='机构名称ID')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    SEQUENCE = Column(VARCHAR(6), comment='序号')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class ASHAREAGENCYZL(Base):
    """中国A股发行中介机构(增量)"""
    __tablename__ = 'ASHAREAGENCYZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_AGENCY_NAME = Column(VARCHAR(200), comment='机构名称')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    S_BUSINESS_TYPCODE = Column(Numeric(9, 0), comment='业务类型代码')
    S_AGENCY_NAMEID = Column(VARCHAR(200), comment='机构名称ID')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    SEQUENCE = Column(VARCHAR(6), comment='序号')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class ASHAREAGINGSTRUCTURE(Base):
    """中国A股应收账款账龄结构"""
    __tablename__ = 'ASHAREAGINGSTRUCTURE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    STATEMENT_TYPE_NAME = Column(VARCHAR(40), comment='报表类型名称')
    MEMO = Column(VARCHAR(100), comment='备注')
    AGING = Column(VARCHAR(20), comment='帐龄')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    AMOUNT_MONEY = Column(Numeric(20, 4), comment='金额')
    RATE = Column(Numeric(20, 4), comment='比例(%)')
    BAD_DEBT_PREPARATION = Column(Numeric(20, 4), comment='坏帐准备')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    MIN_AGING = Column(Numeric(20, 4), comment='最小账龄(年)')
    MAX_AGING = Column(Numeric(20, 4), comment='最大账龄(年)')
    CLASSIFICATION_CRITERIA = Column(VARCHAR(40), comment='分类标准')


class ASHAREANNCOLUMN(Base):
    """沪深公司公告栏目"""
    __tablename__ = 'ASHAREANNCOLUMN'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    N_INFO_CODE = Column(VARCHAR(38), comment='Wind栏目代码')
    N_INFO_PCODE = Column(VARCHAR(38), comment='父节点栏目代码')
    N_INFO_FCODE = Column(VARCHAR(38), comment='本节栏目代码')
    N_INFO_NAME = Column(VARCHAR(200), comment='栏目名称')
    N_INFO_ISVALID = Column(Numeric(2, 0), comment='是否有效')
    N_INFO_LEVELNUM = Column(Numeric(2, 0), comment='栏目级别')


class ASHAREANNCOLUMNZL(Base):
    """沪深公司公告栏目(增量)"""
    __tablename__ = 'ASHAREANNCOLUMNZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    N_INFO_CODE = Column(VARCHAR(38), comment='Wind栏目代码')
    N_INFO_PCODE = Column(VARCHAR(38), comment='父节点栏目代码')
    N_INFO_FCODE = Column(VARCHAR(38), comment='本节栏目代码')
    N_INFO_NAME = Column(VARCHAR(200), comment='栏目名称')
    N_INFO_ISVALID = Column(Numeric(2, 0), comment='是否有效')
    N_INFO_LEVELNUM = Column(Numeric(2, 0), comment='栏目级别')


class ASHAREANNFINANCIALINDICATOR(Base):
    """中国A股公布重要财务指标"""
    __tablename__ = 'ASHAREANNFINANCIALINDICATOR'
    __table_args__ = (
        Index('IDX_ASHAREANNFINANCIALINDICATOR_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    IFLISTED_DATA = Column(Numeric(1, 0), comment='是否上市后数据')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_FA_EPS_DILUTED = Column(Numeric(20, 4), comment='每股收益-摊薄(元)')
    S_FA_EPS_BASIC = Column(Numeric(20, 4), comment='每股收益-基本')
    S_FA_EPS_DILUTED2 = Column(Numeric(20, 6), comment='每股收益-稀释(元)')
    S_FA_EPS_EX = Column(Numeric(20, 4), comment='每股收益-扣除(元)')
    S_FA_EPS_EXBASIC = Column(Numeric(20, 4), comment='每股收益-扣除/基本')
    S_FA_EPS_EXDILUTED = Column(Numeric(20, 4), comment='每股收益-扣除/稀释(元)')
    S_FA_BPS = Column(Numeric(22, 4), comment='每股净资产(元)')
    S_FA_BPS_SH = Column(Numeric(20, 4), comment='归属于母公司股东的每股净资产(元)')
    S_FA_BPS_ADJUST = Column(Numeric(20, 4), comment='每股净资产-调整(元)')
    ROE_DILUTED = Column(Numeric(20, 4), comment='净资产收益率-摊薄(%)')
    ROE_WEIGHTED = Column(Numeric(20, 4), comment='净资产收益率-加权(%)')
    ROE_EX = Column(Numeric(20, 4), comment='净资产收益率-扣除(%)')
    ROE_EXWEIGHTED = Column(Numeric(20, 4), comment='净资产收益率-扣除/加权(%)')
    NET_PROFIT = Column(Numeric(20, 4), comment='国际会计准则净利润(元)')
    RD_EXPENSE = Column(Numeric(20, 4), comment='研发费用(元)')
    S_FA_EXTRAORDINARY = Column(Numeric(22, 4), comment='非经常性损益(元)')
    S_FA_CURRENT = Column(Numeric(20, 4), comment='流动比(%)')
    S_FA_QUICK = Column(Numeric(20, 4), comment='速动比(%)')
    S_FA_ARTURN = Column(Numeric(20, 4), comment='应收账款周转率(%)')
    S_FA_INVTURN = Column(Numeric(20, 4), comment='存货周转率(%)')
    S_FT_DEBTTOASSETS = Column(Numeric(20, 4), comment='资产负债率(%)')
    S_FA_OCFPS = Column(Numeric(20, 4), comment='每股经营活动产生的现金流量净额(元)')
    S_FA_YOYOCFPS = Column(Numeric(22, 4), comment='同比增长率.每股经营活动产生的现金流量净额(%)')
    S_FA_DEDUCTEDPROFIT = Column(Numeric(20, 4), comment='扣除非经常性损益后的净利润(扣除少数股东损益)')
    S_FA_DEDUCTEDPROFIT_YOY = Column(Numeric(22, 4),
                                     comment='同比增长率.扣除非经常性损益后的净利润(扣除少数股东损益)(%)')
    CONTRIBUTIONPS = Column(Numeric(20, 4), comment='每股社会贡献值(元)')
    GROWTH_BPS_SH = Column(Numeric(22, 4), comment='比年初增长率.归属于母公司股东的每股净资产(%)')
    S_FA_YOYEQUITY = Column(Numeric(22, 4), comment='比年初增长率.归属母公司的股东权益(%)')
    YOY_ROE_DILUTED = Column(Numeric(22, 4), comment='同比增长率.净资产收益率(摊薄)(%)')
    YOY_NET_CASH_FLOWS = Column(Numeric(22, 4), comment='同比增长率.经营活动产生的现金流量净额(%)')
    S_FA_YOYEPS_BASIC = Column(Numeric(22, 4), comment='同比增长率.基本每股收益(%)')
    S_FA_YOYEPS_DILUTED = Column(Numeric(22, 4), comment='同比增长率.稀释每股收益(%)')
    S_FA_YOYOP = Column(Numeric(20, 4), comment='同比增长率.营业利润(%)')
    S_FA_YOYEBT = Column(Numeric(20, 4), comment='同比增长率.利润总额(%)')
    NET_PROFIT_YOY = Column(Numeric(20, 4), comment='同比增长率.净利润(%)')
    S_INFO_DIV = Column(VARCHAR(40), comment='分红方案')
    MEMO = Column(VARCHAR(100), comment='备注')


class ASHAREANNINF(Base):
    """沪深公司公告信息"""
    __tablename__ = 'ASHAREANNINF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    N_INFO_STOCKID = Column(VARCHAR(10), comment='证券ID')
    N_INFO_COMPANYID = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(DateTime, comment='公告日期')
    N_INFO_TITLE = Column(VARCHAR(1024), comment='标题')
    N_INFO_FCODE = Column(VARCHAR(200), comment='栏目代码')
    N_INFO_FTXT = Column(TEXT(2147483647), comment='摘要')
    N_INFO_ANNLINK = Column(VARCHAR(1024), comment='公告链接')
    ID = Column(Numeric(11, 0), comment='公告ID')
    COLLECT_DT = Column(DateTime, comment='收录时间')


class ASHAREANNTEXT(Base):
    """沪深公司公告文本"""
    __tablename__ = 'ASHAREANNTEXT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    ANN_OBJECT_ID = Column(VARCHAR(40), comment='公告主表对象ID')
    ANN_TEXT = Column(VARCHAR, comment='公告正文')


class ASHAREASSETTRANSACTION(Base):
    """None"""
    __tablename__ = 'ASHAREASSETTRANSACTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='信息披露方公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='资产卖方公司名称')
    RELATION_TYPE = Column(VARCHAR(40), comment='资产卖方与披露方的关系')
    S_INFO_COMPNAME2 = Column(VARCHAR(100), comment='资产买方公司名称')
    RELATION_TYPE2 = Column(VARCHAR(40), comment='资产买方与披露方的关系')
    TARGET = Column(VARCHAR(2000), comment='交易标的')
    TRADINGAMOUNT = Column(Numeric(20, 4), comment='交易金额(元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='交易金额货币代码')
    BASEDATE = Column(VARCHAR(8), comment='资产评估基准日')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    FIRST_DT = Column(VARCHAR(8), comment='首次公告日期')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日期')
    PROGRESS = Column(VARCHAR(10), comment='方案进度代码')
    IS_RELDPARTRANSACTIONS = Column(Numeric(1, 0), comment='是否关联交易')
    SUMMARY = Column(VARCHAR(2000), comment='交易简介')
    INFLUENCE = Column(VARCHAR(1000), comment='交易对信息披露方的影响')
    HIS_CHANGE = Column(VARCHAR(2000), comment='交易历史变动情况')


class ASHAREAUDITDESCRIPTION(Base):
    """中国A股审计事项描述"""
    __tablename__ = 'ASHAREAUDITDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    AUDIT_PROJECT_TYPE = Column(Numeric(9, 0), comment='审计项目类型代码')
    AUDIT_MATTERS_TYPE = Column(VARCHAR(500), comment='关键审计事项类型')
    AUDIT_MATTERS_NUM = Column(Numeric(5, 0), comment='关键审计事项序号')
    MATTER_DESCRIPTION = Column(TEXT(2147483647), comment='事项描述')
    AUDIT_RESPONSE = Column(TEXT(2147483647), comment='审计应对')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class ASHAREAUDITOPINION(Base):
    """中国A股审计意见"""
    __tablename__ = 'ASHAREAUDITOPINION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_STMNOTE_AUDIT_CATEGORY = Column(Numeric(9, 0), comment='审计结果类别代码')
    S_STMNOTE_AUDIT_AGENCY = Column(VARCHAR(100), comment='会计师事务所')
    S_STMNOTE_AUDIT_CPA = Column(VARCHAR(100), comment='签字会计师')
    S_PAY_AUDIT_EXPENSES = Column(Numeric(20, 4), comment='当期实付审计费用(总额)(元)')


class ASHAREBALANCESHEET(Base):
    """中国A股资产负债表"""
    __tablename__ = 'ASHAREBALANCESHEET'
    __table_args__ = (
        Index('fass', 'S_INFO_WINDCODE', 'REPORT_PERIOD', 'MONETARY_CAP', 'TRADABLE_FIN_ASSETS', 'NOTES_RCV',
              'ACCT_RCV', 'OTH_RCV', 'PREPAY', 'DVD_RCV', 'INT_RCV', 'INVENTORIES', 'CONSUMPTIVE_BIO_ASSETS',
              'DEFERRED_EXP', 'NON_CUR_ASSETS_DUE_WITHIN_1Y', 'SETTLE_RSRV', 'LOANS_TO_OTH_BANKS', 'PREM_RCV',
              'RCV_FROM_REINSURER', 'RCV_FROM_CEDED_INSUR_CONT_RSRV', 'RED_MONETARY_CAP_FOR_SALE', 'OTH_CUR_ASSETS',
              'TOT_CUR_ASSETS', 'FIN_ASSETS_AVAIL_FOR_SALE', 'HELD_TO_MTY_INVEST', 'LONG_TERM_EQY_INVEST',
              'INVEST_REAL_ESTATE', 'TIME_DEPOSITS', 'OTH_ASSETS', 'LONG_TERM_REC', 'FIX_ASSETS', 'CONST_IN_PROG',
              'PROJ_MATL', 'FIX_ASSETS_DISP', 'PRODUCTIVE_BIO_ASSETS', 'OIL_AND_NATURAL_GAS_ASSETS', 'INTANG_ASSETS',
              'R_AND_D_COSTS', 'GOODWILL', 'LONG_TERM_DEFERRED_EXP', 'DEFERRED_TAX_ASSETS', 'LOANS_AND_ADV_GRANTED',
              'OTH_NON_CUR_ASSETS', 'TOT_NON_CUR_ASSETS', 'CASH_DEPOSITS_CENTRAL_BANK', 'ASSET_DEP_OTH_BANKS_FIN_INST',
              'PRECIOUS_METALS', 'DERIVATIVE_FIN_ASSETS', 'AGENCY_BUS_ASSETS', 'SUBR_REC',
              'RCV_CEDED_UNEARNED_PREM_RSRV', 'RCV_CEDED_CLAIM_RSRV', 'RCV_CEDED_LIFE_INSUR_RSRV',
              'RCV_CEDED_LT_HEALTH_INSUR_RSRV', 'MRGN_PAID', 'INSURED_PLEDGE_LOAN', 'CAP_MRGN_PAID',
              'INDEPENDENT_ACCT_ASSETS', 'CLIENTS_CAP_DEPOSIT', 'CLIENTS_RSRV_SETTLE', 'INCL_SEAT_FEES_EXCHANGE',
              'RCV_INVEST', 'TOT_ASSETS', 'ST_BORROW', 'BORROW_CENTRAL_BANK', 'DEPOSIT_RECEIVED_IB_DEPOSITS',
              'LOANS_OTH_BANKS', 'TRADABLE_FIN_LIAB', 'NOTES_PAYABLE', 'ACCT_PAYABLE', 'ADV_FROM_CUST',
              'FUND_SALES_FIN_ASSETS_RP', 'HANDLING_CHARGES_COMM_PAYABLE', 'EMPL_BEN_PAYABLE',
              'TAXES_SURCHARGES_PAYABLE', 'INT_PAYABLE', 'DVD_PAYABLE', 'OTH_PAYABLE', 'ACC_EXP', 'DEFERRED_INC',
              'ST_BONDS_PAYABLE', 'PAYABLE_TO_REINSURER', 'RSRV_INSUR_CONT', 'ACTING_TRADING_SEC', 'ACTING_UW_SEC',
              'NON_CUR_LIAB_DUE_WITHIN_1Y', 'OTH_CUR_LIAB', 'TOT_CUR_LIAB', 'LT_BORROW', 'BONDS_PAYABLE', 'LT_PAYABLE',
              'SPECIFIC_ITEM_PAYABLE', 'PROVISIONS', 'DEFERRED_TAX_LIAB', 'DEFERRED_INC_NON_CUR_LIAB',
              'OTH_NON_CUR_LIAB', 'TOT_NON_CUR_LIAB', 'LIAB_DEP_OTH_BANKS_FIN_INST', 'DERIVATIVE_FIN_LIAB',
              'CUST_BANK_DEP', 'AGENCY_BUS_LIAB', 'OTH_LIAB', 'PREM_RECEIVED_ADV', 'DEPOSIT_RECEIVED',
              'INSURED_DEPOSIT_INVEST', 'UNEARNED_PREM_RSRV', 'OUT_LOSS_RSRV', 'LIFE_INSUR_RSRV', 'LT_HEALTH_INSUR_V',
              'INDEPENDENT_ACCT_LIAB', 'INCL_PLEDGE_LOAN', 'CLAIMS_PAYABLE', 'DVD_PAYABLE_INSURED', 'TOT_LIAB',
              'CAP_STK', 'CAP_RSRV', 'SPECIAL_RSRV', 'SURPLUS_RSRV', 'UNDISTRIBUTED_PROFIT', 'LESS_TSY_STK',
              'PROV_NOM_RISKS', 'CNVD_DIFF_FOREIGN_CURR_STAT', 'UNCONFIRMED_INVEST_LOSS', 'MINORITY_INT',
              'TOT_SHRHLDR_EQY_EXCL_MIN_INT', 'TOT_SHRHLDR_EQY_INCL_MIN_INT', 'TOT_LIAB_SHRHLDR_EQY',
              'SPE_CUR_ASSETS_DIFF', 'TOT_CUR_ASSETS_DIFF', 'SPE_NON_CUR_ASSETS_DIFF', 'TOT_NON_CUR_ASSETS_DIFF',
              'SPE_BAL_ASSETS_DIFF', 'TOT_BAL_ASSETS_DIFF', 'SPE_CUR_LIAB_DIFF', 'TOT_CUR_LIAB_DIFF',
              'SPE_NON_CUR_LIAB_DIFF', 'TOT_NON_CUR_LIAB_DIFF', 'SPE_BAL_LIAB_DIFF', 'TOT_BAL_LIAB_DIFF',
              'SPE_BAL_SHRHLDR_EQY_DIFF', 'TOT_BAL_SHRHLDR_EQY_DIFF', 'SPE_BAL_LIAB_EQY_DIFF', 'TOT_BAL_LIAB_EQY_DIFF',
              'LT_PAYROLL_PAYABLE', 'OTHER_COMP_INCOME', 'OTHER_EQUITY_TOOLS', 'OTHER_EQUITY_TOOLS_P_SHR',
              'LENDING_FUNDS', 'ACCOUNTS_RECEIVABLE', 'ST_FINANCING_PAYABLE', 'PAYABLES', 'TOT_SHR', 'HFS_ASSETS',
              'HFS_SALES', 'FIN_ASSETS_COST_SHARING', 'FIN_ASSETS_FAIR_VALUE', 'CONTRACTUAL_ASSETS',
              'CONTRACT_LIABILITIES', 'ACCOUNTS_RECEIVABLE_BILL', 'ACCOUNTS_PAYABLE', 'OTH_RCV_TOT', 'STM_BS_TOT',
              'CONST_IN_PROG_TOT', 'OTH_PAYABLE_TOT', 'LT_PAYABLE_TOT', 'DEBT_INVESTMENT', 'OTHER_DEBT_INVESTMENT',
              'OTHER_EQUITY_INVESTMENT', 'OTHER_ILLIQUIDFINANCIAL_ASSETS', 'OTHER_SUSTAINABLE_BOND',
              'RECEIVABLES_FINANCING', 'RIGHT_USE_ASSETS', 'LEASE_LIAB'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
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
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    TOT_SHR = Column(Numeric(20, 4), comment='期末总股本')
    HFS_ASSETS = Column(Numeric(20, 4), comment='持有待售的资产')
    HFS_SALES = Column(Numeric(20, 4), comment='持有待售的负债')
    FIN_ASSETS_COST_SHARING = Column(Numeric(20, 4), comment='以摊余成本计量的金融资产')
    FIN_ASSETS_FAIR_VALUE = Column(Numeric(20, 4), comment='以公允价值计量且其变动计入其他综合收益的金融资产')
    CONTRACTUAL_ASSETS = Column(Numeric(20, 4), comment='合同资产')
    CONTRACT_LIABILITIES = Column(Numeric(20, 4), comment='合同负债')
    ACCOUNTS_RECEIVABLE_BILL = Column(Numeric(20, 4), comment='应收票据及应收账款')
    ACCOUNTS_PAYABLE = Column(Numeric(20, 4), comment='应付票据及应付账款')
    OTH_RCV_TOT = Column(Numeric(20, 4), comment='其他应收款(合计)（元）')
    STM_BS_TOT = Column(Numeric(20, 4), comment='固定资产(合计)(元)')
    CONST_IN_PROG_TOT = Column(Numeric(20, 4), comment='在建工程(合计)(元)')
    OTH_PAYABLE_TOT = Column(Numeric(20, 4), comment='其他应付款(合计)(元)')
    LT_PAYABLE_TOT = Column(Numeric(20, 4), comment='长期应付款(合计)(元)')
    DEBT_INVESTMENT = Column(Numeric(20, 4), comment='债权投资(元)')
    OTHER_DEBT_INVESTMENT = Column(Numeric(20, 4), comment='其他债权投资(元)')
    OTHER_EQUITY_INVESTMENT = Column(Numeric(20, 4), comment='其他权益工具投资(元)')
    OTHER_ILLIQUIDFINANCIAL_ASSETS = Column(Numeric(20, 4), comment='其他非流动金融资产(元)')
    OTHER_SUSTAINABLE_BOND = Column(Numeric(20, 4), comment='其他权益工具:永续债(元)')
    RECEIVABLES_FINANCING = Column(Numeric(20, 4), comment='应收款项融资')
    RIGHT_USE_ASSETS = Column(Numeric(20, 4), comment='使用权资产')
    LEASE_LIAB = Column(Numeric(20, 4), comment='租赁负债')


class ASHAREBANKINDICATOR(Base):
    """中国A股银行专用指标"""
    __tablename__ = 'ASHAREBANKINDICATOR'
    __table_args__ = (
        Index('IDX_ASHAREBANKINDICATOR_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
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
    NET_INTEREST_MARGIN_IS_ANN = Column(Numeric(20, 4), comment='净息差(%)计算值')
    NET_INTEREST_SPREAD = Column(Numeric(20, 4), comment='净利差')
    NET_INTEREST_SPREAD_IS_ANN = Column(Numeric(20, 4), comment='净利差(%)计算值')
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
    LOANRESERVESRATIO = Column(Numeric(20, 4), comment='贷款减值准备对贷款总额比率(%)')
    SUBORDINATED_NET_CAPI = Column(Numeric(20, 4), comment='附属资本净额')
    INT_BEAR_ASSET_AVG_BALANCE = Column(Numeric(20, 4), comment='生息资产平均余额')
    INT_BEAR_ASSET_AVG_RETURN = Column(Numeric(20, 4), comment='生息资产平均收益率(%)')
    INT_CCRUED_LIAB_AVG_BALANCE = Column(Numeric(20, 4), comment='计息负债平均余额')
    INT_CCRUED_LIAB_AVG_COSTRATIO = Column(Numeric(20, 4), comment='计息负债平均成本率(%)')
    RESCHEDULEDLOANS = Column(Numeric(20, 4), comment='已重组贷款')
    CORETIER1_NET_CAPI = Column(Numeric(20, 4), comment='核心一级资本净额')
    TIER1_NET_CAPI = Column(Numeric(20, 4), comment='一级资本净额')
    NET_CAPITAL_2013 = Column(Numeric(20, 4), comment='资本净额(资本管理办法)')
    CORETIER1CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='核心一级资本充足率')
    TIER1CAPI_ADE_RATIO = Column(Numeric(20, 4), comment='一级资本充足率')
    CAPI_ADE_RATIO_2013 = Column(Numeric(20, 4), comment='资本充足率(资本管理办法)')
    RISK_WEIGHT_NET_ASSET_2013 = Column(Numeric(20, 4), comment='加权风险资产净额(资本管理办法)')
    LEVERAGE_RATIO = Column(Numeric(20, 4), comment='杠杆率(%)')
    FLUIDITY_COVERAGE = Column(Numeric(20, 4), comment='流动性覆盖率(%)')
    CREDIT_RISKS_TOTAL_ASSETS = Column(Numeric(20, 4), comment='信用风险加权资产总额(元)')
    MARKET_RISK_TOTAL_ASSETS = Column(Numeric(20, 4), comment='市场风险加权资产总额(元)')
    OPERATIONAL_RISK_TOTAL_ASSETS = Column(Numeric(20, 4), comment='操作风险加权资产总额(元)')


class ASHAREBEGUARANTEED(Base):
    """中国A股被担保"""
    __tablename__ = 'ASHAREBEGUARANTEED'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='担保公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='担保公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='担保公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class ASHAREBLOCKTRADE(Base):
    """中国A股大宗交易数据"""
    __tablename__ = 'ASHAREBLOCKTRADE'
    __table_args__ = (
        Index('IDX_ASHAREBLOCKTRADE_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_BLOCK_PRICE = Column(Numeric(20, 4), comment='成交价（元）')
    S_BLOCK_VOLUME = Column(Numeric(20, 4), comment='成交量（万股）')
    S_BLOCK_AMOUNT = Column(Numeric(20, 4), comment='成交金额（万元）')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_BLOCK_BUYERNAME = Column(VARCHAR(200), comment='买方营业部名称')
    S_BLOCK_SELLERNAME = Column(VARCHAR(200), comment='卖方营业部名称')
    S_BLOCK_FREQUENCY = Column(Numeric(20, 4), comment='笔数')


class ASHAREBUYRESALEFINASSETS(Base):
    """中国A股财务附注--买入返售金融资产"""
    __tablename__ = 'ASHAREBUYRESALEFINASSETS'
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


class ASHARECALENDAR(Base):
    """中国A股交易日历"""
    __tablename__ = 'ASHARECALENDAR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DAYS = Column(VARCHAR(8), comment='交易日')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class ASHARECALENDARZL(Base):
    """中国A股交易日历(增量)"""
    __tablename__ = 'ASHARECALENDARZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DAYS = Column(VARCHAR(8), comment='交易日')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class ASHARECAPITALIZATION(Base):
    """中国A股股本"""
    __tablename__ = 'ASHARECAPITALIZATION'
    __table_args__ = (
        Index('IDX_ASHARECAPITALIZATION_ANN_DT', 'ANN_DT'),
        Index('IDX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    TOT_SHR = Column(Numeric(20, 4), comment='总股本(万股)')
    FLOAT_SHR = Column(Numeric(20, 4), comment='流通股(万股)')
    FLOAT_A_SHR = Column(Numeric(20, 4), comment='流通A股(万股)')
    FLOAT_B_SHR = Column(Numeric(20, 4), comment='流通B股(万股)')
    FLOAT_H_SHR = Column(Numeric(20, 4), comment='流通H股(万股)')
    FLOAT_OVERSEAS_SHR = Column(Numeric(20, 4), comment='境外流通股(万股)')
    RESTRICTED_A_SHR = Column(Numeric(20, 4), comment='限售A股(万股)')
    S_SHARE_RTD_STATE = Column(Numeric(20, 4), comment='限售A股(国家持股)')
    S_SHARE_RTD_STATEJUR = Column(Numeric(20, 4), comment='限售A股(国有法人持股)')
    S_SHARE_RTD_SUBOTHERDOMES = Column(Numeric(20, 4), comment='限售A股(其他内资持股)')
    S_SHARE_RTD_DOMESJUR = Column(Numeric(20, 4), comment='限售A股(其他内资持股:境内法人持股)')
    S_SHARE_RTD_INST = Column(Numeric(20, 4), comment='限售A股(其他内资持股:机构配售股)')
    S_SHARE_RTD_DOMESNP = Column(Numeric(20, 4), comment='限售A股(其他内资持股:境内自然人持股)')
    S_SHARE_RTD_SENMANAGER = Column(Numeric(20, 4), comment='限售股份(高管持股)(万股)')
    S_SHARE_RTD_SUBFRGN = Column(Numeric(20, 4), comment='限售A股(外资持股)')
    S_SHARE_RTD_FRGNJUR = Column(Numeric(20, 4), comment='限售A股(境外法人持股)')
    S_SHARE_RTD_FRGNNP = Column(Numeric(20, 4), comment='限售A股(境外自然人持股)')
    RESTRICTED_B_SHR = Column(Numeric(20, 4), comment='限售B股(万股)')
    OTHER_RESTRICTED_SHR = Column(Numeric(20, 4), comment='其他限售股')
    NON_TRADABLE_SHR = Column(Numeric(20, 4), comment='非流通股')
    S_SHARE_NTRD_STATE_PCT = Column(Numeric(20, 4), comment='非流通股(国有股)')
    S_SHARE_NTRD_STATE = Column(Numeric(20, 4), comment='非流通股(国家股)')
    S_SHARE_NTRD_STATJUR = Column(Numeric(20, 4), comment='非流通股(国有法人股)')
    S_SHARE_NTRD_SUBDOMESJUR = Column(Numeric(20, 4), comment='非流通股(境内法人股)')
    S_SHARE_NTRD_DOMESINITOR = Column(Numeric(20, 4), comment='非流通股(境内法人股:境内发起人股)')
    S_SHARE_NTRD_IPOJURIS = Column(Numeric(20, 4), comment='非流通股(境内法人股:募集法人股)')
    S_SHARE_NTRD_GENJURIS = Column(Numeric(20, 4), comment='非流通股(境内法人股:一般法人股)')
    S_SHARE_NTRD_STRTINVESTOR = Column(Numeric(20, 4), comment='非流通股(境内法人股:战略投资者持股)')
    S_SHARE_NTRD_FUNDBAL = Column(Numeric(20, 4), comment='非流通股(境内法人股:基金持股)')
    S_SHARE_NTRD_IPOINIP = Column(Numeric(20, 4), comment='非流通股(自然人股)')
    S_SHARE_NTRD_TRFNSHARE = Column(Numeric(20, 4), comment='转配股(万股)')
    S_SHARE_NTRD_SNORMNGER = Column(Numeric(20, 4), comment='流通股(高管持股)')
    S_SHARE_NTRD_INSDEREMP = Column(Numeric(20, 4), comment='内部职工股(万股)')
    S_SHARE_NTRD_PRFSHARE = Column(Numeric(20, 4), comment='优先股(万股)')
    S_SHARE_NTRD_NONLSTFRGN = Column(Numeric(20, 4), comment='非流通股(非上市外资股)')
    S_SHARE_NTRD_STAQ = Column(Numeric(20, 4), comment='STAQ股(万股)')
    S_SHARE_NTRD_NET = Column(Numeric(20, 4), comment='NET股(万股)')
    S_SHARE_CHANGEREASON = Column(VARCHAR(30), comment='股本变动原因')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DT1 = Column(VARCHAR(8), comment='变动日期1')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
    S_SHARE_TOTALA = Column(Numeric(20, 4), comment='A股合计')
    S_SHARE_TOTALB = Column(Numeric(20, 4), comment='B股合计')
    S_SHARE_OTCA = Column(Numeric(20, 4), comment='三板A股')
    S_SHARE_OTCB = Column(Numeric(20, 4), comment='三板B股')
    S_SHARE_TOTALOTC = Column(Numeric(20, 4), comment='三板合计')
    S_SHARE_H = Column(Numeric(20, 4), comment='香港上市股')
    S_SHARE_TOTALTRADABLE = Column(Numeric(20, 4), comment='流通股合计')
    S_SHARE_TOTALRESTRICTED = Column(Numeric(20, 4), comment='限售股合计')
    S_SHARE_NONTRADABLE = Column(Numeric(20, 4), comment='股改前非流通股')
    IS_VALID = Column(Numeric(5, 0), comment='是否有效')


class ASHARECAPITALOPERATION(Base):
    """中国A股证券投资"""
    __tablename__ = 'ASHARECAPITALOPERATION'
    __table_args__ = (
        Index('IDX_ASHARECAPITALOPERATION_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_CAPITALOPERATION_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_CAPITALOPERATION_SHARE = Column(Numeric(20, 4), comment='股票数量')
    S_CAPITALOPERATION_AMOUNT = Column(Numeric(20, 4), comment='投资金额')
    CRNCY_CODE = Column(VARCHAR(3), comment='货币代码')
    S_CAPITALOPERATION_COMPANYNAME = Column(VARCHAR(100), comment='参股公司名称')
    S_CAPITALOPERAT_COMPWINDCODE = Column(VARCHAR(40), comment='参股公司Wind代码')
    S_END_BAL = Column(Numeric(20, 4), comment='期末账面值')


class ASHARECAPITALSURPLUS(Base):
    """中国A股财务附注--资本公积"""
    __tablename__ = 'ASHARECAPITALSURPLUS'
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


class ASHARECASHADEPOSITSWITHCB(Base):
    """中国A股财务附注--现金及存放中央银行款项"""
    __tablename__ = 'ASHARECASHADEPOSITSWITHCB'
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


class ASHARECASHFLOW(Base):
    """中国A股现金流量表"""
    __tablename__ = 'ASHARECASHFLOW'
    __table_args__ = (
        Index('fass', 'S_INFO_WINDCODE', 'REPORT_PERIOD', 'CASH_RECP_SG_AND_RS', 'RECP_TAX_RENDS', 'NET_INCR_DEP_COB',
              'NET_INCR_LOANS_CENTRAL_BANK', 'NET_INCR_FUND_BORR_OFI', 'CASH_RECP_PREM_ORIG_INCO',
              'NET_INCR_INSURED_DEP', 'NET_CASH_RECEIVED_REINSU_BUS', 'NET_INCR_DISP_TFA', 'NET_INCR_INT_HANDLING_CHRG',
              'NET_INCR_DISP_FAAS', 'NET_INCR_LOANS_OTHER_BANK', 'NET_INCR_REPURCH_BUS_FUND',
              'OTHER_CASH_RECP_RAL_OPER_ACT', 'STOT_CASH_INFLOWS_OPER_ACT', 'CASH_PAY_GOODS_PURCH_SERV_REC',
              'CASH_PAY_BEH_EMPL', 'PAY_ALL_TYP_TAX', 'NET_INCR_CLIENTS_LOAN_ADV', 'NET_INCR_DEP_CBOB',
              'CASH_PAY_CLAIMS_ORIG_INCO', 'HANDLING_CHRG_PAID', 'COMM_INSUR_PLCY_PAID', 'OTHER_CASH_PAY_RAL_OPER_ACT',
              'STOT_CASH_OUTFLOWS_OPER_ACT', 'NET_CASH_FLOWS_OPER_ACT', 'CASH_RECP_DISP_WITHDRWL_INVEST',
              'CASH_RECP_RETURN_INVEST', 'NET_CASH_RECP_DISP_FIOLTA', 'NET_CASH_RECP_DISP_SOBU',
              'OTHER_CASH_RECP_RAL_INV_ACT', 'STOT_CASH_INFLOWS_INV_ACT', 'CASH_PAY_ACQ_CONST_FIOLTA',
              'CASH_PAID_INVEST', 'NET_CASH_PAY_AQUIS_SOBU', 'OTHER_CASH_PAY_RAL_INV_ACT', 'NET_INCR_PLEDGE_LOAN',
              'STOT_CASH_OUTFLOWS_INV_ACT', 'NET_CASH_FLOWS_INV_ACT', 'CASH_RECP_CAP_CONTRIB', 'INCL_CASH_REC_SAIMS',
              'CASH_RECP_BORROW', 'PROC_ISSUE_BONDS', 'OTHER_CASH_RECP_RAL_FNC_ACT', 'STOT_CASH_INFLOWS_FNC_ACT',
              'CASH_PREPAY_AMT_BORR', 'CASH_PAY_DIST_DPCP_INT_EXP', 'INCL_DVD_PROFIT_PAID_SC_MS',
              'OTHER_CASH_PAY_RAL_FNC_ACT', 'STOT_CASH_OUTFLOWS_FNC_ACT', 'NET_CASH_FLOWS_FNC_ACT', 'EFF_FX_FLU_CASH',
              'NET_INCR_CASH_CASH_EQU', 'CASH_CASH_EQU_BEG_PERIOD', 'CASH_CASH_EQU_END_PERIOD', 'NET_PROFIT',
              'UNCONFIRMED_INVEST_LOSS', 'PLUS_PROV_DEPR_ASSETS', 'DEPR_FA_COGA_DPBA', 'AMORT_INTANG_ASSETS',
              'AMORT_LT_DEFERRED_EXP', 'DECR_DEFERRED_EXP', 'INCR_ACC_EXP', 'LOSS_DISP_FIOLTA', 'LOSS_SCR_FA',
              'LOSS_FV_CHG', 'FIN_EXP', 'INVEST_LOSS', 'DECR_DEFERRED_INC_TAX_ASSETS', 'INCR_DEFERRED_INC_TAX_LIAB',
              'DECR_INVENTORIES', 'DECR_OPER_PAYABLE', 'INCR_OPER_PAYABLE', 'OTHERS', 'IM_NET_CASH_FLOWS_OPER_ACT',
              'CONV_DEBT_INTO_CAP', 'CONV_CORP_BONDS_DUE_WITHIN_1Y', 'FA_FNC_LEASES', 'END_BAL_CASH',
              'LESS_BEG_BAL_CASH', 'PLUS_END_BAL_CASH_EQU', 'LESS_BEG_BAL_CASH_EQU', 'IM_NET_INCR_CASH_CASH_EQU',
              'FREE_CASH_FLOW', 'SPE_BAL_CASH_INFLOWS_OPER', 'TOT_BAL_CASH_INFLOWS_OPER', 'SPE_BAL_CASH_OUTFLOWS_OPER',
              'TOT_BAL_CASH_OUTFLOWS_OPER', 'TOT_BAL_NETCASH_OUTFLOWS_OPER', 'SPE_BAL_CASH_INFLOWS_INV',
              'TOT_BAL_CASH_INFLOWS_INV', 'SPE_BAL_CASH_OUTFLOWS_INV', 'TOT_BAL_CASH_OUTFLOWS_INV',
              'TOT_BAL_NETCASH_OUTFLOWS_INV', 'SPE_BAL_CASH_INFLOWS_FNC', 'TOT_BAL_CASH_INFLOWS_FNC',
              'SPE_BAL_CASH_OUTFLOWS_FNC', 'TOT_BAL_CASH_OUTFLOWS_FNC', 'TOT_BAL_NETCASH_OUTFLOWS_FNC',
              'SPE_BAL_NETCASH_INC', 'TOT_BAL_NETCASH_INC', 'SPE_BAL_NETCASH_EQU_UNDIR', 'TOT_BAL_NETCASH_EQU_UNDIR',
              'SPE_BAL_NETCASH_INC_UNDIR', 'TOT_BAL_NETCASH_INC_UNDIR', 'S_DISMANTLE_CAPITAL_ADD_NET',
              'SECURITIE_NETCASH_RECEIVED', 'OTHER_IMPAIR_LOSS_ASSETS', 'CREDIT_IMPAIRMENT_LOSS',
              'RIGHT_USE_ASSETS_DEP'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
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
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_DISMANTLE_CAPITAL_ADD_NET = Column(Numeric(20, 4), comment='拆出资金净增加额')
    IS_CALCULATION = Column(Numeric(5, 0), comment='是否计算报表')
    SECURITIE_NETCASH_RECEIVED = Column(Numeric(20, 4), comment='代理买卖证券收到的现金净额(元)')
    OTHER_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='其他资产减值损失')
    CREDIT_IMPAIRMENT_LOSS = Column(Numeric(20, 4), comment='信用减值损失')
    RIGHT_USE_ASSETS_DEP = Column(Numeric(20, 4), comment='使用权资产折旧')


class ASHARECHANGEWINDCODE(Base):
    """None"""
    __tablename__ = 'ASHARECHANGEWINDCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后代码')
    CHANGE_DATE = Column(VARCHAR(10), comment='代码变更日期')


class ASHARECIRCULATINGHOLDERS(Base):
    """中国A股流通股东持股比例"""
    __tablename__ = 'ASHARECIRCULATINGHOLDERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(200), comment='股东公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='股东公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='股东公司ID')
    S_HOLDER_ENDDATE = Column(VARCHAR(10), comment='报告期')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例')


class ASHARECJZQINDUSTRIESCLASS(Base):
    """中国A股长江证券行业分类"""
    __tablename__ = 'ASHARECJZQINDUSTRIESCLASS'
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='长江证券行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')


class ASHARECNIINDUSTRIESCLASS(Base):
    """中国A股国证行业分类"""
    __tablename__ = 'ASHARECNIINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_IND_CODE = Column(VARCHAR(50), comment='国证行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHARECOCAPITALOPERATION(Base):
    """中国A股公司资本运作"""
    __tablename__ = 'ASHARECOCAPITALOPERATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    S_EVENT_ID = Column(VARCHAR(40), comment='事件ID')
    S_EVENT_CATEGORYCODE = Column(Numeric(9, 0), comment='事件类型代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_FINANCING_AMOUNT = Column(Numeric(20, 4), comment='融资金额(人民币)')
    S_VALUATION_AMOUNT = Column(Numeric(20, 4), comment='估值金额(人民币)')
    S_PE = Column(Numeric(20, 4), comment='市盈率(PE)')
    S_PB = Column(Numeric(20, 4), comment='市净率(PB)')
    S_PS = Column(Numeric(20, 4), comment='市销率(PS)')
    S_FINANCING_RATE = Column(Numeric(20, 4), comment='融资费率')
    S_FINANCING_RT = Column(Numeric(20, 4), comment='融资利率')
    S_FINANCING_AMOUNT_US = Column(Numeric(20, 4), comment='融资金额(美元)')
    S_VALUATION_AMOUNT_US = Column(Numeric(20, 4), comment='估值金额(美元)')
    S_EVENT_DESCRIPTION = Column(VARCHAR(1000), comment='事件说明')
    S_FINANCING_PROCESS = Column(Numeric(9, 0), comment='融资进程')


class ASHARECODEANDSNAME(Base):
    """None"""
    __tablename__ = 'ASHARECODEANDSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='品种ID')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务代码类型')
    S_CODE = Column(VARCHAR(40), comment='业务代码')
    S_SNAME = Column(VARCHAR(100), comment='业务简称')
    IS_COMMON = Column(Numeric(1, 0), comment='是否通用代码')
    MEMO = Column(VARCHAR(800), comment='业务说明')


class ASHARECOMPANYFILINGS(Base):
    """None"""
    __tablename__ = 'ASHARECOMPANYFILINGS'
    __table_args__ = (
        Index('IDX_ASHARECOMPANYFILINGS_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_EST_FLSTITLE_INST = Column(VARCHAR(400), comment='标题')
    S_EST_FLSABSTRACT_INST = Column(TEXT(2147483647), comment='摘要')


class ASHARECOMPANYHOLDSHARES(Base):
    """中国A股控股参股"""
    __tablename__ = 'ASHARECOMPANYHOLDSHARES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_CAPITALOPERATION_COMPANYNAME = Column(VARCHAR(100), comment='被参控公司名称')
    S_CAPITALOPERATION_COMPANYID = Column(VARCHAR(10), comment='被参控公司ID')
    S_CAPITALOPERATION_COMAINBUS = Column(VARCHAR(1100), comment='被参控公司主营业务')
    RELATIONS_CODE = Column(VARCHAR(40), comment='关系代码')
    S_CAPITALOPERATION_PCT = Column(Numeric(20, 4), comment='直接持股比例')
    VOTING_RIGHTS = Column(Numeric(20, 4), comment='表决权比例')
    S_CAPITALOPERATION_AMOUNT = Column(Numeric(20, 4), comment='投资金额(万元)')
    OPERATIONCRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_CAPITALOPERATION_COREGCAP = Column(Numeric(20, 4), comment='被参股公司注册资本(万元)')
    CAPITALCRNCY_CODE = Column(VARCHAR(10), comment='注册资本货币代码')
    IS_CONSOLIDATE = Column(Numeric(5, 0), comment='是否合并报表')
    NOTCONSOLIDATE_REASON = Column(VARCHAR(500), comment='未纳入合并报表原因')


class ASHARECOMPDISCLOSURERESULTS(Base):
    """中国A股上市公司信息披露考评结果"""
    __tablename__ = 'ASHARECOMPDISCLOSURERESULTS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(10), comment='证券id')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    EV_RESULT_TYPE = Column(Numeric(9, 0), comment='考评结果类型代码')
    EV_START_DATE = Column(VARCHAR(8), comment='考评起始日期')
    EV_END_DATE = Column(VARCHAR(8), comment='考评截止日期')


class ASHARECOMPENSATIONPAYABLE(Base):
    """中国A股财务附注--应付职工薪酬"""
    __tablename__ = 'ASHARECOMPENSATIONPAYABLE'
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


class ASHARECOMPRESTRICTED(Base):
    """中国A股限售股解禁公司明细"""
    __tablename__ = 'ASHARECOMPRESTRICTED'
    __table_args__ = (
        Index('IDX_CODE_DATE', 'S_INFO_WINDCODE', 'S_INFO_LISTDATE'),
        Index('IDX_ASHARECOMPRESTRICTED_S_INFO_LISTDATE', 'S_INFO_LISTDATE'),)
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


class ASHARECONCEPTUALPLATE(Base):
    """中国A股公司概念板块"""
    __tablename__ = 'ASHARECONCEPTUALPLATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')


class ASHARECONSENSUSDATA(Base):
    """中国A股盈利预测汇总"""
    __tablename__ = 'ASHARECONSENSUSDATA'
    __table_args__ = (
        Index('IDX_ASHARECONSENSUSDATA_EST_DT', 'EST_DT'),
        Index('finshow', 'S_INFO_WINDCODE', 'EST_REPORT_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
    EST_DT = Column(VARCHAR(8), comment='预测日期')
    EST_REPORT_DT = Column(VARCHAR(8), comment='预测报告期')
    NUM_EST_INST = Column(Numeric(20, 0), comment='预测机构家数')
    EPS_AVG = Column(Numeric(20, 4), comment='每股收益平均值(元)')
    MAIN_BUS_INC_AVG = Column(Numeric(20, 4), comment='主营业务收入平均值(万元)')
    NET_PROFIT_AVG = Column(Numeric(20, 4), comment='净利润平均值(万元)')
    EBIT_AVG = Column(Numeric(20, 4), comment='息税前利润平均值(万元)')
    EBITDA_AVG = Column(Numeric(20, 4), comment='息税折旧摊销前利润平均值(万元)')
    EPS_MEDIAN = Column(Numeric(20, 4), comment='每股收益中值(元)')
    MAIN_BUS_INC_MEDIAN = Column(Numeric(20, 4), comment='主营业务收入中值(万元)')
    NET_PROFIT_MEDIAN = Column(Numeric(20, 4), comment='净利润中值(万元)')
    EBIT_MEDIAN = Column(Numeric(20, 4), comment='息税前利润中值(万元)')
    EBITDA_MEDIAN = Column(Numeric(20, 4), comment='息税折旧摊销前利润中值(万元)')
    CONSEN_DATA_CYCLE_TYP = Column(VARCHAR(10), comment='综合值周期类型')
    EPS_DEV = Column(Numeric(20, 4), comment='每股收益标准差')
    MAIN_BUS_INC_DEV = Column(Numeric(20, 4), comment='主营业务收入标准差(万元)')
    NET_PROFIT_DEV = Column(Numeric(20, 4), comment='净利润标准差(万元)')
    EBIT_DEV = Column(Numeric(20, 4), comment='息税前利润标准差(万元)')
    EBITDA_DEV = Column(Numeric(20, 4), comment='息税折旧摊销前利润标准差(万元)')
    EPS_MAX = Column(Numeric(20, 4), comment='每股收益最大值')
    EPS_MIN = Column(Numeric(20, 4), comment='每股收益最小值')
    MAIN_BUS_INC_MAX = Column(Numeric(20, 4), comment='主营业务收入最大值(万元)')
    MAIN_BUS_INC_MIN = Column(Numeric(20, 4), comment='主营业务收入最小值(万元)')
    MAIN_BUS_INC_UPGRADE = Column(Numeric(20, 4), comment='主营业务收入调高家数（与一个月前相比）')
    MAIN_BUS_INC_DOWNGRADE = Column(Numeric(20, 4), comment='主营业务收入调低家数（与一个月前相比）')
    MAIN_BUS_INC_MAINTAIN = Column(Numeric(20, 4), comment='主营业务收入维持家数（与一个月前相比）')
    NET_PROFIT_MAX = Column(Numeric(20, 4), comment='净利润最大值（万元)')
    NET_PROFIT_MIN = Column(Numeric(20, 4), comment='净利润最小值（万元)')
    NET_PROFIT_UPGRADE = Column(Numeric(20, 4), comment='净利润调高家数（与一个月前相比）')
    NET_PROFIT_DOWNGRADE = Column(Numeric(20, 4), comment='净利润调低家数（与一个月前相比）')
    NET_PROFIT_MAINTAIN = Column(Numeric(20, 4), comment='净利润维持家数（与一个月前相比）')
    S_EST_AVGCPS = Column(Numeric(20, 4), comment='每股现金流平均值')
    S_EST_MEDIANCPS = Column(Numeric(20, 4), comment='每股现金流中值')
    S_EST_STDCPS = Column(Numeric(20, 4), comment='每股现金流标准差')
    S_EST_MAXCPS = Column(Numeric(20, 4), comment='每股现金流最大值')
    S_EST_MINCPS = Column(Numeric(20, 4), comment='每股现金流最小值')
    S_EST_AVGDPS = Column(Numeric(20, 4), comment='每股股利平均值')
    S_EST_MEDIANDPS = Column(Numeric(20, 4), comment='每股股利中值')
    S_EST_STDDPS = Column(Numeric(20, 4), comment='每股股利标准差')
    S_EST_MAXDPS = Column(Numeric(20, 4), comment='每股股利最大值')
    S_EST_MINDPS = Column(Numeric(20, 4), comment='每股股利最小值')
    EBIT_MAX = Column(Numeric(20, 4), comment='息税前利润最大值(万元)')
    EBIT_MIN = Column(Numeric(20, 4), comment='息税前利润最小值(万元)')
    EBITDA_MAX = Column(Numeric(20, 4), comment='息税折旧摊销前利润最大值(万元)')
    EBITDA_MIN = Column(Numeric(20, 4), comment='息税折旧摊销前利润最小值(万元)')
    S_EST_AVGBPS = Column(Numeric(20, 4), comment='每股净资产平均值')
    S_EST_MEDIANBPS = Column(Numeric(20, 4), comment='每股净资产中值')
    S_EST_STDBPS = Column(Numeric(20, 4), comment='每股净资产标准差')
    S_EST_MAXBPS = Column(Numeric(20, 4), comment='每股净资产最大值')
    S_EST_MINBPS = Column(Numeric(20, 4), comment='每股净资产最小值')
    S_EST_AVGEBT = Column(Numeric(20, 4), comment='利润总额平均值(万元)')
    S_EST_MEDIANEBT = Column(Numeric(20, 4), comment='利润总额中值(万元)')
    S_EST_STDEBT = Column(Numeric(20, 4), comment='利润总额标准差(万元)')
    S_EST_MAXEBT = Column(Numeric(20, 4), comment='利润总额最大值(万元)')
    S_EST_MINEBT = Column(Numeric(20, 4), comment='利润总额最小值(万元)')
    S_EST_AVGROA = Column(Numeric(20, 4), comment='总资产收益率平均值（%）')
    S_EST_MEDIANROA = Column(Numeric(20, 4), comment='总资产收益率中值（%）')
    S_EST_STDROA = Column(Numeric(20, 4), comment='总资产收益率标准差（%）')
    S_EST_MAXROA = Column(Numeric(20, 4), comment='总资产收益率最大值（%）')
    S_EST_MINROA = Column(Numeric(20, 4), comment='总资产收益率最小值（%）')
    S_EST_AVGROE = Column(Numeric(20, 4), comment='净资产收益率平均值（%）')
    S_EST_MEDIANROE = Column(Numeric(20, 4), comment='净资产收益率中值（%）')
    S_EST_STDROE = Column(Numeric(20, 4), comment='净资产收益率标准差（%）')
    S_EST_MAXROE = Column(Numeric(20, 4), comment='净资产收益率最大值（%）')
    S_EST_MINROE = Column(Numeric(20, 4), comment='净资产收益率最小值（%）')
    S_EST_AVGOPERATINGPROFIT = Column(Numeric(20, 4), comment='营业利润平均值(万元)')
    S_EST_MEDIANOPERATINGPROFIT = Column(Numeric(20, 4), comment='营业利润中值(万元)')
    S_EST_STDOPERATINGPROFIT = Column(Numeric(20, 4), comment='营业利润标准差(万元)')
    S_EST_MAXOPERATINGPROFIT = Column(Numeric(20, 4), comment='营业利润最大值(万元)')
    S_EST_MINOPERATINGPROFIT = Column(Numeric(20, 4), comment='营业利润最小值(万元)')
    S_EST_EPSINSTNUM = Column(Numeric(20, 4), comment='每股收益预测家数')
    S_EST_MAINBUSINCINSTNUM = Column(Numeric(20, 4), comment='主营业务收入预测家数')
    S_EST_NETPROFITINSTNUM = Column(Numeric(20, 4), comment='净利润预测家数')
    S_EST_CPSINSTNUM = Column(Numeric(20, 4), comment='每股现金流预测家数')
    S_EST_DPSINSTNUM = Column(Numeric(20, 4), comment='每股股利预测家数')
    S_EST_EBITINSTNUM = Column(Numeric(20, 4), comment='息税前利润预测家数')
    S_EST_EBITDAINSTNUM = Column(Numeric(20, 4), comment='息税折旧摊销前利润预测家数')
    S_EST_BPSINSTNUM = Column(Numeric(20, 4), comment='每股净资产预测家数')
    S_EST_EBTINSTNUM = Column(Numeric(20, 4), comment='利润总额预测家数')
    S_EST_ROAINSTNUM = Column(Numeric(20, 4), comment='总资产收益率预测家数')
    S_EST_ROEINSTNUM = Column(Numeric(20, 4), comment='净资产资产收益率预测家数')
    S_EST_OPROFITINSTNUM = Column(Numeric(20, 4), comment='营业利润预测家数')
    S_EST_AVGOC = Column(Numeric(20, 4), comment='营业成本及附加平均值(万元)')
    S_EST_MEDIAOC = Column(Numeric(20, 4), comment='营业成本及附加中值(万元)')
    S_EST_STOC = Column(Numeric(20, 4), comment='营业成本及附加标准差(万元)')
    S_EST_MAXOC = Column(Numeric(20, 4), comment='营业成本及附加最大值(万元)')
    S_EST_MINOC = Column(Numeric(20, 4), comment='营业成本及附加最小值(万元)')
    S_EST_OCINSTNUM = Column(Numeric(20, 4), comment='营业成本及附加预测家数')
    S_EST_BASESHARE = Column(Numeric(20, 4), comment='预测基准股本综合值')
    S_EST_YEARTYPE = Column(VARCHAR(20), comment='预测年度类型')


class ASHARECONSENSUSINDEX(Base):
    """Wind一致预测个股指标"""
    __tablename__ = 'ASHARECONSENSUSINDEX'
    __table_args__ = (
        Index('IDX_ASHARECONSENSUSINDEX_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='日期')
    EST_REPORT_DT = Column(VARCHAR(8), comment='报告期')
    PREDICTION_NUMBER = Column(Numeric(20, 0), comment='预测家数')
    EST_EPS = Column(Numeric(20, 4), comment='每股收益')
    EST_OPER_REVENUE = Column(Numeric(20, 4), comment='主营业务收入')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    EST_EPS_MAX = Column(Numeric(20, 4), comment='每股收益最大值')
    EST_EPS_MIN = Column(Numeric(20, 4), comment='每股收益最小值')
    EST_OPER_REVENUE_MAX = Column(Numeric(20, 4), comment='主营业务收入最大值')
    EST_OPER_REVENUE_MIN = Column(Numeric(20, 4), comment='主营业务收入最小值')
    EST_OPER_REVENUE_RAISED = Column(Numeric(20, 0), comment='主营业务收入调高家数（与1月前相比）')
    EST_OPER_REVENUE_DOWN = Column(Numeric(20, 0), comment='主营业务收入调低家数（与1月前相比）')
    EST_OPER_REVENUE_MAINTAIN = Column(Numeric(20, 0), comment='主营业务收入维持家数（与1月前相比）')
    NET_PROFIT_MAX = Column(Numeric(20, 4), comment='净利润最大值')
    NET_PROFIT_MIN = Column(Numeric(20, 4), comment='净利润最小值')
    NET_PROFIT_RAISED = Column(Numeric(20, 0), comment='净利润调高家数（与1月前相比）')
    NET_PROFIT_DOWN = Column(Numeric(20, 0), comment='净利润调低家数（与1月前相比）')
    NET_PROFIT_MAINTAIN = Column(Numeric(20, 0), comment='净利润维持家数（与1月前相比）')
    EST_EPS_MEDIAN = Column(Numeric(20, 4), comment='每股收益中值')
    EST_EPS_DIFFERENCE = Column(Numeric(20, 4), comment='每股收益标准差')
    EST_OPER_REVENUE_MEDIAN = Column(Numeric(20, 4), comment='主营业务收入中值')
    EST_OPER_REVENUE_DIF = Column(Numeric(20, 4), comment='主营业务收入标准差')
    NET_PROFIT_MEDIAN = Column(Numeric(20, 4), comment='净利润中值')
    NET_PROFIT_DIF = Column(Numeric(20, 4), comment='净利润标准差')
    EST_CFPS = Column(Numeric(20, 4), comment='每股现金流')
    EST_CFPS_MEDIAN = Column(Numeric(20, 4), comment='每股现金流中值')
    EST_CFPS_DIF = Column(Numeric(20, 4), comment='每股现金流标准差')
    EST_CFPS_MAX = Column(Numeric(20, 4), comment='每股现金流最大值')
    EST_CFPS_MIN = Column(Numeric(20, 4), comment='每股现金流最小值')
    EST_DPS = Column(Numeric(20, 4), comment='每股股利')
    EST_DPS_MEDIAN = Column(Numeric(20, 4), comment='每股股利中值')
    EST_DPS_DIF = Column(Numeric(20, 4), comment='每股股利标准差')
    EST_DPS_MAX = Column(Numeric(20, 4), comment='每股股利最大值')
    EST_DPS_MIN = Column(Numeric(20, 4), comment='每股股利最小值')
    EST_EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EST_EBIT_MEDIAN = Column(Numeric(20, 4), comment='息税前利润中值')
    EST_EBIT_DIF = Column(Numeric(20, 4), comment='息税前利润标准差')
    EST_EBIT_MAX = Column(Numeric(20, 4), comment='息税前利润最大值')
    EST_EBIT_MIN = Column(Numeric(20, 4), comment='息税前利润最小值')
    EST_EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    EST_EBITDA_MEDIAN = Column(Numeric(20, 4), comment='息税折旧摊销前利润中值')
    EST_EBITDA_DIF = Column(Numeric(20, 4), comment='息税折旧摊销前利润标准差')
    EST_EBITDA_MAX = Column(Numeric(20, 4), comment='息税折旧摊销前利润最大值')
    EST_EBITDA_MIN = Column(Numeric(20, 4), comment='息税折旧摊销前利润最小值')
    EST_BPS = Column(Numeric(20, 4), comment='每股净资产')
    EST_BPS_MEDIAN = Column(Numeric(20, 4), comment='每股净资产中值')
    EST_BPS_DIF = Column(Numeric(20, 4), comment='每股净资产标准差')
    EST_BPS_MAX = Column(Numeric(20, 4), comment='每股净资产最大值')
    EST_BPS_MIN = Column(Numeric(20, 4), comment='每股净资产最小值')
    EST_TOTAL_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    EST_TOTAL_PROFIT_MEDIAN = Column(Numeric(20, 4), comment='利润总额中值')
    EST_TOTAL_PROFIT_DIF = Column(Numeric(20, 4), comment='利润总额标准差')
    EST_TOTAL_PROFIT_MAX = Column(Numeric(20, 4), comment='利润总额最大值')
    EST_TOTAL_PROFIT_MIN = Column(Numeric(20, 4), comment='利润总额最小值')
    RETURN_ASSETS = Column(Numeric(20, 4), comment='总资产收益率')
    RETURN_ASSETS_MEDIAN = Column(Numeric(20, 4), comment='总资产收益率中值')
    RETURN_ASSETS_DIF = Column(Numeric(20, 4), comment='总资产收益率标准差')
    RETURN_ASSETS_MAX = Column(Numeric(20, 4), comment='总资产收益率最大值')
    RETURN_ASSETS_MIN = Column(Numeric(20, 4), comment='总资产收益率最小值')
    EST_ROE = Column(Numeric(20, 4), comment='净资产收益率')
    EST_ROE_MEDIAN = Column(Numeric(20, 4), comment='净资产收益率中值')
    EST_ROE_DIF = Column(Numeric(20, 4), comment='净资产收益率标准差')
    EST_ROE_MAX = Column(Numeric(20, 4), comment='净资产收益率最大值')
    EST_ROE_MIN = Column(Numeric(20, 4), comment='净资产收益率最小值')
    EST_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    EST_OPER_PROFIT_MEDIAN = Column(Numeric(20, 4), comment='营业利润中值')
    EST_OPER_PROFIT_DIF = Column(Numeric(20, 4), comment='营业利润标准差')
    EST_OPER_PROFIT_MAX = Column(Numeric(20, 4), comment='营业利润最大值')
    EST_OPER_PROFIT_MIN = Column(Numeric(20, 4), comment='营业利润最小值')
    EST_EPS_NUM = Column(Numeric(20, 0), comment='每股收益预测家数')
    EST_OPER_REVENUE_NUM = Column(Numeric(20, 0), comment='主营业务收入预测家数')
    NET_PROFIT_NUM = Column(Numeric(20, 0), comment='净利润预测家数')
    EST_CFPS_NUM = Column(Numeric(20, 0), comment='每股现金流预测家数')
    EST_DPS_NUM = Column(Numeric(20, 0), comment='每股股利预测家数')
    EST_EBIT_NUM = Column(Numeric(20, 0), comment='息税前利润预测家数')
    EST_EBITDA_NUM = Column(Numeric(20, 0), comment='息税折旧摊销前利润预测家数')
    EST_BPS_NUM = Column(Numeric(20, 0), comment='每股净资产预测家数')
    EST_TOTAL_PROFIT_NUM = Column(Numeric(20, 0), comment='利润总额预测家数')
    RETURN_ASSETS_NUM = Column(Numeric(20, 0), comment='总资产收益率预测家数')
    EST_ROE_NUM = Column(Numeric(20, 0), comment='净资产收益率预测家数')
    EST_OPER_PROFIT_NUM = Column(Numeric(20, 0), comment='营业利润预测家数')


class ASHARECONSENSUSROLLINGDATA(Base):
    """Wind一致预测个股滚动指标"""
    __tablename__ = 'ASHARECONSENSUSROLLINGDATA'
    __table_args__ = (
        Index('IDX_ASHARECONSENSUSROLLINGDATA_EST_DT', 'EST_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EST_DT = Column(VARCHAR(8), comment='日期')
    ROLLING_TYPE = Column(VARCHAR(10), comment='类型')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    EST_EPS = Column(Numeric(20, 4), comment='每股收益')
    EST_PE = Column(Numeric(20, 4), comment='市盈率')
    EST_PEG = Column(Numeric(20, 4), comment='PEG')
    EST_PB = Column(Numeric(20, 4), comment='市净率')
    EST_ROE = Column(Numeric(20, 4), comment='净资产收益率')
    EST_OPER_REVENUE = Column(Numeric(20, 4), comment='营业收入')
    EST_CFPS = Column(Numeric(20, 4), comment='每股现金流')
    EST_DPS = Column(Numeric(20, 4), comment='每股股利')
    EST_BPS = Column(Numeric(20, 4), comment='每股净资产')
    EST_EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EST_EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    EST_TOTAL_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    EST_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    EST_OPER_COST = Column(Numeric(20, 4), comment='营业成本及附加')
    BENCHMARK_YR = Column(VARCHAR(8), comment='基准年度')
    EST_BASESHARE = Column(Numeric(20, 4), comment='预测基准股本综合值')


class ASHARECONSEPTION(Base):
    """中国A股Wind概念板块"""
    __tablename__ = 'ASHARECONSEPTION'
    __table_args__ = (
        Index('fass', 'WIND_SEC_CODE', 'S_INFO_WINDCODE', 'ENTRY_DT', 'REMOVE_DT'),
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_SEC_CODE = Column(VARCHAR(50), comment='Wind概念板块代码')
    WIND_SEC_NAME = Column(VARCHAR(100), comment='Wind概念板块名称')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')
    WIND_SEC_NAME_ENG = Column(VARCHAR(200), comment='Wind概念板块英文名称')


class ASHARECONSEPTIONQL(Base):
    """None"""
    __tablename__ = 'ASHARECONSEPTIONQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    WIND_SEC_CODE = Column(VARCHAR(50))
    WIND_SEC_NAME = Column(VARCHAR(100))
    ENTRY_DT = Column(VARCHAR(8))
    REMOVE_DT = Column(VARCHAR(8))
    CUR_SIGN = Column(VARCHAR(10))
    WIND_SEC_NAME_ENG = Column(VARCHAR(200))


class ASHARECONSEPTIONZL(Base):
    """中国A股Wind概念板块(增量)"""
    __tablename__ = 'ASHARECONSEPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    WIND_SEC_CODE = Column(VARCHAR(50))
    WIND_SEC_NAME = Column(VARCHAR(100))
    ENTRY_DT = Column(VARCHAR(8))
    REMOVE_DT = Column(VARCHAR(8))
    CUR_SIGN = Column(VARCHAR(10))
    WIND_SEC_NAME_ENG = Column(VARCHAR(200))


class ASHARECORPOLETDESCRIPTION(Base):
    """中国A股函件基本资料"""
    __tablename__ = 'ASHARECORPOLETDESCRIPTION'
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    LETTERS_EVENT_ID = Column(VARCHAR(20), comment='函件事件ID')
    LETTERS_DEPARTMENT = Column(VARCHAR(100), comment='发函部门')
    LETTERS_DEPARTMENT_ID = Column(VARCHAR(10), comment='发函单位ID')
    LETTERS_NUMBER = Column(VARCHAR(200), comment='函件文号')
    LETTERS_TITLE = Column(VARCHAR(500), comment='函件标题')
    LETTERS_TYPE_CODE = Column(Numeric(9, 0), comment='函件类型代码')
    LETTERS_ANN_DT = Column(VARCHAR(8), comment='发函公告日')
    REQUEST_DATE = Column(VARCHAR(8), comment='要求回函日期')
    EXTENSION_REPLY_DATE = Column(VARCHAR(8), comment='申请延期回复日期')
    IS_EXTENSION_REPLY = Column(Numeric(1, 0), comment='是否延期回复')
    REPLY_ANNOUCEMENT_DATE = Column(VARCHAR(8), comment='回函公告日')
    SUPPLEMENTARY_DATE = Column(VARCHAR(8), comment='补充回函公告日')
    EXTENSION_REPLY_ADATE = Column(VARCHAR(8), comment='申请延期回复公告日')
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')


class ASHARECORPOLETINFOR(Base):
    """中国A股函件内容表"""
    __tablename__ = 'ASHARECORPOLETINFOR'
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    COMP_ID = Column(VARCHAR(10), comment='公司ID')
    PROB_ID = Column(Numeric(11, 0), comment='问题ID')
    LETTERS_EVENT_ID = Column(VARCHAR(20), comment='函件事件ID')
    NUMBER1 = Column(Numeric(20, 0), comment='序号')
    PROB_TYPE = Column(VARCHAR(1024), comment='问题类型代码')
    PROB_TXT = Column(VARCHAR(4000), comment='问题文本')
    ANSW_TXT = Column(VARCHAR, comment='回答文本')
    SUP_ANSW_TXT = Column(VARCHAR(4000), comment='补充回答文本')
    IS_VALID = Column(Numeric(1, 0), comment='是否有效')
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')


class ASHARECORPORATEFINANCE(Base):
    """中国A股购买理财产品"""
    __tablename__ = 'ASHARECORPORATEFINANCE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    EVENT_ID = Column(VARCHAR(40), comment='事件ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    BUY_COMPANY_NAME = Column(VARCHAR(100), comment='实际购买公司名称')
    S_RELATION_TYPCODE = Column(Numeric(9, 0), comment='实际购买公司和上市公司关系类型代码')
    S_ISSUER_NAME = Column(VARCHAR(100), comment='产品发行方公布名称')
    S_ISSUER_ID = Column(VARCHAR(10), comment='产品发行方ID')
    S_FULLNAME = Column(VARCHAR(200), comment='理财产品名称')
    S_INFO_CODE = Column(VARCHAR(10), comment='[内部]理财产品ID')
    S_UNDERLYING = Column(Numeric(9, 0), comment='理财类型代码')
    S_SUBSCRIPTION_DATE = Column(VARCHAR(8), comment='认购日期')
    S_SUBSCRIPTION_AMOUNT = Column(Numeric(20, 4), comment='认购金额')
    S_CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INCOMESTARTDATE = Column(VARCHAR(8), comment='产品起息日期')
    S_INCOMEENDDATE = Column(VARCHAR(8), comment='产品到期日期')
    S_COMMISSION = Column(VARCHAR(40), comment='产品期限')
    S_EXPYIDLD_MIN = Column(Numeric(20, 4), comment='预计最低收益率')
    S_EXPYIELD_MAX = Column(Numeric(20, 4), comment='预计最高收益率')
    S_SOURCES_FUNDS_CODE = Column(Numeric(9, 0), comment='资金来源类型代码')
    IS_CONNECTION_RELATION = Column(Numeric(1, 0), comment='买方与卖方是否有关联关系')
    S_NET_ASSETS_RATIO = Column(Numeric(20, 4), comment='本次出资占公司最近一期审计净资产比例')
    S_SUMMARY = Column(VARCHAR(2000), comment='理财产品摘要')


class ASHARECREDITORRIGHTS(Base):
    """中国A股关联方债权"""
    __tablename__ = 'ASHARECREDITORRIGHTS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='债务公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='债务公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='债务公司公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class ASHARECSINDUSTRIESCLASS(Base):
    """中国A股中证行业成分明细"""
    __tablename__ = 'ASHARECSINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CS_IND_CODE = Column(VARCHAR(50), comment='中证行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')
    CS_IND4_CODE = Column(VARCHAR(50), comment='中证行业代码(四级)')


class ASHARECSINDUSTRIESCLASSZL(Base):
    """中国A股中证行业成分明细(增量)"""
    __tablename__ = 'ASHARECSINDUSTRIESCLASSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CS_IND_CODE = Column(VARCHAR(50), comment='中证行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')
    CS_IND4_CODE = Column(VARCHAR(50), comment='中证行业代码(四级)')


class ASHARECUSTOMER(Base):
    """中国A股公司客户"""
    __tablename__ = 'ASHARECUSTOMER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='下游公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(100), comment='下游公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='下游公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')
    S_INFO_DISCLOSER = Column(VARCHAR(100), comment='披露公司ID')


class ASHAREDEBTINVESTMENT(Base):
    """中国A股财务附注--债权投资"""
    __tablename__ = 'ASHAREDEBTINVESTMENT'
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


class ASHAREDEFENDANT(Base):
    """中国A股公司诉讼-被告"""
    __tablename__ = 'ASHAREDEFENDANT'
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


class ASHAREDEFERREDTAXASSETS(Base):
    """中国A股财务附注--递延所得税资产"""
    __tablename__ = 'ASHAREDEFERREDTAXASSETS'
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


class ASHAREDEFERREDTAXLIABILITY(Base):
    """中国A股财务附注--递延所得税负债"""
    __tablename__ = 'ASHAREDEFERREDTAXLIABILITY'
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


class ASHAREDESCRIPTION(Base):
    """中国A股基本资料"""
    __tablename__ = 'ASHAREDESCRIPTION'
    __table_args__ = (
        Index('IDX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
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
    S_INFO_SEDOLCODE = Column(VARCHAR(40))
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_PINYIN = Column(VARCHAR(40), comment='简称拼音')
    S_INFO_LISTBOARDNAME = Column(VARCHAR(10), comment='上市板')
    IS_SHSC = Column(Numeric(5, 0), comment='是否在沪股通或深港通范围内')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')


class ASHAREDEVALUATIONPREPARATION(Base):
    """中国A股资产减值准备明细表"""
    __tablename__ = 'ASHAREDEVALUATIONPREPARATION'
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
    S_ACCT_RCV = Column(Numeric(20, 4), comment='应收帐款')
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
    S_PRE_BAD_LOANS = Column(Numeric(20, 4), comment='贷款呆帐准备')
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


class ASHAREDIRECTOR(Base):
    """中国A股公司董事成员"""
    __tablename__ = 'ASHAREDIRECTOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='职务')
    S_INFO_MANID = Column(VARCHAR(10), comment='人物id')


class ASHAREDIVIDEND(Base):
    """中国A股分红"""
    __tablename__ = 'ASHAREDIVIDEND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DIV_PROGRESS = Column(VARCHAR(10), comment='方案进度')
    STK_DVD_PER_SH = Column(Numeric(20, 8), comment='每股送转')
    CASH_DVD_PER_SH_PRE_TAX = Column(Numeric(24, 8), comment='每股派息(税前)(元)')
    CASH_DVD_PER_SH_AFTER_TAX = Column(Numeric(24, 8), comment='每股派息(税后)(元)')
    EQY_RECORD_DT = Column(VARCHAR(8), comment='股权登记日')
    EX_DT = Column(VARCHAR(8), comment='除权除息日')
    DVD_PAYOUT_DT = Column(VARCHAR(8), comment='派息日')
    LISTING_DT_OF_DVD_SHR = Column(VARCHAR(8), comment='红股上市日')
    S_DIV_PRELANDATE = Column(VARCHAR(8), comment='预案公告日')
    S_DIV_SMTGDATE = Column(VARCHAR(8), comment='股东大会公告日')
    DVD_ANN_DT = Column(VARCHAR(8), comment='分红实施公告日')
    S_DIV_BASEDATE = Column(VARCHAR(8), comment='基准日期')
    S_DIV_BASESHARE = Column(Numeric(20, 4), comment='基准股本(万股)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日期')
    IS_CHANGED = Column(Numeric(5, 0), comment='方案是否变更')
    REPORT_PERIOD = Column(VARCHAR(8), comment='分红年度')
    S_DIV_CHANGE = Column(VARCHAR(800), comment='方案变更说明')
    S_DIV_BONUSRATE = Column(Numeric(20, 8), comment='每股送股比例')
    S_DIV_CONVERSEDRATE = Column(Numeric(20, 8), comment='每股转增比例')
    MEMO = Column(VARCHAR(200), comment='备注')
    S_DIV_PREANNDT = Column(VARCHAR(8), comment='预案预披露公告日')
    S_DIV_OBJECT = Column(VARCHAR(100), comment='分红对象')
    IS_TRANSFER = Column(Numeric(1, 0), comment='是否不分转')


class ASHAREDIVISIONELIMINATION(Base):
    """中国A股股权分置除权"""
    __tablename__ = 'ASHAREDIVISIONELIMINATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DQ_RESUMPDATE = Column(VARCHAR(8), comment='实施复牌日')
    S_DQ_ADJFACTOR = Column(Numeric(20, 4), comment='复权因子')
    S_DQ_RESUMP_PRECLOSE = Column(Numeric(20, 4), comment='复牌日昨收盘价')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价(流通股除权)')
    S_DQ_FACTOR = Column(Numeric(20, 8), comment='对价因子')


class ASHAREEARNINGEST(Base):
    """中国A股盈利预测明细"""
    __tablename__ = 'ASHAREEARNINGEST'
    __table_args__ = (
        Index('IDX_ASHAREEARNINGEST_EST_DT', 'EST_DT'),
        Index('finshow', 'S_INFO_WINDCODE', 'REPORTING_PERIOD', 'EST_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
    RESEARCH_INST_NAME = Column(VARCHAR(20), comment='研究机构名称')
    ANALYST_NAME = Column(VARCHAR(20), comment='分析师名称')
    EST_DT = Column(VARCHAR(8), comment='预测日期')
    REPORTING_PERIOD = Column(VARCHAR(8), comment='预测报告期')
    EST_EPS_DILUTED = Column(Numeric(20, 4), comment='预测每股收益(摊薄)(元)')
    EST_NET_PROFIT = Column(Numeric(20, 4), comment='预测净利润(万元)')
    EST_MAIN_BUS_INC = Column(Numeric(20, 4), comment='预测主营业务收入(万元)')
    EST_EBIT = Column(Numeric(20, 4), comment='预测息税前利润(万元)')
    EST_EBITDA = Column(Numeric(20, 4), comment='预测息税折旧摊销前利润(万元)')
    EST_BASE_CAP = Column(Numeric(20, 4), comment='预测基准股本(万股)')
    ANN_DT = Column(VARCHAR(8), comment='公告日期(内部)')
    S_EST_CPS = Column(Numeric(20, 4), comment='预测每股现金流')
    S_EST_DPS = Column(Numeric(20, 4), comment='预测每股股利')
    S_EST_BPS = Column(Numeric(20, 4), comment='预测每股净资产')
    S_EST_EBT = Column(Numeric(20, 4), comment='预测利润总额（万元）')
    S_EST_ROA = Column(Numeric(20, 4), comment='预测总资产收益率')
    S_EST_ROE = Column(Numeric(20, 4), comment='预测净资产收益率')
    S_EST_OPROFIT = Column(Numeric(20, 4), comment='预测营业利润(万元）')
    S_EST_EPSDILUTED = Column(Numeric(20, 4), comment='预测每股收益(稀释)(元)')
    S_EST_EPSBASIC = Column(Numeric(20, 4), comment='预测每股收益(基本)(元)')
    S_EST_OC = Column(Numeric(20, 4), comment='预测营业成本及附加（万元）')
    S_EST_NPCAL = Column(Numeric(20, 4), comment='预测净利润（换算）（万元）')
    S_EST_EPSCAL = Column(Numeric(20, 4), comment='预测每股收益（换算）')
    S_EST_NPRATE = Column(Numeric(20, 4), comment='预测净利润调整比率')
    S_EST_EPSRATE = Column(Numeric(20, 4), comment='预测EPS调整比率')
    S_EST_PE = Column(Numeric(20, 4), comment='预测市盈率')
    S_EST_PB = Column(Numeric(20, 4), comment='预测市净率')
    S_EST_EVEBITDA = Column(Numeric(20, 4), comment='预测EV/EBITDA')
    S_EST_DIVIDENDYIELD = Column(Numeric(20, 4), comment='预测股息率')
    S_EST_ENDDATE = Column(VARCHAR(8), comment='预测有效截止')
    S_EST_OPE = Column(Numeric(10, 4), comment='预测主营业务利润率')
    ANALYST_ID = Column(VARCHAR(200), comment='分析师id')
    COLLECT_TIME = Column(DateTime, comment='收录时间')
    FIRST_OPTIME = Column(DateTime, comment='首次入库时间')
    REPORT_TYPECODE = Column(Numeric(9, 0), comment='报告类型')
    REPORT_NAME = Column(VARCHAR(1024), comment='报告标题')
    REPORT_SUMMARY = Column(TEXT(2147483647), comment='报告摘要')
    EST_BASE_CAP_DIF_CODE = Column(Numeric(9, 0), comment='预测基准股本差异原因代码')
    S_EST_VALUE_CALCULATION = Column(Numeric(5, 0), comment='综合值计算标记')


class ASHAREEMBVALUEASSESSRESULTS(Base):
    """中国A股财务附注--内含价值评估结果"""
    __tablename__ = 'ASHAREEMBVALUEASSESSRESULTS'
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


class ASHAREEMBVALUECHANGEANAL(Base):
    """中国A股财务附注--内含价值变动分析"""
    __tablename__ = 'ASHAREEMBVALUECHANGEANAL'
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


class ASHAREENERGYINDEX(Base):
    """中国A股能量、量价与压力支撑技术指标(不复权)"""
    __tablename__ = 'ASHAREENERGYINDEX'
    __table_args__ = (
        Index('IDX_ASHAREENERGYINDEX_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    BOLL_MID = Column(Numeric(20, 8), comment='BOLL布林带MID(26日,2)')
    BOLL_UPPER = Column(Numeric(20, 8), comment='BOLL布林带UPPER(26日,2)')
    BOLL_LOWER = Column(Numeric(20, 8), comment='BOLL布林带LOWER(26日,2)')
    BBIBOLL_BBI = Column(Numeric(20, 8), comment='BBIBOLL多空布林线BBI(10日,3)')
    BBIBOLL_UPR = Column(Numeric(20, 8), comment='BBIBOLL多空布林线UPR(10日,3)')
    BBIBOLL_DWN = Column(Numeric(20, 8), comment='BBIBOLL多空布林线DWN(10日,3)')
    CDP = Column(Numeric(20, 8), comment='CDP逆势操作CDP')
    CDP_AH = Column(Numeric(20, 8), comment='CDP逆势操作AH')
    CDP_AL = Column(Numeric(20, 8), comment='CDP逆势操作AL')
    CDP_NH = Column(Numeric(20, 8), comment='CDP逆势操作NH')
    CDP_NL = Column(Numeric(20, 8), comment='CDP逆势操作NL')
    ENV_UPPER = Column(Numeric(20, 8), comment='ENV指标UPPER(14日)')
    ENV_LOWER = Column(Numeric(20, 8), comment='ENV指标LOWER(14日)')
    MIKE_WR = Column(Numeric(20, 8), comment='MIKE麦克指标WR(12日)')
    MIKE_MR = Column(Numeric(20, 8), comment='MIKE麦克指标MR(12日)')
    MIKE_SR = Column(Numeric(20, 8), comment='MIKE麦克指标SR(12日)')
    MIKE_WS = Column(Numeric(20, 8), comment='MIKE麦克指标WS(12日)')
    MIKE_MS = Column(Numeric(20, 8), comment='MIKE麦克指标MS(12日)')
    MIKE_SS = Column(Numeric(20, 8), comment='MIKE麦克指标SS(12日)')
    MFI = Column(Numeric(20, 8), comment='MFI资金流向指标(14日)')
    OBV = Column(Numeric(20, 8), comment='OBV能量潮OBV')
    OBV_OBV = Column(Numeric(20, 8), comment='OBV能量潮修正OBV')
    PVT = Column(Numeric(20, 8), comment='PVT量价趋势指标')
    WVAD_WVAD = Column(Numeric(20, 8), comment='WVAD威廉变异离散量WVAD(24,6日)')
    WVAD_MAWVAD = Column(Numeric(20, 8), comment='WVAD威廉变异离散量MAWVAD(24,6日)')
    ARBR_AR = Column(Numeric(20, 8), comment='ARBR人气意愿指标AR(26日)')
    ARBR_BR = Column(Numeric(20, 8), comment='ARBR人气意愿指标BR(26日)')
    CR = Column(Numeric(20, 8), comment='CR能量指标(26日)')
    PSY = Column(Numeric(20, 8), comment='PSY心理指标PSY(12,6日)')
    PSYMA = Column(Numeric(20, 8), comment='PSY心理指标PSYMA(12,6日)')
    WAD = Column(Numeric(20, 8), comment='WAD威廉聚散指标WAD(30日)')
    MAWAD = Column(Numeric(20, 8), comment='WAD威廉聚散指标MAWAD(30日)')


class ASHAREENERGYINDEXADJ(Base):
    """中国A股能量、量价与压力支撑技术指标(复权)"""
    __tablename__ = 'ASHAREENERGYINDEXADJ'
    __table_args__ = (
        Index('IDX_ASHAREENERGYINDEXADJ_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    BOLL_MID = Column(Numeric(20, 8), comment='BOLL布林带MID(26日,2)')
    BOLL_UPPER = Column(Numeric(20, 8), comment='BOLL布林带UPPER(26日,2)')
    BOLL_LOWER = Column(Numeric(20, 8), comment='BOLL布林带LOWER(26日,2)')
    BBIBOLL_BBI = Column(Numeric(20, 8), comment='BBIBOLL多空布林线BBI(10日,3)')
    BBIBOLL_UPR = Column(Numeric(20, 8), comment='BBIBOLL多空布林线UPR(10日,3)')
    BBIBOLL_DWN = Column(Numeric(20, 8), comment='BBIBOLL多空布林线DWN(10日,3)')
    CDP = Column(Numeric(20, 8), comment='CDP逆势操作CDP')
    CDP_AH = Column(Numeric(20, 8), comment='CDP逆势操作AH')
    CDP_AL = Column(Numeric(20, 8), comment='CDP逆势操作AL')
    CDP_NH = Column(Numeric(20, 8), comment='CDP逆势操作NH')
    CDP_NL = Column(Numeric(20, 8), comment='CDP逆势操作NL')
    ENV_UPPER = Column(Numeric(20, 8), comment='ENV指标UPPER(14日)')
    ENV_LOWER = Column(Numeric(20, 8), comment='ENV指标LOWER(14日)')
    MIKE_WR = Column(Numeric(20, 8), comment='MIKE麦克指标WR(12日)')
    MIKE_MR = Column(Numeric(20, 8), comment='MIKE麦克指标MR(12日)')
    MIKE_SR = Column(Numeric(20, 8), comment='MIKE麦克指标SR(12日)')
    MIKE_WS = Column(Numeric(20, 8), comment='MIKE麦克指标WS(12日)')
    MIKE_MS = Column(Numeric(20, 8), comment='MIKE麦克指标MS(12日)')
    MIKE_SS = Column(Numeric(20, 8), comment='MIKE麦克指标SS(12日)')
    MFI = Column(Numeric(20, 8), comment='MFI资金流向指标(14日)')
    OBV = Column(Numeric(20, 8), comment='OBV能量潮OBV')
    OBV_OBV = Column(Numeric(20, 8), comment='OBV能量潮修正OBV')
    PVT = Column(Numeric(20, 8), comment='PVT量价趋势指标')
    WVAD_WVAD = Column(Numeric(20, 8), comment='WVAD威廉变异离散量WVAD(24,6日)')
    WVAD_MAWVAD = Column(Numeric(20, 8), comment='WVAD威廉变异离散量MAWVAD(24,6日)')
    ARBR_AR = Column(Numeric(20, 8), comment='ARBR人气意愿指标AR(26日)')
    ARBR_BR = Column(Numeric(20, 8), comment='ARBR人气意愿指标BR(26日)')
    CR = Column(Numeric(20, 8), comment='CR能量指标(26日)')
    PSY = Column(Numeric(20, 8), comment='PSY心理指标PSY(12,6日)')
    PSYMA = Column(Numeric(20, 8), comment='PSY心理指标PSYMA(12,6日)')
    WAD = Column(Numeric(20, 8), comment='WAD威廉聚散指标WAD(30日)')
    MAWAD = Column(Numeric(20, 8), comment='WAD威廉聚散指标MAWAD(30日)')


class ASHAREENGINEERING(Base):
    """中国A股财务附注--在建工程"""
    __tablename__ = 'ASHAREENGINEERING'
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


class ASHAREEODDERIVATIVEINDICATOR(Base):
    """中国A股日行情估值指标"""
    __tablename__ = 'ASHAREEODDERIVATIVEINDICATOR'
    __table_args__ = (
        Index('IDX_ASHAREEODDERIVATIVEINDICATOR_TRADE_DT', 'TRADE_DT'),
        Index('fass', 'S_INFO_WINDCODE', 'TRADE_DT', 'S_VAL_MV', 'S_DQ_MV', 'S_PQ_HIGH_52W_', 'S_PQ_LOW_52W_',
              'S_VAL_PE', 'S_VAL_PB_NEW', 'S_VAL_PE_TTM', 'S_VAL_PCF_OCF', 'S_VAL_PCF_OCFTTM', 'S_VAL_PCF_NCF',
              'S_VAL_PCF_NCFTTM', 'S_VAL_PS', 'S_VAL_PS_TTM', 'S_DQ_TURN', 'S_DQ_FREETURNOVER', 'TOT_SHR_TODAY',
              'FLOAT_A_SHR_TODAY', 'S_DQ_CLOSE_TODAY', 'S_PRICE_DIV_DPS', 'S_PQ_ADJHIGH_52W', 'S_PQ_ADJLOW_52W',
              'FREE_SHARES_TODAY', 'NET_PROFIT_PARENT_COMP_TTM', 'NET_PROFIT_PARENT_COMP_LYR', 'NET_ASSETS_TODAY',
              'NET_CASH_FLOWS_OPER_ACT_TTM', 'NET_CASH_FLOWS_OPER_ACT_LYR', 'OPER_REV_TTM', 'OPER_REV_LYR',
              'NET_INCR_CASH_CASH_EQU_TTM', 'NET_INCR_CASH_CASH_EQU_LYR', 'UP_DOWN_LIMIT_STATUS',
              'LOWEST_HIGHEST_STATUS'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_VAL_MV = Column(Numeric(20, 4), comment='当日总市值')
    S_DQ_MV = Column(Numeric(20, 4), comment='当日流通市值')
    S_PQ_HIGH_52W_ = Column(Numeric(20, 4), comment='52周最高价')
    S_PQ_LOW_52W_ = Column(Numeric(20, 4), comment='52周最低价')
    S_VAL_PE = Column(Numeric(20, 4), comment='市盈率(PE)')
    S_VAL_PB_NEW = Column(Numeric(20, 4), comment='市净率(PB)')
    S_VAL_PE_TTM = Column(Numeric(20, 4), comment='市盈率(PE,TTM)')
    S_VAL_PCF_OCF = Column(Numeric(20, 4), comment='市现率(PCF,经营现金流)')
    S_VAL_PCF_OCFTTM = Column(Numeric(20, 4), comment='市现率(PCF,经营现金流TTM)')
    S_VAL_PCF_NCF = Column(Numeric(20, 4), comment='市现率(PCF,现金净流量)')
    S_VAL_PCF_NCFTTM = Column(Numeric(20, 4), comment='市现率(PCF,现金净流量TTM)')
    S_VAL_PS = Column(Numeric(20, 4), comment='市销率(PS)')
    S_VAL_PS_TTM = Column(Numeric(20, 4), comment='市销率(PS,TTM)')
    S_DQ_TURN = Column(Numeric(20, 4), comment='换手率')
    S_DQ_FREETURNOVER = Column(Numeric(20, 4), comment='换手率(基准.自由流通股本)')
    TOT_SHR_TODAY = Column(Numeric(20, 4), comment='当日总股本')
    FLOAT_A_SHR_TODAY = Column(Numeric(20, 4), comment='当日流通股本')
    S_DQ_CLOSE_TODAY = Column(Numeric(20, 4), comment='当日收盘价')
    S_PRICE_DIV_DPS = Column(Numeric(20, 4), comment='股价/每股派息')
    S_PQ_ADJHIGH_52W = Column(Numeric(20, 4), comment='52周最高价(复权)')
    S_PQ_ADJLOW_52W = Column(Numeric(20, 4), comment='52周最低价(复权)')
    FREE_SHARES_TODAY = Column(Numeric(20, 4), comment='当日自由流通股本')
    NET_PROFIT_PARENT_COMP_TTM = Column(Numeric(20, 4), comment='归属母公司净利润(TTM)')
    NET_PROFIT_PARENT_COMP_LYR = Column(Numeric(20, 4), comment='归属母公司净利润(LYR)')
    NET_ASSETS_TODAY = Column(Numeric(20, 4), comment='当日净资产')
    NET_CASH_FLOWS_OPER_ACT_TTM = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额(TTM)')
    NET_CASH_FLOWS_OPER_ACT_LYR = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额(LYR)')
    OPER_REV_TTM = Column(Numeric(20, 4), comment='营业收入(TTM)')
    OPER_REV_LYR = Column(Numeric(20, 4), comment='营业收入(LYR)')
    NET_INCR_CASH_CASH_EQU_TTM = Column(Numeric(20, 4), comment='现金及现金等价物净增加额(TTM)')
    NET_INCR_CASH_CASH_EQU_LYR = Column(Numeric(20, 4), comment='现金及现金等价物净增加额(LYR)')
    UP_DOWN_LIMIT_STATUS = Column(Numeric(2, 0), comment='涨跌停状态')
    LOWEST_HIGHEST_STATUS = Column(Numeric(2, 0), comment='最高最低价状态')


class ASHAREEODPRICES(Base):
    """中国A股日行情"""
    __tablename__ = 'ASHAREEODPRICES'
    __table_args__ = (
        Index('INDEX_TRADE_DT', 'TRADE_DT'),
        Index('finshow', 'S_INFO_WINDCODE', 'TRADE_DT'),)
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
    S_DQ_LIMIT = Column(Numeric(20, 4), comment='涨停价(元)')
    S_DQ_STOPPING = Column(Numeric(20, 4), comment='跌停价(元)')


class ASHAREEQUFROINFO(Base):
    """中国A股股权冻结信息"""
    __tablename__ = 'ASHAREEQUFROINFO'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_FRO_BGDATE = Column(VARCHAR(8), comment='冻结起始时间')
    S_FRO_ENDDATE = Column(VARCHAR(8), comment='冻结结束时间')
    S_HOLDER_NAME = Column(VARCHAR(100), comment='股东名称')
    S_FRO_SHARES = Column(Numeric(20, 4), comment='冻结数量(万股)')
    FROZEN_INSTITUTION = Column(VARCHAR(100), comment='执行冻结机构')
    DISFROZEN_TIME = Column(VARCHAR(8), comment='解冻日期')
    S_HOLDER_TYPE_CODE = Column(Numeric(9, 0), comment='股东类型代码')
    S_HOLDER_ID = Column(VARCHAR(10), comment='股东ID')
    SHR_CATEGORY_CODE = Column(Numeric(9, 0), comment='股份性质类别代码')
    IS_TURN_FROZEN = Column(Numeric(1, 0), comment='是否轮候冻结')
    IS_DISFROZEN = Column(Numeric(1, 0), comment='是否解冻')
    S_TOTAL_HOLDING_SHR = Column(Numeric(20, 4), comment='持股总数（万股）')
    S_FRO_SHR_RATIO = Column(Numeric(20, 4), comment='本次冻结股数占公司总股本比例')
    S_TOTAL_HOLDING_SHR_RATIO = Column(Numeric(20, 4), comment='持股总数占公司总股本比例')


class ASHAREEQUITYDIVISION(Base):
    """中国A股股权分置方案"""
    __tablename__ = 'ASHAREEQUITYDIVISION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司id')
    WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ANN_APPDT = Column(VARCHAR(8), comment='获准公告日期')
    PRO_SCHE = Column(VARCHAR(8), comment='方案进度')
    NTSHAREHOLDERS_PROP = Column(Numeric(20, 4), comment='非流通股东持股比例(%)')
    SPONSOR = Column(VARCHAR(200), comment='保荐机构')
    SUMMARY_ED = Column(VARCHAR(800), comment='股权分置改革对价方案摘要')
    PREPLANDATE = Column(VARCHAR(8), comment='董事会预案公告日')
    RECORDDATE = Column(VARCHAR(8), comment='股东大会股权登记日')
    VOTING_STARTDATE = Column(VARCHAR(8), comment='董事征集投票权起始日')
    VOTING_ENDDATE = Column(VARCHAR(8), comment='董事征集投票权截止日')
    MEETREG_STARTDATE = Column(VARCHAR(8), comment='现场股东大会登记起始日')
    MEETREG_ENDDATE = Column(VARCHAR(8), comment='现场股东大会登记截止日')
    NETVOTING_STARTDATE = Column(VARCHAR(8), comment='网络投票起始日')
    NETVOTING_ENDDATE = Column(VARCHAR(8), comment='网络投票截止日')
    MEETING_STARTDATE = Column(VARCHAR(8), comment='股东大会召开日')
    MEETING_ENDDATE = Column(VARCHAR(8), comment='股东大会公告日')
    SHARENO_TEN = Column(Numeric(24, 8), comment='每10股支付股数(对价)')
    CASHNO_TEN = Column(Numeric(24, 8), comment='每10股支付现金数(对价)')
    ACT_SHARES_TEN = Column(Numeric(24, 8), comment='流通股东每10股实际获得股数')
    ACT_CASH_TEN = Column(Numeric(24, 8), comment='流通股东每10股实际获得现金数')
    TRANS_TEN = Column(Numeric(24, 8), comment='上市公司每10股送转股数')
    ED_ANNDT = Column(VARCHAR(8), comment='股权分置实施股权公告日')
    ED_REGDT = Column(VARCHAR(8), comment='股权分置实施股权登记日')
    PAY_LISTEDDATE = Column(VARCHAR(8), comment='对价支付股票上市日')
    PAY_CASH_DATE = Column(VARCHAR(8), comment='对价支付现金支付日')
    SASAC_APPDATE = Column(VARCHAR(8), comment='国资委批准日期')
    COMDEP_APPDATE = Column(VARCHAR(8), comment='商务部批准日期')
    IS_ED_EX = Column(Numeric(5, 0), comment='股权分置实施是否除权')
    NTS_LOCKCOM = Column(VARCHAR(3000), comment='非流通股持股锁定承诺')
    ED_PROCODE = Column(VARCHAR(200), comment='股权分置方案类型代码')
    IS_NEWPRO = Column(Numeric(5, 0), comment='是否最新方案')
    SUMMARY_CS = Column(VARCHAR(400), comment='对价方案摘要')
    DESCRIPTION_CH_CS = Column(VARCHAR(1000), comment='对价方案变动说明')
    PLAN_RESDATE = Column(VARCHAR(8), comment='预案阶段复牌日')
    PUT_RESDATE = Column(VARCHAR(8), comment='实施复牌日')
    VOTE_RES_DATE = Column(VARCHAR(8), comment='表决到实施阶段复牌日')
    NTSHOLDERS_SHRINK = Column(Numeric(20, 4), comment='非流通股东每10股缩股')
    TSHOLDERS_SUB_WAR = Column(Numeric(20, 4), comment='流通股东每10股获得认购权证数')
    WARRANT_PRODES = Column(VARCHAR(2000), comment='权证方案说明')
    HOLDINGS_COM = Column(VARCHAR(2000), comment='增持承诺')
    FUT_DIV_COM = Column(VARCHAR(400), comment='未来分红承诺')
    ADD_COM = Column(VARCHAR(1200), comment='追加对价承诺')
    EQINC_PLAN = Column(VARCHAR(800), comment='股权激励方案')
    DIVIDEND_TEN = Column(Numeric(20, 4), comment='上市公司每10股派息')
    IS_BASED_TRACAP = Column(Numeric(5, 0), comment='对价是否基于送转后股本')
    SEND_RATE = Column(Numeric(20, 4), comment='送出率(%)')
    TSHOLDERS_PUT_WAR = Column(Numeric(20, 4), comment='流通股东每10股获得认沽权证数')
    COMTYPE = Column(VARCHAR(80), comment='承诺类型')
    VOTESUS_STARTDATE = Column(VARCHAR(8), comment='股改投票停牌起始日期')
    INJ_ASSET_COM = Column(VARCHAR(1000), comment='注入资产承诺')


class ASHAREEQUITYPLEDGEINFO(Base):
    """中国A股股权质押信息"""
    __tablename__ = 'ASHAREEQUITYPLEDGEINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_PLEDGE_BGDATE = Column(VARCHAR(8), comment='质押起始时间')
    S_PLEDGE_ENDDATE = Column(VARCHAR(8), comment='质押结束时间')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
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


class ASHAREEQUITYRELATIONSHIPS(Base):
    """中国A股股权关系"""
    __tablename__ = 'ASHAREEQUITYRELATIONSHIPS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
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
    IS_CONTROLLING_SHAREHOLDERS = Column(Numeric(1, 0), comment='股东是否为公布控股股东')


class ASHAREEQUITYTRANSFER(Base):
    """中国A股股权转让(恒指专用)"""
    __tablename__ = 'ASHAREEQUITYTRANSFER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(200), comment='信息披露方万得代码')
    TRANSFEROR = Column(VARCHAR(100), comment='转让方名称')
    TRANSFEROR_DISCLOSURE = Column(VARCHAR(40), comment='转让方与披露方关系')
    TRANSFEREE = Column(VARCHAR(100), comment='受让方名称')
    TRANSFEREE_DISCLOSURE = Column(VARCHAR(40), comment='受让方与披露方关系')
    TARGETCOMPANY = Column(VARCHAR(100), comment='标的公司')
    TARGETCOMPANY_DISCLOSURE = Column(VARCHAR(40), comment='标的方与披露方关系')
    PROGRESS = Column(VARCHAR(10), comment='方案进度')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    TRANSFERMETHOD = Column(VARCHAR(40), comment='转让方式')
    SHARECATEGORYBEFTRANSFER = Column(VARCHAR(40), comment='转让前股份性质')
    SHARECATEGORYAFTTRANSFER = Column(VARCHAR(40), comment='转让后股份性质')
    TRANSFERREDSHARES = Column(Numeric(20, 4), comment='转让数量(万股)')
    TRANSFERPROPORATION = Column(Numeric(20, 4), comment='本次转让比例(%)')
    TRANSFEEFISHAREHOLDING = Column(Numeric(20, 4), comment='受让方最终持股比例(%)')
    TRANSFERPRICEPERSHARE = Column(Numeric(20, 4), comment='每股转让价格(元)')
    TRADINGAMOUNT = Column(Numeric(20, 4), comment='交易金额(万元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    IS_TRANSFERRED = Column(Numeric(5, 0), comment='是否过户')
    IS_RELDPARTRANSACTIONS = Column(Numeric(1, 0), comment='是否关联交易')
    FIRST_DT = Column(VARCHAR(8), comment='首次公告日期')
    SASACDATE = Column(VARCHAR(8), comment='国资委批准公告日期')
    APPROVEDDATE = Column(VARCHAR(8), comment='证监会批准公告日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    SUMMARY = Column(VARCHAR(4000), comment='交易简介')
    TRADE_RESULT = Column(VARCHAR(2000), comment='交易结果')
    INFLUENCE = Column(VARCHAR, comment='交易影响')
    HIS_CHANGE = Column(VARCHAR(1000), comment='交易历史变动情况')


class ASHAREESOPDESCRIPTION(Base):
    """中国A股公司员工持股计划基本资料"""
    __tablename__ = 'ASHAREESOPDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BM_PREPRO_ANN_DT = Column(VARCHAR(8), comment='董事会预案公告日')
    SHOLDER_MEETING_ANN_DT = Column(VARCHAR(8), comment='股东大会公告日')
    INITIAL_CAPITAL = Column(Numeric(20, 4), comment='初始资金规模（万元）')
    CAPITAL_RESOURCE_CODE = Column(Numeric(9, 0), comment='资金来源代码')
    ESTIMATED_VOLUMN = Column(Numeric(20, 4), comment='预计股票数量(万)')
    RATIO_TO_TOTALSHARES = Column(Numeric(20, 4), comment='预计占公司总股本比例(%)')
    SHOLDERS_NO = Column(Numeric(20, 0), comment='持有人数')
    SHOLDERS_PROPORTION = Column(Numeric(20, 4), comment='持有人占公司员工比例')
    DURATION = Column(Numeric(20, 0), comment='存续期(月)')
    LOCKUP_PERIOD_M = Column(Numeric(20, 0), comment='锁定期限')
    EMPL_SUBS_AMT = Column(Numeric(20, 4), comment='员工认购金额(万)')
    EMPL_SUBS_PROPORTION = Column(Numeric(20, 4), comment='员工认购比例(%)')
    SENMNGR_SUBS_NO = Column(Numeric(20, 0), comment='高管认购人数')
    SENMNGR_SUBS_AMT = Column(Numeric(20, 4), comment='高管认购金额(万元)')
    SENMNGR_SUBS_PROPORTION = Column(Numeric(20, 4), comment='高管认购比例（%）')
    ESTIMATED_PRICE = Column(Numeric(20, 4), comment='标的股票预估价格')
    SHARES_RESOURCE_CODE = Column(Numeric(9, 0), comment='股票来源代码')
    IS_SELF_MANAGE = Column(Numeric(1, 0), comment='是否自行管理')
    CORR_PRONAME = Column(VARCHAR(100), comment='持股计划对应产品名称')
    RATIO_OWNFUNDS = Column(Numeric(20, 4), comment='员工自有资金占比')
    INITIAL_LEVERAGE = Column(Numeric(20, 4), comment='初始杠杆')
    SHOLDERS_LOAN = Column(Numeric(20, 4), comment='股东借款金额')
    SHOLDERS_LOANRATIO = Column(Numeric(20, 4), comment='股东借款比例')
    ACT_FUNDSIZE = Column(Numeric(20, 4), comment='实际资金规模')
    ACT_SHARESNO = Column(Numeric(20, 4), comment='实际股票数量')
    ACT_SHARESPRICE = Column(Numeric(20, 4), comment='实际股票价格')
    ACT_CAP_RATIO = Column(Numeric(20, 4), comment='实际占公司总股本比例')
    SHAREHOLD_FINDT = Column(VARCHAR(8), comment='持股完成日')
    EVENT_ID = Column(VARCHAR(40), comment='事件ID')
    PROGRESS_CODE = Column(Numeric(9, 0), comment='方案进度代码')
    LOCK_START_DATE = Column(VARCHAR(8), comment='锁定起始日')
    ANN_DATE_NEW = Column(VARCHAR(8), comment='最新公告日')
    ANN_DATE_IMPLEMENTATION = Column(VARCHAR(8), comment='实施公告日')


class ASHAREESOPTRADINGINFO(Base):
    """中国A股公司员工持股计划股票买卖情况"""
    __tablename__ = 'ASHAREESOPTRADINGINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ESOP_WINDCODE = Column(VARCHAR(40), comment='员工持股计划证券ID')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    TRADE_AVG_PRICE = Column(Numeric(20, 4), comment='成交均价')
    TRADING_VOLUME = Column(Numeric(20, 4), comment='成交数量')
    RATIO_TO_TOTALSHARES = Column(Numeric(20, 4), comment='占公司总股本比例')
    LOCKUP_PERIOD = Column(Numeric(20, 0), comment='锁定期限')
    EVENT_ID = Column(VARCHAR(40), comment='事件ID')


class ASHAREEVENTDATEINFORMATION(Base):
    """中国A股事件日期信息"""
    __tablename__ = 'ASHAREEVENTDATEINFORMATION'
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


class ASHAREEXRIGHTDIVIDENDRECORD(Base):
    """中国A股除权除息记录"""
    __tablename__ = 'ASHAREEXRIGHTDIVIDENDRECORD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EX_DATE = Column(VARCHAR(8), comment='除权除息日')
    EX_TYPE = Column(VARCHAR(40), comment='除权类型')
    EX_DESCRIPTION = Column(VARCHAR(100), comment='除权说明')
    CASH_DIVIDEND_RATIO = Column(Numeric(15, 4), comment='派息比例')
    BONUS_SHARE_RATIO = Column(Numeric(15, 4), comment='送股比例')
    RIGHTSISSUE_RATIO = Column(Numeric(15, 4), comment='配股比例')
    RIGHTSISSUE_PRICE = Column(Numeric(15, 4), comment='配股价格')
    CONVERSED_RATIO = Column(Numeric(15, 4), comment='转增比例')
    SEO_PRICE = Column(Numeric(15, 4), comment='增发价格')
    SEO_RATIO = Column(Numeric(15, 4), comment='增发比例')
    CONSOLIDATE_SPLIT_RATIO = Column(Numeric(20, 6), comment='缩减比例')


class ASHAREFAIRVALUECHANGE(Base):
    """中国A股财务附注--公允价值变动收益"""
    __tablename__ = 'ASHAREFAIRVALUECHANGE'
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


class ASHAREFINANCIALACCOUNTS(Base):
    """None"""
    __tablename__ = 'ASHAREFINANCIALACCOUNTS'
    __table_args__ = (
        Index('IDX_ASHAREFINANCIALACCOUNTS_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    SUBJECT_CHINESE_NAME = Column(VARCHAR(100), comment='科目中文名')
    CLASSIFICATION_NUMBER = Column(VARCHAR(10), comment='分类序号')
    S_INFO_DATATYPE = Column(VARCHAR(40), comment='数据类型')
    ANN_ITEM = Column(VARCHAR(100), comment='项目公布名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='项目金额')
    ITEM_NAME = Column(VARCHAR(100), comment='项目容错名称')


class ASHAREFINANCIALDERIVATIVE(Base):
    """中国A股财务衍生指标表"""
    __tablename__ = 'ASHAREFINANCIALDERIVATIVE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    INTERVAL_LENGTH = Column(Numeric(20, 4), comment='区间长度(月)')
    FISCALYEAR = Column(VARCHAR(8), comment='会计年度(Wind判定)')
    REPORT_TYPE = Column(VARCHAR(20), comment='报告类型')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    TOT_SHR = Column(Numeric(20, 4), comment='期末总股本(股)')
    OPPROFIT1 = Column(Numeric(20, 4), comment='营业利润(含价值变动损益)(元)')
    OPERATEINCOME = Column(Numeric(20, 4), comment='经营活动净收益(元)')
    INVESTINCOME = Column(Numeric(20, 4), comment='价值变动净收益(元)')
    S_STM_IS = Column(Numeric(20, 4), comment='折旧与摊销(元)')
    EBIT = Column(Numeric(20, 4), comment='息税前利润(元)')
    EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润(元)')
    FCFF = Column(Numeric(20, 4), comment='企业自由现金流量(FCFF)(元)')
    FCFE = Column(Numeric(20, 4), comment='股权自由现金流量(FCFE)(元)')
    EXINTERESTDEBT_CURRENT = Column(Numeric(20, 4), comment='无息流动负债(元)')
    EXINTERESTDEBT_NONCURRENT = Column(Numeric(20, 4), comment='无息非流动负债(元)')
    INTERESTDEBT = Column(Numeric(20, 4), comment='带息债务(元)')
    NETDEBT = Column(Numeric(20, 4), comment='净债务(元)')
    TANGIBLEASSET = Column(Numeric(20, 4), comment='有形资产(元)')
    WORKINGCAPITAL = Column(Numeric(20, 4), comment='营运资金(元)')
    NETWORKINGCAPITAL = Column(Numeric(20, 4), comment='营运流动资本(元)')
    INVESTCAPITAL = Column(Numeric(20, 4), comment='全部投入资本(元)')
    RETAINEDEARNINGS = Column(Numeric(20, 4), comment='留存收益(元)')
    EPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益(元)')
    EPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益(元)')
    EPS_DILUTED2 = Column(Numeric(20, 4), comment='每股收益(期末摊薄)(元)')
    EPS_DILUTED3 = Column(Numeric(20, 4), comment='每股收益(扣除／期末股本摊薄)(元)')
    BPS = Column(Numeric(20, 4), comment='每股净资产(元)')
    OCFPS = Column(Numeric(20, 4), comment='每股经营活动产生的现金流量净额(元)')
    GRPS = Column(Numeric(20, 4), comment='每股营业总收入(元)')
    ORPS = Column(Numeric(20, 4), comment='每股营业收入(元)')
    SURPLUSCAPITALPS = Column(Numeric(20, 4), comment='每股资本公积(元)')
    RETAINEDPS = Column(Numeric(20, 4), comment='每股留存收益(元)')
    CFPS = Column(Numeric(20, 4), comment='每股现金流量净额(元)')
    EBITPS = Column(Numeric(20, 4), comment='每股息税前利润(元)')
    FCFFPS = Column(Numeric(20, 4), comment='每股企业自由现金流量(元)')
    FCFEPS = Column(Numeric(20, 4), comment='每股股东自由现金流量(元)')
    NETPROFITMARGIN = Column(Numeric(20, 4), comment='销售净利率(%)')
    GROSSPROFITMARGIN = Column(Numeric(20, 4), comment='销售毛利率(%)')
    COGSTOSALES = Column(Numeric(20, 4), comment='销售成本率(%)')
    PROFITTOGR = Column(Numeric(20, 4), comment='净利润／营业总收入(%)')
    SALEEXPENSETOGR = Column(Numeric(20, 4), comment='销售费用／营业总收入(%)')
    ADMINEXPENSETOGR = Column(Numeric(20, 4), comment='行政(管理)费用／营业总收入(%)')
    FINAEXPENSETOGR = Column(Numeric(20, 4), comment='财务费用／营业总收入(%)')
    GCTOGR = Column(Numeric(20, 4), comment='营业总成本／营业总收入(%)')
    OPTOGR = Column(Numeric(20, 4), comment='营业利润(含价值变动损益)／营业总收入(%)')
    EBITTOGR = Column(Numeric(20, 4), comment='息税前利润／营业总收入(%)')
    ROE = Column(Numeric(20, 4), comment='净资产收益率(平均)(%)')
    ROE_DEDUCTED = Column(Numeric(20, 4), comment='净资产收益率(扣除平均)(%)')
    ROA2 = Column(Numeric(20, 4), comment='总资产报酬率(平均)(%)')
    ROA = Column(Numeric(20, 4), comment='总资产净利润(平均)(%)')
    ROIC = Column(Numeric(20, 4), comment='投入资本回报率(平均)(%)')
    ROE_YEARLY = Column(Numeric(20, 4), comment='年化净资产收益率(%)')
    ROA2_YEARLY = Column(Numeric(20, 4), comment='年化总资产报酬率(%)')
    ROA_YEARLY = Column(Numeric(20, 4), comment='年化总资产净利率(%)')
    ROIC_YEARLY = Column(Numeric(20, 4), comment='年化投入资本回报率')
    OPERATEINCOMETOEBT = Column(Numeric(20, 4), comment='经营活动净收益／除税前利润(%)')
    INVESTINCOMETOEBT = Column(Numeric(20, 4), comment='价值变动净收益／除税前利润(%)')
    NONOPERATEPROFITTOEBT = Column(Numeric(20, 4), comment='营业外收支净额／除税前利润(%)')
    TAXTOEBT = Column(Numeric(20, 4), comment='所得税／利润总额(%)')
    CONTINUED_NET_PROFIT = Column(Numeric(20, 4), comment='持续经营净利润／除税后利润(%)')
    NONNETOPTOTAXPROFIT = Column(Numeric(20, 4), comment='非持续经营净利润/除税后利润(%)')
    OCFTOOR = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／营业收入(%)')
    OCFTOOR1 = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／经营活动净收益')
    CAPITALIZEDTODA = Column(Numeric(20, 4), comment='资本支出／折旧和摊销')
    DEBTTOASSETS = Column(Numeric(20, 4), comment='资产负债率(%)')
    ASSETSTOEQUITY = Column(Numeric(20, 4), comment='权益乘数')
    DUPONT_ASSETSTOEQUITY = Column(Numeric(20, 4), comment='权益乘数(用于杜邦分析)')
    CATOASSETS = Column(Numeric(20, 4), comment='流动资产／总资产(%)')
    NCATOASSETS = Column(Numeric(20, 4), comment='非流动资产／总资产(%)')
    TANGIBLEASSETSTOASSETS = Column(Numeric(20, 4), comment='有形资产／总资产(%)')
    INTDEBTTOTOTALCAP = Column(Numeric(20, 4), comment='带息债务／全部投入资本(%)')
    EQUITYTOTOTALCAPITAL = Column(Numeric(20, 4), comment='归属于母公司的股东权益／全部投入资本(%)')
    CURRENTDEBTTODEBT = Column(Numeric(20, 4), comment='流动负债／负债合计(%)')
    LONGDEBTODEBT = Column(Numeric(20, 4), comment='非流动负债／负债合计(%)')
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
    TURNDAYS = Column(Numeric(20, 4), comment='营业周期(天)')
    INVTURNDAYS = Column(Numeric(20, 4), comment='存货周转天数(天)')
    ARTURNDAYS = Column(Numeric(20, 4), comment='应收账款周转天数(天)')
    INVTURN = Column(Numeric(20, 4), comment='存货周转率(次)')
    ARTURN = Column(Numeric(20, 4), comment='应收账款周转率(次)')
    CATURN = Column(Numeric(20, 4), comment='流动资产周转率(次)')
    FATURN = Column(Numeric(20, 4), comment='固定资产周转率(次)')
    ASSETSTURN = Column(Numeric(20, 4), comment='总资产周转率(次)')
    OCFTOPROFIT = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／营业利润(含)(%)')
    CASHTOLIQDEBT = Column(Numeric(20, 4), comment='货币资金／流动负债')
    CASHTOLIQDEBTWITHINTEREST = Column(Numeric(20, 4), comment='货币资金／带息流动负债')
    OPTOLIQDEBT = Column(Numeric(20, 4), comment='营业利润／流动负债')
    OPTODEBT = Column(Numeric(20, 4), comment='营业利润／负债合计')
    PROFITTOOP = Column(Numeric(20, 4), comment='利润总额／营业总收入(%)')
    NET_PROFIT5 = Column(Numeric(20, 4), comment='归属母公司的净利润／净利润(%)')
    NET_TOTAL_PROFIT = Column(Numeric(20, 4), comment='净利润／利润总额(%)')
    TOTAL_PROFIT_EBIT = Column(Numeric(20, 4), comment='利润总额／EBIT(%)')
    YOYEPS_BASIC = Column(Numeric(20, 4), comment='基本每股收益同比增长率(%)')
    YOYEPS_DILUTED = Column(Numeric(20, 4), comment='稀释每股收益同比增长率(%)')
    YOYOCFPS = Column(Numeric(20, 4), comment='每股经营活动产生的现金流量净额同比增长率(%)')
    YOY_TR = Column(Numeric(20, 4), comment='营业总收入同比增长率(%)')
    YOY_OR = Column(Numeric(20, 4), comment='营业收入同比增长率(%)')
    YOYOP = Column(Numeric(20, 4), comment='营业利润同比增长率(含)(%)')
    YOYEBT = Column(Numeric(20, 4), comment='利润总额同比增长率(%)')
    YOYNETPROFIT = Column(Numeric(20, 4), comment='归属母公司股东的净利润同比增长率(%)')
    YOYNETPROFIT_DEDUCTED = Column(Numeric(20, 4), comment='归属母公司股东的净利润-扣除非经常损益同比增长率(%)')
    YOYOCF = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额同比增长率(%)')
    YOYROE = Column(Numeric(20, 4), comment='净资产收益率(平均)?同比增长率(%)')
    YOYBPS = Column(Numeric(20, 4), comment='每股净资产同比增长率(%)')
    YOYASSETS = Column(Numeric(20, 4), comment='资产总计同比增长率(%)')
    YOYEQUITY = Column(Numeric(20, 4), comment='归属母公司的股东权益同比增长率(%)')


class ASHAREFINANCIALEXP(Base):
    """中国A股财务附注--财务费用"""
    __tablename__ = 'ASHAREFINANCIALEXP'
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


class ASHAREFINANCIALEXPENSE(Base):
    """中国A股财务费用明细"""
    __tablename__ = 'ASHAREFINANCIALEXPENSE'
    __table_args__ = (
        Index('IDX_ASHAREFINANCIALEXPENSE_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPECODE = Column(Numeric(9, 0), comment='报表类型代码')
    S_STMNOTE_INTEXP = Column(Numeric(20, 4), comment='利息支出(元)')
    S_STMNOTE_INTINC = Column(Numeric(20, 4), comment='减：利息收入(元)')
    S_STMNOTE_EXCH = Column(Numeric(20, 4), comment='汇兑损益(元)')
    S_STMNOTE_FEE = Column(Numeric(20, 4), comment='手续费(元)')
    S_STMNOTE_OTHERS = Column(Numeric(20, 4), comment='其他(元)')
    S_STMNOTE_FINEXP = Column(Numeric(20, 4), comment='合计(元)')
    S_STMNOTE_FINEXP_1 = Column(Numeric(20, 4), comment='减：利息资本化金额(元)')


class ASHAREFINANCIALINDICATOR(Base):
    """中国A股财务指标"""
    __tablename__ = 'ASHAREFINANCIALINDICATOR'
    __table_args__ = (
        Index('IDX_ASHAREFINANCIALINDICATOR_ANN_DT', 'ANN_DT'),
        Index('INDEX_REPORT_PERIOD', 'REPORT_PERIOD'),
        Index('fass', 'S_INFO_WINDCODE', 'REPORT_PERIOD', 'S_FA_EXTRAORDINARY', 'S_FA_DEDUCTEDPROFIT',
              'S_FA_GROSSMARGIN', 'S_FA_OPERATEINCOME', 'S_FA_INVESTINCOME', 'S_STMNOTE_FINEXP', 'S_STM_IS',
              'S_FA_EBIT', 'S_FA_EBITDA', 'S_FA_FCFF', 'S_FA_FCFE', 'S_FA_EXINTERESTDEBT_CURRENT',
              'S_FA_EXINTERESTDEBT_NONCURRENT', 'S_FA_INTERESTDEBT', 'S_FA_NETDEBT', 'S_FA_TANGIBLEASSET',
              'S_FA_WORKINGCAPITAL', 'S_FA_NETWORKINGCAPITAL', 'S_FA_INVESTCAPITAL', 'S_FA_RETAINEDEARNINGS',
              'S_FA_EPS_BASIC', 'S_FA_EPS_DILUTED', 'S_FA_EPS_DILUTED2', 'S_FA_BPS', 'S_FA_OCFPS', 'S_FA_GRPS',
              'S_FA_ORPS', 'S_FA_SURPLUSCAPITALPS', 'S_FA_SURPLUSRESERVEPS', 'S_FA_UNDISTRIBUTEDPS', 'S_FA_RETAINEDPS',
              'S_FA_CFPS', 'S_FA_EBITPS', 'S_FA_FCFFPS', 'S_FA_FCFEPS', 'S_FA_NETPROFITMARGIN',
              'S_FA_GROSSPROFITMARGIN', 'S_FA_COGSTOSALES', 'S_FA_EXPENSETOSALES', 'S_FA_PROFITTOGR',
              'S_FA_SALEEXPENSETOGR', 'S_FA_ADMINEXPENSETOGR', 'S_FA_FINAEXPENSETOGR', 'S_FA_IMPAIRTOGR_TTM',
              'S_FA_GCTOGR', 'S_FA_OPTOGR', 'S_FA_EBITTOGR', 'S_FA_ROE', 'S_FA_ROE_DEDUCTED', 'S_FA_ROA2', 'S_FA_ROA',
              'S_FA_ROIC', 'S_FA_ROE_YEARLY', 'S_FA_ROA2_YEARLY', 'S_FA_ROE_AVG', 'S_FA_OPERATEINCOMETOEBT',
              'S_FA_INVESTINCOMETOEBT', 'S_FA_NONOPERATEPROFITTOEBT', 'S_FA_TAXTOEBT', 'S_FA_DEDUCTEDPROFITTOPROFIT',
              'S_FA_SALESCASHINTOOR', 'S_FA_OCFTOOR', 'S_FA_OCFTOOPERATEINCOME', 'S_FA_CAPITALIZEDTODA',
              'S_FA_DEBTTOASSETS', 'S_FA_ASSETSTOEQUITY', 'S_FA_DUPONT_ASSETSTOEQUITY', 'S_FA_CATOASSETS',
              'S_FA_NCATOASSETS', 'S_FA_TANGIBLEASSETSTOASSETS', 'S_FA_INTDEBTTOTOTALCAP', 'S_FA_EQUITYTOTOTALCAPITAL',
              'S_FA_CURRENTDEBTTODEBT', 'S_FA_LONGDEBTODEBT', 'S_FA_CURRENT', 'S_FA_QUICK', 'S_FA_CASHRATIO',
              'S_FA_OCFTOSHORTDEBT', 'S_FA_DEBTTOEQUITY', 'S_FA_EQUITYTODEBT', 'S_FA_EQUITYTOINTERESTDEBT',
              'S_FA_TANGIBLEASSETTODEBT', 'S_FA_TANGASSETTOINTDEBT', 'S_FA_TANGIBLEASSETTONETDEBT', 'S_FA_OCFTODEBT',
              'S_FA_OCFTOINTERESTDEBT', 'S_FA_OCFTONETDEBT', 'S_FA_EBITTOINTEREST', 'S_FA_LONGDEBTTOWORKINGCAPITAL',
              'S_FA_EBITDATODEBT', 'S_FA_TURNDAYS', 'S_FA_INVTURNDAYS', 'S_FA_ARTURNDAYS', 'S_FA_INVTURN',
              'S_FA_ARTURN', 'S_FA_CATURN', 'S_FA_FATURN', 'S_FA_ASSETSTURN', 'S_FA_ROA_YEARLY', 'S_FA_DUPONT_ROA',
              'S_STM_BS', 'S_FA_PREFINEXPENSE_OPPROFIT', 'S_FA_NONOPPROFIT', 'S_FA_OPTOEBT', 'S_FA_NOPTOEBT',
              'S_FA_OCFTOPROFIT', 'S_FA_CASHTOLIQDEBT', 'S_FA_CASHTOLIQDEBTWITHINTEREST', 'S_FA_OPTOLIQDEBT',
              'S_FA_OPTODEBT', 'S_FA_ROIC_YEARLY', 'S_FA_TOT_FATURN', 'S_FA_PROFITTOOP', 'S_QFA_OPERATEINCOME',
              'S_QFA_INVESTINCOME', 'S_QFA_DEDUCTEDPROFIT', 'S_QFA_EPS', 'S_QFA_NETPROFITMARGIN',
              'S_QFA_GROSSPROFITMARGIN', 'S_QFA_EXPENSETOSALES', 'S_QFA_PROFITTOGR', 'S_QFA_SALEEXPENSETOGR',
              'S_QFA_ADMINEXPENSETOGR', 'S_QFA_FINAEXPENSETOGR', 'S_QFA_IMPAIRTOGR_TTM', 'S_QFA_GCTOGR', 'S_QFA_OPTOGR',
              'S_QFA_ROE', 'S_QFA_ROE_DEDUCTED', 'S_QFA_ROA', 'S_QFA_OPERATEINCOMETOEBT', 'S_QFA_INVESTINCOMETOEBT',
              'S_QFA_DEDUCTEDPROFITTOPROFIT', 'S_QFA_SALESCASHINTOOR', 'S_QFA_OCFTOSALES', 'S_QFA_OCFTOOR',
              'S_FA_YOYEPS_BASIC', 'S_FA_YOYEPS_DILUTED', 'S_FA_YOYOCFPS', 'S_FA_YOYOP', 'S_FA_YOYEBT',
              'S_FA_YOYNETPROFIT', 'S_FA_YOYNETPROFIT_DEDUCTED', 'S_FA_YOYOCF', 'S_FA_YOYROE', 'S_FA_YOYBPS',
              'S_FA_YOYASSETS', 'S_FA_YOYEQUITY', 'S_FA_YOY_TR', 'S_FA_YOY_OR', 'S_QFA_YOYGR', 'S_QFA_CGRGR',
              'S_QFA_YOYSALES', 'S_QFA_CGRSALES', 'S_QFA_YOYOP', 'S_QFA_CGROP', 'S_QFA_YOYPROFIT', 'S_QFA_CGRPROFIT',
              'S_QFA_YOYNETPROFIT', 'S_QFA_CGRNETPROFIT', 'S_FA_YOY_EQUITY', 'RD_EXPENSE', 'WAA_ROE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
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
    S_FA_ROA = Column(Numeric(20, 4), comment='总资产净利率')
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
    WAA_ROE = Column(Numeric(20, 4), comment='加权平均净资产收益率')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')


class ASHAREFINANCIALSECURITIES(Base):
    """中国A股财务附注--融出证券合计"""
    __tablename__ = 'ASHAREFINANCIALSECURITIES'
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


class ASHAREFINSEGMENTINFO(Base):
    """中国A股金融机构经营分部业务数据"""
    __tablename__ = 'ASHAREFINSEGMENTINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报表类型代码')
    CLASS_CODE = Column(Numeric(9, 0), comment='分部类别代码')
    SUBJECT_CODE = Column(Numeric(9, 0), comment='科目代码')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='金额')
    UNIT = Column(VARCHAR(40), comment='单位')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    SUBJECT_NAME_ANN = Column(VARCHAR(100), comment='[内部]公布科目名称')


class ASHAREFIXEDASSETS(Base):
    """中国A股财务附注--固定资产"""
    __tablename__ = 'ASHAREFIXEDASSETS'
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


class ASHAREFLOATHOLDER(Base):
    """中国A股流通股东"""
    __tablename__ = 'ASHAREFLOATHOLDER'
    __table_args__ = (
        Index('IDX_ASHAREFLOATHOLDER_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_HOLDER_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_HOLDER_HOLDERCATEGORY = Column(VARCHAR(1), comment='股东类型')
    S_HOLDER_NAME = Column(VARCHAR(300), comment='持有人')
    S_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='数量（股）')
    S_HOLDER_WINDNAME = Column(VARCHAR(200), comment='持有人（容错后）')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')


class ASHAREFREEFLOAT(Base):
    """中国A股自由流通股本"""
    __tablename__ = 'ASHAREFREEFLOAT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期(除权日)')
    S_SHARE_FREESHARES = Column(Numeric(20, 4), comment='自由流通股本(万股)')
    CHANGE_DT1 = Column(VARCHAR(8), comment='变动日期(上市日)')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class ASHAREFREEFLOATCALENDAR(Base):
    """中国A股限售股流通日历"""
    __tablename__ = 'ASHAREFREEFLOATCALENDAR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='限售股上市日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_SHARE_LST = Column(Numeric(20, 4), comment='上市股份数量（万股）')
    S_SHARE_NONLST = Column(Numeric(20, 4), comment='未上市股份数量（万股）')
    S_SHARE_UNRESTRICTED = Column(Numeric(20, 4), comment='无限售条件股份数量（万股）')
    S_SHARE_LSTTYPECODE = Column(Numeric(9, 0), comment='上市股份类型代码')
    S_SHARE_LST_IS_ANN = Column(VARCHAR(1), comment='上市数量是否公布值')


class ASHAREFUNDUSING(Base):
    """中国A股募集资金用途"""
    __tablename__ = 'ASHAREFUNDUSING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(38), comment='公司ID')
    FINANCING_EVENTS_TYPE = Column(VARCHAR(100), comment='融资事件类型')
    MONEY_RAISED_AMOUNT = Column(Numeric(20, 4), comment='货币募集金额')
    NON_CURRENCY_RAISE_AMOUNT = Column(Numeric(20, 4), comment='非货币募集金额')
    ISSUE_COST = Column(Numeric(20, 4), comment='发行费用')
    ACTUAL_FUNDRAISING_AMOUNT = Column(Numeric(20, 4), comment='实际募资金额')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    ITEM_NUMBER = Column(VARCHAR(20), comment='项目序号')
    INVESTMENT_PROJECTS = Column(VARCHAR(100), comment='投资项目')
    PLAN_INVEST = Column(Numeric(20, 4), comment='项目总计划投入资金')
    ISSUER_PLAN_INVEST = Column(Numeric(20, 4), comment='募资主体计划投入资金')
    ISSUER_PLAN_FUNDS_INVESTMENT = Column(Numeric(20, 4), comment='募资主体计划投入募集资金')
    FUNDS_HAS_INVESTED = Column(Numeric(20, 4), comment='已投入募集资金')
    IS_CHANGE = Column(Numeric(1, 0), comment='是否变更')
    NEW_ANN_DATE = Column(VARCHAR(8), comment='最新公告日期')


class ASHAREGICSINDUSTRIESCLASS(Base):
    """中信标普GICS行业分类(废弃)"""
    __tablename__ = 'ASHAREGICSINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    GICS_IND_CODE = Column(VARCHAR(50), comment='GICS行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHAREGOODWILL(Base):
    """中国A股财务附注--商誉"""
    __tablename__ = 'ASHAREGOODWILL'
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


class ASHAREGOODWILLDEVALUE(Base):
    """中国A股财务附注--商誉减值准备"""
    __tablename__ = 'ASHAREGOODWILLDEVALUE'
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


class ASHAREGOVERNMENTGRANTS(Base):
    """中国A股政府补助明细"""
    __tablename__ = 'ASHAREGOVERNMENTGRANTS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ITEM_NAME = Column(VARCHAR(500), comment='项目')
    AMOUNT_CURRENT_ISSUE = Column(Numeric(20, 4), comment='本期发生额')
    AMOUNT_PREVIOUS_PERIOD = Column(Numeric(20, 4), comment='上期发生额')
    MEMO = Column(VARCHAR(2000), comment='说明')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class ASHAREGOVERNMENTSUBSIDYDEFIN(Base):
    """中国A股财务附注--递延收益政府补助"""
    __tablename__ = 'ASHAREGOVERNMENTSUBSIDYDEFIN'
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


class ASHAREGROUP(Base):
    """中国A股财务附注--递延收益政府补助"""
    __tablename__ = 'ASHAREGROUP'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='集团公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='集团公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='集团公司ID')


class ASHAREGROUPINFORMATION(Base):
    """中国A股公司集团信息"""
    __tablename__ = 'ASHAREGROUPINFORMATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='集团公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='集团公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='集团公司ID')


class ASHAREGUARANTEE(Base):
    """中国A股担保事件"""
    __tablename__ = 'ASHAREGUARANTEE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    RELATION = Column(VARCHAR(40), comment='担保方与披露方关系')
    GUARANTOR = Column(VARCHAR(100), comment='担保方公司名称')
    RELATION2 = Column(VARCHAR(40), comment='被担保方与披露方关系')
    SECUREDPARTY = Column(VARCHAR(100), comment='被担保方公司名称')
    METHOD = Column(VARCHAR(40), comment='担保方式')
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


class ASHAREGUARANTEERELATIONSHIP(Base):
    """中国A股担保"""
    __tablename__ = 'ASHAREGUARANTEERELATIONSHIP'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='被担保公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='被担保公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='被担保公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class ASHAREGUARANTEESTATISTICS(Base):
    """中国A股担保统计"""
    __tablename__ = 'ASHAREGUARANTEESTATISTICS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
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


class ASHAREHOLDER(Base):
    """中国A股股东"""
    __tablename__ = 'ASHAREHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='股东公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='股东公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='股东公司ID')
    S_HOLDER_ENDDATE = Column(VARCHAR(10), comment='报告期')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例')


class ASHAREHOLDERNUMBER(Base):
    """中国A股股东户数"""
    __tablename__ = 'ASHAREHOLDERNUMBER'
    __table_args__ = (
        Index('IDX_ASHAREHOLDERNUMBER_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_HOLDER_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_HOLDER_NUM = Column(Numeric(20, 4), comment='A股股东户数')
    S_HOLDER_TOTAL_NUM = Column(Numeric(20, 4), comment='股东总户数')


class ASHAREHOLDERSMEETING(Base):
    """中国A股召开股东大会"""
    __tablename__ = 'ASHAREHOLDERSMEETING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    MEETING_DT = Column(VARCHAR(8), comment='会议日期')
    MEETING_TYPE = Column(VARCHAR(20), comment='会议类型')
    VOTINGCODE = Column(Numeric(9, 0), comment='投票通道代码')
    SMTGRECDATE = Column(VARCHAR(8), comment='股东大会股权登记日')
    SPOTMTGSTARTDATE = Column(VARCHAR(8), comment='会议登记起始日')
    SPOTMTGENDDATE = Column(VARCHAR(8), comment='会议登记截止日')
    IS_INTNET = Column(VARCHAR(1), comment='是否可以网络投票')
    INTNETCODE = Column(VARCHAR(10), comment='网络投票代码')
    INTNETNAME = Column(VARCHAR(20), comment='网络投票简称')
    MEETING_CONTENT = Column(TEXT(2147483647), comment='会议内容')
    CHANGE_HIS = Column(VARCHAR(100), comment='变更历史')
    MEETEVENT_ID = Column(VARCHAR(40), comment='会议事件ID')
    IS_NEW = Column(Numeric(5, 0), comment='最新标志')
    INTNET_STARTDATE = Column(VARCHAR(8), comment='互联网投票起始日')
    INTNET_ENDDATE = Column(VARCHAR(8), comment='互联网投票终止日')


class ASHAREHOLDERSMEETINGVOTES(Base):
    """中国A股股东大会投票情况"""
    __tablename__ = 'ASHAREHOLDERSMEETINGVOTES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    MEETING_DT = Column(VARCHAR(8), comment='会议日期')
    MOTION_TITLE = Column(VARCHAR(200), comment='议案标题')
    IS_CLASSIFIED_VOTE = Column(Numeric(5, 0), comment='是否需要分类表决')
    FAVOR_SHARE = Column(Numeric(20, 4), comment='赞成股数')
    FAVOR_SHARE_RADIO = Column(Numeric(20, 4), comment='赞成股数比重(%)')
    OPPOSE_SHARE = Column(Numeric(20, 4), comment='反对股数')
    OPPOSE_SHARE_RADIO = Column(Numeric(20, 4), comment='反对股数比重(%)')
    ABSTAINED_SHARE = Column(Numeric(20, 4), comment='弃权股数')
    ABSTAINED_SHARE_RADIO = Column(Numeric(20, 4), comment='弃权股数比重(%)')
    NON_TRADABLE_FAVOR_SHARE = Column(Numeric(20, 4), comment='非流通股(限售流通股)赞成股数')
    NON_TRADABLE_OPPOSE_SHARE = Column(Numeric(20, 4), comment='非流通股(限售流通股)反对股数')
    NON_TRADABLE_ABSTAIN_SHARE = Column(Numeric(20, 4), comment='非流通股(限售流通股)弃权股数')
    TRADABLE_FAVOR_SHARE = Column(Numeric(20, 4), comment='流通股赞成股数')
    TRADABLE_FAVOR_SHARE_RADIO = Column(Numeric(20, 4), comment='流通股赞成股数比重(%)')
    TRADABLE_OPPOSE_SHARE = Column(Numeric(20, 4), comment='流通股反对股数')
    TRADABLE_OPPOSE_SHARE_RADIO = Column(Numeric(20, 4), comment='流通股反对股数比重(%)')
    TRADABLE_ABSTAIN_SHARE = Column(Numeric(20, 4), comment='流通股弃权股数')
    TRADABLE_ABSTAIN_SHARE_RADIO = Column(Numeric(20, 4), comment='流通股弃权股数比重(%)')
    IS_PASSED = Column(Numeric(5, 0), comment='是否通过')
    IS_SHAREHOLDER_AVOID = Column(Numeric(5, 0), comment='关联股东是否回避')
    AVOID_SHARE = Column(Numeric(20, 4), comment='回避股数')
    AVOID_SHARE_RADIO = Column(Numeric(20, 4), comment='回避股数比重(%)')
    MOTION_TYPE = Column(VARCHAR(100), comment='议案类型')


class ASHAREHOLDING(Base):
    """中国A股控参股"""
    __tablename__ = 'ASHAREHOLDING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='投资公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='投资公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='投资公司ID')
    S_HOLDER_ENDDATE = Column(VARCHAR(10), comment='报告期')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例')


class ASHAREHOLDINGOPERATE(Base):
    """中国A股控股参股公司经营情况"""
    __tablename__ = 'ASHAREHOLDINGOPERATE'
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


class ASHAREIBROKERINDICATOR(Base):
    """中国A股券商专用指标"""
    __tablename__ = 'ASHAREIBROKERINDICATOR'
    __table_args__ = (
        Index('IDX_ASHAREIBROKERINDICATOR_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
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
    CAPITAL_LEVERAGE_RATIO = Column(Numeric(20, 4), comment='资本杠杆率')
    LIQUIDITY_COVERAGE = Column(Numeric(20, 4), comment='流动性覆盖率')
    NET_STABLE_CAPITAL_RATIO = Column(Numeric(20, 4), comment='净稳定资金率')
    NET_ASSETS_LIABILITIES_RATIO = Column(Numeric(20, 4), comment='净资产/负债')
    CORE_NET_CAPITAL = Column(Numeric(20, 4), comment='核心净资本')
    NET_CAPITAL_ATTACHED = Column(Numeric(20, 4), comment='附属净资本')
    SUM_VENTURE_CAPITAL_RESERVE = Column(Numeric(20, 4), comment='各项风险资本准备之和')
    TOTAL_ASSETS = Column(Numeric(20, 4), comment='表内外资产总额')


class ASHAREILLEGALITY(Base):
    """中国A股违规事件"""
    __tablename__ = 'ASHAREILLEGALITY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ILLEG_TYPE = Column(VARCHAR(100), comment='违规类型')
    SUBJECT_TYPE = Column(Numeric(9, 0), comment='主体类别代码')
    SUBJECT = Column(VARCHAR(100), comment='违规主体')
    RELATION_TYPE = Column(Numeric(9, 0), comment='与上市公司的关系')
    BEHAVIOR = Column(TEXT(2147483647), comment='违规行为')
    DISPOSAL_DT = Column(VARCHAR(8), comment='处罚日期')
    DISPOSAL_TYPE = Column(VARCHAR(100), comment='处分类型')
    METHOD = Column(VARCHAR(2000), comment='处分措施')
    PROCESSOR = Column(VARCHAR(200), comment='处理人')
    AMOUNT = Column(Numeric(20, 4), comment='处罚金额(元)')
    BAN_YEAR = Column(Numeric(20, 4), comment='市场禁入期限(年)')
    REF_RULE = Column(VARCHAR(1000), comment='相关法规')


class ASHAREIMPAIRLOSSASSETS(Base):
    """中国A股财务附注--总资产减值损失"""
    __tablename__ = 'ASHAREIMPAIRLOSSASSETS'
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


class ASHAREINCDESCRIPTION(Base):
    """中国A股股权激励基本资料"""
    __tablename__ = 'ASHAREINCDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INC_SEQUENCE = Column(VARCHAR(6), comment='序号')
    S_INC_SUBJECT = Column(Numeric(9, 0), comment='激励标的')
    S_INC_TYPE = Column(Numeric(9, 0), comment='激励方式')
    S_INC_QUANTITY = Column(Numeric(20, 4), comment='激励总数(万股/万份)')
    S_INC_FIRSTINC = Column(VARCHAR(8), comment='起始日')
    S_INC_ENDINC = Column(VARCHAR(8), comment='到期日')
    S_INC_INITEXECPRI = Column(Numeric(20, 4), comment='期权初始行权价格(股票转让价格)')
    S_INC_EXPIRYDATE = Column(Numeric(20, 4), comment='有效期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INC_PROGRAMDESCRIPT = Column(VARCHAR(3000), comment='方案说明')
    S_INC_INCENTSHARESALEDESCRIPT = Column(VARCHAR(1000), comment='激励股票出售说明')
    S_INC_INCENTCONDITION = Column(VARCHAR(2000), comment='激励授予条件')
    S_INC_OPTEXESPECIALCONDITION = Column(VARCHAR(2000), comment='期权行权特别条件')
    PROGRESS = Column(VARCHAR(10), comment='方案进度')
    PRICE_DESCRIPTION = Column(VARCHAR(80), comment='价格说明')
    INC_NUMBERS_RATE = Column(Numeric(20, 4), comment='激励数量占当前总股本比例(%)')
    PREPLAN_ANN_DATE = Column(VARCHAR(8), comment='预案公告日')
    GM_DATE = Column(VARCHAR(8), comment='股东大会公告日')
    IMPLEMENT_DATE = Column(VARCHAR(8), comment='首次实施公告日')
    INC_FUND_DESCRIPTION = Column(VARCHAR(1000), comment='激励基金说明')
    INTERVAL_MONTHS = Column(Numeric(20, 4), comment='授权日与首次可行权日间隔时间(月)')
    EQINC_PLAN_EVENT_ID = Column(VARCHAR(40), comment='股权激励事件ID')


class ASHAREINCEXECQTYPRI(Base):
    """中国A股股权激励期权行权数量与价格"""
    __tablename__ = 'ASHAREINCEXECQTYPRI'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(100), comment='Wind代码')
    S_INC_SEQUENCE = Column(VARCHAR(10), comment='序号')
    S_INC_NAME = Column(VARCHAR(200), comment='姓名')
    S_INC_EXECQTY = Column(Numeric(20, 4), comment='行权数量(万份)')
    S_INC_EXECPRI = Column(Numeric(20, 4), comment='行权价格')
    S_INC_EXECDATE = Column(VARCHAR(8), comment='行权日期')


class ASHAREINCEXERCISEPCT(Base):
    """中国A股股权激励期权行权比例"""
    __tablename__ = 'ASHAREINCEXERCISEPCT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INC_SEQUENCE = Column(VARCHAR(6), comment='序号')
    S_INC_EXECBATCH = Column(VARCHAR(6), comment='行权期')
    S_INC_EXECPCT = Column(Numeric(20, 4), comment='行权比例(%)')
    S_INC_INTERVALTIME = Column(Numeric(20, 4), comment='首个授权日至行权期间隔时间(月)')


class ASHAREINCEXERCISEPCTZL(Base):
    """中国A股股权激励期权行权比例(增量)"""
    __tablename__ = 'ASHAREINCEXERCISEPCTZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INC_SEQUENCE = Column(VARCHAR(6), comment='序号')
    S_INC_EXECBATCH = Column(VARCHAR(6), comment='行权期')
    S_INC_EXECPCT = Column(Numeric(20, 4), comment='行权比例(%)')
    S_INC_INTERVALTIME = Column(Numeric(20, 4), comment='首个授权日至行权期间隔时间(月)')


class ASHAREINCOME(Base):
    """中国A股利润表"""
    __tablename__ = 'ASHAREINCOME'
    __table_args__ = (
        Index('fass', 'S_INFO_WINDCODE', 'REPORT_PERIOD', 'TOT_OPER_REV', 'OPER_REV', 'INT_INC', 'NET_INT_INC',
              'INSUR_PREM_UNEARNED', 'HANDLING_CHRG_COMM_INC', 'NET_HANDLING_CHRG_COMM_INC', 'NET_INC_OTHER_OPS',
              'PLUS_NET_INC_OTHER_BUS', 'PREM_INC', 'LESS_CEDED_OUT_PREM', 'CHG_UNEARNED_PREM_RES',
              'INCL_REINSURANCE_PREM_INC', 'NET_INC_SEC_TRADING_BROK_BUS', 'NET_INC_SEC_UW_BUS',
              'NET_INC_EC_ASSET_MGMT_BUS', 'OTHER_BUS_INC', 'PLUS_NET_GAIN_CHG_FV', 'PLUS_NET_INVEST_INC',
              'INCL_INC_INVEST_ASSOC_JV_ENTP', 'PLUS_NET_GAIN_FX_TRANS', 'TOT_OPER_COST', 'LESS_OPER_COST',
              'LESS_INT_EXP', 'LESS_HANDLING_CHRG_COMM_EXP', 'LESS_TAXES_SURCHARGES_OPS', 'LESS_SELLING_DIST_EXP',
              'LESS_GERL_ADMIN_EXP', 'LESS_FIN_EXP', 'LESS_IMPAIR_LOSS_ASSETS', 'PREPAY_SURR', 'TOT_CLAIM_EXP',
              'CHG_INSUR_CONT_RSRV', 'DVD_EXP_INSURED', 'REINSURANCE_EXP', 'OPER_EXP', 'LESS_CLAIM_RECB_REINSURER',
              'LESS_INS_RSRV_RECB_REINSURER', 'LESS_EXP_RECB_REINSURER', 'OTHER_BUS_COST', 'OPER_PROFIT',
              'PLUS_NON_OPER_REV', 'LESS_NON_OPER_EXP', 'IL_NET_LOSS_DISP_NONCUR_ASSET', 'TOT_PROFIT', 'INC_TAX',
              'UNCONFIRMED_INVEST_LOSS', 'NET_PROFIT_INCL_MIN_INT_INC', 'NET_PROFIT_EXCL_MIN_INT_INC',
              'MINORITY_INT_INC', 'OTHER_COMPREH_INC', 'TOT_COMPREH_INC', 'TOT_COMPREH_INC_PARENT_COMP',
              'TOT_COMPREH_INC_MIN_SHRHLDR', 'EBIT', 'EBITDA', 'NET_PROFIT_AFTER_DED_NR_LP',
              'NET_PROFIT_UNDER_INTL_ACC_STA', 'S_FA_EPS_BASIC', 'S_FA_EPS_DILUTED', 'INSURANCE_EXPENSE',
              'SPE_BAL_OPER_PROFIT', 'TOT_BAL_OPER_PROFIT', 'SPE_BAL_TOT_PROFIT', 'TOT_BAL_TOT_PROFIT',
              'SPE_BAL_NET_PROFIT', 'TOT_BAL_NET_PROFIT', 'UNDISTRIBUTED_PROFIT', 'ADJLOSSGAIN_PREVYEAR',
              'TRANSFER_FROM_SURPLUSRESERVE', 'TRANSFER_FROM_HOUSINGIMPREST', 'TRANSFER_FROM_OTHERS',
              'DISTRIBUTABLE_PROFIT', 'WITHDR_LEGALSURPLUS', 'WITHDR_LEGALPUBWELFUNDS', 'WORKERS_WELFARE',
              'WITHDR_BUZEXPWELFARE', 'WITHDR_RESERVEFUND', 'DISTRIBUTABLE_PROFIT_SHRHDER', 'PRFSHARE_DVD_PAYABLE',
              'WITHDR_OTHERSURPRESERVE', 'COMSHARE_DVD_PAYABLE', 'CAPITALIZED_COMSTOCK_DIV',
              'NET_AFTER_DED_NR_LP_CORRECT', 'OTHER_INCOME', 'ASSET_DISPOSAL_INCOME', 'CONTINUED_NET_PROFIT',
              'END_NET_PROFIT', 'CREDIT_IMPAIRMENT_LOSS', 'NET_EXPOSURE_HEDGING_BENEFITS', 'RD_EXPENSE',
              'STMNOTE_FINEXP', 'FIN_EXP_INT_INC', 'OTHER_IMPAIR_LOSS_ASSETS', 'TOT_OPER_COST2'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
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
    NET_PROFIT_AFTER_DED_NR_LP = Column(Numeric(20, 4), comment='扣除非经常性损益后净利润（扣除少数股东损益）')
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
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    NET_AFTER_DED_NR_LP_CORRECT = Column(Numeric(20, 4), comment='扣除非经常性损益后的净利润(财务重要指标(更正前))')
    OTHER_INCOME = Column(Numeric(20, 4), comment='其他收益')
    MEMO = Column(VARCHAR(1000), comment='备注')
    ASSET_DISPOSAL_INCOME = Column(Numeric(20, 4), comment='资产处置收益')
    CONTINUED_NET_PROFIT = Column(Numeric(20, 4), comment='持续经营净利润')
    END_NET_PROFIT = Column(Numeric(20, 4), comment='终止经营净利润')
    CREDIT_IMPAIRMENT_LOSS = Column(Numeric(20, 4), comment='信用减值损失')
    NET_EXPOSURE_HEDGING_BENEFITS = Column(Numeric(20, 4), comment='净敞口套期收益')
    RD_EXPENSE = Column(Numeric(20, 4), comment='研发费用')
    STMNOTE_FINEXP = Column(Numeric(20, 4), comment='财务费用:利息费用')
    FIN_EXP_INT_INC = Column(Numeric(20, 4), comment='财务费用:利息收入')
    IS_CALCULATION = Column(Numeric(5, 0), comment='是否计算报表')
    OTHER_IMPAIR_LOSS_ASSETS = Column(Numeric(20, 4), comment='其他资产减值损失')
    TOT_OPER_COST2 = Column(Numeric(20, 4), comment='营业总成本2')


class ASHAREINCOMETAX(Base):
    """中国A股财务附注--所得税"""
    __tablename__ = 'ASHAREINCOMETAX'
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


class ASHAREINCOMETAXADJPROC(Base):
    """中国A股财务附注--所得税调整过程"""
    __tablename__ = 'ASHAREINCOMETAXADJPROC'
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


class ASHAREINCQUANTITYDETAILS(Base):
    """中国A股股权激励数量明细"""
    __tablename__ = 'ASHAREINCQUANTITYDETAILS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INC_SEQUENCE = Column(VARCHAR(6), comment='序号')
    S_INC_NAME = Column(VARCHAR(80), comment='姓名')
    S_INC_POST = Column(VARCHAR(80), comment='职位')
    S_INC_QUANTITY = Column(Numeric(20, 4), comment='数量(万股/万份)')
    S_INC_TOTALQTYPCT = Column(Numeric(20, 4), comment='占本次授予总数量比例(%)')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class ASHAREINCQUANTITYPRICE(Base):
    """中国A股股权激励数量与价格"""
    __tablename__ = 'ASHAREINCQUANTITYPRICE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INC_SEQUENCE = Column(VARCHAR(6), comment='序号')
    S_INC_TRANSFERPRIPER = Column(Numeric(20, 4), comment='每股转让价格(行权价格)')
    S_INC_QUANTITY = Column(Numeric(20, 4), comment='激励数量(万份)')
    S_INC_GETFUNDQTY = Column(Numeric(20, 4), comment='提取激励基金数量(元)')
    S_INC_ISCOMPLETED = Column(Numeric(5, 0), comment='股权激励是否全部完成')
    S_INC_GRANTDATE = Column(VARCHAR(8), comment='期权授权日')
    S_INC_DNEXEC_QUANTITY = Column(Numeric(20, 4), comment='已授权未行权的期权数量(万份)')
    S_INC_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')


class ASHAREINDUSRATING(Base):
    """中国A股行业投资评级"""
    __tablename__ = 'ASHAREINDUSRATING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    WIND_IND_CODE = Column(VARCHAR(50), comment='Wind行业ID')
    RATING_INSTITUTE = Column(VARCHAR(20), comment='机构')
    RATING_INSTITUTE_ID = Column(VARCHAR(38), comment='[内部]机构id')
    RATING_ANALYST = Column(VARCHAR(20), comment='分析师')
    RATING_ANALYST_ID = Column(VARCHAR(200), comment='[内部]分析师id')
    REPORT_TYPE_CODE = Column(Numeric(9, 0), comment='报告类型代码')
    RATING_DT = Column(VARCHAR(8), comment='评级日期')
    END_DT = Column(VARCHAR(8), comment='有效期截止日')
    RATING_MEMO = Column(VARCHAR(2000), comment='[内部]摘要')
    SCORE = Column(Numeric(20, 0), comment='得分')
    RATING = Column(VARCHAR(100), comment='新评级')
    REPORT_IND = Column(VARCHAR(100), comment='原始行业')
    COLLECT_DT = Column(VARCHAR(8), comment='[内部]公告日期')


class ASHAREINDUSTRIESCLASS(Base):
    """中国A股Wind行业分类"""
    __tablename__ = 'ASHAREINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_IND_CODE = Column(VARCHAR(50), comment='Wind行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHAREINDUSTRIESCLASSCITICS(Base):
    """中国A股中信行业分类"""
    __tablename__ = 'ASHAREINDUSTRIESCLASSCITICS'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    WIND_CODE = Column(VARCHAR(40))
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CITICS_IND_CODE = Column(VARCHAR(50), comment='中信行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHAREINDUSTRIESCLASSCITICSZL(Base):
    """中国A股中信行业分类(增量)"""
    __tablename__ = 'ASHAREINDUSTRIESCLASSCITICSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40))
    CITICS_IND_CODE = Column(VARCHAR(50), comment='中信行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHAREINDUSTRIESCLASSZL(Base):
    """中国A股Wind行业分类(增量)"""
    __tablename__ = 'ASHAREINDUSTRIESCLASSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_CODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_IND_CODE = Column(VARCHAR(50), comment='Wind行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHAREINDUSTRIESCODE(Base):
    """行业代码"""
    __tablename__ = 'ASHAREINDUSTRIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='行业代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='行业名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')
    USED = Column(Numeric(1, 0), comment='是否有效')
    INDUSTRIESALIAS = Column(VARCHAR(12), comment='板块别名')
    SEQUENCE = Column(Numeric(4, 0), comment='展示序号')
    MEMO = Column(VARCHAR(100), comment='备注')
    CHINESEDEFINITION = Column(VARCHAR(600), comment='板块中文定义')
    WIND_NAME_ENG = Column(VARCHAR(200), comment='板块英文名称')


class ASHAREINSIDEHOLDER(Base):
    """中国A股前十大股东"""
    __tablename__ = 'ASHAREINSIDEHOLDER'
    __table_args__ = (
        Index('IDX_ASHAREINSIDEHOLDER_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_HOLDER_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_HOLDER_HOLDERCATEGORY = Column(VARCHAR(1), comment='股东类型')
    S_HOLDER_NAME = Column(VARCHAR(100), comment='股东名称')
    S_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='持股数量')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例')
    S_HOLDER_SHARECATEGORY = Column(VARCHAR(40), comment='持股性质代码')
    S_HOLDER_RESTRICTEDQUANTITY = Column(Numeric(20, 4), comment='持有限售股份（非流通股）数量')
    S_HOLDER_ANAME = Column(VARCHAR(100), comment='股东名称')
    S_HOLDER_SEQUENCE = Column(VARCHAR(200), comment='关联方序号')
    S_HOLDER_SHARECATEGORYNAME = Column(VARCHAR(40), comment='持股性质')
    S_HOLDER_MEMO = Column(VARCHAR(1500), comment='股东说明')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(10), comment='报告期')


class ASHAREINSIDERTRADE(Base):
    """中国A股内部人交易"""
    __tablename__ = 'ASHAREINSIDERTRADE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    RELATED_MANAGER_NAME = Column(VARCHAR(100), comment='相关管理层姓名')
    REPORTED_TRADER_NAME = Column(VARCHAR(100), comment='变动人姓名')
    CHANGE_VOLUME = Column(Numeric(20, 4), comment='变动数')
    TRADE_AVG_PRICE = Column(Numeric(20, 4), comment='成交均价')
    POSITION_AFTER_TRADE = Column(Numeric(20, 4), comment='变动后持股')
    TRADE_DT = Column(VARCHAR(8), comment='变动日期')
    ANN_DT = Column(VARCHAR(8), comment='填报日期')
    TRADE_REASON_CODE = Column(Numeric(9, 0), comment='变动原因类型代码')
    RELATED_MANAGER_POST = Column(VARCHAR(80), comment='相关管理层职务')
    TRADER_MANAGER_RELATION = Column(VARCHAR(20), comment='变动人与管理层的关系')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='实际公告日期')
    IS_SHORT_TERM_TRADE = Column(Numeric(5, 0), comment='是否为短线交易')


class ASHAREINSTHOLDERDERDATA(Base):
    """中国A股机构持股衍生数据"""
    __tablename__ = 'ASHAREINSTHOLDERDERDATA'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_HOLDER_COMPCODE = Column(VARCHAR(40), comment='股东公司id')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    S_HOLDER_HOLDERCATEGORY = Column(VARCHAR(40), comment='股东类型')
    S_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='持股数')
    S_HOLDER_PCT = Column(Numeric(20, 6), comment='持股比例(计算)')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_FLOAT_A_SHR = Column(Numeric(20, 4), comment='流通A股')


class ASHAREINSURANCEINDICATOR(Base):
    """中国A股保险专用指标"""
    __tablename__ = 'ASHAREINSURANCEINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
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


class ASHAREINTANGIBLEASSETS(Base):
    """中国A股财务附注--无形资产"""
    __tablename__ = 'ASHAREINTANGIBLEASSETS'
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


class ASHAREINTENSITYTREND(Base):
    """中国A股强弱与趋向技术指标(不复权)"""
    __tablename__ = 'ASHAREINTENSITYTREND'
    __table_args__ = (
        Index('IDX_ASHAREINTENSITYTREND_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    MARKET = Column(Numeric(20, 8), comment='大盘同步指标沪深300(7日)')
    STRENGTH = Column(Numeric(20, 8), comment='阶段强势指标沪深300(20日)')
    WEAKKNESS = Column(Numeric(20, 8), comment='阶段弱势指标沪深300(20日)')
    BOTTOMING_B = Column(Numeric(20, 8), comment='筑底指标B(125,5,20日)')
    BOTTOMING_D = Column(Numeric(20, 8), comment='筑底指标D(125,5,20日)')
    DMI_PDI = Column(Numeric(20, 8), comment='DMI趋向指标PDI(14,6日)')
    DMI_MDI = Column(Numeric(20, 8), comment='DMI趋向指标MDI(14,6日)')
    DMI_ADX = Column(Numeric(20, 8), comment='DMI趋向指标ADX(14,6日)')
    DMI_ADXR = Column(Numeric(20, 8), comment='DMI趋向指标ADXR(14,6日)')
    EXPMA = Column(Numeric(20, 8), comment='EXPMA指数平均数(12日)')
    MA_5D = Column(Numeric(20, 8), comment='MA简单移动平均(5日)')
    MA_10D = Column(Numeric(20, 8), comment='MA简单移动平均(10日)')
    MA_20D = Column(Numeric(20, 8), comment='MA简单移动平均(20日)')
    MA_30D = Column(Numeric(20, 8), comment='MA简单移动平均30日)')
    MA_60D = Column(Numeric(20, 8), comment='MA简单移动平均(60日)')
    MA_120D = Column(Numeric(20, 8), comment='MA简单移动平均(120日)')
    MA_250D = Column(Numeric(20, 8), comment='MA简单移动平均(250日)')
    MACD_DIFF = Column(Numeric(20, 8), comment='MACD指数平滑异同平均DIFF(26,12,9日)')
    MACD_DEA = Column(Numeric(20, 8), comment='MACD指数平滑异同平均DEA(26,12,9日)')
    MACD_MACD = Column(Numeric(20, 8), comment='MACD指数平滑异同平均MACD(26,12,9日)')
    BBI = Column(Numeric(20, 8), comment='BBI多空指数(3,6,12,24日)')
    DDI = Column(Numeric(20, 8), comment='DDI方向标准离差指数DDI(13,30,5,10日)')
    DDI_ADDI = Column(Numeric(20, 8), comment='DDI方向标准离差指数ADDI(13,30,5,10日)')
    DDI_AD = Column(Numeric(20, 8), comment='DDI方向标准离差指数AD(13,30,5,10日)')
    DMA_DDD = Column(Numeric(20, 8), comment='DMA平均线差DDD(10,50,10日)')
    DMA_AMA = Column(Numeric(20, 8), comment='DMA平均线差AMA(10,50,10日)')
    MTM = Column(Numeric(20, 8), comment='MTM动力指标MTM(6,6日)')
    MTM_MTMMA = Column(Numeric(20, 8), comment='MTM动力指标MTMMA(6,6日)')
    PRICEOSC = Column(Numeric(20, 8), comment='PRICEOSC价格振荡指标(26,12日)')
    TRIX = Column(Numeric(20, 8), comment='TRIX三重指数平滑平均TRIX(12,20日)')
    TRMA = Column(Numeric(20, 8), comment='TRIX三重指数平滑平均TRMA(12,20日)')
    SAR = Column(Numeric(20, 8), comment='SAR抛物转向(4,2,20日)')


class ASHAREINTENSITYTRENDADJ(Base):
    """中国A股强弱与趋向技术指标(后复权)"""
    __tablename__ = 'ASHAREINTENSITYTRENDADJ'
    __table_args__ = (
        Index('IDX_ASHAREINTENSITYTRENDADJ_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    MARKET = Column(Numeric(20, 8), comment='大盘同步指标沪深300(7日)')
    STRENGTH = Column(Numeric(20, 8), comment='阶段强势指标沪深300(20日)')
    WEAKKNESS = Column(Numeric(20, 8), comment='阶段弱势指标沪深300(20日)')
    BOTTOMING_B = Column(Numeric(20, 8), comment='筑底指标B(125,5,20日)')
    BOTTOMING_D = Column(Numeric(20, 8), comment='筑底指标D(125,5,20日)')
    DMI_PDI = Column(Numeric(20, 8), comment='DMI趋向指标PDI(14,6日)')
    DMI_MDI = Column(Numeric(20, 8), comment='DMI趋向指标MDI(14,6日)')
    DMI_ADX = Column(Numeric(20, 8), comment='DMI趋向指标ADX(14,6日)')
    DMI_ADXR = Column(Numeric(20, 8), comment='DMI趋向指标ADXR(14,6日)')
    EXPMA = Column(Numeric(20, 8), comment='EXPMA指数平均数(12日)')
    MA_5D = Column(Numeric(20, 8), comment='MA简单移动平均(5日)')
    MA_10D = Column(Numeric(20, 8), comment='MA简单移动平均(10日)')
    MA_20D = Column(Numeric(20, 8), comment='MA简单移动平均(20日)')
    MA_30D = Column(Numeric(20, 8), comment='MA简单移动平均30日)')
    MA_60D = Column(Numeric(20, 8), comment='MA简单移动平均(60日)')
    MA_120D = Column(Numeric(20, 8), comment='MA简单移动平均(120日)')
    MA_250D = Column(Numeric(20, 8), comment='MA简单移动平均(250日)')
    MACD_DIFF = Column(Numeric(20, 8), comment='MACD指数平滑异同平均DIFF(26,12,9日)')
    MACD_DEA = Column(Numeric(20, 8), comment='MACD指数平滑异同平均DEA(26,12,9日)')
    MACD_MACD = Column(Numeric(20, 8), comment='MACD指数平滑异同平均MACD(26,12,9日)')
    BBI = Column(Numeric(20, 8), comment='BBI多空指数(3,6,12,24日)')
    DDI = Column(Numeric(20, 8), comment='DDI方向标准离差指数DDI(13,30,5,10日)')
    DDI_ADDI = Column(Numeric(20, 8), comment='DDI方向标准离差指数ADDI(13,30,5,10日)')
    DDI_AD = Column(Numeric(20, 8), comment='DDI方向标准离差指数AD(13,30,5,10日)')
    DMA_DDD = Column(Numeric(20, 8), comment='DMA平均线差DDD(10,50,10日)')
    DMA_AMA = Column(Numeric(20, 8), comment='DMA平均线差AMA(10,50,10日)')
    MTM = Column(Numeric(20, 8), comment='MTM动力指标MTM(6,6日)')
    MTM_MTMMA = Column(Numeric(20, 8), comment='MTM动力指标MTMMA(6,6日)')
    PRICEOSC = Column(Numeric(20, 8), comment='PRICEOSC价格振荡指标(26,12日)')
    TRIX = Column(Numeric(20, 8), comment='TRIX三重指数平滑平均TRIX(12,20日)')
    TRMA = Column(Numeric(20, 8), comment='TRIX三重指数平滑平均TRMA(12,20日)')
    SAR = Column(Numeric(20, 8), comment='SAR抛物转向(4,2,20日)')


class ASHAREINTERESTRATERISK(Base):
    """中国A股财务附注-利率风险"""
    __tablename__ = 'ASHAREINTERESTRATERISK'
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


class ASHAREINTERESTRECEIVABLE(Base):
    """中国A股财务附注--应收利息"""
    __tablename__ = 'ASHAREINTERESTRECEIVABLE'
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


class ASHAREINTERNETVOTING(Base):
    """中国A股股东大会议案网络投票表决情况"""
    __tablename__ = 'ASHAREINTERNETVOTING'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_EVENT_ID = Column(VARCHAR(40), comment='会议事件ID')
    S_EVENT_NUM = Column(VARCHAR(20), comment='议案序号')
    S_EVENT_NAME = Column(VARCHAR(2000), comment='议案名称')
    S_INFO_TYPE = Column(VARCHAR(300), comment='表决方式类型')
    S_INFO_PRICE = Column(Numeric(20, 4), comment='申报价格')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='[内部]公司ID')
    ANN_DT = Column(VARCHAR(8), comment='[内部]公告日期')


class ASHAREINTPAYABLE(Base):
    """中国A股财务附注--应付利息"""
    __tablename__ = 'ASHAREINTPAYABLE'
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


class ASHAREINTRODUCTION(Base):
    """中国A股公司简介"""
    __tablename__ = 'ASHAREINTRODUCTION'
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
    S_INFO_BUSINESSSCOPE = Column(TEXT(2147483647), comment='经营范围')
    S_INFO_COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')


class ASHAREINTRODUCTIONBT(Base):
    """中国A股公司简介(回测)"""
    __tablename__ = 'ASHAREINTRODUCTIONBT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    LATEST_OBJECT_ID = Column(VARCHAR(100), comment='最新对象ID')
    BACKREASON_CODE = Column(VARCHAR(2), comment='修改原因代码')
    BACKTIME = Column(DateTime, comment='修改时间')
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
    S_INFO_BUSINESSSCOPE = Column(VARCHAR(3700), comment='经营范围')
    S_INFO_COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')


class ASHAREINTRODUCTIONZL(Base):
    """中国A股公司简介(增量)"""
    __tablename__ = 'ASHAREINTRODUCTIONZL'
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
    S_INFO_BUSINESSSCOPE = Column(TEXT(2147483647), comment='经营范围')
    S_INFO_COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')


class ASHAREINVEFALLPRICERES(Base):
    """中国A股财务附注--存货跌价准备"""
    __tablename__ = 'ASHAREINVEFALLPRICERES'
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


class ASHAREINVENTORYDETAILS(Base):
    """中国A股存货明细"""
    __tablename__ = 'ASHAREINVENTORYDETAILS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    INV_OBJECT = Column(VARCHAR(100), comment='项目')
    INV_AMT = Column(Numeric(20, 4), comment='金额')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PROVISION = Column(Numeric(20, 4), comment='跌价准备')
    STATEMENT_TYPE = Column(Numeric(9, 0), comment='报告类型代码')
    NET = Column(Numeric(20, 4), comment='净额')
    SUBJECT_NAME = Column(VARCHAR(20), comment='科目名称')


class ASHAREINVESTMENTINCOME(Base):
    """中国A股财务附注--投资收益"""
    __tablename__ = 'ASHAREINVESTMENTINCOME'
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


class ASHAREINVESTMENTPEVC(Base):
    """中国A股投资PEVC基金"""
    __tablename__ = 'ASHAREINVESTMENTPEVC'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='投资公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='投资公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='投资公司ID')
    S_HOLDER_DATE = Column(VARCHAR(10), comment='投资时间')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='股权比例')


class ASHAREINVESTMENTREALESTATE(Base):
    """中国A股财务附注--投资性房地产"""
    __tablename__ = 'ASHAREINVESTMENTREALESTATE'
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


class ASHAREIPO(Base):
    """中国A股首次公开发行数据"""
    __tablename__ = 'ASHAREIPO'
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
    S_FELLOW_UNFROZEDATE = Column(VARCHAR(8), comment='网上中签结果公告日')
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
    S_IPO_LPURNAMEONL = Column(VARCHAR(20), comment='废弃')
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
    PREL_INQ_EFFECT_QT_NUM = Column(Numeric(20, 4), comment='初步询价有效报价总量(万股)')
    IS_LEADUNDERWRITER = Column(Numeric(1, 0), comment='是否有主承销商')
    OFFLINE_PLACING_METHODCODE = Column(Numeric(9, 0), comment='网下投资者分类配售方式代码')
    OFFLINE_PLACING_NTDPROPORTION = Column(Numeric(20, 4), comment='网下投资者分类配售限售比例')
    S_IPO_ASSET_SCALE_DDL = Column(VARCHAR(8), comment='资产规模截止日')
    ABNORMALISSUE_ANN_DT = Column(VARCHAR(8), comment='发行异常公告日')
    ONLINE_ESTIMTSHARES_BFCALLBK = Column(Numeric(20, 4), comment='回拨前网上预计配售股数')
    S_IPO_CALLBACK_DIRECTION = Column(VARCHAR(50), comment='回拨方向')
    OFFLINE_ESTIMTSHARES_BFCALLBK = Column(Numeric(20, 4), comment='回拨前网下预计配售股数')


class ASHAREIPOAMOUNT(Base):
    """中国A股股票发行数量"""
    __tablename__ = 'ASHAREIPOAMOUNT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DATE = Column(VARCHAR(8), comment='变动日')
    ANN_DATE = Column(VARCHAR(8), comment='公告日')
    S_IPO_OSDEXPOFFAMOUNT = Column(Numeric(20, 4), comment='发行股份数')
    S_SHARE_TOTALRESTRICTED = Column(Numeric(20, 4), comment='限售股数')
    S_SHARE_TOTALTRADABLE = Column(Numeric(20, 4), comment='无限售股份数')
    S_SHARE_BE_LISTED = Column(Numeric(20, 4), comment='其中:待上市流通股数')
    S_SHARE_NTRD_STATJUR = Column(Numeric(20, 4), comment='非流通股份数')
    S_SHARE_CHANGEREASON = Column(VARCHAR(100), comment='[内部]股本变动原因')


class ASHAREIPOCLASS(Base):
    """中国A股IPO类型"""
    __tablename__ = 'ASHAREIPOCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_TYPECODE = Column(VARCHAR(50), comment='分类代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHAREIPOPRICINGFORECAST(Base):
    """中国A股上市定价预测"""
    __tablename__ = 'ASHAREIPOPRICINGFORECAST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    RESEARCH_INST_NAME = Column(VARCHAR(20), comment='机构名称')
    RESEARCH_INST_ID = Column(VARCHAR(10), comment='机构ID')
    RESEARCH_INST_ID2 = Column(VARCHAR(40), comment='机构编码')
    ANALYST_NAME = Column(VARCHAR(40), comment='分析师名称')
    ANALYST_ID = Column(VARCHAR(100), comment='作者ID')
    EST_DT = Column(VARCHAR(8), comment='预测日期')
    COLLECT_TIME = Column(VARCHAR(8), comment='[内部]公告日期')
    FIRST_OPTIME = Column(DateTime, comment='[内部]发布日期')
    PRICE_FLOOR = Column(Numeric(20, 4), comment='定价区间下限')
    PRICE_CEILING = Column(Numeric(20, 4), comment='定价区间上限')
    INQUIRY_PRICE_FLOOR = Column(Numeric(20, 4), comment='询价建议区间下限')
    INQUIRY_PRICE_CEILING = Column(Numeric(20, 4), comment='询价建议区间上限')
    EST_MEMO = Column(VARCHAR(500), comment='预测摘要')


class ASHAREIPOROADSHOW(Base):
    """中国A股路演推介信息"""
    __tablename__ = 'ASHAREIPOROADSHOW'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ROADSHOW_TYPE = Column(Numeric(9, 0), comment='路演类型代码')
    ROADSHOW_MODE = Column(Numeric(9, 0), comment='路演方式代码')
    ROADSHOW_DATE = Column(Numeric(9, 0), comment='路演日期')
    START_TM = Column(VARCHAR(8), comment='路演开始时间')
    END_TM = Column(VARCHAR(8), comment='路演截止时间')
    CITY = Column(VARCHAR(10), comment='路演城市')
    PLACE = Column(VARCHAR(300), comment='路演地点')
    ADDRESS = Column(VARCHAR(500), comment='路演地址')


class ASHAREISSUECOMMAUDIT(Base):
    """中国A股发行审核一览"""
    __tablename__ = 'ASHAREISSUECOMMAUDIT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPANYNAME = Column(VARCHAR(100), comment='公司名称')
    S_IC_YEAR = Column(VARCHAR(4), comment='年度')
    S_IC_SESSIONTIMES = Column(VARCHAR(3), comment='会议届次')
    S_IC_AUDITTYPE = Column(VARCHAR(40), comment='审核类型')
    S_IC_TYPE = Column(Numeric(9, 0), comment='发审委类型')
    S_IC_ANNOUNCEMENTDATE = Column(VARCHAR(8), comment='会议公告日期')
    S_IC_DATE = Column(VARCHAR(8), comment='会议日期')
    S_IC_AUDITOCETYPE = Column(VARCHAR(1), comment='审核结果类型')
    S_IC_AUDITANNOCEDATE = Column(VARCHAR(8), comment='审核结果公告日期')
    S_INFO_EXPECTEDISSUESHARES = Column(Numeric(20, 4), comment='预计发行股数(万股)')
    S_INFO_EXPECTEDCOLLECTION = Column(Numeric(20, 4), comment='预计募集资金(万元)')
    S_INFO_VETO_REASON = Column(TEXT(2147483647), comment='被否原因')


class ASHAREISSUECOMMAUDITZL(Base):
    """中国A股发行审核一览(增量)"""
    __tablename__ = 'ASHAREISSUECOMMAUDITZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPANYNAME = Column(VARCHAR(100), comment='公司名称')
    S_IC_YEAR = Column(VARCHAR(4), comment='年度')
    S_IC_SESSIONTIMES = Column(VARCHAR(3), comment='会议届次')
    S_IC_AUDITTYPE = Column(VARCHAR(40), comment='审核类型')
    S_IC_TYPE = Column(Numeric(9, 0), comment='发审委类型')
    S_IC_ANNOUNCEMENTDATE = Column(VARCHAR(8), comment='会议公告日期')
    S_IC_DATE = Column(VARCHAR(8), comment='会议日期')
    S_IC_AUDITOCETYPE = Column(VARCHAR(1), comment='审核结果类型')
    S_IC_AUDITANNOCEDATE = Column(VARCHAR(8), comment='审核结果公告日期')
    S_INFO_EXPECTEDISSUESHARES = Column(Numeric(20, 4), comment='预计发行股数(万股)')
    S_INFO_EXPECTEDCOLLECTION = Column(Numeric(20, 4), comment='预计募集资金(万元)')
    S_INFO_VETO_REASON = Column(TEXT(2147483647), comment='被否原因')


class ASHAREISSUINGDATEPREDICT(Base):
    """中国A股定期报告披露日期"""
    __tablename__ = 'ASHAREISSUINGDATEPREDICT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_STM_PREDICT_ISSUINGDATE = Column(VARCHAR(9), comment='预计披露日期(最新)')
    S_STM_ACTUAL_ISSUINGDATE = Column(VARCHAR(8), comment='实际披露日期')
    S_STM_CORRECT_NUM = Column(VARCHAR(20), comment='更正公告披露次数')
    S_STM_CORRECT_ISSUINGDATE = Column(VARCHAR(100), comment='更正公告披露日期')
    ANN_DT = Column(VARCHAR(8), comment='预计披露日期公告日(最新)')


class ASHAREISSUINGDATEPREDICTBT(Base):
    """中国A股定期报告披露日期(回测)"""
    __tablename__ = 'ASHAREISSUINGDATEPREDICTBT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    LATEST_OBJECT_ID = Column(VARCHAR(100), comment='最新对象ID')
    BACKREASON_CODE = Column(VARCHAR(2), comment='修改原因代码')
    BACKTIME = Column(DateTime, comment='修改时间')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_STM_PREDICT_ISSUINGDATE = Column(VARCHAR(8), comment='预计披露日期')
    S_STM_ACTUAL_ISSUINGDATE = Column(VARCHAR(8), comment='实际披露日期')
    S_STM_CORRECT_NUM = Column(VARCHAR(20), comment='更正公告披露次数')
    S_STM_CORRECT_ISSUINGDATE = Column(VARCHAR(100), comment='更正公告披露日期')
    ANN_DT = Column(VARCHAR(8), comment='预计披露日期公告日')


class ASHAREKINDSOVELOANSTERM(Base):
    """中国A股财务附注--期限划分下的各类逾期贷款"""
    __tablename__ = 'ASHAREKINDSOVELOANSTERM'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    ITEM_DATA = Column(VARCHAR(40), comment='数据内容')
    ITEM_TYPE_CODE = Column(VARCHAR(4), comment='项目类别代码')
    ANN_ITEM = Column(VARCHAR(400), comment='项目公布名称')
    ITEM_AMOUNT = Column(Numeric(20, 4), comment='项目金额(元)')
    ITEM_NAME = Column(VARCHAR(100), comment='项目容错名称')


class ASHAREL2INDICATORS(Base):
    """中国A股Level2指标"""
    __tablename__ = 'ASHAREL2INDICATORS'
    __table_args__ = (
        Index('IDX_ASHAREL2INDICATORS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_LI_INITIATIVEBUYRATE = Column(Numeric(20, 4), comment='主买比率(%)')
    S_LI_INITIATIVEBUYMONEY = Column(Numeric(20, 4), comment='主买总额(万元)')
    S_LI_INITIATIVEBUYAMOUNT = Column(Numeric(20, 4), comment='主买总量(手)')
    S_LI_INITIATIVESELLRATE = Column(Numeric(20, 4), comment='主卖比率(%)')
    S_LI_INITIATIVESELLMONEY = Column(Numeric(20, 4), comment='主卖总额(万元)')
    S_LI_INITIATIVESELLAMOUNT = Column(Numeric(20, 4), comment='主卖总量(手)')
    S_LI_LARGEBUYRATE = Column(Numeric(20, 4), comment='大买比率(%)')
    S_LI_LARGEBUYMONEY = Column(Numeric(20, 4), comment='大买总额(万元)')
    S_LI_LARGEBUYAMOUNT = Column(Numeric(20, 4), comment='大买总量(手)')
    S_LI_LARGESELLRATE = Column(Numeric(20, 4), comment='大卖比率(%)')
    S_LI_LARGESELLMONEY = Column(Numeric(20, 4), comment='大卖总额(万元)')
    S_LI_LARGESELLAMOUNT = Column(Numeric(20, 4), comment='大卖总量(手)')
    S_LI_ENTRUSTRATE = Column(Numeric(20, 4), comment='总委比(%)')
    S_LI_ENTRUDIFFERAMOUNT = Column(Numeric(20, 4), comment='总委差量(手)')
    S_LI_ENTRUDIFFERAMONEY = Column(Numeric(20, 4), comment='总委差额(万元)')
    S_LI_ENTRUSTBUYMONEY = Column(Numeric(20, 4), comment='总委买额(万元)')
    S_LI_ENTRUSTSELLMONEY = Column(Numeric(20, 4), comment='总委卖额(万元)')
    S_LI_ENTRUSTBUYAMOUNT = Column(Numeric(20, 4), comment='总委买量(手)')
    S_LI_ENTRUSTSELLAMOUNT = Column(Numeric(20, 4), comment='总委卖量(手)')


class ASHARELEADUNDERWRITER(Base):
    """中国A股发行主承销商"""
    __tablename__ = 'ASHARELEADUNDERWRITER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_LU_ANNISSUEDATE = Column(VARCHAR(8), comment='发行公告日')
    S_LU_ISSUEDATE = Column(VARCHAR(8), comment='发行日期')
    S_LU_ISSUETYPE = Column(VARCHAR(1), comment='发行类型')
    S_LU_TOTALISSUECOLLECTION = Column(Numeric(20, 4), comment='募集资金合计(万元)')
    S_LU_TOTALISSUEEXPENSES = Column(Numeric(20, 4), comment='发行费用合计(万元)')
    S_LU_TOTALUDERANDSPONEFEE = Column(Numeric(20, 4), comment='承销与保荐费用(万元)')
    S_LU_NUMBER = Column(VARCHAR(1), comment='参与主承销商个数')
    S_LU_NAME = Column(VARCHAR(100), comment='参与主承销商名称')
    S_LU_INSTITYPE = Column(VARCHAR(40), comment='主承销商类型')
    S_LU_AUX_TYPE = Column(VARCHAR(40), comment='辅助类型')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='主承销商id')
    ALL_LU = Column(VARCHAR(1000), comment='全部参与主承销商名称')
    MEETING_DT = Column(VARCHAR(8), comment='发审委会议日期')
    PASS_DT = Column(VARCHAR(8), comment='发审委通过公告日')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    TYPE = Column(VARCHAR(40), comment='发行类型')
    NETCOLLECTION = Column(Numeric(20, 4), comment='募资净额合计(万元)')
    AVG_TOTALCOLL = Column(Numeric(20, 4), comment='募集总额算术平均 (万元)')
    AVG_NETCOLL = Column(Numeric(20, 4), comment='募资净额算术平均 (万元)')


class ASHARELIQUIDITYRISK(Base):
    """中国A股财务附注--流动性风险"""
    __tablename__ = 'ASHARELIQUIDITYRISK'
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


class ASHARELOANDETAILS(Base):
    """中国A股贷款明细"""
    __tablename__ = 'ASHARELOANDETAILS'
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


class ASHARELOANSOTHBANKS(Base):
    """中国A股财务附注--拆入资金"""
    __tablename__ = 'ASHARELOANSOTHBANKS'
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


class ASHARELONGLOAN(Base):
    """中国A股长期借款"""
    __tablename__ = 'ASHARELONGLOAN'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='债务公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='债务公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='债务公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class ASHARELTEQYINVEST(Base):
    """中国A股财务附注--长期股权投资"""
    __tablename__ = 'ASHARELTEQYINVEST'
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


class ASHARELTLOAN(Base):
    """中国A股财务附注--长期借款"""
    __tablename__ = 'ASHARELTLOAN'
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


class ASHARELTPAYABLES(Base):
    """中国A股财务附注--长期应付款"""
    __tablename__ = 'ASHARELTPAYABLES'
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


class ASHARELTPREPAIDEXP(Base):
    """中国A股财务附注--长期待摊费用"""
    __tablename__ = 'ASHARELTPREPAIDEXP'
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


class ASHAREMAINANDNOTEITEMS(Base):
    """None"""
    __tablename__ = 'ASHAREMAINANDNOTEITEMS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEQUENCE1 = Column(Numeric(6, 0), comment='顺序编号')
    ACCOUNTS_ID = Column(VARCHAR(20), comment='科目ID')
    IS_NOT_NULL = Column(Numeric(1, 0), comment='是否非空')
    IS_SHOW = Column(Numeric(1, 0), comment='是否展示')
    S_INFO_TYPECODE = Column(Numeric(9, 0), comment='报表品种代码')
    SUBJECT_CHINESE_NAME = Column(VARCHAR(100), comment='科目中文名')


class ASHAREMAJOREVENT(Base):
    """中国A股重大事件汇总"""
    __tablename__ = 'ASHAREMAJOREVENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_EVENT_CATEGORYCODE = Column(Numeric(9, 0), comment='事件类型代码')
    S_EVENT_ANNCEDATE = Column(VARCHAR(8), comment='披露日期')
    S_EVENT_HAPDATE = Column(VARCHAR(8), comment='发生日期')
    S_EVENT_EXPDATE = Column(VARCHAR(8), comment='失效日期')
    S_EVENT_CONTENT = Column(TEXT(2147483647), comment='事件内容')
    S_EVENT_TEMPLATEID = Column(Numeric(12, 0), comment='模板ID')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class ASHAREMAJORHOLDERPLANHOLD(Base):
    """中国A股股东增持计划"""
    __tablename__ = 'ASHAREMAJORHOLDERPLANHOLD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    S_PH_STARTDATE = Column(VARCHAR(8), comment='增持计划起始日期')
    S_PH_ENDDATE = Column(VARCHAR(8), comment='增持计划截止日期')
    S_PH_CONDITIONORNOT = Column(Numeric(5, 0), comment='是否无条件增持')
    S_PH_TRIGGERPRICE = Column(Numeric(20, 4), comment='增持触发价格')
    S_PH_CONTINUOUSDAYS = Column(Numeric(20, 4), comment='连续天数')
    S_PH_CALCULATEDAYS = Column(Numeric(20, 4), comment='计算天数')
    S_PH_CALCULATEPRICEMODE = Column(VARCHAR(80), comment='价格计算方式')
    S_PH_SHARENUMDOWNLIMIT = Column(Numeric(20, 4), comment='增持股数下限(万股)')
    S_PH_SHARENUMUPLIMIT = Column(Numeric(20, 4), comment='增持股数上限(万股)')
    S_PH_INTENDPUTMONEYDOWNLIMIT = Column(Numeric(20, 4), comment='拟投入金额下限(亿元)')
    S_PH_INTENDPUTMONEYUPLIMIT = Column(Numeric(20, 4), comment='拟投入金额上限(亿元)')
    S_PH_PRICEUPLIMIT = Column(Numeric(20, 4), comment='增持价格上限')


class ASHAREMAJORHOLDERPLANHOLDZL(Base):
    """中国A股大股东增持计划(增量)"""
    __tablename__ = 'ASHAREMAJORHOLDERPLANHOLDZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    S_PH_STARTDATE = Column(VARCHAR(8), comment='增持计划起始日期')
    S_PH_ENDDATE = Column(VARCHAR(8), comment='增持计划截止日期')
    S_PH_CONDITIONORNOT = Column(Numeric(5, 0), comment='是否无条件增持')
    S_PH_TRIGGERPRICE = Column(Numeric(20, 4), comment='增持触发价格')
    S_PH_CONTINUOUSDAYS = Column(Numeric(20, 4), comment='连续天数')
    S_PH_CALCULATEDAYS = Column(Numeric(20, 4), comment='计算天数')
    S_PH_CALCULATEPRICEMODE = Column(VARCHAR(80), comment='价格计算方式')
    S_PH_SHARENUMDOWNLIMIT = Column(Numeric(20, 4), comment='增持股数下限(万股)')
    S_PH_SHARENUMUPLIMIT = Column(Numeric(20, 4), comment='增持股数上限(万股)')
    S_PH_INTENDPUTMONEYDOWNLIMIT = Column(Numeric(20, 4), comment='拟投入金额下限(亿元)')
    S_PH_INTENDPUTMONEYUPLIMIT = Column(Numeric(20, 4), comment='拟投入金额上限(亿元)')
    S_PH_PRICEUPLIMIT = Column(Numeric(20, 4), comment='增持价格上限')


class ASHAREMAJORRECEIVABLES(Base):
    """中国A股主要其它应收款明细"""
    __tablename__ = 'ASHAREMAJORRECEIVABLES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    DEBTOR_NAME = Column(VARCHAR(100), comment='债务人名称')
    ARREARS = Column(Numeric(20, 4), comment='金额')
    DELAYTIME = Column(VARCHAR(40), comment='拖欠时间')
    DELAYREASON = Column(VARCHAR(100), comment='拖欠原因')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')


class ASHAREMANAGEMENT(Base):
    """中国A股公司管理层成员"""
    __tablename__ = 'ASHAREMANAGEMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_GENDER = Column(VARCHAR(10), comment='性别')
    S_INFO_MANAGER_EDUCATION = Column(VARCHAR(10), comment='学历')
    S_INFO_MANAGER_NATIONALITY = Column(VARCHAR(40), comment='国籍')
    S_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(8), comment='出生年份')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8), comment='离职日期')
    S_INFO_MANAGER_TYPE = Column(Numeric(5, 0), comment='管理层类别')
    S_INFO_MANAGER_POST = Column(VARCHAR(60), comment='职务')
    S_INFO_MANAGER_INTRODUCTION = Column(VARCHAR(2000), comment='个人简历')
    MANID = Column(VARCHAR(10), comment='人物ID')
    DISPLAY_ORDER = Column(Numeric(4, 0), comment='展示顺序')


class ASHAREMANAGEMENTEXPENSE(Base):
    """中国A股财务附注--管理费用明细"""
    __tablename__ = 'ASHAREMANAGEMENTEXPENSE'
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


class ASHAREMANAGEMENTHOLDREWARD(Base):
    """中国A股公司管理层持股及报酬"""
    __tablename__ = 'ASHAREMANAGEMENTHOLDREWARD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    END_DATE = Column(VARCHAR(8), comment='截止日期')
    CRNY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_POST = Column(VARCHAR(80), comment='职务')
    S_MANAGER_RETURN = Column(Numeric(20, 4), comment='报酬')
    S_MANAGER_QUANTITY = Column(Numeric(20, 4), comment='持股数量')
    MANID = Column(VARCHAR(10), comment='人物ID')
    S_MANAGER_RETURN_OTHER = Column(Numeric(5, 0), comment='是否在股东或关联单位领取报酬、津贴')


class ASHAREMARGINSHORTFEERATE(Base):
    """中国A股融资融券费率"""
    __tablename__ = 'ASHAREMARGINSHORTFEERATE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    PUBLISHER_ID = Column(VARCHAR(40), comment='发布方ID')
    ITEM_CODE = Column(Numeric(9, 0), comment='项目类别代码')
    EFFECTIVE_DATE = Column(VARCHAR(8), comment='生效日')
    FEE_RATE = Column(Numeric(20, 4), comment='项目数据')


class ASHAREMARGINSUBJECT(Base):
    """中国A股融资融券标的及担保物"""
    __tablename__ = 'ASHAREMARGINSUBJECT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_MARGIN_SHARETYPE = Column(Numeric(9, 0), comment='融资融券相关证券类型代码')
    S_MARGIN_EFFECTDATE = Column(VARCHAR(8), comment='生效日')
    S_MARGIN_ELIMINDATE = Column(VARCHAR(8), comment='剔除日')
    S_MARGIN_MARGINRATE = Column(Numeric(20, 4), comment='保证金比例')
    S_MARGIN_CONVERSIONRATE = Column(Numeric(20, 4), comment='折算率')
    S_MARGIN_RATEEFFECTDATE = Column(VARCHAR(8), comment='保证金比例或折算率生效日')
    S_IS_NEW = Column(Numeric(1, 0), comment='是否最新')
    S_MARGIN_EXPIRATIONDATE = Column(VARCHAR(8), comment='保证金比例或折算率失效日')


class ASHAREMARGINTRADE(Base):
    """中国A股融资融券交易明细"""
    __tablename__ = 'ASHAREMARGINTRADE'
    __table_args__ = (
        Index('IDX_ASHAREMARGINTRADE_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_MARGIN_TRADINGBALANCE = Column(Numeric(20, 4), comment='融资余额(元)')
    S_MARGIN_PURCHWITHBORROWMONEY = Column(Numeric(20, 4), comment='融资买入额(元,股)')
    S_MARGIN_REPAYMENTTOBROKER = Column(Numeric(20, 4), comment='融资偿还额(元,股)')
    S_MARGIN_SECLENDINGBALANCE = Column(Numeric(20, 4), comment='融券余额(元)')
    S_MARGIN_SECLENDINGBALANCEVOL = Column(Numeric(20, 4), comment='融券余量(股,份,手)')
    S_MARGIN_SALESOFBORROWEDSEC = Column(Numeric(20, 4), comment='融券卖出量(股,份,手)')
    S_MARGIN_REPAYMENTOFBORROWSEC = Column(Numeric(20, 4), comment='融券偿还量(股,份,手)')
    S_MARGIN_MARGINTRADEBALANCE = Column(Numeric(20, 4), comment='融资融券余额(元)')
    S_REFIN_SL_VOL_3D = Column(Numeric(20, 0), comment='转融券融出数量(3天)')
    S_REFIN_SL_VOL_7D = Column(Numeric(20, 0), comment='转融券融出数量(7天)')
    S_REFIN_SL_VOL_14D = Column(Numeric(20, 0), comment='转融券融出数量(14天)')
    S_REFIN_SL_VOL_28D = Column(Numeric(20, 0), comment='转融券融出数量(28天)')
    S_REFIN_SL_VOL_182D = Column(Numeric(20, 0), comment='转融券融出数量(182天)')
    S_REFIN_SB_VOL_3D = Column(Numeric(20, 0), comment='转融券融入数量(3天)')
    S_REFIN_SB_VOL_7D = Column(Numeric(20, 0), comment='转融券融入数量(7天)')
    S_REFIN_SB_VOL_14D = Column(Numeric(20, 0), comment='转融券融入数量(14天)')
    S_SB_VOL_28D = Column(Numeric(20, 0), comment='转融券融入数量(28天)')
    S_SB_VOL_182D = Column(Numeric(20, 0), comment='转融券融入数量(182天)')
    S_REFIN_SL_EOD_VOL = Column(Numeric(20, 0), comment='转融券融出日成交量')
    S_REFIN_SB_EOD_VOL = Column(Numeric(20, 0), comment='转融券融入日成交量')
    S_REFIN_SL_EOP_VOL = Column(Numeric(20, 0), comment='转融券期末余量')
    S_REFIN_SL_EOP_BAL = Column(Numeric(20, 4), comment='转融券期末余额')
    S_REFIN_REPAY_VOL = Column(Numeric(20, 0), comment='转融券偿还量')


class ASHAREMARGINTRADESUM(Base):
    """中国A股融资融券交易汇总"""
    __tablename__ = 'ASHAREMARGINTRADESUM'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_MARSUM_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')
    S_MARSUM_TRADINGBALANCE = Column(Numeric(20, 4), comment='融资余额(元)')
    S_MARSUM_PURCHWITHBORROWMONEY = Column(Numeric(20, 4), comment='融资买入额(元)')
    S_MARSUM_REPAYMENTTOBROKER = Column(Numeric(20, 4), comment='融资偿还额(元)')
    S_MARSUM_SECLENDINGBALANCE = Column(Numeric(20, 4), comment='融券余额(元)')
    S_MARSUM_SALESOFBORROWEDSEC = Column(Numeric(20, 4), comment='融券卖出量(股,份,手)')
    S_MARSUM_MARGINTRADEBALANCE = Column(Numeric(20, 4), comment='融资融券余额(元)')
    S_MARSUM_MARGIN_MARGIN = Column(Numeric(20, 4), comment='融券余量')
    S_MARSUM_FINANCING_MARGIN = Column(Numeric(20, 4), comment='融资余量股(份/手)')
    S_MARSUM_SECURITIES_SALES = Column(Numeric(20, 4), comment='融券卖出额(元)')
    S_MARSUM_SECURITIES_REPAY = Column(Numeric(20, 4), comment='融券偿还额(元)')
    S_MARSUM_FLOW_EQUITY = Column(Numeric(24, 8), comment='A股流通股本(万股)')
    S_MARSUM_CIRCULATION_VALUE = Column(Numeric(20, 4), comment='A股流通市值(万元)')
    S_MARSUM_TURNOVER_AMOUNT = Column(Numeric(20, 4), comment='A股成交金额(万元)')


class ASHAREMARKETOVERALLINDEX(Base):
    """沪深市场总体指标(月)"""
    __tablename__ = 'ASHAREMARKETOVERALLINDEX'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    MONTH1 = Column(VARCHAR(8), comment='月份')
    EXCHANGE = Column(VARCHAR(20), comment='交易所')
    LISTED_COMPANY_NUM = Column(Numeric(15, 4), comment='上市公司总数')
    LISTED_SECURITIES_NUM = Column(Numeric(15, 4), comment='上市证券总数')
    LISTED_STOCK_NUM = Column(Numeric(15, 4), comment='上市股票总数')
    LISTED_ASHARE_NUM = Column(Numeric(15, 4), comment='上市A股总数')
    LISTED_BSHARE_NUM = Column(Numeric(15, 4), comment='上市B股总数')
    STOCK_TOTAL_CAPITAL = Column(Numeric(15, 4), comment='股票-总股本(亿元)')
    STOCK_TOTAL_MARKET_VALUE = Column(Numeric(15, 4), comment='股票-总市值(亿元)')
    STOCK_FLOW_EQUITY = Column(Numeric(15, 4), comment='股票-流通股本(亿股)')
    STOCK_FLOW_MARKET_VALUE = Column(Numeric(15, 4), comment='股票-流通市值(亿元)')
    OPEN_ACCOUNTS_NUM = Column(Numeric(15, 4), comment='投资者开户总数(万户)')
    AVERAGE_PE = Column(Numeric(15, 4), comment='平均市盈率')
    ASHARE_AVERAGE_PE = Column(Numeric(15, 4), comment='A股平均市盈率')
    BSHARE_AVERAGE_PE = Column(Numeric(15, 4), comment='B股平均市盈率')
    STOCK_FUND_TRANSACTION_AMOUNT = Column(Numeric(15, 4), comment='股票、基金成交金额:当年累计(亿元)')
    ASHARE_TRANSACTION_AMOUNT = Column(Numeric(15, 4), comment='A股成交金额:当年累计(亿元)')
    BSHARE_TRANSACTION_AMOUNT = Column(Numeric(15, 4), comment='B股成交金额:当年累计(亿元)')
    FUND_TRANSACTION_AMOUNT = Column(Numeric(15, 4), comment='基金成交金额:当年累计(亿元)')
    BOND_TRANSACTION_AMOUNT = Column(Numeric(15, 4), comment='债券成交金额:当年累计(亿元)')
    ASHARE_STAMP_DUTY = Column(Numeric(15, 4), comment='代扣A股交易印花税(亿元)')
    BSHARE_STAMP_DUTY = Column(Numeric(15, 4), comment='代扣B股交易印花税(亿美元/港币)')
    STOCK_REPURCHASE_AMOUNT = Column(Numeric(20, 4), comment='股票回购金额:当年累计')


class ASHAREMECHANISMOWNERSHIP(Base):
    """None"""
    __tablename__ = 'ASHAREMECHANISMOWNERSHIP'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(200), comment='股东公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='股东公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='股东公司ID')
    S_HOLDER_ENDDATE = Column(VARCHAR(10), comment='报告期')
    S_HOLDER_PCT = Column(Numeric(20, 4), comment='持股比例')


class ASHAREMERGERSACQUISITIONS(Base):
    """中国A股收购兼并（恒指专用）"""
    __tablename__ = 'ASHAREMERGERSACQUISITIONS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(200), comment='信息披露方万得代码')
    TARGETOFACQUISN = Column(VARCHAR(100), comment='被收购方名称')
    TARGETOFACQUISN_DISCLOSURE = Column(VARCHAR(40), comment='被收购方与披露方关系')
    ACQUIRINGFIRM = Column(VARCHAR(100), comment='收购方名称')
    ACQUIRINGFIRM_DISCLOSURE = Column(VARCHAR(40), comment='收购方与披露方关系')
    PROGRESS = Column(VARCHAR(10), comment='方案进度')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PAYMENTMETHOD = Column(VARCHAR(40), comment='支付方式')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    TRADINGAMOUNT = Column(Numeric(20, 4), comment='交易金额(万元)')
    IS_RELDPARTRANSACTIONS = Column(Numeric(1, 0), comment='是否关联交易')
    FIRST_DT = Column(VARCHAR(8), comment='首次公告日期')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日期')


class ASHAREMERGERSUBJECT(Base):
    """中国A股并购标的"""
    __tablename__ = 'ASHAREMERGERSUBJECT'
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


class ASHAREMJRHOLDERTRADE(Base):
    """中国A股重要股东增减持"""
    __tablename__ = 'ASHAREMJRHOLDERTRADE'
    __table_args__ = (
        Index('IDX_ASHAREMJRHOLDERTRADE_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    TRANSACT_STARTDATE = Column(VARCHAR(8), comment='变动起始日期')
    TRANSACT_ENDDATE = Column(VARCHAR(8), comment='变动截至日期')
    HOLDER_NAME = Column(VARCHAR(200), comment='持有人')
    HOLDER_TYPE = Column(VARCHAR(1), comment='持有人类型')
    TRANSACT_TYPE = Column(VARCHAR(4), comment='买卖方向')
    TRANSACT_QUANTITY = Column(Numeric(20, 4), comment='变动数量')
    TRANSACT_QUANTITY_RATIO = Column(Numeric(20, 4), comment='变动数量占流通量比例(%)')
    HOLDER_QUANTITY_NEW = Column(Numeric(20, 4), comment='最新持有流通数量')
    HOLDER_QUANTITY_NEW_RATIO = Column(Numeric(20, 4), comment='最新持有流通数量占流通量比例(%)')
    AVG_PRICE = Column(Numeric(20, 4), comment='平均价格')
    WHETHER_AGREED_REPUR_TRANS = Column(Numeric(1, 0), comment='是否约定购回式交易')
    BLOCKTRADE_QUANTITY = Column(Numeric(20, 4), comment='通过大宗交易系统的变动数量')
    IS_RESTRICTED = Column(Numeric(1, 0), comment='是否为减持限售股份')
    IS_REANNOUNCED = Column(Numeric(1, 0), comment='是否重复披露')
    TRADE_DETAIL = Column(VARCHAR(1000), comment='变动说明')
    NEW_HOLD_TOT = Column(Numeric(20, 4), comment='最新持股总数')


class ASHAREMONETARYFUNDOFPROJ(Base):
    """中国A股财务附注--货币资金(按项目)"""
    __tablename__ = 'ASHAREMONETARYFUNDOFPROJ'
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


class ASHAREMONETARYFUNDS(Base):
    """中国A股公司货币资金明细"""
    __tablename__ = 'ASHAREMONETARYFUNDS'
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


class ASHAREMONEYFLOW(Base):
    """中国A股资金流向数据"""
    __tablename__ = 'ASHAREMONEYFLOW'
    __table_args__ = (
        Index('IDX_ASHAREMONEYFLOW_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    BUY_VALUE_EXLARGE_ORDER = Column(Numeric(20, 4), comment='机构买入金额(万元)')
    SELL_VALUE_EXLARGE_ORDER = Column(Numeric(20, 4), comment='机构卖出金额(万元)')
    BUY_VALUE_LARGE_ORDER = Column(Numeric(20, 4), comment='大户买入金额(万元)')
    SELL_VALUE_LARGE_ORDER = Column(Numeric(20, 4), comment='大户卖出金额(万元)')
    BUY_VALUE_MED_ORDER = Column(Numeric(20, 4), comment='中户买入金额(万元)')
    SELL_VALUE_MED_ORDER = Column(Numeric(20, 4), comment='中户卖出金额(万元)')
    BUY_VALUE_SMALL_ORDER = Column(Numeric(20, 4), comment='散户买入金额(万元)')
    SELL_VALUE_SMALL_ORDER = Column(Numeric(20, 4), comment='散户卖出金额(万元)')
    BUY_VOLUME_EXLARGE_ORDER = Column(Numeric(20, 4), comment='机构买入总量(手)')
    SELL_VOLUME_EXLARGE_ORDER = Column(Numeric(20, 4), comment='机构卖出总量(手)')
    BUY_VOLUME_LARGE_ORDER = Column(Numeric(20, 4), comment='大户买入总量(手)')
    SELL_VOLUME_LARGE_ORDER = Column(Numeric(20, 4), comment='大户卖出总量(手)')
    BUY_VOLUME_MED_ORDER = Column(Numeric(20, 4), comment='中户买入总量(手) ')
    SELL_VOLUME_MED_ORDER = Column(Numeric(20, 4), comment='中户卖出总量(手) ')
    BUY_VOLUME_SMALL_ORDER = Column(Numeric(20, 4), comment='散户买入总量(手) ')
    SELL_VOLUME_SMALL_ORDER = Column(Numeric(20, 4), comment='散户卖出总量(手) ')
    TRADES_COUNT = Column(Numeric(20, 4), comment='成交笔数(笔)')
    BUY_TRADES_EXLARGE_ORDER = Column(Numeric(20, 4), comment='机构买入单数(单) ')
    SELL_TRADES_EXLARGE_ORDER = Column(Numeric(20, 4), comment='机构卖出单数(单) ')
    BUY_TRADES_LARGE_ORDER = Column(Numeric(20, 4), comment='大户买入单数(单) ')
    SELL_TRADES_LARGE_ORDER = Column(Numeric(20, 4), comment='大户卖出单数(单) ')
    BUY_TRADES_MED_ORDER = Column(Numeric(20, 4), comment='中户买入单数(单) ')
    SELL_TRADES_MED_ORDER = Column(Numeric(20, 4), comment='中户卖出单数(单) ')
    BUY_TRADES_SMALL_ORDER = Column(Numeric(20, 4), comment='散户买入单数(单) ')
    SELL_TRADES_SMALL_ORDER = Column(Numeric(20, 4), comment='散户卖出单数(单) ')
    VOLUME_DIFF_SMALL_TRADER = Column(Numeric(20, 4), comment='散户量差(含主动被动)(手) ')
    VOLUME_DIFF_SMALL_TRADER_ACT = Column(Numeric(20, 4), comment='散户量差(仅主动)(手) ')
    VOLUME_DIFF_MED_TRADER = Column(Numeric(20, 4), comment='中户量差(含主动被动)(手) ')
    VOLUME_DIFF_MED_TRADER_ACT = Column(Numeric(20, 4), comment='中户量差(仅主动)(手) ')
    VOLUME_DIFF_LARGE_TRADER = Column(Numeric(20, 4), comment='大户量差(含主动被动)(手) ')
    VOLUME_DIFF_LARGE_TRADER_ACT = Column(Numeric(20, 4), comment='大户量差(仅主动)(手) ')
    VOLUME_DIFF_INSTITUTE = Column(Numeric(20, 4), comment='机构量差(含主动被动)(手) ')
    VOLUME_DIFF_INSTITUTE_ACT = Column(Numeric(20, 4), comment='机构量差(仅主动)(手) ')
    VALUE_DIFF_SMALL_TRADER = Column(Numeric(20, 4), comment='散户金额差(含主动被动)(万元) ')
    VALUE_DIFF_SMALL_TRADER_ACT = Column(Numeric(20, 4), comment='散户金额差(仅主动)(万元) ')
    VALUE_DIFF_MED_TRADER = Column(Numeric(20, 4), comment='中户金额差(含主动被动)(万元) ')
    VALUE_DIFF_MED_TRADER_ACT = Column(Numeric(20, 4), comment='中户金额差(仅主动)(万元) ')
    VALUE_DIFF_LARGE_TRADER = Column(Numeric(20, 4), comment='大户金额差(含主动被动)(万元) ')
    VALUE_DIFF_LARGE_TRADER_ACT = Column(Numeric(20, 4), comment='大户金额差(仅主动)(万元) ')
    VALUE_DIFF_INSTITUTE = Column(Numeric(20, 4), comment='机构金额差(含主动被动)(万元) ')
    VALUE_DIFF_INSTITUTE_ACT = Column(Numeric(20, 4), comment='机构金额差(仅主动)(万元) ')
    S_MFD_INFLOWVOLUME = Column(Numeric(20, 4), comment='净流入量(手) ')
    NET_INFLOW_RATE_VOLUME = Column(Numeric(20, 4), comment='流入率(量)(%) ')
    S_MFD_INFLOW_OPENVOLUME = Column(Numeric(20, 4), comment='开盘资金流入量(手) ')
    OPEN_NET_INFLOW_RATE_VOLUME = Column(Numeric(20, 4), comment='开盘资金流入率(量)(%) ')
    S_MFD_INFLOW_CLOSEVOLUME = Column(Numeric(20, 4), comment='尾盘资金流入量(手) ')
    CLOSE_NET_INFLOW_RATE_VOLUME = Column(Numeric(20, 4), comment='尾盘资金流入率(量)(%) ')
    S_MFD_INFLOW = Column(Numeric(20, 4), comment='净流入金额(万元) ')
    NET_INFLOW_RATE_VALUE = Column(Numeric(20, 4), comment='流入率(金额)')
    S_MFD_INFLOW_OPEN = Column(Numeric(20, 4), comment='开盘资金流入金额(万元) ')
    OPEN_NET_INFLOW_RATE_VALUE = Column(Numeric(20, 4), comment='开盘资金流入率(金额)')
    S_MFD_INFLOW_CLOSE = Column(Numeric(20, 4), comment='尾盘资金流入金额(万元) ')
    CLOSE_NET_INFLOW_RATE_VALUE = Column(Numeric(20, 4), comment='尾盘资金流入率(金额)')
    TOT_VOLUME_BID = Column(Numeric(20, 4), comment='委买总量(手) ')
    TOT_VOLUME_ASK = Column(Numeric(20, 4), comment='委卖总量(手) ')
    MONEYFLOW_PCT_VOLUME = Column(Numeric(20, 4), comment='资金流向占比(量)(%) ')
    OPEN_MONEYFLOW_PCT_VOLUME = Column(Numeric(20, 4), comment='开盘资金流向占比(量)(%) ')
    CLOSE_MONEYFLOW_PCT_VOLUME = Column(Numeric(20, 4), comment='尾盘资金流向占比(量)(%) ')
    MONEYFLOW_PCT_VALUE = Column(Numeric(20, 4), comment='资金流向占比(金额)')
    OPEN_MONEYFLOW_PCT_VALUE = Column(Numeric(20, 4), comment='开盘资金流向占比(金额)')
    CLOSE_MONEYFLOW_PCT_VALUE = Column(Numeric(20, 4), comment='尾盘资金流向占比(金额)')
    S_MFD_INFLOWVOLUME_LARGE_ORDER = Column(Numeric(20, 4), comment='大单净流入量(手)')
    NET_INFLOW_RATE_VOLUME_L = Column(Numeric(20, 6), comment='大单流入率(量)(%)')
    S_MFD_INFLOW_LARGE_ORDER = Column(Numeric(20, 4), comment='大单净流入金额(万元)')
    NET_INFLOW_RATE_VALUE_L = Column(Numeric(20, 6), comment='[内部]大单流入率(金额)(%)')
    MONEYFLOW_PCT_VOLUME_L = Column(Numeric(20, 6), comment='大单资金流向占比(量)(%)')
    MONEYFLOW_PCT_VALUE_L = Column(Numeric(20, 6), comment='[内部]大单资金流向占比(金额)(%)')
    S_MFD_INFLOW_OPENVOLUME_L = Column(Numeric(20, 4), comment='大单开盘资金流入量(手)')
    OPEN_NET_INFLOW_RATE_VOLUME_L = Column(Numeric(20, 6), comment='[内部]大单开盘资金流入率(量)(%)')
    S_MFD_INFLOW_OPEN_LARGE_ORDER = Column(Numeric(20, 4), comment='大单开盘资金流入金额(万元)')
    OPEN_NET_INFLOW_RATE_VALUE_L = Column(Numeric(20, 6), comment='[内部]大单开盘资金流入率(金额)(%)')
    OPEN_MONEYFLOW_PCT_VOLUME_L = Column(Numeric(20, 6), comment='[内部]大单开盘资金流向占比(量)(%)')
    OPEN_MONEYFLOW_PCT_VALUE_L = Column(Numeric(20, 6), comment='大单开盘资金流向占比(金额)(%)')
    S_MFD_INFLOW_CLOSEVOLUME_L = Column(Numeric(20, 4), comment='大单尾盘资金流入量(手)')
    CLOSE_NET_INFLOW_RATE_VOLUME_L = Column(Numeric(20, 6), comment='[内部]大单尾盘资金流入率(量)(%)')
    S_MFD_INFLOW_CLOSE_LARGE_ORDER = Column(Numeric(20, 4), comment='大单尾盘资金流入金额(万元)')
    CLOSE_NET_INFLOW_RATE_VALU_L = Column(Numeric(20, 6), comment='[内部]大单尾盘资金流入率(金额)(%)')
    CLOSE_MONEYFLOW_PCT_VOLUME_L = Column(Numeric(20, 6), comment='大单尾盘资金流向占比(量)(%)')
    CLOSE_MONEYFLOW_PCT_VALUE_L = Column(Numeric(20, 6), comment='[内部]大单尾盘资金流向占比(金额)(%)')
    BUY_VALUE_EXLARGE_ORDER_ACT = Column(Numeric(20, 4), comment='机构买入金额(仅主动)(万元)')
    SELL_VALUE_EXLARGE_ORDER_ACT = Column(Numeric(20, 4), comment='机构卖出金额(仅主动)(万元)')
    BUY_VALUE_LARGE_ORDER_ACT = Column(Numeric(20, 4), comment='大户买入金额(仅主动)(万元)')
    SELL_VALUE_LARGE_ORDER_ACT = Column(Numeric(20, 4), comment='大户卖出金额(仅主动)(万元)')
    BUY_VALUE_MED_ORDER_ACT = Column(Numeric(20, 4), comment='中户买入金额(仅主动)(万元)')
    SELL_VALUE_MED_ORDER_ACT = Column(Numeric(20, 4), comment='中户卖出金额(仅主动)(万元)')
    BUY_VALUE_SMALL_ORDER_ACT = Column(Numeric(20, 4), comment='散户买入金额(仅主动)(万元)')
    SELL_VALUE_SMALL_ORDER_ACT = Column(Numeric(20, 4), comment='散户卖出金额(仅主动)(万元)')
    BUY_VOLUME_EXLARGE_ORDER_ACT = Column(Numeric(20, 4), comment='机构买入总量(仅主动)(万股)')
    SELL_VOLUME_EXLARGE_ORDER_ACT = Column(Numeric(20, 4), comment='机构卖出总量(仅主动)(万股)')
    BUY_VOLUME_LARGE_ORDER_ACT = Column(Numeric(20, 4), comment='大户买入总量(仅主动)(万股)')
    SELL_VOLUME_LARGE_ORDER_ACT = Column(Numeric(20, 4), comment='大户卖出总量(仅主动)(万股)')
    BUY_VOLUME_MED_ORDER_ACT = Column(Numeric(20, 4), comment='中户买入总量(仅主动)(万股)')
    SELL_VOLUME_MED_ORDER_ACT = Column(Numeric(20, 4), comment='中户卖出总量(仅主动)(万股)')
    BUY_VOLUME_SMALL_ORDER_ACT = Column(Numeric(20, 4), comment='散户买入总量(仅主动)(万股)')
    SELL_VOLUME_SMALL_ORDER_ACT = Column(Numeric(20, 4), comment='散户卖出总量(仅主动)(万股)')


class ASHAREMONTHLYREPORTSOFBROKERS(Base):
    """中国券商月报"""
    __tablename__ = 'ASHAREMONTHLYREPORTSOFBROKERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPECODE = Column(Numeric(9, 0), comment='报表类型代码')
    ACC_STA_CODE = Column(Numeric(1, 0), comment='原始报表采用会计准则代码')
    IFLISTED_DATA = Column(Numeric(5, 0), comment='是否上市后数据')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入')
    NET_PROFIT_INCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(含少数股东权益)')
    NET_PROFIT_EXCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(不含少数股东权益)')
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(不含少数股东权益)')
    TOT_SHRHLDR_EQY_INCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(含少数股东权益)')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')


class ASHAREMONTHLYYIELD(Base):
    """中国A股月收益率"""
    __tablename__ = 'ASHAREMONTHLYYIELD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='截至日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_MQ_PCTCHANGE = Column(Numeric(20, 4), comment='月收益率(%)')
    S_MQ_TURN = Column(Numeric(20, 4), comment='月换手率(合计)(%)')
    S_MQ_AVGTURN = Column(Numeric(20, 4), comment='月换手率(算术平均)(%)')
    S_MQ_AMOUNT = Column(Numeric(20, 4), comment='月成交金额(万元)')
    S_RISK_BETAR24 = Column(Numeric(20, 4), comment='BETA(24月)')
    S_RISK_BETAR60 = Column(Numeric(20, 4), comment='BETA (60月)')
    S_MQ_VARPCTCHANGE24 = Column(Numeric(20, 4), comment='月收益率方差(24月)')
    S_MQ_DEVPCTCHANGE24 = Column(Numeric(20, 4), comment='月收益率标准差(24月)')
    S_MQ_AVGPCTCHANGE24 = Column(Numeric(20, 4), comment='月收益率平均值(24月)')
    S_MQ_VARPCTCHANGE60 = Column(Numeric(20, 4), comment='月收益率方差(60月)')
    S_MQ_DEVPCTCHANGE60 = Column(Numeric(20, 4), comment='月收益率标准差(60月)')
    S_MQ_AVGPCTCHANGE60 = Column(Numeric(20, 4), comment='月收益率平均值(60月)')


class ASHAREMSCIMEMBERS(Base):
    """None"""
    __tablename__ = 'ASHAREMSCIMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class ASHARENEINDUSTRIESCLASS(Base):
    """中国A股国民经济行业分类"""
    __tablename__ = 'ASHARENEINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    NE_IND_CODE = Column(VARCHAR(50), comment='国民经济行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHARENONCURRENTLIABILITIES1Y(Base):
    """中国A股财务附注--一年内到期的非流动负债"""
    __tablename__ = 'ASHARENONCURRENTLIABILITIES1Y'
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


class ASHARENONOPEREXP(Base):
    """中国A股财务附注--营业外支出"""
    __tablename__ = 'ASHARENONOPEREXP'
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


class ASHARENONOPERREV(Base):
    """中国A股财务附注--营业外收入"""
    __tablename__ = 'ASHARENONOPERREV'
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


class ASHARENONPROFITLOSS(Base):
    """中国A股非经常性损益"""
    __tablename__ = 'ASHARENONPROFITLOSS'
    __table_args__ = (
        Index('IDX_ASHARENONPROFITLOSS_ANN_DT', 'ANN_DT'),)
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
    FAIRVALUE_CHANGE_GAINS_LOSSES = Column(Numeric(20, 4),
                                           comment='持有(或处置)交易性金融资产和负债产生的公允价值变动损益')
    PROVISION_IMPAIRMENT_REVERSED = Column(Numeric(20, 4), comment='单独进行监制测试的应收款项减值准备转回')
    PROCEEDS_LOAN = Column(Numeric(20, 4), comment='对外委托贷款取得的收益')
    CHANGES_REAL_ESTATE_VALUE = Column(Numeric(20, 4), comment='公允价值法计量的投资性房地产价值变动损益')
    PROFIT_LOSS_ADJUSTMENT = Column(Numeric(20, 4), comment='法规要求一次性损益调整影响')
    CUSTODY_FEE_INCOME = Column(Numeric(20, 4), comment='受托经营取得的托管费收入')
    IS_PUBLISHED = Column(Numeric(1, 0), comment='是否公布')


class ASHARENOTESPAYABLE(Base):
    """中国A股财务附注--应付票据"""
    __tablename__ = 'ASHARENOTESPAYABLE'
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


class ASHARENOTESRECEIVABLE(Base):
    """中国A股财务附注--应收票据"""
    __tablename__ = 'ASHARENOTESRECEIVABLE'
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


class ASHAREOFFERFOROFFER(Base):
    """中国A股要约收购"""
    __tablename__ = 'ASHAREOFFERFOROFFER'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='被要约收购公司id')
    ACQUIRER_NAME = Column(VARCHAR(100), comment='收购人名称')
    IS_PRIVATIZATION = Column(Numeric(5, 0), comment='是否属于私有化')
    START_DATE = Column(VARCHAR(8), comment='要约起始日期')
    END_DATE = Column(VARCHAR(8), comment='要约终止日期')
    CIRCULATION_STOCK_NUM = Column(Numeric(20, 4), comment='预定收购流通股数量(万股)')
    CIRCULATION_STOCK_PROPORTION = Column(Numeric(20, 4), comment='预定收购流通股数量占总股本比例(%)')
    PURCHASING_PRICE = Column(Numeric(20, 4), comment='流通股每股收购价格')
    CONV_CODE = Column(VARCHAR(10), comment='流通股股东申报代码')
    RESTRICTED_STOCK_NUM = Column(Numeric(20, 4), comment='预定收购非流通股(限售流通股)数量(万股)')
    RESTRICTED_STOCK_PROPORTION = Column(Numeric(20, 4), comment='预定收购非流通股(限售流通股)数量占总股本比例(%)')
    RESTRICTED_PURCHASING_PRICE = Column(Numeric(20, 4), comment='非流通股(限售流通股)每股收购价格')
    RESTRICTED_CONV_CODE = Column(VARCHAR(10), comment='非流通股(限售流通股)股东申报代码')
    TOTAL_AMOUNT_FUNDS = Column(Numeric(20, 4), comment='预定收购资金总额(万元)')
    PAYMENT_METHOD = Column(VARCHAR(20), comment='支付方式')
    CIRCULATION_STOCK_NUM1 = Column(Numeric(20, 4), comment='实际收购流通股数量(万股)')
    TOTAL_AMOUNT_FUNDS1 = Column(Numeric(20, 4), comment='实际收购资金总额(万元)')
    OFFER_FOR_OFFER = Column(VARCHAR(200), comment='要约收购目的')
    EFFECTIVE_CONDITIONS = Column(VARCHAR(400), comment='要约收购生效条件')
    PRICE_DESCRIPTION = Column(VARCHAR(1000), comment='要约收购价格说明')
    FINANCIALADVISOR = Column(VARCHAR(80), comment='财务顾问')
    S_PROFITNOTICE_FIRSTANNDATE = Column(VARCHAR(8), comment='首次公告日')
    S_PROFITNOTICE_DATE = Column(VARCHAR(8), comment='要约收购书公告日')
    S_RESULT_BULLETIN_DAY = Column(VARCHAR(8), comment='要约收购结果公告日')
    NANN_DATE = Column(VARCHAR(8), comment='最新公告日期')
    SHAREHOLDING_RATIO = Column(Numeric(20, 4), comment='要约收购书公告日收购人持股比例(%)')
    NEW_SHAREHOLDING_RATIO = Column(Numeric(20, 4), comment='要约期满收购人持股比例(%)')
    CIRCULATION_STOCK_RATIO = Column(Numeric(20, 4), comment='实际收购流通股数量占总股本比例(%)')
    RESTRICTED_STOCK_NUM1 = Column(Numeric(20, 4), comment='实际收购非流通股(限售流通股)数量(万股)')
    RESTRICTED_STOCK_RATIO = Column(Numeric(20, 4), comment='实际收购非流通股(限售流通股)数量占总股本比例(%)')
    CAPITAL_DESCRIPTION = Column(VARCHAR(500), comment='要约收购资金说明')
    OFFER_CODE = Column(Numeric(9, 0), comment='要约方式代码')
    EVENT_ID = Column(VARCHAR(20), comment='并购事件ID')


class ASHAREOPERATIONEVENT(Base):
    """中国A股运营事件"""
    __tablename__ = 'ASHAREOPERATIONEVENT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司id')
    SEC_ID = Column(VARCHAR(10), comment='品种ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    EVENT_TYPE = Column(Numeric(9, 0), comment='事件类型')
    EVENT_NAME = Column(VARCHAR(400), comment='事件标题')
    CATTYPE_ID = Column(Numeric(9, 0), comment='品种类别代码')


class ASHAREOPERREVANDCOST(Base):
    """中国A股财务附注--营业收入和营业成本"""
    __tablename__ = 'ASHAREOPERREVANDCOST'
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


class ASHAREOTHERACCOUNTSRECEIVABLE(Base):
    """中国A股其它应收款帐龄结构"""
    __tablename__ = 'ASHAREOTHERACCOUNTSRECEIVABLE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    AGING = Column(VARCHAR(30), comment='帐龄')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')
    OTH_RCV = Column(Numeric(20, 4), comment='金额')
    OTH_RCV_PCT = Column(Numeric(20, 4), comment='比例')
    EXTRA_AMOUNT = Column(Numeric(20, 4), comment='坏帐准备')
    MIN_AGING = Column(Numeric(20, 4), comment='最小帐龄')
    MAX_AGING = Column(Numeric(20, 4), comment='最大帐龄')


class ASHAREOTHERCOMPREHINCOME(Base):
    """中国A股财务附注--其他综合收益"""
    __tablename__ = 'ASHAREOTHERCOMPREHINCOME'
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


class ASHAREOTHERCURRENTASSETS(Base):
    """中国A股财务附注--其他流动资产"""
    __tablename__ = 'ASHAREOTHERCURRENTASSETS'
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


class ASHAREOTHERCURRENTLIABILITIES(Base):
    """中国A股财务附注--其他流动负债"""
    __tablename__ = 'ASHAREOTHERCURRENTLIABILITIES'
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


class ASHAREOTHERDEBTINVESTMENT(Base):
    """中国A股财务附注--其他债权投资"""
    __tablename__ = 'ASHAREOTHERDEBTINVESTMENT'
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


class ASHAREOTHEREQTYINSTRTINVESMT(Base):
    """中国A股财务附注--其他权益工具投资"""
    __tablename__ = 'ASHAREOTHEREQTYINSTRTINVESMT'
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


class ASHAREOTHERINCOME(Base):
    """中国A股财务附注--其他收益"""
    __tablename__ = 'ASHAREOTHERINCOME'
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


class ASHAREOTHERNONCURRENTASSETS(Base):
    """中国A股财务附注--其他非流动资产"""
    __tablename__ = 'ASHAREOTHERNONCURRENTASSETS'
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


class ASHAREOTHERNONCURRENTLIAB(Base):
    """中国A股财务附注--其他非流动负债"""
    __tablename__ = 'ASHAREOTHERNONCURRENTLIAB'
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


class ASHAREOTHERPAYABLES(Base):
    """中国A股财务附注--其他应付款"""
    __tablename__ = 'ASHAREOTHERPAYABLES'
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


class ASHAREOTHERRECEIVABLES(Base):
    """中国A股其它应收款大股东欠款"""
    __tablename__ = 'ASHAREOTHERRECEIVABLES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    DEBTOR_NAME = Column(VARCHAR(100), comment='债务人名称')
    ARREARS = Column(Numeric(20, 4), comment='金额')
    OTH_RCV_PCT = Column(Numeric(20, 4), comment='比例(%)')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')


class ASHAREOWNERSHIP(Base):
    """中国A股企业所有制板块"""
    __tablename__ = 'ASHAREOWNERSHIP'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    WIND_SEC_CODE = Column(VARCHAR(10), comment='板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class ASHAREOWNERSHIPZL(Base):
    """中国A股企业所有制板块(增量)"""
    __tablename__ = 'ASHAREOWNERSHIPZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    WIND_SEC_CODE = Column(VARCHAR(10), comment='板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class ASHAREPEVCINVESTMENT(Base):
    """中国A股PEVC投资机构"""
    __tablename__ = 'ASHAREPEVCINVESTMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='股东公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='股东公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='股东公司ID')
    S_HOLDER_DATE = Column(VARCHAR(8), comment='融资时间')
    S_HOLDER_PCT = Column(Numeric(12, 4), comment='股权比例')


class ASHAREPLACEMENTDETAILS(Base):
    """中国A股网下配售机构获配明细"""
    __tablename__ = 'ASHAREPLACEMENTDETAILS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_HOLDER_NAME = Column(VARCHAR(200), comment='股东名称')
    S_HOLDER_TYPECODE = Column(Numeric(9, 0), comment='股东类型代码')
    S_HOLDER_TYPE = Column(VARCHAR(20), comment='股东类型')
    TYPEOFINVESTOR = Column(VARCHAR(20), comment='法人投资者类型')
    ORDQTY = Column(Numeric(20, 4), comment='有效报价的申购数量(股)')
    PLACEMENT = Column(Numeric(20, 4), comment='获配数量(股)')
    TRADE_DT = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    LOCKMONTH = Column(Numeric(20, 4), comment='锁定期(月)')
    TRADABLE_DT = Column(VARCHAR(8), comment='可流通日期')
    ANN_ORDQTY = Column(Numeric(20, 4), comment='有效报价的申购数量(股)')
    IS_SEOORIPO = Column(Numeric(1, 0), comment='是否增发或首发')
    LATEST_OWN_QTY = Column(Numeric(20, 4), comment='最新持股数量(万股/万张)')
    PLACEMENT_FINANCING = Column(Numeric(20, 4), comment='获配数量(配套融资)')
    PLACEMENT_CURRENCY = Column(Numeric(20, 4), comment='获配数量(货币认购)(万股)')
    PLACEMENT_NON_CURRENCY = Column(Numeric(20, 4), comment='获配数量(非货币认购)')
    MEETEVENT_ID = Column(VARCHAR(40), comment='融资事件ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='股东ID')


class ASHAREPLACEMENTINFO(Base):
    """中国A股网下配售机构获配统计"""
    __tablename__ = 'ASHAREPLACEMENTINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='公告日期')
    PCT_CHANGE_1D = Column(Numeric(9, 0), comment='投资者类型代码')
    PCT_CHANGE_1W = Column(Numeric(20, 8), comment='网下中签率')
    PCT_CHANGE_1M = Column(Numeric(20, 4), comment='配售数量')
    VOLUME_W = Column(Numeric(20, 4), comment='申购数量')
    VOLUME_M = Column(Numeric(20, 4), comment='配售数量占比')
    AMOUNT_W = Column(Numeric(20, 4), comment='有效申购数量占比')


class ASHAREPLAINTIFF(Base):
    """中国A股公司诉讼-原告"""
    __tablename__ = 'ASHAREPLAINTIFF'
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


class ASHAREPLEDGEPROPORTION(Base):
    """中国A股股票质押比例"""
    __tablename__ = 'ASHAREPLEDGEPROPORTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_PLEDGE_NUM = Column(Numeric(20, 0), comment='质押笔数')
    S_SHARE_UNRESTRICTED_NUM = Column(Numeric(20, 4), comment='无限售股份质押数量')
    S_SHARE_RESTRICTED_NUM = Column(Numeric(20, 4), comment='有限售股份质押数量')
    S_TOT_SHR = Column(Numeric(20, 4), comment='A股总股本')
    S_PLEDGE_RATIO = Column(Numeric(20, 4), comment='质押比例')


class ASHAREPLEDGETRADE(Base):
    """中国A股质押日交易明细"""
    __tablename__ = 'ASHAREPLEDGETRADE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    INITIAL_NUM = Column(Numeric(20, 4), comment='初始交易数量')
    REPURCHASE_NUM = Column(Numeric(20, 4), comment='购回交易数量')
    REPURCHASE_ALLOWANCE = Column(Numeric(20, 4), comment='待购回余量')
    REPURCHASE_ALLOWANCE1 = Column(Numeric(20, 4), comment='待购回余量(无限售条件)')
    REPURCHASE_ALLOWANCE2 = Column(Numeric(20, 4), comment='待购回余量(有限售条件)')


class ASHAREPOVERTYALLEVIATIONDATA(Base):
    """中国A股公司扶贫情况统计"""
    __tablename__ = 'ASHAREPOVERTYALLEVIATIONDATA'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    AMOUNT_POVERTY_ALLEVIATION = Column(Numeric(20, 4), comment='精准扶贫发生额')
    AMOUNT_ANTIPY_DONATION = Column(Numeric(20, 4), comment='扶贫捐款发生额')
    AMOUNT_TARGET_LOAN = Column(Numeric(20, 4), comment='精准贷款发生额')
    AMOUNT_PERSONAL_ANTIPY_LOAN = Column(Numeric(20, 4), comment='个人扶贫贷款发生额')
    AMOUNT_COMP_ANTIPY_LOAN = Column(Numeric(20, 4), comment='企业扶贫贷款发生额')
    AMOUNT_COMP_ANTIPY_FUNDS = Column(Numeric(20, 4), comment='扶贫资金发生额')
    AMOUNT_BORW_FUNDS_DEMO = Column(Numeric(20, 4), comment='物质拆款发生额')
    AMOUNT_INDUSTRY_DEVELOPMENT = Column(Numeric(20, 4), comment='产业发展脱贫发生额')
    AMOUNT_TRANSFER_EMPLOYMENT = Column(Numeric(20, 4), comment='转移就业脱贫发生额')
    AMOUNT_ANTIPY_RELOCATION = Column(Numeric(20, 4), comment='异地搬迁脱贫发生额')
    AMOUNT_ANTIPY_EDUCATION = Column(Numeric(20, 4), comment='教育扶贫发生额')
    AMOUNT_ANTIPY_HEALTH = Column(Numeric(20, 4), comment='健康扶贫发生额')
    AMOUNT_ECOLOGICAL_ANTIPY = Column(Numeric(20, 4), comment='生态保护扶贫发生额')
    AMOUNT_SOCIAL_ASSISTANCE = Column(Numeric(20, 4), comment='兜底保障发生额')
    AMOUNT_SOCIAL_ANTIPY = Column(Numeric(20, 4), comment='社会扶贫发生额')
    AMOUNT_INFRASTRUCTURE_ANTIPY = Column(Numeric(20, 4), comment='基础设施扶贫发生额')
    AMOUNT_CULTURAL_ANTIPY = Column(Numeric(20, 4), comment='文化扶贫发生额')
    AMOUNT_LIVELIHOOD_ANTIPY = Column(Numeric(20, 4), comment='民生项目发生额')
    AMOUNT_OTHERPROJECT_ANTIPY = Column(Numeric(20, 4), comment='其他项目发生额')
    TARGETED_ANTIPY_BALANCE = Column(Numeric(20, 4), comment='精准贷款余额')
    PER_ANTIPY_LOAN_BALANCE = Column(Numeric(20, 4), comment='个人扶贫贷款余额')
    COMP_ANTIPY_LOAN_BALANCE = Column(Numeric(20, 4), comment='企业扶贫贷款余额')


class ASHAREPREVIOUSENNAME(Base):
    """中国A股证券曾用英文名"""
    __tablename__ = 'ASHAREPREVIOUSENNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID ')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(10), comment='证券id ')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    S_INFO_ENAME = Column(VARCHAR(100), comment='英文简称 ')
    CUR_SIGN = Column(Numeric(1, 0), comment='是否最新 ')


class ASHAREPREVIOUSNAME(Base):
    """中国A股证券曾用名"""
    __tablename__ = 'ASHAREPREVIOUSNAME'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截至日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券简称')
    CHANGEREASON = Column(Numeric(9, 0), comment='变动原因代码')


class ASHAREPRODUCT(Base):
    """中国A股公司产品"""
    __tablename__ = 'ASHAREPRODUCT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')
    S_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_PRODUCT_NAME = Column(VARCHAR(100), comment='产品名称')
    S_PRODUCT_NUMBER = Column(Numeric(20, 4), comment='数量')
    NUMBER_TYPECODE = Column(Numeric(9, 0), comment='数量类型代码')
    FREQUENCY_CODE = Column(Numeric(9, 0), comment='频率代码')


class ASHAREPROFITEXPRESS(Base):
    """中国A股业绩快报"""
    __tablename__ = 'ASHAREPROFITEXPRESS'
    __table_args__ = (
        Index('IDX_ASHAREPROFITEXPRESS_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入(元)')
    OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润(元)')
    TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额(元)')
    NET_PROFIT_EXCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(元)')
    TOT_ASSETS = Column(Numeric(20, 4), comment='总资产(元)')
    TOT_SHRHLDR_EQY_EXCL_MIN_INT = Column(Numeric(20, 4), comment='股东权益合计(不含少数股东权益)(元)')
    EPS_DILUTED = Column(Numeric(20, 4), comment='每股收益(摊薄)(元)')
    ROE_DILUTED = Column(Numeric(20, 4), comment='净资产收益率(摊薄)(%)')
    S_ISAUDIT = Column(Numeric(5, 0), comment='是否审计')
    YOYNET_PROFIT_EXCL_MIN_INT_INC = Column(Numeric(20, 4), comment='去年同期修正后净利润')
    BRIEF_PERFORMANCE = Column(VARCHAR(2500), comment='业绩简要说明')
    MEMO = Column(VARCHAR(400), comment='备注')
    S_FA_BPS = Column(Numeric(20, 4), comment='每股净资产')
    S_FA_YOYSALES = Column(Numeric(20, 4), comment='同比增长率:营业收入')
    S_FA_YOYOP = Column(Numeric(20, 4), comment='同比增长率:营业利润')
    S_FA_YOYEBT = Column(Numeric(20, 4), comment='同比增长率:利润总额')
    S_FA_YOYNETPROFIT_DEDUCTED = Column(Numeric(20, 4), comment='同比增长率:归属母公司股东的净利润')
    S_FA_YOYEPS_BASIC = Column(Numeric(20, 4), comment='同比增长率:基本每股收益')
    S_FA_ROE_YEARLY = Column(Numeric(20, 4), comment='同比增减:加权平均净资产收益率')
    S_FA_GROWTH_ASSETS = Column(Numeric(20, 4), comment='比年初增长率:总资产')
    S_FA_YOYEQUITY = Column(Numeric(20, 4), comment='比年初增长率:归属母公司的股东权益')
    GROWTH_BPS_SH = Column(Numeric(20, 4), comment='比年初增长率:归属于母公司股东的每股净资产')
    LAST_YEAR_OPER_REV = Column(Numeric(20, 4), comment='去年同期营业收入')
    LAST_YEAR_OPER_PROFIT = Column(Numeric(20, 4), comment='去年同期营业利润')
    LAST_YEAR_TOT_PROFIT = Column(Numeric(20, 4), comment='去年同期利润总额')
    LAST_YEAR_NET_PROFIT_EXCL_INC = Column(Numeric(20, 4), comment='去年同期净利润')
    LAST_YEAR_EPS_DILUTED = Column(Numeric(20, 4), comment='去年同期每股收益')
    S_EARLY_NET_ASSETS = Column(Numeric(20, 4), comment='期初净资产')
    S_EARLY_BPS = Column(Numeric(20, 4), comment='期初每股净资产')
    ACTUAL_ANN_DT = Column(VARCHAR(8), comment='[内部]实际公告日期')


class ASHAREPROFITNOTICE(Base):
    """中国A股业绩预告"""
    __tablename__ = 'ASHAREPROFITNOTICE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_PROFITNOTICE_DATE = Column(VARCHAR(8), comment='公告日期')
    S_PROFITNOTICE_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_PROFITNOTICE_STYLE = Column(Numeric(9, 0), comment='业绩预告类型代码')
    S_PROFITNOTICE_SIGNCHANGE = Column(VARCHAR(10), comment='是否变脸')
    S_PROFITNOTICE_CHANGEMIN = Column(Numeric(20, 4), comment='预告净利润变动幅度下限（%）')
    S_PROFITNOTICE_CHANGEMAX = Column(Numeric(20, 4), comment='预告净利润变动幅度上限（%）')
    S_PROFITNOTICE_NETPROFITMIN = Column(Numeric(20, 4), comment='预告净利润下限（万元）')
    S_PROFITNOTICE_NETPROFITMAX = Column(Numeric(20, 4), comment='预告净利润上限（万元）')
    S_PROFITNOTICE_NUMBER = Column(Numeric(15, 4), comment='公布次数')
    S_PROFITNOTICE_FIRSTANNDATE = Column(VARCHAR(8), comment='首次公告日')
    S_PROFITNOTICE_ABSTRACT = Column(VARCHAR(200), comment='业绩预告摘要')
    S_PROFITNOTICE_REASON = Column(VARCHAR(2000), comment='业绩变动原因')
    S_PROFITNOTICE_NET_PARENT_FIRM = Column(Numeric(20, 4), comment='上年同期归母净利润')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')


class ASHAREPROSECUTION(Base):
    """中国A股诉讼事件"""
    __tablename__ = 'ASHAREPROSECUTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
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
    RESULT = Column(TEXT(2147483647), comment='判决内容')
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


class ASHAREPROVISIONBADDEBTS(Base):
    """中国A股坏帐准备提取比例"""
    __tablename__ = 'ASHAREPROVISIONBADDEBTS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(40), comment='报表类型')
    AGING = Column(VARCHAR(70), comment='帐龄')
    EXTRACTION_RATIO = Column(Numeric(20, 4), comment='提取比例')
    MIN_AGING = Column(Numeric(20, 4), comment='最小帐龄')
    MAX_AGING = Column(Numeric(20, 4), comment='最大帐龄')


class ASHARERALATEDTRADE(Base):
    """中国A股关联交易"""
    __tablename__ = 'ASHARERALATEDTRADE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_RELATEDTRADE_NAME = Column(VARCHAR(80), comment='B公司名称')
    S_RELATEDTRADE_RELATIONCODE = Column(VARCHAR(300), comment='关联关系')
    S_RELATEDTRADE_CONTROL = Column(Numeric(5, 0), comment='是否存在控制关系')
    S_RELATEDTRADE_TRADETYPE = Column(VARCHAR(300), comment='交易类型')
    S_RELATEDTRADE_SETTLETYPE = Column(VARCHAR(300), comment='结算方式')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_RELATEDTRADE_AMOUNT = Column(VARCHAR(20), comment='交易金额')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')


class ASHARERDEXPENDITURE(Base):
    """中国A股财务附注--研发支出"""
    __tablename__ = 'ASHARERDEXPENDITURE'
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
    ITEM_TYPE_NAME = Column(VARCHAR(100), comment='项目类别名称')


class ASHARERDEXPENSE(Base):
    """中国A股财务附注--研发费用"""
    __tablename__ = 'ASHARERDEXPENSE'
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


class ASHARERECEIVABLES(Base):
    """中国A股应收账款"""
    __tablename__ = 'ASHARERECEIVABLES'
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
    PERIOD = Column(VARCHAR(50), comment='拖欠时间')


class ASHAREREGINV(Base):
    """中国A股立案调查"""
    __tablename__ = 'ASHAREREGINV'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司ID')
    SEC_ID = Column(VARCHAR(10), comment='证券id')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SUR_INSTITUTE = Column(VARCHAR(100), comment='调查机构')
    SUR_REASONS = Column(VARCHAR(500), comment='调查原因')
    STR_ANNDATE = Column(VARCHAR(8), comment='开始公告日期')
    END_ANNDATE = Column(VARCHAR(8), comment='结束公告日期')
    STR_DATE = Column(VARCHAR(8), comment='开始日期')


class ASHAREREGIONAL(Base):
    """中国A股企业地域板块"""
    __tablename__ = 'ASHAREREGIONAL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    WIND_SEC_CODE = Column(VARCHAR(10), comment='板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class ASHAREREGIONALZL(Base):
    """中国A股企业地域板块(增量)"""
    __tablename__ = 'ASHAREREGIONALZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    S_INFO_COMPNAME = Column(VARCHAR(200), comment='公司名称')
    WIND_SEC_CODE = Column(VARCHAR(10), comment='板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class ASHARERELATEDCLAIMSDEBTS(Base):
    """中国A股关联方债权债务往来"""
    __tablename__ = 'ASHARERELATEDCLAIMSDEBTS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    ASSOCIATED_NAME = Column(VARCHAR(100), comment='关联方名称')
    ASSOCIATED_FUNDING_AMOUNT = Column(Numeric(20, 4), comment='向关联方提供资金发生额')
    ASSOCIATED_FUNDING_BALANCE = Column(Numeric(20, 4), comment='向关联方提供资金余额')
    ASHARE_FUNDING_AMOUNT = Column(Numeric(20, 4), comment='关联方向上市公司提供资金发生额')
    ASHARE_FUNDING_BALANCE = Column(Numeric(20, 4), comment='关联方向上市公司提供资金余额')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    CONNECTION_RELATION = Column(VARCHAR(40), comment='关联关系')


class ASHARERELATEDPARTYDEBT(Base):
    """中国A股关联方债务"""
    __tablename__ = 'ASHARERELATEDPARTYDEBT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='债权公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='债权公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='债权公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_AMOUNT = Column(Numeric(20, 4), comment='金额')


class ASHAREREPORTPERIODINDEX(Base):
    """中国A股WIND计算调整后财务指标"""
    __tablename__ = 'ASHAREREPORTPERIODINDEX'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    END_DATE = Column(VARCHAR(8), comment='截止日期')
    S_FT_BPS = Column(Numeric(20, 4), comment='净资产')
    S_BPS_CHANGE_REASON = Column(VARCHAR(10), comment='净资产变动原因')
    S_CAP_RSRV = Column(Numeric(20, 4), comment='资本公积金')
    S_CAP_RSRV_CHANGE_REASON = Column(VARCHAR(10), comment='资本公积金变动原因')
    S_UNDISTRIBUTEDPS = Column(Numeric(20, 4), comment='未分配利润')
    S_CHANGE_REASON = Column(VARCHAR(10), comment='未分配利润变动原因')
    MEMO = Column(VARCHAR(100), comment='备注')


class ASHARERESTRUCTURINGEVENTS(Base):
    """中国A股重大重组事件"""
    __tablename__ = 'ASHARERESTRUCTURINGEVENTS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='万得代码')
    PROGRESS = Column(Numeric(9, 0), comment='重组进度')
    EVENT = Column(VARCHAR(200), comment='重组事件')
    FORM = Column(Numeric(9, 0), comment='重组形式代码')
    PURPOSE = Column(Numeric(9, 0), comment='重组目的代码')
    TYPE = Column(Numeric(9, 0), comment='重组类型代码')
    TRADING_OBJECT = Column(VARCHAR(200), comment='交易标的')
    TRADING_OBJECTCODE = Column(Numeric(9, 0), comment='交易标的类型')
    IS_M_A = Column(Numeric(5, 0), comment='是否并购')
    IS_IMPTRESTRUCTURING = Column(Numeric(5, 0), comment='是否重大资产重组')
    IS_CONTROLCHANGED = Column(Numeric(5, 0), comment='控制权是否变更')
    SHARES_TRADED = Column(Numeric(20, 4), comment='交易股份占比(%)')
    TOTALVALUEDEALS = Column(Numeric(20, 4), comment='交易总价值(万元)')
    BUYERTOPAYCASH = Column(Numeric(20, 4), comment='买方支付现金(万元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PAYMENTMETHOD = Column(Numeric(9, 0), comment='支付方式代码')
    INJECTEDASSETBOOKNET = Column(Numeric(20, 4), comment='注入资产净资产账面值(万元)')
    ASSETINJECTEDASSESSNET = Column(Numeric(20, 4), comment='注入资产净资产评估值(万元)')
    ULTIMATEASSESSMETHOD = Column(Numeric(9, 0), comment='最后采用评估方法')
    BASEDATE = Column(VARCHAR(8), comment='资产评估基准日')
    APPRECIATIONRATE = Column(Numeric(20, 4), comment='增值率')
    INDEPFINAADVISER = Column(VARCHAR(200), comment='独立财务顾问')
    ACQUIRERADVISER = Column(VARCHAR(200), comment='购买方财务顾问')
    SUSPENSIONDATE = Column(VARCHAR(8), comment='重大资产重组停牌日')
    PRELANDATE = Column(VARCHAR(8), comment='预案公告日')
    SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    PASSDATE = Column(VARCHAR(8), comment='发审委通过公告日')
    APPROVEDDATE = Column(VARCHAR(8), comment='证监会核准公告日')
    SEO_DT = Column(VARCHAR(8), comment='增发公告日(交易完成日期)')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日')
    INSTITUTIONLISTED_DT = Column(VARCHAR(8), comment='向机构所持增发上市日期')
    ORIENTATIONSEO_DT = Column(VARCHAR(8), comment='定增股份上市日期')
    ISSUEVOLUME = Column(Numeric(20, 4), comment='增发发行数量(万元)')
    SEO_PRICE = Column(Numeric(20, 4), comment='增发价格(元)')
    SEO_DOWNPRICE = Column(Numeric(20, 4), comment='增发预案价下限(元)')
    BASE_DT_AVGP_20_M = Column(Numeric(20, 4), comment='定价基准日前20日交易均价')
    BASE_DT = Column(VARCHAR(8), comment='定价基准日')
    BASE_DT_TYPE = Column(VARCHAR(10), comment='定价基准日类型')
    ESTIMATEDNETPROFIT = Column(Numeric(20, 4), comment='预测净利润(元)')
    FORECASTYEAR = Column(VARCHAR(10), comment='预测年度')
    ISSUEDSHARESAGO_SEO_M = Column(Numeric(20, 4), comment='重组实施前总股本（万股）')
    ISSUEDSHARESAGO_SEO_A = Column(Numeric(20, 4), comment='重组实施后总股本（万股）')
    FIRST_ANN_DATE = Column(VARCHAR(8), comment='首次披露日期')
    EVENT_ID = Column(VARCHAR(20), comment='并购事件ID')


class ASHARERIGHTISSUE(Base):
    """中国A股配股"""
    __tablename__ = 'ASHARERIGHTISSUE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_RIGHTSISSUE_PROGRESS = Column(VARCHAR(10), comment='方案进度')
    S_RIGHTSISSUE_PRICE = Column(Numeric(20, 4), comment='配股价格(元)')
    S_RIGHTSISSUE_RATIO = Column(Numeric(20, 5), comment='配股比例')
    S_RIGHTSISSUE_AMOUNT = Column(Numeric(20, 4), comment='配股计划数量(万股)')
    S_RIGHTSISSUE_AMOUNTACT = Column(Numeric(20, 4), comment='配股实际数量(万股)')
    S_RIGHTSISSUE_NETCOLLECTION = Column(Numeric(20, 4), comment='募集资金(元)')
    S_RIGHTSISSUE_REGDATESHAREB = Column(VARCHAR(8), comment='股权登记日')
    S_RIGHTSISSUE_EXDIVIDENDDATE = Column(VARCHAR(8), comment='除权日')
    S_RIGHTSISSUE_LISTEDDATE = Column(VARCHAR(8), comment='配股上市日')
    S_RIGHTSISSUE_PAYSTARTDATE = Column(VARCHAR(8), comment='缴款起始日')
    S_RIGHTSISSUE_PAYENDDATE = Column(VARCHAR(8), comment='缴款终止日')
    S_RIGHTSISSUE_PREPLANDATE = Column(VARCHAR(8), comment='预案公告日')
    S_RIGHTSISSUE_SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    S_RIGHTSISSUE_PASSDATE = Column(VARCHAR(8), comment='发审委通过公告日')
    S_RIGHTSISSUE_APPROVEDDATE = Column(VARCHAR(8), comment='证监会核准公告日')
    S_RIGHTSISSUE_ANNCEDATE = Column(VARCHAR(8), comment='配股实施公告日')
    S_RIGHTSISSUE_RESULTDATE = Column(VARCHAR(8), comment='配股结果公告日')
    S_RIGHTSISSUE_LISTANNDATE = Column(VARCHAR(8), comment='上市公告日')
    S_RIGHTSISSUE_GUARANTOR = Column(VARCHAR(8), comment='基准年度')
    S_RIGHTSISSUE_GUARTYPE = Column(Numeric(20, 4), comment='基准股本(万股)')
    S_RIGHTSISSUE_CODE = Column(VARCHAR(10), comment='配售代码')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日期')
    S_RIGHTSISSUE_YEAR = Column(VARCHAR(8), comment='配股年度')
    S_RIGHTSISSUE_CONTENT = Column(VARCHAR(150), comment='配股说明')
    S_RIGHTSISSUE_NAME = Column(VARCHAR(40), comment='配股简称')
    S_RATIO_DENOMINATOR = Column(Numeric(20, 4), comment='配股比例分母')
    S_RATIO_MOLECULAR = Column(Numeric(20, 4), comment='配股比例分子')
    S_SUBSCRIPTION_METHOD = Column(VARCHAR(30), comment='认购方式')
    S_EXPECTED_FUND_RAISING = Column(Numeric(20, 4), comment='预计募集资金(元)')
    S_RIGHTSISSUE_COST = Column(Numeric(20, 4), comment='配售费用')
    S_RIGHTSISSUE_REGDATE_BSHARE = Column(VARCHAR(8), comment='B股股权登记日')
    S_ALLOTMENT_OBJECT = Column(VARCHAR(40), comment='配股对象')
    S_PRICE_CAP = Column(Numeric(20, 4), comment='配股预案价上限')
    S_LOWER_PRICE_LIMIT = Column(Numeric(20, 4), comment='配股预案价下限')
    S_UNDERWRITING_METHOD = Column(VARCHAR(20), comment='承销方式')
    S_UNDERWRITER_SUBSCRIPTION = Column(Numeric(20, 4), comment='承销商余额认购数量(万股)')
    S_STATE_OWNED_SHARE_NUM = Column(Numeric(20, 4), comment='国有股理论配股数量(万股)')
    S_LEGAL_PERSON_SHARE_NUM = Column(Numeric(20, 4), comment='法人股理论配股数量(万股)')
    S_EMPLOYEE_STOCK_SHARE_NUM = Column(Numeric(20, 4), comment='职工股理论配股数量(万股)')
    S_TRANSFER_SHARE_NUM = Column(Numeric(20, 4), comment='转配股理论配股数量(万股)')
    S_CIRCULATED_SHARE_NUM = Column(Numeric(20, 4), comment='已流通股理论配股数量(万股)')
    S_STATE_OWNED_SHARE_NUM1 = Column(Numeric(20, 4), comment='国有股实际配股数量(万股)')
    S_LEGAL_PERSON_SHARE_NUM1 = Column(Numeric(20, 4), comment='法人股实际配股数量(万股)')
    S_EMPLOYEE_STOCK_SHARE_NUM1 = Column(Numeric(20, 4), comment='职工股实际配股数量(万股)')
    S_TRANSFER_SHARE_NUM1 = Column(Numeric(20, 4), comment='转配股实际配股数量(万股)')
    S_CIRCULATED_SHARE_NUM1 = Column(Numeric(20, 4), comment='已流通股实际配股数量(万股)')
    S_HOLDER_HELD_NUMBER = Column(Numeric(20, 4), comment='持股5%以上大股东持股数量(万股)')
    S_HOLDER_SUBSCRIPTION_NUMBER1 = Column(Numeric(20, 4), comment='持股5%以上的大股东理论认购股数量(万股)')
    S_HOLDER_SUBSCRIPTION_NUMBER = Column(Numeric(20, 4), comment='持股5%以上大股东认购股数量(万股)')
    S_HOLDER_SUBSCRIPTION_METHOD = Column(VARCHAR(100), comment='持股5%以上大股东认购方式(万股)')


class ASHARESALEEXPENSE(Base):
    """中国A股财务附注--销售费用明细"""
    __tablename__ = 'ASHARESALEEXPENSE'
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


class ASHARESALESSEGMENT(Base):
    """中国A股主营业务构成"""
    __tablename__ = 'ASHARESALESSEGMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_SEGMENT_ITEMCODE = Column(Numeric(9, 0), comment='项目类别')
    S_SEGMENT_ITEM = Column(VARCHAR(100), comment='主营业务项目')
    S_SEGMENT_SALES = Column(Numeric(20, 4), comment='主营业务收入(元)')
    S_SEGMENT_PROFIT = Column(Numeric(20, 4), comment='主营业务利润(元)')
    S_SEGMENT_COST = Column(Numeric(20, 4), comment='主营业务成本(元)')
    IS_PUBLISHED_VALUE = Column(Numeric(1, 0), comment='是否公布值')
    PCT_SEGMENT_SALES = Column(Numeric(20, 4), comment='主营业务收入占比(%)')
    PCT_SEGMENT_PROFIT = Column(Numeric(20, 4), comment='主营业务利润占比(%)')
    PCT_SEGMENT_COST = Column(Numeric(20, 4), comment='主营业务成本占比(%)')
    INC_SEGMENT_SALES = Column(Numeric(20, 4), comment='主营业务收入同比增长率(%)')
    INC_SEGMENT_PROFIT = Column(Numeric(20, 4), comment='主营业务利润同比增长率(%)')
    INC_SEGMENT_COST = Column(Numeric(20, 4), comment='主营业务成本同比增长率(%)')
    GROSS_PROFIT_MARGIN = Column(Numeric(20, 4), comment='毛利率(%)')
    INC_PROFIT_MARGIN = Column(Numeric(20, 4), comment='毛利率增长率(%)')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    SUBJECT_CODE = Column(VARCHAR(20), comment='科目ID')


class ASHARESALESSEGMENTMAPPING(Base):
    """主营及附注科目对应关系表"""
    __tablename__ = 'ASHARESALESSEGMENTMAPPING'
    MAIN_ACCOUNTS_ID = Column(VARCHAR(20), comment='主科目ID')
    MAIN_ACCOUNTS_NAME = Column(VARCHAR(200), comment='主科目名称')
    SUB_ACCOUNTS_ID = Column(VARCHAR(20), comment='子科目ID')
    SUB_ACCOUNTS_NAME = Column(VARCHAR(200), comment='子科目名称')
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')


class ASHARESELLSUBJECT(Base):
    """中国A股并购出售标的"""
    __tablename__ = 'ASHARESELLSUBJECT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_COMP_NAME = Column(VARCHAR(100), comment='并购公司名称')
    S_INFO_COMP_SNAME = Column(VARCHAR(40), comment='并购公司中文简称')
    S_INFO_COMPCODE1 = Column(VARCHAR(100), comment='并购出售目标公司ID')
    S_INFO_PROGRESS = Column(VARCHAR(300), comment='方案进度')
    S_UPDATE_DATE = Column(VARCHAR(8), comment='最新披露日期')
    S_MEETEVENT_ID = Column(VARCHAR(20), comment='事件ID')
    S_INFO_COMP_NAME1 = Column(VARCHAR(100), comment='并购出售目标公司名称')
    S_INFO_COMP_SNAME1 = Column(VARCHAR(40), comment='并购出售目标公司中文简称')


class ASHARESENSITANALYSIS(Base):
    """中国A股财务附注--敏感性分析"""
    __tablename__ = 'ASHARESENSITANALYSIS'
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


class ASHARESEO(Base):
    """中国A股增发"""
    __tablename__ = 'ASHARESEO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_FELLOW_PROGRESS = Column(Numeric(5, 0), comment='方案进度')
    S_FELLOW_ISSUETYPE = Column(VARCHAR(10), comment='发行方式')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_FELLOW_PRICE = Column(Numeric(20, 4), comment='发行价格(元)')
    S_FELLOW_AMOUNT = Column(Numeric(20, 4), comment='发行数量(万股)')
    S_FELLOW_COLLECTION = Column(Numeric(20, 4), comment='募集资金(元)')
    S_FELLOW_RECORDDATE = Column(VARCHAR(8), comment='股权登记日')
    S_FELLOW_PAYSTARTDATE = Column(VARCHAR(8), comment='缴款起始日期')
    S_FELLOW_PAYENDDATE = Column(VARCHAR(8), comment='缴款截止日期')
    S_FELLOW_SUBDATE = Column(VARCHAR(8), comment='网上申购日')
    S_FELLOW_OTCDATE = Column(VARCHAR(8), comment='网下发行日期')
    S_FELLOW_LISTDATE = Column(VARCHAR(8), comment='向公众增发股份上市日期')
    S_FELLOW_INSTLISTDATE = Column(VARCHAR(8), comment='向机构增发股份上市日期')
    S_FELLOW_CHANGEDATE = Column(VARCHAR(8), comment='定向增发股份变动日期')
    S_FELLOW_ROADSHOWDATE = Column(VARCHAR(8), comment='网上路演日')
    S_FELLOW_REFUNDDATE = Column(VARCHAR(8), comment='网下申购定金退款日或补缴余款日')
    S_FELLOW_UNFROZEDATE = Column(VARCHAR(8), comment='网上申购资金解冻日')
    S_FELLOW_PREPLANDATE = Column(VARCHAR(8), comment='预案公告日')
    S_FELLOW_SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    S_FELLOW_PASSDATE = Column(VARCHAR(8), comment='发审委/上市委通过公告日')
    S_FELLOW_APPROVEDDATE = Column(VARCHAR(10), comment='证监会通过公告日')
    S_FELLOW_ANNCEDATE = Column(VARCHAR(8), comment='上网发行公告日')
    S_FELLOW_RATIOANNCEDATE = Column(VARCHAR(8), comment='网上中签率公告日')
    S_FELLOW_OFFERINGDATE = Column(VARCHAR(8), comment='增发公告日')
    S_FELLOW_LISTANNDATE = Column(VARCHAR(8), comment='上市公告日')
    S_FELLOW_OFFERINGOBJECT = Column(VARCHAR(200), comment='发行对象')
    S_FELLOW_PRICEUPLIMIT = Column(Numeric(20, 4), comment='增发预案价上限')
    S_FELLOW_PRICEDOWNLIMIT = Column(Numeric(20, 4), comment='增发预案价下限')
    S_SEO_CODE = Column(VARCHAR(10), comment='增发代码')
    S_SEO_NAME = Column(VARCHAR(20), comment='增发简称')
    S_SEO_PE = Column(Numeric(20, 4), comment='发行市盈率(摊薄)')
    S_SEO_AMTBYPLACING = Column(Numeric(20, 4), comment='上网发行数量(万股)')
    S_SEO_AMTTOJUR = Column(Numeric(20, 4), comment='网下发行数量(万股)')
    S_SEO_HOLDERSUBSMODE = Column(VARCHAR(30), comment='大股东认购方式')
    S_SEO_HOLDERSUBSRATE = Column(Numeric(20, 4), comment='大股东认购比例(%)')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日期')
    PRICINGMODE = Column(Numeric(9, 0), comment='定向增发定价方式代码')
    S_FELLOW_ORGPRICEMIN = Column(Numeric(20, 4), comment='原始预案价下限')
    S_FELLOW_DISCNTRATIO = Column(Numeric(20, 4), comment='折扣率')
    S_FELLOW_DATE = Column(VARCHAR(8), comment='定增发行日期')
    S_FELLOW_SUBINVITATIONDT = Column(VARCHAR(8), comment='认购邀请书日')
    S_FELLOW_YEAR = Column(VARCHAR(8), comment='增发年度')
    S_FELLOW_OBJECTIVE_CODE = Column(Numeric(9, 0), comment='定向增发目的代码')
    PRICINGDATE = Column(VARCHAR(8), comment='定价基准日')
    IS_NO_PUBLIC = Column(Numeric(5, 0), comment='是否属于非公开发行')
    EXPENSE = Column(Numeric(20, 4), comment='发行费用(元)')
    S_RIGHTSISSUE_EXDIVIDENDDATE = Column(VARCHAR(8), comment='除权日')
    IS_EXDIVIDEND = Column(Numeric(1, 0), comment='是否除权')
    SUB_MODE = Column(Numeric(9, 0), comment='定增认购方式代码')
    OLDSPLA_MOLE = Column(Numeric(20, 4), comment='老股东配售比例分子')
    OLDSPLA_MODE = Column(VARCHAR(10), comment='老股东配售代码')
    EXP_COLLECTION = Column(Numeric(20, 4), comment='预计募集资金(元)')
    S_FELLOW_TYPE = Column(VARCHAR(100), comment='增发类型')
    S_FELLOW_OBJECTIVE = Column(VARCHAR, comment='增发目的说明')
    S_FELLOW_OFFERINGOBJECT_DES = Column(VARCHAR(2000), comment='发行对象说明')
    EVENT_ID = Column(VARCHAR(40), comment='事件ID')
    PRICE_CONDITION = Column(VARCHAR(2000), comment='价格制定依据')
    PRICE_DT_TYPE = Column(VARCHAR(100), comment='定价基准日类型')
    ORGPRICE_PCT = Column(Numeric(20, 4), comment='预案价格相对基准价格比例(%)')
    ACTPRICE_PCT = Column(Numeric(20, 4), comment='实施价格相对基准价格比例(%)')
    APPRVBYSASSC_DT = Column(VARCHAR(8), comment='国资委批准公告日期')
    S_FELLOW_INITIAL_PLAN = Column(VARCHAR(8), comment='初始预案公告日')
    LEADUNDERWRITER = Column(VARCHAR(500), comment='主承销商')
    CURRENCY_SUBSCRIPTION_NUM = Column(Numeric(20, 4), comment='货币认购数量(万股)')
    NON_MONETARY_SUBSCRIPTION_NUM = Column(Numeric(20, 4), comment='非货币认购数量(元)')
    CURRENCY_SUBSCRIPTION_AMOUNT = Column(Numeric(20, 4), comment='货币认购金额(万股)')
    NOCURRENCY_SUBSCRIPTION_AMOUNT = Column(Numeric(20, 4), comment='非货币认购金额(元)')
    IS_CONTAIN_HOLDER = Column(Numeric(20, 4), comment='发行对象是否包含控股股东')
    OLDSPLA_DENOMINATOR = Column(Numeric(20, 4), comment='老股东配售比例分母')
    NUM_SHARES_PREAONLINE = Column(Numeric(20, 4), comment='网上向老股东优先配售数量(万股)')
    SHARE_RECORDDATE = Column(VARCHAR(8), comment='股份登记日（定向）')


class ASHARESEOBT(Base):
    """中国A股增发(回测)"""
    __tablename__ = 'ASHARESEOBT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    LATEST_OBJECT_ID = Column(VARCHAR(100), comment='最新对象ID')
    BACKREASON_CODE = Column(VARCHAR(2), comment='修改原因代码')
    BACKTIME = Column(DateTime, comment='修改时间')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_FELLOW_PROGRESS = Column(Numeric(5, 0), comment='方案进度')
    S_FELLOW_ISSUETYPE = Column(VARCHAR(10), comment='发行方式')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_FELLOW_PRICE = Column(Numeric(20, 4), comment='发行价格(元)')
    S_FELLOW_AMOUNT = Column(Numeric(20, 4), comment='发行数量(万股)')
    S_FELLOW_COLLECTION = Column(Numeric(20, 4), comment='募集资金(元)')
    S_FELLOW_RECORDDATE = Column(VARCHAR(8), comment='股权登记日')
    S_FELLOW_PAYSTARTDATE = Column(VARCHAR(8), comment='向老股东配售(或优先配售)缴款起始日')
    S_FELLOW_PAYENDDATE = Column(VARCHAR(8), comment='向老股东配售(或优先配售)缴款终止日')
    S_FELLOW_SUBDATE = Column(VARCHAR(8), comment='网上申购日')
    S_FELLOW_OTCDATE = Column(VARCHAR(8), comment='股份登记(定向) 日期')
    S_FELLOW_LISTDATE = Column(VARCHAR(8), comment='向公众增发股份上市日期')
    S_FELLOW_INSTLISTDATE = Column(VARCHAR(8), comment='向机构增发股份上市日期')
    S_FELLOW_CHANGEDATE = Column(VARCHAR(8), comment='定向增发股份变动日期')
    S_FELLOW_ROADSHOWDATE = Column(VARCHAR(8), comment='网上路演日')
    S_FELLOW_REFUNDDATE = Column(VARCHAR(8), comment='网下申购资金(定金)退款日')
    S_FELLOW_UNFROZEDATE = Column(VARCHAR(8), comment='网上申购资金解冻日')
    S_FELLOW_PREPLANDATE = Column(VARCHAR(8), comment='预案公告日')
    S_FELLOW_SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    S_FELLOW_PASSDATE = Column(VARCHAR(8), comment='发审委通过公告日')
    S_FELLOW_APPROVEDDATE = Column(VARCHAR(10), comment='证监会核准公告日')
    S_FELLOW_ANNCEDATE = Column(VARCHAR(8), comment='上网发行公告日')
    S_FELLOW_RATIOANNCEDATE = Column(VARCHAR(8), comment='网上中签率公告日')
    S_FELLOW_OFFERINGDATE = Column(VARCHAR(8), comment='增发公告日')
    S_FELLOW_LISTANNDATE = Column(VARCHAR(8), comment='上市公告日')
    S_FELLOW_OFFERINGOBJECT = Column(VARCHAR(200), comment='发行对象')
    S_FELLOW_PRICEUPLIMIT = Column(Numeric(20, 4), comment='增发预案价上限')
    S_FELLOW_PRICEDOWNLIMIT = Column(Numeric(20, 4), comment='增发预案价下限')
    S_SEO_CODE = Column(VARCHAR(10), comment='增发代码')
    S_SEO_NAME = Column(VARCHAR(20), comment='增发简称')
    S_SEO_PE = Column(Numeric(20, 4), comment='发行市盈率(摊薄)')
    S_SEO_AMTBYPLACING = Column(Numeric(20, 4), comment='上网发行数量(万股)')
    S_SEO_AMTTOJUR = Column(Numeric(20, 4), comment='网下发行数量(万股)')
    S_SEO_HOLDERSUBSMODE = Column(VARCHAR(30), comment='大股东认购方式')
    S_SEO_HOLDERSUBSRATE = Column(Numeric(20, 4), comment='大股东认购比例(%)')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日期')
    PRICINGMODE = Column(Numeric(9, 0), comment='定向增发定价方式代码')
    S_FELLOW_ORGPRICEMIN = Column(Numeric(20, 4), comment='原始预案价下限')
    S_FELLOW_DISCNTRATIO = Column(Numeric(20, 4), comment='折扣率')
    S_FELLOW_DATE = Column(VARCHAR(8), comment='定增发行日期')
    S_FELLOW_SUBINVITATIONDT = Column(VARCHAR(8), comment='认购邀请书日')
    S_FELLOW_YEAR = Column(VARCHAR(8), comment='增发年度')
    S_FELLOW_OBJECTIVE_CODE = Column(Numeric(9, 0), comment='定向增发目的代码')
    PRICINGDATE = Column(VARCHAR(8), comment='定价基准日')
    IS_NO_PUBLIC = Column(Numeric(5, 0), comment='是否属于非公开发行')
    EXP_COLLECTION = Column(Numeric(20, 4), comment='预计募集资金(元)')
    EXPENSE = Column(Numeric(20, 4), comment='发行费用(元)')
    S_RIGHTSISSUE_EXDIVIDENDDATE = Column(VARCHAR(8), comment='除权日')
    IS_EXDIVIDEND = Column(Numeric(1, 0), comment='是否除权')
    SUB_MODE = Column(Numeric(9, 0), comment='定增认购方式代码')
    OLDSPLA_MOLE = Column(Numeric(20, 4), comment='老股东配售比例分子')
    OLDSPLA_MODE = Column(VARCHAR(10), comment='老股东配售代码')
    S_FELLOW_TYPE = Column(VARCHAR(100), comment='增发类型')
    S_FELLOW_OBJECTIVE = Column(VARCHAR(4000), comment='增发目的说明')
    S_FELLOW_OFFERINGOBJECT_DES = Column(VARCHAR(800), comment='发行对象说明')
    EVENT_ID = Column(VARCHAR(40), comment='事件ID')
    PRICE_CONDITION = Column(VARCHAR(2000), comment='价格制定依据')
    PRICE_DT_TYPE = Column(VARCHAR(40), comment='定价基准日类型')
    ORGPRICE_PCT = Column(Numeric(20, 4), comment='预案价格相对基准价格比例(%)')
    ACTPRICE_PCT = Column(Numeric(20, 4), comment='实施价格相对基准价格比例(%)')
    APPRVBYSASSC_DT = Column(VARCHAR(8), comment='国资委批准公告日期')
    S_FELLOW_INITIAL_PLAN = Column(VARCHAR(8), comment='初始预案公告日')


class ASHARESSEINDUSTRIESCLASS(Base):
    """中国A股上证所行业分类"""
    __tablename__ = 'ASHARESSEINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SSE_IND_CODE = Column(VARCHAR(50), comment='上证所行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHAREST(Base):
    """中国A股特别处理"""
    __tablename__ = 'ASHAREST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_TYPE_ST = Column(VARCHAR(8), comment='特别处理类型')
    ENTRY_DT = Column(VARCHAR(8), comment='实施日期')
    REMOVE_DT = Column(VARCHAR(8), comment='撤销日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REASON = Column(VARCHAR(100), comment='实施原因')


class ASHARESTAFF(Base):
    """中国A股员工人数变更"""
    __tablename__ = 'ASHARESTAFF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 4), comment='员工人数(人)')
    S_INFO_TOTALEMPLOYEES2 = Column(Numeric(20, 0), comment='母公司员工人数(人)')
    MEMO = Column(VARCHAR(1000), comment='特殊情况说明')


class ASHARESTAFFSTRUCTURE(Base):
    """中国A股员工构成"""
    __tablename__ = 'ASHARESTAFFSTRUCTURE'
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
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')


class ASHARESTIBCONCEPTUALPLATE(Base):
    """中国A股科创板上市概念板块"""
    __tablename__ = 'ASHARESTIBCONCEPTUALPLATE'
    __table_args__ = (
        Index('fass', 'WIND_SEC_CODE', 'S_INFO_WINDCODE', 'ENTRY_DT', 'REMOVE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_SEC_CODE = Column(VARCHAR(50), comment='Wind概念板块代码')
    WIND_SEC_NAME = Column(VARCHAR(100), comment='Wind概念板块名称')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHARESTIBEMERGINGINDUSTRIES(Base):
    """中国A股科创板所属新兴产业分类"""
    __tablename__ = 'ASHARESTIBEMERGINGINDUSTRIES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    WIND_SEC_CODE = Column(VARCHAR(50), comment='Wind概念板块代码')
    WIND_SEC_NAME = Column(VARCHAR(100), comment='Wind概念板块名称')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHARESTIBHOLDERVOTE(Base):
    """中国A股科创板公司股东表决权"""
    __tablename__ = 'ASHARESTIBHOLDERVOTE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    DEADLINE = Column(VARCHAR(8), comment='截止日期')
    S_HOLDER_HOLDERCATEGORY = Column(VARCHAR(1), comment='股东类型')
    S_HOLDER_NAME = Column(VARCHAR(100), comment='股东名称')
    S_HOLDER_CODE = Column(VARCHAR(10), comment='股东ID')
    S_HOLDER_QUANTITY = Column(Numeric(20, 4), comment='持股数量(股)')
    S_HOLDER_VOTING_NUMBER = Column(Numeric(20, 4), comment='表决权数量(票)')
    S_HOLDER_LSTTYPECODE = Column(Numeric(9, 0), comment='股份类型')


class ASHARESTIBINTEREST(Base):
    """中国A股科创板股份权益概念"""
    __tablename__ = 'ASHARESTIBINTEREST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDUSTRYCODE = Column(VARCHAR(20), comment='板块代码')
    S_INFO_INDUSTRYNAME = Column(VARCHAR(100), comment='板块名称')


class ASHARESTIBINVESTMENTIENDING(Base):
    """中国A股科创板战投出借信息"""
    __tablename__ = 'ASHARESTIBINVESTMENTIENDING'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DT = Column(VARCHAR(8), comment='交易日期')
    S_SHARE_TOTALRESTRICTED = Column(Numeric(20, 4), comment='限售股(万股)')
    S_SHARE_FLOAT = Column(Numeric(20, 4), comment='非限售股(万股)')
    S_SHARE_LENDING = Column(Numeric(20, 4), comment='可出借股份(万股)')
    S_SHARE_LENDING_MARGIN = Column(Numeric(20, 4), comment='出借余量(万股)')
    S_SHARE_CHANGE = Column(Numeric(20, 4), comment='当日出借变动股份(万股)')


class ASHARESTLOAN(Base):
    """中国A股财务附注--短期借款"""
    __tablename__ = 'ASHARESTLOAN'
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


class ASHARESTOCKRATING(Base):
    """中国A股投资评级明细"""
    __tablename__ = 'ASHARESTOCKRATING'
    __table_args__ = (
        Index('IDX_ASHARESTOCKRATING_ANN_DT', 'ANN_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_EST_INSTITUTE = Column(VARCHAR(100), comment='研究机构名称')
    S_EST_RATINGANALYST = Column(VARCHAR(100), comment='分析师名称')
    S_EST_ESTNEWTIME_INST = Column(VARCHAR(8), comment='评级日期')
    S_EST_SCORERATING_INST = Column(Numeric(20, 4), comment='本次标准评级')
    S_EST_PRESCORERATING_INST = Column(Numeric(20, 4), comment='前次标准评级')
    S_EST_LOWPRICE_INST = Column(Numeric(20, 4), comment='本次最低目标价')
    S_EST_HIGHPRICE_INST = Column(Numeric(20, 4), comment='本次最高目标价')
    S_EST_PRELOWPRICE_INST = Column(Numeric(20, 4), comment='前次最低目标价')
    S_EST_PREHIGHPRICE_INST = Column(Numeric(20, 4), comment='前次最高目标价')
    ANN_DT = Column(VARCHAR(8), comment='公告日期(内部)')
    S_EST_RATING_INST = Column(VARCHAR(20), comment='本次评级')
    S_EST_PRERATING_INST = Column(VARCHAR(20), comment='前次评级')
    S_EST_REPORT_TITLE = Column(VARCHAR(400), comment='报告标题')
    S_EST_REPORT_TYPE = Column(Numeric(9, 0), comment='报告类别')
    S_EST_RATINGANALYSTID = Column(VARCHAR(200), comment='分析师id')
    S_RATING_CHANGE = Column(Numeric(9, 0), comment='评级变动方向')
    S_RATING_VALIDENDDT = Column(VARCHAR(8), comment='评级有效截止日')


class ASHARESTOCKRATINGCONSUS(Base):
    """中国A股投资评级汇总"""
    __tablename__ = 'ASHARESTOCKRATINGCONSUS'
    __table_args__ = (
        Index('IDX_ASHARESTOCKRATINGCONSUS_RATING_DT', 'RATING_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    RATING_DT = Column(VARCHAR(8), comment='日期')
    S_WRATING_AVG = Column(Numeric(20, 4), comment='综合评级')
    S_WRATING_INSTNUM = Column(Numeric(20, 4), comment='评级机构数量')
    S_WRATING_UPGRADE = Column(Numeric(20, 4), comment='调高家数（相比一月前）')
    S_WRATING_DOWNGRADE = Column(Numeric(20, 4), comment='调低家数（相比一月前）')
    S_WRATING_MAINTAIN = Column(Numeric(20, 4), comment='维持家数（相比一月前）')
    S_WRATING_NUMOFBUY = Column(Numeric(20, 4), comment='买入家数')
    S_WRATING_NUMOFOUTPERFORM = Column(Numeric(20, 4), comment='增持家数')
    S_WRATING_NUMOFHOLD = Column(Numeric(20, 4), comment='中性家数')
    S_WRATING_NUMOFUNDERPERFORM = Column(Numeric(20, 4), comment='减持家数')
    S_WRATING_NUMOFSELL = Column(Numeric(20, 4), comment='卖出家数')
    S_WRATING_CYCLE = Column(VARCHAR(10), comment='周期')
    S_EST_PRICE = Column(Numeric(20, 4), comment='一致预测目标价')
    S_EST_PRICEINSTNUM = Column(Numeric(20, 4), comment='目标价预测机构数')


class ASHARESTOCKREPO(Base):
    """中国A股回购"""
    __tablename__ = 'ASHARESTOCKREPO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EVENT_ID = Column(VARCHAR(38), comment='事件ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    STATUS = Column(Numeric(9, 0), comment='进度类型代码')
    EXP_DT = Column(VARCHAR(8), comment='过期日期')
    QTY = Column(Numeric(20, 4), comment='回购数量')
    AMT = Column(Numeric(20, 4), comment='回购金额')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    CRNCY_CODE = Column(VARCHAR(20), comment='货币代码')
    STOCK_REPO_OBJECTIVE_CODE = Column(Numeric(9, 0), comment='股份回购目的代码')
    S_SHARE_LSTTYPECODE = Column(Numeric(9, 0), comment='回购股份类型代码')


class ASHARESTOCKSWAP(Base):
    """中国A股股票置换"""
    __tablename__ = 'ASHARESTOCKSWAP'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRANSFERER_WINDCODE = Column(VARCHAR(40), comment='换股方万得代码')
    TRANSFERER_NAME = Column(VARCHAR(40), comment='换股方简称')
    PROGRESS = Column(VARCHAR(10), comment='方案进度')
    TARGETCOMP_WINDCODE = Column(VARCHAR(40), comment='标的方万得代码')
    TARGETCOMP_NAME = Column(VARCHAR(40), comment='标的方简称')
    TRANSFERER_CONVERSIONPRICE = Column(Numeric(20, 4), comment='换股方换股价')
    TARGETCOMP_CONVERSIONPRICE = Column(Numeric(20, 4), comment='标的方换股价')
    CONVERSIONRATIO = Column(Numeric(20, 8), comment='换股比例')
    IS_CASHOPTION = Column(Numeric(5, 0), comment='是否有现金选择权')
    CASHOPTION = Column(Numeric(20, 4), comment='现金选择权')
    CASHOPTION_REPORTSTARTDATE = Column(VARCHAR(8), comment='现金选择权申报起始日')
    CASHOPTION_REPORTENDDATE = Column(VARCHAR(8), comment='现金选择权申报截止日')
    CASHOPTION_APPLICATIONCODE = Column(VARCHAR(10), comment='现金选择权申请代码')
    CASHOPTION_SHAREPURCHASER = Column(VARCHAR(80), comment='现金选择权股份购买方')
    CASHOPTION_APPLICANTNAME = Column(VARCHAR(40), comment='现金选择权适用方简称')
    IS_OVERALLLISTING = Column(Numeric(5, 0), comment='是否属于整体上市')
    PRELANDATE = Column(VARCHAR(8), comment='预案公告日')
    MTSTARTDATE = Column(VARCHAR(8), comment='股东大会召开日')
    SMTGRECDATE = Column(VARCHAR(8), comment='股东大会股权登记日')
    SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    IECANNOUNCEMENTDATE = Column(VARCHAR(8), comment='证监会发审委公告日')
    ANNCEDATE = Column(VARCHAR(8), comment='实施公告日')
    ANNCELSTDATE = Column(VARCHAR(8), comment='上市公告日')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日')
    TRADERESUMPTIONDATE = Column(VARCHAR(8), comment='预案公布后复牌日')
    LASTTRADEDATE = Column(VARCHAR(8), comment='实施前最后交易日')
    EQUITYREGISTRATIONDATE = Column(VARCHAR(8), comment='换股股权登记日')
    LISTDATE = Column(VARCHAR(8), comment='上市日')
    CONSOLIDATIONBASEDATE = Column(VARCHAR(8), comment='合并基准日')
    FINANCIALADVISOR = Column(VARCHAR(80), comment='财务顾问')
    PLANDESCRIPTION = Column(VARCHAR(300), comment='方案说明')
    CASHARRIVALDATE = Column(VARCHAR(8), comment='现金选择权现金到账日')
    EFFECTIVEREPORTEDSHARES = Column(Numeric(20, 4), comment='现金选择权有效申报股数')


class ASHARESTOCKSWAPZL(Base):
    """中国A股股票置换(增量)"""
    __tablename__ = 'ASHARESTOCKSWAPZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRANSFERER_WINDCODE = Column(VARCHAR(40), comment='换股方万得代码')
    TRANSFERER_NAME = Column(VARCHAR(40), comment='换股方简称')
    PROGRESS = Column(VARCHAR(10), comment='方案进度')
    TARGETCOMP_WINDCODE = Column(VARCHAR(40), comment='标的方万得代码')
    TARGETCOMP_NAME = Column(VARCHAR(40), comment='标的方简称')
    TRANSFERER_CONVERSIONPRICE = Column(Numeric(20, 4), comment='换股方换股价')
    TARGETCOMP_CONVERSIONPRICE = Column(Numeric(20, 4), comment='标的方换股价')
    CONVERSIONRATIO = Column(Numeric(20, 8), comment='换股比例')
    IS_CASHOPTION = Column(Numeric(5, 0), comment='是否有现金选择权')
    CASHOPTION = Column(Numeric(20, 4), comment='现金选择权')
    CASHOPTION_REPORTSTARTDATE = Column(VARCHAR(8), comment='现金选择权申报起始日')
    CASHOPTION_REPORTENDDATE = Column(VARCHAR(8), comment='现金选择权申报截止日')
    CASHOPTION_APPLICATIONCODE = Column(VARCHAR(10), comment='现金选择权申请代码')
    CASHOPTION_SHAREPURCHASER = Column(VARCHAR(80), comment='现金选择权股份购买方')
    CASHOPTION_APPLICANTNAME = Column(VARCHAR(40), comment='现金选择权适用方简称')
    IS_OVERALLLISTING = Column(Numeric(5, 0), comment='是否属于整体上市')
    PRELANDATE = Column(VARCHAR(8), comment='预案公告日')
    MTSTARTDATE = Column(VARCHAR(8), comment='股东大会召开日')
    SMTGRECDATE = Column(VARCHAR(8), comment='股东大会股权登记日')
    SMTGANNCEDATE = Column(VARCHAR(8), comment='股东大会公告日')
    IECANNOUNCEMENTDATE = Column(VARCHAR(8), comment='证监会发审委公告日')
    ANNCEDATE = Column(VARCHAR(8), comment='实施公告日')
    ANNCELSTDATE = Column(VARCHAR(8), comment='上市公告日')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日')
    TRADERESUMPTIONDATE = Column(VARCHAR(8), comment='预案公布后复牌日')
    LASTTRADEDATE = Column(VARCHAR(8), comment='实施前最后交易日')
    EQUITYREGISTRATIONDATE = Column(VARCHAR(8), comment='换股股权登记日')
    LISTDATE = Column(VARCHAR(8), comment='上市日')
    CONSOLIDATIONBASEDATE = Column(VARCHAR(8), comment='合并基准日')
    FINANCIALADVISOR = Column(VARCHAR(80), comment='财务顾问')
    PLANDESCRIPTION = Column(VARCHAR(300), comment='方案说明')
    CASHARRIVALDATE = Column(VARCHAR(8), comment='现金选择权现金到账日')
    EFFECTIVEREPORTEDSHARES = Column(Numeric(20, 4), comment='现金选择权有效申报股数')


class ASHARESTRANGETRADE(Base):
    """中国A股证券交易异动营业部买卖信息"""
    __tablename__ = 'ASHARESTRANGETRADE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_STRANGE_BGDATE = Column(VARCHAR(8), comment='交易起始日')
    S_STRANGE_ENDDATE = Column(VARCHAR(8), comment='交易截止日')
    S_STRANGE_RANGE = Column(Numeric(20, 4), comment='涨跌幅')
    S_STRANGE_VOLUME = Column(Numeric(20, 4), comment='总成交量(万股)')
    S_STRANGE_AMOUNT = Column(Numeric(20, 4), comment='总成交金额')
    S_STRANGE_TRADERNAME = Column(VARCHAR(200), comment='营业部名称')
    S_STRANGE_TRADERAMOUNT = Column(Numeric(20, 4), comment='营业部买卖金额')
    S_STRANGE_BUYAMOUNT = Column(Numeric(20, 4), comment='买入金额(元)')
    S_STRANGE_SELLAMOUNT = Column(Numeric(20, 4), comment='卖出金额(元)')
    S_VARIANT_TYPE = Column(VARCHAR(40), comment='异动类型')


class ASHARESTRANGETRADEDETAIL(Base):
    """中国A股交易异动"""
    __tablename__ = 'ASHARESTRANGETRADEDETAIL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TYPE_CODE = Column(VARCHAR(3), comment='异动类型')
    START_DT = Column(VARCHAR(8), comment='起始日')
    END_DT = Column(VARCHAR(8), comment='截止日')
    VOLUME = Column(Numeric(20, 4), comment='成交量(万股)')
    AMOUNT = Column(Numeric(20, 4), comment='成交金额(元)')
    PCTCHANGE = Column(Numeric(20, 4), comment='涨跌幅(%)')
    CHANGE_DEVIATION = Column(Numeric(20, 4), comment='涨跌幅偏离值(%)')
    SWING = Column(Numeric(20, 4), comment='振幅(%)')
    TURN = Column(Numeric(20, 4), comment='换手率(%)')
    CHANGE_DEVIATION_3D = Column(Numeric(20, 4), comment='连续三个交易日累计涨跌幅偏离值(%)')
    TURN_3D = Column(Numeric(20, 4), comment='连续三个交易日累计换手率(%)')
    TURN_3DTO5D = Column(Numeric(20, 4), comment='连续三个交易日日均换手率与前五个交易日的日均换手率的比值(倍)')
    MARGIN_PCT = Column(Numeric(20, 4), comment='融资买入(融资卖出)成交占比')


class ASHARESTYLECOEFFICIENT(Base):
    """中国A股股票风格系数"""
    __tablename__ = 'ASHARESTYLECOEFFICIENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CHANGE_DATE = Column(VARCHAR(8), comment='变动日期')
    DATE_CLOSING_DATE = Column(VARCHAR(8), comment='引用数据的截止日期')
    STYLE_COEFFICIENT = Column(Numeric(20, 4), comment='风格系数')
    GROWTH_Z = Column(Numeric(20, 4), comment='成长性Z分值')
    VALUE_Z = Column(Numeric(20, 4), comment='价值因子Z分值(ZVP)')
    AVG_MARKET_VALUE = Column(Numeric(20, 4), comment='1年日均市值(万元)')
    GROSS_OPER_REV = Column(Numeric(20, 4), comment='营业收入增长率(%)')
    GROSS_OPER_NETPROFIT = Column(Numeric(20, 4), comment='净利润增长率(%)')
    VALUE_COEFFICIENT = Column(Numeric(20, 4), comment='调整市值系数')


class ASHARESUPERVISOR(Base):
    """中国A股公司监事成员"""
    __tablename__ = 'ASHARESUPERVISOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    S_INFO_DIMENSION = Column(VARCHAR(100), comment='维度')
    S_INFO_DIMENSION1 = Column(VARCHAR(100), comment='子维度')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='职务')
    S_INFO_MANID = Column(VARCHAR(10), comment='人物id')


class ASHARESUPPLIER(Base):
    """中国A股公司供应商"""
    __tablename__ = 'ASHARESUPPLIER'
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


class ASHARESURPLUSRESERVE(Base):
    """中国A股财务附注--盈余公积"""
    __tablename__ = 'ASHARESURPLUSRESERVE'
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


class ASHARESWINDUSTRIESCLASS(Base):
    """申万行业分类"""
    __tablename__ = 'ASHARESWINDUSTRIESCLASS'
    __table_args__ = (
        Index('fass', 'SW_IND_CODE', 'S_INFO_WINDCODE', 'ENTRY_DT', 'REMOVE_DT'),
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SW_IND_CODE = Column(VARCHAR(50), comment='申万行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHARESWNINDUSTRIESCLASS(Base):
    """申万行业分类(2021版)"""
    __tablename__ = 'ASHARESWNINDUSTRIESCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SW_IND_CODE = Column(VARCHAR(50), comment='申万行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHARESWINDUSTRIESCLASSZL(Base):
    """申万行业分类(增量)"""
    __tablename__ = 'ASHARESWINDUSTRIESCLASSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SW_IND_CODE = Column(VARCHAR(50), comment='申万行业代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class ASHARESWINGREVERSETREND(Base):
    """中国A股摆动与反趋向技术指标(不复权)"""
    __tablename__ = 'ASHARESWINGREVERSETREND'
    __table_args__ = (
        Index('IDX_ASHARESWINGREVERSETREND_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    RC_50D = Column(Numeric(20, 8), comment='RC变化率指数(50日)')
    MI_A12D = Column(Numeric(20, 8), comment='MI动量指标A(12日)')
    MI_MI12D = Column(Numeric(20, 8), comment='MI动量指标MI?(12日)')
    MICD_DIF = Column(Numeric(20, 8), comment='MICD异同离差动力指数DIF(3,10,20日)')
    MICD_MICD = Column(Numeric(20, 8), comment='MICD异同离差动力指数MICD(3,10,20,10日)')
    RCCD_DIF = Column(Numeric(20, 8), comment='RCCD异同离差变化率指数DIF(59,21,28日)')
    RCCD_RCCD = Column(Numeric(20, 8), comment='RCCD异同离差变化率指数RCCD(59,21,28日)')
    SRMI_9D = Column(Numeric(20, 8), comment='SRMI?MI修正指标(9日)')
    ATR_TR14D = Column(Numeric(20, 8), comment='ATR真实波幅TR(14日)')
    ATR_ATR14D = Column(Numeric(20, 8), comment='ATR真实波幅ATR(14日)')
    MASS = Column(Numeric(20, 8), comment='MASS梅丝线(9,25日)')
    VHF = Column(Numeric(20, 8), comment='VHF纵横指标(28日)')
    CVLT = Column(Numeric(20, 8), comment='CVLT佳庆离散指标(10日)')
    ADTM_ADTM = Column(Numeric(20, 8), comment='ADTM动态买卖气指标ADTM(23,8日)')
    ADTM_ADTMMA = Column(Numeric(20, 8), comment='ADTM动态买卖气指标ADTMMA(23,8日)')
    BIAS = Column(Numeric(20, 8), comment='BIAS乖离率(12日)')
    KDJ_K = Column(Numeric(20, 8), comment='KDJ随机指标K(9,3,3日)')
    KDJ_D = Column(Numeric(20, 8), comment='KDJ随机指标D(9,3,3日)')
    KDJ_J = Column(Numeric(20, 8), comment='KDJ随机指标J(9,3,3日)')
    RSI = Column(Numeric(20, 8), comment='RSI相对强弱指标(6日)')
    CCI = Column(Numeric(20, 8), comment='CCI顺势指标(14日)')
    DBCD_DBCD = Column(Numeric(20, 8), comment='DBCD异同离差乖离率DBCD(5,16,76日)')
    DBCD_MM = Column(Numeric(20, 8), comment='DBCD异同离差乖离率MM(5,16,76日)')
    DPO = Column(Numeric(20, 8), comment='DPO区间震荡线DPO(20,6日)')
    DPO_MADPO = Column(Numeric(20, 8), comment='DPO区间震荡线MADPO(20,6日)')
    LWR1 = Column(Numeric(20, 8), comment='LWR威廉指标LWR1(9,3,3日)')
    LWR2 = Column(Numeric(20, 8), comment='LWR威廉指标LWR2(9,3,3日)')
    ROC = Column(Numeric(20, 8), comment='ROC变动速率ROC(12,6日)')
    ROC_ROCMA = Column(Numeric(20, 8), comment='ROC变动速率ROCMA(12,6日)')
    SI = Column(Numeric(20, 8), comment='SI摆动指标')
    SLOWKD_K = Column(Numeric(20, 8), comment='SLOWKD慢速K(9,3,3,5日)')
    SLOWKD_D = Column(Numeric(20, 8), comment='SLOWKD慢速D(9,3,3,5日)')
    WR = Column(Numeric(20, 8), comment='WR威廉指标(14日)')
    BIAS36 = Column(Numeric(20, 8), comment='B3612三减六日乖离BIAS36')
    BIAS612 = Column(Numeric(20, 8), comment='B3612三减六日乖离BIAS612')


class ASHARESWINGREVERSETRENDADJ(Base):
    """中国A股摆动与反趋向技术指标(后复权)"""
    __tablename__ = 'ASHARESWINGREVERSETRENDADJ'
    __table_args__ = (
        Index('IDX_ASHARESWINGREVERSETRENDADJ_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    RC_50D = Column(Numeric(20, 8), comment='RC变化率指数(50日)')
    MI_A12D = Column(Numeric(20, 8), comment='MI动量指标A(12日)')
    MI_MI12D = Column(Numeric(20, 8), comment='MI动量指标MI?(12日)')
    MICD_DIF = Column(Numeric(20, 8), comment='MICD异同离差动力指数DIF(3,10,20日)')
    MICD_MICD = Column(Numeric(20, 8), comment='MICD异同离差动力指数MICD(3,10,20,10日)')
    RCCD_DIF = Column(Numeric(20, 8), comment='RCCD异同离差变化率指数DIF(59,21,28日)')
    RCCD_RCCD = Column(Numeric(20, 8), comment='RCCD异同离差变化率指数RCCD(59,21,28日)')
    SRMI_9D = Column(Numeric(20, 8), comment='SRMI?MI修正指标(9日)')
    ATR_TR14D = Column(Numeric(20, 8), comment='ATR真实波幅TR(14日)')
    ATR_ATR14D = Column(Numeric(20, 8), comment='ATR真实波幅ATR(14日)')
    MASS = Column(Numeric(20, 8), comment='MASS梅丝线(9,25日)')
    VHF = Column(Numeric(20, 8), comment='VHF纵横指标(28日)')
    CVLT = Column(Numeric(20, 8), comment='CVLT佳庆离散指标(10日)')
    ADTM_ADTM = Column(Numeric(20, 8), comment='ADTM动态买卖气指标ADTM(23,8日)')
    ADTM_ADTMMA = Column(Numeric(20, 8), comment='ADTM动态买卖气指标ADTMMA(23,8日)')
    BIAS = Column(Numeric(20, 8), comment='BIAS乖离率(12日)')
    KDJ_K = Column(Numeric(20, 8), comment='KDJ随机指标K(9,3,3日)')
    KDJ_D = Column(Numeric(20, 8), comment='KDJ随机指标D(9,3,3日)')
    KDJ_J = Column(Numeric(20, 8), comment='KDJ随机指标J(9,3,3日)')
    RSI = Column(Numeric(20, 8), comment='RSI相对强弱指标(6日)')
    CCI = Column(Numeric(20, 8), comment='CCI顺势指标(14日)')
    DBCD_DBCD = Column(Numeric(20, 8), comment='DBCD异同离差乖离率DBCD(5,16,76日)')
    DBCD_MM = Column(Numeric(20, 8), comment='DBCD异同离差乖离率MM(5,16,76日)')
    DPO = Column(Numeric(20, 8), comment='DPO区间震荡线DPO(20,6日)')
    DPO_MADPO = Column(Numeric(20, 8), comment='DPO区间震荡线MADPO(20,6日)')
    LWR1 = Column(Numeric(20, 8), comment='LWR威廉指标LWR1(9,3,3日)')
    LWR2 = Column(Numeric(20, 8), comment='LWR威廉指标LWR2(9,3,3日)')
    ROC = Column(Numeric(20, 8), comment='ROC变动速率ROC(12,6日)')
    ROC_ROCMA = Column(Numeric(20, 8), comment='ROC变动速率ROCMA(12,6日)')
    SI = Column(Numeric(20, 8), comment='SI摆动指标')
    SLOWKD_K = Column(Numeric(20, 8), comment='SLOWKD慢速K(9,3,3,5日)')
    SLOWKD_D = Column(Numeric(20, 8), comment='SLOWKD慢速D(9,3,3,5日)')
    WR = Column(Numeric(20, 8), comment='WR威廉指标(14日)')
    BIAS36 = Column(Numeric(20, 8), comment='B3612三减六日乖离BIAS36')
    BIAS612 = Column(Numeric(20, 8), comment='B3612三减六日乖离BIAS612')


class ASHARETAXESPAY(Base):
    """中国A股财务附注--应交税费"""
    __tablename__ = 'ASHARETAXESPAY'
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


class ASHARETAXESPAYABLE(Base):
    """中国A股应交税费明细"""
    __tablename__ = 'ASHARETAXESPAYABLE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司id')
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


class ASHARETAXRATE(Base):
    """中国A股公司税率明细"""
    __tablename__ = 'ASHARETAXRATE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(100), comment='公司ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    TAX_RATE = Column(Numeric(20, 4), comment='税率(%)')
    BEGIN_MON = Column(Numeric(22, 0), comment='起始月份')
    END_MON = Column(Numeric(22, 0), comment='终止月份')
    DISCOUNT_REASON = Column(VARCHAR(3000), comment='税项优惠原因')
    MEMO = Column(VARCHAR(100), comment='备注')


class ASHARETAXSURCHARGE(Base):
    """中国A股财务附注--营业税金及附加"""
    __tablename__ = 'ASHARETAXSURCHARGE'
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


class ASHARETECHINDICATORS(Base):
    """中国A股成交量技术指标"""
    __tablename__ = 'ASHARETECHINDICATORS'
    __table_args__ = (
        Index('IDX_ASHARETECHINDICATORS_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    VOLUME_RATIO_5D = Column(Numeric(20, 8), comment='量比(5日)')
    VAM_1M = Column(Numeric(20, 8), comment='VMA量简单移动平均(1月)')
    VAM_5M = Column(Numeric(20, 8), comment='VMA量简单移动平均(5日)')
    VAM_22M = Column(Numeric(20, 8), comment='VMA量简单移动平均(22日)')
    VAM_60M = Column(Numeric(20, 8), comment='VMA量简单移动平均(60日)')
    AMA_1W = Column(Numeric(20, 8), comment='AMA额简单移动平均(1周)')
    AMA_1M = Column(Numeric(20, 8), comment='AMA额简单移动平均(1月)')
    AMA_1Q = Column(Numeric(20, 8), comment='AMA额简单移动平均(1季)')
    VMACD = Column(Numeric(20, 8), comment='VMACD量指数平滑异同平均DIF(12,26,9日)')
    VMACD_DEA = Column(Numeric(20, 8), comment='VMACD量指数平滑异同平均DEA(12,26,9日)')
    VMACD_MACD = Column(Numeric(20, 8), comment='VMACD量指数平滑异同平均MACD(12,26,9日)')
    VOSC = Column(Numeric(20, 8), comment='VOSC成交量震荡(12,26日)')
    TAPI_16D = Column(Numeric(20, 8), comment='TAPI加权指数成交值TAPI(6日)')
    TAPI_6D = Column(Numeric(20, 8), comment='TAPI加权指数成交值TAPIMA(6日)')
    VSTD_10D = Column(Numeric(20, 8), comment='VSTD成交量标准差(10日)')
    VMACD_EMA12D = Column(Numeric(20, 8), comment='VMACD量指数平滑异同平均EMA(成交量,12日)')
    VMACD_EMA26D = Column(Numeric(20, 8), comment='VMACD量指数平滑异同平均EMA(成交量,26日)')
    VRSI_6D = Column(Numeric(20, 8), comment='VRSI量相对强弱(6日)')
    VROC_12D = Column(Numeric(20, 8), comment='VROC量变动速率(12日)')
    SOBV = Column(Numeric(20, 8), comment='SOBV能量潮')
    VR_26D = Column(Numeric(20, 8), comment='VR成交量比率(26日)')


class ASHARETOTALINVEST(Base):
    """中国A股财务附注--总投资收益"""
    __tablename__ = 'ASHARETOTALINVEST'
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


class ASHARETRADINGFINANCIALASSETS(Base):
    """中国A股财务附注--交易性金融资产"""
    __tablename__ = 'ASHARETRADINGFINANCIALASSETS'
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


class ASHARETRADINGSUSPENSION(Base):
    """中国A股停复牌信息"""
    __tablename__ = 'ASHARETRADINGSUSPENSION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DQ_SUSPENDDATE = Column(VARCHAR(8), comment='停牌日期')
    S_DQ_SUSPENDTYPE = Column(Numeric(9, 0), comment='停牌类型代码')
    S_DQ_RESUMPDATE = Column(VARCHAR(8), comment='复牌日期')
    S_DQ_CHANGEREASON = Column(VARCHAR(400), comment='停牌原因')
    S_DQ_TIME = Column(VARCHAR(200), comment='停复牌时间')
    S_DQ_CHANGEREASONTYPE = Column(Numeric(9, 0), comment='停牌原因代码')


class ASHARETRADINGSUSPENSIONDERIVED(Base):
    """A股停复牌信息表衍生数据"""
    __tablename__ = 'ASHARETRADINGSUSPENSIONDERIVED'
    OBJECT_ID = Column(VARCHAR(40), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_DQ_SUSPENDDATE = Column(VARCHAR(8), comment='停牌日期')
    S_DQ_SUSPENDDATE_START = Column(VARCHAR(8), comment='停牌起始日期')
    S_DQ_SUSPENDDAYS_CONTINU = Column(Numeric(20, 0), comment='连续停牌天数')
    S_DQ_RESUMPDATE = Column(VARCHAR(8), comment='复牌日期')
    S_DQ_CHANGEREASONTYPE = Column(Numeric(9, 0), comment='停牌原因代码')
    S_DQ_SUSPENDTYPE = Column(VARCHAR(20), comment='停牌类型')


class ASHARETRUSTINVESTMENTTOT(Base):
    """中国A股关联方往来及委托理财合计"""
    __tablename__ = 'ASHARETRUSTINVESTMENTTOT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    RP_SALE_PRODUCT = Column(Numeric(20, 4), comment='向关联方销售产品金额合计(万元)')
    CONTRO_PARTY_CAPITAL_AMOUNT = Column(Numeric(20, 4), comment='向控股方提供资金发生额合计(万元)')
    CONTRO_PARTY_CAPITAL_BALANCE = Column(Numeric(20, 4), comment='向控股方提供资金余额合计(万元)')
    RP_AMOUNT = Column(Numeric(20, 4), comment='向关联方提供资金发生额合计(万元)')
    RP_BALANCE = Column(Numeric(20, 4), comment='向关联方提供资金余额合计(万元)')
    AMOUNT_FUNDS_AVAILABLE = Column(Numeric(20, 4), comment='关联方向上市公司提供资金发生额合计(万元)')
    FUNDING_BALANCE = Column(Numeric(20, 4), comment='关联方向上市公司提供资金余额合计(万元)')
    FP_AMOUNT_TOT = Column(Numeric(20, 4), comment='委托理财累计金额(万元)')
    FP_BALANCE = Column(Numeric(20, 4), comment='委托理财余额(万元)')
    FP_OVERDUE_AMOUNT = Column(Numeric(20, 4), comment='委托理财逾期未收回的本金和收益累计金额(万元)')
    FP_ADDUP_PROFIT = Column(Numeric(20, 4), comment='委托理财收益累计金额(万元)')
    RP_SALE_PRODUCT_RATIO = Column(Numeric(20, 4), comment='向关联方销售产品金额占比(%)')
    RP_PURCHASE_AMOUNT = Column(Numeric(20, 4), comment='向关联方采购产品金额合计(万元)')
    RP_PURCHASE_RATIO = Column(Numeric(20, 4), comment='向关联方采购产品金额占比(%)')
    RP_SALE_PRODUCT_EST = Column(Numeric(20, 4), comment='向关联方销售产品预计金额合计(万元)')
    RP_LABOUR_SERVICES_EST = Column(Numeric(20, 4), comment='向关联方提供劳务预计金额合计(万元)')
    RP_PURCHASE_AMOUNT_EST = Column(Numeric(20, 4), comment='向关联方采购产品预计金额合计(万元)')
    RP_ACCEPT_SERVICE_EST = Column(Numeric(20, 4), comment='向关联方接受劳务预计金额合计(万元)')
    RP_OTHER_TRANSACTIONS = Column(Numeric(20, 4), comment='向关联方其他交易预计金额合计(万元)')
    PRICING_PRINCIPLE = Column(VARCHAR(2000), comment='定价原则')


class ASHARETTMANDMRQ(Base):
    """中国A股TTM与MRQ"""
    __tablename__ = 'ASHARETTMANDMRQ'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='万得代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STATEMENT_TYPE = Column(VARCHAR(80), comment='报表类型')
    S_FA_OR_TTM = Column(Numeric(20, 4), comment='营业收入(TTM)')
    S_FA_COST_TTM = Column(Numeric(20, 4), comment='营业成本-非金融类(TTM)')
    S_FA_EXPENSE_TTM = Column(Numeric(20, 4), comment='营业支出-金融类(TTM)')
    S_FA_GROSSMARGIN_TTM = Column(Numeric(20, 4), comment='毛利(TTM)')
    S_FA_OPERATEINCOME_TTM = Column(Numeric(20, 4), comment='经营活动净收益(TTM)')
    S_FA_INVESTINCOME_TTM = Column(Numeric(20, 4), comment='价值变动净收益(TTM)')
    S_FA_OP_TTM = Column(Numeric(20, 4), comment='营业利润(TTM)')
    S_FA_EBT_TTM = Column(Numeric(20, 4), comment='利润总额(TTM)')
    S_FA_PROFIT_TTM = Column(Numeric(20, 4), comment='净利润(TTM)')
    S_FA_NETPROFIT_TTM = Column(Numeric(20, 4), comment='归属于母公司的净利润(TTM)')
    S_FA_GR_TTM = Column(Numeric(20, 4), comment='营业总收入(TTM)')
    S_FA_GC_TTM = Column(Numeric(20, 4), comment='营业总成本(TTM)')
    S_FA_CASHFLOW_TTM = Column(Numeric(20, 4), comment='现金净流量(TTM)')
    S_FA_OPERATECASHFLOW_TTM = Column(Numeric(20, 4), comment='经营活动现金净流量(TTM)')
    S_FA_INVESTCASHFLOW_TTM = Column(Numeric(20, 4), comment='投资活动现金净流量(TTM)')
    S_FA_FINANCECASHFLOW_TTM = Column(Numeric(20, 4), comment='筹资活动现金净流量(TTM)')
    S_FA_ASSET_MRQ = Column(Numeric(20, 4), comment='资产总计(MRQ)')
    S_FA_DEBT_MRQ = Column(Numeric(20, 4), comment='负债合计(MRQ)')
    S_FA_TOTALEQUITY_MRQ = Column(Numeric(20, 4), comment='股东权益(MRQ)')
    S_FA_EQUITY_MRQ = Column(Numeric(20, 4), comment='归属于母公司的股东权益(MRQ)')
    S_FA_EQUITY_NEW = Column(Numeric(20, 4), comment='归属于母公司的股东权益(最新)')
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
    S_FA_EPS_TTM = Column(Numeric(20, 4), comment='每股收益(TTM)')
    S_FA_ORPS_TTM = Column(Numeric(20, 4), comment='每股营业收入(TTM)')
    S_FA_OCFPS_TTM = Column(Numeric(20, 4), comment='每股经营活动产生的现金流量净额(TTM)')
    S_FA_CFPS_TTM = Column(Numeric(20, 4), comment='每股现金流量净额(TTM)')
    S_FA_BPS_NEW = Column(Numeric(20, 4), comment='每股净资产(最新)')
    S_FA_SALESCASHIN_TTM = Column(Numeric(20, 4), comment='销售商品提供劳务收到的现金(TTM)')
    S_FA_OPERATEEXPENSE_TTM = Column(Numeric(20, 4), comment='销售费用(TTM) ')
    S_FA_ADMINEXPENSE_TTM = Column(Numeric(20, 4), comment='管理费用(TTM) ')
    S_FA_FINAEXPENSE_TTM = Column(Numeric(20, 4), comment='财务费用(TTM) ')
    S_FA_EXPENSE = Column(Numeric(20, 4), comment='期间费用(TTM) ')
    S_FA_NONOPERATEPROFIT_TTM = Column(Numeric(20, 4), comment='营业外收支净额(TTM)')
    S_FA_IMPAIRMENT_TTM = Column(Numeric(20, 4), comment='资产减值损失')
    S_FA_EBIT_TTM = Column(Numeric(20, 4), comment='息税前利润')
    S_FA_INVESTCAPITAL_MRQ = Column(Numeric(20, 4), comment='全部投入资本(MRQ) ')
    FA_ROIC_TTM = Column(Numeric(20, 4), comment='投入资本回报率ROIC(TTM)')
    S_STM_BSMRQ = Column(Numeric(20, 4), comment='固定资产合计(MRQ)')
    S_FA_NONOPPROFIT_TTM = Column(Numeric(20, 4), comment='非营业利润(TTM)')
    S_FA_PREFINEXP_OP_TTM = Column(Numeric(20, 4), comment='扣除财务费用前营业利润(TTM)')
    S_FA_OPTOEBT_TTM = Column(Numeric(20, 4), comment='营业利润／利润总额(TTM)')
    S_FA_NOPTOEBT_TTM = Column(Numeric(20, 4), comment='非营业利润／利润总额(TTM)')
    S_FA_TAXTOEBT_TTM = Column(Numeric(20, 4), comment='税项／利润总额(TTM)')
    S_FA_OPTOOR_TTM = Column(Numeric(20, 4), comment='营业利润／营业收入(TTM)')
    S_FA_EBTTOOR_TTM = Column(Numeric(20, 4), comment='利润总额／营业收入(TTM)')
    S_FA_PREFINEXPOPTOOR_TTM = Column(Numeric(20, 4), comment='扣除融资费用前营业利润／营业收入(TTM)')
    S_FA_NETPROFITTOOR_TTM = Column(Numeric(20, 4), comment='归属母公司股东的净利润／营业收入(TTM)')
    S_FA_PREFINEXPOPTOEBT_TTM = Column(Numeric(20, 4), comment='扣除融资费用前营业利润／利润总额(TTM)')
    S_FA_OCFTOOP_TTM = Column(Numeric(20, 4), comment='经营活动产生的现金流量净额／营业利润(TTM)')
    ROA_EXCLMININTINC_TTM = Column(Numeric(20, 4), comment='总资产净利率-不含少数股东损益(TTM)')
    S_FA_DEBTTOASSETS_MRQ = Column(Numeric(20, 4), comment='资产负债率(MRQ)')


class ASHARETTMHIS(Base):
    """中国A股TTM指标历史数据"""
    __tablename__ = 'ASHARETTMHIS'
    __table_args__ = (
        Index('IDX_ASHARETTMHIS_ANN_DT', 'ANN_DT'),
        Index('fass', 'S_INFO_WINDCODE', 'REPORT_PERIOD', 'TOT_OPER_REV_TTM', 'OPER_REV_TTM', 'NET_PROFIT_TTM',
              'NET_PROFIT_PARENT_COMP_TTM', 'NET_CASH_FLOWS_OPER_ACT_TTM', 'NET_INCR_CASH_CASH_EQU_TTM',
              'S_FA_COST_TTM', 'S_FA_EXPENSE_TTM', 'S_FA_GROSSMARGIN_TTM', 'S_FA_OPERATEINCOME_TTM',
              'S_FA_INVESTINCOME_TTM', 'S_FA_OP_TTM', 'S_FA_EBT_TTM', 'S_FA_GR_TTM', 'S_FA_GC_TTM',
              'S_FA_INVESTCASHFLOW_TTM', 'S_FA_FINANCECASHFLOW_TTM', 'S_FA_ASSET_MRQ', 'S_FA_DEBT_MRQ',
              'S_FA_TOTALEQUITY_MRQ', 'S_FA_EQUITY_MRQ', 'S_FA_NETPROFITMARGIN_TTM', 'S_FA_GROSSPROFITMARGIN_TTM',
              'S_FA_EXPENSETOSALES_TTM', 'S_FA_PROFITTOGR_TTM', 'S_FA_OPERATEEXPENSETOGR_TTM',
              'S_FA_ADMINEXPENSETOGR_TTM', 'S_FA_FINAEXPENSETOGR_TTM', 'S_FA_IMPAIRTOGR_TTM', 'S_FA_GCTOGR_TTM',
              'S_FA_OPTOGR_TTM', 'S_FA_ROA_TTM', 'S_FA_ROA2_TTM', 'S_FA_ROE_TTM', 'S_FA_OPERATEINCOMETOEBT_TTM',
              'S_FA_INVESTINCOMETOEBT_TTM', 'S_FA_NONOPERATEPROFITTOEBT_TTM', 'S_FA_SALESCASHINTOOR_TTM',
              'S_FA_OCFTOOR_TTM', 'S_FA_OCFTOOPERATEINCOME_TTM', 'S_FA_DEDUCTEDPROFIT_TTM', 'S_FA_EBITDA_TTM_INVERSE',
              'S_FA_EBITDA_TTM', 'S_FA_EBIT_TTM', 'FA_ROIC_TTM', 'S_FA_SALESCASHIN_TTM', 'S_FA_OPERATEEXPENSE_TTM',
              'S_FA_ADMINEXPENSE_TTM', 'S_FA_FINAEXPENSE_TTM', 'S_FA_EXPENSE', 'S_FA_NONOPERATEPROFIT_TTM',
              'S_FA_IMPAIRMENT_TTM', 'S_FA_EBIT_TTM_INVERSE', 'S_FA_INVESTCAPITAL_MRQ', 'FA_ROIC_TTM2', 'S_STM_BSMRQ',
              'S_FA_NONOPPROFIT_TTM', 'S_FA_PREFINEXP_OP_TTM', 'S_FA_OPTOEBT_TTM', 'S_FA_NOPTOEBT_TTM',
              'S_FA_TAXTOEBT_TTM', 'S_FA_OPTOOR_TTM', 'S_FA_EBTTOOR_TTM', 'S_FA_PREFINEXPOPTOOR_TTM',
              'S_FA_NETPROFITTOOR_TTM', 'S_FA_PREFINEXPOPTOEBT_TTM', 'S_FA_OCFTOOP_TTM', 'ROA_EXCLMININTINC_TTM',
              'S_FA_DEBTTOASSETS_MRQ', 'INT_EXP_TTM', 'INC_TAX_TTM', 'MINORITY_INT_TTM', 'CONTINUOUS_NET_OP_TTM',
              'NONCONTINUOUS_NET_OP_TTM', 'NONNETOPTOTAXPROFIT', 'NETOPTOTAXPROFIT'),)
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
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')


class ASHARETYPECODE(Base):
    """类型编码表"""
    __tablename__ = 'ASHARETYPECODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_TYPNAME = Column(VARCHAR(300), comment='类型名称')
    S_TYPCODE = Column(VARCHAR(40), comment='类型代码')
    S_ORIGIN_TYPCODE = Column(VARCHAR(40), comment='原始类型代码')
    S_CLASSIFICATION = Column(VARCHAR(100), comment='分类')


class ASHARETYPECODEZL(Base):
    """类型编码表(增量)"""
    __tablename__ = 'ASHARETYPECODEZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_TYPNAME = Column(VARCHAR(300), comment='类型名称')
    S_TYPCODE = Column(VARCHAR(40), comment='类型代码')
    S_ORIGIN_TYPCODE = Column(VARCHAR(40), comment='原始类型代码')
    S_CLASSIFICATION = Column(VARCHAR(100), comment='分类')


class ASHAREUNDISTRIBUTEDPROFIT(Base):
    """中国A股财务附注--未分配利润"""
    __tablename__ = 'ASHAREUNDISTRIBUTEDPROFIT'
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


class ASHAREWEEKLYYIELD(Base):
    """中国A股周收益率"""
    __tablename__ = 'ASHAREWEEKLYYIELD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='截至日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_WQ_PCTCHANGE = Column(Numeric(20, 4), comment='周收益率(%)')
    S_WQ_TURN = Column(Numeric(20, 4), comment='周换手率(合计)(%)')
    S_WQ_AVGTURN = Column(Numeric(20, 4), comment='周换手率(算术平均)(%)')
    S_WQ_AMOUNT = Column(Numeric(20, 4), comment='周成交金额(万元)')
    S_RISK_BETAR100 = Column(Numeric(20, 4), comment='BETA (100周)')
    S_WQ_VARPCTCHANGE100 = Column(Numeric(20, 4), comment='周收益率方差(100周)')
    S_WQ_DEVPCTCHANGE100 = Column(Numeric(20, 4), comment='周收益率标准差(100周)')
    S_WQ_AVGPCTCHANGE100 = Column(Numeric(20, 4), comment='周收益率平均值(100周)')


class ASHAREWINDCUSTOMCODE(Base):
    """None"""
    __tablename__ = 'ASHAREWINDCUSTOMCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_ASHARECODE = Column(VARCHAR(10), comment='证券id')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司id')
    S_INFO_SECURITIESTYPES = Column(VARCHAR(10), comment='品种类型(兼容)')
    S_INFO_SECTYPENAME = Column(VARCHAR(40), comment='品种类型(名称)')
    S_INFO_COUNTRYNAME = Column(VARCHAR(100), comment='国家及地区名称')
    S_INFO_COUNTRYCODE = Column(VARCHAR(10), comment='国家及地区代码')
    S_INFO_EXCHMARKETNAME = Column(VARCHAR(40), comment='交易所名称(兼容)')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')
    CRNCY_NAME = Column(VARCHAR(40), comment='交易币种名称')
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


class ASHAREWINNING(Base):
    """中国A股新股中签数据"""
    __tablename__ = 'ASHAREWINNING'
    OBJECT_ID = Column(VARCHAR(40), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    LAST_DIGIT = Column(Numeric(1, 0), comment='末尾位数')
    WINNING_NUMBER = Column(VARCHAR(200), comment='中签号码')


class ASHAREYIELD(Base):
    """中国A股日收益率"""
    __tablename__ = 'ASHAREYIELD'
    __table_args__ = (
        Index('IDX_ASHAREYIELD_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    PCT_CHANGE_D = Column(Numeric(22, 4), comment='日涨跌幅(%)')
    PCT_CHANGE_W = Column(Numeric(22, 4), comment='周涨跌幅(%)')
    PCT_CHANGE_M = Column(Numeric(22, 4), comment='月涨跌幅(%)')
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


class AINDEXALTERNATIVEMEMBERS(Base):
    """中国A股中证指数备选成分股名单"""
    __tablename__ = 'AINDEXALTERNATIVEMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    SEQUENCE = Column(Numeric(20, 0), comment='序号')


class AINDEXCONSENSUSDATA(Base):
    """Wind一致预测指数指标"""
    __tablename__ = 'AINDEXCONSENSUSDATA'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EST_DT = Column(VARCHAR(8), comment='日期')
    EST_REPORT_DT = Column(VARCHAR(8), comment='报告期')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    EST_EPS = Column(Numeric(20, 4), comment='每股收益')
    EST_PE = Column(Numeric(20, 4), comment='市盈率')
    EST_PEG = Column(Numeric(20, 4), comment='PEG')
    EST_PB = Column(Numeric(20, 4), comment='市净率')
    EST_ROE = Column(Numeric(20, 4), comment='净资产收益率')
    EST_OPER_REVENUE = Column(Numeric(20, 4), comment='营业收入')
    EST_CFPS = Column(Numeric(20, 4), comment='每股现金流')
    EST_DPS = Column(Numeric(20, 4), comment='每股股利')
    EST_BPS = Column(Numeric(20, 4), comment='每股净资产')
    EST_EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EST_EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    EST_TOTAL_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    EST_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    EST_OPER_COST = Column(Numeric(20, 4), comment='营业成本及附加')
    EST_SHR = Column(Numeric(20, 4), comment='预测基准股本')
    TYPE1 = Column(VARCHAR(10), comment='类型')


class AINDEXCONSENSUSROLLINGDATA(Base):
    """Wind一致预测指数滚动指标"""
    __tablename__ = 'AINDEXCONSENSUSROLLINGDATA'
    __table_args__ = (
        Index('IDX_AINDEXCONSENSUSROLLINGDATA_EST_DT', 'EST_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='证券ID')
    EST_DT = Column(VARCHAR(8), comment='日期')
    ROLLING_TYPE = Column(VARCHAR(10), comment='类型')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    EST_EPS = Column(Numeric(20, 4), comment='每股收益')
    EST_PE = Column(Numeric(20, 4), comment='市盈率')
    EST_PEG = Column(Numeric(20, 4), comment='PEG')
    EST_ = Column(Numeric(20, 4), comment='市净率')
    EST_ROE = Column(Numeric(20, 4), comment='净资产收益率')
    EST_OPER_REVENUE = Column(Numeric(20, 4), comment='营业收入')
    EST_CFPS = Column(Numeric(20, 4), comment='每股现金流')
    EST_DPS = Column(Numeric(20, 4), comment='每股股利')
    EST_BPS = Column(Numeric(20, 4), comment='每股净资产')
    EST_EBIT = Column(Numeric(20, 4), comment='息税前利润')
    EST_EBITDA = Column(Numeric(20, 4), comment='息税折旧摊销前利润')
    EST_TOTAL_PROFIT = Column(Numeric(20, 4), comment='利润总额')
    EST_OPER_PROFIT = Column(Numeric(20, 4), comment='营业利润')
    EST_OPER_COST = Column(Numeric(20, 4), comment='营业成本及附加')
    BENCHMARK_YR = Column(VARCHAR(8), comment='基准年度')


class AINDEXCSI100WEIGHT(Base):
    """None"""
    __tablename__ = '中证100指数权重'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(10), comment='生效日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    INDEXNAME = Column(VARCHAR(100), comment='指数名称')
    INDEXNAME_ENG = Column(VARCHAR(100), comment='指数英文名称')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EXCHANGE = Column(VARCHAR(20), comment='交易所英文简称')
    TOT_SHR = Column(Numeric(20, 2), comment='总股本(股)')
    FREE_SHR_RATIO = Column(Numeric(20, 4), comment='自由流通比例(%)(归档后)')
    SHR_CALCULATION = Column(Numeric(20, 2), comment='计算用股本(股)')
    WEIGHTFACTOR = Column(Numeric(20, 8), comment='权重因子')
    CLOSEVALUE = Column(Numeric(20, 4), comment='收盘')
    OPEN_ADJUSTED = Column(Numeric(20, 4), comment='调整后开盘参考价')
    TOT_MV = Column(Numeric(20, 2), comment='总市值')
    MV_CALCULATION = Column(Numeric(20, 2), comment='计算用市值')
    WEIGHT = Column(Numeric(20, 4), comment='权重(%)')


class AINDEXCSI500WEIGHT(Base):
    """中证500指数权重"""
    __tablename__ = 'AINDEXCSI500WEIGHT'
    __table_args__ = (
        Index('IDX_AINDEXCSI500WEIGHT_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(10), comment='生效日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    INDEXNAME = Column(VARCHAR(40), comment='指数名称')
    INDEXNAME_ENG = Column(VARCHAR(100), comment='指数英文名称')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EXCHANGE = Column(VARCHAR(20), comment='交易所')
    TOT_SHR = Column(Numeric(20, 2), comment='总股本(股)')
    FREE_SHR_RATIO = Column(Numeric(20, 4), comment='自由流通比例(%)(归档后)')
    SHR_CALCULATION = Column(Numeric(20, 2), comment='计算用股本(股)')
    WEIGHTFACTOR = Column(Numeric(20, 8), comment='权重因子')
    CLOSEVALUE = Column(Numeric(20, 4), comment='收盘')
    OPEN_ADJUSTED = Column(Numeric(20, 4), comment='调整后开盘参考价')
    TOT_MV = Column(Numeric(20, 2), comment='总市值')
    MV_CALCULATION = Column(Numeric(20, 2), comment='计算用市值')
    WEIGHT = Column(Numeric(20, 4), comment='权重(%)')


class AINDEXCSI500WEIGHTWEIGHT(Base):
    """中证500等权重指数权重"""
    __tablename__ = 'AINDEXCSI500WEIGHTWEIGHT'
    __table_args__ = (
        Index('IDX_AINDEXCSI500WEIGHTWEIGHT_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(10), comment='生效日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    INDEX_NAME = Column(VARCHAR(40), comment='指数名称')
    INDEXNAME_ENG = Column(VARCHAR(100), comment='指数英文名称')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份券Wind代码')
    S_EXCHANGE = Column(VARCHAR(40), comment='交易所')
    TOT_SHR = Column(Numeric(20, 2), comment='总股本(股)')
    FREE_SHR_RATIO = Column(Numeric(20, 4), comment='自由流通比例(%)(归档后)')
    SHR_CALCULATION = Column(Numeric(20, 2), comment='计算用股本(股)')
    WEIGHT_FACTOR = Column(Numeric(20, 8), comment='权重因子')
    CLOSE_VALUE = Column(Numeric(20, 4), comment='收盘')
    OPEN_ADJUSTED = Column(Numeric(20, 4), comment='调整后开盘参考价')
    TOT_MV = Column(Numeric(20, 2), comment='总市值')
    MV_CALCULATION = Column(Numeric(20, 2), comment='计算用市值')
    S_WEIGHT = Column(Numeric(20, 4), comment='权重(%)')


class AINDEXCSI800WEIGHT(Base):
    """中证800指数权重"""
    __tablename__ = 'AINDEXCSI800WEIGHT'
    __table_args__ = (
        Index('IDX_AINDEXCSI800WEIGHT_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(10), comment='生效日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    INDEXNAME = Column(VARCHAR(40), comment='指数名称')
    INDEXNAME_ENG = Column(VARCHAR(100), comment='指数英文名称')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EXCHANGE = Column(VARCHAR(20), comment='交易所')
    TOT_SHR = Column(Numeric(20, 2), comment='总股本(股)')
    FREE_SHR_RATIO = Column(Numeric(20, 4), comment='自由流通比例(%)(归档后)')
    SHR_CALCULATION = Column(Numeric(20, 2), comment='计算用股本(股)')
    WEIGHTFACTOR = Column(Numeric(20, 8), comment='权重因子')
    CLOSEVALUE = Column(Numeric(20, 4), comment='收盘')
    OPEN_ADJUSTED = Column(Numeric(20, 4), comment='调整后开盘参考价')
    TOT_MV = Column(Numeric(20, 2), comment='总市值')
    MV_CALCULATION = Column(Numeric(20, 2), comment='计算用市值')
    WEIGHT = Column(Numeric(20, 4), comment='权重(%)')


class AINDEXCSIEMERGINGCOMPWEIGHT(Base):
    """中国战略新兴产业指数权重"""
    __tablename__ = 'AINDEXCSIEMERGINGCOMPWEIGHT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(10), comment='生效日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    INDEXNAME = Column(VARCHAR(100), comment='指数名称')
    INDEXNAME_ENG = Column(VARCHAR(100), comment='指数英文名称')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EXCHANGE = Column(VARCHAR(20), comment='交易所')
    TOT_SHR = Column(Numeric(20, 2), comment='总股本(股)')
    FREE_SHR_RATIO = Column(Numeric(20, 4), comment='自由流通比例(%)(归档后)')
    SHR_CALCULATION = Column(Numeric(20, 2), comment='计算用股本(股)')
    WEIGHTFACTOR = Column(Numeric(20, 8), comment='权重因子')
    CLOSEVALUE = Column(Numeric(20, 4), comment='收盘')
    OPEN_ADJUSTED = Column(Numeric(20, 4), comment='调整后开盘参考价')
    TOT_MV = Column(Numeric(20, 2), comment='总市值')
    MV_CALCULATION = Column(Numeric(20, 2), comment='计算用市值')
    WEIGHT = Column(Numeric(20, 4), comment='权重(%)')


class AINDEXDESCRIPTION(Base):
    """中国A股指数基本资料"""
    __tablename__ = 'AINDEXDESCRIPTION'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(70), comment='证券简称')
    S_INFO_COMPNAME = Column(VARCHAR(100), comment='指数名称')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8), comment='基期')
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4), comment='基点')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='发布日期')
    S_INFO_INDEX_WEIGHTSRULE = Column(VARCHAR(10), comment='加权方式')
    S_INFO_PUBLISHER = Column(VARCHAR(100), comment='发布方')
    S_INFO_INDEXCODE = Column(Numeric(9, 0), comment='指数类别代码')
    S_INFO_INDEXSTYLE = Column(VARCHAR(40), comment='指数风格')
    INDEX_INTRO = Column(TEXT(2147483647), comment='指数简介')
    WEIGHT_TYPE = Column(Numeric(9, 0), comment='权重类型')
    EXPIRE_DATE = Column(VARCHAR(8), comment='终止发布日期')
    INCOME_PROCESSING_METHOD = Column(VARCHAR(20), comment='收益处理方式')
    CHANGE_HISTORY = Column(VARCHAR(100), comment='变更历史')


class AINDEXDESCRIPTIONQL(Base):
    """None"""
    __tablename__ = 'AINDEXDESCRIPTIONQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_CODE = Column(VARCHAR(40))
    S_INFO_NAME = Column(VARCHAR(70))
    S_INFO_COMPNAME = Column(VARCHAR(100))
    S_INFO_EXCHMARKET = Column(VARCHAR(40))
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8))
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4))
    S_INFO_LISTDATE = Column(VARCHAR(8))
    S_INFO_INDEX_WEIGHTSRULE = Column(VARCHAR(10))
    S_INFO_PUBLISHER = Column(VARCHAR(100))
    S_INFO_INDEXCODE = Column(Numeric(9, 0))
    S_INFO_INDEXSTYLE = Column(VARCHAR(40))
    INDEX_INTRO = Column(TEXT(2147483647))
    WEIGHT_TYPE = Column(Numeric(9, 0))
    EXPIRE_DATE = Column(VARCHAR(8))
    INCOME_PROCESSING_METHOD = Column(VARCHAR(20))
    CHANGE_HISTORY = Column(VARCHAR(100))


class AINDEXDESCRIPTIONZL(Base):
    """中国A股指数基本资料(增量)"""
    __tablename__ = 'AINDEXDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_CODE = Column(VARCHAR(40))
    S_INFO_NAME = Column(VARCHAR(50))
    S_INFO_COMPNAME = Column(VARCHAR(100))
    S_INFO_EXCHMARKET = Column(VARCHAR(40))
    S_INFO_INDEX_BASEPER = Column(VARCHAR(8))
    S_INFO_INDEX_BASEPT = Column(Numeric(20, 4))
    S_INFO_LISTDATE = Column(VARCHAR(8))
    S_INFO_INDEX_WEIGHTSRULE = Column(VARCHAR(10))
    S_INFO_PUBLISHER = Column(VARCHAR(100))
    S_INFO_INDEXCODE = Column(Numeric(9, 0))
    S_INFO_INDEXSTYLE = Column(VARCHAR(40))
    INDEX_INTRO = Column(TEXT(2147483647))
    WEIGHT_TYPE = Column(Numeric(9, 0))
    EXPIRE_DATE = Column(VARCHAR(8))
    INCOME_PROCESSING_METHOD = Column(VARCHAR(20))
    CHANGE_HISTORY = Column(VARCHAR(100), comment='变更历史')


class AINDEXEODPRICES(Base):
    """中国A股指数日行情"""
    __tablename__ = 'AINDEXEODPRICES'
    __table_args__ = (
        Index('IDX_AINDEXEODPRICES_CODE_DT', 'S_INFO_WINDCODE', 'TRADE_DT'),
        Index('NonClusteredIndex-20200806-190448', 'S_INFO_WINDCODE', 'TRADE_DT'),
        Index('IDX_AINDEXEODPRICES_TRADE_DT', 'TRADE_DT'),)
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


class AINDEXFINANCIALDERIVATIVE(Base):
    """中国A股指数财务衍生指标"""
    __tablename__ = 'AINDEXFINANCIALDERIVATIVE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    INGREDIENT_NUM = Column(Numeric(20, 0), comment='成分股数量')
    LOSS_INGREDIENT_NUM = Column(Numeric(20, 0), comment='亏损成分股数量')
    NET_PROFIT_TOT = Column(Numeric(20, 4), comment='净利润合计')
    OPER_REV = Column(Numeric(20, 4), comment='营业收入合计')
    S_VAL_PCF_OCF = Column(Numeric(20, 4), comment='经营现金流合计')
    NET_INCR_CASH_CASH_EQU_TOT = Column(Numeric(20, 4), comment='现金及现金等价物净增加额合计')
    TOTAL_ASSETS = Column(Numeric(20, 4), comment='总资产合计')
    TOTAL_NET_ASSETS = Column(Numeric(20, 4), comment='净资产合计')
    TOTAL_INVENTORY = Column(Numeric(20, 4), comment='存货合计')
    TOTAL_ACCOUNTS_RECEIVABLE = Column(Numeric(20, 4), comment='应收账款合计')
    ROE = Column(Numeric(20, 4), comment='ROE')
    ROA = Column(Numeric(20, 4), comment='ROA')
    NET_PROFIT_RATE = Column(Numeric(20, 4), comment='净利润率')
    GROSS_PROFIT_MARGIN = Column(Numeric(20, 4), comment='毛利率')
    ASSETS_LIABILITIES = Column(Numeric(20, 4), comment='资产负债率')
    PERIOD_EXPENSE_RATE = Column(Numeric(20, 4), comment='期间费用率')
    FINANCIAL_LEVERAGE = Column(Numeric(20, 4), comment='财务杠杆')
    ASSET_TURNOVER = Column(Numeric(20, 4), comment='资产周转率')
    NET_ASSET_TURNOVER = Column(Numeric(20, 4), comment='净资产周转率')
    S_FA_INVTURNDAYS = Column(Numeric(20, 4), comment='存货周转天数')
    S_FA_ARTURNDAYS = Column(Numeric(20, 4), comment='应收账款周转天数')
    NET_BUSINESS_CYCLE = Column(Numeric(20, 4), comment='净营业周期')
    NET_CASHFLOW_PROFIT = Column(Numeric(20, 4), comment='现金流净利润比')
    CASHFLOW_INCOME_RATIO = Column(Numeric(20, 4), comment='现金流收入比')
    NET_PROFIT_TTM = Column(Numeric(20, 4), comment='净利润(TTM)')
    OPER_REV_TTM = Column(Numeric(20, 4), comment='营业收入(TTM)')
    S_VAL_PCF_OCF_TTM = Column(Numeric(20, 4), comment='经营现金流(TTM)')
    NET_INCR_CASH_CASH_EQU_TTM = Column(Numeric(20, 4), comment='现金及现金等价物净增加额(TTM)')
    ROE_TTM = Column(Numeric(20, 4), comment='ROE(TTM)')
    ROA_TTM = Column(Numeric(20, 4), comment='ROA(TTM)')
    NET_PROFIT_RATE_TTM = Column(Numeric(20, 4), comment='净利润率(TTM)')
    NET_PROFIT_GROWTH_RATE = Column(Numeric(20, 4), comment='净利润同比增速')
    NET_PROFIT_GROWTH_RATE_TTM = Column(Numeric(20, 4), comment='净利润同比增速(TTM)')
    NET_PROFIT_GROWTH_RATE_QUA = Column(Numeric(20, 4), comment='单季度:净利润同比增速')
    NET_PROFIT_GROWTH_RATE_CHAIN = Column(Numeric(20, 4), comment='单季度:净利润环比增速')
    OPER_REV_GROWTH_RATE = Column(Numeric(20, 4), comment='营业收入同比增速')
    OPER_REV_GROWTH_RATE_TTM = Column(Numeric(20, 4), comment='营业收入同比增速(TTM)')
    OPER_REV_GROWTH_RATE_QUA = Column(Numeric(20, 4), comment='单季度:营业收入同比增速')
    OPER_REV_GROWTH_RATE_CHAIN = Column(Numeric(20, 4), comment='单季度:营业收入环比增速')
    S_VAL_PCF_OCF_GROWTH_RATE = Column(Numeric(20, 4), comment='经营现金流同比增速')
    S_VAL_PCF_OCF_GROWTH_RATE_TTM = Column(Numeric(20, 4), comment='经营现金流同比增速(TTM)')
    S_VAL_PCF_OCF_QUA = Column(Numeric(20, 4), comment='单季度:经营现金流同比增速')
    S_VAL_PCF_OCF_CHAIN = Column(Numeric(20, 4), comment='单季度:经营现金流环比增速')
    ROE_INCREASE_LESS = Column(Numeric(20, 4), comment='ROE同比增减')
    ROE_INCREASE_LESS_TTM = Column(Numeric(20, 4), comment='ROE同比增减(TTM)')
    ROE_INCREASE_LESS_QUA = Column(Numeric(20, 4), comment='单季度:ROE同比增减')
    ROE_INCREASE_LESS_CHAIN = Column(Numeric(20, 4), comment='单季度:ROE环比增减')
    ROA_INCREASE_LESS = Column(Numeric(20, 4), comment='ROA同比增减')
    ROA_INCREASE_LESS_TTM = Column(Numeric(20, 4), comment='ROA同比增减(TTM)')
    ROA_INCREASE_LESS_QUA = Column(Numeric(20, 4), comment='单季度:ROA同比增减')
    ROA_INCREASE_LESS_CHAIN = Column(Numeric(20, 4), comment='单季度:ROA环比增减')
    NET_PRO_RATE_INCREASE_LESS = Column(Numeric(20, 4), comment='净利润率同比增减')
    NET_PRO_RATE_INC_LESS_TTM = Column(Numeric(20, 4), comment='净利率同比增减(TTM)')
    NET_PRO_RATE_INC_LESS_QUA = Column(Numeric(20, 4), comment='单季度:净利润率同比增减')
    NET_PRO_RATE_INC_LESS_CHAIN = Column(Numeric(20, 4), comment='单季度:净利润率环比增减')
    GROSSPROFIT_MARGIN_INC_LESS = Column(Numeric(20, 4), comment='毛利率同比增减')
    GROSS_MARGIN_INC_LESS_QUA = Column(Numeric(20, 4), comment='单季度:毛利率同比增减')
    GROSS_MARGIN_INC_LESS_CHAIN = Column(Numeric(20, 4), comment='单季度:毛利率环比增减')
    PERIOD_EXPENSE_INC_LESS = Column(Numeric(20, 4), comment='期间费用率同比增减')
    PERIOD_EXPENSE_INC_LESS_QUA = Column(Numeric(20, 4), comment='单季度:期间费用率同比增减')
    PERIOD_EXPENSE_INC_LESS_CHAIN = Column(Numeric(20, 4), comment='单季度:期间费用率环比增减')
    NET_ASSETS_GROWTH_RATE = Column(Numeric(20, 4), comment='净资产比年初增速')
    ASSETS_GROWTH_RATE = Column(Numeric(20, 4), comment='总资产比年初增速')
    STOCK_RATIO_GROWTH_RATE = Column(Numeric(20, 4), comment='存货比年初增速')
    ACCOUNTS_GROWTH_RATE = Column(Numeric(20, 4), comment='应收账款比年初增速')
    REPORT_TYPE_CODE = Column(Numeric(9, 0), comment='报表类型代码')
    S_FA_CURRENT = Column(Numeric(20, 4), comment='流动比率')
    S_FA_QUICK = Column(Numeric(20, 4), comment='速动比率')
    SALES_EXPENSE_RATE = Column(Numeric(20, 4), comment='销售费用率')
    SALES_EXPENSE_RATE_QUA = Column(Numeric(20, 4), comment='单季度:销售费用率')
    PERIOD_EXPENSE_RATE_QUA = Column(Numeric(20, 4), comment='单季度:期间费用率')
    NET_PROFIT_RATE_QUA = Column(Numeric(20, 4), comment='单季度:净利润率')
    PROFIT_RATE_QUA = Column(Numeric(20, 4), comment='单季度:毛利率')
    ROE_QUA = Column(Numeric(20, 4), comment='单季度:ROE')
    ROA_QUA = Column(Numeric(20, 4), comment='单季度:ROA')
    OPER_COST_TOT = Column(Numeric(20, 4), comment='营业成本合计')
    SELLING_DIST_EXP_TOT = Column(Numeric(20, 4), comment='销售费用合计')
    GERL_ADMIN_EXP_TOT = Column(Numeric(20, 4), comment='管理费用合计')
    FIN_EXP_TOT = Column(Numeric(20, 4), comment='财务费用合计')
    IMPAIR_LOSS_ASSETS_TOT = Column(Numeric(20, 4), comment='资产减值损失合计')
    NET_GAIN_CHG_FV_TOT = Column(Numeric(20, 4), comment='公允价值变动净收益合计')
    NET_INVEST_INC_TOT = Column(Numeric(20, 4), comment='投资净收益合计')
    OPER_PROFIT_TOT = Column(Numeric(20, 4), comment='营业利润合计')
    NON_OPER_REV_TOT = Column(Numeric(20, 4), comment='营业外收入合计')
    NON_OPER_EXP_TOT = Column(Numeric(20, 4), comment='营业外支出合计')
    TOT_PROFIT = Column(Numeric(20, 4), comment='利润总额合计')
    INC_TAX_TOT = Column(Numeric(20, 4), comment='所得税合计')
    NET_PROFIT_INCL_MIN_INT_INC = Column(Numeric(20, 4), comment='净利润(含少数股东权益)合计')
    NET_AFTER_DED_NR_LP_CORRECT = Column(Numeric(20, 4), comment='扣非归属净利润合计')
    S_FA_EXTRAORDINARY = Column(Numeric(20, 4), comment='非经常性损益合计')
    S_FA_SALESCASHINTOOR = Column(Numeric(20, 4), comment='销售商品提供劳务收到的现金合计')
    STOT_CASH_INFLOWS_OPER_TOT = Column(Numeric(20, 4), comment='经营活动现金流入合计')
    CASH_PAY_GOODS_PURCH_SERV_REC = Column(Numeric(20, 4), comment='购买商品支付的现金合计')
    CASH_PAY_BEH_EMPL = Column(Numeric(20, 4), comment='支付给职工以及为职工支付的现金合计')
    STOT_CASH_OUTFLOWS_OPER_TOT = Column(Numeric(20, 4), comment='经营活动现金流出合计')
    NET_CASH_RECP_DISP_FIOLTA = Column(Numeric(20, 4), comment='处置固定资产等收回的现金合计')
    STOT_CASH_INFLOWS_INV_TOT = Column(Numeric(20, 4), comment='投资活动现金流入合计')
    CASH_PAY_ACQ_CONST_FIOLTA = Column(Numeric(20, 4), comment='购建固定无形和长期资产支付的现金合计')
    CASH_PAID_INVEST = Column(Numeric(20, 4), comment='投资支付的现金合计')
    CASH_PAID_INVEST_TOT = Column(Numeric(20, 4), comment='投资现金流出合计')
    NET_CASH_FLOWS_INV_TOT = Column(Numeric(20, 4), comment='投资活动净流量合计')
    CASH_RECP_CAP_CONTRIB = Column(Numeric(20, 4), comment='吸收投资收到的现金合计')
    CASH_RECP_BORROW = Column(Numeric(20, 4), comment='取得借款收到的现金合计')
    PROC_ISSUE_BONDS = Column(Numeric(20, 4), comment='发行债券收到的现金合计')
    STOT_CASH_INFLOWS_FNC_TOT = Column(Numeric(20, 4), comment='筹资活动现金流入合计')
    CASH_PREPAY_AMT_BORR = Column(Numeric(20, 4), comment='偿付债务支付的现金合计')
    CASH_PAY_DIST_DPCP_INT_EXP = Column(Numeric(20, 4), comment='分配股利偿付利息支付的现金合计')
    STOT_CASH_OUTFLOWS_FNC_TOT = Column(Numeric(20, 4), comment='筹资活动现金流出合计')
    NET_CASH_FLOWS_FNC_TOT = Column(Numeric(20, 4), comment='筹资活动净流量合计')
    CASH_CASH_EQU_END_PERIOD = Column(Numeric(20, 4), comment='期末现金合计')
    MONETARY_CAP = Column(Numeric(20, 4), comment='货币资金合计')
    NOTES_RCV = Column(Numeric(20, 4), comment='应收票据合计')
    ACCT_RCV = Column(Numeric(20, 4), comment='应收账款合计')
    PREPAY = Column(Numeric(20, 4), comment='预付款项合计')
    TOT_CUR_ASSETS = Column(Numeric(20, 4), comment='流动资产合计')
    LONG_TERM_EQY_INVEST = Column(Numeric(20, 4), comment='长期股权投资合计')
    INVEST_REAL_ESTATE = Column(Numeric(20, 4), comment='投资性房地产合计')
    FIX_ASSETS = Column(Numeric(20, 4), comment='固定资产合计')
    CONST_IN_PROG = Column(Numeric(20, 4), comment='在建工程合计')
    TOT_NON_CUR_ASSETS = Column(Numeric(20, 4), comment='非流动资产合计')
    ST_BORROW = Column(Numeric(20, 4), comment='短期借款合计')
    NOTES_PAYABLE = Column(Numeric(20, 4), comment='应付票据合计')
    ACCT_PAYABLE = Column(Numeric(20, 4), comment='应付账款合计')
    ADV_FROM_CUST = Column(Numeric(20, 4), comment='预收账款合计')
    EMPL_BEN_PAYABLE = Column(Numeric(20, 4), comment='应付职工薪酬合计')
    NON_CUR_LIAB_DUE_WITHIN_1Y = Column(Numeric(20, 4), comment='一年内到期的非流动负债合计')
    TOT_CUR_LIAB = Column(Numeric(20, 4), comment='流动负债合计')
    LT_BORROW = Column(Numeric(20, 4), comment='长期借款合计')
    BONDS_PAYABLE = Column(Numeric(20, 4), comment='应付债券合计')
    TOT_NON_CUR_LIAB = Column(Numeric(20, 4), comment='非流动负债合计')
    PAID_UP_CAPITAL = Column(Numeric(20, 4), comment='实收资本合计')
    CAP_RSRV = Column(Numeric(20, 4), comment='资本公积金合计')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='未分配利润合计')
    OWNERS_EQUITY = Column(Numeric(20, 4), comment='所有者权益合计')


class AINDEXHS300CLOSEWEIGHT(Base):
    """沪深300指数成份股当日收盘权重"""
    __tablename__ = 'AINDEXHS300CLOSEWEIGHT'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE_TRADE_DT', 'S_INFO_WINDCODE', 'TRADE_DT'),
        Index('IDX_AINDEXHS300CLOSEWEIGHT_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    TRADE_DT = Column(VARCHAR(10), comment='交易日期')
    I_WEIGHT = Column(Numeric(20, 4), comment='权重')
    S_IN_INDEX = Column(Numeric(20, 2), comment='计算用股本(股)')
    I_WEIGHT_11 = Column(Numeric(20, 2), comment='总股本(股)')
    I_WEIGHT_12 = Column(VARCHAR(2), comment='自由流通比例(%)(归档后)')
    I_WEIGHT_14 = Column(Numeric(20, 8), comment='权重因子')
    I_WEIGHT_15 = Column(Numeric(20, 4), comment='收盘')
    I_WEIGHT_16 = Column(VARCHAR(2), comment='调整后开盘参考价')
    I_WEIGHT_17 = Column(Numeric(20, 2), comment='总市值')
    I_WEIGHT_18 = Column(Numeric(20, 2), comment='计算用市值')


class AINDEXHS300FREEWEIGHT(Base):
    """沪深300免费指数权重"""
    __tablename__ = 'AINDEXHS300FREEWEIGHT'
    __table_args__ = (
        Index('IDX_AINDEXHS300FREEWEIGHT_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    I_WEIGHT = Column(Numeric(20, 4), comment='权重')


class AINDEXHS300WEIGHT(Base):
    """沪深300指数成份股次日开盘权重"""
    __tablename__ = 'AINDEXHS300WEIGHT'
    __table_args__ = (
        Index('IDX_AINDEXHS300WEIGHT_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    I_WEIGHT = Column(Numeric(20, 4), comment='权重')
    S_IN_INDEX = Column(Numeric(20, 2), comment='计算用股本(股)')
    I_WEIGHT_11 = Column(Numeric(20, 2), comment='总股本(股)')
    I_WEIGHT_12 = Column(Numeric(20, 4), comment='自由流通比例(%)(归档后)')
    I_WEIGHT_14 = Column(Numeric(20, 8), comment='权重因子')
    I_WEIGHT_15 = Column(Numeric(20, 4), comment='收盘')
    I_WEIGHT_16 = Column(Numeric(20, 4), comment='调整后开盘参考价')
    I_WEIGHT_17 = Column(Numeric(20, 2), comment='总市值')
    I_WEIGHT_18 = Column(Numeric(20, 2), comment='计算用市值')


class AINDEXINDUSTRIESEODCITICS(Base):
    """中国A股中信行业指数日行情"""
    __tablename__ = 'AINDEXINDUSTRIESEODCITICS'
    __table_args__ = (
        Index('IDX_AINDEXINDUSTRIESEODCITICS_TRADE_DT', 'TRADE_DT'),)
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


class AINDEXMEMBERS(Base):
    """中国A股指数成份股"""
    __tablename__ = 'AINDEXMEMBERS'
    __table_args__ = (
        Index('fass', 'S_INFO_WINDCODE', 'S_CON_WINDCODE', 'S_CON_INDATE', 'S_CON_OUTDATE'),
        Index('INDEX_S_INFO_WINDCODE_INDATE', 'S_INFO_WINDCODE', 'S_CON_INDATE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXMEMBERSCITICS(Base):
    """中国A股中信指数成份股"""
    __tablename__ = 'AINDEXMEMBERSCITICS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXMEMBERSCITICS2(Base):
    """中国A股中信指数成份股二级"""
    __tablename__ = 'AINDEXMEMBERSCITICS2'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXMEMBERSCITICS2ZL(Base):
    """中国A股中信指数成份股二级(增量)"""
    __tablename__ = 'AINDEXMEMBERSCITICS2ZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXMEMBERSCITICS3(Base):
    """中国A股中信指数成份股三级"""
    __tablename__ = 'AINDEXMEMBERSCITICS3'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXMEMBERSCITICS3ZL(Base):
    """中国A股中信指数成份股三级(增量)"""
    __tablename__ = 'AINDEXMEMBERSCITICS3ZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXMEMBERSCITICSZL(Base):
    """中国A股中信指数成份股(增量)"""
    __tablename__ = 'AINDEXMEMBERSCITICSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXMEMBERSWIND(Base):
    """中国A股万得指数成份股"""
    __tablename__ = 'AINDEXMEMBERSWIND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXMEMBERSWINDQL(Base):
    """None"""
    __tablename__ = 'AINDEXMEMBERSWINDQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    F_INFO_WINDCODE = Column(VARCHAR(40))
    S_CON_WINDCODE = Column(VARCHAR(40))
    S_CON_INDATE = Column(VARCHAR(8))
    S_CON_OUTDATE = Column(VARCHAR(8))
    CUR_SIGN = Column(Numeric(1, 0))


class AINDEXMEMBERSWINDZL(Base):
    """中国A股万得指数成份股(增量)"""
    __tablename__ = 'AINDEXMEMBERSWINDZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class AINDEXSSE50WEIGHT(Base):
    """上证50指数权重"""
    __tablename__ = 'AINDEXSSE50WEIGHT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(10), comment='生效日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    INDEXNAME = Column(VARCHAR(100), comment='指数名称')
    INDEXNAME_ENG = Column(VARCHAR(100), comment='指数英文名称')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EXCHANGE = Column(VARCHAR(20), comment='交易所')
    TOT_SHR = Column(Numeric(20, 2), comment='总股本(股)')
    FREE_SHR_RATIO = Column(Numeric(20, 4), comment='自由流通比例(%)(归档后)')
    SHR_CALCULATION = Column(Numeric(20, 2), comment='计算用股本(股)')
    WEIGHTFACTOR = Column(Numeric(20, 8), comment='权重因子')
    CLOSEVALUE = Column(Numeric(20, 4), comment='收盘')
    OPEN_ADJUSTED = Column(Numeric(20, 4), comment='调整后开盘参考价')
    TOT_MV = Column(Numeric(20, 2), comment='总市值')
    MV_CALCULATION = Column(Numeric(20, 2), comment='计算用市值')
    WEIGHT = Column(Numeric(20, 4), comment='权重(%)')


class AINDEXVALUATION(Base):
    """中国A股指数估值数据"""
    __tablename__ = 'AINDEXVALUATION'
    __table_args__ = (
        Index('IDX_AINDEXVALUATION_TRADE_DT', 'TRADE_DT'),
        Index('NonClusteredIndex-20201103-142352', 'S_INFO_WINDCODE', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CON_NUM = Column(Numeric(20, 4), comment='成分股数量')
    PE_LYR = Column(Numeric(20, 4), comment='市盈率(PE,LYR)')
    PE_TTM = Column(Numeric(20, 4), comment='市盈率(PE,TTM)')
    PB_LF = Column(Numeric(20, 4), comment='市净率(PB,LF)')
    PCF_LYR = Column(Numeric(20, 4), comment='市现率(PCF,LYR)')
    PCF_TTM = Column(Numeric(20, 4), comment='市现率(PCF,TTM)')
    PS_LYR = Column(Numeric(20, 4), comment='市销率(PS,LYR)')
    PS_TTM = Column(Numeric(20, 4), comment='市销率(PS,TTM)')
    MV_TOTAL = Column(Numeric(24, 4), comment='当日总市值合计（元）')
    MV_FLOAT = Column(Numeric(24, 4), comment='当日流通市值合计（元）')
    DIVIDEND_YIELD = Column(Numeric(20, 4), comment='股息率')
    PEG_HIS = Column(Numeric(20, 4), comment='历史PEG')
    TOT_SHR = Column(Numeric(24, 4), comment='总股本合计（股）')
    TOT_SHR_FLOAT = Column(Numeric(24, 4), comment='流通股本合计（股）')
    TOT_SHR_FREE = Column(Numeric(24, 4), comment='自由流通股本合计（股）')
    TURNOVER = Column(Numeric(20, 4), comment='换手率')
    TURNOVER_FREE = Column(Numeric(20, 4), comment='换手率(自由流通)')
    EST_NET_PROFIT_Y1 = Column(Numeric(20, 4), comment='预测净利润(Y1)')
    EST_NET_PROFIT_Y2 = Column(Numeric(20, 4), comment='预测净利润(Y2)')
    EST_BUS_INC_Y1 = Column(Numeric(20, 4), comment='预测营业收入(Y1)')
    EST_BUS_INC_Y2 = Column(Numeric(20, 4), comment='预测营业收入(Y2)')
    EST_EPS_Y1 = Column(Numeric(20, 4), comment='预测每股收益(Y1)')
    EST_EPS_Y2 = Column(Numeric(20, 4), comment='预测每股收益(Y2)')
    EST_YOYPROFIT_Y1 = Column(Numeric(20, 4), comment='预测净利润同比增速(Y1)')
    EST_YOYPROFIT_Y2 = Column(Numeric(20, 4), comment='预测净利润同比增速(Y2)')
    EST_YOYGR_Y1 = Column(Numeric(20, 4), comment='预测营业收入同比增速(Y1)')
    EST_YOYGR_Y2 = Column(Numeric(20, 4), comment='预测营业收入同比增速(Y2)')
    EST_PE_Y1 = Column(Numeric(20, 4), comment='预测PE(Y1)')
    EST_PE_Y2 = Column(Numeric(20, 4), comment='预测PE(Y2)')
    EST_PEG_Y1 = Column(Numeric(20, 4), comment='预测PEG(Y1)')
    EST_PEG_Y2 = Column(Numeric(20, 4), comment='预测PEG(Y2)')


class AINDEXWINDINDUSTRIESEOD(Base):
    """中国A股Wind行业指数日行情"""
    __tablename__ = 'AINDEXWINDINDUSTRIESEOD'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
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


class COMMITPROFIT(Base):
    """中国A股盈利承诺明细表"""
    __tablename__ = 'COMMITPROFIT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    EVENT_ID = Column(VARCHAR(40), comment='事件ID')
    TARGETCOMP_CODE = Column(VARCHAR(40), comment='标的公司ID')
    TARGETCOMPNAME = Column(VARCHAR(100), comment='[内部]标的公司名称')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMMITANN_DT = Column(VARCHAR(8), comment='承诺公告日')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    COMMITNETPROFIT = Column(Numeric(20, 4), comment='承诺净利润(元)')


class COMMITPROFITSUMMARY(Base):
    """中国A股盈利承诺汇总表"""
    __tablename__ = 'COMMITPROFITSUMMARY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    EVENT_ID = Column(VARCHAR(40), comment='事件ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_COMMITANN_DT = Column(VARCHAR(8), comment='承诺公告日')
    ANN_DT = Column(VARCHAR(8), comment='最新公告日')
    TARGETCOMP = Column(VARCHAR(400), comment='标的公司')
    COMMITNETPROFIT = Column(Numeric(20, 4), comment='承诺净利润(元)')
    ACTUALNETPROFIT = Column(Numeric(20, 4), comment='实际净利润(元)')
    ISCOMMITPROFITSUPPLY = Column(Numeric(1, 0), comment='是否承诺利润补充')
    ISNEEDSUPPLY = Column(Numeric(1, 0), comment='是否需要补充')
    SUPPLYCONTENT = Column(Numeric(9, 0), comment='补偿内容代码')
    INJECTEDASSETNETPROFITEST = Column(Numeric(20, 4), comment='注入资产净利润预测(元)')
    EARNINGEST = Column(Numeric(20, 4), comment='上市公司盈利预测(元)')
    SUPPLYTYPE = Column(Numeric(9, 0), comment='盈利补偿方法代码')


class CSIHEALTHCARE100INDEXWEIGHT(Base):
    """中证医药100指数权重"""
    __tablename__ = 'CSIHEALTHCARE100INDEXWEIGHT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(10), comment='生效日期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    INDEXNAME = Column(VARCHAR(100), comment='指数名称')
    INDEXNAME_ENG = Column(VARCHAR(100), comment='指数英文名称')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    EXCHANGE = Column(VARCHAR(40), comment='交易所')
    TOT_SHR = Column(Numeric(20, 2), comment='总股本(股)')
    FREE_SHR_RATIO = Column(Numeric(20, 4), comment='自由流通比例(%)(归档后)')
    SHR_CALCULATION = Column(Numeric(20, 2), comment='计算用股本(股)')
    WEIGHTFACTOR = Column(Numeric(20, 8), comment='权重因子')
    CLOSEVALUE = Column(Numeric(20, 4), comment='收盘')
    OPEN_ADJUSTED = Column(Numeric(20, 4), comment='调整后开盘参考价')
    TOT_MV = Column(Numeric(20, 2), comment='总市值')
    MV_CALCULATION = Column(Numeric(20, 2), comment='计算用市值')
    WEIGHT = Column(Numeric(20, 4), comment='权重(%)')


class CSIIMPLICITDEFAULTRATE(Base):
    """中证隐含违约率及隐含评级数据"""
    __tablename__ = 'CSIIMPLICITDEFAULTRATE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(100), comment='日期')
    IMPLICIT_DEFAULT_RATE = Column(Numeric(20, 4), comment='隐含违约率')
    CSI_CREDITRATING = Column(VARCHAR(40), comment='隐含评级')


class CSINDUSANALYSIS(Base):
    """中证行业估值"""
    __tablename__ = 'CSINDUSANALYSIS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    INDUSTRIESCODE = Column(VARCHAR(10), comment='行业代码')
    MARKETCODE = Column(Numeric(9, 0), comment='市场代码')
    INDUST_VAL_PE = Column(Numeric(20, 4), comment='市盈率-加权平均')
    INDUST_VAL_PE_TTM = Column(Numeric(20, 4), comment='市盈率【TTM】-加权平均')
    INDUST_VAL_PB = Column(Numeric(20, 4), comment='市净率')
    SAMPLE_NUM = Column(Numeric(20, 4), comment='样本券个数')


class CSITOTALBONDINDEEODPRICE(Base):
    """中证全债指数行情"""
    __tablename__ = 'CSITOTALBONDINDEEODPRICE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_DQ_INDEXVALUE = Column(Numeric(20, 4), comment='指数值')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交量(万元)')
    S_DQ_SETTLE = Column(Numeric(20, 4), comment='结算金额(万元)')
    S_DQ_MODIFIEDDURATION = Column(Numeric(20, 4), comment='修正久期')
    S_DQ_CNVXTY = Column(Numeric(20, 4), comment='凸性')
    S_DQ_YIELD = Column(Numeric(20, 4), comment='到期收益率(%)')
    S_DQ_MODIDURA = Column(Numeric(20, 4), comment='久期')
    S_DQ_INDEX_SIZE = Column(Numeric(5, 0), comment='指数样本数量')
    S_DQ_AVGPRICE = Column(Numeric(20, 4), comment='平均价格')


class HS300IEODPRICES(Base):
    """沪深300指数日行情"""
    __tablename__ = 'HS300IEODPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PRE_CLOSE = Column(Numeric(20, 4), comment='昨收盘价(点)')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价(点)')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价(点)')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价(点)')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='收盘价(点)')
    CHG = Column(Numeric(20, 4), comment='涨跌(点)')
    PCT_CHG = Column(Numeric(20, 4), comment='涨跌幅(%)')
    VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    AMT = Column(Numeric(20, 4), comment='成交金额(千元)')


class MERGERAGENCY(Base):
    """中国A股并购事件中介机构"""
    __tablename__ = 'MERGERAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    EVENT_ID = Column(VARCHAR(20), comment='并购事件ID')
    AGENCY_NAME = Column(VARCHAR(200), comment='中介机构公司名称')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='中介机构公司ID')
    AGENCY_TYPCODE = Column(Numeric(9, 0), comment='中介机构类型代码')
    OBJECT_TYPCODE = Column(Numeric(9, 0), comment='中介机构服务对象类型代码')
    OBJECT_COMPNAME = Column(VARCHAR(200), comment='中介机构服务对象（公司）名称')
    S_INFO_COMPCODE2 = Column(VARCHAR(40), comment='中介机构服务对象（公司）ID')
    START_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class MERGEREVENT(Base):
    """中国A股并购事件"""
    __tablename__ = 'MERGEREVENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    EVENT_ID = Column(VARCHAR(20), comment='并购事件ID')
    ANN_DATE = Column(VARCHAR(8), comment='首次披露日期')
    UPDATE_DATE = Column(VARCHAR(8), comment='最新披露日期')
    EVENT_TITLE = Column(VARCHAR(200), comment='并购事件标题')
    UNDERLYING = Column(VARCHAR(200), comment='交易标的')
    UNDERLYING_TYPE_CODE = Column(Numeric(9, 0), comment='标的类型代码')
    IS_RELATED_PARTY_TRANSAC = Column(Numeric(1, 0), comment='是否为关联交易')
    IS_MAJORASSETRESTRUCTURE = Column(Numeric(1, 0), comment='是否重大资产重组')
    IS_CONTROL_CHANGE = Column(Numeric(1, 0), comment='控制权是否变更')
    RESTRUCTURE_WAY_CODE = Column(Numeric(9, 0), comment='重组形式代码')
    RESTRUCTURE_TYPE_CODE = Column(Numeric(9, 0), comment='重组类型代码')
    MERGER_TYPE_CODE = Column(Numeric(9, 0), comment='并购类型代码')
    MERGER_WAY_CODE = Column(Numeric(9, 0), comment='并购方式代码')
    IS_BE_APPROVAL = Column(Numeric(1, 0), comment='是否已完成审批')
    PROGRESS_CODE = Column(Numeric(9, 0), comment='交易方案进度代码')
    TRADE_VALUE = Column(Numeric(20, 4), comment='交易总价值(万元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    PRICING_BASIS_CODE = Column(Numeric(9, 0), comment='定价依据代码')
    EVALUE_METHOD_CODE = Column(Numeric(9, 0), comment='评估方法代码')
    EVALUE_WAY_CODE = Column(Numeric(9, 0), comment='选用评估方法代码')
    PAYMENT_WAY_CODE = Column(Numeric(9, 0), comment='支付方式代码')
    CASH_PAYMENT = Column(Numeric(20, 4), comment='买方支付现金(万元)')
    EVALUE_VALUE = Column(Numeric(20, 4), comment='评估价值')
    EVALUE_BASIS_DATE_ = Column(VARCHAR(8), comment='资产评估基准日')
    TRANSFER_NUMBERS = Column(Numeric(20, 4), comment='转让股数(万股)')
    TRANSFER_PRICE = Column(Numeric(20, 4), comment='转让单价')
    STOCKRIGHT_PROPORTION = Column(Numeric(20, 4), comment='交易股权占比(%)')
    APPRECIATION_RATE = Column(Numeric(20, 4), comment='增值率')
    MERGER_AIM_CODE = Column(Numeric(9, 0), comment='并购目的类型代码')
    LOCATION_TYPE_CODE = Column(Numeric(9, 0), comment='并购地区类型代码')
    ECD = Column(VARCHAR(8), comment='交易预计完成日期')
    COMPLETION_DATE = Column(VARCHAR(8), comment='交易完成日期')
    CHRONICLE = Column(TEXT(2147483647), comment='并购大事记')
    RELEVANTINTELLIGENCE_ID = Column(VARCHAR(20), comment='关联情报ID')
    IS_MERGER = Column(Numeric(1, 0), comment='是否并购')


class MERGERINTELLIGENCE(Base):
    """中国A股前瞻性情报"""
    __tablename__ = 'MERGERINTELLIGENCE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INTELLIGENCE_ID = Column(VARCHAR(20), comment='情报ID')
    TITLE = Column(VARCHAR(400), comment='标题')
    ANN_DATE = Column(VARCHAR(8), comment='发布日期')
    INVOLVED_AMOUNT = Column(VARCHAR(1000), comment='涉及金额')
    SUBJECT_TYPECODE = Column(Numeric(9, 0), comment='主题分类代码')
    WIND_IND_CODE = Column(VARCHAR(10), comment='所属Wind行业代码')
    LEVEL_CODE = Column(Numeric(9, 0), comment='情报等级代码')
    KEY_WORDS = Column(VARCHAR(100), comment='情报关键字')
    DATA_SOURCE = Column(VARCHAR(200), comment='来源名称')
    INVOLVED_EQUITY = Column(VARCHAR(200), comment='涉及股权')
    CONTENT = Column(VARCHAR(3000), comment='正文内容')
    EVENT_ID = Column(VARCHAR(20), comment='交易事件ID')
    PROGRESS_CODE = Column(Numeric(9, 0), comment='事件进度代码')
    RECEIPT_DATE = Column(DateTime, comment='收录时间')
    IS_IMPORTANT = Column(Numeric(1, 0), comment='是否重要')
    EFFECTIVE_DATE = Column(VARCHAR(8), comment='生效日期')


class MERGERPARTICIPANT(Base):
    """中国A股并购事件参与方"""
    __tablename__ = 'MERGERPARTICIPANT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    EVENT_ID = Column(VARCHAR(20), comment='情报ID(或事件ID)')
    PARTY_NAME = Column(VARCHAR(200), comment='参与方名称')
    COUNTRY_CODE = Column(VARCHAR(10), comment='所属国家或地区代码')
    PARTY_ID = Column(VARCHAR(10), comment='参与方ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='参与方关联证券Wind代码')
    PARTY_TYPE_CODE = Column(Numeric(9, 0), comment='参与方类型代码')
    RELATIONSHIP = Column(Numeric(9, 0), comment='参与方与关联证券代码关系')
    PARTY_ROLE_CODE = Column(Numeric(9, 0), comment='参与方角色代码')
    PRE_PROPORTION = Column(Numeric(20, 4), comment='转让前持股比例')
    AFTER_PROPORTION = Column(Numeric(20, 4), comment='转让后持股比例')
    STOCKRIGHT_PROPORTION = Column(Numeric(20, 4), comment='标的方交易股权占比')
    EVALUE_VALUE = Column(Numeric(20, 4), comment='标的方评估价值')
    APPRECIATION_RATE = Column(Numeric(20, 4), comment='标的方增值率')


class SHAREFUNDSTYLETHRESHOLD(Base):
    """中国A股股票风格分类阈值(基金重仓股)"""
    __tablename__ = 'SHAREFUNDSTYLETHRESHOLD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_CHANGE_DATE = Column(VARCHAR(8), comment='变动日期')
    THRESHOLD_LARGE_STOCK = Column(Numeric(20, 4), comment='大盘股门限值(万元)')
    THRESHOLD_MID_STOCK = Column(Numeric(20, 4), comment='中盘股门限值(万元)')
    THRESHOLD_GROWTH_STOCK = Column(Numeric(20, 4), comment='成长型门限值')
    THRESHOLD_VALUE_STOCK = Column(Numeric(20, 4), comment='价值型门限值')
    DATE_CLOSING_DATE = Column(VARCHAR(8), comment='引用数据的截止日期')


class SWINDEXMEMBERS(Base):
    """申万指数成份明细"""
    __tablename__ = 'SWINDEXMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class SWINDEXMEMBERSQL(Base):
    """None"""
    __tablename__ = 'SWINDEXMEMBERSQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_CON_WINDCODE = Column(VARCHAR(40))
    S_CON_INDATE = Column(VARCHAR(8))
    S_CON_OUTDATE = Column(VARCHAR(8))
    CUR_SIGN = Column(Numeric(1, 0))


class SWINDEXMEMBERSZL(Base):
    """申万指数成份明细(增量)"""
    __tablename__ = 'SWINDEXMEMBERSZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
