select * from QT_TradingCapitalFlow 
where InnerCode=3 and TradingDate >'20170601'
ORDER  by TradingDate 

select InnerCode , SecuCode from SecuMain

select * from SecuMain
where InnerCode =3



select a.*,b.SecuCode  from QT_TradingCapitalFlow a,SecuMain b 
where a.InnerCode =b.InnerCode 

select * from SF_PLANMAIN a
where a.ChiName like '%苏银理财%'

-- 银行理财产品要素
select * from SF_BFPLANINFO


-- 银行理财产品条款 
select * from  SF_BFPLANTERM

-- 银行理财产品净值收益
select * from SF_BFNETVALUE


select enddate,TradingType ,BTradeValue from LC_SHSCTradeStat
where  enddate >'20160101'
order by enddate 

-- 金融产品数据库 


-- 金融产品概况
select t.ChiName,a.* from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode

-- 金融产品主表 

select t.ChiName,a.LockupPerUn from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode


select t.ChiName,a.SecuCategory,a.FinProCode,a.RiskLevelCode,a.RegistrationCode,a.IncomeType,a.ParValue,a.CurrencyUnit,a.RaisingType,a.IssueObject,a.IssueRegion,a.PurchaseChannels,a.PopularizeStDate,a.PopularizeEdDate,a.EstablishmentDate,a.MaturityDate,a.ActMaturityDate,a.MinInvestTerm,a.MinInvestTermUnit,a.InvestTerm,a.InvestTermUnit,a.LeastBuySum,a.IncreasingAmountPER,a.MaximumApplying,a.IssueVolCeiling,a.IssueVolFloor,a.ActRaisingAmount,a.PublishDesc,a.IfCancel,a.CancelRegulation,a.ExpAnEnYield,a.ExpAnBeYield,a.BenchmarkMax,a.BenchmarkMin,a.AnnualDays,a.DeliveryDays,a.InvestAdvisorCode,a.TrusteeCode,a.OperationType,a.IfDiscloseDP,a.InvestmentType,a.IfPledge,a.IfStructure,a.IfTermination,a.TerminationConditions,a.ApplyFrequency,a.Applyconfirmationtime,a.RedeemFrequency,a.RedeemDeliverytime,a.PRConditions,a.ChargeRateDesc,a.MaturityYieldDesc,a.InvestmentDesc,a.InvestRatio,a.InvestRestrictions,a.InvestStrategy,a.TrustFunction,a.TrustFundUse,a.MaturityType,a.ProjectSite,a.Counterparty,a.InvestAdviser,a.InvestScope,a.ProfitDistribution,a.ProfitDistDesc,a.StrArrangement,a.IfHaveMortgage,a.IfHavePledge,a.IFHaveGuarantee,a.RiskControlDesc,a.ProductHighlights,a.RepaySource,a.PlanType,a.PlanNature,a.InvestDirection,a.ExitType,a.LockupPeriod,a.LockupPerUn,a.DurationDesc,a.SubsNum,a.ValueByManager,a.InvestTarget,a.InvestConcept,a.RegisteredName,a.ProductCode,a.ConfirmationNum,a.ConfirmationDate,a.InsertTime,a.UpdateTime,a.JSID from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode

SecuCategory,FinProCode,RiskLevelCode,RegistrationCode,IncomeType,ParValue,CurrencyUnit,RaisingType,IssueObject,IssueRegion,PurchaseChannels,PopularizeStDate,PopularizeEdDate,EstablishmentDate,MaturityDate,ActMaturityDate,MinInvestTerm,MinInvestTermUnit,InvestTerm,InvestTermUnit,LeastBuySum,IncreasingAmountPER,MaximumApplying,IssueVolCeiling,IssueVolFloor,ActRaisingAmount,PublishDesc,IfCancel,CancelRegulation,ExpAnEnYield,ExpAnBeYield,BenchmarkMax,BenchmarkMin,AnnualDays,DeliveryDays,InvestAdvisorCode,TrusteeCode,OperationType,IfDiscloseDP,InvestmentType,IfPledge,IfStructure,IfTermination,TerminationConditions,ApplyFrequency,Applyconfirmationtime,RedeemFrequency,RedeemDeliverytime,PRConditions,ChargeRateDesc,MaturityYieldDesc,InvestmentDesc,InvestRatio,InvestRestrictions,InvestStrategy,TrustFunction,TrustFundUse,MaturityType,ProjectSite,Counterparty,InvestAdviser,InvestScope,ProfitDistribution,ProfitDistDesc,StrArrangement,IfHaveMortgage,IfHavePledge,IFHaveGuarantee,RiskControlDesc,ProductHighlights,RepaySource,PlanType,PlanNature,InvestDirection,ExitType,LockupPeriod,LockupPerUn,DurationDesc,SubsNum,ValueByManager,InvestTarget,InvestConcept,RegisteredName,ProductCode,ConfirmationNum,ConfirmationDate,InsertTime,UpdateTime,JSID from FP_BasicInfo

select LockupPerUn from FP_BasicInfo


-- 金融产品净值 
select * from FP_NetValue
where FinProCode ='SEC00007HYFY'


-- 金融产品概况表 

select t.ChiName,a.* from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode

-- 建立索引 
--金融产品概况表
CREATE INDEX FP_BasicInfo_index ON FP_BasicInfo  
(FinProCode, RiskLevelCode,IncomeType,RaisingType,MinInvestTermUnit, InvestTermUnit,
IfCancel,InvestAdvisorCode,TrusteeCode,OperationType,IfDiscloseDP,InvestmentType,IfPledge,
IfStructure,IfTermination,ApplyFrequency,RedeemFrequency)

-- 金融产品指标码表 FP_Indicator
CREATE INDEX FP_Indicator_index ON FP_Indicator  
(GilCode,ChiName)

select * from FP_Indicator

-- 金融产品主表 FP_SecuMain
CREATE INDEX FP_SecuMain_index ON FP_SecuMain  
(FinProCode,ChiName)


-- 需要更新的数据
-- 企业码表（EP_CompanyMain) （无） 
CREATE INDEX EP_CompanyMain_index ON EP_CompanyMain  
(FinProCode,ChiName)


-- 大的关联数据 

select t.ChiName,a.PopularizeStDate,a.* from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode
order by a.PopularizeEdDate 

select * from FP_Indicator

PopularizeStDate	


--(1) 统计数据（产品数量）    注意 需要加索引 
select t.ChiName,a.* from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode



-- （2） 净值数据 
select *  from  FP_NetValue

select ChiName,InfoPublDate ,StartDate ,EndDate ,HoldInterval ,UnitNV ,AccumulatedUnitNV ,DailyProfit ,LatestWeeklyYield ,AnnualYield ,nv from (
select  t.ChiName ,a.* from  FP_NetValue a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode) b
where ChiName = '苏银理财恒源2年定开2007期'


-- 统计精致产品个数 
select * from (
select  t.ChiName ,a.* from  FP_NetValue a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode)b     

select ChiName,FinProCode ,EndDate ,UnitNV , GrowthRateFactor ,UnitNVRestored from (
select  t.ChiName ,a.* from  FP_NetValueRe a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode) b
where ChiName = '苏银理财恒源2年定开2007期'

select x.ChiName,x.InfoPublDate ,x.StartDate ,x.EndDate ,x.HoldInterval ,x.UnitNV ,x.AccumulatedUnitNV ,x.DailyProfit ,x.LatestWeeklyYield ,x.AnnualYield ,x.nv,
y.GrowthRateFactor,y.UnitNVRestored
from( 
select ChiName,InfoPublDate ,StartDate ,EndDate ,HoldInterval ,UnitNV ,AccumulatedUnitNV ,DailyProfit ,LatestWeeklyYield ,AnnualYield ,nv from (
select  t.ChiName ,a.* from  FP_NetValue a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode) b
where ChiName = '苏银理财恒源2年定开2007期') x inner join (select ChiName,FinProCode ,EndDate ,UnitNV , GrowthRateFactor ,UnitNVRestored from (
select  t.ChiName ,a.* from  FP_NetValueRe a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode) b
where ChiName = '苏银理财恒源2年定开2007期') y 
on x.EndDate = y.EndDate


-- 聚源和路演产品对比 
select * from FP_BasicInfo


select FinProCode,ChiName,SecuState from FP_SecuMain
where ChiName like '%苏银理财%'




select count(*) from (  -- 27209
select  t.ChiName ,a.* from  FP_NetValue a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode) b

select distinct ChiName from (  --  产品数量
select  t.ChiName ,a.* from  FP_NetValue a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode) b

-- 风险等级 (特别慢) 
select t.ChiName,a.RiskLevelCode,a.RiskControlDesc from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理 财%')t 
on a.FinProCode = t.FinProCode


-- 预期收益率 
select t.ChiName,a.ExpAnEnYield,a.ExpAnBeYield,a.BenchmarkMax ,a.BenchmarkMin from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%苏银理财%')t 
on a.FinProCode = t.FinProCode

select t.ChiName,a.ExpAnEnYield,a.ExpAnBeYield,a.BenchmarkMax ,a.BenchmarkMin from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain )t 
on a.FinProCode = t.FinProCode

-- 产品明细 

select t.ChiName,a.* from  dbo.FP_PortfolioDetails a full join (select * from  FP_SecuMain  )t 
on a.FinProCode = t.FinProCode
join dbo.FP_BasicInfo c 
on a.FinProCode  = c.FinProCode 

where a.SecuCategory ='FCC0000001TD'
--and t.ChiName like  '%农银理财%'
and a.InvestObject ='FCC0000001D1'
and c.InvestmentType = 'FCC0000001T8'
order by a.FinProCode, a.EndDate 




select t.ChiName,a.* from  FP_AssetAllocation a full join (select * from  FP_SecuMain  )t 
on a.FinProCode = t.FinProCode
where  a.FinProcode ='SEC00002PRZT'

where a.FinProCode='SEC00007I1RZ'

select distinct AssetName from FP_AssetAllocation
where SecuCategory = 'FCC0000001TD'

select * from FP_PortfolioDetails

select  ActRaisingAmount from FP_BasicInfo
where FinProCode = 'SEC00007I1RZ'

select  * from FP_secumain
where FinProCode = 'SEC00007I1RZ'

select * from FP_PortfolioDetails
select * from FP_AssetAllocation

-- 投资策略 

SELECT  t.ChiName,a.InvestStrategy   FROM FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain )t 
on a.FinProCode = t.FinProCode
 
select  t.ChiName,a.InvestStrategy   FROM FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where FinProCode = 'SEC000031UKJ')t 
on a.FinProCode = t.FinProCode

本理财产品通过自上而下的宏观经济基本面分析，在通过投资固定收益类资产获得稳定投资收益的同时，
通过对权益资产组合的动态调整增厚收益，实现投资组合能够适应不同经济情景的目的。具体而言，以
债券、非标准化债权类资产、债券回购等固定收益类资产配置为主来获取稳健收益，通过投资权益类资
产灵活抓取市场机会，并且进行紧密的投后跟踪管理，严格控制产品投资风险，追求稳定收益基础上获
取增强收入，
让投资者在风险相对可控的情况下分享多市场快速发展的红利，以更好地实现投资者财富保值增值的目的。

-- 发行对象 
SELECT  distinct a.IssueObject   FROM FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain )t 
on a.FinProCode = t.FinProCode


-- 聚源数据同步事项
-- 金融产品主表 (有）
select * from FP_SecuMain

-- 金融产品概况
select * from FP_BasicInfo 

-- 金融产品费率
select * from FP_ChargeRate
where FinProCode = 'SEC00007J68U'
and ChargeRateType ='FCC0000001RU'


--金融产品净值
select * from FP_NetValue 

-- 金融产品复权净值
select * from FP_NetValueRe

-- 金融产品收益表现
select * from FP_Performance

-- 金融产品投资目标与业绩基准
select * from FP_InvestCriterion

-- 金融产品资产配置
select * from FP_AssetAllocation

-- 金融产品投资组合明细
select * from FP_PortfolioDetails
where FinProCode = 'SEC00003AK9V'

-- 金融产品份额变动 
select * from FP_SharesChange

-- 金融产品收益分配
select * from FP_ProfitDistribution

-- 金融产品投资经理
select * from FP_InvestManager

-- 金融产品投资经理基本资料
select * from FP_PersonalInfo

-- 金融产品代码关联
select * from FP_CodeRelationship

投资资产组合净值扣除销售服务费、产品托管费后超过业绩比较基准收益时，
兴业银行有权收取投资管理费。投资管理费年化费率不超过0.30%。

优惠内容：投资管理费
优惠前费率：0.25%
优惠后费率：0.05%
--金融产品指标码表
select * from FP_Indicator 

----------------------------  Index ---------------------------- 
-- 金融产品主表 
CREATE INDEX FP_SecuMain_index ON FP_SecuMain
(FinProCode,EnterpriseCode,SecuCode,ChiName,SecuCategory,SecuState)  

--金融产品概况表
CREATE INDEX FP_BasicInfo_index ON FP_BasicInfo  
(SecuCategory,FinProCode, RiskLevelCode,IncomeType,RaisingType,
InvestAdvisorCode,TrusteeCode,OperationType,IfDiscloseDP,InvestmentType,IfPledge,
IfStructure,IfTermination)


--金融产品净值
CREATE INDEX FP_NetValue_index ON FP_NetValue 
(SecuCategory,FinProCode,InfoPublDate,StartDate,EndDate)  

-- 金融产品复权净值
CREATE INDEX FP_NetValueRe_index ON FP_NetValueRe 
(SecuCategory,FinProCode,EndDate)  


-- 金融产品收益表现
CREATE INDEX FP_Performance_index ON FP_Performance 
(SecuCategory,FinProCode,EndDate)  

-- 金融产品投资目标与业绩基准
select * from FP_InvestCriterion
CREATE INDEX FP_InvestCriterion_index ON FP_InvestCriterion 
(SecuCategory,FinProCode,InfoPublDate,InfoSource,IfExecuted) 

-- 金融产品资产配置
CREATE INDEX FP_AssetAllocation_index ON FP_AssetAllocation 
(SecuCategory,FinProCode,EndDate)  

-- 金融产品投资组合明细
CREATE INDEX FP_PortfolioDetails_index ON FP_PortfolioDetails 
(SecuCategory,FinProCode,ReportType,EndDate,InvestType,InvestObject,DetailType,
SecuCode,InnerCode)  

-- 金融产品份额变动 
CREATE INDEX FP_SharesChange_index ON FP_SharesChange 
(SecuCategory,FinProCode,InfoPublDate,BeginDate,ChangeType,EndDate)

-- 金融产品收益分配
CREATE INDEX FP_ProfitDistribution_index ON FP_ProfitDistribution 
(SecuCategory,FinProCode,InfoPublDate,Year,DistType)

-- 金融产品投资经理
CREATE INDEX FP_InvestManager_index ON FP_InvestManager 
(SecuCategory,FinProCode,InfoPublDate)


-- 金融产品代码关联
CREATE INDEX FP_CodeRelationship_index ON FP_CodeRelationship 
(SecuCategory,FinProCode,RelatedFinProCode)

-- 金融产品指标码表 FP_Indicator
CREATE INDEX FP_Indicator_index ON FP_Indicator  
(GilCode,ChiName)


-- 外资
select t.ChiName,a.* from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%交银施罗德%')t --95
on a.FinProCode = t.FinProCode

select t.ChiName,a.* from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%高盛工银%')t   -- 0 
on a.FinProCode = t.FinProCode


select t.ChiName,a.* from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain 
where ChiName like '%贝莱德建信%')t   --5 


-- 产品数量 -- 476581
select t.ChiName,a.* from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain )t
on a.FinProCode = t.FinProCode

-- 公司数量 --  380
select  distinct EnterpriseCode from FP_SecuMain
where SecuCategory = 'FCC0000001TD'


select t.ChiName,a.InvestRatio,a.InvestRestrictions from  FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain )t
on a.FinProCode = t.FinProCode


select * from FP_Indicator

-- 产品明细    


 select b.ChiName,a.* from FP_AssetAllocation a inner join FP_SecuMain b
 on a.FinProCode = b.FinProCode
 where ChiName = '苏银理财恒源周开放融享1号'
 order by enddate 
 
 
select b.ChiName,a.* from FP_AssetAllocation a inner join FP_SecuMain b
on a.FinProCode = b.FinProCode
where ChiName like '%苏银理财%'


-- 目的是通过这几个类型 将策略 分位几种类型  
-- RiskLevelCode,风险评级
--- IncomeType 收益类型,
-- RaisingType 募集方式 ,
-- 募集方式  RaisingType
-- InvestmentType 投资性质,
-- 最短持有期限单位(MinInvestTermUnit)
--期限类型(MaturityType),
--投资领域(InvestScope)
-- 是否有抵押(IfHaveMortgage),
--计划类型(PlanType),
--计划投资方向(InvestDirection)
-- 封闭期单位(LockupPerUn),
--退出方式(ExitType),
--是否结构化(IfStructure)
--运作方式（OperationType）
-- 是否可质押（IfPledge）
--能否提前终止（IfTermination）
--赎回频率(RedeemFrequency)
--期限类型(MaturityType)
--投资领域(InvestScope)
-- 收益分配方式(ProfitDistribution)
-- 是否有抵押(IfHaveMortgage)
-- 是否有质押(IfHavePledge)
-- 是否有担保(IFHaveGuarantee)




-- SecuCategory  证券类别 
SELECT  t.ChiName,a.*,a.IncomeType,a.InvestmentType,a.RaisingType,a.InvestmentType FROM FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain )t 
on a.FinProCode = t.FinProCode
where ChiName like '%建信理财%'









select * from FP_SecuMain





select  * from FP_SecuMain --拿到公司号 
where ChiNameAbbr like '%理财%' 

select  * from EP_CompanyMain --拿到公司号 
where ChiNameAbbr like '%理财%' 

select * from dbo.FP_SecuMain  -- 上银理财  （可以拿到产品号）
where EnterpriseCode = 'SEC00003E656'  

select b.* from (
SELECT  t.ChiName,a.* FROM FP_BasicInfo a inner join (select FinProCode,ChiName from  FP_SecuMain )t 
on a.FinProCode = t.FinProCode) b
where b.FinProCode = 'SEC000035412'

select * from  dbo.FP_BasicInfo 
where FinProCode = 'SEC000035412'
 

-- 字段检验非空

-- 基准利率 
select count(*)  from  dbo.FP_BasicInfo -- 477571  

select count(*)  from  dbo.FP_BasicInfo -- 244452  
where  SecuCategory = 'FCC0000001TD'

select count(*) as BenchmarkMax_num from  dbo.FP_BasicInfo  -- 113619  0.5
where BenchmarkMax is not null and SecuCategory = 'FCC0000001TD'

select count(*) as BenchmarkMin_num from  dbo.FP_BasicInfo  -- 113291  0.5
where BenchmarkMin is not null   and SecuCategory = 'FCC0000001TD'

select count(*) as ExpAnEnYield_num from  dbo.FP_BasicInfo  -- 108840  0.44
where ExpAnEnYield is not null  and SecuCategory = 'FCC0000001TD'

select count(*) as ExpAnBeYield_num from  dbo.FP_BasicInfo  -- 96011  0.39
where ExpAnBeYield is not null and SecuCategory = 'FCC0000001TD'

-- 投资性质 

select count(*)  from  dbo.FP_BasicInfo -- 244452  
where  SecuCategory = 'FCC0000001TD'

select count(*) as InvestmentType_num from  dbo.FP_BasicInfo  -- 226612  0.9
where InvestmentType is not null and SecuCategory = 'FCC0000001TD'


-- 投资比例限制 
select top 10 InvestRestrictions,InvestRatio,InvestmentDesc  from  dbo.FP_BasicInfo -- 244452  
where SecuCategory = 'FCC0000001TD'

select count(*)  from  dbo.FP_BasicInfo -- 244452  
where InvestRestrictions is not null and SecuCategory = 'FCC0000001TD'


-- 统计理财子个数  26 

select distinct chinaname, CompanyCode from (
select b.ChiName as chinaname ,a.* from (
select * from FP_SecuMain where SecuCategory ='FCC0000001TD') a inner join (select * from 
LC_InstiArchive  c where c.ChiName like '%理财%') b
on a.CompanyCode = b.CompanyCode)t

select distinct  CompanyCode from (
select b.ChiName as chinaname ,a.* from (
select * from FP_SecuMain where SecuCategory ='FCC0000001TD') a inner join (select * from 
LC_InstiArchive  c where c.ChiName like '%理财%') b
on a.CompanyCode = b.CompanyCode)t

-- 统计理财子产品

select * from FP_SecuMain  -- 17217 
where CompanyCode in (select distinct  CompanyCode from (
select b.ChiName as chinaname ,a.* from (
select * from FP_SecuMain where SecuCategory ='FCC0000001TD') a inner join (select * from 
LC_InstiArchive  c where c.ChiName like '%理财%') b
on a.CompanyCode = b.CompanyCode)t)
and SecuState in('FCC0000001TG')

-- 选择理财子公司 
select distinct agentname from LC_InstiQualCoRe 
where    QualName='商业理财子公司'

-- 区分城市行、外资银行等 
select * from LC_InstiQualCoRe 
where AgentName = '杭银理财有限责任公司'


SELECT
	DISTINCT 
--	D.ChiName,
--	D.CompanyNature,
--	D.CompanyCval,
	A.AgentName	
FROM
	dbo.LC_InstiQualCoRe A
full JOIN 
	(SELECT * FROM FP_SecuMain C WHERE C.SecuCategory = 'FCC0000001TD') B ON  
	B.CompanyCode = A.CompanyCode
--FULL  JOIN LC_InstiArchive C ON
--	A.CompanyCode = C.CompanyCode
--FULL  JOIN LC_InstiArchive D ON
--	D.CompanyCode = C.ParentCompany
WHERE
	QualCode = 2029
	

-- 全部理财子公司
select  DISTINCT  AgentName from  LC_InstiQualCoRe
where QualCode = 2029
	
select distinct agentname from LC_InstiQualCoRe 
where AgentName like '%理财%' and QualName='商业理财子公司'
and AgentName not in(SELECT
	DISTINCT A.AgentName
FROM
	dbo.LC_InstiQualCoRe A
JOIN FP_SecuMain B ON
	B.CompanyCode = A.CompanyCode
JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
JOIN LC_InstiArchive D ON
	D.CompanyCode = C.ParentCompany
join LC_InstiQualCoRe E on
	D.CompanyCode = E.CompanyCode 
WHERE
	A.QualCode = 2029
	and E.QualCode in (2004,2007,2008,2015,2018)
	AND B.SecuCategory = 'FCC0000001TD')
	
	
	select count(*) from (
	SELECT
	DISTINCT D.ChiName,
	E.QualName,
	A.AgentName,
	B.FinProCode,
	B.ChiName as product_name
FROM
	dbo.LC_InstiQualCoRe A
FULL JOIN (SELECT * FROM FP_SecuMain T WHERE T.SecuCategory = 'FCC0000001TD') B ON
	B.CompanyCode = A.CompanyCode
JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
JOIN LC_InstiArchive D ON
	D.CompanyCode = C.ParentCompany
join LC_InstiQualCoRe E on
	D.CompanyCode = E.CompanyCode 
WHERE 
	A.QualCode = 2029
	and E.QualCode in (2004,2007,2008,2015,2029) -- 规定类别 
	and B.SecuState in ('FCC0000001TF','FCC0000001TG')
	)m
	
-- 理财子公司计算产品数目 
select
	AgentName,
	count(*) as num
from
	(
	select
		A.AgentName, B.finprocode
	from
		LC_InstiQualCoRe A
	FULL JOIN (
		SELECT * FROM  FP_SecuMain T
		WHERE
			T.SecuCategory = 'FCC0000001TD') B ON
		B.CompanyCode = A.CompanyCode
	where
		A.QualCode = 2029) t
group by
	AgentName
order by
	num desc

select *  from(
select   
	A.AgentName,B.finprocode from  LC_InstiQualCoRe A
FULL JOIN (SELECT * FROM FP_SecuMain T WHERE T.SecuCategory = 'FCC0000001TD') B ON
	B.CompanyCode = A.CompanyCode
where A.QualCode = 2029) t
where t.AgentName = '贝莱德建信理财有限责任公司'


-- 明天增加存续期 筛选 
	SELECT
	DISTINCT D.ChiName,
	E.QualName,
	A.AgentName,
	B.FinProCode,
	B.ChiName as product_name,
	G.ChiName as SecuState_name
FROM
	LC_InstiQualCoRe A
FULL JOIN (SELECT * FROM FP_SecuMain T WHERE T.SecuCategory = 'FCC0000001TD') B ON  --  银行理财
	B.CompanyCode = A.CompanyCode
JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
JOIN LC_InstiArchive D ON
	D.CompanyCode = C.ParentCompany
join LC_InstiQualCoRe E on
	D.CompanyCode = E.CompanyCode 
join FP_BasicInfo F on 
	B.FinProCode = F.FinProCode
join FP_Indicator G on  
	B.SecuState = G.GilCode
WHERE 
	A.QualCode = 2029  -- 商业银行理财子公司
	and E.QualCode in (2004,2007,2008,2015,2029) -- 规定类别  城商行、国有行、外资合营的划分等
	and B.SecuState in ('FCC0000001TF','FCC0000001TG') -- 募集期和存续期
	and F.PopularizeStDate>='20180801'  -- 销售起始日 


-- 查询提前终止 


		
SELECT Redeem_name,count(*) FROM (
select   
	A.AgentName,
	B.finprocode,
	b.ChiName,
	C.RedeemFrequency,
	D.ChiName AS Redeem_name
	from  LC_InstiQualCoRe A
JOIN (SELECT * FROM FP_SecuMain T WHERE T.SecuCategory = 'FCC0000001TD') B ON
	B.CompanyCode = A.CompanyCode
JOIN FP_BasicInfo C ON 
	B.FinProCode = C.FinProCode
JOIN  FP_Indicator D ON 
	C.RedeemFrequency = D.GilCode
WHERE A.QualCode = 2029
AND  A.AgentName = '苏银理财有限责任公司')T
GROUP BY Redeem_name





select DISTINCT 
		A.FinProCode as 产品代码,
		A.ChiName as 产品名称,
		C.EndDate as 日期,
        C.MarketValue as 净资产,
        F.ChiName as 募集方式,
from
        FP_SecuMain A
left join LC_InstiArchive B on
        A.CompanyCode = B.CompanyCode
left join (select * from FP_AssetAllocation where EndDate ='20220630'
		and AssetTypeCode ='FCC0000001X9' ) C
    on    A.FinProCode = C.FinProCode 
LEFT join FP_BasicInfo D on
        A.FinProCode = D.FinProCode
join FP_Indicator F 
	on D.RaisingType = F.GilCode
where B.AbbrChiName = '苏银理财' and  D.PopularizeStDate >='20180801'
AND A.SecuState IN ('FCC0000001TF','FCC0000001TG')
and A.FinProCode  not in (select distinct FinProCode from 
   FP_CodeRelationship where CodeDefine in ('FCC000000YDC','FCC000001E0I'))



select DISTINCT 
		A.FinProCode as 产品代码,
		A.ChiName as 产品名称,
		C.EndDate as 日期,
        C.MarketValue as 净资产,
        F.ChiName as 募集方式
from
        FP_SecuMain A
left join LC_InstiArchive B on
        A.CompanyCode = B.CompanyCode
left join (select * from FP_AssetAllocation where EndDate ='20220630'
		and AssetTypeCode ='FCC0000001X9' ) C
    on    A.FinProCode = C.FinProCode 
LEFT join FP_BasicInfo D on
        A.FinProCode = D.FinProCode
join FP_Indicator F 
	on D.RaisingType = F.GilCode
where B.AbbrChiName = '苏银理财' and  D.PopularizeStDate >='20180801'
AND A.SecuState IN ('FCC0000001TF','FCC0000001TG')


and A.FinProCode  not in (select distinct FinProCode from 
   FP_CodeRelationship where CodeDefine in ('FCC000000YDC','FCC000001E0I'))
   

select * from FP_AssetAllocation
where FinProCode ='SEC00007HP17'

select * from dbo.FP_NetValue 
where FinProCode ='SEC00007HP17'

select * from dbo.FP_SharesChange
where FinProCode ='SEC00007HP17'

 -- 查看已有的索引 
 exec sp_helpindex  FP_AssetAllocation

  
 
 
 --同一产品份额关联-FCC000001E0I（指银行未给出母产品代码，我们选取原始份额作为主产品去关联其他份额）
SELECT CodeDefine 代码关联方式,RelatedFinProCode 主产品,FinProCode 子产品 FROM FP_CodeRelationship
  WHERE RelatedFinProCode='SEC00007649R'
SELECT B.RegistrationCode 登记编码,A.ChiName 产品名称, A.FinProCode,* FROM FP_SecuMain A
  LEFT JOIN FP_BasicInfo B ON A.FinProCode=B.FinProCode
  WHERE A.FinProCode IN ('SEC00007649R','SEC00007H8TO')
 
  select distinct FinProCode from FP_CodeRelationship
  where CodeDefine in ('FCC000000YDC','FCC000001E0I')
  and SecuCategory = 'FCC0000001TD'

  
  
  
 -- 不同期关联
 SELECT CodeDefine 代码关联方式,RelatedFinProCode 主产品,FinProCode 子产品 FROM FP_CodeRelationship
  WHERE RelatedFinProCode='SEC00003EH32'
SELECT B.RegistrationCode 登记编码,A.ChiName 产品名称,A.FinProCode,B.EstablishmentDate 成立日,B.MaturityDate 到期日,B.ActMaturityDate 实际到期日 FROM FP_SecuMain A
  LEFT JOIN FP_BasicInfo B ON A.FinProCode=B.FinProCode
  WHERE A.FinProCode IN ('SEC00003EH32','SEC00007GANQ','SEC00003EH36','SEC00003JL66','SEC00007GANN','SEC00007GUN8','SEC00007HTIY')
  ORDER BY B.EstablishmentDate DESC


  
SELECT * FROM dbo.FP_SecuMain fsm 
WHERE FinProCode = 'SEC00007G908'



SELECT	
		Insti.AgentName,
		SecuMain.FinProCode,
		SecuMain.ChiName,
		BasicInfo.MinInvestTerm ,
		BasicInfo.MinInvestTermUnit,
		BasicInfo.MinInvestDay,
		CASE
			when BasicInfo.MinInvestDay is null
		or BasicInfo.MinInvestDay = -1 then '数据缺失'
		when BasicInfo.MinInvestDay = 1 then '日开'
		when BasicInfo.MinInvestDay <= 14 then '2-14天 周开为主'
		when BasicInfo.MinInvestDay <= 32 then '15-32天 月开为主'
		when BasicInfo.MinInvestDay <= 186 then '33-186天 半年开为主'
		when BasicInfo.MinInvestDay <= 370 then '187-370天 年开为主'
		when BasicInfo.MinInvestDay <= 800 then '371-800天 两年开为主'
		else '>800天'
	end as MinInvestTimeType,
		BasicInfo.InvestTerm,
		BasicInfo.InvestTermUnit,
		BasicInfo.BenchmarkMax,
		BasicInfo.BenchmarkMin,
		BasicInfo.OperationType,
		AssetAllocation.AssetValue,
		AssetAllocation.AssetPublDate,
		AssetAllocation.AssetPublDateIndex
from
		LC_InstiQualCoRe Insti
join 
	(
	SELECT
			*
	FROM
			FP_SecuMain T
	WHERE
		-- 银行理财
		T.SecuCategory = 'FCC0000001TD'
		) SecuMain on
		Insti.CompanyCode = SecuMain.CompanyCode
left join 
    (
	select
			*,
			CASE
				when MinInvestTermUnit is null
				or MinInvestTerm is null then -1
				when MinInvestTermUnit = 'FCC0000001S9' then MinInvestTerm
				when MinInvestTermUnit = 'FCC0000001TC' then MinInvestTerm * 7
				when MinInvestTermUnit = 'FCC0000001S8' then MinInvestTerm * 30
				when MinInvestTermUnit = 'FCC0000001S7' then MinInvestTerm * 365
				else -1
			end as MinInvestDay
		from
				FP_BasicInfo 
		) BasicInfo ON
		SecuMain.FinProCode = BasicInfo.FinProCode
left join (
	select
		FinProCode,
		InfoPublDate as AssetPublDate,
		MarketValue as AssetValue,
		ROW_NUMBER() over(PARTITION by FinProCode
	ORDER BY
		InfoPublDate DESC) as AssetPublDateIndex
	from
		FP_AssetAllocation
	where
		-- 金融产品净资产合计
		AssetTypeCode = 'FCC0000001X9') AssetAllocation
		on
	SecuMain.FinProCode = AssetAllocation.FinProCode
where
	-- 商业银行理财子公司
	Insti.QualCode = 2029
	-- 募集期和存续期
	and SecuMain.SecuState IN ('FCC0000001TF', 'FCC0000001TG')
	-- 公募
	and BasicInfo.RaisingType = 'FCC0000001T2'
	-- 开放净值型
	and BasicInfo.OperationType = 'FCC0000001T6'
	-- 固收类
	and BasicInfo.InvestmentType = 'FCC0000001T8'
	-- 取最新的金融产品净资产 或 没有资产信息
	and (AssetAllocation.AssetPublDateIndex = 1 or AssetAllocation.AssetPublDateIndex is null)


	
	
-- 最新的产品信息
-- 明天增加存续期 筛选 

select distinct T.AgentName from (
	SELECT
	DISTINCT D.ChiName,
	E.QualName,
	A.AgentName,
	B.FinProCode,
	B.ChiName as product_name,
	G.ChiName as SecuState_name,
	I.ChiName as RaisingType,
	H.ChiName as OperationType,
	J.ChiName as InvestmentType
FROM
	(select * from LC_InstiQualCoRe  where QualCode = 2029)A   -- 商业银行理财子公司
FULL JOIN (SELECT * FROM FP_SecuMain T WHERE T.SecuCategory = 'FCC0000001TD') B ON  --  银行理财
	B.CompanyCode = A.CompanyCode
FULL JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
FULL JOIN LC_InstiArchive D ON
	D.CompanyCode = C.ParentCompany
FULL JOIN LC_InstiQualCoRe E on
	D.CompanyCode = E.CompanyCode 
FULL JOIN FP_BasicInfo F on 
	B.FinProCode = F.FinProCode
FULL JOIN FP_Indicator G on  
	B.SecuState = G.GilCode
FULL JOIN FP_Indicator H on 
	F.OperationType = H.GilCode
FULL JOIN FP_Indicator I on
	F.RaisingType = I.GilCode 
FULL JOIN FP_Indicator J on 
	F.InvestmentType = J.GilCode 
--WHERE 
	--A.QualCode = 2029  -- 商业银行理财子公司
	and E.QualCode in (2004,2007,2008,2015,2029) -- 规定母公司类别  城商行、国有行、外资合营的划分等
	and B.SecuState in ('FCC0000001TF','FCC0000001TG') -- 募集期和存续期
	and F.PopularizeStDate>='20180801'  -- 销售起始日 
	
	--and A.AgentName ='工银理财有限责任公司'
	--and H.ChiName = '开放式净值型'
	--and J.ChiName  = '固定收益类'
	) T 

select * 

-- 公司层面统计（查询有多少家理财子公司 ）
	SELECT
	DISTINCT
	A.AgentName as CompanyName ,
	D.ChiName as ParentCompName,
	E.QualName as ParentCompType,
	C.EstablishmentDate ,
	B.FinProCode ,
	B.ChiName as product_name,
	G.ChiName as SecuState,
	F.PopularizeStDate,
	F.EstablishmentDate as product_establish_date,
	CASE
		when F.MinInvestDay is null
		or F.MinInvestDay = -1 then '数据缺失'
		when F.MinInvestDay = 1 then '日开'
		when F.MinInvestDay <= 14 then '周开'
		when F.MinInvestDay <= 32 then '月开'
		when F.MinInvestDay <= 186 then '半年开'
		when F.MinInvestDay <= 370 then '年开'
		when F.MinInvestDay <= 800 then '两年开'
		else '超过两年'
	end as MinInvestTimeType,
	I.ChiName as RaisingType,
	H.ChiName as OperationType,
	J.ChiName as InvestmentType,
	AssetAllocation.EndDate,
	case 
	when AssetAllocation.AssetValue is not null 
		then AssetAllocation.AssetValue
	else F.ActRaisingAmount * 100000000
	end as AssetValue,
	AssetAllocation.AssetPublDateIndex,
	case 
	when CodeRelationship.FinProCode is not null then '子产品'
	when RelatedCodeRelationship.RelatedFinProCode is not null then '母产品'
	when CodeRelationship_fenqi.FinProCode is not null then '分期产品'
	when CodeRelationship_fenqixian.FinProCode is not null then '分期限产品'
	else '产品'
	end as ProductType
FROM
		(select * from LC_InstiQualCoRe  
			where QualCode = 2029) A   -- 商业银行理财子公司
left JOIN (SELECT * FROM FP_SecuMain  
		    WHERE SecuCategory = 'FCC0000001TD'
		    ) B ON
	B.CompanyCode = A.CompanyCode
left JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
left JOIN LC_InstiArchive D ON
	D.CompanyCode = C.ParentCompany
left JOIN (select * from LC_InstiQualCoRe 
	where QualCode in (2004,2007,2008,2015,2029)
	)E -- 规定母公司类别  城商行、国有行、外资合营的划分等 
	on D.CompanyCode = E.CompanyCode 
left JOIN (select
			*,
			CASE
				when MinInvestTermUnit is null
				or MinInvestTerm is null then -1
				when MinInvestTermUnit = 'FCC0000001S9' then MinInvestTerm
				when MinInvestTermUnit = 'FCC0000001TC' then MinInvestTerm * 7
				when MinInvestTermUnit = 'FCC0000001S8' then MinInvestTerm * 30
				when MinInvestTermUnit = 'FCC0000001S7' then MinInvestTerm * 365
				else -1
			end as MinInvestDay
		from
				FP_BasicInfo ) F on 
	B.FinProCode = F.FinProCode
left JOIN FP_Indicator G on  
	B.SecuState = G.GilCode
left JOIN FP_Indicator H on 
	F.OperationType = H.GilCode
left JOIN FP_Indicator I on
	F.RaisingType = I.GilCode 
left JOIN FP_Indicator J on 
	F.InvestmentType = J.GilCode
left join
	(select
		FinProCode,
		EndDate as EndDate,
		MarketValue as AssetValue,
		ROW_NUMBER() over(PARTITION by FinProCode
	ORDER BY
		InfoPublDate DESC) as AssetPublDateIndex
	from
		FP_AssetAllocation 
	where
		-- 金融产品净资产合计
		AssetTypeCode = 'FCC0000001X9' 
		-- 非空的市值
		and MarketValue is not null
	) AssetAllocation on 
	AssetAllocation.FinProCode = B.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine in ('FCC000000YDC','FCC000001E0I')) CodeRelationship
		on B.FinProCode = CodeRelationship.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine in ('FCC000000YDC','FCC000001E0I')) RelatedCodeRelationship
		on B.FinProCode = RelatedCodeRelationship.RelatedFinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine  ='FCC000000YDD') CodeRelationship_fenqi
		on B.FinProCode = CodeRelationship_fenqi.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine ='FCC00000129X') CodeRelationship_fenqixian
		on B.FinProCode = CodeRelationship_fenqixian.FinProCode
where (AssetAllocation.AssetPublDateIndex = 1 or
      AssetAllocation.AssetPublDateIndex is null)
     


--WHERE 
	--A.QualCode = 2029  -- 商业银行理财子公司
	--and E.QualCode in (2004,2007,2008,2015,2029) -- 规定母公司类别  城商行、国有行、外资合营的划分等
	--and B.SecuState in ('FCC0000001TF','FCC0000001TG') -- 募集期和存续期
	--and F.PopularizeStDate>='20180801'  -- 销售起始日 
	

	
-- 发行产品数量统计（查询有多少家理财子公司 ）

	SELECT
	DISTINCT
	A.AgentName as CompanyName ,
	D.ChiName as ParentCompName,
	E.QualName as ParentCompType,
	C.EstablishmentDate ,
	B.FinProCode ,
	B.ChiName as product_name,
	F.PopularizeStDate,
	F.EstablishmentDate as product_establish_date,
	YEAR(F.EstablishmentDate),
	case 
	when CodeRelationship.FinProCode is not null then '子产品'
	when RelatedCodeRelationship.RelatedFinProCode is not null then '母产品'
	when CodeRelationship_fenqi.FinProCode is not null then '分期产品'
	when CodeRelationship_fenqixian.FinProCode is not null then '分期限产品'
	else '产品'
	end as ProductType
FROM
		(select * from LC_InstiQualCoRe  
			where QualCode = 2029) A   -- 商业银行理财子公司
left JOIN (SELECT * FROM FP_SecuMain  
		    WHERE SecuCategory = 'FCC0000001TD'
		    ) B ON
	B.CompanyCode = A.CompanyCode
left JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
left JOIN LC_InstiArchive D ON
	D.CompanyCode = C.ParentCompany
left JOIN (select * from LC_InstiQualCoRe 
	where QualCode in (2004,2007,2008,2015,2029)
	)E -- 规定母公司类别  城商行、国有行、外资合营的划分等 
	on D.CompanyCode = E.CompanyCode 
left join (select * from FP_CodeRelationship
			where CodeDefine in ('FCC000000YDC','FCC000001E0I')) CodeRelationship
		on B.FinProCode = CodeRelationship.FinProCode
left join FP_BasicInfo  F on 
	B.FinProCode = F.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine in ('FCC000000YDC','FCC000001E0I')) RelatedCodeRelationship
		on B.FinProCode = RelatedCodeRelationship.RelatedFinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine  ='FCC000000YDD') CodeRelationship_fenqi
		on B.FinProCode = CodeRelationship_fenqi.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine ='FCC00000129X') CodeRelationship_fenqixian
		on B.FinProCode = CodeRelationship_fenqixian.FinProCode

		
		
-- 统计发行数量 
select CompanyName,count(*)as juyuan_num from (
SELECT
	DISTINCT
	A.AgentName as CompanyName ,
	C.EstablishmentDate ,
	B.FinProCode ,
	B.SecuCode,
	B.ChiName as product_name,
	F.RegistrationCode,
	F.PopularizeStDate,
	F.EstablishmentDate as product_establish_date
	FROM
		(select * from LC_InstiQualCoRe  
			where QualCode = 2029) A   -- 商业银行理财子公司
left JOIN (SELECT * FROM FP_SecuMain  
		    WHERE SecuCategory = 'FCC0000001TD'
		    ) B ON
	B.CompanyCode = A.CompanyCode
left JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
left JOIN LC_InstiArchive D ON
	D.CompanyCode = C.ParentCompany
left JOIN (select * from LC_InstiQualCoRe 
	where QualCode in (2004,2007,2008,2015,2029)
	)E -- 规定母公司类别  城商行、国有行、外资合营的划分等 
	on D.CompanyCode = E.CompanyCode 
left join (select * from FP_CodeRelationship
			where CodeDefine in ('FCC000000YDC','FCC000001E0I')) CodeRelationship
		on B.FinProCode = CodeRelationship.FinProCode
left join FP_BasicInfo  F on 
	B.FinProCode = F.FinProCode
where F.EstablishmentDate >= '20220101'
and F.EstablishmentDate <='20220926'
and A.AgentName = '建信理财有限责任公司'
and B.SecuCode = 'JXCXDYHH211201004')T
group by CompanyName

select distinct AgentName from LC_InstiQualCoRe  
where QualCode = 2029

	    
select A.AgentName as company,
	C.FinProCode,
	B.ChiName as product_name,
	C.EstablishmentDate as product_establish_date,
	YEAR(C.EstablishmentDate) as est_date_year,
	C.PopularizeStDate
from LC_InstiQualCoRe   A
join dbo.FP_SecuMain B
on A.CompanyCode = B.CompanyCode
join dbo.FP_BasicInfo C 
on B.FinProCode = C.FinProCode
where A.AgentName = '广银理财有限责任公司'
	and C.EstablishmentDate> ='20220101'
	and C.EstablishmentDate< ='20220926'
	
	
--查看净值--
select 
	FinProCode,
	AccumulatedUnitNV
from dbo.FP_NetValue fnv 
where FinProCode  in (	SELECT
	DISTINCT 
	B.FinProCode
FROM
	LC_InstiQualCoRe A
FULL JOIN (SELECT * FROM FP_SecuMain T WHERE T.SecuCategory = 'FCC0000001TD') B ON  --  银行理财
	B.CompanyCode = A.CompanyCode
JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
JOIN LC_InstiArchive D ON
	D.CompanyCode = C.ParentCompany
join LC_InstiQualCoRe E on
	D.CompanyCode = E.CompanyCode 
join FP_BasicInfo F on 
	B.FinProCode = F.FinProCode
join FP_Indicator G on  
	B.SecuState = G.GilCode
join FP_Indicator H on 
	F.OperationType = H.GilCode
join FP_Indicator I on
	F.RaisingType = I.GilCode 
join FP_Indicator J on 
	F.InvestmentType = J.GilCode 
WHERE 
	A.QualCode = 2029  -- 商业银行理财子公司
	and E.QualCode in (2004,2007,2008,2015,2029) -- 规定类别  城商行、国有行、外资合营的划分等
	and B.SecuState in ('FCC0000001TF','FCC0000001TG') -- 募集期和存续期
	and F.EstablishmentDate>='20220101'  
	and A.AgentName = '广银理财有限责任公司'


	
	select A.FinProCode,A.EndDate,A.UnitNV ,A.UnitNVRestored ,B.AccumulatedUnitNV from dbo.FP_NetValueRe  A
	full join dbo.FP_NetValue B
	on A.FinProCode = B.FinProCode
	where A.FinProCode ='SEC00003593O'
	
	select * from FP_NetValue
	where FinProCode ='SEC00003593O'   -- 上银理财复权净值出问题的表

	
select top 10 * from dbo.FP_SecuMain 
where ChiName = '广银理财有限责任公司'

	
select count(*) from dbo.FP_AssetAllocation
 
select count(*) from dbo.FP_PortfolioDetails


select * from dbo.FP_AssetAllocation

select * from dbo.FP_PortfolioDetails

select * from dbo.FP_Indicator

select * from dbo.FP_BasicInfo

select * from dbo.FP_SecuMain

-- 查看是否含有某个产品 

SELECT * FROM FP_SecuMain A 
left JOIN (SELECT * FROM FP_SecuMain  
		    WHERE SecuCategory = 'FCC0000001TD'
		    ) B ON
	B.CompanyCode = A.CompanyCode
where  B.ChiName = '建信理财私行专享“恒星”多元配置混合类最低持有18个月产品'


SELECT * FROM FP_SecuMain  
where   ChiName like '%恒星%'


-- 公司层面统计（查询有多少家理财子公司 ）
	SELECT
	DISTINCT
	A.AgentName as CompanyName ,
	case 
	when A.QualCode = 2004 then '城市商业银行'
	when A.QualCode = 2015 then '农村商业银行'
	else '其他'
	end as bank_type,
	C.EstablishmentDate ,
	B.FinProCode ,
	B.ChiName as product_name,
	G.ChiName as SecuState,
	F.PopularizeStDate,
	F.EstablishmentDate as product_establish_date,
	AssetAllocation.EndDate,
	case 
	when AssetAllocation.AssetValue is not null 
		then AssetAllocation.AssetValue
	else F.ActRaisingAmount * 100000000
	end as AssetValue,
	AssetAllocation.AssetPublDateIndex,
	case 
	when CodeRelationship.FinProCode is not null then '子产品'
	when RelatedCodeRelationship.RelatedFinProCode is not null then '母产品'
	when CodeRelationship_fenqi.FinProCode is not null then '分期产品'
	when CodeRelationship_fenqixian.FinProCode is not null then '分期限产品'
	else '产品'
	end as ProductType
FROM (select * from LC_InstiQualCoRe  
			where QualCode  in (2004,2015)) A   -- 城农商行
left JOIN (SELECT * FROM FP_SecuMain  
		    WHERE SecuCategory = 'FCC0000001TD'
		    ) B ON
	B.CompanyCode = A.CompanyCode
left JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
left JOIN FP_BasicInfo  F on 
	B.FinProCode = F.FinProCode
left JOIN FP_Indicator G on  
	B.SecuState = G.GilCode
left join
	(select
		FinProCode,
		EndDate as EndDate,
		MarketValue as AssetValue,
		ROW_NUMBER() over(PARTITION by FinProCode
	ORDER BY
		InfoPublDate DESC) as AssetPublDateIndex
	from
		FP_AssetAllocation 
	where
		-- 金融产品净资产合计
		AssetTypeCode = 'FCC0000001X9' 
		-- 非空的市值
		and MarketValue is not null
	) AssetAllocation on 
	AssetAllocation.FinProCode = B.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine in ('FCC000000YDC','FCC000001E0I')) CodeRelationship
		on B.FinProCode = CodeRelationship.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine in ('FCC000000YDC','FCC000001E0I')) RelatedCodeRelationship
		on B.FinProCode = RelatedCodeRelationship.RelatedFinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine  ='FCC000000YDD') CodeRelationship_fenqi
		on B.FinProCode = CodeRelationship_fenqi.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine ='FCC00000129X') CodeRelationship_fenqixian
		on B.FinProCode = CodeRelationship_fenqixian.FinProCode
where (AssetAllocation.AssetPublDateIndex = 1 or
      AssetAllocation.AssetPublDateIndex is null)


      
      

-- 输入一个产品代码 获取基本信息
 
select distinct FinProCode from dbo.FP_BasicInfo 
where RiskLevelCode ='FCC0000001ST'
and SecuCategory ='FCC0000001TD'

select DISTINCT ChiName from dbo.FP_BasicInfo 
join dbo.FP_Indicator 
on FP_BasicInfo.InvestTermUnit = FP_Indicator.GilCode



SELECT CodeDefine 代码关联方式,RelatedFinProCode 主产品,FinProCode 子产品 FROM FP_CodeRelationshiP
where RelatedFinProCode = 'SEC00003JDSP'




---分期关联-FCC000000YDD
SELECT CodeDefine 代码关联方式,RelatedFinProCode 主产品,FinProCode 子产品 FROM FP_CodeRelationship
  WHERE RelatedFinProCode='SEC00003EH32'
SELECT B.RegistrationCode 登记编码,A.ChiName 产品名称,A.FinProCode,B.EstablishmentDate 成立日,B.MaturityDate 到期日,B.ActMaturityDate 实际到期日 FROM FP_SecuMain A
  LEFT JOIN FP_BasicInfo B ON A.FinProCode=B.FinProCode
  WHERE A.FinProCode IN ('SEC00003EH32','SEC00007GANQ','SEC00003EH36','SEC00003JL66','SEC00007GANN','SEC00007GUN8','SEC00007HTIY')
  ORDER BY B.EstablishmentDate DESC
 
--母子产品份额关联-FCC000000YDC（指银行给出母产品代码，该母产品无份额、但是会有加权过的净值等信息，我们选择该母产品作为主产品去关联其他份额）
SELECT CodeDefine 代码关联方式,RelatedFinProCode 主产品,FinProCode 子产品 FROM FP_CodeRelationship
  WHERE RelatedFinProCode='SEC00007FYKB'
SELECT B.RegistrationCode 登记编码,A.ChiName 产品名称, A.FinProCode,* FROM FP_SecuMain A
  LEFT JOIN FP_BasicInfo B ON A.FinProCode=B.FinProCode
  WHERE A.FinProCode IN ('SEC00007FYKB','SEC00007FYKL','SEC00007FYKR')
 
--同一产品份额关联-FCC000001E0I（指银行未给出母产品代码，我们选取原始份额作为主产品去关联其他份额）
SELECT CodeDefine 代码关联方式,RelatedFinProCode 主产品,FinProCode 子产品 FROM FP_CodeRelationship
  WHERE RelatedFinProCode='SEC00007649R'
SELECT B.RegistrationCode 登记编码,A.ChiName 产品名称, A.FinProCode,* FROM FP_SecuMain A
  LEFT JOIN FP_BasicInfo B ON A.FinProCode=B.FinProCode
  WHERE A.FinProCode IN ('SEC00007649R','SEC00007H8TO')

  SELECT CodeDefine 代码关联方式,RelatedFinProCode 主产品,FinProCode 子产品 FROM FP_CodeRelationship
  where CodeDefine ='FCC00000129X'
  
  SELECT B.RegistrationCode 登记编码,A.ChiName 产品名称, A.FinProCode,* FROM FP_SecuMain A
  LEFT JOIN FP_BasicInfo B ON A.FinProCode=B.FinProCode
  WHERE A.FinProCode IN ('SEC000076Q4F','SEC00003KC23','SEC000075NCS','SEC0000766VY')
  
  SELECT CodeDefine 代码关联方式,RelatedFinProCode 主产品,FinProCode 子产品 FROM FP_CodeRelationship
  where RelatedFinProCode ='SEC00007FZI1'

  
    SELECT B.RegistrationCode 登记编码,A.ChiName 产品名称, A.FinProCode,* FROM FP_SecuMain A
  LEFT JOIN FP_BasicInfo B ON A.FinProCode=B.FinProCode
  WHERE A.FinProCode IN ('SEC00007FZI1','SEC00007G8SB','SEC00007GUV4','SEC00007H7U9','SEC00007HU5Z')
  
  
  -- 分期产品也不能要 徽银理财的产品 
  select * from dbo.FP_AssetAllocation faa 
  where FinProCode IN ('SEC00007FZI1','SEC00007G8SB','SEC00007GUV4','SEC00007H7U9','SEC00007HU5Z')
  and InfoSource ='半年度投资管理报告'
  
  
  select * from EP_CompanyMain
  where EnterpriseCode='ETP0001AYIE5'
  
    select count(*) from LC_InstiArchive

select distinct InfoSource from  FP_AssetAllocation

select distinct t.InfoSource from (
select b.ChiName ,c.ChiName as comp_name,a.* from  FP_AssetAllocation a
left join dbo.FP_SecuMain b
on a.FinProCode = b.FinProCode
join dbo.LC_InstiArchive c
on b.CompanyCode = c.CompanyCode 
join LC_InstiQualCoRe  d
on c.CompanyCode = d.CompanyCode
where 
--a.InfoSource ='半年度报告'
 b.SecuCategory ='FCC0000001TD'
and d.QualCode =2029 
and a.EndDate >'20220101')t

  
 select distinct t.InfoSource from (
select b.ChiName ,c.ChiName as comp_name,a.* from  FP_AssetAllocation a
left join dbo.FP_SecuMain b
on a.FinProCode = b.FinProCode
join dbo.LC_InstiArchive c
on b.CompanyCode = c.CompanyCode 
join LC_InstiQualCoRe  d
on c.CompanyCode = d.CompanyCode
where 
a.InfoSource ='定期报告'
and a.EndDate ='2022-06-30'
and b.SecuCategory ='FCC0000001TD'
and d.QualCode =2029 
and a.EndDate >'20220101'
--and a.FinProCode ='SEC00003G480'
)t
  



SELECT
	DISTINCT
	A.AgentName as CompanyName ,
	C.EstablishmentDate ,
	B.FinProCode ,
	B.ChiName as product_name,
	G.ChiName as SecuState,
	F.PopularizeStDate,
	F.EstablishmentDate as product_establish_date,
	H.ChiName as InvestmentType ,
	case 
	when CodeRelationship.FinProCode is not null then '子产品'
	when RelatedCodeRelationship.RelatedFinProCode is not null then '母产品'
	when CodeRelationship_fenqi.FinProCode is not null then '分期产品'
	when CodeRelationship_fenqixian.FinProCode is not null then '分期限产品'
	else '产品'
	end as ProductType
	FROM (select * from LC_InstiQualCoRe  
			where QualCode=2029) A   -- 银行理财子产品 
left JOIN (SELECT * FROM FP_SecuMain  
		    WHERE SecuCategory = 'FCC0000001TD'
		    ) B ON
B.CompanyCode = A.CompanyCode
left JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
left JOIN FP_BasicInfo  F on 
	B.FinProCode = F.FinProCode
left JOIN FP_Indicator G on  
	B.SecuState = G.GilCode
left JOIN FP_Indicator H on  
	F.InvestmentType = H.GilCode
left join (select * from FP_CodeRelationship
			where CodeDefine in ('FCC000000YDC','FCC000001E0I')) CodeRelationship
		on B.FinProCode = CodeRelationship.FinProCode
left join (select * from FP_CodeRelationship
	where CodeDefine in ('FCC000000YDC','FCC000001E0I')) RelatedCodeRelationship
		on B.FinProCode = RelatedCodeRelationship.RelatedFinProCode
left join (select * from FP_CodeRelationship
where CodeDefine  ='FCC000000YDD') CodeRelationship_fenqi
		on B.FinProCode = CodeRelationship_fenqi.FinProCode
left join (select * from FP_CodeRelationship
			where CodeDefine ='FCC00000129X') CodeRelationship_fenqixian
on B.FinProCode = CodeRelationship_fenqixian.FinProCode  

select distinct b.ChiName from dbo.FP_PortfolioDetails fpd 
left join dbo.FP_Indicator  b
on fpd.InvestObject = b.GilCode 


-- 查看名称 
select  a.ChiName ,fbi.* from dbo.FP_BasicInfo fbi 
join dbo.FP_SecuMain a
on fbi.FinProCode = a.FinProCode 
where a.FinProCode ='SEC0000363GH'
and fbi.CurrencyUnit !='FCC000000015'

select distinct CurrencyUnit  from dbo.FP_BasicInfo fbi 


where InvestObject like '%非标%'


-- 检查 复权净值问题 

select  * from dbo.FP_NetValueRe fnvr 
where updatetime >'2022-10-20'

where finprocode= 'SEC0000363GH'



select  * from dbo.FP_NetValueRe fnvr 
where UnitNv is not null and UnitNVRestored is NULL  
and updatetime >'2022-10-20'


select *from dbo.FP_NetValue fnv 
where finprocode = 'SEC0000363GH'
order by enddate

-------------------------  bank_wealth_product ------------------------------ 
DECLARE @code date
set @code= '2022-12-31'
SELECT
	DISTINCT A.AgentName as CompanyName,
	D.ChiName as ParentCompName,
	E.QualName as ParentCompType,
	C.EstablishmentDate,
	B.FinProCode ,
	B.ChiName as product_name,
	G.ChiName as SecuState,
	F.PopularizeStDate,
	case
		when F.MinInvestDay is null
		or F.MinInvestDay = -1 or F.OperationType is null  then '数据缺失'
		when (F.OperationType = 'FCC0000001T4') and (F.MinInvestDay <= 370) then '封闭短期'
		when (F.OperationType = 'FCC0000001T4') and (F.MinInvestDay > 370) and (F.MinInvestDay <= 1105)  then '封闭中期'
		when (F.OperationType = 'FCC0000001T4') and (F.MinInvestDay > 1105)  then '封闭长期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay <= 31)   then '开放短期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay > 31) and (F.MinInvestDay <= 93)  then '开放短中期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay > 93) and (F.MinInvestDay <= 186)  then '开放中期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay > 186) and (F.MinInvestDay <= 370)  then '开放中长期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay > 370)   then '开放长期'
		else '其他'
	end as MinInvestTimeType,
	H.ChiName as RaisingType,
	I.ChiName as OperationType,
	J.ChiName as InvestmentType,
	COALESCE(AssetAllocation.EndDate,net_value_nv.EndDate) as EndDate,
	case
		when AssetAllocation.AssetValue is not null then AssetAllocation.AssetValue
		when net_value_nv.NV is not null  then net_value_nv.NV
		else F.ActRaisingAmount * 100000000
	end as AssetValue,
	AssetAllocation.AssetPublDateIndex,
	case
		when CodeRelationship.FinProCode is not null then '子产品'
		when RelatedCodeRelationship.RelatedFinProCode is not null then '母产品'
		when CodeRelationship_fenqi.FinProCode is not null then '分期产品'
		when CodeRelationship_fenqixian.FinProCode is not null then '分期限产品'
		else '产品'
	end as ProductType,
	F.EstablishmentDate as product_establish_date,
	K.ChiName as CurrencyUnit,
	B.SecuAbbr,
	F.MinInvestTerm,
	L.ChiName as MinInvestTermUnit,
	M.ChiName as RiskLevel,
	F.BenchmarkMax,
	F.BenchmarkMin,
	F.IssueObject,
	fee.manage_fee,
	fee.manage_fee_unit,
	fee.carry_fee,
	fee.carry_fee_unit,
	case 
		when  F.ActMaturityDate is not null then  F.ActMaturityDate
		else  F.MaturityDate 
	end as MaturityDate,
	case
	when F.InvestmentType = 'FCC0000001T8' then 
		case 
			when B.ChiName like '%现金%' then 1
			else 
				case 
					when F.MinInvestDay = 1 then 
						case 
							when A.AgentName = '中银理财有限责任公司' and B.ChiName like '%乐享%' then 1 
							when A.AgentName = '建信理财有限责任公司' and (B.ChiName like '%龙宝%' or 
							B.ChiName like '%建信宝%' or 
							B.ChiName like '%安鑫%' or 
							B.ChiName like '%恒赢%' or
							B.ChiName like '%净鑫%' or
							B.ChiName like '%净利%' or 
							B.ChiName like '%天天利%' )  then 1
							when A.AgentName = '交银理财有限责任公司' and (B.ChiName like '%现金添利%' or 
							B.ChiName like '%悦享%' ) then 1 
							when A.AgentName = '农银理财有限责任公司' and B.ChiName like '%时时付%' then 1 
							when A.AgentName = '工银理财有限责任公司' and B.ChiName like '%添利宝%' then 1 
							when A.AgentName = '光大理财有限责任公司' and B.ChiName like '%阳光碧%' then 1 
							when A.AgentName = '招银理财有限责任公司' and (B.ChiName like '%日日欣%' or 
							B.ChiName like '%朝招金%' or 
							B.ChiName like '%开鑫宝%' ) then 1 
							when A.AgentName = '兴银理财有限责任公司' and B.ChiName like '%添利%' then 1 
							when A.AgentName = '杭银理财有限责任公司' and (B.ChiName like '%新钱包%' or
							B.ChiName like '%金钱包%' or 
							B.ChiName like '%臻钱包%' ) then 1 
							when A.AgentName = '宁银理财有限责任公司' and( B.ChiName like '%宁欣天天鎏金%' or 
							B.ChiName like '%天利鑫%' ) then 1 
							when A.AgentName = '徽银理财有限责任公司' and B.ChiName like '%天天盈%' then 1 
							when A.AgentName = '南银理财有限责任公司' and B.ChiName like '%添睿%' then 1 
							when A.AgentName = '苏银理财有限责任公司' and B.ChiName like '%启源%' then 1 
							when A.AgentName = '平安理财有限责任公司' and B.ChiName like '%天天成长%' then 1 
							when A.AgentName = '青银理财有限责任公司' and B.ChiName like '%奋斗%' then 1 
							when A.AgentName = '渝农商理财有限责任公司' and B.ChiName like '%渝快宝%'  then 1 
							when A.AgentName = '信银理财有限责任公司' and B.ChiName like '%日盈象%' then 1
							when A.AgentName = '广银理财有限责任公司' and B.ChiName like '%鎏金%' then 1 
							when A.AgentName = '民生理财有限责任公司' and B.ChiName like '%天天增利%' then 1
							when A.AgentName = '恒丰理财有限责任公司' and B.ChiName like '%新恒梦钱包%' then 1 
							when A.AgentName = '中邮理财有限责任公司' and (B.ChiName like '%零钱宝%' or 
							B.ChiName like '%理财宝%') then 1 
							else 0 
						end 
					else 0 
				end
			end  
 		else 0 
 	end as inv_type,
F.RegistrationCode,
lever.lever_date,
lever.leverage,
manager.ChiName as manage_comp,
F.MinInvestDay,
fi.ChiName as IfStructure,
F.InvestTerm,
F.InvestTermUnit,
F.ActRaisingAmount * 100000000 as ActRaisingAmount
FROM
	(
	select
		*
	from
		LC_InstiQualCoRe
	where
		QualCode in (2029)) A
	-- 银行理财子
left JOIN (
	SELECT
		*
	FROM
		FP_SecuMain
	WHERE
		SecuCategory = 'FCC0000001TD' ) B ON
	B.CompanyCode = A.CompanyCode
left JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
left join LC_InstiArchive D on
	D.CompanyCode = C.ParentCompany
left JOIN (
	select
		*
	from
		LC_InstiQualCoRe
	where
		QualCode in (2004, 2007, 2008, 2015, 2029) )E
	-- 规定母公司类别  城商行、国有行、外资合营的划分等 
 on
	D.CompanyCode = E.CompanyCode
left JOIN (
	select
		*,
		CASE
			when MinInvestTermUnit is null
			or MinInvestTerm is null then -1
			when MinInvestTermUnit = 'FCC0000001S9' then MinInvestTerm
			when MinInvestTermUnit = 'FCC0000001TC' then MinInvestTerm * 7
			when MinInvestTermUnit = 'FCC0000001S8' then MinInvestTerm * 30
			when MinInvestTermUnit = 'FCC0000001S7' then MinInvestTerm * 365
			else -1
		end as MinInvestDay
	from
		FP_BasicInfo ) F on
	B.FinProCode = F.FinProCode
left JOIN FP_Indicator G on
	B.SecuState = G.GilCode
left JOIN FP_Indicator H on
	F.RaisingType = H.GilCode
left JOIN FP_Indicator I on
	F.OperationType = I.GilCode
left JOIN FP_Indicator J on
	F.InvestmentType = J.GilCode
left JOIN FP_Indicator K on
	F.CurrencyUnit = K.GilCode
left join FP_Indicator L on
	F.MinInvestTermUnit = L.GilCode
left join FP_Indicator M on
	F.RiskLevelCode = M.GilCode
left join (
	select
		COALESCE(manage.FinProCode,carry.FinProCode) as FinProCode, 
		carry.carry_fee, 
		carry.carry_fee_unit ,
		manage.manage_fee,
		manage.manage_fee_unit
		from
		(
		select * from (
		select
			FinProCode as FinProCode, ChargeRate as carry_fee, dd.ChiName as carry_fee_unit, ROW_NUMBER() over(PARTITION by FinProCode
		ORDER BY
			FP_ChargeRate.CancelDate DESC) as date_index
		from
			FP_ChargeRate
		left join dbo.FP_Indicator dd on
			FP_ChargeRate.ChargeRateUnit = dd.GilCode
		where
			FP_ChargeRate.ChargeRateType = 'FCC0000001RX'
			and FP_ChargeRate.ExcuteDate <= @code
			and FP_ChargeRate.CancelDate >= @code
			and FP_ChargeRate.ChargeRate is not null
			) carry_1
			where carry_1.date_index = 1) carry
	FULL join (
	select * from (
		select
			FinProCode, ChargeRate as manage_fee, ee.ChiName as manage_fee_unit, ROW_NUMBER() 
			over(PARTITION by FinProCode
		ORDER BY
			FP_ChargeRate.CancelDate DESC) as date_index
		from
			FP_ChargeRate
		left join dbo.FP_Indicator ee on
			FP_ChargeRate.ChargeRateUnit = ee.GilCode
		where
			FP_ChargeRate.ChargeRateType = 'FCC0000001RU'
			and FP_ChargeRate.ChargeRateInterval = 'FCC0000001SF'
		    and FP_ChargeRate.ExcuteDate <= @code
			and FP_ChargeRate.CancelDate >= @code)manage1
			where manage1.date_index = 1)  manage on
		manage.FinProCode = carry.FinProCode )fee on
	B.FinProCode = fee.FinProCode
left join (
	select
		FinProCode,AssetTypeCode, EndDate as EndDate, MarketValue as AssetValue, ROW_NUMBER() 
		over(PARTITION by FinProCode
	ORDER BY
		InfoPublDate desc,AssetTypeCode) as AssetPublDateIndex
	from
		(select * from FP_AssetAllocation
	where
		-- 金融产品净资产或者总资产
 AssetTypeCode in ('FCC0000001X9','FCC0000001XA')
		-- 非空的市值
		and MarketValue is not null 
		and EndDate <=@code)ttt) AssetAllocation on
	AssetAllocation.FinProCode = B.FinProCode
left join (
	select
		*
	from
		FP_CodeRelationship
	where
		CodeDefine in ('FCC000000YDC', 'FCC000001E0I')) CodeRelationship on
	B.FinProCode = CodeRelationship.FinProCode
left join (
	select
		*
	from
		FP_CodeRelationship
	where
		CodeDefine in ('FCC000000YDC', 'FCC000001E0I')) RelatedCodeRelationship on
	B.FinProCode = RelatedCodeRelationship.RelatedFinProCode
left join (
	select
		*
	from
		FP_CodeRelationship
	where
		CodeDefine = 'FCC000000YDD') CodeRelationship_fenqi on
	B.FinProCode = CodeRelationship_fenqi.FinProCode
left join (
	select
		*
	from
		FP_CodeRelationship
	where
		CodeDefine = 'FCC00000129X') CodeRelationship_fenqixian on
	B.FinProCode = CodeRelationship_fenqixian.FinProCode
left join ( 
	select FinProCode, EndDate as lever_date ,leverage from(
	select FinProCode ,EndDate ,leverage ,ROW_NUMBER() over(PARTITION by FinProCode
			ORDER BY
				c.EndDate DESC) as date_index
	from (
	select COALESCE (a.FinProCode,b.FinProCode) as FinProCode,
		   COALESCE (a.EndDate,b.EndDate) as EndDate,
		   all_value_sum / net_value_sum as leverage
	from (
	select FinProCode,EndDate,MarketValue as net_value_sum from dbo.FP_AssetAllocation
	where AssetTypeCode  = 'FCC0000001X9' and SecuCategory  = 'FCC0000001TD') a 
	join (
	select FinProCode,EndDate,MarketValue as  all_value_sum from dbo.FP_AssetAllocation  
	where AssetTypeCode  = 'FCC0000001XA' and SecuCategory = 'FCC0000001TD') b 
	on a.FinProCode  = b.FinProCode and a.EndDate = b.EndDate
	)c) t 
	where t.date_index = 1 
	) lever
	on B.FinProCode = lever.FinProCode
left join LC_InstiArchive manager
on B.CompanyCode  = manager.CompanyCode
left join FP_Indicator fi
on F.IfStructure = fi.GilCode
left join (select FinProCode,
	EndDate,
	NV from (
select
	FinProCode,
	EndDate,
	NV,
	ROW_NUMBER() over(PARTITION by FinProCode
order by
	EndDate desc ) as num
from
	dbo.FP_NetValue ) fnv
	where fnv.num = 1 
	and fnv.NV is not null)net_value_nv
on net_value_nv.FinProCode = B.FinProCode
where
	(AssetAllocation.AssetPublDateIndex = 1
	or AssetAllocation.AssetPublDateIndex is null)	
	
产品扣除理财产品总税费（包括但不限于产品应缴增值税、应付销售手续费、托管费、固定管理费等，
但不包括浮动管理费，下同）后，本产品年化收益率低于业绩基准（含），投资管理人不收取浮动管理费；
年化收益率超过业绩基准的部分，20%归客户所有，其余80%作为投资管理人的浮动管理费

 
 -- 富滇银行
 select LC_InstiArchive.ChiName,FP_SecuMain.FinProCode,
 AssetAllocation.EndDate,AssetAllocation.AssetValue,AssetAllocation.AssetPublDateIndex
 from dbo.FP_SecuMain 
 left join LC_InstiArchive 
 on FP_SecuMain.CompanyCode = LC_InstiArchive.CompanyCode
 left join (select
		FinProCode, EndDate as EndDate, MarketValue as AssetValue, 
		ROW_NUMBER() over(PARTITION by FinProCode
	ORDER BY
		InfoPublDate DESC) as AssetPublDateIndex
	from
		FP_AssetAllocation
	where
 AssetTypeCode = 'FCC0000001XA'
		-- 非空的市值
		and MarketValue is not null ) AssetAllocation on
	FP_SecuMain.FinProCode = AssetAllocation.FinProCode 
 where FP_SecuMain.CompanyCode = 2109
 and FP_SecuMain.SecuState = 'FCC0000001TG'
 
 and (AssetAllocation.AssetPublDateIndex = 1
	or AssetAllocation.AssetPublDateIndex is null)
 
 
	
	
 select * from LC_InstiArchive
 where CompanyCode =2109
 
 
 select * from dbo.FP_SecuMain fsm 
left join dbo.FP_NetValue fnv 
on fsm.FinProCode  = fnv.FinProCode 
where fsm.FinProCode ='SEC000036ZXD'
 
 and  AssetTypeCode = 'FCC0000001X9'
 
 
 -- 测试净值
select FinProCode,EndDate,UnitNV,
AccumulatedUnitNV,DailyProfit,LatestWeeklyYield,NV,* 
from FP_NetValue
where FinProCode ='SEC00007IFWL'
and EndDate >'2022-01-01'

 
-- 测试复权净值 
select * from dbo.FP_NetValueRe fnvr 
where FinProCode ='SEC0000376VN'

-- 测试联合净值和复权净值 
select t1.*,t2.UnitNVRestored from (select  FinProCode,EndDate,UnitNV,AccumulatedUnitNV,DailyProfit,LatestWeeklyYield 
from FP_NetValue
where FinProCode ='SEC000077688'
and EndDate >'2022-01-01') t1 
left join (select * from dbo.FP_NetValueRe fnvr 
where FinProCode ='SEC000077688')t2
on t1.EndDate = t2.EndDate 




--测试基本信息 

select ActRaisingAmount,RegistrationCode* from dbo.FP_BasicInfo fbi 
where FinProCode ='SEC000033QLE'
 
select InvestmentType,RegistrationCode from dbo.FP_BasicInfo fbi 
where fbi.RegistrationCode ='Z7001623A000022'

select * from dbo.FP_SecuMain fsm 
where FinProCode ='SEC00007IG12'
and 


-- 测试持仓 
select * from dbo.FP_AssetAllocation faa 
where FinProCode ='SEC00007GQYG'
order by EndDate desc

-- 测试产品存在
select * from dbo.FP_SecuMain fsm 
where ChiName like '%固收债权封闭式%'
 
 select * from dbo.FP_PortfolioDetails fpd 
 where FinProCode = 'SEC00003IXX5'
 
 select * from dbo.FP_SecuMain fsm 
 where FinProCode ='SEC0000779V5'
 
select * from dbo.FP_AssetAllocation faa 


-- 下载前十大持仓数据
select main.ChiName as 理财产品名称,
fpd.FinProCode as 理财产品代码,
fpd.EndDate as 报告日期,
fpd.SecuCode as 持仓标的代码,
fpd.SecuName as 持仓标的名称,
fpd.MarketValue as 持仓市值,
fpd.IfNonStandardAssets as 是否是非标,
fpd.RatioInNV as 持仓占比
from dbo.FP_PortfolioDetails fpd 
join dbo.FP_SecuMain main 
on fpd.FinProCode = main.FinProCode 
join  dbo.LC_InstiQualCoRe company
on main.CompanyCode = company.CompanyCode
where company.QualCode in (2029)
and fpd.EndDate = '2023-03-31'




and main.SecuCategory = 'FCC0000001TD'
and fpd.ReportType ='FCC000000YHK'

and fpd.PenetrationType = 'FCC0000019PL'


select * from dbo.FP_PortfolioDetails fpd 
where FinProCode ='SEC00002J7MR'
 

--- 下载净值数据 （理财子） 
select info.RegistrationCode as regis_code, net_value.* from (
select * from LC_InstiQualCoRe where QualCode in (2029)) LC
left join (SELECT * FROM FP_SecuMain WHERE SecuCategory = 'FCC0000001TD' ) main ON
	main.CompanyCode = LC.CompanyCode 
inner join (
select COALESCE(fnv.FinProCode,re.FinProCode) as FinProCode,
COALESCE(fnv.EndDate,re.EndDate) as EndDate,
fnv.UnitNV,fnv.AccumulatedUnitNV,fnv.DailyProfit,fnv.LatestWeeklyYield,
re.UnitNVRestored 
from dbo.FP_NetValue fnv
full join dbo.FP_NetValueRe re 
on fnv.FinProCode = re.FinProCode 
and fnv.EndDate = re.EndDate 
where fnv.EndDate >='2021-12-01'
and re.EndDate >= '2021-12-01') net_value
on main.FinProCode = net_value.FinProCode 
join dbo.FP_BasicInfo info 
on info.FinProCode = main.FinProCode 
 

-- 下载资产配置表 （20230331） 
select * from dbo.FP_SecuMain fsm   
left join (select * from LC_InstiQualCoRe where QualCode in (2029))lc
on fsm.CompanyCode = lc.

 
select * from dbo.FP_AssetAllocation  faa 
where FinProCode = 'SEC00003K6MF'
 

select *from dbo.FP_PortfolioDetails fpd 
where FinProCode = 'SEC00003K6MF'

select * from dbo.FP_NetValue fnv 
where FinProCode ='SEC000035ZO2'


select 
fsm.ChiName as prodcut_name,
fnv.* from dbo.LC_InstiArchive lia 
left join  dbo.FP_SecuMain fsm 
on lia.CompanyCode  = fsm.CompanyCode 
left join  dbo.FP_NetValue fnv 
on fsm.FinProCode  = fnv.FinProCode 
where lia.ChiName ='杭银理财有限责任公司' 
and fnv.EndDate >='20220101' 


select * from dbo.FP_NetValue fnv 
where FinProCode  ='SEC00007HOCR'

select
		FinProCode,AssetTypeCode, EndDate as EndDate, MarketValue as AssetValue, ROW_NUMBER() over(PARTITION by FinProCode
	ORDER BY
		InfoPublDate desc,AssetTypeCode) as AssetPublDateIndex
	from
		FP_AssetAllocation
	where
		-- 金融产品净资产或者总资产
 AssetTypeCode in ('FCC0000001X9','FCC0000001XA')
		-- 非空的市值
		and MarketValue is not null 
		and EndDate <='2022-06-30'
		and FinProCode ='SEC00007GTCN'
		
select * from (	
select FinProCode,InfoSource,EndDate ,count(*) as num from (
select * from dbo.FP_AssetAllocation faa 
where  AssetTypeCode in ('FCC0000001X9','FCC0000001XA'))t 
GROUP by FinProCode,InfoSource,EndDate)a
order by a.num desc



select * from dbo.FP_AssetAllocation faa 
where FinProCode ='SEC00003J1IN'
order by EndDate desc


select FinProCode,ChiName as manager from dbo.FP_BasicInfo fbi
left join EP_CompanyMain b 
on fbi.InvestAdvisorCode  = b.EnterpriseCode


where FinProCode ='SEC00003J1IN'

-- 验证青银净值 
SEC000077E2D  - 单位净值 
SEC00007G7Q0 - 单位净值 
SEC00007GES3
SEC00007GJBA
SEC00007GOW1
SEC00007GRP3
SEC00007GV4M
SEC00007GZ2W
SEC00007H3DU
SEC00007H92G
SEC00007HLVD
SEC00007HO9Y
SEC00007HR7M

select * from dbo.FP_NetValue fnv 
where FinProCode ='SEC000076LU9' 

select * from dbo.FP_AssetAllocation faa 
where FinProCode ='SEC00007H92G'

select * from dbo.FP_SecuMain fsm 
where ChiName  like '%青银理财%'

select * from dbo.FP_BasicInfo fbi 
where RegistrationCode ='Z7006622000063'

select * from dbo.FP_PortfolioDetails fpd 
where FinProCode ='SEC00002IX7O'and EndDate >='2022-06-30'





-- 中原银行
 select LC_InstiArchive.ChiName,FP_SecuMain.FinProCode,
 AssetAllocation.EndDate,AssetAllocation.AssetValue,AssetAllocation.AssetPublDateIndex
 from dbo.FP_SecuMain 
 left join LC_InstiArchive 
 on FP_SecuMain.CompanyCode = LC_InstiArchive.CompanyCode
 left join (select
		FinProCode,AssetTypeCode, EndDate as EndDate, MarketValue as AssetValue, ROW_NUMBER() over(PARTITION by FinProCode
	ORDER BY
		InfoPublDate desc,AssetTypeCode) as AssetPublDateIndex
	from
		FP_AssetAllocation
	where
		-- 金融产品净资产或者总资产
 AssetTypeCode in ('FCC0000001X9','FCC0000001XA')
		-- 非空的市值
		and MarketValue is not null 
		and EndDate <='2023-01-01' ) AssetAllocation on
	FP_SecuMain.FinProCode = AssetAllocation.FinProCode 
 where FP_SecuMain.CompanyCode = 3037
 and FP_SecuMain.SecuState = 'FCC0000001TG'
 and (AssetAllocation.AssetPublDateIndex = 1
	or AssetAllocation.AssetPublDateIndex is null)
 

select * from dbo.LC_InstiArchive
where ChiName like '%湖北银行%'

select* from dbo.FP_SecuMain fsm 
where ChiName like '%光证资管诚享%'

select * from dbo.FP_BasicInfo fbi 
where FinProCode ='SEC00007HW8S'

SELECT * FROM FP_FCAUM ORDER BY EndDate DESC


SELECT distinct comp.ChiName FROM FP_FCAssetAllocation compasset
left join LC_InstiArchive comp
on compasset.CompanyCode = comp.CompanyCode
where compasset.EndDate = '2022-12-31'

-- 公司维度信息 

select distinct ChiName from (
SELECT comp.ChiName ,cum.* FROM FP_FCAUM  cum
left join LC_InstiArchive comp
on cum.CompanyCode =comp.CompanyCode
where EndDate ='2022-12-31')t 


SELECT comp.ChiName ,EndDate, indi.ChiName as ProductCategory, cum.DataValue FROM FP_FCAUM  cum
left join LC_InstiArchive comp
on cum.CompanyCode =comp.CompanyCode
left join FP_Indicator indi
on cum.ProductCategory = indi.GilCode 
left join  FP_Indicator indi_2
on cum.IndiCategory = indi_2.GilCode
where EndDate ='2022-12-31'
and cum.BusinessCategory ='FCC000001E7Z' -- 存续
and cum.IndiCategory = 'FCC0000000MS' -- 数量


SELECT comp.ChiName ,EndDate, indi.ChiName as ProductCategory, cum.DataValue FROM FP_FCAUM  cum
left join LC_InstiArchive comp
on cum.CompanyCode =comp.CompanyCode
left join FP_Indicator indi
on cum.ProductCategory = indi.GilCode 
left join  FP_Indicator indi_2
on cum.IndiCategory = indi_2.GilCode
where EndDate ='2022-12-31'
and cum.BusinessCategory ='FCC000001E7Z' -- 存续
and cum.IndiCategory = 'FCC0000001BC' -- 金额


SELECT comp.ChiName ,EndDate, indi.ChiName as ProductCategory, cum.DataValue FROM FP_FCAUM  cum
left join LC_InstiArchive comp
on cum.CompanyCode =comp.CompanyCode
left join FP_Indicator indi
on cum.ProductCategory = indi.GilCode 
left join  FP_Indicator indi_2
on cum.IndiCategory = indi_2.GilCode
where EndDate ='2022-12-31'
and cum.BusinessCategory ='FCC000001E7Z' -- 存续
and cum.IndiCategory = 'FIC0000056B8' -- 金额占比



select distinct ChiName from (
SELECT comp.ChiName ,cum.* FROM FP_FCAssetAllocation cum
left join LC_InstiArchive comp
on cum.CompanyCode =comp.CompanyCode
where EndDate ='2022-12-31') a


SELECT comp.ChiName ,EndDate,indi_2.ChiName as PenetrationType,
indi.ChiName as AssetTypeCode, cum.AssetName,
cum.MarketValue,COALESCE (cum.RatioInNV,cum.RatioInTotalAsset)as raito FROM FP_FCAssetAllocation  cum
left join LC_InstiArchive comp
on cum.CompanyCode =comp.CompanyCode
left join FP_Indicator indi
on cum.AssetTypeCode = indi.GilCode 
left join  FP_Indicator indi_2
on cum.PenetrationType = indi_2.GilCode
where EndDate ='2022-12-31'

select * from FP_RelatedInstitutions
where AgentType ='FCC000001EA5'


-- 杠杆率 
FP_SecuMain.ChiName, 
FP_SecuMain.FinProCode,
FP_SecuMain.Sec

select 
LC_InstiQualCoRe.AgentName,
FP_SecuMain.ChiName, 
info.RegistrationCode,
FP_SecuMain.FinProCode,
indi.ChiName as SecuState,
FP_MainFinancialIndex.EndDate,
FP_MainFinancialIndex.LeverageRatio,
FP_MainFinancialIndex.LeverageRatioCalc
from FP_SecuMain 
left join  LC_InstiQualCoRe
on FP_SecuMain.CompanyCode = LC_InstiQualCoRe.CompanyCode
left join  FP_MainFinancialIndex
on FP_SecuMain.FinProCode = FP_MainFinancialIndex.FinProCode
left join dbo.FP_Indicator indi 
on FP_SecuMain.SecuState = indi.GilCode 
left join dbo.FP_BasicInfo info 
on FP_SecuMain.FinProCode = info.FinProCode
where FP_MainFinancialIndex.SecuCategory = 'FCC0000001TD'
and LC_InstiQualCoRe.QualCode = 2029
and FP_SecuMain


select dis from MF_FundsReference




-- 代销数据 
select
	SecuMain.FinProCode,
	SecuMain.SecuCode,
	SecuMain.ChiName,
	BasicInfo.RegistrationCode as '产品登记编码',
	BasicInfo.RaisingType,
	BasicInfo.InvestmentType,
	SecuMain.CompanyCode,
	InstiArchive.ChiName as '管理人',
	RelatedInstitutions.ConsignmentName as '代销机构',
	ConsignmentInstiArchive.ConsignmentType,
	RelatedInstitutions.StartDate,
	RelatedInstitutions.EndDate,
	RelatedInstitutions.SaleCode
from
	(
	select
		FinProCode,
		CompanyCode,
		SecuCode,
		ChiName
	from
		FP_SecuMain
	where
		-- 限制为银行理财
		SecuCategory = 'FCC0000001TD'
		and SecuState != 'FCC0000001TH') as SecuMain
left join 
(
	select
		FinProCode,
		RegistrationCode,
		CASE 
			when RaisingType = 'FCC0000001T2' then '公募'
			when RaisingType = 'FCC0000001T3' then '私募'
		END as RaisingType,
		CASE 
			when InvestmentType = 'FCC0000001T8' then '固定收益类'
			when InvestmentType = 'FCC0000001T9' then '权益类'
			when InvestmentType = 'FCC0000001TA' then '商品及金融衍生品类'
			when InvestmentType = 'FCC0000001TB' then '混合类'
			when InvestmentType = 'FCC0000014S4' then '流动性资产'
		END as InvestmentType
	from
		FP_BasicInfo) as BasicInfo on
	SecuMain.FinProCode = BasicInfo.FinProCode
left join 
(
	select
		CompanyCode,
		ChiName
	from
		LC_InstiArchive) as InstiArchive on
	SecuMain.CompanyCode = InstiArchive.CompanyCode
inner join
(
	select
		FinProCode,
		CompanyCode as ConsignmentCode,
		AgentName as ConsignmentName,
		StartDate,
		EndDate,
		SaleCode
	from
		FP_RelatedInstitutions
	where
		-- 限制为代销机构
		AgentType = 'FCC000001EA5'
		-- 数据有效
		and IfEffected = 'FCC000000005') as RelatedInstitutions on
	SecuMain.FinProCode = RelatedInstitutions.FinProCode
left join (
	select
		CompanyCode as ConsignmentCode,
		CASE 
			when CompanyType = 1110 then '综合类券商'
			when CompanyType = 1130 then '经纪类券商'
			when CompanyType = 1140 then '证券分公司'
			when CompanyType = 1150 then '证券营业部'
			when CompanyType = 1190 then '其他证券公司'
			when CompanyType = 1199 then '证券交易所'
			when CompanyType = 1300 then '信托投资公司'
			when CompanyType = 1301 then '信托担保人'
			when CompanyType = 1510 then '证券咨询公司'
			when CompanyType = 2100 then '基金管理公司'
			when CompanyType = 2101 then '证券投资基金'
			when CompanyType = 2110 then '基金分公司'
			when CompanyType = 3100 then '证券监管机构'
			when CompanyType = 3200 then '保险监管机构'
			when CompanyType = 3300 then '银行业监管机构'
			when CompanyType = 3400 then '银行保险监管机构'
			when CompanyType = 4110 then '保险公司'
			when CompanyType = 4120 then '保险分公司'
			when CompanyType = 4130 then '保险资产管理公司'
			when CompanyType = 4500 then '资产管理公司'
			when CompanyType = 4700 then '银行'
			when CompanyType = 4710 then '银行分行'
			when CompanyType = 4800 then '投资银行'
			when CompanyType = 5100 then '财务公司'
			when CompanyType = 6100 then '期货交易所'
			when CompanyType = 6110 then '期货经纪公司'
			when CompanyType = 7110 then '会计师事务所'
			when CompanyType = 7130 then '律师事务所'
			when CompanyType = 7140 then '评估评级公司'
			when CompanyType = 8001 then '指数公司'
			when CompanyType = 9900 then '其他'
			when CompanyType = 9901 then '合格境外机构投资者'
			when CompanyType = 9903 then '社保基金'
			when CompanyType = 9905 then '企业年金'
			when CompanyType = 9907 then '集合资产管理计划'
			when CompanyType = 9909 then '基金资产管理计划'
			when CompanyType = 9911 then '信托公司单一证券信托'
			when CompanyType = 9912 then '信托公司集合信托计划'
			when CompanyType = 9913 then '银行理财产品'
			when CompanyType = 9914 then '保险产品'
			when CompanyType = 9915 then '保险账户'
			when CompanyType = 9920 then '其他分支机构'
			when CompanyType = 9930 then '社会团体'
			when CompanyType = 9951 then '一般院校'
			when CompanyType = 9953 then '高等院校'
			when CompanyType = 9955 then '研究院所机构'
			when CompanyType = 9959 then '院校企业'
			when CompanyType = 9961 then '政府机构'
			when CompanyType = 9963 then '事业单位'
			when CompanyType = 9965 then '国资机构'
			when CompanyType = 9967 then '法院'
			when CompanyType = 9996 then '集合公司'
			when CompanyType = 9997 then '工会持股会'
			when CompanyType = 9998 then '美国上市中国概念公司'
			when CompanyType = 9999 then '自然人'
		END as ConsignmentType
	from 
		LC_InstiArchive) as ConsignmentInstiArchive on
	RelatedInstitutions.ConsignmentCode = ConsignmentInstiArchive.ConsignmentCode
where
	ConsignmentInstiArchive.ConsignmentType = '银行'
	or ConsignmentInstiArchive.ConsignmentType = '银行分行'
	-- ConsignmentInstiArchive.ConsignmentType = '资产管理公司' 好像是银行直销

	
-- new bank

-------------------------  bank_wealth_product ------------------------------ 
DECLARE @code date
set @code= '2023-06-30'
SELECT
	DISTINCT A.AgentName as CompanyName,
	D.ChiName as ParentCompName,
	E.QualName as ParentCompType,
	C.EstablishmentDate,
	B.FinProCode as FinProCode,
	B.ChiName as product_name,
	G.ChiName as SecuState,
	F.PopularizeStDate,
	case
		when F.MinInvestDay is null
		or F.MinInvestDay = -1 or F.OperationType is null  then '数据缺失'
		when (F.OperationType = 'FCC0000001T4') and (F.MinInvestDay <= 370) then '封闭短期'
		when (F.OperationType = 'FCC0000001T4') and (F.MinInvestDay > 370) and (F.MinInvestDay <= 1105)  then '封闭中期'
		when (F.OperationType = 'FCC0000001T4') and (F.MinInvestDay > 1105)  then '封闭长期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay <= 31)   then '开放短期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay > 31) and (F.MinInvestDay <= 93)  then '开放短中期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay > 93) and (F.MinInvestDay <= 186)  then '开放中期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay > 186) and (F.MinInvestDay <= 370)  then '开放中长期'
		when (F.OperationType = 'FCC0000001T6') and (F.MinInvestDay > 370)   then '开放长期'
		else '其他'
	end as MinInvestTimeType,
	H.ChiName as RaisingType,
	I.ChiName as OperationType,
	J.ChiName as InvestmentType,
	COALESCE(AssetAllocation.EndDate,net_value_nv.EndDate) as EndDate,
	case
		when AssetAllocation.AssetValue is not null then AssetAllocation.AssetValue
		when net_value_nv.NV is not null  then net_value_nv.NV
		else F.ActRaisingAmount * 100000000
	end as AssetValue,
	AssetAllocation.AssetPublDateIndex,
	case
		when CodeRelationship.FinProCode is not null then '子产品'
		when RelatedCodeRelationship.RelatedFinProCode is not null then '母产品'
		when CodeRelationship_fenqi.FinProCode is not null then '分期产品'
		when CodeRelationship_fenqixian.FinProCode is not null then '分期限产品'
		else '产品'
	end as ProductType,
	F.EstablishmentDate as product_establish_date,
	K.ChiName as CurrencyUnit,
	B.SecuAbbr,
	F.MinInvestTerm,
	L.ChiName as MinInvestTermUnit,
	M.ChiName as RiskLevel,
	F.BenchmarkMax,
	F.BenchmarkMin,
	F.IssueObject,
	fee.manage_fee,
	fee.manage_fee_unit,
	fee.carry_fee,
	fee.carry_fee_unit,
    fee.sale_fee,
	fee.sale_fee_unit,
	case 
		when  F.ActMaturityDate is not null then  F.ActMaturityDate
		else  F.MaturityDate 
	end as MaturityDate,
	case
	when F.InvestmentType = 'FCC0000001T8' then 
		case 
			when B.ChiName like '%现金%' then 1
			else 
				case 
					when F.MinInvestDay = 1 then 
						case 
							when A.AgentName = '中银理财有限责任公司' and B.ChiName like '%乐享%' then 1 
							when A.AgentName = '建信理财有限责任公司' and (B.ChiName like '%龙宝%' or 
							B.ChiName like '%建信宝%' or 
							B.ChiName like '%安鑫%' or 
							B.ChiName like '%恒赢%' or
							B.ChiName like '%净鑫%' or
							B.ChiName like '%净利%' or 
							B.ChiName like '%天天利%' )  then 1
							when A.AgentName = '交银理财有限责任公司' and (B.ChiName like '%现金添利%' or 
							B.ChiName like '%悦享%' ) then 1 
							when A.AgentName = '农银理财有限责任公司' and B.ChiName like '%时时付%' then 1 
							when A.AgentName = '工银理财有限责任公司' and B.ChiName like '%添利宝%' then 1 
							when A.AgentName = '光大理财有限责任公司' and B.ChiName like '%阳光碧%' then 1 
							when A.AgentName = '招银理财有限责任公司' and (B.ChiName like '%日日欣%' or 
							B.ChiName like '%朝招金%' or 
							B.ChiName like '%开鑫宝%' ) then 1 
							when A.AgentName = '兴银理财有限责任公司' and B.ChiName like '%添利%' then 1 
							when A.AgentName = '杭银理财有限责任公司' and (B.ChiName like '%新钱包%' or
							B.ChiName like '%金钱包%' or 
							B.ChiName like '%臻钱包%' ) then 1 
							when A.AgentName = '宁银理财有限责任公司' and( B.ChiName like '%宁欣天天鎏金%' or 
							B.ChiName like '%天利鑫%' ) then 1 
							when A.AgentName = '徽银理财有限责任公司' and B.ChiName like '%天天盈%' then 1 
							when A.AgentName = '南银理财有限责任公司' and B.ChiName like '%添睿%' then 1 
							when A.AgentName = '苏银理财有限责任公司' and B.ChiName like '%启源%' then 1 
							when A.AgentName = '平安理财有限责任公司' and B.ChiName like '%天天成长%' then 1 
							when A.AgentName = '青银理财有限责任公司' and B.ChiName like '%奋斗%' then 1 
							when A.AgentName = '渝农商理财有限责任公司' and B.ChiName like '%渝快宝%'  then 1 
							when A.AgentName = '信银理财有限责任公司' and B.ChiName like '%日盈象%' then 1
							when A.AgentName = '广银理财有限责任公司' and B.ChiName like '%鎏金%' then 1 
							when A.AgentName = '民生理财有限责任公司' and B.ChiName like '%天天增利%' then 1
							when A.AgentName = '恒丰理财有限责任公司' and B.ChiName like '%新恒梦钱包%' then 1 
							when A.AgentName = '中邮理财有限责任公司' and (B.ChiName like '%零钱宝%' or 
							B.ChiName like '%理财宝%') then 1 
							else 0 
						end 
					else 0 
				end
			end  
 		else 0 
 	end as inv_type,
F.RegistrationCode,
lever.lever_date,
lever.leverage,
manager.ChiName as manage_comp,
F.MinInvestDay,
fi.ChiName as IfStructure,
F.InvestTerm,
F.InvestTermUnit,
F.ActRaisingAmount * 100000000 as ActRaisingAmount
FROM
	(
	select
		*
	from
		LC_InstiQualCoRe
	where
		QualCode in (2029)) A
	-- 银行理财子
left JOIN (
	SELECT
		*
	FROM
		FP_SecuMain
	WHERE
		SecuCategory = 'FCC0000001TD' ) B ON
	B.CompanyCode = A.CompanyCode
left JOIN LC_InstiArchive C ON
	A.CompanyCode = C.CompanyCode
left join LC_InstiArchive D on
	D.CompanyCode = C.ParentCompany
left JOIN (
	select
		*
	from
		LC_InstiQualCoRe
	where
		QualCode in (2004, 2007, 2008, 2015, 2029) )E
	-- 规定母公司类别  城商行、国有行、外资合营的划分等 
 on
	D.CompanyCode = E.CompanyCode
left JOIN (
	select
		*,
		CASE
			when MinInvestTermUnit is null
			or MinInvestTerm is null then -1
			when MinInvestTermUnit = 'FCC0000001S9' then MinInvestTerm
			when MinInvestTermUnit = 'FCC0000001TC' then MinInvestTerm * 7
			when MinInvestTermUnit = 'FCC0000001S8' then MinInvestTerm * 30
			when MinInvestTermUnit = 'FCC0000001S7' then MinInvestTerm * 365
			else -1
		end as MinInvestDay
	from
		FP_BasicInfo ) F on
	B.FinProCode = F.FinProCode
left JOIN FP_Indicator G on
	B.SecuState = G.GilCode
left JOIN FP_Indicator H on
	F.RaisingType = H.GilCode
left JOIN FP_Indicator I on
	F.OperationType = I.GilCode
left JOIN FP_Indicator J on
	F.InvestmentType = J.GilCode
left JOIN FP_Indicator K on
	F.CurrencyUnit = K.GilCode
left join FP_Indicator L on
	F.MinInvestTermUnit = L.GilCode
left join FP_Indicator M on
	F.RiskLevelCode = M.GilCode
left join (
	select
		COALESCE(manage.FinProCode,carry.FinProCode,sale.FinProCode) as FinProCode,
		carry.carry_fee, 
		carry.carry_fee_unit ,
		manage.manage_fee,
		manage.manage_fee_unit,
        sale.sale_fee,
		sale.sale_fee_unit
		from
		(
		select * from (
		select
			FinProCode as FinProCode, ChargeRate as carry_fee, dd.ChiName as carry_fee_unit, ROW_NUMBER() over(PARTITION by FinProCode
		ORDER BY
			FP_ChargeRate.CancelDate DESC) as date_index
		from
			FP_ChargeRate
		left join dbo.FP_Indicator dd on
			FP_ChargeRate.ChargeRateUnit = dd.GilCode
		where
			FP_ChargeRate.ChargeRateType = 'FCC0000001RX'
			and FP_ChargeRate.ExcuteDate <= @code
			and FP_ChargeRate.CancelDate >= @code
			and FP_ChargeRate.ChargeRate is not null
			) carry_1
			where carry_1.date_index = 1) carry
	FULL join (
	select * from (
		select
			FinProCode, ChargeRate as manage_fee, ee.ChiName as manage_fee_unit, ROW_NUMBER() 
			over(PARTITION by FinProCode
		ORDER BY
			FP_ChargeRate.CancelDate DESC) as date_index
		from
			FP_ChargeRate
		left join dbo.FP_Indicator ee on
			FP_ChargeRate.ChargeRateUnit = ee.GilCode
		where
			FP_ChargeRate.ChargeRateType = 'FCC0000001S1'
			and FP_ChargeRate.ChargeRateInterval = 'FCC0000001SF'
		    and FP_ChargeRate.ExcuteDate <= @code
			and FP_ChargeRate.CancelDate >= @code)manage1
			where manage1.date_index = 1)  manage on
		manage.FinProCode = carry.FinProCode
	FULL join (
	select * from (
		select
			FinProCode, ChargeRate as sale_fee, ee.ChiName as sale_fee_unit, ROW_NUMBER()
			over(PARTITION by FinProCode
		ORDER BY
			FP_ChargeRate.CancelDate DESC) as date_index
		from
			FP_ChargeRate
		left join dbo.FP_Indicator ee on
			FP_ChargeRate.ChargeRateUnit = ee.GilCode
		where
			FP_ChargeRate.ChargeRateType = 'FCC0000001RU'
			and FP_ChargeRate.ChargeRateInterval = 'FCC0000001SF'
		    and FP_ChargeRate.ExcuteDate <= @code
			and FP_ChargeRate.CancelDate >= @code)sale1
			where sale1.date_index = 1)  sale on
		manage.FinProCode = sale.FinProCode )fee on
	B.FinProCode = fee.FinProCode
left join (
	select
		FinProCode,AssetTypeCode, EndDate as EndDate, MarketValue as AssetValue, ROW_NUMBER() 
		over(PARTITION by FinProCode
	ORDER BY
		InfoPublDate desc,AssetTypeCode) as AssetPublDateIndex
	from
		(select * from FP_AssetAllocation
	where
		-- 金融产品净资产或者总资产
 AssetTypeCode in ('FCC0000001X9','FCC0000001XA')
		-- 非空的市值
		and MarketValue is not null 
		and EndDate <=@code)ttt) AssetAllocation on
	AssetAllocation.FinProCode = B.FinProCode
left join (
	select
		*
	from
		FP_CodeRelationship
	where
		CodeDefine in ('FCC000000YDC', 'FCC000001E0I')) CodeRelationship on
	B.FinProCode = CodeRelationship.FinProCode
left join (
	select
		*
	from
		FP_CodeRelationship
	where
		CodeDefine in ('FCC000000YDC', 'FCC000001E0I')) RelatedCodeRelationship on
	B.FinProCode = RelatedCodeRelationship.RelatedFinProCode
left join (
	select
		*
	from
		FP_CodeRelationship
	where
		CodeDefine = 'FCC000000YDD') CodeRelationship_fenqi on
	B.FinProCode = CodeRelationship_fenqi.FinProCode
left join (
	select
		*
	from
		FP_CodeRelationship
	where
		CodeDefine = 'FCC00000129X') CodeRelationship_fenqixian on
	B.FinProCode = CodeRelationship_fenqixian.FinProCode
left join ( 
	select FinProCode, EndDate as lever_date ,leverage from(
	select FinProCode ,EndDate ,leverage ,ROW_NUMBER() over(PARTITION by FinProCode
			ORDER BY
				c.EndDate DESC) as date_index
	from (
	select COALESCE (a.FinProCode,b.FinProCode) as FinProCode,
		   COALESCE (a.EndDate,b.EndDate) as EndDate,
		   all_value_sum / net_value_sum as leverage
	from (
	select FinProCode,EndDate,MarketValue as net_value_sum from dbo.FP_AssetAllocation
	where AssetTypeCode  = 'FCC0000001X9' and SecuCategory  = 'FCC0000001TD') a 
	join (
	select FinProCode,EndDate,MarketValue as  all_value_sum from dbo.FP_AssetAllocation  
	where AssetTypeCode  = 'FCC0000001XA' and SecuCategory = 'FCC0000001TD') b 
	on a.FinProCode  = b.FinProCode and a.EndDate = b.EndDate
	)c) t 
	where t.date_index = 1 
	) lever
	on B.FinProCode = lever.FinProCode
left join LC_InstiArchive manager
on B.CompanyCode  = manager.CompanyCode
left join FP_Indicator fi
on F.IfStructure = fi.GilCode
left join (select FinProCode,
	EndDate,
	NV from (
select
	FinProCode,
	EndDate,
	NV,
	ROW_NUMBER() over(PARTITION by FinProCode
order by
	EndDate desc ) as num
from
	dbo.FP_NetValue ) fnv
	where fnv.num = 1 
	and fnv.NV is not null)net_value_nv
on net_value_nv.FinProCode = B.FinProCode
where
	(AssetAllocation.AssetPublDateIndex = 1
	or AssetAllocation.AssetPublDateIndex is null)	
	
	
	