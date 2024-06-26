# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/11/15 17:15 
# @Author    : Wangyd5 
# @File      : cal_product_score
# @Project   : sublicai
# @Function  ： 产品打分体系（产品推荐得分）
# --------------------------------


# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/11 11:25
# @Author    : Wangyd5
# @File      : cal_nav_net_value
# @Project   : licai
# @Function  ：
# --------------------------------

from process.module.preprocess_bank_table import select_product_info_cache
from process.module.cal_non_cash_nav_net_value import cal_product_nav
from database.read.read_py_base import PyReader
from process.util_cal.process_net_value import nav_fill
import pandas as pd
from tools.tools import Timer


def cal_score(type,AssetValue_rank,interval_ret_annual_rank,
                max_draw_down_rank,sharpe_rank):
    """ 计算每个理财产品的得分"""
    coef_asset = 0
    coef_ret = 0
    coef_mdd = 0
    coef_sharpe = 0
    if type == '现金管理类':
        coef_asset = 0.3
        coef_ret = 0.7
    elif type == '固定收益类（非现金）':
        coef_ret = 0.6
        coef_mdd = 0.2
        coef_sharpe = 0.2
    elif type == '混合类':
        coef_ret = 0.3
        coef_mdd = 0.3
        coef_sharpe = 0.4
    elif type == '权益类':
        coef_ret = 0.3
        coef_mdd = 0.3
        coef_sharpe = 0.4
    elif type == '商品及金融衍生品类':
        coef_ret = 0.3
        coef_mdd = 0.3
        coef_sharpe = 0.4

    score = AssetValue_rank * coef_asset + interval_ret_annual_rank * coef_ret + \
                      max_draw_down_rank * coef_mdd + sharpe_rank * coef_sharpe
    return score


def cal_rank(df):
    """ 计算单个类别的得分"""
    tmp_df = df.copy()
    tmp_df['AssetValue_rank'] = tmp_df['AssetValue'].rank(method='dense', na_option='keep', pct=True)
    tmp_df['interval_ret_annual_rank'] = tmp_df['interval_ret_annual'].rank(method='dense', na_option='keep', pct=True)
    tmp_df['max_draw_down_rank'] = tmp_df['max_draw_down'].rank(method='dense', na_option='keep', pct=True)
    tmp_df['sharpe_rank'] = tmp_df['sharpe'].rank(method='dense', na_option='keep', pct=True)
    tmp_df['AssetValue_rank'] = tmp_df['AssetValue_rank'].fillna(0)
    tmp_df['interval_ret_annual_rank'] = tmp_df['interval_ret_annual_rank'].fillna(0)
    tmp_df['max_draw_down_rank'] = tmp_df['max_draw_down_rank'].fillna(0)
    tmp_df['sharpe_rank'] = tmp_df['sharpe_rank'].fillna(0)

    tmp_df['score'] = tmp_df.apply(lambda x:cal_score(x.InvestmentType,x.AssetValue_rank,x.interval_ret_annual_rank,
                                                      x.max_draw_down_rank,x.sharpe_rank),axis=1)
    tmp_df['score_rank'] = tmp_df['score'].rank(method='dense', na_option='keep', pct=False, ascending=False)
    tmp_df['number'] = len(tmp_df)
    tmp_df['socre_final'] = 1 - tmp_df['score_rank'] / tmp_df['number']
    tmp_df['score'] = tmp_df['socre_final'].copy()
    tmp_df['rank_str'] = tmp_df.apply(lambda x: '(' + str(int(x.score_rank)) + '/' + str(x.number) + ')', axis=1)
    return tmp_df




if __name__ == '__main__':
    with Timer(True):
        begin_date = '20200101'
        end_date = '20230630'
        reader = PyReader()
        product_info = select_product_info_cache(end_date=end_date, state=1)
        product_info = product_info[product_info['InvestmentType'] != '现金管理类']
        code_list = product_info['FinProCode'].tolist()
        # a = 1/0
        result = pd.DataFrame()

        for i,cp_id in enumerate(code_list[0:100]):
            try:
                print(i,cp_id)
                net_value = reader.get_net_value(cp_id=cp_id)
                df_new = nav_fill(net_value)
                if df_new.empty:
                    continue
                tmp_res = cal_product_nav(tmp_nav=df_new[['FinProCode', 'trade_dt', 'net_value']], finprocode=cp_id)
                result = result.append(tmp_res)
            except:
                pass

        # merge 基础信息
        nv_indicator = pd.merge(product_info.set_index(['FinProCode'])[['RegistrationCode','CompanyName', 'product_name', 'InvestmentType','OperationType','open_type',
                                                               'RaisingType', 'AssetValue']],
                       result, left_index=True, right_index=True, how='inner')

        nv_indicator = nv_indicator.reset_index()
        nv_indicator = nv_indicator.rename(columns={'index':'FinProCode'})

        # 进行分组计算得分

        product_info = select_product_info_cache(end_date=end_date, state=1)
        # fixme 在一个登记编码下 挑选出最具有代表性的产品
        product_info = product_info[product_info['ProductType'].isin(['产品', '母产品'])]
        product_code_list = list(product_info['FinProCode'].unique())
        nv_indicator = nv_indicator[nv_indicator['FinProCode'].isin(product_code_list)].copy()
        # 筛选数据
        base_data = pd.merge(nv_indicator, product_info[['FinProCode', 'close_open']], on='FinProCode')
        base_data = base_data[base_data['close_open'] != '数据缺失']

        base_data = base_data.dropna(
            subset=['interval_ret_annual', 'max_draw_down', 'sharpe', 'InvestmentType', 'RaisingType',
                    'close_open']).copy()
        base_data = base_data.fillna('-')
        grouped = base_data.groupby(['InvestmentType', 'RaisingType', 'close_open'])
        score_df = pd.DataFrame([])
        for type, df in grouped:
            print(type)
            tmp_df = cal_rank(df)
            score_df = score_df.append(tmp_df)







