# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/9/15 18:41 
# @Author    : Wangyd5 
# @File      : tst
# @Project   : sublicai
# @Function  ：
# --------------------------------

# -*- coding=utf-8 -*-
# -----------------------------
# @Time      : 2022/8/31 17:30
# @Author    : wangyd5
# @File      : a.py
# @Project   : tst
# @Function  ：
# -----------------------------



import pandas as pd
import pyodbc

driver = list(pyodbc.drivers())[0]
from sqlalchemy import create_engine

charset = 'GBK'
engine = create_engine('mssql+pyodbc://readeronly:readeronly@10.237.122.83:1433/JYDB' + f'?driver={driver}',
                       connect_args={'charset': charset}, pool_pre_ping=True)

# FP_BasicInfo = pd.read_sql("""SELECT * FROM FP_BasicInfo """, engine)
FP_Indicator = pd.read_sql("""SELECT * FROM FP_Indicator """, engine)
FP_SecuMain = pd.read_sql("""SELECT * FROM FP_SecuMain where EnterpriseCode = 'ETP0001SLL0Q'   """,engine)  # fixme   更改查询方式
# company_info = pd.read_sql("""SELECT * FROM EP_CompanyMain """, engine)

FP_Indicator_dict = FP_Indicator.set_index('GilCode')['ChiName'].to_dict()

FP_SecuMain['SecuCategory_cn'] = FP_SecuMain['SecuCategory'].map(FP_Indicator_dict)
FP_SecuMain = FP_SecuMain[FP_SecuMain['SecuCategory_cn'] == '银行理财']

#  判断策略的几个字段类型
"""
风险相关 
    风险评级 RiskLevelCode
    是否结构化(IfStructure)
    是否有抵押(IfHaveMortgage)
    是否有质押(IfHavePledge)
    是否有担保(IFHaveGuarantee)
    是否可质押（IfPledge）

收益相关
    收益类型,IncomeType ,
    投资领域(InvestScope)
    投资性质 InvestmentType
    计划投资方向(InvestDirection)  股票型、债券型等等 
    投资领域(InvestScope)

流动性  
    能否提前终止（IfTermination）
    赎回频率(RedeemFrequency)
    退出方式(ExitType)  
    封闭期单位(LockupPerUn)
    最短持有期限单位(MinInvestTermUnit)
    期限类型(MaturityType)
    收益分配方式(ProfitDistribution)

-- 产品形态 
    募集方式  RaisingType
    计划类型(PlanType)  -- 区分大集合、小集合之类的 
    运作方式（OperationType）

"""

risk_col = ['RiskLevelCode', 'IfStructure', 'IfHaveMortgage', 'IfHavePledge', 'IFHaveGuarantee', 'IfPledge']
ret_col = ['IncomeType', 'InvestScope', 'InvestmentType', 'InvestDirection', 'InvestScope']
liquidity_col = ['IfTermination', 'RedeemFrequency', 'ExitType', 'LockupPerUn',
                 'MinInvestTermUnit', 'MaturityType', 'ProfitDistribution']
col = risk_col + ret_col + liquidity_col

company_name = '中银理财'
company_code = 'ETP0001SLL0Q'
# company_code = company_info.loc[company_info['ChiNameAbbr'] == company_name,'EnterpriseCode'].iloc[0]
#  获取理财子产品代码
finprocode = FP_SecuMain.loc[FP_SecuMain['EnterpriseCode'] == company_code, 'FinProCode'].tolist()

FP_BasicInfo = pd.read_sql(f"""SELECT * FROM FP_BasicInfo where FinProCode ='SEC000035412' """, engine)

FP_BasicInfo['RaisingType'] = FP_BasicInfo['RaisingType'].map(FP_Indicator_dict)
FP_BasicInfo['RiskLevelCode'] = FP_BasicInfo['RiskLevelCode'].map(FP_Indicator_dict)
FP_BasicInfo['IncomeType'] = FP_BasicInfo['IncomeType'].map(FP_Indicator_dict)
FP_BasicInfo['RaisingType'] = FP_BasicInfo['RaisingType'].map(FP_Indicator_dict)
FP_BasicInfo['MinInvestTermUnit'] = FP_BasicInfo['MinInvestTermUnit'].map(FP_Indicator_dict)
FP_BasicInfo['InvestTermUnit'] = FP_BasicInfo['InvestTermUnit'].map(FP_Indicator_dict)
FP_BasicInfo['IfCancel'] = FP_BasicInfo['IfCancel'].map(FP_Indicator_dict)
FP_BasicInfo['OperationType'] = FP_BasicInfo['OperationType'].map(FP_Indicator_dict)
FP_BasicInfo['InvestmentType'] = FP_BasicInfo['InvestmentType'].map(FP_Indicator_dict)
FP_BasicInfo['IfPledge'] = FP_BasicInfo['IfPledge'].map(FP_Indicator_dict)
FP_BasicInfo['IfStructure'] = FP_BasicInfo['IfStructure'].map(FP_Indicator_dict)
FP_BasicInfo['IfTermination'] = FP_BasicInfo['IfTermination'].map(FP_Indicator_dict)
FP_BasicInfo['RedeemFrequency'] = FP_BasicInfo['RedeemFrequency'].map(FP_Indicator_dict)
FP_BasicInfo['MaturityType'] = FP_BasicInfo['MaturityType'].map(FP_Indicator_dict)
FP_BasicInfo['InvestScope'] = FP_BasicInfo['InvestScope'].map(FP_Indicator_dict)
FP_BasicInfo['ProfitDistribution'] = FP_BasicInfo['ProfitDistribution'].map(FP_Indicator_dict)
FP_BasicInfo['IfHaveMortgage'] = FP_BasicInfo['IfHaveMortgage'].map(FP_Indicator_dict)
FP_BasicInfo['IfHavePledge'] = FP_BasicInfo['IfHavePledge'].map(FP_Indicator_dict)
FP_BasicInfo['IFHaveGuarantee'] = FP_BasicInfo['IFHaveGuarantee'].map(FP_Indicator_dict)
FP_BasicInfo['IfHavePledge'] = FP_BasicInfo['IfHavePledge'].map(FP_Indicator_dict)
FP_BasicInfo['PlanType'] = FP_BasicInfo['PlanType'].map(FP_Indicator_dict)
FP_BasicInfo['InvestDirection'] = FP_BasicInfo['InvestDirection'].map(FP_Indicator_dict)

FP_BasicInfo = FP_BasicInfo[col]
FP_BasicInfo['company'] = company_name
FP_BasicInfo['FinProcode'] = 'SEC000035412'


a = pd.read_pickle('D:\institution\sublicai\docs\company_sets_dict.pkl')
for key, value in a.items():
    print(key)
    print(value)
















