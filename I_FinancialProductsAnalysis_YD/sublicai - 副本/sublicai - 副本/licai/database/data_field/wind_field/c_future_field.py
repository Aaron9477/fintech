# -*- coding: utf-8 -*-
# ------------------------------
# @Time    : 2021/10/21 10:54
# @Author  : lisl3
# @File    : c_future_field.py
# @Project : cscfist
# @Function: 中国期货
# @Version : V0.0.1
# ------------------------------
from sqlalchemy import Column, VARCHAR, Numeric, TEXT, Index
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CFUTUREINDEXDESCRIPTION(Base):
    """中国期货指数基本资料"""
    __tablename__ = 'CFUTUREINDEXDESCRIPTION'
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


class CFUTUREINDEXEODPRICES(Base):
    """中国期货指数日行情"""
    __tablename__ = 'CFUTUREINDEXEODPRICES'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    CRNCY_CODE = Column(VARCHAR(10), comment='交易货币代码')
    S_DQ_PRECLOSE = Column(Numeric(20, 4), comment='昨收盘价')
    S_DQ_OPEN = Column(Numeric(20, 4), comment='开盘价')
    S_DQ_HIGH = Column(Numeric(20, 4), comment='最高价')
    S_DQ_LOW = Column(Numeric(20, 4), comment='最低价')
    S_DQ_CLOSE = Column(Numeric(20, 4), comment='最新价')
    S_DQ_CHANGE = Column(Numeric(20, 4), comment='涨跌(点)')
    S_DQ_PCTCHANGE = Column(Numeric(20, 4), comment='涨跌幅(%)')
    S_DQ_VOLUME = Column(Numeric(20, 4), comment='成交量(手)')
    S_DQ_AMOUNT = Column(Numeric(20, 4), comment='成交金额(千元)')
    S_DQ_OI = Column(Numeric(20, 8), comment='持仓量')


class CFUTURESARBITRAGECONTRACT(Base):
    """中国期货套利合约关系表"""
    __tablename__ = 'CFUTURESARBITRAGECONTRACT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_RALATEDCODE = Column(VARCHAR(40), comment='关联证券Wind代码')
    S_RELATION_TYPCODE = Column(Numeric(9, 0), comment='关系类型代码')
    S_INFO_EFFECTIVE_DT = Column(VARCHAR(8), comment='生效日期')
    S_INFO_INVALID_DT = Column(VARCHAR(8), comment='失效日期')


class CFUTURESCALENDAR(Base):
    """中国期货交易日历"""
    __tablename__ = 'CFUTURESCALENDAR'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DAYS = Column(VARCHAR(8), comment='日期')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class CFUTURESCALENDARZL(Base):
    """中国期货交易日历(增量)"""
    __tablename__ = 'CFUTURESCALENDARZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    TRADE_DAYS = Column(VARCHAR(8), comment='日期')
    S_INFO_EXCHMARKET = Column(VARCHAR(40), comment='交易所英文简称')


class CFUTURESCHANGEWINDCODE(Base):
    """中国期货Wind代码变更表"""
    __tablename__ = 'CFUTURESCHANGEWINDCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_OLDWINDCODE = Column(VARCHAR(40), comment='变更前代码')
    S_INFO_NEWWINDCODE = Column(VARCHAR(40), comment='变更后代码')
    CHANGE_DATE = Column(VARCHAR(10), comment='代码变更日期')


class CFUTURESCONTPRO(Base):
    """中国期货标准合约属性"""
    __tablename__ = 'CFUTURESCONTPRO'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(20), comment='标准合约代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='标准合约名称')
    S_INFO_TUNIT = Column(VARCHAR(40), comment='交易计量单位')
    S_INFO_PUNIT = Column(Numeric(20, 4), comment='交易单位(每手)')
    S_INFO_MFPRICE = Column(VARCHAR(200), comment='最小变动价位')
    S_INFO_FTMARGINS = Column(VARCHAR(800), comment='最低交易保证金')
    S_INFO_CDMONTHS = Column(VARCHAR(200), comment='合约月份说明')
    S_INFO_THOURS = Column(VARCHAR(800), comment='交易时间说明')
    S_INFO_LTDATED = Column(VARCHAR(200), comment='最后交易日说明')
    S_INFO_DDATE = Column(VARCHAR(400), comment='交割日期说明')
    S_INFO_CEMULTIPLIER = Column(Numeric(20, 4), comment='合约乘数')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='合约上市日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    S_INFO_EXNAME = Column(VARCHAR(20), comment='交易所简称')
    S_INFO_DMEAN = Column(VARCHAR(400), comment='交割方式说明')
    S_INFO_DSITE = Column(VARCHAR(400), comment='交割地点说明')
    S_INFO_LTDATEHOUR = Column(VARCHAR(400), comment='最后交易日交易时间说明')
    S_INFO_CEVALUE = Column(VARCHAR(400), comment='合约价值说明')
    S_INFO_MAXPRICEFLUCT = Column(VARCHAR(800), comment='最大价格波动说明')
    S_INFO_POSLIMIT = Column(VARCHAR(800), comment='头寸限制说明')
    S_INFO_UDLSECODE = Column(VARCHAR(20), comment='标的证券代码')
    FS_INFO_PUNIT = Column(VARCHAR(200), comment='报价单位')
    S_INFO_RTD = Column(Numeric(20, 4), comment='均价计算使用值')
    S_SUB_TYPCODE = Column(Numeric(9, 0), comment='品种细类代码')
    CONTRACT_ID = Column(VARCHAR(10), comment='合约ID')


class CFUTURESCONTPROCHANGE(Base):
    """中国期货标准合约属性变更"""
    __tablename__ = 'CFUTURESCONTPROCHANGE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    CONTRACT_ID = Column(VARCHAR(38), comment='合约ID')
    ITEM = Column(VARCHAR(50), comment='变更字段名称')
    CHANGE_DT = Column(VARCHAR(8), comment='变更日期')
    S_INFO_OLD = Column(VARCHAR(1000), comment='变更前')
    S_INFO_NEW = Column(VARCHAR(1000), comment='变更后')


class CFUTURESCONTPROZL(Base):
    """中国期货标准合约属性(增量)"""
    __tablename__ = 'CFUTURESCONTPROZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(20), comment='标准合约代码')
    S_INFO_NAME = Column(VARCHAR(40), comment='标准合约名称')
    S_INFO_TUNIT = Column(VARCHAR(40), comment='交易计量单位')
    S_INFO_PUNIT = Column(Numeric(20, 4), comment='交易单位(每手)')
    S_INFO_MFPRICE = Column(VARCHAR(200), comment='最小变动价位')
    S_INFO_FTMARGINS = Column(VARCHAR(800), comment='最低交易保证金')
    S_INFO_CDMONTHS = Column(VARCHAR(200), comment='合约月份说明')
    S_INFO_THOURS = Column(VARCHAR(800), comment='交易时间说明')
    S_INFO_LTDATED = Column(VARCHAR(200), comment='最后交易日说明')
    S_INFO_DDATE = Column(VARCHAR(400), comment='交割日期说明')
    S_INFO_CEMULTIPLIER = Column(Numeric(20, 4), comment='合约乘数')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='合约上市日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='退市日期')
    S_INFO_EXNAME = Column(VARCHAR(20), comment='交易所简称')
    S_INFO_DMEAN = Column(VARCHAR(400), comment='交割方式说明')
    S_INFO_DSITE = Column(VARCHAR(400), comment='交割地点说明')
    S_INFO_LTDATEHOUR = Column(VARCHAR(400), comment='最后交易日交易时间说明')
    S_INFO_CEVALUE = Column(VARCHAR(400), comment='合约价值说明')
    S_INFO_MAXPRICEFLUCT = Column(VARCHAR(800), comment='最大价格波动说明')
    S_INFO_POSLIMIT = Column(VARCHAR(800), comment='头寸限制说明')
    S_INFO_UDLSECODE = Column(VARCHAR(20), comment='标的证券代码')
    FS_INFO_PUNIT = Column(VARCHAR(200), comment='报价单位')
    S_INFO_RTD = Column(Numeric(20, 4), comment='均价计算使用值')
    S_SUB_TYPCODE = Column(Numeric(9, 0), comment='品种细类代码')
    CONTRACT_ID = Column(VARCHAR(10), comment='合约ID')


class CFUTURESCONTRACTMAPPING(Base):
    """中国期货连续(主力)合约和月合约映射表"""
    __tablename__ = 'CFUTURESCONTRACTMAPPING'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='连续(主力)合约Wind代码')
    FS_MAPPING_WINDCODE = Column(VARCHAR(20), comment='映射月合约Wind代码')
    STARTDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    CONTRACT_ID = Column(VARCHAR(10), comment='合约ID')


class CFUTURESCONTRACTMAPPINGQL(Base):
    """None"""
    __tablename__ = 'CFUTURESCONTRACTMAPPINGQL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True)
    S_INFO_WINDCODE = Column(VARCHAR(40))
    FS_MAPPING_WINDCODE = Column(VARCHAR(20))
    STARTDATE = Column(VARCHAR(8))
    ENDDATE = Column(VARCHAR(8))
    CONTRACT_ID = Column(VARCHAR(10))


class CFUTURESCONTRACTMAPPINGZL(Base):
    """中国期货连续(主力)合约和月合约映射表(增量)"""
    __tablename__ = 'CFUTURESCONTRACTMAPPINGZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='连续(主力)合约Wind代码')
    FS_MAPPING_WINDCODE = Column(VARCHAR(20), comment='映射月合约Wind代码')
    STARTDATE = Column(VARCHAR(8), comment='起始日期')
    ENDDATE = Column(VARCHAR(8), comment='截止日期')
    CONTRACT_ID = Column(VARCHAR(10), comment='合约ID')


class CFUTURESDECLARATIONOFDI(Base):
    """中国期货交割意向申报"""
    __tablename__ = 'CFUTURESDECLARATIONOFDI'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    FS_INFO_MEMBERCODE = Column(VARCHAR(10), comment='会员公司ID')
    DE_SHORT_DELIVERY_VOLUME = Column(Numeric(20, 4), comment='申报卖方交割量')
    DE_LONG_DELIVERY_VOLUME = Column(Numeric(20, 4), comment='申报买方交割量')
    SETTLEMENT_MEM_NUMBER = Column(VARCHAR(20), comment='结算会员号')


class CFUTURESDELIVERY(Base):
    """中国期货交割数据"""
    __tablename__ = 'CFUTURESDELIVERY'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    DELIVERY_VOLUME = Column(Numeric(20, 4), comment='交割量')
    DELIVERY_AMOUNT = Column(Numeric(20, 4), comment='交割金额')
    DELIVERY_TYPE = Column(Numeric(1, 0), comment='交割类型')
    DELIVERABLE = Column(VARCHAR(10), comment='可交割ID')


class CFUTURESDELIVERYFEE(Base):
    """中国期货交易交割手续费"""
    __tablename__ = 'CFUTURESDELIVERYFEE'
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DATE = Column(VARCHAR(8), comment='日期')
    TRANSACTION_FEE = Column(Numeric(20, 8), comment='交易手续费额')
    TRANSACTION_FEE_RATE = Column(Numeric(20, 8), comment='交易手续费率')
    DELIVERY_FEE = Column(Numeric(20, 8), comment='交割手续费')
    DELIVERY_FEE_RATE = Column(Numeric(20, 8), comment='交割手续费率')
    COMSON_CHARGE_CP = Column(Numeric(20, 8), comment='平今仓手续费')
    DISCOUNT_RATE_CP = Column(Numeric(20, 8), comment='平今折扣率')
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')


class CFUTURESDELIVERYWHINFO(Base):
    """中国期货交割仓库基本资料"""
    __tablename__ = 'CFUTURESDELIVERYWHINFO'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_EXNAME = Column(VARCHAR(20), comment='交易所简称')
    CNTRY_CODE = Column(VARCHAR(10), comment='国家或地区代码')
    S_INFO_SCCODE = Column(VARCHAR(50), comment='标准合约代码')
    DESIGN_DELVY_WRHS = Column(VARCHAR(200), comment='指定交割仓库名称')
    OFFICE_ADDRESS = Column(VARCHAR(400), comment='办公地址')
    DEPOSIT_ADDRESS = Column(VARCHAR(400), comment='存放地址')
    CONTACT_INFO = Column(VARCHAR(1000), comment='联系方式')
    WAREHOUSE_NUMB = Column(VARCHAR(80), comment='仓库编号')
    DELIVERY_WRHS_TYPE = Column(VARCHAR(20), comment='交割仓库类别')
    BUSSINESS_ADDRESS = Column(VARCHAR(200), comment='办公地址')
    POSTCODE = Column(VARCHAR(6), comment='邮编')
    LOADING_STATION = Column(VARCHAR(200), comment='装运站/港')
    AGRMT_STORAGE = Column(Numeric(20, 4), comment='协议库容')
    DELIVERY_ZONE = Column(VARCHAR(200), comment='交割专区')
    IS_BEN_WRHS = Column(Numeric(1, 0), comment='是否基准库')
    UPGRADE_DISCOUNT = Column(VARCHAR(200), comment='与基准库升贴水')
    MAXIMUN_STAND_WRHS = Column(Numeric(20, 4), comment='标准仓单最大量')
    DAILY_DELIVERY_SPEED = Column(Numeric(20, 4), comment='日发货速度')
    PRODUCT_SPECIFICATIONS = Column(VARCHAR(200), comment='产品规格')
    IS_NORMAL_BUSINESS = Column(Numeric(1, 0), comment='是否正常营业')


class CFUTURESDESCRIPTION(Base):
    """中国期货基本资料"""
    __tablename__ = 'CFUTURESDESCRIPTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券中文简称')
    S_INFO_ENAME = Column(VARCHAR(100), comment='证券英文简称')
    FS_INFO_SCCODE = Column(VARCHAR(50), comment='标准合约代码')
    FS_INFO_TYPE = Column(Numeric(1, 0), comment='合约类型')
    FS_INFO_CCTYPE = Column(Numeric(9, 0), comment='连续合约类型')
    S_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='最后交易日期')
    FS_INFO_DLMONTH = Column(VARCHAR(8), comment='交割月份')
    FS_INFO_LPRICE = Column(Numeric(20, 4), comment='挂牌基准价')
    FS_INFO_LTDLDATE = Column(VARCHAR(8), comment='最后交割日')
    S_INFO_FULLNAME = Column(VARCHAR(40), comment='证券中文名称')
    S_INFO_VOUCHERDATE = Column(VARCHAR(8), comment='交券日')
    S_INFO_PAYMENTDATE = Column(VARCHAR(8), comment='缴款日')


class CFUTURESDESCRIPTIONZL(Base):
    """中国期货基本资料(增量)"""
    __tablename__ = 'CFUTURESDESCRIPTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(40), comment='交易代码')
    S_INFO_NAME = Column(VARCHAR(50), comment='证券中文简称')
    S_INFO_ENAME = Column(VARCHAR(100), comment='证券英文简称')
    FS_INFO_SCCODE = Column(VARCHAR(50), comment='标准合约代码')
    FS_INFO_TYPE = Column(Numeric(1, 0), comment='合约类型')
    FS_INFO_CCTYPE = Column(Numeric(9, 0), comment='连续合约类型')
    S_INFO_EXCHMARKET = Column(VARCHAR(10), comment='交易所')
    S_INFO_LISTDATE = Column(VARCHAR(8), comment='上市日期')
    S_INFO_DELISTDATE = Column(VARCHAR(8), comment='最后交易日期')
    FS_INFO_DLMONTH = Column(VARCHAR(8), comment='交割月份')
    FS_INFO_LPRICE = Column(Numeric(20, 4), comment='挂牌基准价')
    FS_INFO_LTDLDATE = Column(VARCHAR(8), comment='最后交割日')
    S_INFO_FULLNAME = Column(VARCHAR(40), comment='证券中文名称')


class CFUTURESHEDGINGPOSITIONS(Base):
    """中国期货套保持仓"""
    __tablename__ = 'CFUTURESHEDGINGPOSITIONS'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    FS_INFO_SCCODE = Column(VARCHAR(10), comment='标准合约代码')
    FS_INFO_DATE = Column(VARCHAR(8), comment='日期')
    BUY_HEDGING_QUOTA = Column(Numeric(20, 4), comment='买套保额度(元)')
    BUY_HEDGING_HOLD_AMOUNT = Column(Numeric(20, 4), comment='期货买套保持仓量(手)')
    SELL_HEDGING_QUOTA = Column(Numeric(20, 4), comment='卖套保额度(元)')
    SELL_HEDGING_HOLD_AMOUNT = Column(Numeric(20, 4), comment='期货卖套保持仓量(手)')


class CFUTURESINDUSTRIESCODE(Base):
    """中国期货行业代码"""
    __tablename__ = 'CFUTURESINDUSTRIESCODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    INDUSTRIESCODE = Column(VARCHAR(38), comment='板块代码')
    INDUSTRIESNAME = Column(VARCHAR(50), comment='板块名称')
    LEVELNUM = Column(Numeric(1, 0), comment='级数')
    USED = Column(Numeric(1, 0), comment='是否使用')
    INDUSTRIESALIAS = Column(VARCHAR(12), comment='板块别名')
    SEQUENCE1 = Column(Numeric(4, 0), comment='展示序号')
    MEMO = Column(VARCHAR(100), comment='[内部]备注')
    CHINESEDEFINITION = Column(VARCHAR(600), comment='板块中文定义')


class CFUTURESINSTOCK(Base):
    """中国期货库存(仓单)"""
    __tablename__ = 'CFUTURESINSTOCK'
    __table_args__ = (
        Index('IDX_CFUTURESINSTOCK_ANN_DATE', 'ANN_DATE'),)
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    FS_INFO_SCNAME = Column(VARCHAR(40), comment='标准合约名称')
    ANN_DATE = Column(VARCHAR(8), comment='日期')
    IN_STOCK_TOTAL = Column(Numeric(20, 4), comment='库存合计')
    IN_STOCK = Column(Numeric(20, 4), comment='库存（注册成仓单）')
    AVAILABLE_IN_STOCK = Column(Numeric(20, 4), comment='可用库容量')
    UNIT = Column(VARCHAR(40), comment='单位')


class CFUTURESINTRODUCTION(Base):
    """中国期货公司简介"""
    __tablename__ = 'CFUTURESINTRODUCTION'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_PROVINCE = Column(VARCHAR(20), comment='省份')
    S_INFO_CITY = Column(VARCHAR(50), comment='城市')
    S_INFO_CHAIRMAN = Column(VARCHAR(38), comment='法人代表')
    S_INFO_PRESIDENT = Column(VARCHAR(38), comment='总经理')
    S_INFO_BDSECRETARY = Column(VARCHAR(500), comment='信息披露人ID')
    S_INFO_REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    S_INFO_FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    S_INFO_CHINESEINTRODUCTION = Column(VARCHAR(2000), comment='公司简介')
    S_INFO_COMPTYPE = Column(VARCHAR(20), comment='公司类型')
    S_INFO_WEBSITE = Column(VARCHAR(80), comment='主页')
    S_INFO_EMAIL = Column(VARCHAR(80), comment='电子邮箱')
    S_INFO_OFFICE = Column(VARCHAR(80), comment='办公地址')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_COUNTRY = Column(VARCHAR(20), comment='国家及地区')
    S_INFO_BUSINESSSCOPE = Column(VARCHAR(2000), comment='经营范围')
    S_INFO_COMPANY_TYPE = Column(VARCHAR(10), comment='[内部]公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    COMP_NAME = Column(VARCHAR(100), comment='公司名称')


class CFUTURESINTRODUCTIONZL(Base):
    """中国期货公司简介增量"""
    __tablename__ = 'CFUTURESINTRODUCTIONZL'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_COMPCODE = Column(VARCHAR(40), comment='公司ID')
    S_INFO_PROVINCE = Column(VARCHAR(20), comment='省份')
    S_INFO_CITY = Column(VARCHAR(50), comment='城市')
    S_INFO_CHAIRMAN = Column(VARCHAR(38), comment='法人代表')
    S_INFO_PRESIDENT = Column(VARCHAR(38), comment='总经理')
    S_INFO_BDSECRETARY = Column(VARCHAR(500), comment='信息披露人ID')
    S_INFO_REGCAPITAL = Column(Numeric(20, 4), comment='注册资本(万元)')
    S_INFO_FOUNDDATE = Column(VARCHAR(8), comment='成立日期')
    S_INFO_CHINESEINTRODUCTION = Column(VARCHAR(2000), comment='公司简介')
    S_INFO_COMPTYPE = Column(VARCHAR(20), comment='公司类型')
    S_INFO_WEBSITE = Column(VARCHAR(160), comment='主页')
    S_INFO_EMAIL = Column(VARCHAR(160), comment='电子邮箱')
    S_INFO_OFFICE = Column(VARCHAR(80), comment='办公地址')
    ANN_DT = Column(VARCHAR(8), comment='公告日期')
    S_INFO_COUNTRY = Column(VARCHAR(20), comment='国家及地区')
    S_INFO_BUSINESSSCOPE = Column(VARCHAR(2000), comment='经营范围')
    S_INFO_COMPANY_TYPE = Column(VARCHAR(10), comment='[内部]公司类别')
    S_INFO_TOTALEMPLOYEES = Column(Numeric(20, 0), comment='员工总数(人)')
    S_INFO_MAIN_BUSINESS = Column(VARCHAR(1000), comment='主要产品及业务')
    COMP_NAME = Column(VARCHAR(200), comment='公司名称')


class CFUTURESMARGINRATIO(Base):
    """中国期货保证金比例"""
    __tablename__ = 'CFUTURESMARGINRATIO'
    __table_args__ = (
        Index('IDX_CFUTURESMARGINRATIO_TRADE_DT', 'TRADE_DT'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='合约Wind代码')
    MARGINRATIO = Column(VARCHAR(40), comment='保证金比例')
    TRADE_DT = Column(VARCHAR(8), comment='变动日期')


class CFUTURESPOSITIONLIMIT(Base):
    """中国期货月合约持仓限制"""
    __tablename__ = 'CFUTURESPOSITIONLIMIT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='月合约Wind代码')
    POSITION_LIMIT_TYPE = Column(Numeric(9, 0), comment='限仓对象类型代码')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')
    POSITION_LIMIT = Column(Numeric(20, 0), comment='持仓限定数量')
    POSITION_LIMIT_RATIO = Column(Numeric(20, 4), comment='持仓限定比例')
    CHANGE_REASON = Column(VARCHAR(100), comment='变动原因')


class CFUTURESPRICECHANGELIMIT(Base):
    """中国期货标准合约价格波动限制变更"""
    __tablename__ = 'CFUTURESPRICECHANGELIMIT'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    SEC_ID = Column(VARCHAR(40), comment='证券ID')
    PCT_CHG_LIMIT = Column(Numeric(20, 4), comment='涨跌停板幅度(%)')
    CHANGE_DT = Column(VARCHAR(8), comment='变动日期')


class CFUTURESTYPECODE(Base):
    """中国期货类型编码表"""
    __tablename__ = 'CFUTURESTYPECODE'
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_TYPNAME = Column(VARCHAR(300), comment='类型名称')
    S_TYPCODE = Column(VARCHAR(40), comment='类型代码')
    S_ORIGIN_TYPCODE = Column(Numeric(9, 0), comment='类型代码')
    S_CLASSIFICATION = Column(VARCHAR(100), comment='分类')


class CFUTURESUNILATERALMAKT(Base):
    """中国期货交易所单边市状态"""
    __tablename__ = 'CFUTURESUNILATERALMAKT'
    OBJECT_ID = Column(VARCHAR(38), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    TRADE_DT = Column(VARCHAR(8), comment='日期')
    S_INFO_EXCHMARKETNAME = Column(VARCHAR(100), comment='交易所名称')
    UNILATERAL_STATUS = Column(VARCHAR(1), comment='单边市状态')
    CON_UNILATERAL_STATUS = Column(Numeric(5, 0), comment='连续单边市天数')
    HARDEN_STOP = Column(Numeric(20, 4), comment='涨停价格')
    SUDDEN_STOP = Column(Numeric(20, 4), comment='跌停价格')


class CFUTURESWAREHOUSESTOCKS(Base):
    """中国期货库存报告"""
    __tablename__ = 'CFUTURESWAREHOUSESTOCKS'
    __table_args__ = (
        Index('IDX_CFUTURESWAREHOUSESTOCKS_ANN_DATE', 'ANN_DATE'),)
    OBJECT_ID = Column(VARCHAR(100), primary_key=True, comment='对象ID')
    S_INFO_WINDCODE = Column(VARCHAR(40), comment='Wind代码')
    S_INFO_CODE = Column(VARCHAR(20), comment='标准合约代码')
    ANN_DATE = Column(VARCHAR(8), comment='日期')
    WAREHOUSE_REGION = Column(VARCHAR(40), comment='地区')
    WAREHOUSE_NAME = Column(VARCHAR(100), comment='仓库简称')
    DELIVERABLE_W = Column(Numeric(20, 4), comment='本周库存合计')
    ON_WARRANT_W = Column(Numeric(20, 4), comment='本周库存（注册成仓单）')
    AVAILABLE_WAREHOUSE_W = Column(Numeric(20, 4), comment='本周可用库容量')
    QUANTITY_UNIT = Column(VARCHAR(40), comment='单位')
    WAREHOUSE_IN = Column(Numeric(20, 4), comment='入仓')
    WAREHOUSE_OUT = Column(Numeric(20, 4), comment='出仓')
    CANCELLED_WARRANTS = Column(Numeric(20, 4), comment='注销仓单量')
    EFFECTIVE_FORECAST = Column(Numeric(20, 4), comment='有效预报')


class CFUTURESWINDCUSTOMCODE(Base):
    """中国期货Wind兼容代码"""
    __tablename__ = 'CFUTURESWINDCUSTOMCODE'
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
