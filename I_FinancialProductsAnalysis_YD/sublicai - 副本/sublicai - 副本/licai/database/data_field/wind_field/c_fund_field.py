# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/10/21 10:53
# @Author  : lisl3
# @File    : c_fund_field.py
# @Project : cscfist
# @Function: 中国基金
# @Version : V0.0.1
# ------------------------------
from sqlalchemy import Column, VARCHAR, Numeric, TEXT, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CFUNDADMPERMITSCHEDULE(Base):
    """中国共同基金行政许可事项进度表"""
    __tablename__ = 'CFUNDADMPERMITSCHEDULE'
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
    COMP_NAME = Column(VARCHAR(300), comment='[内部]申请人名称')
    PROGRESS_CODE = Column(Numeric(9, 0), comment='审核进度代码')
    ANN_DATE_NDRC = Column(VARCHAR(8), comment='审结日期')
    AUDIT_EVENT_ID = Column(VARCHAR(40), comment='审核事件ID')
    AUDIT_CHANNEL_CODE = Column(Numeric(9, 0), comment='审核通道代码')
    FEEDBACK_DATE = Column(VARCHAR(8), comment='反馈回复日期')
    OTHER_COMP_ID = Column(VARCHAR(10), comment='其他公司ID')
    OTHER_COMP_TYPE_CODE = Column(Numeric(9, 0), comment='其他公司类型代码')
    SEC_CODE = Column(VARCHAR(10), comment='[内部]审批产品证券ID')


class CFUNDBANKACCOUNT(Base):
    """中国基金公司银行账号信息表"""
    __tablename__ = 'CFUNDBANKACCOUNT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='公司ID')
    COMP_NAME = Column(VARCHAR(100), comment='公司名称')
    NAME_BANK_ACCOUNT = Column(VARCHAR(100), comment='开户银行名称')
    ACCOUNT_NAME = Column(VARCHAR(100), comment='账户名称')
    BANK_ACCOUNT = Column(VARCHAR(50), comment='银行账号')
    BANK_NUMBER = Column(VARCHAR(30), comment='开户行编号')
    EXCHANGE_NUMBER = Column(VARCHAR(30), comment='交换行号')
    LINE_NUMBER = Column(VARCHAR(30), comment='联行行号')
    LINE_PAYMENT_SYSTEM = Column(VARCHAR(30), comment='人行支付系统行号')
    UPDATE1 = Column(VARCHAR(8), comment='更新日期')
    IS_EFFECTIVE = Column(Numeric(1, 0), comment='是否有效')


class CFUNDCHANGEWINDCODE(Base):
    """None"""
    __tablename__ = 'CFUNDCHANGEWINDCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后代码')
    CHANGE_DATE = Column(VARCHAR(10), comment='代码变更日期')


class CFUNDCODEANDSNAME(Base):
    """None"""
    __tablename__ = 'CFUNDCODEANDSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='品种ID')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务代码类型')
    S_CODE = Column(VARCHAR(40), comment='业务代码')
    S_SNAME = Column(VARCHAR(100), comment='业务简称')
    IS_COMMON = Column(Numeric(1, 0), comment='是否通用代码')
    MEMO = Column(VARCHAR(800), comment='业务说明')


class CFUNDCOMPANYPREVIOUSNAME(Base):
    """中国共同基金公司曾用名"""
    __tablename__ = 'CFUNDCOMPANYPREVIOUSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')
    COMP_NAME_ENG = Column(VARCHAR(200), comment='公司英文名称')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    CHANGE_REASON = Column(VARCHAR(100), comment='更名原因')


class CFUNDEVENTDATEINFORMATION(Base):
    """中国共同基金事件日期信息"""
    __tablename__ = 'CFUNDEVENTDATEINFORMATION'
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


class CFUNDFACTIONALSTYLE(Base):
    """中国共同基金公司派系风格"""
    __tablename__ = 'CFUNDFACTIONALSTYLE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='公司ID')
    SEC_IND_CODE = Column(VARCHAR(20), comment='所属板块代码')
    ENTRY_DT = Column(VARCHAR(8), comment='纳入日期')
    REMOVE_DT = Column(VARCHAR(8), comment='剔除日期')
    MEMO = Column(VARCHAR(500), comment='[内部]备注')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CFUNDHOLDERSMEETING(Base):
    """中国共同基金持有人大会通知"""
    __tablename__ = 'CFUNDHOLDERSMEETING'
    OBJECT_ID = Column(VARCHAR(200), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    MEETING_NAME = Column(VARCHAR(40), comment='会议名称')
    IS_NEW = Column(Numeric(5, 0), comment='最新标志')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    MEETING_DT = Column(VARCHAR(8), comment='会议日期')
    MEETING_TYPE = Column(VARCHAR(20), comment='会议类型')
    MEETING_CONTENT = Column(VARCHAR, comment='会议内容')
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


class CFUNDHOLDRESTRICTEDCIRCULATION(Base):
    """中国共同基金持有流通受限证券明细"""
    __tablename__ = 'CFUNDHOLDRESTRICTEDCIRCULATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    F_INFO_RESTRICTEDCODE = Column(VARCHAR(20), comment='流通受限证券代码')
    PLACING_METHOD = Column(VARCHAR(40), comment='配售方式')
    PLACING_DATE = Column(VARCHAR(8), comment='配售日期')
    CIRCULATION_DATE = Column(VARCHAR(8), comment='可流通日期')
    INVESTMENT_AMOUNT = Column(Numeric(20, 4), comment='投资金额(成本)(元)')
    YEAR_END_VALUATION = Column(Numeric(20, 4), comment='年末估值/市价(账面价值)(元)')
    PLACING_QUANTITY = Column(Numeric(20, 4), comment='配售(持有)数量(股/张)')
    COST_TO_NET_WORTH = Column(Numeric(20, 4), comment='成本占净值比例(%)')
    BOOK_VALUE_NET_WORTH = Column(Numeric(20, 4), comment='账面价值占净值比例(%)')
    RESTRICTED_TYPE = Column(VARCHAR(50), comment='流通受限类型')


class CFUNDILLEGALITY(Base):
    """中国共同基金违规事件"""
    __tablename__ = 'CFUNDILLEGALITY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    ILLEG_TYPE = Column(VARCHAR(100), comment='违规类型')
    SUBJECT_TYPE = Column(Numeric(9, 0), comment='主体类别代码')
    SUBJECT = Column(VARCHAR(100), comment='违规主体')
    RELATION_TYPE = Column(Numeric(9, 0), comment='与上市公司的关系')
    BEHAVIOR = Column(TEXT(2147483647), comment='违规行为')
    DISPOSAL_DT = Column(VARCHAR(8), comment='处罚日期')
    DISPOSAL_TYPE = Column(VARCHAR(100), comment='处分类型')
    METHOD1 = Column(VARCHAR(2000), comment='处分措施')
    PROCESSOR = Column(VARCHAR(200), comment='处理人')
    AMOUNT = Column(Numeric(20, 4), comment='处罚金额(元)')
    BAN_YEAR = Column(Numeric(20, 4), comment='市场禁入期限(年)')
    REF_RULE = Column(VARCHAR(1000), comment='相关法规')
    ILLEG_TYPE_CODE = Column(VARCHAR(1000), comment='违规类型代码')


class CFUNDINDEXMEMBERS(Base):
    """中国基金指数成份"""
    __tablename__ = 'CFUNDINDEXMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_INDATE = Column(VARCHAR(8), comment='纳入日期')
    S_CON_OUTDATE = Column(VARCHAR(8), comment='剔除日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CFUNDINDEXTABLE(Base):
    """中国共同基金跟踪基准指数偏离度阀值"""
    __tablename__ = 'CFUNDINDEXTABLE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_CON_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    F_TRACKDEV = Column(Numeric(20, 4), comment='日均跟踪偏离度阀值')
    F_TRACKINGERROR = Column(Numeric(20, 4), comment='年化跟踪误差阀值')


class CFUNDINDUSTRIESCODE(Base):
    """None"""
    __tablename__ = 'CFUNDINDUSTRIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='板块代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='板块名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')
    USED = Column(Numeric(1, 0), comment='是否使用')
    INDUSTRIESALIAS = Column(VARCHAR(12), comment='板块别名')
    SEQUENCE1 = Column(Numeric(4, 0), comment='展示序号')
    MEMO = Column(VARCHAR(100), comment='[内部]备注')
    CHINESEDEFINITION = Column(VARCHAR(600), comment='板块中文定义')


class CFUNDINTRODUCTION(Base):
    """中国基金公司简介"""
    __tablename__ = 'CFUNDINTRODUCTION'
    __table_args__ = (
        Index('INDEX_COMP_SNAME', 'COMP_SNAME'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(40), comment='公司ID')
    COMP_NAME = Column(VARCHAR(100), comment='公司名称')
    COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')
    COMP_NAME_ENG = Column(VARCHAR(100), comment='英文名称')
    COMP_SNAMEENG = Column(VARCHAR(100), comment='英文名称缩写')
    PROVINCE = Column(VARCHAR(20), comment='省份')
    CITY = Column(VARCHAR(50), comment='城市')
    ADDRESS = Column(VARCHAR(200), comment='注册地址')
    OFFICE = Column(VARCHAR(200), comment='办公地址')
    ZIPCODE = Column(VARCHAR(10), comment='邮编')
    PHONE = Column(VARCHAR(50), comment='电话')
    FAX = Column(VARCHAR(50), comment='传真')
    EMAIL = Column(VARCHAR(80), comment='电子邮件')
    WEBSITE = Column(VARCHAR(80), comment='公司网址')
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
    BUSINESSSCOPE = Column(VARCHAR(2000), comment='经营范围')
    COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    SOCIAL_CREDIT_CODE = Column(VARCHAR(30), comment='统一社会信用编码')
    S_INFO_ORG_CODE = Column(VARCHAR(30), comment='组织机构代码')


class CFUNDINTRODUCTIONZL(Base):
    """中国基金公司简介(增量)"""
    __tablename__ = 'CFUNDINTRODUCTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(40), comment='公司ID')
    COMP_NAME = Column(VARCHAR(100), comment='公司名称')
    COMP_SNAME = Column(VARCHAR(40), comment='公司中文简称')
    COMP_NAME_ENG = Column(VARCHAR(100), comment='英文名称')
    COMP_SNAMEENG = Column(VARCHAR(100), comment='英文名称缩写')
    PROVINCE = Column(VARCHAR(20), comment='省份')
    CITY = Column(VARCHAR(50), comment='城市')
    ADDRESS = Column(VARCHAR(200), comment='注册地址')
    OFFICE = Column(VARCHAR(200), comment='办公地址')
    ZIPCODE = Column(VARCHAR(10), comment='邮编')
    PHONE = Column(VARCHAR(50), comment='电话')
    FAX = Column(VARCHAR(50), comment='传真')
    EMAIL = Column(VARCHAR(80), comment='电子邮件')
    WEBSITE = Column(VARCHAR(80), comment='公司网址')
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
    BUSINESSSCOPE = Column(VARCHAR(2000), comment='经营范围')
    COMPANY_TYPE = Column(VARCHAR(10), comment='公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    SOCIAL_CREDIT_CODE = Column(VARCHAR(30), comment='统一社会信用编码')
    S_INFO_ORG_CODE = Column(VARCHAR(30), comment='组织机构代码')


class CFUNDMANAGEMENT(Base):
    """中国基金公司管理层成员"""
    __tablename__ = 'CFUNDMANAGEMENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司id')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    S_INFO_MANAGER_NAME = Column(VARCHAR(80), comment='姓名')
    S_INFO_MANAGER_GENDER = Column(VARCHAR(10), comment='性别代码')
    S_INFO_MANAGER_EDUCATION = Column(VARCHAR(10), comment='学历')
    S_INFO_MANAGER_NATIONALITY = Column(VARCHAR(40), comment='国籍')
    S_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(8), comment='出生日期')
    S_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    S_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8), comment='离职日期')
    S_INFO_MANAGER_TYPE = Column(VARCHAR(20), comment='管理层类别')
    S_INFO_MANAGER_POST = Column(VARCHAR(40), comment='公布职务名称')
    S_INFO_MANAGER_INTRODUCTION = Column(VARCHAR(2000), comment='个人简历')


class CFUNDPCHREDM(Base):
    """中国共同基金申购赎回天数"""
    __tablename__ = 'CFUNDPCHREDM'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_ISSUEDATE = Column(VARCHAR(8), comment='发行公告日')
    F_INFO_SETUPDATE = Column(VARCHAR(8), comment='成立公告日')
    F_INFO_INVSHARE = Column(Numeric(20, 4), comment='合同生效时管理人员工持有份额')
    F_INFO_INVTOTRTO = Column(Numeric(24, 6), comment='合同生效时管理人员工持有比例(%)')
    F_INFO_ISSUETYPE = Column(Numeric(9, 0), comment='发行方式代码')
    F_INFO_ISSUE_OBJECT = Column(Numeric(9, 0), comment='发行对象代码')
    F_INFO_SUB_MODE = Column(Numeric(9, 0), comment='投资者认购方式代码')
    F_INFO_APPROVED_DATE = Column(VARCHAR(8), comment='获批日期')
    F_INFO_TRADE = Column(Numeric(1, 0), comment='是否交易')
    F_INFO_FUNDMANAGEMENTCOMP = Column(Numeric(1, 0), comment='是否基金主体')
    F_INFO_SUSREDMDAY1 = Column(Numeric(20, 4), comment='赎回交收天数')
    F_INFO_SUSPCHDAY = Column(Numeric(20, 4), comment='申购确认天数')
    F_INFO_SUSREDMDAY2 = Column(Numeric(20, 4), comment='赎回确认天数')
    F_INFO_SUSREDMDAY3 = Column(Numeric(20, 4), comment='实际赎回交收天数')
    F_INFO_SUSPCHDAY1 = Column(Numeric(20, 4), comment='申购确认查询天数')
    F_INFO_SUSREDMDAY4 = Column(Numeric(20, 4), comment='赎回确认查询天数')
    F_INFO_TYPECODE = Column(Numeric(9, 0), comment='产品异常状态代码')


class CFUNDPCHREDMCMF(Base):
    """基金公司申购赎回基金情况"""
    __tablename__ = 'CFUNDPCHREDMCMF'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CFUNDNAME = Column(VARCHAR(80), comment='基金管理公司')
    TYPE = Column(VARCHAR(20), comment='类型(申购/赎回)')
    ANN_DT = Column(VARCHAR(8), comment='申购(赎回)公告日期')
    TRADE_DT = Column(VARCHAR(8), comment='申购(赎回)日期')
    PCH_AMOUNT = Column(Numeric(20, 4), comment='申购金额(万元)')
    PCH_EXP = Column(Numeric(20, 4), comment='申购费用(万元)')
    PCH_FEERATIO = Column(Numeric(20, 4), comment='申购费率(%)')
    REDM_SHARE = Column(Numeric(20, 4), comment='赎回份额(份)')
    REDM_FEERATIO = Column(Numeric(20, 4), comment='赎回费率(%)')
    PCHREDMTYPECODE = Column(Numeric(9, 0), comment='申购赎回类型代码')


class CFUNDPORTFOLIOCHANGES(Base):
    """中国共同基金投资组合重大变动(报告期)"""
    __tablename__ = 'CFUNDPORTFOLIOCHANGES'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='基金代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='股票代码')
    CHANGE_TYPE = Column(VARCHAR(10), comment='变动类型')
    ACCUMULATED_AMOUNT = Column(Numeric(20, 4), comment='累计金额')
    BEGIN_NET_ASSET_RATIO = Column(Numeric(20, 4), comment='占期初基金资产净值比例')


class CFUNDPREVIOUSNAME(Base):
    """中国共同基金曾用名"""
    __tablename__ = 'CFUNDPREVIOUSNAME'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截至日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_NAME = Column(VARCHAR(40), comment='证券简称')
    CHANGEREASON = Column(Numeric(9, 0), comment='变动原因代码')


class CFUNDRALATEDSECURITIESCODE(Base):
    """None"""
    __tablename__ = 'CFUNDRALATEDSECURITIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_RALATEDCODE = Column(VARCHAR(40), comment='关联证券Wind代码')
    S_RELATION_TYPCODE = Column(Numeric(9, 0), comment='关系类型代码')
    S_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    S_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期')


class CFUNDRATESENSITIVE(Base):
    """中国共同基金利率敏感分析"""
    __tablename__ = 'CFUNDRATESENSITIVE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    PRICE_FLUNCUATION = Column(Numeric(20, 4), comment='价格变动')
    CHANGE_AMOUNT = Column(Numeric(20, 4), comment='基金资产净值相对变动额')
    TYPE_CODE = Column(Numeric(9, 0), comment='敏感分析价格类型代码')


class CFUNDSTYLECOEFFICIENT(Base):
    """中国共同基金风格系数"""
    __tablename__ = 'CFUNDSTYLECOEFFICIENT'
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


class CFUNDSTYLETHRESHOLD(Base):
    """中国共同基金股票风格分类门限值"""
    __tablename__ = 'CFUNDSTYLETHRESHOLD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_CHANGE_DATE = Column(VARCHAR(8), comment='变动日期')
    THRESHOLD_LARGE_STOCK = Column(Numeric(20, 4), comment='大盘股门限值(万元)')
    THRESHOLD_MID_STOCK = Column(Numeric(20, 4), comment='中盘股门限值(万元)')
    THRESHOLD_GROWTH_STOCK = Column(Numeric(20, 4), comment='成长型门限值')
    THRESHOLD_VALUE_STOCK = Column(Numeric(20, 4), comment='价值型门限值')
    DATE_CLOSING_DATE = Column(VARCHAR(8), comment='引用数据的截止日期')


class CFUNDTACODE(Base):
    """中国基金公司TA代码"""
    __tablename__ = 'CFUNDTACODE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    COMP_ID = Column(VARCHAR(10), comment='品种ID')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务代码类型')
    S_CODE = Column(VARCHAR(40), comment='业务代码')
    S_SNAME = Column(VARCHAR(100), comment='业务简称')
    IS_COMMON = Column(Numeric(1, 0), comment='是否通用代码')
    MEMO = Column(VARCHAR(800), comment='业务说明')
    COMP_TYPE_CODE = Column(Numeric(9, 0), comment='主体类别代码')


class CFUNDTYPECODE(Base):
    """None"""
    __tablename__ = 'CFUNDTYPECODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_TYPNAME = Column(VARCHAR(300), comment='类型名称')
    S_TYPCODE = Column(VARCHAR(40), comment='类型代码')
    S_ORIGIN_TYPCODE = Column(Numeric(9, 0), comment='类型代码')
    S_CLASSIFICATION = Column(VARCHAR(100), comment='分类')


class CFUNDWINDCUSTOMCODE(Base):
    """None"""
    __tablename__ = 'CFUNDWINDCUSTOMCODE'
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


class CFUNDWINDINDEXCOMPONENT(Base):
    """中国共同基金WIND指数对应成份板块"""
    __tablename__ = 'CFUNDWINDINDEXCOMPONENT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_CON_CODE = Column(VARCHAR(16), comment='成份板块代码')
    S_CON_NAME = Column(VARCHAR(100), comment='成份板块名称')


class CFUNDWINDINDEXMEMBERS(Base):
    """中国共同基金WIND指数最新成份明细"""
    __tablename__ = 'CFUNDWINDINDEXMEMBERS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_CON_CODE = Column(VARCHAR(16), comment='板块代码')
    S_CON_NAME = Column(VARCHAR(100), comment='板块名称')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='成份万得代码')


class CHINACLOSEDFUNDEODPRICE(Base):
    """中国上市基金日行情"""
    __tablename__ = 'CHINACLOSEDFUNDEODPRICE'
    __table_args__ = (
        Index('IDX_CHINACLOSEDFUNDEODPRICE_TRADE_DT', 'TRADE_DT'),)
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
    TRADES_COUNT = Column(Numeric(20, 4), comment='成交笔数')
    DISCOUNT_RATE = Column(Numeric(20, 6), comment='贴水率（%）')


class CHINAETFPCHREDMLIST(Base):
    """中国ETF申购赎回清单"""
    __tablename__ = 'CHINAETFPCHREDMLIST'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    F_INFO_CASHDIF = Column(Numeric(20, 4), comment='现金差额(元)')
    F_INFO_MINPRASET = Column(Numeric(20, 4), comment='最小申购赎回单位资产净值(元)')
    F_INFO_ESTICASH = Column(Numeric(20, 4), comment='预估现金部分(元)')
    F_INFO_CASHSUBUPLIMIT = Column(Numeric(20, 4), comment='现金替代比例上限(%)')
    F_INFO_MINPRUNITS = Column(Numeric(20, 4), comment='最小申购赎回单位(份)')
    F_INFO_PRPERMIT = Column(Numeric(1, 0), comment='申购赎回允许情况')
    F_INFO_CONNUM = Column(Numeric(20, 4), comment='标的指数成分股数量')
    F_INFO_PURCHASE_CAP = Column(Numeric(20, 4), comment='申购上限')
    F_INFO_REDEMPTION_CAP = Column(Numeric(20, 4), comment='赎回上限')
    PRICE_DATE = Column(VARCHAR(8), comment='净值截至日期')
    F_PRT_NETASSET = Column(Numeric(20, 4), comment='基金份额净值')
    F_IS_IOPV = Column(Numeric(5, 0), comment='是否需要公布IOPV')


class CHINAETFPCHREDMMEMBERS(Base):
    """中国ETF申购赎回成份"""
    __tablename__ = 'CHINAETFPCHREDMMEMBERS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_CON_WINDCODE = Column(VARCHAR(40), comment='成份股Wind代码')
    S_CON_STOCKNUMBER = Column(Numeric(20, 4), comment='股票数量')
    F_INFO_CASHSUBSIGN = Column(Numeric(1, 0), comment='现金替代标志')
    F_INFO_CASUBPREMRA = Column(Numeric(20, 4), comment='现金替代溢价比例(%)')
    F_INFO_CASUBAMOUNT = Column(Numeric(20, 4), comment='固定替代金额(元)')


class CHINAFEEDERFUND(Base):
    """中国联接基金基本资料"""
    __tablename__ = 'CHINAFEEDERFUND'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='被联接基金指数Wind代码')
    F_INFO_FEEDER_WINDCODE = Column(VARCHAR(40), comment='联接基金Wind代码')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='被联接基金Wind代码')


class CHINAFEEDERFUNDZL(Base):
    """中国联接基金(增量)"""
    __tablename__ = 'CHINAFEEDERFUNDZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='被联接基金指数Wind代码')
    F_INFO_FEEDER_WINDCODE = Column(VARCHAR(40), comment='联接基金Wind代码')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='被联接基金Wind代码')


class CHINAFUNDMAJOREVENT(Base):
    """中国共同基金重大事件"""
    __tablename__ = 'CHINAFUNDMAJOREVENT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_EVENT_CATEGORYCODE = Column(Numeric(9, 0), comment='事件类型代码')
    S_EVENT_ANNCEDATE = Column(VARCHAR(8), comment='披露日期')
    S_EVENT_HAPDATE = Column(VARCHAR(8), comment='发生日期')
    S_EVENT_EXPDATE = Column(VARCHAR(8), comment='失效日期')
    S_EVENT_CONTENT = Column(TEXT(2147483647), comment='事件说明')
    S_EVENT_TEMPLATEID = Column(Numeric(12, 0), comment='模板ID')


class CHINAGRADINGFUND(Base):
    """中国分级基金基本资料"""
    __tablename__ = 'CHINAGRADINGFUND'
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


class CHINAGRADINGFUNDZL(Base):
    """中国分级基金(增量)"""
    __tablename__ = 'CHINAGRADINGFUNDZL'
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


class CHINAHEDGEFUNDDESCRIPTION(Base):
    """中国私募基金基本资料"""
    __tablename__ = 'CHINAHEDGEFUNDDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
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
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
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
    F_INFO_BENCHMARK = Column(VARCHAR(8), comment='业绩比较基准')
    F_INFO_STATUS = Column(Numeric(9, 0), comment='存续状态')
    F_INFO_RESTRICTEDORNOT = Column(VARCHAR(20), comment='限定类型')
    F_INFO_STRUCTUREDORNOT = Column(Numeric(1, 0), comment='是否结构化产品')
    F_INFO_INVESTSCOPE = Column(VARCHAR(2000), comment='投资范围')
    SUMMARY = Column(TEXT(2147483647), comment='计划摘要')
    LOCKPERIOD = Column(VARCHAR(1000), comment='封闭期说明')
    UNLOCKPERIOD = Column(VARCHAR(200), comment='开放日说明')
    EST_ISSUE_SIZE = Column(Numeric(20, 4), comment='预计最大发行规模')
    ISSUE_SIZE = Column(Numeric(20, 4), comment='实际发行规模')
    MIN_AMOUNT = Column(VARCHAR(40), comment='最低追加金额说明')
    FLOAT_INCOME = Column(VARCHAR(500), comment='浮动收益说明')
    FUNDMANAGEMENTCOMPID = Column(VARCHAR(100), comment='管理人公司ID')
    ADVISOR = Column(VARCHAR(200), comment='投资顾问')
    F_PRODUCT_TYPE = Column(Numeric(9, 0), comment='产品渠道分类')
    F_REGIST_NUMBER = Column(VARCHAR(100), comment='私募产品登记备案号')


class CHINAHEDGEFUNDFEE(Base):
    """中国私募基金费率"""
    __tablename__ = 'CHINAHEDGEFUNDFEE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券id')
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
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')
    SUPPLEMENTARY = Column(VARCHAR(800), comment='费率补充说明')


class CHINAHEDGEFUNDMANAGER(Base):
    """中国私募基金基金经理"""
    __tablename__ = 'CHINAHEDGEFUNDMANAGER'
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
    F_INFO_MANAGER_TYPE = Column(Numeric(9, 0), comment='所属派系')
    F_INFO_MANAGER_ID = Column(VARCHAR(10), comment='基金经理ID')
    F_INFO_MANAGER_BRIEFING = Column(TEXT(2147483647), comment='简历')


class CHINAHEDGEFUNDMANAGERQL(Base):
    """None"""
    __tablename__ = 'CHINAHEDGEFUNDMANAGERQL'
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
    F_INFO_MANAGER_TYPE = Column(Numeric(9, 0))
    F_INFO_MANAGER_ID = Column(VARCHAR(10))
    F_INFO_MANAGER_BRIEFING = Column(TEXT(2147483647))


class CHINAHEDGEFUNDMANAGERZL(Base):
    """中国私募基金基金经理(增量)"""
    __tablename__ = 'CHINAHEDGEFUNDMANAGERZL'
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
    F_INFO_MANAGER_TYPE = Column(Numeric(9, 0), comment='所属派系')
    F_INFO_MANAGER_ID = Column(VARCHAR(10), comment='基金经理ID')
    F_INFO_MANAGER_BRIEFING = Column(VARCHAR(2500), comment='简历')


class CHINAHEDGEFUNDNAV(Base):
    """中国私募基金净值"""
    __tablename__ = 'CHINAHEDGEFUNDNAV'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    PRICE_DATE = Column(VARCHAR(8), comment='截止日期')
    F_NAV_UNIT = Column(Numeric(24, 8), comment='单位净值')
    F_NAV_ACCUMULATED = Column(Numeric(24, 8), comment='累计净值')
    F_NAV_DIVACCUMULATED = Column(Numeric(20, 4), comment='累计分红')
    F_NAV_ADJFACTOR = Column(Numeric(20, 6), comment='复权因子')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')


class CHINAHEDGEFUNDPERFORMANCE(Base):
    """中国私募基金业绩表现"""
    __tablename__ = 'CHINAHEDGEFUNDPERFORMANCE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
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
    F_SFRETURN_RECENTQUARTER = Column(Numeric(20, 6), comment='最近3月同类收益率')
    F_SFRANK_RECENTQUARTER = Column(Numeric(20, 0), comment='最近三月同类排名')
    F_SFRETURN_RECENTHALFYEAR = Column(Numeric(20, 6), comment='最近6月同类收益率')
    F_SFRANK_RECENTHALFYEAR = Column(Numeric(20, 0), comment='最近六月同类排名')
    F_SFRETURN_RECENTYEAR = Column(Numeric(20, 6), comment='最近1年同类收益率')
    F_SFRANK_RECENTYEAR = Column(Numeric(20, 0), comment='最近一年同类排名')
    F_SFRETURN_RECENTTWOYEAR = Column(Numeric(20, 6), comment='最近2年同类收益率')
    F_SFRANK_RECENTTWOYEAR = Column(Numeric(20, 0), comment='最近两年同类排名')
    F_SFRETURN_RECENTTHREEYEAR = Column(Numeric(20, 6), comment='最近3年同类收益率')
    F_SFRANK_RECENTTHREEYEAR = Column(Numeric(20, 0), comment='最近三年同类排名')
    F_SFRETURN_RECENTFIVEYEAR = Column(Numeric(20, 6), comment='最近5年同类收益率')
    F_SFRANK_RECENTFIVEYEAR = Column(Numeric(20, 0), comment='最近五年同类排名')
    F_SFRETURN_SINCEFOUND = Column(Numeric(20, 6), comment='成立以来同类收益率')
    F_SFRANK_SINCEFOUND = Column(Numeric(20, 0), comment='成立以来同类排名')
    F_SFANNUALYEILD = Column(Numeric(20, 6), comment='成立以来年化同类收益率')
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
    F_FUNDTYPE = Column(VARCHAR(50), comment='所属基金类型名称')
    F_AVGRETURN_DAY = Column(Numeric(20, 6), comment='当日收益率')
    F_SFRANK_THISYEART = Column(VARCHAR(50), comment='本年以来同类排名')
    F_SFRANK_RECENTQUARTERT = Column(VARCHAR(50), comment='最近3月同类排名')
    F_SFRANK_RECENTHALFYEART = Column(VARCHAR(50), comment='最近6月同类排名')
    F_SFRANK_RECENTYEART = Column(VARCHAR(50), comment='最近1年同类排名')
    F_SFRANK_RECENTTWOYEART = Column(VARCHAR(50), comment='最近2年同类排名')
    F_SFRANK_RECENTTHREEYEART = Column(VARCHAR(50), comment='最近3年同类排名')
    F_SFRANK_RECENTFIVEYEART = Column(VARCHAR(50), comment='最近5年同类排名')
    F_SFRANK_SINCEFOUNDT = Column(VARCHAR(50), comment='成立以来同类排名')
    F_SFRANK_ANNUALYEILDT = Column(VARCHAR(50), comment='成立以来年化同类排名')
    F_SFRANK_RECENTWEEKT = Column(VARCHAR(50), comment='最近1周同类排名')
    F_SFRANK_RECENTMONTHT = Column(VARCHAR(50), comment='最近1月同类排名')


class CHINAHEDGEFUNDSECTOR(Base):
    """中国私募基金Wind板块"""
    __tablename__ = 'CHINAHEDGEFUNDSECTOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SECTOR = Column(VARCHAR(40), comment='所属板块')
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_SECTOREXITDT = Column(VARCHAR(8), comment='截止日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class CHINAMFDIVIDEND(Base):
    """中国共同基金分红"""
    __tablename__ = 'CHINAMFDIVIDEND'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_E_BCH_DT = Column(VARCHAR(8), comment='可分配收益基准日')
    F_DIV_PROGRESS = Column(VARCHAR(10), comment='方案进度')
    CASH_DVD_PER_SH_TAX = Column(Numeric(20, 6), comment='每股派息(元)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    EQY_RECORD_DT = Column(VARCHAR(8), comment='权益登记日')
    EX_DT = Column(VARCHAR(8), comment='除息日')
    F_DIV_EDEXDATE = Column(VARCHAR(8), comment='除息日(场外)')
    PAY_DT = Column(VARCHAR(8), comment='派息日')
    F_DIV_PAYDATE = Column(VARCHAR(8), comment='派息日(场外)')
    F_DIV_IMPDATE = Column(VARCHAR(8), comment='分红实施公告日')
    F_SH_BCH_Y = Column(VARCHAR(8), comment='份额基准年度')
    F_BCH_UNIT = Column(Numeric(20, 4), comment='基准基金份额(万份)')
    F_E_APR = Column(Numeric(20, 4), comment='可分配收益(元)')
    F_EX_DIV_DT = Column(VARCHAR(8), comment='净值除权日')
    F_E_APR_AMOUNT = Column(Numeric(20, 4), comment='收益分配金额(元)')
    F_REINV_BCH_DT = Column(VARCHAR(8), comment='红利再投资份额净值基准日')
    F_REINV_TOAC_DT = Column(VARCHAR(8), comment='红利再投资到账日')
    F_REINV_REDEEM_DT = Column(VARCHAR(8), comment='红利再投资可赎回起始日')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_DIV_OBJECT = Column(VARCHAR(100), comment='分配对象')
    F_DIV_IPAYDT = Column(VARCHAR(8), comment='收益支付日')


class CHINAMFMPERFORMANCE(Base):
    """中国共同基金基金经理业绩表现"""
    __tablename__ = 'CHINAMFMPERFORMANCE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    FUNDMANAGER_ID = Column(VARCHAR(10), comment='基金经理ID')
    TRADE_DATE = Column(VARCHAR(8), comment='日期')
    FMINDEX_TYPE = Column(Numeric(9, 0), comment='基金经理指数类型')
    FMINDEX_POINT = Column(Numeric(20, 8), comment='基金经理指数点位')
    TOTRETURN_YTD = Column(Numeric(20, 8), comment='今年以来回报')
    RANKING_YTD = Column(VARCHAR(20), comment='今年以来同类排名')
    TOTRETURN_1W = Column(Numeric(20, 8), comment='最近1周回报')
    RANKING_1W = Column(VARCHAR(20), comment='最近1周同类排名')
    TOTRETURN_1M = Column(Numeric(20, 8), comment='最近1月回报')
    RANKING_1M = Column(VARCHAR(20), comment='最近1月同类排名')
    TOTRETURN_3M = Column(Numeric(20, 8), comment='最近3月回报')
    RANKING_3M = Column(VARCHAR(20), comment='最近3月同类排名')
    TOTRETURN_6M = Column(Numeric(20, 8), comment='最近6月回报')
    RANKING_6M = Column(VARCHAR(20), comment='最近6月同类排名')
    TOTRETURN_1Y = Column(Numeric(20, 8), comment='最近1年回报')
    RANKING_1Y = Column(VARCHAR(20), comment='最近1年同类排名')
    TOTRETURN_2Y = Column(Numeric(20, 8), comment='最近2年回报')
    RANKING_2Y = Column(VARCHAR(20), comment='最近2年同类排名')
    TOTRETURN_3Y = Column(Numeric(20, 8), comment='最近3年回报')
    RANKING_3Y = Column(VARCHAR(20), comment='最近3年同类排名')
    TOTRETURN_5Y = Column(Numeric(20, 8), comment='最近5年回报')
    RANKING_5Y = Column(VARCHAR(20), comment='最近5年同类排名')
    TOTRETURN_10Y = Column(Numeric(20, 8), comment='最近10年回报')
    RANKING_10Y = Column(VARCHAR(20), comment='最近10年同类排名')
    TOTRETURN_ES = Column(Numeric(20, 8), comment='履任以来回报')
    ANNRETURNES = Column(Numeric(20, 8), comment='履任以来年化回报')
    RANKING_ES = Column(VARCHAR(20), comment='履任以来同类排名')
    WORSTTOTRETURN_6M = Column(Numeric(20, 8), comment='最差连续六月回报')
    BESTTOTRETURN_6M = Column(Numeric(20, 8), comment='最高连续六月回报')
    SUCBASERETURN_YTD = Column(Numeric(20, 8), comment='今年以来超越基准回报')
    SUCBASERETURN_1W = Column(Numeric(20, 8), comment='最近1周超越基准回报')
    SUCBASERETURN_1M = Column(Numeric(20, 8), comment='最近1月超越基准回报')
    SUCBASERETURN_3M = Column(Numeric(20, 8), comment='最近3月超越基准回报')
    SUCBASERETURN_6M = Column(Numeric(20, 8), comment='最近6月超越基准回报')
    SUCBASERETURN_1Y = Column(Numeric(20, 8), comment='最近1年超越基准回报')
    SUCBASERETURN_2Y = Column(Numeric(20, 8), comment='最近2年超越基准回报')
    SUCBASERETURN_3Y = Column(Numeric(20, 8), comment='最近3年超越基准回报')
    SUCBASERETURN_5Y = Column(Numeric(20, 8), comment='最近5年超越基准回报')
    SUCBASERETURN_10Y = Column(Numeric(20, 8), comment='最近10年超越基准回报')
    SUCBASERETURN_ES = Column(Numeric(20, 8), comment='履任以来超越基准回报')


class CHINAMFPERFORMANCE(Base):
    """中国共同基金业绩表现"""
    __tablename__ = 'CHINAMFPERFORMANCE'
    __table_args__ = (
        Index('S_INFO_WINDCODE_INDEX', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
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
    F_SFRANK_SINCEFOUND = Column(Numeric(20, 0), comment='成立以来同类排名(不建议使用)')
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
    F_FUNDTYPE = Column(VARCHAR(50), comment='基金分类')
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
    F_BETA_6M = Column(Numeric(20, 8), comment='BETA(6月)')
    F_BETA_1Y = Column(Numeric(20, 8), comment='BETA(1年)')
    F_BETA_2Y = Column(Numeric(20, 8), comment='BETA(2年)')
    F_BETA_3Y = Column(Numeric(20, 8), comment='BETA(3年)')
    F_ALPHA_6M = Column(Numeric(20, 8), comment='ALPHA(6月)')
    F_ALPHA_1Y = Column(Numeric(20, 8), comment='ALPHA(1年)')
    F_ALPHA_2Y = Column(Numeric(20, 8), comment='ALPHA(2年)')
    F_ALPHA_3Y = Column(Numeric(20, 8), comment='ALPHA(3年)')
    F_SFRETURN_DAY = Column(Numeric(20, 6), comment='当日同类收益率')
    F_SFRANK_DAY = Column(Numeric(20, 0), comment='当日同类收益率排名 ')
    F_SFRANK_DAYT = Column(VARCHAR(50), comment='当日同类收益率排名')
    F_ANNUALYEILD_SINCEFOUND = Column(Numeric(20, 6), comment='成立以来年化收益率')


class CHINAMFRISKANALYSISINDEX(Base):
    """中国共同基金风险分析指标"""
    __tablename__ = 'CHINAMFRISKANALYSISINDEX'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    RISKANALYSIS_CODE = Column(Numeric(9, 0), comment='指标类型代码')
    RISKANALYSIS_NAME = Column(VARCHAR(100), comment='指标名称')
    RISKANALYSIS_VALUE = Column(Numeric(20, 8), comment='指标数值')


class CHINAMUTFUNDSHARE(Base):
    """None"""
    __tablename__ = 'CHINAMUTFUNDSHARE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    F_INFO_WINDCODE = Column(VARCHAR(40))
    ANN_DT = Column(VARCHAR(8))
    F_UNIT_CHANGEDATE = Column(VARCHAR(8))
    F_UNIT_NONTRADABLE = Column(Numeric(20, 6))
    F_INFO_SHARE = Column(Numeric(20, 6))
    F_UNIT_TOTAL = Column(Numeric(20, 6))
    F_INFO_CHANGEREASON = Column(VARCHAR(10))
    FUNDSHARE_TOTAL = Column(Numeric(20, 6))
    F_UNIT_MERGEDSHARESORNOT = Column(Numeric(5, 0))
    CUR_SIGN = Column(Numeric(5, 0))


class CHINAMUTUALFUNDAGENCY(Base):
    """中国共同基金中介机构"""
    __tablename__ = 'CHINAMUTUALFUNDAGENCY'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_AGENCY_NAME = Column(VARCHAR(200), comment='中介机构名称')
    S_AGENCY_FNAME = Column(VARCHAR(100), comment='中介机构名称(容错后)')
    S_AGENCY_ID = Column(VARCHAR(40), comment='中介机构ID')
    S_RELATION_TYPCODE = Column(VARCHAR(10), comment='关系类型代码')
    BEGINDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='终止日期')


class CHINAMUTUALFUNDASSETPORTFOLIO(Base):
    """中国共同基金投资组合——资产配置"""
    __tablename__ = 'CHINAMUTUALFUNDASSETPORTFOLIO'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE_ENDDATE', 'S_INFO_WINDCODE', 'F_PRT_ENDDATE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_PRT_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    F_PRT_TOTALASSET = Column(Numeric(20, 4), comment='资产总值(元)')
    F_PRT_NETASSET = Column(Numeric(20, 4), comment='资产净值(元)')
    F_PRT_STOCKVALUE = Column(Numeric(20, 4), comment='持有股票市值(元)')
    F_PRT_STOCKTONAV = Column(Numeric(20, 4), comment='持有股票市值占资产净值比例(%)')
    F_PRT_PASVSTKVALUE = Column(Numeric(15, 2), comment='指数投资持有股票市值(元)')
    F_PRT_PASVSTKTONAV = Column(Numeric(20, 4), comment='指数投资持有股票市值占资产净值比例(%)')
    F_PRT_POSVSTKVALUE = Column(Numeric(20, 4), comment='积极投资持有股票市值(元)')
    F_PRT_POSVSTKTONAV = Column(Numeric(20, 4), comment='积极投资持有股票市值占资产净值比例(%)')
    F_PRT_GOVBOND = Column(Numeric(20, 4), comment='持有国债市值(元)')
    F_PRT_GOVBONDTONAV = Column(Numeric(20, 4), comment='持有国债市值占资产净值比例(%)')
    F_PRT_CASH = Column(Numeric(20, 4), comment='持有现金(元)')
    F_PRT_CASHTONAV = Column(Numeric(20, 4), comment='持有现金占资产净值比例(%)')
    F_PRT_GOVCASHVALUE = Column(Numeric(20, 4), comment='持有国债及现金总值(元)')
    F_PRT_GOVCASHTONAV = Column(Numeric(20, 4), comment='持有国债及现金占资产净值比例(%)')
    F_PRT_BDVALUE_NOGOV = Column(Numeric(20, 4), comment='持有债券市值(不含国债)(元)')
    F_PRT_BDTONAV_NOGOV = Column(Numeric(20, 4), comment='持有债券市值(不含国债)占资产净值比例(%)')
    F_PRT_FINANBOND = Column(Numeric(20, 4), comment='持有金融债市值(元)')
    F_PRT_FINANBONDTONAV = Column(Numeric(20, 4), comment='持有金融债市值占资产净值比例(%)')
    F_PRT_COVERTBOND = Column(Numeric(15, 2), comment='持有可转债市值(元)')
    F_PRT_COVERTBONDTONAV = Column(Numeric(20, 4), comment='持有可转债市值占资产净值比例(%)')
    F_PRT_CORPBOND = Column(Numeric(20, 4), comment='持有企债市值(元)')
    F_PRT_CORPBONDTONAV = Column(Numeric(20, 4), comment='持有企债市值占资产净值比例(%)')
    F_PRT_BONDVALUE = Column(Numeric(20, 4), comment='持有债券市值总计(元)')
    F_PRT_BONDTONAV = Column(Numeric(20, 4), comment='持有债券市值总计占资产净值比例(%)')
    F_PRT_CTRBANKBILL = Column(Numeric(20, 4), comment='持有央行票据市值(元)')
    F_PRT_CTRBANKBILLTONAV = Column(Numeric(20, 4), comment='持有央行票据市值占资产净值比例(%)')
    F_PRT_WARRANTVALUE = Column(Numeric(20, 4), comment='持有权证市值(元)')
    F_PRT_WARRANTONAV = Column(Numeric(20, 4), comment='持有权证市值占资产净值比例(%)')
    F_PRT_ABSVALUE = Column(Numeric(20, 4), comment='持有资产支持证券市值(元)')
    F_PRT_ABSVALUETONAV = Column(Numeric(20, 4), comment='持有资产支持证券占资产净值比例(%)')
    F_PRT_POLIFINANBDVALUE = Column(Numeric(20, 4), comment='持有政策性金融债市值(元)')
    F_PRT_POLIFINANBDTONAV = Column(Numeric(20, 4), comment='持有政策性金融债市值占资产净值比例(%)')
    F_PRT_FUNDVALUE = Column(Numeric(20, 4), comment='持有基金市值(元)')
    F_PRT_FUNDTONAV = Column(Numeric(20, 4), comment='持有基金市值占资产净值比例(%)')
    F_PRT_MMVALUE = Column(Numeric(20, 4), comment='持有货币市场工具市值(元)')
    F_PRT_MMTONAV = Column(Numeric(20, 4), comment='持有货币市场工具市值占资产净值比例(%)')
    F_PRT_OTHER = Column(Numeric(20, 4), comment='持有其他资产(元)')
    F_PRT_OTHERTONAV = Column(Numeric(20, 4), comment='持有其他资产占资产净值比例(%)')
    F_PRT_DEBCREBALANCE = Column(Numeric(20, 4), comment='借贷方差额(元)')
    F_MMF_AVGPTM = Column(Numeric(20, 4), comment='投资组合平均剩余期限(天)')
    F_MMF_REVERSEREPO = Column(Numeric(20, 4), comment='买入返售证券(元)')
    F_MMF_REPO = Column(Numeric(20, 4), comment='卖出回购证券(元)')
    F_PRT_STOCKTOTOT = Column(Numeric(20, 4), comment='持有股票市值占资产总值比例(%)')
    F_PRT_BONDTOTOT = Column(Numeric(20, 4), comment='持有债券市值占资产总值比例(%)')
    F_PRT_CASHTOTOT = Column(Numeric(20, 4), comment='持有现金占资产总值比例(%)')
    F_PRT_OTHERTOTOT = Column(Numeric(20, 4), comment='持有其他资产占资产总值比例(%)')
    F_PRT_WARRANTOTOT = Column(Numeric(20, 4), comment='持有权证市值占资产总值比例(%)')
    F_PRT_FUNDTOTOT = Column(Numeric(20, 4), comment='持有基金市值占资产总值比例(%)')
    F_PRT_MMTOTOT = Column(Numeric(20, 4), comment='持有货币市场工具市值占资产总值比例(%)')
    F_PRT_STOCKTONAVCHANGE = Column(Numeric(20, 4), comment='持有股票比例较上期变化(%)')
    F_PRT_BONDTONAVCHANGE = Column(Numeric(20, 4), comment='持有债券比例较上期变化(%)')
    F_PRT_CASHTONAVCHANGE = Column(Numeric(20, 4), comment='持有现金比例较上期变化(%)')
    F_PRT_OTHERTOTOTCHANGE = Column(Numeric(20, 4), comment='持有其他资产比例较上期变化(%)')
    F_PRT_CPVALUE = Column(Numeric(20, 4), comment='持有短期融资券市值(元)')
    F_PRT_MTNVALUE = Column(Numeric(20, 4), comment='持有中期票据市值(元)')
    F_PRT_CDS = Column(Numeric(20, 4), comment='持有同业存单市值(元)')
    F_PRT_HKSTOCKVALUE = Column(Numeric(20, 4), comment='港股通投资港股市值')
    F_PRT_HKSTOCKTONAV = Column(Numeric(20, 4), comment='港股通投资港股市值占资产净值比')
    F_PRT_REVERSEREPOTOTOT = Column(Numeric(20, 4), comment='持有买入返售证券占资产总值比例(%)')
    F_PRT_REVERSEREPOTONAV = Column(Numeric(20, 4), comment='持有买入返售证券占资产净值比例(%)')
    F_ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class CHINAMUTUALFUNDBENCHMARK(Base):
    """中国共同基金业绩比较基准配置"""
    __tablename__ = 'CHINAMUTUALFUNDBENCHMARK'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDEXWINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    S_INFO_BGNDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_ENDDT = Column(VARCHAR(8), comment='截止日期')
    S_INFO_INDEXWEG = Column(Numeric(20, 4), comment='指数权重')
    S_INFO_OPERATORS = Column(VARCHAR(20), comment='运算符')
    S_INFO_CONSTANT = Column(Numeric(20, 4), comment='常数')
    S_INFO_AFTERTAXORNOT = Column(Numeric(1, 0), comment='是否税后')
    CUR_SIGN = Column(Numeric(1, 0), comment='是否最新')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_FXCODE = Column(VARCHAR(40), comment='汇率Wind代码')
    S_INC_SEQUENCE = Column(Numeric(2, 0), comment='序号')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')
    SEC_ID2 = Column(VARCHAR(10), comment='证券ID2')
    IS_COMPOUND = Column(Numeric(1, 0), comment='是否复利')


class CHINAMUTUALFUNDBENCHMARKEOD(Base):
    """中国共同基金业绩比较基准行情"""
    __tablename__ = 'CHINAMUTUALFUNDBENCHMARKEOD'
    __table_args__ = (
        Index('NonClusteredIndex-20201029-104841', 'S_INFO_WINDCODE', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='指数Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    S_DQ_CLOSE = Column(Numeric(20, 8), comment='收盘价')
    S_DQ_PCTCHANGE = Column(Numeric(20, 8), comment='涨跌幅(%)')


class CHINAMUTUALFUNDBONDPORTFOLIO(Base):
    """中国共同基金投资组合——持券明细"""
    __tablename__ = 'CHINAMUTUALFUNDBONDPORTFOLIO'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE_ENDDATE', 'S_INFO_WINDCODE', 'F_PRT_ENDDATE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    F_PRT_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_BONDWINDCODE = Column(VARCHAR(40), comment='持有债券Wind代码')
    F_PRT_BDVALUE = Column(Numeric(20, 4), comment='持有债券市值(元)')
    F_PRT_BDQUANTITY = Column(Numeric(20, 4), comment='持有债券数量（张）')
    F_PRT_BDVALUETONAV = Column(Numeric(20, 4), comment='持有债券市值占基金净值比例(%)')
    F_ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class CHINAMUTUALFUNDDESCRIPTION(Base):
    """中国共同基金基本资料"""
    __tablename__ = 'CHINAMUTUALFUNDDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_FRONT_CODE = Column(VARCHAR(40), comment='前端代码')
    F_INFO_BACKEND_CODE = Column(VARCHAR(40), comment='后端代码')
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
    CRNY_CODE = Column(VARCHAR(10), comment='货币代码')
    F_INFO_PTMYEAR = Column(Numeric(20, 4), comment='存续期')
    F_ISSUE_OEF_STARTDATEINST = Column(VARCHAR(8), comment='机构投资者认购起始日')
    F_ISSUE_OEF_DNDDATEINST = Column(VARCHAR(8), comment='机构投资者认购终止日')
    F_INFO_PARVALUE = Column(Numeric(20, 4), comment='面值')
    F_INFO_TRUSTTYPE = Column(VARCHAR(40), comment='信托类别')
    F_INFO_TRUSTEE = Column(VARCHAR(100), comment='受托人')
    F_PCHREDM_PCHSTARTDATE = Column(VARCHAR(8), comment='日常申购起始日')
    F_INFO_REDMSTARTDATE = Column(VARCHAR(8), comment='日常赎回起始日')
    F_INFO_MINBUYAMOUNT = Column(Numeric(20, 4), comment='起点金额')
    F_INFO_EXPECTEDRATEOFRETURN = Column(Numeric(20, 4), comment='预期收益率')
    F_INFO_ISSUINGPLACE = Column(VARCHAR(100), comment='发行地')
    F_INFO_BENCHMARK = Column(VARCHAR(500), comment='业绩比较基准')
    F_INFO_STATUS = Column(Numeric(9, 0), comment='存续状态')
    F_INFO_RESTRICTEDORNOT = Column(VARCHAR(20), comment='限定类型')
    F_INFO_STRUCTUREDORNOT = Column(Numeric(1, 0), comment='是否结构化产品')
    F_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    F_INFO_FIRSTINVESTSTYLE = Column(VARCHAR(20), comment='投资风格')
    F_INFO_ISSUEDATE = Column(VARCHAR(8), comment='发行日期')
    F_INFO_TYPE = Column(VARCHAR(20), comment='基金类型')
    F_INFO_ISINITIAL = Column(Numeric(5, 0), comment='是否为初始基金')
    F_INFO_PINYIN = Column(VARCHAR(40), comment='简称拼音')
    F_INFO_INVESTSCOPE = Column(VARCHAR(2000), comment='投资范围')
    F_INFO_INVESTOBJECT = Column(VARCHAR(500), comment='投资目标')
    F_INFO_INVESTCONCEPTION = Column(VARCHAR(2000), comment='投资理念')
    F_INFO_DECISION_BASIS = Column(VARCHAR(2000), comment='决策依据')
    IS_INDEXFUND = Column(Numeric(5, 0), comment='是否指数基金')
    F_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    F_INFO_CORP_FUNDMANAGEMENTID = Column(VARCHAR(10), comment='基金管理人ID')
    F_INFO_CUSTODIANBANKID = Column(VARCHAR(40), comment='托管人id')
    MAX_NUM_HOLDER = Column(Numeric(20, 4), comment='单一投资者持有份额上限(亿份)')
    MAX_NUM_COLTARGET = Column(Numeric(20, 4), comment='封闭期目标募集数量上限(亿份)')
    INVESTSTRATEGY = Column(TEXT(2147483647), comment='投资策略')
    RISK_RETURN = Column(TEXT(2147483647), comment='基金风险收益特征')
    F_PCHREDM_PCHMINAMT = Column(Numeric(20, 4), comment='每次最低申购金额(场外)(万元)')
    F_PCHREDM_PCHMINAMT_EX = Column(Numeric(20, 4), comment='每次最低申购金额(场内) (万元)')
    F_INFO_LISTDATE = Column(VARCHAR(8), comment='上市时间')
    F_INFO_ANNDATE = Column(VARCHAR(8), comment='公告日期')
    F_CLOSED_OPERATION_PERIOD = Column(Numeric(20, 4), comment='封闭运作期')
    F_CLOSED_OPERATION_INTERVAL = Column(Numeric(20, 4), comment='封闭运作期满开放日间隔')
    F_INFO_REGISTRANT = Column(VARCHAR(10), comment='基金注册与过户登记人ID')
    F_PERSONAL_STARTDATEIND = Column(VARCHAR(8), comment='个人投资者认购起始日')
    F_PERSONAL_ENDDATEIND = Column(VARCHAR(8), comment='个人投资者认购终止日')
    F_INFO_FUND_ID = Column(VARCHAR(100), comment='基金品种ID')


class CHINAMUTUALFUNDFLOATSHARE(Base):
    """中国共同基金场内流通份额"""
    __tablename__ = 'CHINAMUTUALFUNDFLOATSHARE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    F_UNIT_FLOATSHARE = Column(Numeric(20, 4), comment='场内份额(份)')


class CHINAMUTUALFUNDINDPORTFOLIO(Base):
    """中国共同基金投资组合——行业配置"""
    __tablename__ = 'CHINAMUTUALFUNDINDPORTFOLIO'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_PRT_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    S_INFO_CSRCINDUSCODE = Column(VARCHAR(40), comment='证监会行业编号')
    F_PRT_INDUSVALUE = Column(Numeric(20, 4), comment='持有行业市值(元)')
    F_PRT_INDUSTONAV = Column(Numeric(20, 4), comment='持有行业市值占基金净值比例(%)')
    F_PRT_INDPOSVALUE = Column(Numeric(20, 4), comment='积极投资持有行业市值(元)')
    F_PRT_INDPOSPRO = Column(Numeric(20, 4), comment='积极投资持有行业比例(%)')
    F_PRT_INDPASSIVEVALUE = Column(Numeric(20, 4), comment='指数投资持有行业市值(元)')
    F_PRT_INDPASSIVEPRO = Column(Numeric(20, 4), comment='指数投资持有行业比例(%)')
    F_PRT_INDUSTONAVCHANGE = Column(Numeric(20, 4), comment='持有行业市值比例较上期变化(%)')
    S_INFO_CSRCINDUSNAME = Column(VARCHAR(60), comment='行业名称')


class CHINAMUTUALFUNDISSUE(Base):
    """中国共同基金发行"""
    __tablename__ = 'CHINAMUTUALFUNDISSUE'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_CHINESENAME = Column(VARCHAR(100), comment='基金中文名称')
    F_INFO_ENGLISHNAME = Column(VARCHAR(100), comment='基金英文名称')
    F_INFO_SHORTNAME = Column(VARCHAR(40), comment='基金中文简称')
    F_INFO_MGRCOMP = Column(VARCHAR(100), comment='基金管理人')
    F_INFO_CUSTODIANBANK = Column(VARCHAR(100), comment='基金托管人')
    F_INFO_TYPE = Column(Numeric(9, 0), comment='基金类型')
    F_INFO_INVESTYPE = Column(Numeric(9, 0), comment='基金投资类型')
    F_ISSUE_DATE = Column(VARCHAR(8), comment='发行日期')
    F_ISSUE_COLPERIOD = Column(VARCHAR(10), comment='设立募集期(月)')
    F_ISSUE_MAXCOLSHARE = Column(Numeric(20, 4), comment='设立募集目标(亿份)')
    F_ISSUE_NETPCHSHARE = Column(Numeric(20, 4), comment='净认购份额-成立条件(亿份)')
    F_ISSUE_NETPCHNUM = Column(Numeric(20, 4), comment='认购户数-成立条件')
    F_INFO_PARVALUE = Column(Numeric(20, 4), comment='基金面值')
    F_INFO_PTMYEAR = Column(Numeric(20, 4), comment='存续期(年)')
    F_INFO_MANAFEERATIO = Column(Numeric(20, 4), comment='管理费率(%)')
    F_INFO_CUSTFEERATIO = Column(Numeric(20, 4), comment='托管费率(%)')
    F_INFO_SALEFEERATIO = Column(Numeric(20, 4), comment='销售费率(%)')
    F_INFO_SETUPDATE = Column(VARCHAR(8), comment='基金成立日期')
    F_INFO_MATURITYDATE = Column(VARCHAR(8), comment='基金到期日期')
    F_ISSUE_SHARES = Column(Numeric(20, 4), comment='发行数量(亿份)')
    S_FELLOW_DISTOR = Column(Numeric(20, 4), comment='总有效申购户数')
    F_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    F_PCH_STARTDATE = Column(VARCHAR(8), comment='申购起始日期')
    F_REDM_STARTDATE = Column(VARCHAR(8), comment='赎回起始日期')
    F_ISSUE_STARTDATEIND = Column(VARCHAR(8), comment='投资者认购起始日期')
    F_ISSUE_ENDDATEIND = Column(VARCHAR(8), comment='投资者认购终止日期')
    F_ISSUE_MINAMTIND = Column(Numeric(20, 4), comment='认购下限(万元)')
    F_ISSUE_MAXAMTIND = Column(Numeric(20, 4), comment='认购上限(万元)')
    F_PCHREDM_PCHMINAMT = Column(Numeric(22, 6), comment='每次最低申购金额(万元)')
    F_PCHREDM_REDMMINAMT = Column(Numeric(20, 4), comment='单笔赎回份额下限(份)')
    F_PCHREDM_HUGEREDMPRO = Column(Numeric(20, 4), comment='巨额赎回认定比例(%)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    F_INFO_ISSUEPRICE = Column(Numeric(20, 4), comment='发行价格')
    F_INFO_OVRSUBRATIO = Column(Numeric(20, 4), comment='超额认购倍数')


class CHINAMUTUALFUNDMANAGER(Base):
    """中国共同基金基金经理"""
    __tablename__ = 'CHINAMUTUALFUNDMANAGER'
    __table_args__ = (
        Index('INDEX_F_INFO_WINDCODE', 'F_INFO_WINDCODE'),
        Index('INDEX_F_INFO_FUNDMANAGER_ID', 'F_INFO_FUNDMANAGER_ID'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_INFO_FUNDMANAGER = Column(VARCHAR(40), comment='姓名')
    F_INFO_MANAGER_GENDER = Column(VARCHAR(10), comment='性别')
    F_INFO_MANAGER_BIRTHYEAR = Column(VARCHAR(10), comment='出身年份')
    F_INFO_MANAGER_EDUCATION = Column(VARCHAR(20), comment='学历')
    F_INFO_MANAGER_NATIONALITY = Column(VARCHAR(10), comment='国籍')
    F_INFO_MANAGER_STARTDATE = Column(VARCHAR(8), comment='任职日期')
    F_INFO_MANAGER_LEAVEDATE = Column(VARCHAR(8), comment='离职日期')
    F_INFO_MANAGER_RESUME = Column(TEXT(2147483647), comment='简历')
    F_INFO_FUNDMANAGER_ID = Column(VARCHAR(10), comment='基金经理ID')
    S_INFO_MANAGER_POST = Column(VARCHAR(100), comment='职务')
    F_INFO_ESCROW_FUNDMANAGER = Column(VARCHAR(50), comment='代管基金经理')
    F_INFO_ESCROW_STARTDATE = Column(VARCHAR(8), comment='代管起始日期')
    F_INFO_ESCROW_LEAVEDATE = Column(VARCHAR(8), comment='代管结束日期')


class CHINAMUTUALFUNDNAV(Base):
    """中国共同基金净值"""
    __tablename__ = 'CHINAMUTUALFUNDNAV'
    __table_args__ = (
        Index('IDX_CHINAMUTUALFUNDNAV_ANN_DATE', 'ANN_DATE'),
        Index('INDEX_PRICE_DATE', 'PRICE_DATE'),
        Index('IDX_CHINAMUTUALFUNDNAV_CODE_DT', 'F_INFO_WINDCODE', 'PRICE_DATE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    PRICE_DATE = Column(VARCHAR(8), comment='截止日期')
    F_NAV_UNIT = Column(Numeric(24, 8), comment='单位净值')
    F_NAV_ACCUMULATED = Column(Numeric(24, 8), comment='累计净值')
    F_NAV_DIVACCUMULATED = Column(Numeric(20, 4), comment='累计分红(废弃)')
    F_NAV_ADJFACTOR = Column(Numeric(24, 8), comment='复权因子')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    F_PRT_NETASSET = Column(Numeric(20, 4), comment='资产净值')
    F_ASSET_MERGEDSHARESORNOT = Column(Numeric(1, 0), comment='是否合计数据')
    NETASSET_TOTAL = Column(Numeric(20, 4), comment='合计资产净值')
    F_NAV_ADJUSTED = Column(Numeric(22, 8), comment='复权单位净值')
    IS_EXDIVIDENDDATE = Column(Numeric(5, 0), comment='是否净值除权日')
    F_NAV_DISTRIBUTION = Column(Numeric(20, 4), comment='累计单位分配')


class CHINAMUTUALFUNDPCHREDM(Base):
    """中国共同基金申购赎回情况"""
    __tablename__ = 'CHINAMUTUALFUNDPCHREDM'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_UNIT_RPSTARTDATE = Column(VARCHAR(8), comment='报告期开始日期')
    F_UNIT_RPENDDATE = Column(VARCHAR(8), comment='报告期结束日期')
    F_UNIT_STARTSHARES = Column(Numeric(20, 4), comment='期初基金总份额(份)')
    F_UNIT_PURCHASE = Column(Numeric(20, 4), comment='本期基金总申购份额(份)')
    F_UNIT_REDEMPTION = Column(Numeric(20, 4), comment='本期基金总赎回份额(份)')
    F_UNIT_ENDSHARES = Column(Numeric(20, 4), comment='期末基金总份额(份)')
    TRADE_DT = Column(VARCHAR(8), comment='公告日期')
    F_UNIT_STARTSHARES_TOTAL = Column(Numeric(20, 4), comment='期初基金总份额-合计')
    F_UNIT_ENDSHARES_TOTAL = Column(Numeric(20, 4), comment='期末基金总份额-合计')
    F_UNIT_PURCHASE_TOTAL = Column(Numeric(20, 4), comment='本期基金总申购份额-合计')
    F_UNIT_REDEMPTION_TOTAL = Column(Numeric(20, 4), comment='本期基金总赎回份额-合计')
    IS_MERGE_DATA = Column(Numeric(5, 0), comment='是否为合并数据')


class CHINAMUTUALFUNDPOSESTIMATION(Base):
    """中国共同基金Wind基金仓位估算"""
    __tablename__ = 'CHINAMUTUALFUNDPOSESTIMATION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    F_EST_DATE = Column(VARCHAR(8), comment='估算日期')
    F_EST_LARGECAPWEG = Column(Numeric(20, 4), comment='大市值组合权重')
    F_EST_MIDCAPWEG = Column(Numeric(20, 4), comment='中市值组合权重')
    F_EST_SMALLCAPWEG = Column(Numeric(20, 4), comment='小市值组合权重')
    F_EST_POSITION = Column(Numeric(20, 4), comment='基金仓位')
    F_EST_NAV = Column(Numeric(20, 4), comment='估算收盘净值(元)')


class CHINAMUTUALFUNDREPNAVPER(Base):
    """中国共同基金净值表现(报告期)"""
    __tablename__ = 'CHINAMUTUALFUNDREPNAVPER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_INFO_REPORTPERIOD = Column(VARCHAR(8), comment='报告期')
    PERIOD_CODE = Column(VARCHAR(10), comment='期间代码')
    F_NAV_RETURN = Column(Numeric(20, 4), comment='净值增长率')
    F_NAV_STDDEVRETURN = Column(Numeric(20, 4), comment='净值增长率标准差')
    F_NAV_BENCHRETURN = Column(Numeric(20, 4), comment='业绩比较基准收益率')
    F_NAV_BENCHSTDDEV = Column(Numeric(20, 4), comment='业绩比较基准收益率标准差')
    F_NAV_BENCHDEVRETURN = Column(Numeric(20, 4), comment='净值增长率减基准收益率')
    F_NAV_STDDEVNAVBENCH = Column(Numeric(20, 4), comment='净值增长率标准差减基准收益率标准差')


class CHINAMUTUALFUNDSEATTRADING(Base):
    """中国共同基金席位交易量及佣金"""
    __tablename__ = 'CHINAMUTUALFUNDSEATTRADING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_REPORTPERIOD = Column(VARCHAR(8), comment='报告期')
    S_INFO_SECURNAME = Column(VARCHAR(100), comment='证券公司简称')
    F_TRADE_STOCKAM = Column(Numeric(20, 4), comment='股票交易金额(元)')
    F_TRADE_STOCKPRO = Column(Numeric(20, 4), comment='股票交易金额占比(%)')
    F_TRADE_BONDAM = Column(Numeric(20, 4), comment='债券交易金额(元)')
    F_TRADE_BONDPRO = Column(Numeric(20, 4), comment='债券交易金额占比(%)')
    F_TRADE_REPOAM = Column(Numeric(20, 4), comment='回购交易金额(元)')
    F_TRADE_REPOPRO = Column(Numeric(20, 4), comment='回购交易金额占比(%)')
    F_TRADE_SBAM = Column(Numeric(20, 4), comment='股票债券成交金额(元)')
    F_TRADE_SBPRO = Column(Numeric(20, 4), comment='股票债券交易量占比(%)')
    F_TRADE_WARRANTAM = Column(Numeric(20, 4), comment='权证交易金额(元)')
    F_TRADE_WARRANTPRO = Column(Numeric(20, 4), comment='权证交易金额占比(%)')
    F_TRADE_FUNDAM = Column(Numeric(20, 4), comment='基金交易金额(元)')
    F_TRADE_FUNDPRO = Column(Numeric(20, 4), comment='基金交易金额占比(%)')
    F_COMMISSIONAM = Column(Numeric(20, 4), comment='交易佣金(元)')
    F_COMMISSIONPRO = Column(Numeric(20, 4), comment='交易佣金占比(%)')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')


class CHINAMUTUALFUNDSECTOR(Base):
    """中国Wind基金分类"""
    __tablename__ = 'CHINAMUTUALFUNDSECTOR'
    __table_args__ = (
        Index('INDEX_F_INFO_WINDCODE', 'F_INFO_WINDCODE'),
        Index('INDEX_S_INFO_SECTOR', 'S_INFO_SECTOR'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SECTOR = Column(VARCHAR(40), comment='所属板块')
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_SECTOREXITDT = Column(VARCHAR(8), comment='截止日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class CHINAMUTUALFUNDSECTORQL(Base):
    """None"""
    __tablename__ = 'CHINAMUTUALFUNDSECTORQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    F_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_SECTOR = Column(VARCHAR(40))
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8))
    S_INFO_SECTOREXITDT = Column(VARCHAR(8))
    CUR_SIGN = Column(VARCHAR(10))


class CHINAMUTUALFUNDSECTORZL(Base):
    """中国Wind基金分类(增量)"""
    __tablename__ = 'CHINAMUTUALFUNDSECTORZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SECTOR = Column(VARCHAR(40), comment='所属板块')
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_SECTOREXITDT = Column(VARCHAR(8), comment='截止日期')
    CUR_SIGN = Column(VARCHAR(10), comment='最新标志')


class CHINAMUTUALFUNDSHARE(Base):
    """中国共同基金份额"""
    __tablename__ = 'CHINAMUTUALFUNDSHARE'
    __table_args__ = (
        Index('INDEX_F_INFO_WINDCODE_CHANGE_DT', 'F_INFO_WINDCODE', 'CHANGE_DATE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DATE = Column(VARCHAR(8), comment='变动日期')
    F_UNIT_TOTAL = Column(Numeric(20, 6), comment='基金总份额(万份)')
    F_INFO_SHARE = Column(Numeric(20, 6), comment='流通份额(万份)')
    FUNDSHARE = Column(Numeric(20, 6), comment='基金份额(万份)')
    F_UNIT_MERGEDSHARESORNOT = Column(Numeric(5, 0), comment='是否为合并数据')
    CHANGEREASON = Column(VARCHAR(10), comment='份额变动原因')
    FUNDSHARE_TOTAL = Column(Numeric(20, 6), comment='基金合计份额(万份)')
    CUR_SIGN = Column(Numeric(5, 0), comment='最新标志')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class CHINAMUTUALFUNDSTOCKPORTFOLIO(Base):
    """中国共同基金投资组合——持股明细"""
    __tablename__ = 'CHINAMUTUALFUNDSTOCKPORTFOLIO'
    __table_args__ = (
        Index('INDEX_F_PRT_ENDDATE', 'F_PRT_ENDDATE'),
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    F_PRT_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_STOCKWINDCODE = Column(VARCHAR(10), comment='持有股票Wind代码')
    F_PRT_STKVALUE = Column(Numeric(20, 4), comment='持有股票市值(元)')
    F_PRT_STKQUANTITY = Column(Numeric(20, 4), comment='持有股票数量（股）')
    F_PRT_STKVALUETONAV = Column(Numeric(20, 4), comment='持有股票市值占基金净值比例(%)')
    F_PRT_POSSTKVALUE = Column(Numeric(20, 4), comment='积极投资持有股票市值(元)')
    F_PRT_POSSTKQUANTITY = Column(Numeric(20, 4), comment='积极投资持有股数（股）')
    F_PRT_POSSTKTONAV = Column(Numeric(20, 4), comment='积极投资持有股票市值占净资产比例(%)')
    F_PRT_PASSTKEVALUE = Column(Numeric(20, 4), comment='指数投资持有股票市值(元)')
    F_PRT_PASSTKQUANTITY = Column(Numeric(20, 4), comment='指数投资持有股数（股）')
    F_PRT_PASSTKTONAV = Column(Numeric(20, 4), comment='指数投资持有股票市值占净资产比例(%)')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    STOCK_PER = Column(Numeric(20, 2), comment='占股票市值比')
    FLOAT_SHR_PER = Column(Numeric(24, 4), comment='占流通股本比例(%)')


class CHINAMUTUALFUNDSUSPENDPCHREDM(Base):
    """中国共同基金暂停申购赎回"""
    __tablename__ = 'CHINAMUTUALFUNDSUSPENDPCHREDM'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_SUSPCHSTARTDT = Column(VARCHAR(8), comment='暂停申购起始日期')
    F_INFO_SUSPCHANNDT = Column(VARCHAR(8), comment='暂停申购公告日期')
    F_INFO_REPCHDT = Column(VARCHAR(8), comment='恢复申购日期')
    F_INFO_REPCHANNDT = Column(VARCHAR(8), comment='恢复申购公告日期')
    F_INFO_PURCHASEUPLIMIT = Column(Numeric(20, 4), comment='单日申购上限')
    F_INFO_SUSPCHREASON = Column(VARCHAR(800), comment='暂停申购原因')
    F_INFO_SUSPCHTYPE = Column(Numeric(9, 0), comment='暂停申购类型代码')


class CHINAMUTUALFUNDTRACKINGINDEX(Base):
    """中国共同基金被动型基金跟踪指数"""
    __tablename__ = 'CHINAMUTUALFUNDTRACKINGINDEX'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDEXWINDCODE = Column(VARCHAR(40), comment='跟踪指数Wind代码')
    ENTRY_DT = Column(VARCHAR(8), comment='生效日期')
    REMOVE_DT = Column(VARCHAR(8), comment='失效日期')


class CHINAMUTUALFUNDTRACKINGINDEXQL(Base):
    """None"""
    __tablename__ = 'CHINAMUTUALFUNDTRACKINGINDEXQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    S_INFO_INDEXWINDCODE = Column(VARCHAR(40))
    ENTRY_DT = Column(VARCHAR(8))
    REMOVE_DT = Column(VARCHAR(8))


class CHINAMUTUALFUNDTRACKINGINDEXZL(Base):
    """中国共同基金被动型基金跟踪指数(增量)"""
    __tablename__ = 'CHINAMUTUALFUNDTRACKINGINDEXZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_INDEXWINDCODE = Column(VARCHAR(40), comment='跟踪指数Wind代码')
    ENTRY_DT = Column(VARCHAR(8), comment='生效日期')
    REMOVE_DT = Column(VARCHAR(8), comment='失效日期')


class CHINAMUTUALFUNDTRANSFORMATION(Base):
    """中国共同基金转型"""
    __tablename__ = 'CHINAMUTUALFUNDTRANSFORMATION'
    __table_args__ = (
        Index('INDEX_POSTWINDCODE', 'POSTWINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    PREWINDCODE = Column(VARCHAR(40), comment='转型前基金Wind代码')
    POSTWINDCODE = Column(VARCHAR(40), comment='转型后基金Wind代码')
    F_INFO_PRENAME = Column(VARCHAR(40), comment='转型前基金简称')
    F_INFO_PREFULLNAME = Column(VARCHAR(100), comment='转型前基金全称')
    F_INFO_PRECODE = Column(VARCHAR(10), comment='转型前基金代码')
    F_INFO_POSTNAME = Column(VARCHAR(40), comment='转型后基金简称')
    F_INFO_POSTFULLNAME = Column(VARCHAR(100), comment='转型后基金全称')
    F_INFO_POSTCODE = Column(VARCHAR(10), comment='转型后基金代码')
    F_INFO_POSTISLIST = Column(Numeric(1, 0), comment='基金封转开后是否上市')
    F_INFO_CTOSUSPENDDATE = Column(VARCHAR(8), comment='封转开停牌起始日期')
    F_INFO_MEETINGANNDATE = Column(VARCHAR(8), comment='基金转型会议召开公告日期')
    F_INFO_MEETINGDATE = Column(VARCHAR(8), comment='基金转型会议日期')
    F_INFO_APPROVALRATE = Column(Numeric(20, 8), comment='基金转型赞成率(%)')
    F_INFO_RESUMPDATE = Column(VARCHAR(8), comment='封转开复牌日期')
    F_INFO_CFUNDREDEMCODE = Column(VARCHAR(10), comment='原封闭式基金持有人赎回代码')
    F_INFO_CFUNDENDDATE = Column(VARCHAR(8), comment='封闭式基金终止上市日期')
    F_INFO_CFUNDENDANNDATE = Column(VARCHAR(8), comment='封闭式基金终止上市公告日期')
    F_INFO_TANSTYPE = Column(VARCHAR(40), comment='转型类别')
    F_UNIT_PCH = Column(Numeric(20, 4), comment='集中申购份额')
    F_UNIT_SPLITSHARE = Column(Numeric(20, 4), comment='转型拆分份额')
    F_INFOTANSTYPECODE = Column(Numeric(9, 0), comment='转型类别代码')
    F_FUND_TRANSFORMATION_DATE = Column(VARCHAR(8), comment='基金转型生效日期')


class CHINAMUTUALFUNDTRANSFORMATIONZ(Base):
    """中国共同基金转型(增量)"""
    __tablename__ = 'CHINAMUTUALFUNDTRANSFORMATIONZ'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    PREWINDCODE = Column(VARCHAR(40), comment='转型前基金Wind代码')
    POSTWINDCODE = Column(VARCHAR(40), comment='转型后基金Wind代码')
    F_INFO_PRENAME = Column(VARCHAR(40), comment='转型前基金简称')
    F_INFO_PREFULLNAME = Column(VARCHAR(100), comment='转型前基金全称')
    F_INFO_PRECODE = Column(VARCHAR(10), comment='转型前基金代码')
    F_INFO_POSTNAME = Column(VARCHAR(40), comment='转型后基金简称')
    F_INFO_POSTFULLNAME = Column(VARCHAR(100), comment='转型后基金全称')
    F_INFO_POSTCODE = Column(VARCHAR(10), comment='转型后基金代码')
    F_INFO_POSTISLIST = Column(Numeric(1, 0), comment='基金封转开后是否上市')
    F_INFO_CTOSUSPENDDATE = Column(VARCHAR(8), comment='封转开停牌起始日期')
    F_INFO_MEETINGANNDATE = Column(VARCHAR(8), comment='基金转型会议召开公告日期')
    F_INFO_MEETINGDATE = Column(VARCHAR(8), comment='基金转型会议日期')
    F_INFO_APPROVALRATE = Column(Numeric(20, 8), comment='基金转型赞成率(%)')
    F_INFO_RESUMPDATE = Column(VARCHAR(8), comment='封转开复牌日期')
    F_INFO_CFUNDREDEMCODE = Column(VARCHAR(10), comment='原封闭式基金持有人赎回代码')
    F_INFO_CFUNDENDDATE = Column(VARCHAR(8), comment='封闭式基金终止上市日期')
    F_INFO_CFUNDENDANNDATE = Column(VARCHAR(8), comment='封闭式基金终止上市公告日期')
    F_INFO_TANSTYPE = Column(VARCHAR(40), comment='转型类别')
    F_UNIT_PCH = Column(Numeric(20, 4), comment='集中申购份额')
    F_UNIT_SPLITSHARE = Column(Numeric(20, 4), comment='转型拆分份额')
    F_INFOTANSTYPECODE = Column(Numeric(9, 0), comment='转型类别代码')
    F_FUND_TRANSFORMATION_DATE = Column(VARCHAR(8), comment='基金转型生效日期')


class CLOSEDFUNDPCHREDM(Base):
    """中国封闭式基金场内申购赎回"""
    __tablename__ = 'CLOSEDFUNDPCHREDM'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所')
    SUBSTRIPTION_CODE = Column(VARCHAR(20), comment='场内认购代码')
    SUBSTRIPTION_NAME = Column(VARCHAR(40), comment='场内认购简称')
    SUBSTRIPTION_PRICE = Column(Numeric(20, 4), comment='场内认购价格')
    SUBSTRIPTION_START_DT = Column(VARCHAR(8), comment='场内认购起始日')
    SUBSTRIPTION_END_DT = Column(VARCHAR(8), comment='场内认购截止日')
    PCH_CODE = Column(VARCHAR(20), comment='场内基金代码')
    PCH_NAME = Column(VARCHAR(40), comment='场内基金简称')
    PCH_START_DT = Column(VARCHAR(8), comment='场内申购起始日')
    REDM_START_DT = Column(VARCHAR(8), comment='场内赎回起始日')


class CMFAIPINFO(Base):
    """None"""
    __tablename__ = 'CMFAIPINFO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    START_DT = Column(VARCHAR(8), comment='定投开始时间')
    END_DT = Column(VARCHAR(8), comment='定投截止日期')
    MIN_PURCHASE = Column(Numeric(20, 4), comment='定投起始金额(元)')
    MAX_PURCHASE = Column(Numeric(20, 4), comment='定投最高金额(元)')
    LEVEL_AMOUNT = Column(Numeric(20, 4), comment='投资额级差(元)')
    TYPE_CODE = Column(Numeric(9, 0), comment='定投类型代码')
    COMP_NAME = Column(VARCHAR(200), comment='定投代销机构名称')
    COMP_ID = Column(VARCHAR(10), comment='定投代销机构ID')
    MEMO = Column(VARCHAR(500), comment='备注')
    SEQUENCE = Column(Numeric(1, 0), comment='序号')


class CMFBALANCESHEET(Base):
    """中国共同基金资产负债表"""
    __tablename__ = 'CMFBALANCESHEET'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    IS_LIST = Column(Numeric(5, 0), comment='是否上市后数据')
    F_STM_BS = Column(Numeric(20, 4), comment='银行存款')
    SETTLE_RSRV = Column(Numeric(20, 4), comment='清算备付金')
    MRGN_PAID = Column(Numeric(20, 4), comment='交易保证金')
    TRADABLE_FIN_ASSETS = Column(Numeric(20, 4), comment='交易性金融资产')
    STOCK_VALUE = Column(Numeric(20, 4), comment='股票投资市值')
    STOCK_COST = Column(Numeric(20, 4), comment='股票投资成本')
    STOCK_ADD_VALUE = Column(Numeric(20, 4), comment='股票投资估值增值')
    FUND_VALUE = Column(Numeric(20, 4), comment='基金投资市值(基金投资)')
    BOND_VALUE = Column(Numeric(20, 4), comment='债券投资市值')
    ABS_VALUE = Column(Numeric(20, 4), comment='资产支持证券投资市值')
    BOND_COST = Column(Numeric(20, 4), comment='债券投资成本')
    BOND_ADD_VALUE = Column(Numeric(20, 4), comment='债券投资估值增值')
    GOVBOND_COST = Column(Numeric(20, 4), comment='国债投资成本')
    GOVBOND_ADD_VALUE = Column(Numeric(15, 2), comment='国债投资估值增值')
    CONVERTBOND_COST = Column(Numeric(20, 4), comment='可转债投资成本')
    CONVERTBOND_ADD_VALUE = Column(Numeric(20, 4), comment='可转债投资估值增值')
    DERIVATIVE_FIN_VALUE = Column(Numeric(20, 4), comment='权证投资市值')
    DERIVATIVE_FIN_COST = Column(Numeric(20, 4), comment='权证投资成本')
    TRADE_RCV = Column(Numeric(20, 4), comment='应收证券交易清算款')
    WAR_RCV = Column(Numeric(20, 4), comment='配股权证')
    INT_RCV = Column(Numeric(20, 4), comment='应收利息')
    ACCT_RCV = Column(Numeric(20, 4), comment='应收帐款')
    DVD_RCV = Column(Numeric(20, 4), comment='应收股利')
    PUR_RCV = Column(Numeric(20, 4), comment='应收申购款')
    DEFERRED_TAX_ASSETS = Column(Numeric(20, 4), comment='递延所得税资产')
    OTH_RCV = Column(Numeric(20, 4), comment='其他应收款项')
    DEFERRED_EXP = Column(Numeric(20, 4), comment='待摊费用')
    REPO_REV = Column(Numeric(20, 4), comment='买入返售证券')
    OTH_ASSETS = Column(Numeric(20, 4), comment='其他资产')
    TOT_ASSETS = Column(Numeric(20, 4), comment='资产总计')
    ST_BORROW = Column(Numeric(20, 4), comment='短期借款')
    MANAGE_PAYABLE = Column(Numeric(20, 4), comment='应付基金管理费')
    TRUSTEE_PAYABLE = Column(Numeric(20, 4), comment='应付基金托管费')
    SEC_TRADE_PAYABLE = Column(Numeric(20, 4), comment='应付交易清算款')
    ACCT_PAYABLE = Column(Numeric(20, 4), comment='应付帐款')
    TRADE_PAYABLE = Column(Numeric(20, 4), comment='应付佣金')
    OTH_PAYABLE = Column(Numeric(20, 4), comment='其他应付款项')
    RIGHT_PAYABLE = Column(Numeric(20, 4), comment='应付配股款')
    REDE_PAYABLE = Column(Numeric(20, 4), comment='应付赎回费')
    REDE_PAYABLE2 = Column(Numeric(20, 4), comment='应付赎回款')
    REPO_AMOUNT = Column(Numeric(20, 4), comment='卖出回购证券')
    INT_PAYABLE = Column(Numeric(20, 4), comment='应付利息')
    REV_PAYABLE = Column(Numeric(20, 4), comment='应付收益')
    NOTPAYTAX = Column(Numeric(20, 4), comment='未交税金')
    ACC_EXP = Column(Numeric(20, 4), comment='预提费用')
    DEFERRED_TAX_LIAB = Column(Numeric(20, 4), comment='递延所得税负债')
    OTH_LIAB = Column(Numeric(20, 4), comment='其他负债')
    SELL_EXP = Column(Numeric(20, 4), comment='应付销售费用')
    TRADABLE_FIN_LIAB = Column(Numeric(20, 4), comment='交易性金融负债')
    DERIVATIVE_FIN_LIAB = Column(Numeric(20, 4), comment='衍生金融负债')
    TOT_LIAB = Column(Numeric(20, 4), comment='负债总额')
    PAIDINCAPITAL = Column(Numeric(20, 4), comment='实收基金')
    UNDISTRIBUTED_ET_INC = Column(Numeric(20, 4), comment='未分配收益')
    UNREALIZED_PROFIT = Column(Numeric(20, 4), comment='未实现利得')
    UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='未分配利润')
    UNREALIZED_ADD_VALUE = Column(Numeric(20, 4), comment='未实现估值增值')
    HOLDER_EQUITY = Column(Numeric(20, 4), comment='持有人权益合计')
    PRT_NETASSET = Column(Numeric(20, 4), comment='基金资产净值')
    TOT_LIAB_SHRHLDR_EQY = Column(Numeric(20, 4), comment='负债及持有人权益合计')


class CMFCODEANDSNAME(Base):
    """中国共同基金业务代码及简称"""
    __tablename__ = 'CMFCODEANDSNAME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TYPE_CODE = Column(Numeric(9, 0), comment='业务类型代码')
    S_CODE = Column(VARCHAR(20), comment='业务代码')
    S_SNAME = Column(VARCHAR(100), comment='业务简称')
    IS_COMMON = Column(Numeric(1, 0), comment='是否通用代码')
    MEMO = Column(VARCHAR(800), comment='备注')


class CMFCONSEPTION(Base):
    """中国共同基金Wind概念分类"""
    __tablename__ = 'CMFCONSEPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SECTOR = Column(VARCHAR(10), comment='所属板块代码')
    S_INFO_SECTORNAME = Column(VARCHAR(40), comment='所属板块名称')
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_SECTOREXITDT = Column(VARCHAR(8), comment='截止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CMFDESCCHANGE(Base):
    """中国共同基金基本资料属性变更"""
    __tablename__ = 'CMFDESCCHANGE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ITEM = Column(VARCHAR(50), comment='变更字段名称')
    CHANGE_DT = Column(VARCHAR(8), comment='变更日期')
    S_INFO_OLD = Column(VARCHAR(2100), comment='变更前')
    S_INFO_NEW = Column(VARCHAR(2300), comment='变更后')


class CMFFAIRVALUECHANGEPROFIT(Base):
    """中国共同基金公允价值变动收益(报告期)"""
    __tablename__ = 'CMFFAIRVALUECHANGEPROFIT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    STOCK_CHANGE_FAIR_VALUE = Column(Numeric(20, 4), comment='股票投资公允价值变动收益')
    BOND_CHANGE_FAIR_VALUE = Column(Numeric(20, 4), comment='债券投资(交易所市场)公允价值变动收益')
    BOND1_CHANGE_FAIR_VALUE = Column(Numeric(20, 4), comment='债券投资(银行间同业市场)公允价值变动收益')
    WARRANT_CHANGE_FAIR_VALUE = Column(Numeric(20, 4), comment='权证投资公允价值变动收益')
    TOT_CHANGE_FAIR_VALUE = Column(Numeric(20, 4), comment='合计公允价值变动收益')
    ABS_CHANGE_FAIR_VALUE = Column(Numeric(20, 4), comment='资产支持证券投资公允价值变动收益')
    FORWARD_CHANGE_FAIR_VALUE = Column(Numeric(20, 4), comment='外汇远期投资公允价值变动收益')
    FUND_CHANGE_FAIR_VALUE = Column(Numeric(20, 4), comment='基金投资公允价值变动收益')
    OTHER = Column(Numeric(20, 4), comment='其他')
    MEMO = Column(VARCHAR(200), comment='备注')


class CMFFINANCIALINDICATOR(Base):
    """中国共同基金财务指标(报告期)"""
    __tablename__ = 'CMFFINANCIALINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    IS_LIST = Column(Numeric(5, 0), comment='是否上市后数据')
    ANAL_NETINCOME = Column(Numeric(20, 4), comment='本期利润扣减本期公允价值变动损益后的净额')
    ANAL_INCOME = Column(Numeric(20, 4), comment='本期利润')
    ANAL_AVGNETINCOMEPERUNIT = Column(Numeric(20, 4), comment='加权平均基金份额本期利润')
    ANAL_AVGNAVRETURN = Column(Numeric(20, 4), comment='加权平均净值利润率(%)')
    ANAL_NAV_RETURN = Column(Numeric(20, 4), comment='净值增长率(%)')
    NAV_ACC_RETURN = Column(Numeric(20, 4), comment='累计净值增长率(%)')
    ANAL_DISTRIBUTABLE = Column(Numeric(20, 4), comment='期末可供分配基金收益')
    ANAL_DISTRIBUTABLEPERUNIT = Column(Numeric(20, 4), comment='期末可供分配单位基金收益')
    PRT_NETASSET = Column(Numeric(20, 4), comment='资产净值')
    PRT_NETASSETPERUNIT = Column(Numeric(20, 4), comment='单位净值')
    PRT_TOTALASSET = Column(Numeric(20, 4), comment='资产总值')
    UNIT_TOTAL = Column(Numeric(20, 4), comment='期末基金总份额(份)')


class CMFFIXEDINVESTMENTRATE(Base):
    """中国共同基金定投收益率及排名表"""
    __tablename__ = 'CMFFIXEDINVESTMENTRATE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    F_TYPE_CODE = Column(VARCHAR(20), comment='投资类型代码')
    F_TYPE_NAME = Column(VARCHAR(40), comment='基金投资类型名称')
    F_FIXED_INVESTMENT_CYCLE = Column(VARCHAR(20), comment='定投周期')
    F_FIXED_AMOUNT = Column(Numeric(20, 0), comment='定投金额')
    F_PURCHASE_RATE = Column(Numeric(20, 4), comment='申购费率')
    F_DIVIDEND_METHOD = Column(VARCHAR(20), comment='分红方式')
    F_AVGRETURN_THISYEAR = Column(Numeric(20, 6), comment='近一年定投总收益率')
    F_SFRANK_RECENTYEART = Column(VARCHAR(20), comment='近一年定投同类排名')
    F_ANNUALYEILD_THISYEAR = Column(Numeric(20, 6), comment='近一年定投年化收益率')
    F_RECENTYEART_THISYEAR = Column(VARCHAR(20), comment='近一年定投年化收益同类排名')
    F_AVGRETURN_TWOYEAR = Column(Numeric(20, 6), comment='近二年定投总收益率')
    F_SFRANK_RECENTYEART_TWOSYEAR = Column(VARCHAR(20), comment='近二年定投同类排名')
    F_ANNUALYEILD_TWOSYEAR = Column(Numeric(20, 6), comment='近二年定投年化收益率')
    F_ANNUALYEILD_TWOYEAR = Column(VARCHAR(20), comment='近二年定投年化收益同类排名')
    F_AVGRETURN_THREEYEAR = Column(Numeric(20, 6), comment='近三年定投总收益率')
    F_SFRANK_THREESYEAR = Column(VARCHAR(20), comment='近三年定投同类排名')
    F_ANNUALYEILD_THREESYEAR = Column(Numeric(20, 6), comment='近三年定投年化收益率')
    F_ANNUALYEILD_THREEYEAR = Column(VARCHAR(20), comment='近三年定投年化收益同类排名')
    F_AVGRETURN_FIVEYEAR = Column(Numeric(20, 6), comment='近五年定投总收益率')
    F_SFRANK_RECENTYEART_FIVESYEAR = Column(VARCHAR(20), comment='近五年定投同类排名')
    F_ANNUALYEILD_FIVESYEAR = Column(Numeric(20, 6), comment='近五年定投年化收益率')
    F_ANNUALYEILD_FIVEYEAR = Column(VARCHAR(20), comment='近五年定投年化收益同类排名')


class CMFHOLDER(Base):
    """中国共同基金持有人"""
    __tablename__ = 'CMFHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='证券ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_FA_LATELYRD = Column(VARCHAR(8), comment='报告期')
    S_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    B_INFO_HOLDER = Column(VARCHAR(200), comment='持有人')
    B_INFO_HOLDAMOUNT = Column(Numeric(20, 4), comment='数量(股、张、份)')
    B_ISSUER_SHARECATEGORY = Column(VARCHAR(1), comment='[内部]股东类型： 1 个人；2 公司')


class CMFHOLDERSTRUCTURE(Base):
    """中国共同基金持有人结构"""
    __tablename__ = 'CMFHOLDERSTRUCTURE'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券ID')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    SCOPE = Column(VARCHAR(10), comment='范围')
    HOLDER_NUMBER = Column(Numeric(20, 0), comment='基金份额持有人户数(户)')
    HOLDER_AVGHOLDING = Column(Numeric(20, 4), comment='平均每户持有基金份额(份)')
    HOLDER_INSTITUTION_HOLDING = Column(Numeric(20, 4), comment='机构投资者持有份额(份)')
    HOLDER_INSTITUTION_HOLDINGPCT = Column(Numeric(20, 4), comment='机构投资者持有份额占比(%)')
    HOLDER_PERSONAL_HOLDING = Column(Numeric(20, 4), comment='个人投资者持有份额(份)')
    HOLDER_PERSONAL_HOLDINGPCT = Column(Numeric(20, 4), comment='个人投资者持有份额占比(%)')
    HOLDER_MNGEMP_HOLDING = Column(Numeric(20, 4), comment='管理人员工持有份额(份)')
    HOLDER_MNGEMP_HOLDINGPCT = Column(Numeric(20, 8), comment='管理人员工持有份额占比(%)')
    HOLDER_FEEDER_HOLDING = Column(Numeric(20, 4), comment='联接基金持有份额(份)')
    HOLDER_FEEDER_HOLDINGPCT = Column(Numeric(20, 4), comment='联接基金持有份额占比(%)')
    PUR_COST = Column(Numeric(20, 4), comment='报告期买入股票成本总额(元)')
    SELL_INCOME = Column(Numeric(20, 4), comment='报告期卖出股票收入总额(元)')


class CMFHOLDINGRATIOANOMALY(Base):
    """中国共同基金单一投资者持有基金份额比例异常信息"""
    __tablename__ = 'CMFHOLDINGRATIOANOMALY'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_UNIT_RPSTARTDATE = Column(VARCHAR(8), comment='报告期开始日期')
    F_UNIT_RPENDDATE = Column(VARCHAR(8), comment='报告期截止日期')
    TRADE_DT = Column(VARCHAR(8), comment='公告日期')
    F_INQUIRER_TYPE = Column(VARCHAR(100), comment='投资者类别')
    F_INQUIRER_TYPE_NUM = Column(Numeric(2, 0), comment='投资者序号')
    F_HOLDING_TIME = Column(VARCHAR(500), comment='持有时间区间')
    F_START_NUM_HOLDER = Column(Numeric(20, 4), comment='期初持有份额')
    F_UNIT_PCH = Column(Numeric(20, 4), comment='申购份额')
    F_UNIT_REDM = Column(Numeric(20, 4), comment='赎回份额')
    F_END_NUM_HOLDER = Column(Numeric(20, 4), comment='期末持有份额')
    F_END_NUM_HOLDER_PROPORTION = Column(Numeric(20, 4), comment='期末持有份额占基金份额比例')
    IS_MERGE = Column(Numeric(1, 0), comment='是否为合并数据')
    F_INQUIRER_TYPECODE = Column(VARCHAR(1), comment='投资者类别代码')


class CMFINCOME(Base):
    """中国共同基金利润表"""
    __tablename__ = 'CMFINCOME'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    IS_LIST = Column(Numeric(5, 0), comment='是否上市后数据')
    TOT_INC = Column(Numeric(20, 4), comment='收入合计')
    INT_INC = Column(Numeric(20, 4), comment='利息收入合计')
    CASH_INT_INC = Column(Numeric(20, 4), comment='存款利息收入')
    BOND_INT_INC = Column(Numeric(20, 4), comment='债券利息收入')
    ABS_INT_INC = Column(Numeric(20, 4), comment='资产支持证券利息收入')
    REPO_INT_INC = Column(Numeric(20, 4), comment='买入返售证券收入')
    OTHER_INT_INC = Column(Numeric(20, 4), comment='其他利息收入')
    INV_INC = Column(Numeric(20, 4), comment='投资收益合计')
    STOCK_INV_INC = Column(Numeric(20, 4), comment='股票差价收入')
    BOND_INV_INC = Column(Numeric(20, 4), comment='债券差价收入')
    FUND_INV_INC = Column(Numeric(20, 4), comment='证券买卖差价-基金')
    ABS_INV_INC = Column(Numeric(20, 4), comment='资产支持证券投资收益')
    DERIVATIVE_INV_INC = Column(Numeric(20, 4), comment='权证差价收入')
    DVD_INC = Column(Numeric(20, 4), comment='股息收入')
    CHANGE_FAIR_VALUE = Column(Numeric(22, 4), comment='未实现利得')
    EXCH_INC = Column(Numeric(20, 4), comment='汇兑收入')
    OTHER_INC = Column(Numeric(20, 4), comment='其它收入')
    TOT_EXP = Column(Numeric(20, 4), comment='费用合计')
    MGMT_EXP = Column(Numeric(20, 4), comment='管理费')
    CUST_MAINT_EXP = Column(Numeric(20, 4), comment='客户维护费')
    CUSTODIAN_EXP = Column(Numeric(20, 4), comment='托管费')
    SELLING_DIST_EXP = Column(Numeric(20, 4), comment='基金销售服务费')
    TRADE_EXP = Column(Numeric(20, 4), comment='交易费用')
    INT_EXP = Column(Numeric(20, 4), comment='利息支出')
    REPO_EXP = Column(Numeric(20, 4), comment='卖出回购证券支出')
    OTHER_EXP = Column(Numeric(20, 4), comment='其他费用合计')
    ACCT_EXP = Column(Numeric(20, 4), comment='会计师费')
    AUDIT_EXP = Column(Numeric(20, 4), comment='审计费用')
    TOT_PROFIT = Column(Numeric(22, 4), comment='基金经营业绩')
    INC_TAX = Column(Numeric(20, 4), comment='所得税费用')
    NET_PROFIT = Column(Numeric(20, 4), comment='净利润')
    MEMO = Column(VARCHAR(1000), comment='备注')


class CMFINDEXDESCRIPTION(Base):
    """中国共同基金指数基本资料"""
    __tablename__ = 'CMFINDEXDESCRIPTION'
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
    INCOME_PROCESSING_METHOD = Column(VARCHAR(20), comment='收益处理方式')
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


class CMFINDEXEOD(Base):
    """中国共同基金指数行情"""
    __tablename__ = 'CMFINDEXEOD'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='指数简称')
    TRADE_DT = Column(VARCHAR(8), comment='交易日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='最新价')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')


class CMFINDUSTRYPLATE(Base):
    """中国共同基金WIND行业板块主题分类"""
    __tablename__ = 'CMFINDUSTRYPLATE'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_SECTOR = Column(VARCHAR(16), comment='板块代码')
    S_INFO_NAME = Column(VARCHAR(100), comment='板块名称')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='成份万得代码')


class CMFIOPVNAV(Base):
    """中国上市基金IOPV收盘净值"""
    __tablename__ = 'CMFIOPVNAV'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    PRICE_DATE = Column(VARCHAR(8), comment='日期')
    F_IOPV_NAV = Column(Numeric(20, 8), comment='IOPV收盘净值')


class CMFISSUINGDATEPREDICT(Base):
    """中国共同基金定期报告披露日期"""
    __tablename__ = 'CMFISSUINGDATEPREDICT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='基金ID')
    START_DT = Column(VARCHAR(8), comment='报告起始日')
    END_DT = Column(VARCHAR(8), comment='报告截止日')
    S_STM_ACTUAL_ISSUINGDATE = Column(VARCHAR(8), comment='实际披露日期')
    S_STM_CORRECT_NUM = Column(VARCHAR(20), comment='更正公告披露次数')
    S_STM_CORRECT_ISSUINGDATE = Column(VARCHAR(8), comment='更正公告披露日期')
    S_OPERATION_REVIEW = Column(TEXT(2147483647), comment='市场与基金运作回顾')
    S_RATE_RATINGOUTLOOK = Column(TEXT(2147483647), comment='市场展望')
    S_RATINGOUTLOOK = Column(VARCHAR(800), comment='市场展望(精简版)')


class CMFLIQUIDATION(Base):
    """中国共同基金清算"""
    __tablename__ = 'CMFLIQUIDATION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CLEARINGTYPE_CODE = Column(Numeric(9, 0), comment='清算类型代码')
    STARTDATE_CLEARING = Column(VARCHAR(8), comment='清算起始日')
    ENDDATE_CLEARING = Column(VARCHAR(8), comment='清算终止日')
    REASONS_CLEARING = Column(VARCHAR(2000), comment='清算原因说明')
    TIMES_CLEARING = Column(Numeric(5, 0), comment='清算次数')
    FIRST_ANN_DATE = Column(VARCHAR(8), comment='首次披露日期')


class CMFMGQUALIFICATIONS(Base):
    """中国共同基金基金经理资历表"""
    __tablename__ = 'CMFMGQUALIFICATIONS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_FUNDMANAGER_ID = Column(VARCHAR(10), comment='基金经理ID')
    CHARACTER_QUALFN = Column(VARCHAR(100), comment='人物资历代码')
    BEGIN_DT = Column(VARCHAR(8), comment='起始日期')
    END_DT = Column(VARCHAR(8), comment='终止日期')


class CMFNAVCHANGE(Base):
    """中国共同基金净值变动表"""
    __tablename__ = 'CMFNAVCHANGE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    RPSTARTDATE = Column(VARCHAR(8), comment='报告期开始日期')
    RPENDDATE = Column(VARCHAR(8), comment='报告期结束日期')
    BEG_NAV = Column(Numeric(22, 4), comment='期初基金净值')
    FUND_NETINCOME = Column(Numeric(22, 4), comment='基金净收益')
    UNREALCAPGAINS = Column(Numeric(22, 4), comment='未实现资本利得')
    NAVCHANGE_OPER_ACT = Column(Numeric(22, 4), comment='经营活动产生的基金净值变动')
    ADJLOSSGAIN_PREVYEAR = Column(Numeric(22, 4), comment='以前年度损益调整')
    NAVCHANGE_RES_TOHOLDERS = Column(Numeric(22, 4), comment='向基金持有人分配收益产生的基金净值变动数')
    EDN_NAV = Column(Numeric(22, 4), comment='期末基金净值')
    BEG_NAV_ADJ = Column(Numeric(20, 4), comment='调整后年初基金净值')
    CUR_FUND_UNIT_TRADE = Column(Numeric(20, 4), comment='本期基金单位交易')
    FUND_PUR = Column(Numeric(20, 4), comment='基金申购款')
    FUND_REDE = Column(Numeric(20, 4), comment='基金赎回款')
    NAVCHANGE_FUND_UNIT_TRADE = Column(Numeric(20, 4), comment='基金单位交易产生的基金净值变动数')
    BEG_FUNDS_REC = Column(Numeric(20, 4), comment='期初实收基金')
    FUNDS_REC_CHANGE_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的实收基金变动数')
    FUNDS_REC_CHANGE_FUNIT_TRADE = Column(Numeric(20, 4), comment='基金单位交易产生的实收基金变动数')
    FUNDS_REC_PUR = Column(Numeric(20, 4), comment='基金申购款-实收基金')
    FUNDS_REC_REDE = Column(Numeric(20, 4), comment='基金赎回款-实收基金')
    FUNDS_REC_CHANGE_RES_TOHOLD = Column(Numeric(20, 4), comment='向基金持有人分配收益产生的实收基金变动数')
    END_FUNDS_REC = Column(Numeric(20, 4), comment='期末实收基金')
    BEG_UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='期初未分配利润')
    UNDTPRTCHANGE_OPER_ACT = Column(Numeric(20, 4), comment='经营活动产生的未分配利润变动数')
    UNDTPRTCHANGE_FUNIT_TRADE = Column(Numeric(20, 4), comment='基金单位交易产生的未分配利润变动数')
    FUND_PUR_UNDTPRT = Column(Numeric(20, 4), comment='基金申购款-未分配利润')
    FUND_REDE_UNDTPRT = Column(Numeric(20, 4), comment='基金赎回款-未分配利润')
    UNDTPRT_CHANGE_RES_TOHOLD = Column(Numeric(20, 4), comment='向基金持有人分配收益产生的未分配利润变动数')
    END_UNDISTRIBUTED_PROFIT = Column(Numeric(20, 4), comment='期末未分配利润')


class CMFNAVOPERATIONRECORD(Base):
    """中国共同基金净值操作记录表"""
    __tablename__ = 'CMFNAVOPERATIONRECORD'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    PRICE_DATE = Column(VARCHAR(8), comment='净值截止日期')
    HANDLE_DATE = Column(VARCHAR(8), comment='处理日期')
    HANDLE_ACTION = Column(VARCHAR(20), comment='处理动作')
    F_NAV_OLD = Column(Numeric(11, 6), comment='调整前净值')


class CMFOTHERPORTFOLIO(Base):
    """中国共同基金投资组合——其他证券"""
    __tablename__ = 'CMFOTHERPORTFOLIO'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    END_DT = Column(VARCHAR(8), comment='截止日期')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='货币代码')
    S_INFO_HOLDWINDCODE = Column(VARCHAR(40), comment='Wind代码')
    VALUE = Column(Numeric(20, 4), comment='持仓市值')
    QUANTITY = Column(Numeric(20, 4), comment='持仓数量(股/张)')
    VALUETONAV = Column(Numeric(20, 4), comment='持仓市值占基金净值比例(%)')


class CMFPREFERENTIALFEE(Base):
    """中国共同基金优惠费率（废弃）"""
    __tablename__ = 'CMFPREFERENTIALFEE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(10), comment='证券ID')
    TYPE_CODE = Column(Numeric(9, 0), comment='优惠活动类型代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    START_DT = Column(VARCHAR(8), comment='费率优惠开始日期')
    END_DT = Column(VARCHAR(8), comment='费率优惠截止日期')
    AMOUNTDOWNLIMIT = Column(Numeric(20, 4), comment='申购金额下限(万元)')
    AMOUNTUPLIMIT = Column(Numeric(20, 4), comment='申购金额上限(万元)')
    PREFERENTIAL_RATE = Column(Numeric(20, 4), comment='优惠费率(%)')
    WAY_TYPE = Column(Numeric(9, 0), comment='优惠活动参与方式代码')
    COMP_NAME = Column(VARCHAR(200), comment='参加优惠活动的代销机构名称')
    COMP_ID = Column(VARCHAR(10), comment='参加优惠活动的代销机构公司ID')
    MEMO = Column(VARCHAR(500), comment='备注')
    SEQUENCE = Column(Numeric(1, 0), comment='序号')


class CMFPROPORTIONOFINVEOBJ(Base):
    """中国共同基金投资品种比例信息"""
    __tablename__ = 'CMFPROPORTIONOFINVEOBJ'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    INVEST_PCT_TYPECODE = Column(Numeric(9, 0), comment='基金投资占比类型代码')
    STOCK_INVEST_PCT_DOWN = Column(Numeric(5, 0), comment='股票投资比例下限')
    STOCK_INVEST_PCT_UP = Column(Numeric(5, 0), comment='股票投资比例上限')
    BOND_INVEST_PCT_DOWN = Column(Numeric(5, 0), comment='债券投资比例下限')
    BOND_INVEST_PCT_UP = Column(Numeric(5, 0), comment='债券投资比例上限')
    MMT_INVEST_PCT_DOWN = Column(Numeric(5, 0), comment='货币工具比例下限')
    MMT_INVEST_PCT_UP = Column(Numeric(5, 0), comment='货币工具比例上限')
    FUND_INVEST_PCT_DOWN = Column(Numeric(5, 0), comment='基金投资比例下限')
    FUND_INVEST_PCT_UP = Column(Numeric(5, 0), comment='基金投资比例上限')
    COMM_INVEST_PCT_DOWN = Column(Numeric(5, 0), comment='商品衍生品投资比例下限')
    COMM_INVEST_PCT_UP = Column(Numeric(5, 0), comment='商品衍生品投资比例上限')
    IS_TOT_PCT = Column(Numeric(1, 0), comment='是否合计占比')
    OTHER_INVEST_PCT_DOWN = Column(Numeric(5, 0), comment='其他非股票投资比例下限')
    OTHER_INVEST_PCT_UP = Column(Numeric(5, 0), comment='其他非股票投资比例上限')


class CMFQUARTERLYFINANCIALINDICATOR(Base):
    """中国共同基金季报财务指标"""
    __tablename__ = 'CMFQUARTERLYFINANCIALINDICATOR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(20), comment='Wind代码')
    F_UNIT_RPSTARTDATE = Column(VARCHAR(8), comment='报告期开始日期')
    F_UNIT_RPENDDATE = Column(VARCHAR(8), comment='报告期结束日期')
    TRADE_DT = Column(VARCHAR(8), comment='公告日期')
    F_ANAL_NETINCOME = Column(Numeric(20, 4), comment='本期利润扣减本期公允价值变动损益后的净额')
    F_FA_INVESTINCOMETOEBT = Column(Numeric(20, 4), comment='加权平均基金份额本期净收益')
    F_FINAFDASSETNAV = Column(Numeric(20, 4), comment='期末基金资产净值')
    F_FINAUNFDASSNAV = Column(Numeric(20, 4), comment='期末基金份额资产净值')
    F_NAV_RETURN = Column(Numeric(20, 4), comment='本期基金份额净值增长率')
    F_CUMULATIVE_NAV_RETURN = Column(Numeric(20, 4), comment='累计基金份额净值增长率')
    F_NAV_STDDEVRETURN = Column(Numeric(20, 4), comment='基金份额净值增长率标准差')
    F_NAV_BENCHRETURN = Column(Numeric(20, 4), comment='业绩比较基准收益率')
    F_NAV_BENCHSTDDEV = Column(Numeric(20, 4), comment='业绩比较基准收益率标准差')
    F_NAV_BENCHDEVRETURN = Column(Numeric(20, 4), comment='净值增长率减基准收益率')
    F_NAV_STDDEVNAVBENCH = Column(Numeric(20, 4), comment='净值增长率标准差减基准收益率标准差')
    F_ANAL_INCOME = Column(Numeric(20, 4), comment='本期利润')
    F_ANAL_AVGNETINCOMEPERUNIT = Column(Numeric(20, 4), comment='加权平均基金份额本期利润')


class CMFRATIOSUBSCRIBE(Base):
    """中国共同基金比例认购"""
    __tablename__ = 'CMFRATIOSUBSCRIBE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SUSENDDT = Column(VARCHAR(8), comment='发行(申购)截至日期')
    ANN_DT = Column(VARCHAR(8), comment='比例确认公告日期')
    EFFSUBSAPPAMOUNT = Column(Numeric(20, 4), comment='有效认购申请金额')
    EFFSUBSAMOUNT = Column(Numeric(20, 4), comment='有效认购金额')
    CONFIRM_RATIO = Column(Numeric(20, 4), comment='确认比例(%)')


class CMFRELATEDPARTIESHOLDER(Base):
    """基金关联方持有份额"""
    __tablename__ = 'CMFRELATEDPARTIESHOLDER'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    END_DATE = Column(VARCHAR(8), comment='截止日期')
    HOLDER_COMPCODE = Column(VARCHAR(10), comment='持有人公司ID')
    HOLDER_NAME = Column(VARCHAR(300), comment='持有人公布名称')
    HOLDER_TYPECODE = Column(Numeric(9, 0), comment='持有人类型代码')
    HOLD_AMOUNT = Column(Numeric(22, 6), comment='持有份额(万份)')
    HOLD_RATIO = Column(Numeric(20, 4), comment='持有比例(%)')


class CMFRISKLEVEL(Base):
    """中国共同基金初始风险等级"""
    __tablename__ = 'CMFRISKLEVEL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    RISK_LEVEL = Column(VARCHAR(40), comment='基金风险等级')


class CMFSECCLASS(Base):
    """中国共同基金证监会分类"""
    __tablename__ = 'CMFSECCLASS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_SECTOR = Column(VARCHAR(10), comment='所属板块代码')
    S_INFO_SECTORNAME = Column(VARCHAR(40), comment='所属板块名称')
    S_INFO_SECTORENTRYDT = Column(VARCHAR(8), comment='起始日期')
    S_INFO_SECTOREXITDT = Column(VARCHAR(8), comment='截止日期')
    CUR_SIGN = Column(Numeric(1, 0), comment='最新标志')


class CMFSELLINGAGENTS(Base):
    """中国共同基金代销机构"""
    __tablename__ = 'CMFSELLINGAGENTS'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='WIND代码')
    F_ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_AGENCY_NAMEID = Column(VARCHAR(20), comment='中介机构公司ID')
    F_AGENCY_NAME = Column(VARCHAR(200), comment='机构名称')
    F_RELATION = Column(VARCHAR(30), comment='关系类型')
    F_BEGIN_DATE = Column(VARCHAR(8), comment='起始日期')
    F_END_DATE = Column(VARCHAR(8), comment='终止日期')
    CUR_SIGN = Column(Numeric(5, 0), comment='最新标志')


class CMFSUBREDFEE(Base):
    """中国开放式基金费率表"""
    __tablename__ = 'CMFSUBREDFEE'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    FEETYPECODE = Column(VARCHAR(30), comment='费率类型')
    CHARGEWAY = Column(VARCHAR(20), comment='收费类型')
    AMOUNTDOWNLIMIT = Column(Numeric(20, 4), comment='金额下限(万元)')
    AMOUNTUPLIMIT = Column(Numeric(20, 4), comment='金额上限(万元)')
    HOLDINGPERIOD_DOWNLIMIT = Column(Numeric(20, 4), comment='持有年限下限')
    HOLDINGPERIOD_UPLIMIT = Column(Numeric(20, 4), comment='持有年限上限')
    FEERATIO = Column(Numeric(20, 4), comment='费率(%)')
    ISUPLIMITFEE = Column(VARCHAR(1), comment='是否上限费率')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    SUPPLEMENTARY = Column(VARCHAR(800), comment='费率补充说明')
    TRADINGPLACE = Column(VARCHAR(40), comment='场所')
    TRADINGPLACECODE = Column(Numeric(9, 0), comment='投资群体代码')
    HOLDINGPERIODUNIT = Column(VARCHAR(20), comment='持有期限单位')
    USED = Column(Numeric(1, 0), comment='是否有效')
    MEMO = Column(VARCHAR(4), comment='区间是否包含掩码')


class CMFTHEMECONCEPT(Base):
    """中国共同基金WIND概念板块主题分类"""
    __tablename__ = 'CMFTHEMECONCEPT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_SECTOR = Column(VARCHAR(16), comment='板块代码')
    S_INFO_NAME = Column(VARCHAR(100), comment='板块名称')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='成份万得代码')


class CMFTRADINGSUSPENSION(Base):
    """中国共同基金停复牌"""
    __tablename__ = 'CMFTRADINGSUSPENSION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券id')
    S_DQ_SUSPENDDATE = Column(VARCHAR(8), comment='停牌日期')
    S_DQ_SUSPENDTIME = Column(VARCHAR(200), comment='停复牌时间')
    S_DQ_SUSPENDTYPE = Column(Numeric(9, 0), comment='停牌类型代码')
    S_DQ_RESUMPDATE = Column(VARCHAR(8), comment='复牌日期')
    S_DQ_CHANGEREASON = Column(VARCHAR(400), comment='停牌原因')


class CMFUNDOPERATEPERIOD(Base):
    """中国共同基金滚动运作周期"""
    __tablename__ = 'CMFUNDOPERATEPERIOD'
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


class CMFUNDSPLIT(Base):
    """中国共同基金基金份额拆分与折算"""
    __tablename__ = 'CMFUNDSPLIT'
    __table_args__ = (
        Index('INDEX_S_INFO_WINDCODE', 'S_INFO_WINDCODE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_SPLITTYPE = Column(VARCHAR(40), comment='类型')
    F_INFO_SPLITANNDATE = Column(VARCHAR(8), comment='实施公告日期')
    F_INFO_SPLITANNOECDATE = Column(VARCHAR(8), comment='实施结果公告日期')
    F_INFO_SHARETRANSDATE = Column(VARCHAR(8), comment='拆分折算日')
    F_INFO_SHAREKINDATE = Column(VARCHAR(8), comment='基金份额变更登记日')
    F_INFO_SPLITINC = Column(Numeric(20, 10), comment='拆分折算比例')
    F_INFO_SPLIT_DT = Column(VARCHAR(8), comment='拆分折算场内除权日')
    CONCOSINC = Column(Numeric(20, 10), comment='折算成本基金的比例')
    CONRELINC = Column(Numeric(20, 10), comment='折算成关联基金的比例')
    REL_WINDCODE = Column(VARCHAR(40), comment='关联基金Wind代码')
    F_INFO_SPLITTYPECODE = Column(Numeric(9, 0), comment='折算类型代码')


class CMFUNDTHIRDPARTYINDPORTFOLIO(Base):
    """中国共同基金投资组合第三方行业配置"""
    __tablename__ = 'CMFUNDTHIRDPARTYINDPORTFOLIO'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(20), comment='Wind代码')
    CALCUL_DATE = Column(VARCHAR(8), comment='计算日期')
    PRT_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    IND_CODE = Column(VARCHAR(10), comment='行业代码')
    PRT_INDUSVALUE = Column(Numeric(20, 4), comment='持仓市值')
    PCT_NAV = Column(Numeric(20, 4), comment='持仓市值占基金资产净值比')
    CURRENCY_CODE = Column(VARCHAR(10), comment='货币代码')


class CMFUNDTHIRDPARTYRATING(Base):
    """中国共同基金第三方评级"""
    __tablename__ = 'CMFUNDTHIRDPARTYRATING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    RPTDATE = Column(VARCHAR(10), comment='日期（月份）')
    STARLEVEL = Column(Numeric(20, 4), comment='星级')
    F_INFO_TYPE = Column(VARCHAR(80), comment='基金类型')
    RATING_INTERVAL = Column(VARCHAR(40), comment='评级区间')
    RATING_GAGENCY = Column(VARCHAR(40), comment='评级机构')
    RATING_TYPE = Column(VARCHAR(80), comment='评级类型')


class CMFUNDWINDRATING(Base):
    """中国共同基金Wind基金评级"""
    __tablename__ = 'CMFUNDWINDRATING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    RPTDATE = Column(VARCHAR(8), comment='日期')
    STARLEVEL = Column(Numeric(20, 4), comment='星级')
    F_INFO_TYPE = Column(VARCHAR(80), comment='基金类型')
    RATING_INTERVAL = Column(VARCHAR(40), comment='评级区间')
    RATE_STYLE = Column(VARCHAR(80), comment='评级类型')


class CMMFPORTFOLIOPTM(Base):
    """中国货币式基金投资组合剩余期限(报告期)"""
    __tablename__ = 'CMMFPORTFOLIOPTM'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    F_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    REPORT_PERIOD = Column(VARCHAR(8), comment='报告期')
    F_PTM_TOP = Column(Numeric(20, 4), comment='剩余期下限')
    F_PTM_BOTTOM = Column(Numeric(20, 4), comment='剩余期上限')
    RATIO_ASSERT_NAV = Column(Numeric(20, 4), comment='资产占净值比例(%)')
    RATIO_LIAB_NAV = Column(Numeric(20, 4), comment='负债占净值比例(%)')
    TYPECODE = Column(VARCHAR(200), comment='类型')


class CMMQUARTERLYDATA(Base):
    """中国货币式基金重要指标(报告期)"""
    __tablename__ = 'CMMQUARTERLYDATA'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')
    F_INFO_BGNDATE = Column(VARCHAR(8), comment='报告期起始日期')
    F_INFO_ENDDATE = Column(VARCHAR(8), comment='报告期截止日期')
    FLOATING_BOND_AMOUNT = Column(Numeric(20, 4), comment='剩余存续期超过397天的浮动利率债券金额')
    FLOATING_BOND_AMOUNT_RATIO = Column(Numeric(20, 4), comment='剩余存续期超过397天的浮动利率债券占资产净值比例(%)')
    BONDREPO_BALANCE = Column(Numeric(20, 4), comment='报告期内债券回购融资余额')
    BONDREPO_BALANCE_RATIO = Column(Numeric(20, 4), comment='报告期内债券回购融资余额占资产净值的比例(%)')
    END_BONDREPO_BALANCE = Column(Numeric(20, 4), comment='报告期末债券回购融资余额')
    END_BONDREPO_BALANCE_RATIO = Column(Numeric(20, 4), comment='报告期末债券回购融资余额占资产净值的比例(%)')
    AVG_REMAINDER_PERIOD_MAX = Column(Numeric(20, 4), comment='报告期内投资组合平均剩余期限最高值')
    AVG_REMAINDER_PERIOD_MIN = Column(Numeric(20, 4), comment='报告期内投资组合平均剩余期限最低值')
    DEVIATION_DEGREE_FREQUENCY = Column(Numeric(20, 4), comment='报告期内偏离度的绝对值在0.25％(含)－0.5％间的次数')
    DEVIATION_DEGREE_MAX = Column(Numeric(20, 4), comment='报告期内偏离度的最高值(%)')
    DEVIATION_DEGREE_MIN = Column(Numeric(20, 4), comment='报告期内偏离度的最低值(%)')
    DEVIATION_DEGREE_AVG_VALUE = Column(Numeric(20, 4), comment='报告期内每个工作日偏离度的绝对值的简单平均值(%)')
    FIXED_DEPOSIT = Column(Numeric(20, 4), comment='商业银行定期存款')


class CMONEYMARKETDAILYFINCOME(Base):
    """中国货币式基金日收益(拆分)"""
    __tablename__ = 'CMONEYMARKETDAILYFINCOME'
    __table_args__ = (
        Index('IDX_CMONEYMARKETDAILYFINCOME_CODE_DATE', 'S_INFO_WINDCODE', 'F_INFO_ENDDATE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_BGNDATE = Column(VARCHAR(8), comment='起始日期')
    F_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    F_INFO_UNITYIELD = Column(Numeric(20, 4), comment='单位净值')
    F_ACCUNITNAV = Column(Numeric(20, 4), comment='累计单位净值')
    F_INCOME_PER_MILLION = Column(Numeric(20, 5), comment='万份收益')
    F_INFO_YEARLYROE = Column(Numeric(20, 4), comment='七日年化收益率')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class CMONEYMARKETFINCOME(Base):
    """中国货币式基金日收益"""
    __tablename__ = 'CMONEYMARKETFINCOME'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    F_INFO_BGNDATE = Column(VARCHAR(8), comment='起始日期')
    F_INFO_ENDDATE = Column(VARCHAR(8), comment='截止日期')
    F_INFO_UNITYIELD = Column(Numeric(20, 5), comment='每万份基金单位收益')
    F_INFO_YEARLYROE = Column(Numeric(20, 4), comment='最近七日收益所折算的年资产收益率')
    ANN_DATE = Column(VARCHAR(8), comment='公告日期')


class CMONEYMARKETFSCARRYOVERM(Base):
    """中国货币市场基金份额结转方式"""
    __tablename__ = 'CMONEYMARKETFSCARRYOVERM'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    F_INFO_INCOMESCARRYOVERM = Column(VARCHAR(20), comment='收益分配份额结转方式')
    F_INFO_INCOMESCARRYOVERDTCODE = Column(Numeric(9, 0), comment='收益分配份额结转日期类型代码')
    F_IS_NEW = Column(Numeric(1, 0), comment='是否最新')


class CMONEYMARKETFSCARRYOVERMZL(Base):
    """中国货币市场基金份额结转方式(增量)"""
    __tablename__ = 'CMONEYMARKETFSCARRYOVERMZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    F_INFO_INCOMESCARRYOVERM = Column(VARCHAR(20), comment='收益分配份额结转方式')
    F_INFO_INCOMESCARRYOVERDTCODE = Column(Numeric(9, 0), comment='收益分配份额结转日期类型代码')
    F_IS_NEW = Column(Numeric(1, 0), comment='是否最新')


class COMPANYAWARD(Base):
    """中国共同基金机构奖项排名"""
    __tablename__ = 'COMPANYAWARD'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_CHINESEINTRODUCTION = Column(VARCHAR(40), comment='机构简称')
    S_INFO_COMPCODE = Column(VARCHAR(10), comment='机构公司ID')
    S_INFO_AWARD_CODE = Column(Numeric(9, 0), comment='奖项代码')
    S_INFO_YEAR = Column(VARCHAR(8), comment='年度')
    S_INFO_RANKING = Column(Numeric(5, 0), comment='排名')


class ETFPCHREDM(Base):
    """中国ETF申购赎回"""
    __tablename__ = 'ETFPCHREDM'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    S_INFO_EXCHMARKET = Column(VARCHAR(20), comment='交易所')
    ONLINE_OFFERING_CODE = Column(VARCHAR(10), comment='网上现金发售代码')
    NETWORKCASHBUYSTARTDT = Column(VARCHAR(8), comment='网上现金认购起始日')
    NETWORKCASHBUYENDDT = Column(VARCHAR(8), comment='网上现金认购截止日')
    NETWORKCASHBUYDOWNLIMIT = Column(Numeric(20, 4), comment='网上现金认购份额下限(份)')
    NETWORKCASHBUYUPLIMIT = Column(Numeric(20, 4), comment='网上现金认购份额上限(份)')
    OFFNETWORKBUYSTARTDT = Column(VARCHAR(8), comment='网下现金认购起始日')
    OFFNETWORKBUYENDDT = Column(VARCHAR(8), comment='网下现金认购截止日')
    OFFNETWORKCASHBUYDOWNLIMIT = Column(Numeric(20, 4), comment='网下现金认购份额下限(份)')
    PCH_START_DT = Column(VARCHAR(8), comment='申购起始日')
    REDM_START_DT = Column(VARCHAR(8), comment='赎回起始日')
    PCH_CODE = Column(VARCHAR(10), comment='申购赎回代码')
    PCH_NAME = Column(VARCHAR(40), comment='申购赎回简称')
    LIST_DT = Column(VARCHAR(8), comment='上市日期')
    LIST_SHARE = Column(Numeric(20, 4), comment='上市交易份额')
    CONVERSION_DT = Column(VARCHAR(8), comment='份额折算日')
    CONVERSION_RATIO = Column(Numeric(20, 8), comment='份额折算比例')


class LOFDESCRIPTION(Base):
    """中国LOF基金基本资料"""
    __tablename__ = 'LOFDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='wind代码')
    S_INFO_LISTBOARDNAME = Column(VARCHAR(10), comment='上市板')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    S_INFO_OUTSTANDINGBALANCE = Column(Numeric(20, 4), comment='上市交易份额')


class LOFPCHREDM(Base):
    """中国开放式基金场内申购赎回"""
    __tablename__ = 'LOFPCHREDM'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='基金Wind代码')
    S_INFO_EXCHMARKET = Column(VARCHAR(20), comment='交易所')
    SUBSTRIPTION_CODE = Column(VARCHAR(20), comment='场内认购基金代码')
    SUBSTRIPTION_NAME = Column(VARCHAR(40), comment='场内认购基金简称')
    SUBSTRIPTION_PRICE = Column(Numeric(20, 4), comment='场内认购价格')
    SUBSTRIPTION_START_DT = Column(VARCHAR(8), comment='场内认购起始日')
    SUBSTRIPTION_END_DT = Column(VARCHAR(8), comment='场内认购截止日')
    PCH_CODE = Column(VARCHAR(20), comment='场内申购赎回基金代码')
    PCH_NAME = Column(VARCHAR(40), comment='场内申购赎回基金简称')
    PCH_START_DT = Column(VARCHAR(8), comment='场内申购起始日')
    REDM_START_DT = Column(VARCHAR(8), comment='场内赎回起始日')
