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


def merge_py_jy_product_info():
    print('产品信息 py 和 jy 数据开始合并...')
    path = os.path.join(os.path.join(project_path, 'docs'), LicaiBaseTable.table_product_info_py)
    py_data = pd.read_csv(path, parse_dates=['PopularizeStDate', 'EndDate', 'product_establish_date', 'MaturityDate'],encoding='utf8')
    # 转化时间
    # from dateutil.parser import parse
    # py_data['MaturityDate'] = py_data['MaturityDate'].apply(lambda x: parse(x) if str(x) != 'nan' else x)
    jy_data = juyuan_reader.get_basic_info_from_csv(database='jy')

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
                           'asset_type', 'resource']]

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
         'asset_type', 'resource']]

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
    path = os.path.join(os.path.join(project_path, 'docs'), LicaiBaseTable.sub_table_product_info_base_merge)
    merge_data_2.to_csv(path, index=False)



if __name__ == '__main__':
    merge_py_jy_product_info()




