# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/9/14 11:09 
# @Author    : Wangyd5 
# @File      : jy_filed
# @Project   : sublicai
# @Function  ：
# --------------------------------

from sqlalchemy import Column, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import VARCHAR, Numeric

Base = declarative_base()

class FpSecuMain(Base):
    __tablename__ = 'FP_SecuMain'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    EnterpriseCode = Column(VARCHAR(12), comment='企业编码')
    CompanyCode = Column(Numeric(10), comment='公司代码')
    SecuCode = Column(VARCHAR(50), comment='证券代码')
    ChiName = Column(VARCHAR(200), comment='中文名称')
    SecuAbbr = Column(VARCHAR(100), comment='证券简称')
    ChiSpelling = Column(VARCHAR(50), comment='拼音缩写')
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    SecuState = Column(VARCHAR(12), comment='证券状态')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('EnterpriseCode', "FinProCode", "SecuCode"),)


class FpBasicInfo(Base):
    """
    金融产品概况
    """
    __tablename__ = 'FP_BasicInfo'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    RiskLevelCode = Column(VARCHAR(12), comment='风险评级')
    RegistrationCode = Column(VARCHAR(50), comment='登记编码')
    IncomeType = Column(VARCHAR(12), comment='收益类型')
    ParValue = Column(Numeric(10), comment='产品面值')
    CurrencyUnit = Column(VARCHAR(12), comment='货币单位')
    RaisingType = Column(VARCHAR(12), comment='募集方式')
    IssueObject = Column(VARCHAR(200), comment='发行对象')
    IssueRegion = Column(VARCHAR(500), comment='发行地区')
    PurchaseChannels = Column(VARCHAR(200), comment='购买渠道')
    PopularizeStDate = Column(VARCHAR(30), comment='销售起始日')
    PopularizeEdDate = Column(VARCHAR(30), comment='销售截止日')
    EstablishmentDate = Column(VARCHAR(30), comment='产品成立日')
    MaturityDate = Column(VARCHAR(30), comment='产品到期日')
    ActMaturityDate = Column(VARCHAR(30), comment='实际到期日')
    MinInvestTerm = Column(Numeric(10, 2), comment='最短持有期限')
    MinInvestTermUnit = Column(VARCHAR(12), comment='最短持有期限单位')
    InvestTerm = Column(Numeric(19, 8), comment='投资期限')
    InvestTermUnit = Column(VARCHAR(12), comment='投资期限单位')
    LeastBuySum = Column(Numeric(19, 6), comment='最低认购金额(万元)')
    IncreasingAmountPER = Column(Numeric(19, 6), comment='递增金额(万元)')
    MaximumApplying = Column(Numeric(19, 6), comment='申购上限(万元)')
    IssueVolCeiling = Column(Numeric(21, 8), comment='发行规模上限(亿元)')
    IssueVolFloor = Column(Numeric(21, 8), comment='发行规模下限(亿元)')
    ActRaisingAmount = Column(Numeric(19, 10), comment='实际募资金额(亿元)')
    PublishDesc = Column(VARCHAR(1000), comment='募集说明')
    IfCancel = Column(VARCHAR(12), comment='是否允许撤单')
    CancelRegulation = Column(VARCHAR(1000), comment='撤单规则')
    ExpAnEnYield = Column(Numeric(19, 6), comment='预期收益率上限(%)')
    ExpAnBeYield = Column(Numeric(19, 6), comment='预期收益率下限(%)')
    BenchmarkMax = Column(Numeric(19, 6), comment='业绩比较基准上限(%)')
    BenchmarkMin = Column(Numeric(19, 6), comment='业绩比较基准下限(%)')
    AnnualDays = Column(Numeric(10), comment='年化天数')
    DeliveryDays = Column(VARCHAR(100), comment='资金到账日')
    InvestAdvisorCode = Column(VARCHAR(12), comment='管理人')
    TrusteeCode = Column(VARCHAR(12), comment='托管人')
    OperationType = Column(VARCHAR(12), comment='运作方式')
    IfDiscloseDP = Column(VARCHAR(12), comment='是否披露每万份收益')
    InvestmentType = Column(VARCHAR(12), comment='投资性质')
    IfPledge = Column(VARCHAR(12), comment='是否可质押')
    IfStructure = Column(VARCHAR(12), comment='是否结构化')
    IfTermination = Column(VARCHAR(12), comment='能否提前终止')
    TerminationConditions = Column(VARCHAR(1000), comment='提前终止条件')
    ApplyFrequency = Column(VARCHAR(12), comment='申购频率')
    Applyconfirmationtime = Column(VARCHAR(200), comment='申购确认时间')
    RedeemFrequency = Column(VARCHAR(12), comment='赎回频率')
    RedeemDeliverytime = Column(VARCHAR(200), comment='赎回到账时间')
    PRConditions = Column(VARCHAR(1000), comment='申购和赎回说明')
    ChargeRateDesc = Column(VARCHAR(1000), comment='费用说明')
    MaturityYieldDesc = Column(VARCHAR(1000), comment='收益说明')
    InvestmentDesc = Column(VARCHAR(1000), comment='投资标的说明')
    InvestRatio = Column(VARCHAR(1000), comment='投资比例')
    InvestRestrictions = Column(VARCHAR(1000), comment='其他投资限制')
    InvestStrategy = Column(VARCHAR(1000), comment='投资策略')
    TrustFunction = Column(VARCHAR(12), comment='信托功能')
    TrustFundUse = Column(VARCHAR(12), comment='信托资金运用方式')
    MaturityType = Column(VARCHAR(12), comment='期限类型')
    ProjectSite = Column(VARCHAR(100), comment='项目所在地')
    Counterparty = Column(VARCHAR(12), comment='交易对手')
    InvestAdviser = Column(VARCHAR(12), comment='投资顾问')
    InvestScope = Column(VARCHAR(12), comment='投资领域')
    ProfitDistribution = Column(VARCHAR(12), comment='收益分配方式')
    ProfitDistDesc = Column(VARCHAR(1000), comment='收益分配说明')
    StrArrangement = Column(VARCHAR(2000), comment='结构化安排')
    IfHaveMortgage = Column(VARCHAR(12), comment='是否有抵押')
    IfHavePledge = Column(VARCHAR(12), comment='是否有质押')
    IFHaveGuarantee = Column(VARCHAR(12), comment='是否有担保')
    RiskControlDesc = Column(VARCHAR(1000), comment='风控措施')
    ProductHighlights = Column(VARCHAR(1000), comment='产品亮点')
    RepaySource = Column(VARCHAR(1000), comment='还款来源')
    PlanType = Column(VARCHAR(12), comment='计划类型')
    PlanNature = Column(VARCHAR(12), comment='计划性质')
    InvestDirection = Column(VARCHAR(12), comment='计划投资方向')
    ExitType = Column(VARCHAR(12), comment='退出方式')
    LockupPeriod = Column(Numeric(19, 4), comment='封闭期')
    LockupPerUn = Column(VARCHAR(12), comment='封闭期单位')
    DurationDesc = Column(VARCHAR(200), comment='封闭期说明')
    SubsNum = Column(Numeric(10), comment='有效认购户数')
    ValueByManager = Column(Numeric(19, 4), comment='管理人参与金额(元)')
    InvestTarget = Column(VARCHAR(2000), comment='投资目标')
    InvestConcept = Column(VARCHAR(1000), comment='投资理念')
    RegisteredName = Column(VARCHAR(12), comment='注册登记人')
    ProductCode = Column(VARCHAR(20), comment='人社部登记代码')
    ConfirmationNum = Column(VARCHAR(50), comment='确认函号')
    ConfirmationDate = Column(VARCHAR(30), comment='确认函日期')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='修改时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('SecuCategory', "FinProCode"),)


class FpChargeRate(Base):
    """
    金融产品费率
    """
    __tablename__ = 'FP_ChargeRate'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    InfoPublDate = Column(VARCHAR(30), comment='信息发布日期')
    SerialNumber = Column(Numeric(10), comment='序号')
    ChargeRateType = Column(VARCHAR(12), comment='费率类别')
    ExcuteDate = Column(VARCHAR(30), comment='执行日期')
    CancelDate = Column(VARCHAR(30), comment='取消日期')
    IfEffected = Column(VARCHAR(12), comment='是否有效')
    AppliObject = Column(VARCHAR(12), comment='适用对象')
    ChargeRateInterval = Column(VARCHAR(12), comment='费率区间划分')
    ChargeRateIntervalBe = Column(Numeric(19, 4), comment='费率区间起始')
    ChargeRateIntervalEd = Column(Numeric(19, 4), comment='费率区间截止')
    IfApplyBegin = Column(VARCHAR(12), comment='是否包含费率区间起始')
    IfApplyEnd = Column(VARCHAR(12), comment='是否包含费率区间截止')
    IntervalUnit = Column(VARCHAR(12), comment='费率区间单位')
    ChargeRate = Column(Numeric(19, 6), comment='费率值')
    ChargeRateUnit = Column(VARCHAR(12), comment='费率单位')
    ChargeRateDesc = Column(VARCHAR(1000), comment='费率描述')
    UpdateTime = Column(VARCHAR(30), comment='更新日期')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('SecuCategory', "FinProCode"),)


class FpNetValue(Base):
    """
    金融产品净值
    """
    __tablename__ = 'FP_NetValue'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    InfoPublDate = Column(VARCHAR(30), comment='发布日期')
    StartDate = Column(VARCHAR(30), comment='开始日期')
    EndDate = Column(VARCHAR(30), comment='截止日期')
    HoldInterval = Column(VARCHAR(200), comment='持有期限区间')
    UnitNV = Column(Numeric(18, 9), comment='单位净值')
    AccumulatedUnitNV = Column(Numeric(18, 9), comment='累计净值')
    DailyProfit = Column(Numeric(18, 9), comment='每万份收益(元)')
    LatestWeeklyYield = Column(Numeric(18, 9), comment='七日年化收益率')
    AnnualYield = Column(Numeric(18, 9), comment='年化收益率')
    NV = Column(Numeric(18, 4), comment='净资产值(元)')
    Remark = Column(VARCHAR(500), comment='备注')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('SecuCategory', "FinProCode", 'StartDate', 'EndDate'),)


class FpNetValueRe(Base):
    """
    金融产品复权净值
    """
    __tablename__ = 'FP_NetValueRe'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    EndDate = Column(VARCHAR(30), comment='截止日期')
    UnitNV = Column(Numeric(18, 9), comment='单位净值')
    GrowthRateFactor = Column(Numeric(18, 9), comment='复权因子')
    UnitNVRestored = Column(Numeric(18, 9), comment='复权单位净值')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('SecuCategory', "FinProCode", 'EndDate'),)


class FpPerformance(Base):
    """
    金融产品收益表现
    """
    __tablename__ = 'FP_Performance'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    EndDate = Column(VARCHAR(30), comment='截止日期')
    NVDailyGrowthRate = Column(Numeric(18, 4), comment='日回报率(%)')
    RRInSelectedWeek = Column(Numeric(18, 4), comment='本周以来回报率(%)')
    RRInSingleWeek = Column(Numeric(18, 4), comment='一周回报率(%)')
    RRInSelectedMonth = Column(Numeric(18, 4), comment='本月以来回报率(%)')
    RRInSingleMonth = Column(Numeric(18, 4), comment='一个月回报率(%)')
    RRInThreeMonth = Column(Numeric(18, 4), comment='三个月回报率(%)')
    RRInSixMonth = Column(Numeric(18, 4), comment='六个月回报率(%)')
    RRSinceThisYear = Column(Numeric(18, 4), comment='今年以来回报率(%)')
    RRInSingleYear = Column(Numeric(18, 4), comment='一年回报率(%)')
    RRInTwoYear = Column(Numeric(18, 4), comment='二年回报率(%)')
    AnnualizedRRInTwoYear = Column(Numeric(18, 4), comment='二年年化回报率(%)')
    RRInThreeYear = Column(Numeric(18, 4), comment='三年回报率(%)')
    AnnualRRInThreeYear = Column(Numeric(18, 4), comment='三年年化回报率(%)')
    RRInFiveYear = Column(Numeric(18, 4), comment='五年回报率(%)')
    AnnualizedRRInFiveYear = Column(Numeric(18, 4), comment='五年年化回报率(%)')
    RRInTenYear = Column(Numeric(18, 4), comment='十年回报率(%)')
    AnnualizedRRInTenYear = Column(Numeric(18, 4), comment='十年年化回报率(%)')
    RRSinceStart = Column(Numeric(18, 4), comment='设立以来回报率(%)')
    AnnualizedRRSinceStart = Column(Numeric(18, 4), comment='设立以来年化回报率(%)')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('SecuCategory', "FinProCode",'EndDate'),)


class FpInvestCriterion(Base):
    """
    金融产品投资目标与业绩基准
    """
    __tablename__ = 'FP_InvestCriterion'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    InfoPublDate = Column(VARCHAR(30), comment='信息发布日期')
    InfoSource = Column(VARCHAR(100), comment='信息来源')
    IfExecuted = Column(VARCHAR(12), comment='是否执行')
    ExcuteDate = Column(VARCHAR(30), comment='执行日期')
    CancelDate = Column(VARCHAR(30), comment='取消日期')
    InvestTarget = Column(VARCHAR(12), comment='投资标的')
    InvestTargetName = Column(VARCHAR(200), comment='投资标的原始名称')
    TracedIndexCode = Column(VARCHAR(12), comment='参照基准指数内部编码')
    MaxInvestRatio = Column(Numeric(9, 6), comment='投资比例上限')
    MinInvestRatio = Column(Numeric(9, 6), comment='投资比例下限')
    InvestRatioBenchmark = Column(VARCHAR(12), comment='投资比例基准')
    InvestRatioDescription = Column(VARCHAR(1000), comment='投资比例描述')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('SecuCategory', "FinProCode"),)


class FpAssetAllocation(Base):
    """
    金融产品资产配置
    """
    __tablename__ = 'FP_AssetAllocation'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    InfoPublDate = Column(VARCHAR(30), comment='信息发布日期')
    InfoSource = Column(VARCHAR(100), comment='信息来源')
    EndDate = Column(VARCHAR(30), comment='截止日期')
    AssetTypeCode = Column(VARCHAR(12), comment='资产种类')
    AssetName = Column(VARCHAR(200), comment='资产种类原始名称')
    MarketValue = Column(Numeric(19, 4), comment='资产市值')
    RatioInNV = Column(Numeric(9, 6), comment='资产占净资产比例')
    RatioInTotalAsset = Column(Numeric(9, 6), comment='资产占总资产比例')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('SecuCategory', "FinProCode", "EndDate"),)


class FpPortfolioDetails(Base):
    """
    金融产品投资组合明细
    """
    __tablename__ = 'FP_PortfolioDetails'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    InfoPublDate = Column(VARCHAR(30), comment='信息发布日期')
    InfoSource = Column(VARCHAR(100), comment='信息来源')
    ReportType = Column(VARCHAR(12), comment='报告类型')
    EndDate = Column(VARCHAR(30), comment='截止日期')
    AdjustMark = Column(VARCHAR(12), comment='调整标志')
    InvestType = Column(VARCHAR(12), comment='投资类型')
    PenetrationType = Column(VARCHAR(12), comment='穿透类型')
    InvestObject = Column(VARCHAR(12), comment='投资对象')
    DetailType = Column(VARCHAR(12), comment='投资明细类别')
    SerialNumber = Column(Numeric(10), comment='序号')
    SecuCode = Column(VARCHAR(50), comment='证券代码(披露)')
    SecuName = Column(VARCHAR(200), comment='证券名称')
    InnerCode = Column(VARCHAR(12), comment='证券内部编码')
    SharesHolding = Column(Numeric(19, 2), comment='持仓数量(股)')
    MarketValue = Column(Numeric(19, 4), comment='持仓市值(元)')
    RatioInNV = Column(Numeric(18, 6), comment='占净值比')
    Remark = Column(VARCHAR(500), comment='备注说明')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('SecuCategory', "FinProCode", "EndDate"),)


class FpCodeRelationship(Base):
    """
    金融产品代码关联
    """
    __tablename__ = 'FP_CodeRelationship'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    FinProCode = Column(VARCHAR(12), comment='金融产品编码')
    SecuCategory = Column(VARCHAR(12), comment='证券类别')
    CodeDefine = Column(VARCHAR(12), comment='代码关联方式')
    RelatedFinProCode = Column(VARCHAR(12), comment='关联代码金融产品编码')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('RelatedFinProCode', "FinProCode"),)


class FpIndicator(Base):
    """
    金融产品指标码表
    """
    __tablename__ = 'FP_Indicator'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    GilCode = Column(VARCHAR(12), comment='聚源指标代码')
    ChiName = Column(VARCHAR(150), comment='中文名称')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('GilCode'),)


class LC_InstiQualCoRe(Base):
    """
    构资格对应关系表
    """
    __tablename__ = 'LC_InstiQualCoRe'
    ID = Column(Numeric(19), comment='ID',primary_key=True)
    InfoPublDate = Column(VARCHAR(30), comment='信息发布日期')
    InfoSource = Column(Numeric(10), comment='信息来源')
    CompanyCode = Column(Numeric(10), comment='机构编码')
    AgentName = Column(VARCHAR(100), comment='机构名称')
    QualCategory = Column(Numeric(10), comment='资格类别')
    QualCode = Column(Numeric(10), comment='资格内部编码')
    QualName = Column(VARCHAR(100), comment='资格名称')
    AdminNumber = Column(VARCHAR(100), comment='行政文号')
    QualStartDate = Column(VARCHAR(30), comment='资格起始日')
    QualEndDate = Column(VARCHAR(30), comment='资格截止日')
    QualState = Column(Numeric(10), comment='资格状态')
    Remark = Column(VARCHAR(2000), comment='备注')
    InsertTime = Column(VARCHAR(30), comment='发布时间')
    UpdateTime = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('QualCode'),)


class LC_InstiArchive(Base):
    """
    机构基本资料
    """
    __tablename__ = 'LC_InstiArchive'
    ID = Column(Numeric(19), comment='ID', primary_key=True)
    CompanyCode = Column(Numeric(10), comment='企业编号')
    ParentCompany = Column(Numeric(10), comment='所属公司')
    ListedCode = Column(Numeric(10), comment='上市公司代码')
    InvestAdvisorName = Column(Numeric(10), comment='基金管理人名称')
    TrusteeName = Column(Numeric(10), comment='基金托管人名称')
    ChiName = Column(VARCHAR(100), comment='中文名称')
    AbbrChiName = Column(VARCHAR(100), comment='中文简称')
    NameChiSpelling = Column(VARCHAR(100), comment='中文拼音简称')
    EngName = Column(VARCHAR(100), comment='英文名称')
    AbbrEngName = Column(VARCHAR(100), comment='英文简称')
    OrganizationCode = Column(VARCHAR(20), comment='组织机构代码')
    CreditCode = Column(VARCHAR(20), comment='统一社会信用代码')
    RegCapital = Column(Numeric(19, 4), comment='注册资本(元)')
    CurrencyUnit = Column(Numeric(10), comment='货币单位')
    EstablishmentDate = Column(VARCHAR(30), comment='成立日期')
    EconomicNature = Column(Numeric(10), comment='经济性质')
    CompanyNature = Column(Numeric(10), comment='企业性质')
    CompanyType = Column(Numeric(10), comment='企业类别')
    CompanyCval = Column(Numeric(10), comment='公司属性')
    RegStatus = Column(Numeric(10), comment='登记状态')
    RegAddr = Column(VARCHAR(200), comment='注册地址')
    RegZip = Column(VARCHAR(6), comment='注册地址邮编')
    RegCity = Column(Numeric(10), comment='注册所在城市')
    RegArea = Column(Numeric(10), comment='注册所在区县')
    OfficeAddr = Column(VARCHAR(200), comment='办公地址')
    ContactAddr = Column(VARCHAR(200), comment='联系地址')
    ContactZip = Column(VARCHAR(6), comment='联系地址邮编')
    ContactCity = Column(Numeric(10), comment='联系所在城市')
    Email = Column(VARCHAR(50), comment='电子邮箱')
    Website = Column(VARCHAR(50), comment='网址')
    LegalPersonRepr = Column(VARCHAR(50), comment='法人代表')
    GeneralManager = Column(VARCHAR(50), comment='总经理')
    OtherManager = Column(VARCHAR(50), comment='其它负责人')
    Contactman = Column(VARCHAR(50), comment='联系人')
    RegOrg = Column(VARCHAR(100), comment='登记机构')
    Tel = Column(VARCHAR(50), comment='联系电话')
    Fax = Column(VARCHAR(50), comment='传真')
    BriefIntroText = Column(VARCHAR(1000), comment='公司简介')
    BusinessMajor = Column(VARCHAR(1000), comment='经营范围-主营业务')
    Industry = Column(Numeric(10), comment='所属行业')
    StartDate = Column(VARCHAR(30), comment='存续起始日')
    CloseDate = Column(VARCHAR(30), comment='存续截止日')
    CloseReason = Column(Numeric(10), comment='存续截止原因')
    IfExisted = Column(Numeric(10), comment='是否存在')
    XGRQ = Column(VARCHAR(30), comment='更新时间')
    JSID = Column(Numeric(19), comment='JSID')
    __table_args__ = (Index('CompanyCode'),)





def create_table(connection):
    Base.metadata.create_all(connection.engine)
