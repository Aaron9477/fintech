# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/9/14 14:09 
# @Author    : Wangyd5 
# @File      : read_juyuan
# @Project   : sublicai
# @Function  ：
# --------------------------------


import os
from typing import Optional
from typing import Union

import numpy as np
import pandas as pd
from sqlalchemy import or_,and_

from database.connection.connection_base import ConnectionBase
from database.connection.sql_server_con import get_default_juyuan_connection
from database.data_field import *
from database.operator_base import BaseReader
from config.specify_variable import *
from config.basic_config import project_path
from functools import lru_cache
from config.licai_base_table_config import LicaiBaseTable
from sql import SqlStatement

class JuyuanReader(BaseReader):
    def __init__(self, juyuan_connection: Optional[ConnectionBase] = None):
        """
        Args:
            juyuan_connection: 数据库连接。如果为None则使用默认配置连接
        """
        if juyuan_connection is None:
            juyuan_connection = get_default_juyuan_connection()
        super().__init__(db_connection=juyuan_connection)


    def get_bank_wealth_company_info(self) -> dict:
        """
        获取理财子公司的名称和代码
        :return: {str: int }
        """
        table_name = LC_InstiQualCoRe
        columns = ['CompanyCode', 'AgentName', 'QualCode']
        query = self.query(table_name, columns)
        code = 2029  # 代表商业理财子公司
        query = query.filter(table_name.QualCode == code)
        df = self.batch_query(query)
        return df.set_index('AgentName')['CompanyCode'].to_dict()
    
    def get_bank_wealth_product(self):
        """ 获取bank 表"""
        sql_state = SqlStatement.jy_sql_bank
        df = pd.read_sql(sql_state,con=self.engine)
        return df


    def get_product_code_by_company(self,
                                    company: Union[None, str] = None,
                                    secu_state: Union[None, str, list] = None) -> list:
        """
        获取理财产品代码
        :param company:  理财子公司名称，如 "建信理财有限责任公司"
        :param secu_state: 产品状态
        :return: []
        """
        table_name = FpSecuMain
        query = self.query(table_name).filter(table_name.SecuCategory == 'FCC0000001TD')
        if company is not None:
            query = query.join(LC_InstiQualCoRe, LC_InstiQualCoRe.CompanyCode == table_name.CompanyCode).filter(
                LC_InstiQualCoRe.AgentName == company
            )
        if secu_state is None:
            secu_state = list(secu_state_dict.values())[2]  # 运行期
        else:
            secu_state = [secu_state_dict[x] for x in secu_state]
        df = self.batch_query(query, table_name.SecuState, secu_state)
        return list(df['FinProCode'].unique())

    def get_product_info(self,
                         code: Union[None,str,list] = None,
                         Category='FCC0000001TD',  # 银行理财
                         filter_child_product = True
                         ) -> pd.DataFrame:

        """
        读取数据库 银行理财 基本信息数据
        :param code: 理财产品代码
        :param Category:
        :return:
        """
        table_name = FpBasicInfo
        # 筛选 银行理财
        query = self.session.query(LC_InstiArchive.ChiName,FpSecuMain.ChiName, table_name).outerjoin(FpSecuMain,
                                                                            table_name.FinProCode == FpSecuMain.FinProCode).\
        outerjoin(LC_InstiArchive,LC_InstiArchive.CompanyCode == FpSecuMain.CompanyCode).\
            filter(table_name.SecuCategory == Category)
        # 查询数据
        df = self.batch_query(query, table_name.FinProCode, code)
        df.rename(columns={'ChiName':'compyname',
                           'ChiName_1':'product_cname'},inplace=True)
        # 获取 FpIndicator 数据
        fbindicator_ser = self.batch_query(self.query(FpIndicator)).set_index('GilCode')['ChiName']

        # 将代码映射为汉字
        def map_func(x):
            if x in fbindicator_ser:
                return fbindicator_ser[x]
            else:
                return x
        # 选择特定的列
        columns = ['compyname','product_cname','FinProCode','InvestmentType','OperationType','RiskLevelCode','RegistrationCode',
                   'IncomeType','RaisingType','PopularizeStDate','PopularizeEdDate','EstablishmentDate','MaturityDate',
                   'ActMaturityDate','MinInvestTerm','MinInvestTermUnit','InvestTerm','InvestTermUnit','LeastBuySum',
                   'IncreasingAmountPER','ActRaisingAmount','ExpAnEnYield','ExpAnBeYield','BenchmarkMax','BenchmarkMin',
                   'InvestAdvisorCode','TrusteeCode']
        df = df[columns].copy()
        for col in df.columns:
            df[col] = df[col].map(map_func)

        # 调整投资期限
        def transfer_period_unit(invest_term,termunit):
            if termunit == '日':
                return invest_term
            elif termunit == '周':
                return invest_term * 7
            elif termunit == '月':
                return invest_term * 30
            elif termunit == '年':
                return invest_term * 365
            else:
                return np.nan

        df['MinInvestTerm'] = df.apply(lambda x:transfer_period_unit(x.MinInvestTerm,x.MinInvestTermUnit),axis=1)
        df['InvestTerm'] = df.apply(lambda x: transfer_period_unit(x.InvestTerm, x.InvestTermUnit), axis=1)
        df.drop(['MinInvestTermUnit','InvestTermUnit'],axis=1,inplace=True)

        # 处理母产品和子产品
        relationship_df = self.batch_query(self.query(FpCodeRelationship))
        relationship_muzi = relationship_df[relationship_df['CodeDefine'].isin(['FCC000000YDC','FCC000001E0I'])]
        relationship_dict = {key:'份额母产品' for key in list(relationship_muzi['RelatedFinProCode'])}
        relationship_dict.update({key:'份额子产品' for key in list(relationship_muzi['FinProCode'])})
        relationship_fenqi = relationship_df[relationship_df['CodeDefine'] == 'FCC000000YDD']
        relationship_dict.update({key: '分期母产品' for key in list(relationship_fenqi['RelatedFinProCode'])})
        relationship_dict.update({key: '分期子产品' for key in list(relationship_fenqi['FinProCode'])})
        relationship_fenqixian = relationship_df[relationship_df['CodeDefine'] == 'FCC00000129X']
        relationship_dict.update({key: '分期限母产品' for key in list(relationship_fenqixian['RelatedFinProCode'])})
        relationship_dict.update({key: '分期限子产品' for key in list(relationship_fenqixian['FinProCode'])})
        df['type'] = df['FinProCode'].map(relationship_dict)
        df['type'] = df['type'].fillna('产品')
        if filter_child_product:
            df = df[df['type'].isin(['份额母产品','分期母产品','分期限母产品','产品'])].copy()
        return df

    def get_mktvalue_by_product(self,code: Union[None, str, list] = None,
                                    end_date: Union[None,str] = None) -> pd.DataFrame:

        """  从资产配置表中获取 最新的存续规模数据  """
        table_name = FpAssetAllocation
        query = self.query(table_name, ['FinProCode','EndDate','MarketValue']).filter(and_(table_name.MarketValue.isnot(None),
                                                                                           table_name.AssetTypeCode == 'FCC0000001X9',
                                                                                           table_name.EndDate <= end_date))  # 金融资产净合计
        # 查询数据
        df = self.batch_query(query, table_name.FinProCode, code)
        df = df[['FinProCode', 'EndDate', 'MarketValue']].sort_values(['FinProCode', 'EndDate'])
        df = df.groupby('FinProCode').apply(lambda x: x.tail(1)).reset_index(drop=True)

        # 用实际募集规模来代替
        actual_raising_query = self.query(FpBasicInfo,['FinProCode','EstablishmentDate','ActRaisingAmount']).filter(FpBasicInfo.ActRaisingAmount.isnot(None))
        actual_raising_data = self.batch_query(actual_raising_query,FpBasicInfo.FinProCode,code)
        finprocode_list = [x for x in actual_raising_data['FinProCode'].to_list() if x not in df['FinProCode'].to_list()]
        actual_raising_merge = actual_raising_data[actual_raising_data['FinProCode'].isin(finprocode_list)].copy()
        actual_raising_merge.rename(columns={'EstablishmentDate':'EndDate',
                                            'ActRaisingAmount':'MarketValue'},inplace=True)
        actual_raising_merge['MarketValue'] = actual_raising_merge['MarketValue'] * 100000000
        data = pd.concat([df,actual_raising_merge])
        return data


    def get_FpAssetAllocation(self,code: Union[None, str, list] = None,
                                    end_date: Optional[str] = None,
                                    begin_date: Optional[str] = None,
                                    trade_date: Optional[str] = None,
                                    columns: Optional[list] = None,
                                    info_source = '半年度投资报告') -> pd.DataFrame:
        """
        获取资产配置表数据
        :param code:
        :param end_date:
        :param begin_date:
        :param trade_date:
        :param columns:
        :return:
        """
        table_name = FpNetValue
        query = self.query(table_name, columns)
        # 查询数据
        query = self.filter_date(query,table_name.EndDate,begin_date,end_date,trade_date)
        data = self.batch_query(query,table_name.FinProCode,code)
        return data


    def get_FpNetValueRe_by_product(self,
                                    code: Union[None, str, list] = None,
                                    columns: Optional[list] = None) -> pd.DataFrame:

        """ 复权净值数据   （净值数据有问题，暂时不采用）"""  # fixme 复权净值数据有时候为空   SEC00002E0BA 还存在在2021-09-24后  复权净值有数，单位净值没数 之前反过来，不敢用复权净值数据
        #
        # 计算方法：如果有复权净值数据，采用复权净值计算收益率，如果没有则采用净值数据计算收益率
        table_name = FpNetValueRe
        query = self.query(table_name, columns)
        # 查询数据
        FpNetValueRe_df = self.batch_query(query, table_name.FinProCode, code)
        table_name = FpNetValue
        query = self.query(table_name, columns)
        # 查询数据
        FpNetValue_df = self.batch_query(query, table_name.FinProCode, code)
        df = pd.merge(FpNetValue_df[['FinProCode', 'EndDate', 'AccumulatedUnitNV']],
                      FpNetValueRe_df[['FinProCode', 'EndDate', 'UnitNVRestored']],
                      on=['FinProCode', 'EndDate'], how='outer')

        # 处理净值数据，计算收益率
        def cal_product_ret(tmp_df):
            tmp_df['ret_unitnvrestored'] = tmp_df['UnitNVRestored'].pct_change()
            tmp_df['ret_unit'] = tmp_df['AccumulatedUnitNV'].pct_change()

            def func(ret_unitnvrestored, ret_unit):
                if (not np.isnan(ret_unitnvrestored)) & (ret_unitnvrestored != 0):
                    return ret_unitnvrestored
                else:
                    if (not np.isnan(ret_unit)) & (ret_unit != 0):
                        return ret_unit
                    else:
                        return np.nan

            tmp_df['ret'] = tmp_df.apply(lambda x: func(x.ret_unitnvrestored, x.ret_unit), axis=1)
            tmp_df['net_value'] = (1 + tmp_df['ret']).cumprod()
            tmp_df.dropna(subset=['ret'], inplace=True)
            return tmp_df

        result = df.groupby('FinProCode').apply(cal_product_ret)
        if not result.empty:
            return result[['FinProCode', 'EndDate', 'ret', 'net_value']]

    def get_FpNetValue_by_product(self,
                                  code: Union[None, str, list] = None,
                                  begin_date: Union[None, str] = None,
                                  end_date: Union[None, str] = None,
                                  columns: Optional[list] = None) -> pd.DataFrame:

        """ 净值数据  """

        # 计算方法：采用累计净值计算
        table_name = FpNetValue
        query = self.query(table_name, columns)
        # 筛选条件
        if begin_date is not None:
            query = query.filter(or_(table_name.EndDate >= begin_date, table_name.EndDate.is_(None)))
        if end_date is not None:
            query = query.filter(table_name.EndDate <= end_date)
        query = query.order_by(table_name.FinProCode,table_name.EndDate)
        # 查询数据
        df = self.batch_query(query, table_name.FinProCode, code)[['FinProCode', 'EndDate', 'AccumulatedUnitNV']]

        df['ret'] = df.groupby('FinProCode')['AccumulatedUnitNV'].apply(lambda x: x.pct_change())
        df.rename(columns={'AccumulatedUnitNV': 'net_value'}, inplace=True)
        if not df.empty:
            return df[['FinProCode', 'EndDate', 'ret', 'net_value']]

    @lru_cache(None)
    def get_basic_info_from_csv(self,database='py'):
        if database == 'jy':
            path = os.path.join(os.path.join(project_path,'docs'),LicaiBaseTable.table_product_info_jy)
        elif database == 'py':
            path = os.path.join(os.path.join(project_path,'docs'),LicaiBaseTable.sub_table_product_info_base_merge)
        else:
            raise ValueError('请输入正确的数据库，如py 代表普益数据库，jy 代表聚源数据库........')
        try:
            data = pd.read_csv(path,parse_dates=['PopularizeStDate','EndDate','product_establish_date','MaturityDate'],encoding='gbk')
        except:
            data = pd.read_csv(path,parse_dates=['PopularizeStDate','EndDate','product_establish_date','MaturityDate'],encoding='utf8')

        data['FinProCode'] = data['FinProCode'].map(lambda x:str(x))
        # 转化时间
        if database == 'jy':
            from dateutil.parser import parse
            data['MaturityDate'] = data['MaturityDate'].apply(lambda x: parse(x) if str(x) != 'nan' else x)
        return data

    @lru_cache(None)
    def get_net_value_from_local(self):
        """ 从本地获取净值 """
        path = os.path.join(os.path.join(project_path,'docs'),LicaiBaseTable.table_net_value_jy)
        data = pd.read_csv(path,parse_dates=['EndDate'])
        return data

    @lru_cache(None)
    def get_net_value_from_local_py(self):
        """ 从本地获取净值 """
        path = os.path.join(os.path.join(project_path, 'docs'), LicaiBaseTable.table_net_value_py)
        data = pd.read_csv(path, parse_dates=['EndDate'])
        return data

    @lru_cache(None)
    def get_code_net_value_from_local(self,
                                      code: Union[str,list,None] = None,
                                      begin_date: object = None,
                                      end_date: object = None,
                                      database='py') -> object:
        """ 从本地获取净值 """
        if database == 'jy':
            data = self.get_net_value_from_local()
        elif database == 'py':
            data = self.get_net_value_from_local_py()
            data['LatestWeeklyYield'] = data['LatestWeeklyYield'] / 100
        else:
            raise ValueError('请输入正确的数据库，可以选择py 代表普益，jy 代表聚源.........')
        if begin_date is not None:
            data = data[data['EndDate'] >= begin_date]
        if end_date is not None:
            data = data[data['EndDate'] <= end_date]
        if code is None:
            return data
        else:
            data = data[data['FinProCode'] == code].copy()

            return data



    def get_FP_CodeRelationship_dict(self):
        """
        获取母产品关联数据
        :return: dict   母产品产品产品代码：[子产品] ,子产品产品产品代码：[母产品]
        """

        table_name = FpCodeRelationship
        query = self.query(table_name)
        query = query.filter(and_(table_name.SecuCategory == 'FCC0000001TD',   # 银行理财
                                  table_name.CodeDefine.in_(['FCC000000YDC','FCC000001E0I'])  # 份额关联
                                  )
                             )
        data = self.batch_query(query)
        muzi_dict = data.groupby('RelatedFinProCode')['FinProCode'].apply(lambda x:list(x))
        zimu_dict = data.groupby('FinProCode')['RelatedFinProCode'].apply(lambda x:list(x))
        return muzi_dict,zimu_dict



if __name__ == '__main__':
    reader = JuyuanReader()
    Finprocode = 'SEC00007G7LB'
    Finprocode = 'SEC00003E656'
    Finprocode = ['SEC00002E0BA', 'SEC00007G7LB', 'SEC00007H2QI']
    Finprocode = ['SEC00003B5M1', 'SEC00003CEXM', 'SEC00003HDNX', 'SEC00007G908', 'SEC00007HPGH']

    # Finprocode = ['SEC00007HTIY']

    # # 获取理财子公司
    # data = reader.get_bank_wealth_company_info()
    #
    # # 获取理财子公司产品代码
    company_name = '交银理财有限责任公司'
    # product_code = reader.get_product_code_by_company(company=company_name)
    # #
    # # # 获取产品信息
    # product_info = reader.get_product_info(code=product_code)
    # #
    # # # 获取存续规模
    # mkt_value = reader.get_mktvalue_by_product(code=product_code,end_date='20220630')
    # merge_data = pd.merge(product_info,mkt_value,on=['FinProCode'])
    # #
    # merge_data.loc[:,'MarketValue'].sum() / 100000000
    # len(merge_data.loc[:,'MarketValue'])

    info = reader.get_basic_info_from_csv()
    # nv = reader.get_code_net_value_from_local(code='SEC000036A7G')



    # info['ProductMaturityDate'].iloc[33]
    #
    # 'EstablishmentDate', 'PopularizeStDate', 'EndDate',
    # 'product_establish_date', 'ActMaturityDate', 'ProductMaturityDate'
    # 获取大类资产配置
    # data = reader.get_FpAssetAllocation(code=product_code)
    # data2 = data[data['InfoSource'] == '季度投资管理报告']
    # a = data2[data2['AssetTypeCode'] == 'FCC0000001X9']

    # 净值数据
    # data = reader.get_FpNetValue_by_product(code=Finprocode)

    # 产品信息数据
    # product = reader.get_product_basic_info()

    # 资产配置 规模数据
    # a_FpAssetAllocation_mtk_value = reader.get_mtk_value_FpAssetAllocation(code=Finprocode)

    # 基本信息
    # a_fpbasicinfo = reader.get_FpBasicInfo(code=Finprocode)

    # 获取母产品、子产品对应
    # muzi_dict, zimu_dict = reader.get_FP_CodeRelationship_dict()

    # # 从本地获取净值
    # all_nv_data = reader.get_net_value_from_local()
    #
    # # 从本地获取净值 产品 SEC000036A7G  SEC00003E7J9
    # nv_data = reader.get_code_net_value_from_local(code='SEC000036A7G')

    # # fixme  还有问题  母产品有很短的净值数据  而且产品净值数据是不一样的  SEC000039QOD 和 SEC000036A7G   向羽洁姐确认 不同子产品的差别
    # begin_date = '20220101'
    # end_date = '20230331'
    # code = 7748869
    # net_value_df_all = reader.get_code_net_value_from_local(code=code,begin_date=begin_date, end_date=end_date)

    from tools.tools import Timer
    with Timer(True):
        bank = reader.get_bank_wealth_product()

