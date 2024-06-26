# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/12/12 14:51 
# @Author    : Wangyd5 
# @File      : preprocess_bank_table
# @Project   : sublicai
# @Function  ：数据预处理
# --------------------------------


from process.modify.identify_cash_type import bank_wealth_product_process_cash
from database.get_instance import juyuan_reader
from database.read.read_py_base import PyReader
from config.basic_config import project_path
import datetime
import pandas as pd
import os
from config.licai_base_table_config import delete_upate_sub_table,LicaiBaseTable
from process.module.py_base_data import merge_py_jy_product_info

py_reader = PyReader()


# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/2/27 15:30
# @Author    : Wangyd5
# @File      : py_base_data
# @Project   : sublicai
# @Function  ：普益和聚源数据整合
# --------------------------------

import pandas as pd

import os
from database.get_instance import juyuan_reader
from config.basic_config import project_path
from config.licai_base_table_config import LicaiBaseTable
from database.read.read_py_base import PyReader
from database.read.read_juyuan_base import JuyuanReader

py_reader = PyReader()
jy_reader = JuyuanReader()



def merge_py_jy_product_info():

    # 从数据库下载数据
    py_data = py_reader.get_bank_wealth_product()
    jy_data = juyuan_reader.get_bank_wealth_product()


    tmp_py_data = py_data[['CompanyName', 'ParentCompName', 'ParentCompType', 'FinProCode',
                           'product_name', 'SecuState', 'PopularizeStDate', 'RaisingType',
                           'OperationType', 'InvestmentType', 'EndDate', 'AssetValue',
                           'ProductType', 'product_establish_date', 'invest_currency',
                           'CurrencyUnit', 'RiskLevel', 'Benchmark', 'BenchmarkMax', 'BenchmarkMin',
                           'manage_fee', 'carry_fee', 'MaturityDate', 'inv_type',
                           'RegistrationCode', 'IfStructure', 'InvestTerm', 'product_series',
                           'transfer_date', 'trustee_bank', 'profit_type', 'IssueObject', 'open_type', 'open_rules',
                           'fixed_income_upper',
                           'fixed_income_lower', 'equity_upper', 'equity_lower', 'derivatives_upper',
                           'derivatives_lower', 'invest_strategy',
                           'top_raise_scale', 'actual_raise_scale', 'is_index', 'is_early_redeem', 'old_invest_scope',
                           'report_date', 'product_type_son',
                           'asset_type', 'resource','product_object']]

    tmp_jy_data = jy_data[['EstablishmentDate',
                           'MinInvestTimeType', 'SecuAbbr', 'MinInvestTerm', 'manage_fee_unit', 'carry_fee_unit',
                           'MinInvestTermUnit', 'RegistrationCode', 'MinInvestDay', 'manage_fee', 'carry_fee',
                           'IssueObject']]
    tmp_jy_data = tmp_jy_data.groupby('RegistrationCode').apply(lambda x: x.head(1)).reset_index(drop=True)

    merge_data = pd.merge(tmp_py_data, tmp_jy_data, on='RegistrationCode', how='left')

    merge_data = merge_data[
        ['CompanyName', 'ParentCompName', 'ParentCompType', 'EstablishmentDate', 'FinProCode', 'product_name',
         'SecuState', 'PopularizeStDate', 'MinInvestTimeType', 'RaisingType', 'OperationType', 'InvestmentType',
         'EndDate', 'AssetValue', 'ProductType', 'product_establish_date', 'CurrencyUnit', 'SecuAbbr',
         'MinInvestTerm', 'MinInvestTermUnit', 'RiskLevel', 'Benchmark', 'BenchmarkMax', 'BenchmarkMin',
         'manage_fee_x', 'manage_fee_y', 'manage_fee_unit', 'carry_fee_x', 'carry_fee_y', 'carry_fee_unit',
         'MaturityDate', 'inv_type', 'RegistrationCode',
         'MinInvestDay', 'IfStructure', 'InvestTerm', 'product_series', 'IssueObject_x', 'IssueObject_y',
         'open_type', 'open_rules', 'fixed_income_upper',
         'fixed_income_lower', 'equity_upper', 'equity_lower', 'derivatives_upper',
         'derivatives_lower', 'invest_strategy',
         'top_raise_scale', 'actual_raise_scale', 'is_index', 'is_early_redeem', 'old_invest_scope', 'report_date',
         'product_type_son',
         'asset_type', 'resource','product_object']]


    def func(df):
        try:
            if len(df['EndDate'].dropna()) > 0:
                tmp = df.dropna(subset=['EndDate'])['AssetValue'].iloc[0]
                df.loc[:, 'AssetValue'] = tmp
        except Exception:
            print(df[['EndDate', 'AssetValue']])
        finally:
            return df

    # 做映射companyName
    dict_df = pd.merge(py_data[['CompanyName', 'RegistrationCode']], jy_data[['CompanyName', 'RegistrationCode']],
                       on=['RegistrationCode'], how='outer')
    dict_df = dict_df.drop_duplicates(subset=['CompanyName_x', 'CompanyName_y'])
    dict_df = dict_df.dropna()
    dict_df = dict_df.set_index(['CompanyName_x'])['CompanyName_y'].to_dict()

    merge_data['CompanyName'] = merge_data['CompanyName'].map(dict_df)

    merge_data_2 = merge_data.groupby('RegistrationCode').apply(lambda x: func(x))
    # path = os.path.join(os.path.join(project_path, 'docs'), LicaiBaseTable.sub_table_product_info_base_merge)
    # merge_data_2.to_csv(path, index=False)
    return merge_data_2


def select_product_info(end_date=datetime.datetime.now().strftime('%Y%m%d'),
                        begin_date='20150101',
                        state=None,
                        InvestmentType=None,
                        OperationType=None,
                        min_term_min=None,
                        min_term_max=None):


    """
    对 bank_wealth_product 预处理,筛选产品
    :param begin_date: 删除该日期之前到期的产品
    :param ProductType:
    :param state: state=1 表示筛选存续产品；state=0 表示到期产品,None 代表全部产品
    :param InvestmentType:
    :param OperationType:
    :param min_term_min:
    :param min_term_max:
    :param end_date: 形式为  '20220101',时间点用来判断是否是存续期产品
    :return:
    """
    end_date = datetime.datetime.strptime(end_date,'%Y%m%d')
    data = merge_py_jy_product_info()

    if 'PRConditions' in data.columns:
        data = data.drop('PRConditions', axis=1)

    # 增加特色标签
    def add_spec_lag(product_name,currency_unit):
        res = None
        if (str(currency_unit) != '人民币') & (str(currency_unit) !='nan') & (str(currency_unit) != '人民币元'):
            res = '外币'
        if ('esg' in str(product_name).lower()) | ('绿色' in str(product_name).lower()) | ('低碳' in str(product_name).lower()):
            res = 'ESG'
        if '养老' in str(product_name):
            res = '养老'
        return res

    data['spec_lag'] = data.apply(lambda x:add_spec_lag(x.product_name,x.CurrencyUnit),axis=1)

    data['close_open'] = data['MinInvestTimeType']
    data = data[data['FinProCode'].notnull()]
    # 判断存续期
    index = (data['product_establish_date'] < end_date) & \
            ((data['MaturityDate'] >= end_date) |
             (data['MaturityDate'].isnull()))

    data['state'] = None
    data.loc[index, 'state'] = 1
    # 到期产品
    index = (data['MaturityDate'] <= end_date) & (data['MaturityDate'].notnull())
    data.loc[index,'state'] = 0

    # data = data.groupby('RegistrationCode').apply(lambda x:x.sort_values(['AssetValue'],ascending=False).head(1))
    index = data['ProductType'].isin(['产品','母产品','子产品'])
    if state is not None:
        index = index & (data['state'] == state)
    if InvestmentType is not None:
        index = index & (data['InvestmentType'] == InvestmentType)
    if OperationType is not None:
        index = index & (data['OperationType'] == OperationType)
    if min_term_min is not None:
        index = index & (data['MinInvestTerm'] >= min_term_min)
    if min_term_max is not None:
        index = index & (data['MinInvestTerm'] <= min_term_max)

    # 删除 在 begin_date 前到期的产品
    index = index & ((data['MaturityDate'] >= datetime.datetime.strptime(begin_date,'%Y%m%d')) | (data['MaturityDate'].isnull()))
    data = data.loc[index,:].copy()
    # 处理现金管理类
    # data = bank_wealth_product_process_cash(data,database=database)
    # 其他类归为固定收益类非现金
    data['InvestmentType'] = data['InvestmentType'].map(lambda x: str(x).replace('固定收益类', '固定收益类（非现金）'))
    return data



def select_product_info_cache(end_date=datetime.datetime.now().strftime('%Y%m%d'),
                                state=None,
                                InvestmentType=None,
                                OperationType=None,
                                min_term_min=None,
                                min_term_max=None):
    """
    @end_date : '2022-01-01'
    """
    tmp_path = end_date + '_' + LicaiBaseTable.sub_table_product_info_py
    path = os.path.join(os.path.join(project_path, 'docs'), tmp_path)

    if not os.path.exists(path):
        data = select_product_info(end_date=end_date, state=state,InvestmentType=InvestmentType,OperationType=OperationType,
                                   min_term_min=min_term_min,min_term_max=min_term_max)
        data.to_csv(path,index=False)
        print(f'生成数据表{path}...')
    else:
        print(f'读取数据表{path}...')
        data = pd.read_csv(path,parse_dates=['PopularizeStDate', 'EndDate', 'product_establish_date', 'MaturityDate'],encoding='utf8')
        if state is not None:
            data = data[data['state'] == state]

        # data['FinProCode'] = data['FinProCode'].map(lambda x:str(x))
        # 转化时间
        # from dateutil.parser import parse
        # data['MaturityDate'] = data['MaturityDate'].apply(lambda x: parse(x) if str(x) != 'nan' else x)
    return data


if __name__ == '__main__':

    from tools.tools import Timer
    with Timer(True):
        end_date = '20230907'
        data = select_product_info_cache(end_date=end_date)

    data = data[['FinProCode','product_object']]

    data.to_csv(r'M:\Device\C\Users\csc23998\sublicai\licai\docs\product_object.csv',index=False)


