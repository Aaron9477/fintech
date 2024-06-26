# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.signal
import datetime
#%matplotlib inline
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
plt.rcParams['axes.unicode_minus'] = False


def get_min(arr):
    try:
        return min(arr)
    except:
        return 10**10

def get_max(arr):
    try:
        return max(arr)
    except:
        return -10**10

def get_manager_stock_trade_ability(all_portfolio_stock_turn_volume, all_stock_price, all_stock_extreme_point,
                                    begin_date, end_date, ignore_edge_trading=False):
    portfolio_ids = []
    stock_names = []
    buy_left = []
    sell_left = []
    buy_right = []
    sell_right = []
    power_left = []
    power_right = []
    power_buy = []
    amount_buy = []
    power_sell = []
    amount_sell = []
    amount_left = []
    amount_right = []
    amount_buy_left = []
    amount_sell_left = []
    amount_buy_right = []
    amount_sell_right = []

    # 交易日期在begin_date和end_date之间的交易
    all_portfolio_stock_turn_volume = all_portfolio_stock_turn_volume[(all_portfolio_stock_turn_volume['backdate'] >= begin_date) &
                                        (all_portfolio_stock_turn_volume['backdate'] <= end_date)]
    portfolio_id_input = list(set(all_portfolio_stock_turn_volume['PORTFOLIOID']))

    for portfolio_id in portfolio_id_input:
        portfolio_stock_turn_volume = all_portfolio_stock_turn_volume[all_portfolio_stock_turn_volume['PORTFOLIOID'] == portfolio_id]
        stocks = list(set(portfolio_stock_turn_volume['windcode']))

        for stock in stocks:
            stock_price = all_stock_price[all_stock_price['windcode'] == stock]#[['S_DQ_ADJCLOSE']]
            stock_price = pd.DataFrame(stock_price['S_DQ_ADJCLOSE'].values, index=stock_price['backdate'].values, columns=[stock])
            stock_price = stock_price.sort_index().dropna()
            # 如果财汇股票行情表里没有该证券代码的信息，说明不是股票资产，跳过当前循环
            if len(stock_price.index) == 0:
                continue

            stock_turn_volume_origin = portfolio_stock_turn_volume[portfolio_stock_turn_volume['windcode'] == stock]
            # todo:目前使用的交易数量。可以修改成交易金额，并去掉后续代码中使用收盘价的部分
            stock_turn_volume = pd.DataFrame(stock_turn_volume_origin['BS'].replace(0, np.nan) *
                                             stock_turn_volume_origin['CJSL'].replace(0, np.nan))
            stock_turn_volume.columns = ['持仓调整']
            stock_turn_volume.index = stock_turn_volume_origin['backdate'].values
            stock_turn_volume.dropna()
            if len(stock_turn_volume.index) == 0:
                continue

            # 溪恒逻辑：过滤掉新股
            turn_start_date = stock_turn_volume_origin['backdate'].min()
            if stock_price.index[0] > turn_start_date - datetime.timedelta(days=180):
                continue

            # 日期补全
            date_completed = pd.date_range(start=stock_price.index.min(), end=stock_price.index.max())
            stock_price_completed = pd.DataFrame(stock_price, index=date_completed).fillna(method='ffill')

            stock_turn_volume['close'] = stock_price_completed.loc[stock_turn_volume.index, stock_price_completed.columns[0]]

            # 使用loc方法根据股票代码筛选对应的行
            stock_extreme_point = all_stock_extreme_point.loc[all_stock_extreme_point['stock'] == stock]

            # todo:未找到极值点的逻辑是否优化？
            # 未找到极值点，直接跳过
            if stock_extreme_point.empty:
                continue

            stock_extreme_point['extremum_date'] = pd.to_datetime(stock_extreme_point['extremum_date'])
            stock_extreme_min_dates = stock_extreme_point[stock_extreme_point['min_or_max'] == 'min']['extremum_date']
            stock_extreme_max_dates = stock_extreme_point[stock_extreme_point['min_or_max'] == 'max']['extremum_date']

            # 对日期进行排序
            stock_extreme_min_dates = np.array(stock_extreme_min_dates.sort_values())
            stock_extreme_max_dates = np.array(stock_extreme_max_dates.sort_values())

            extres = np.append(stock_extreme_min_dates, stock_extreme_max_dates)
            LR = []
            LR_power = []
            # stock_price_array = stock_price.iloc[:, 0].values
            for ind_date in stock_turn_volume.index:
                # stock_day_price = stock_price_completed.loc[ind_date, 'close']
                if ind_date <= get_min(extres):
                    stock_turn_volume = stock_turn_volume.drop(index=ind_date)
                    continue
                extre_left = extres[extres < ind_date].max()
                extre_right = extres[extres >= ind_date].min()
                buy_sell_sign = np.sign(stock_turn_volume.loc[ind_date, '持仓调整'])

                if ignore_edge_trading and (extre_left == get_min(extres) or extre_right == get_max(extres)):
                    buy_sell_sign = 0

                if extre_left in stock_extreme_min_dates:
                    LR.append(buy_sell_sign)
                else:
                    LR.append(-buy_sell_sign)

                if buy_sell_sign > 0:
                    trade_ability = (stock_price_completed.loc[ind_date].values[0] - min(stock_price_completed.loc[extre_left].values[0], stock_price_completed.loc[extre_right].values[0])) / (
                                stock_price_completed.loc[extre_right].values[0] - stock_price_completed.loc[extre_left].values[0])
                else:
                    trade_ability = (stock_price_completed.loc[ind_date].values[0] - max(stock_price_completed.loc[extre_left].values[0], stock_price_completed.loc[extre_right].values[0])) / (
                                stock_price_completed.loc[extre_right].values[0] - stock_price_completed.loc[extre_left].values[0])
                LR_power.append(trade_ability * abs(buy_sell_sign))
            stock_turn_volume['LR'] = LR
            stock_turn_volume['LR_power'] = LR_power

            # 基础信息
            portfolio_ids.append(portfolio_id)
            stock_names.append(stock)

            # 细项交易能力
            position_adj_buy_left = stock_turn_volume[(stock_turn_volume['持仓调整'] > 0) * (stock_turn_volume['LR'] < 0)]
            position_adj_sell_left = stock_turn_volume[(stock_turn_volume['持仓调整'] < 0) * (stock_turn_volume['LR'] < 0)]
            position_adj_buy_right = stock_turn_volume[(stock_turn_volume['持仓调整'] > 0) * (stock_turn_volume['LR'] > 0)]
            position_adj_sell_right = stock_turn_volume[(stock_turn_volume['持仓调整'] < 0) * (stock_turn_volume['LR'] > 0)]
            # todo:溪恒代码用100减，可能因为在计算trade_ability，计算反了。需要修改。
            buy_left.append(100 - 100 * (position_adj_buy_left['close'] * np.abs(
                position_adj_buy_left['持仓调整'] * position_adj_buy_left['LR_power'])).sum() / (
                                        position_adj_buy_left['close'] * np.abs(position_adj_buy_left['持仓调整'])).sum())
            sell_left.append(100 - 100 * (position_adj_sell_left['close'] * np.abs(
                position_adj_sell_left['持仓调整'] * position_adj_sell_left['LR_power'])).sum() / (
                                         position_adj_sell_left['close'] * np.abs(position_adj_sell_left['持仓调整'])).sum())
            buy_right.append(100 - 100 * (position_adj_buy_right['close'] * np.abs(
                position_adj_buy_right['持仓调整'] * position_adj_buy_right['LR_power'])).sum() / (
                                         position_adj_buy_right['close'] * np.abs(position_adj_buy_right['持仓调整'])).sum())
            sell_right.append(100 - 100 * (position_adj_sell_right['close'] * np.abs(
                position_adj_sell_right['持仓调整'] * position_adj_sell_right['LR_power'])).sum() / (
                                          position_adj_sell_right['close'] * np.abs(position_adj_sell_right['持仓调整'])).sum())
            amount_buy_left.append((position_adj_buy_left['close'] * np.abs(position_adj_buy_left['持仓调整'])).sum())
            amount_sell_left.append((position_adj_sell_left['close'] * np.abs(position_adj_sell_left['持仓调整'])).sum())
            amount_buy_right.append((position_adj_buy_right['close'] * np.abs(position_adj_buy_right['持仓调整'])).sum())
            amount_sell_right.append((position_adj_sell_right['close'] * np.abs(position_adj_sell_right['持仓调整'])).sum())

            # 左右交易能力
            position_adj_left = stock_turn_volume[stock_turn_volume['LR'] < 0]
            power_left.append(100 - 100 * (position_adj_left['close'] * np.abs(
                position_adj_left['持仓调整'] * position_adj_left['LR_power'])).sum() / (
                                          position_adj_left['close'] * np.abs(position_adj_left['持仓调整'])).sum())
            position_adj_right = stock_turn_volume[stock_turn_volume['LR'] > 0]
            power_right.append(100 - 100 * (position_adj_right['close'] * np.abs(
                position_adj_right['持仓调整'] * position_adj_right['LR_power'])).sum() / (
                                           position_adj_right['close'] * np.abs(position_adj_right['持仓调整'])).sum())
            amount_left.append((position_adj_left['close'] * np.abs(position_adj_left['持仓调整'])).sum())
            amount_right.append((position_adj_right['close'] * np.abs(position_adj_right['持仓调整'])).sum())

            # 买卖交易能力
            position_adj_buy = stock_turn_volume[stock_turn_volume['持仓调整'] > 0]
            position_adj_sell = stock_turn_volume[stock_turn_volume['持仓调整'] < 0]
            power_buy.append(100 - 100 * (position_adj_buy['close'] * position_adj_buy['持仓调整'] * np.abs(
                position_adj_buy['LR_power'])).sum() / (position_adj_buy['close'] * position_adj_buy['持仓调整']).sum())
            power_sell.append(100 - 100 * (position_adj_sell['close'] * position_adj_sell['持仓调整'] * np.abs(
                position_adj_sell['LR_power'])).sum() / (position_adj_sell['close'] * position_adj_sell['持仓调整']).sum())
            amount_buy.append((position_adj_buy['close'] * position_adj_buy['持仓调整']).sum())
            amount_sell.append((-position_adj_sell['close'] * position_adj_sell['持仓调整']).sum())

    BSpreference = pd.DataFrame(
        [portfolio_ids, stock_names, buy_left, sell_left, buy_right, sell_right, power_left, power_right, power_buy, power_sell,
         amount_buy_left, amount_sell_left, amount_buy_right, amount_sell_right, amount_left, amount_right, amount_buy, amount_sell],
        columns=stock_names, index=['投资组合id', '股票', '左侧买入能力', '左侧卖出能力', '右侧买入能力', '右侧卖出能力', '左侧交易能力',
                                    '右侧交易能力', '买入交易能力', '卖出交易能力', '左侧买入金额', '左侧卖出金额', '右侧买入金额',
                                    '右侧卖出金额', '左侧交易金额', '右侧交易金额', '买入交易金额', '卖出交易金额']).T
    BSpreference['个股交易总金额'] = BSpreference['买入交易金额'] + BSpreference['卖出交易金额']

    BSpreference_sorted = BSpreference.groupby('投资组合id').apply(lambda x: x.sort_values(by='个股交易总金额', ascending=False))
    BSpreference_sorted = BSpreference_sorted.reset_index(drop=True)
    BSpreference_sorted['个股交易总金额排名'] = BSpreference_sorted.groupby('投资组合id').cumcount() + 1

    return BSpreference_sorted


def get_manager_trade_ability(manager_stock_trade_ability, begin_date, end_date):
    # 定义能力列和交易金额列
    ability_columns = ['左侧买入能力', '左侧卖出能力', '右侧买入能力', '右侧卖出能力',
                       '左侧交易能力', '右侧交易能力', '买入交易能力', '卖出交易能力']
    trade_amount_columns = ['左侧买入金额', '左侧卖出金额', '右侧买入金额', '右侧卖出金额',
                            '左侧交易金额', '右侧交易金额', '买入交易金额', '卖出交易金额']

    # 按照投资组合ID分组
    grouped = manager_stock_trade_ability.groupby('投资组合id')

    # 初始化一个空的DataFrame来存储每个投资组合的加权能力
    every_manager_trade_ability = pd.DataFrame()

    # 初始化变量来存储所有组合的整体加权能力值和交易金额总和
    overall_weighted_abilities = {ability: 0 for ability in ability_columns}
    overall_trade_amount_sums = {trade: 0 for trade in trade_amount_columns}

    # 遍历分组，计算每个投资组合的能力加权平均值和交易金额总和
    for portfolio_id, group in grouped:
        # 对于每个投资组合，初始化一个字典来存储加权后的能力值
        weighted_abilities = {ability: 0 for ability in ability_columns}
        trade_amount_sums = {trade: 0 for trade in trade_amount_columns}

        # 遍历每个股票记录，计算加权能力
        for index, row in group.iterrows():
            for ability in ability_columns:
                # 对应的交易金额列
                trade_col = trade_amount_columns[ability_columns.index(ability)]
                # 只处理非空的ability值和交易金额
                if not pd.isnull(row[ability]) and not pd.isnull(row[trade_col]):
                    # 累加加权能力值和交易金额
                    weighted_abilities[ability] += row[ability] * row[trade_col]
                    trade_amount_sums[trade_col] += row[trade_col]

        # 更新整体加权能力值和交易金额总和
        for ability in ability_columns:
            overall_weighted_abilities[ability] += weighted_abilities[ability]
        for trade in trade_amount_columns:
            overall_trade_amount_sums[trade] += trade_amount_sums[trade]

        # 计算加权平均能力
        for ability in ability_columns:
            trade_col = trade_amount_columns[ability_columns.index(ability)]
            if trade_amount_sums[trade_col] > 0:
                weighted_abilities[ability] /= trade_amount_sums[trade_col]

        # 创建新的DataFrame行，包含加权后的能力值和交易金额总和
        new_row = {ability: weighted_abilities[ability] for ability in ability_columns}
        new_row.update({trade: trade_amount_sums[trade] for trade in trade_amount_columns})
        new_row['投资组合id'] = portfolio_id

        # 将新行添加到结果DataFrame中
        every_manager_trade_ability = every_manager_trade_ability.append(new_row, ignore_index=True)

    # 计算整体加权平均能力，这里需要除以整体交易金额总和
    for ability in ability_columns:
        trade_col = trade_amount_columns[ability_columns.index(ability)]
        overall_weighted_abilities[ability] /= overall_trade_amount_sums[trade_col] if overall_trade_amount_sums[trade_col] > 0 else 1
    # 创建包含整体加权能力值和交易金额总和的新DataFrame行
    overall_manager_trade_ability = {ability: overall_weighted_abilities[ability] for ability in ability_columns}
    overall_manager_trade_ability.update({trade: overall_trade_amount_sums[trade] for trade in trade_amount_columns})

    # 将整体加权能力DataFrame转换为DataFrame
    overall_manager_trade_ability = pd.DataFrame([overall_manager_trade_ability])

    every_manager_trade_ability.rename(columns={'投资组合id': 'portfolio_id', '左侧买入金额': 'buy_left_amount', '左侧卖出金额':'sell_left_amount',
                                                '右侧买入金额': 'buy_right_amount', '右侧卖出金额': 'sell_right_amount',
                                                '左侧买入能力': 'buy_left_ability', '左侧卖出能力': 'sell_left_ability',
                                                '右侧买入能力': 'buy_right_ability', '右侧卖出能力': 'sell_right_ability',}, inplace=True)
    every_manager_trade_ability['begin_date'] = begin_date
    every_manager_trade_ability['end_date'] = end_date
    every_manager_trade_ability['trade_amount'] = every_manager_trade_ability['buy_left_amount'] + every_manager_trade_ability['sell_left_amount'] \
                                                  + every_manager_trade_ability['buy_right_amount'] + every_manager_trade_ability['sell_right_amount']
    every_manager_trade_ability['buy_left_percent'] = every_manager_trade_ability['buy_left_amount'] / every_manager_trade_ability['trade_amount']
    every_manager_trade_ability['sell_left_percent'] = every_manager_trade_ability['sell_left_amount'] / every_manager_trade_ability['trade_amount']
    every_manager_trade_ability['buy_right_percent'] = every_manager_trade_ability['buy_right_amount'] / every_manager_trade_ability['trade_amount']
    every_manager_trade_ability['sell_right_percent'] = every_manager_trade_ability['sell_right_amount'] / every_manager_trade_ability['trade_amount']
    every_manager_trade_ability['trade_ability'] = every_manager_trade_ability['buy_left_ability'] * every_manager_trade_ability['buy_left_percent'] \
                                                   + every_manager_trade_ability['sell_left_ability'] * every_manager_trade_ability['sell_left_percent'] \
                                                   + every_manager_trade_ability['buy_right_ability'] * every_manager_trade_ability['buy_right_percent'] \
                                                   + every_manager_trade_ability['sell_right_ability'] * every_manager_trade_ability['sell_right_percent']

    def sort_and_insert_rankings(df):
        columns_to_rank = ['buy_left_ability', 'sell_left_ability', 'buy_right_ability', 'sell_right_ability', 'trade_ability']
        for col in columns_to_rank:
            rank_col = col.split('ability')[0] + 'rank'
            df[rank_col] = df[col].rank(method='min').astype(int).astype(str) + '/' + str(len(df))
        return df

    every_manager_trade_ability = sort_and_insert_rankings(every_manager_trade_ability)
    every_manager_trade_ability = every_manager_trade_ability[['portfolio_id', 'begin_date', 'end_date',
                                                               'buy_left_amount', 'sell_left_amount', 'buy_right_amount', 'sell_right_amount', 'trade_amount',
                                                               'buy_left_percent', 'sell_left_percent', 'buy_right_percent', 'sell_right_percent',
                                                               'buy_left_ability', 'sell_left_ability', 'buy_right_ability', 'sell_right_ability', 'trade_ability',
                                                               'buy_left_rank', 'sell_left_rank', 'buy_right_rank', 'sell_right_rank', 'trade_rank']]

    overall_manager_trade_ability['begin_date'] = begin_date
    overall_manager_trade_ability['end_date'] = end_date
    overall_manager_trade_ability.rename(columns={'左侧买入金额': 'buy_left_amount', '左侧卖出金额':'sell_left_amount',
                                                  '右侧买入金额': 'buy_right_amount', '右侧卖出金额': 'sell_right_amount',
                                                  '左侧买入能力': 'buy_left_ability', '左侧卖出能力': 'sell_left_ability',
                                                  '右侧买入能力': 'buy_right_ability', '右侧卖出能力': 'sell_right_ability',}, inplace=True)
    overall_manager_trade_ability['trade_amount'] = overall_manager_trade_ability['buy_left_amount'] + overall_manager_trade_ability['sell_left_amount'] \
                                                  + overall_manager_trade_ability['buy_right_amount'] + overall_manager_trade_ability['sell_right_amount']
    overall_manager_trade_ability['buy_left_percent'] = overall_manager_trade_ability['buy_left_amount'] / overall_manager_trade_ability['trade_amount']
    overall_manager_trade_ability['sell_left_percent'] = overall_manager_trade_ability['sell_left_amount'] / overall_manager_trade_ability['trade_amount']
    overall_manager_trade_ability['buy_right_percent'] = overall_manager_trade_ability['buy_right_amount'] / overall_manager_trade_ability['trade_amount']
    overall_manager_trade_ability['sell_right_percent'] = overall_manager_trade_ability['sell_right_amount'] / overall_manager_trade_ability['trade_amount']
    overall_manager_trade_ability['trade_ability'] = overall_manager_trade_ability['buy_left_ability'] * overall_manager_trade_ability['buy_left_percent'] \
                                                   + overall_manager_trade_ability['sell_left_ability'] * overall_manager_trade_ability['sell_left_percent'] \
                                                   + overall_manager_trade_ability['buy_right_ability'] * overall_manager_trade_ability['buy_right_percent'] \
                                                   + overall_manager_trade_ability['sell_right_ability'] * overall_manager_trade_ability['sell_right_percent']

    def calculate_min_max(df_a, df_b):
        # 指定需要计算最大最小值的列
        columns_to_calculate = ['buy_left_ability', 'sell_left_ability', 'buy_right_ability', 'sell_right_ability', 'trade_ability']

        # 计算最大值和最小值
        max_values = df_a[columns_to_calculate].max()
        min_values = df_a[columns_to_calculate].min()

        # 将每列的最大值和最小值添加到 DataFrame B 中
        for col in columns_to_calculate:
            df_b[f'{col}_max'] = [max_values[col]]
            df_b[f'{col}_min'] = [min_values[col]]

        return df_b

    overall_manager_trade_ability = calculate_min_max(every_manager_trade_ability, overall_manager_trade_ability)

    return every_manager_trade_ability, overall_manager_trade_ability


def get_fair_value_changes(TZSH_DETAIL, all_stock_turn_volume, begin_date, end_date):
    def convert_date_format(date_str):
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y%m%d')

    stock_id_list = list(set(all_stock_turn_volume['windcode']))
    TZSH_DETAIL = TZSH_DETAIL[TZSH_DETAIL['I_CODE'].isin(stock_id_list)]

    TZSH_DETAIL['T_DATE'] = pd.to_datetime(TZSH_DETAIL['T_DATE'], format='%Y/%m/%d')
    TZSH_DETAIL = TZSH_DETAIL[(TZSH_DETAIL['T_DATE'] >= begin_date) & (TZSH_DETAIL['T_DATE'] <= end_date)]

    TZSH_DETAIL = TZSH_DETAIL.groupby(['PORT_CODE', 'I_CODE']).agg({'GYBD': 'sum', 'TZSY': 'sum'}).reset_index()

    TZSH_DETAIL.rename(columns={'PORT_CODE': 'portfolio_id', 'I_CODE': 'stock_code', 'GYBD': 'fair_value_changes',
                                'TZSY': 'investment_disposal_income'}, inplace=True)
    return TZSH_DETAIL


if __name__ == '__main__':
    all_stock_turn_volume = pd.read_csv('../石化投资组合股票交易数据_240603_部分测试数据.csv')
    all_stock_price = pd.read_csv('../财汇股票行情数据_240603.csv')
    all_stock_extreme_point = pd.read_csv('财汇股票行情数据_240603_极值数据.csv')
    TZSH_DETAIL = pd.read_csv('../组合持仓明细及归因相关表_240625.csv')
    begin_date, end_date = 20200218, 20240618

    begin_date = pd.to_datetime(begin_date, format='%Y%m%d')
    end_date = pd.to_datetime(end_date, format='%Y%m%d')

    all_stock_turn_volume = all_stock_turn_volume[['PORTFOLIOID', 'STOCK_CODE', 'BCRQ', 'BS', 'CJSL', 'CJJE']]
    # 过滤同一资产组合下，相同投资经理的交易数据
    all_stock_turn_volume = all_stock_turn_volume.drop_duplicates()

    all_stock_turn_volume.rename(columns={'STOCK_CODE': 'windcode', 'BCRQ': 'backdate'}, inplace=True)
    all_stock_price.rename(columns={'SYMBOL': 'windcode', 'TCLOSE': 'S_DQ_ADJCLOSE', 'TRADEDATE': 'backdate'}, inplace=True)

    all_stock_turn_volume['backdate'] = pd.to_datetime(all_stock_turn_volume['backdate'].astype(str), format='%Y%m%d')
    all_stock_price['backdate'] = pd.to_datetime(all_stock_price['backdate'].astype(str), format='%Y%m%d')

    # 取all_stock_price时间在20150101之后的数据
    all_stock_price = all_stock_price[all_stock_price['backdate'] > '20150101']

    BSpreference = get_manager_stock_trade_ability(all_stock_turn_volume, all_stock_price, all_stock_extreme_point,
                                                   begin_date, end_date)
    portfolio_stock_trade_ability = BSpreference[['投资组合id', '股票', '买入交易能力', '卖出交易能力', '买入交易金额',
                                                  '卖出交易金额', '个股交易总金额', '个股交易总金额排名']]
    portfolio_stock_trade_ability.rename(columns={'投资组合id': 'portfolio_id', '股票': 'stock_code', '买入交易能力': 'buy_ability',
                                                  '卖出交易能力': 'sell_ability', '买入交易金额': 'buy_amount', '卖出交易金额': 'sell_amount',
                                                  '个股交易总金额': 'trade_amount', '个股交易总金额排名': 'transaction_amount_rank'}, inplace=True)

    fair_value_changes = get_fair_value_changes(TZSH_DETAIL, all_stock_turn_volume, begin_date, end_date)

    portfolio_stock_trade_ability = pd.merge(portfolio_stock_trade_ability, fair_value_changes, how='left', on=['portfolio_id', 'stock_code'])
    portfolio_stock_trade_ability.to_csv('投资组合针对单只股票交易能力.csv', index=False)

    portfolio_trade_ability, overall_manager_trade_ability = get_manager_trade_ability(BSpreference, begin_date, end_date)
    portfolio_trade_ability.to_csv('投资组合交易能力.csv', index=False)
    overall_manager_trade_ability.to_csv('整体交易能力.csv', index=False)


