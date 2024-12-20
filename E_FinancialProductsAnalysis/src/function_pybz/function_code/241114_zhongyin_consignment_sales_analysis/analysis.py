import dateutil
import pandas as pd
import numpy as np

from preprocess import preprocess
import argparse


def date_omit(df, col):
    df[col] = pd.to_datetime(df[col])
    df[col] = df[col].dt.strftime('%Y/%m/%d')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    # 去年同期一天
    parser.add_argument('--path_基本数据', type=str, help='path_基本数据', default='bank_wealth_product_base_pyjy_24Q3_241108.csv')
    parser.add_argument('--path_代销数据', type=str, help='path_代销数据', default='中信建投-241115-220701.xlsx')
    parser.add_argument('--path_业绩数据', type=str, help='path_业绩数据', default='py_licai_product_nv_indicator_for_zhongyinlicai_20220101_20241122.csv')
    parser.add_argument('--output_file', type=str, help='output_file', default='代销行所有产品数据情况.xlsx')
    parser.add_argument('--analysis_date', type=str, help='analysis_date', default='2024-11-15')
    args = parser.parse_args()

    all_data_file = args.path_基本数据
    consignment_data_file = args.path_代销数据
    performance_data_file = args.path_业绩数据
    output_file = args.output_file
    analysis_date = args.analysis_date

    all_data_df = pd.read_csv(all_data_file)
    consignment_data_df = pd.read_excel(consignment_data_file)
    performance_data_df = pd.read_csv(performance_data_file, encoding='gbk')

    all_data_df = preprocess(all_data_df, analysis_date)
    all_data_df['理财公司简称'] = all_data_df.apply(lambda x: x[0].split('有限')[0], axis=1)

    all_data_df = all_data_df[['理财公司简称', 'FinProCode', 'product_name', 'RegistrationCode', 'InvestmentType', 'RaisingType',
                              'OperationType', 'open_type', 'AssetValue', 'product_establish_date', 'MaturityDate', 'CurrencyUnit',
                              'MinInvestTerm', 'RiskLevel', 'Benchmark', 'BenchmarkMax', 'BenchmarkMin', 'manage_fee_x',
                              'carry_fee_x', 'sale_fee_x', 'IssueObject_y']]

    consignment_data_df = consignment_data_df[consignment_data_df['代销结束日'] > analysis_date]
    consignment_data_df = consignment_data_df[['产品登记编码', '普益代码', '发行机构', '代销机构', '代销开始日', '代销结束日']]

    performance_data_df = performance_data_df[['FinProCode', 'begin_date', 'end_index', 'interval_ret_one_m',
                                               'interval_ret_two_m', 'interval_ret_three_m', 'interval_ret_six_m',
                                               'interval_ret_one_y', 'max_drawdown_one_m', 'max_drawdown_two_m',
                                               'max_drawdown_three_m', 'max_drawdown_six_m', 'max_drawdown_one_y',
                                               'interval_ret_annual', 'max_draw_down', 'shapre_original', 'vol_annual']]

    combin_df = pd.merge(all_data_df, consignment_data_df, how='inner', left_on=['RegistrationCode', 'FinProCode'],
                         right_on=['产品登记编码', '普益代码'])  # 合并匹配基础数据和代销数据

    combin_df = pd.merge(combin_df, performance_data_df, how='left', on='FinProCode')

    date_omit(combin_df, 'product_establish_date')
    date_omit(combin_df, 'MaturityDate')
    date_omit(combin_df, 'begin_date')
    date_omit(combin_df, 'end_index')
    date_omit(combin_df, '代销开始日')
    date_omit(combin_df, '代销结束日')

    combin_df.rename(columns={'product_name': '产品名称', 'RegistrationCode': '登记编码', 'InvestmentType': '产品类型',
                              'RaisingType': '募集方式', 'OperationType': '运作方式', 'open_type': '开放形式',
                              'AssetValue': '产品存续规模（元）', 'product_establish_date': '产品成立日期', 'MaturityDate': '产品终止日期',
                              'CurrencyUnit': '币种', 'MinInvestTerm': '最短持有期', 'RiskLevel': '风险等级', 'Benchmark': '业绩基准',
                              'BenchmarkMax': '业绩基准上限（%）', 'BenchmarkMin': '业绩基准下限（%）', 'manage_fee_x': '管理费（%）',
                              'carry_fee_x': '业绩计提比例（%）', 'sale_fee_x': '销售服务费（%）', 'IssueObject_y': '销售对象',

                              'begin_date': '业绩统计起始日', 'end_index': '业绩统计截止日',
                              'max_drawdown_one_m': '近1个月最大回撤',  'max_drawdown_two_m': '近2个月最大回撤',
                              'max_drawdown_three_m': '近3个月最大回撤', 'max_drawdown_six_m': '近6个月最大回撤',
                              'max_drawdown_one_y': '近1年最大回撤',

                              'interval_ret_annual': '成立以来年化收益率', 'max_draw_down': '成立以来最大回撤',
                              'shapre_original': '成立以来夏普比', 'vol_annual': '成立以来年化波动率', }, inplace=True)

    # combin_df = combin_df[combin_df['代销机构'] == '招商银行']

    cash_prod_df = combin_df[combin_df['产品类型'] == '现金管理类']
    not_cash_prod_df = combin_df[combin_df['产品类型'] != '现金管理类']

    cash_prod_df.rename(columns={'interval_ret_one_m': '近1个月年化收益率', 'interval_ret_two_m': '近2个月年化收益率',
                                 'interval_ret_three_m': '近3个月年化收益率', 'interval_ret_six_m': '近6个月年化收益率',
                                 'interval_ret_one_y': '近1年年化收益率'}, inplace=True)

    not_cash_prod_df.rename(columns={'interval_ret_one_m': '近1个月累计收益率', 'interval_ret_two_m': '近2个月累计收益率',
                                     'interval_ret_three_m': '近3个月累计收益率', 'interval_ret_six_m': '近6个月累计收益率',
                                     'interval_ret_one_y': '近1年累计收益率'}, inplace=True)

    cash_prod_df = cash_prod_df[['产品名称', '登记编码', '发行机构', '产品成立日期', '产品终止日期', '代销机构', '代销开始日', '代销结束日',

                                 '产品类型', '募集方式', '运作方式', '开放形式', '币种', '销售对象', '最短持有期', '风险等级',
                                 '业绩基准', '业绩基准上限（%）', '业绩基准下限（%）', '管理费（%）', '业绩计提比例（%）', '销售服务费（%）',

                                 '产品存续规模（元）', '近1个月年化收益率', '近2个月年化收益率', '近3个月年化收益率', '近6个月年化收益率',
                                 '近1年年化收益率', '成立以来年化收益率', ]]

    not_cash_prod_df = not_cash_prod_df[['产品名称', '登记编码', '发行机构', '产品成立日期', '产品终止日期', '代销机构', '代销开始日', '代销结束日',

                                        '产品类型', '募集方式', '运作方式', '开放形式', '币种', '销售对象', '最短持有期', '风险等级',
                                        '业绩基准', '业绩基准上限（%）', '业绩基准下限（%）', '管理费（%）', '业绩计提比例（%）', '销售服务费（%）',

                                        '产品存续规模（元）', '业绩统计起始日', '业绩统计截止日', '近1个月累计收益率', '近2个月累计收益率',
                                        '近3个月累计收益率', '近6个月累计收益率', '近1年累计收益率', '近1个月最大回撤', '近2个月最大回撤',
                                        '近3个月最大回撤', '近6个月最大回撤', '近1年最大回撤', '成立以来年化收益率', '成立以来最大回撤',
                                         '成立以来夏普比', '成立以来年化波动率']]

    writer = pd.ExcelWriter(output_file)
    not_cash_prod_df.to_excel(writer, sheet_name='非现金类产品报表', index=False)
    cash_prod_df.to_excel(writer, sheet_name='现金管理类产品报表', index=False)
    writer.save()
    writer.close()