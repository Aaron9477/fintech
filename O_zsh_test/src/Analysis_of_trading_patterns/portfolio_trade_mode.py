import pandas as pd


def get_trade_mode(all_stock_ma_price, all_portfolio_stock_turn_volume, begin_date, end_date):
    # todo:begin_date是否有为空的情况？
    # todo:end_date是否有投资经理不在任，还为空的情况
    current_date = int(pd.to_datetime('today').date().strftime('%Y%m%d'))
    all_portfolio_stock_turn_volume['BEG_DATE'] = pd.to_datetime(all_portfolio_stock_turn_volume['BEG_DATE'].astype(str))\
        .dt.strftime('%Y%m%d').fillna(-1).astype(int)
    all_portfolio_stock_turn_volume['END_DATE'] = pd.to_datetime(all_portfolio_stock_turn_volume['END_DATE'].astype(str))\
        .dt.strftime('%Y%m%d').fillna(current_date).astype(int)

    # 交易日期在begin_date和end_date之间的交易
    all_portfolio_stock_turn_volume = all_portfolio_stock_turn_volume[(all_portfolio_stock_turn_volume['BCRQ'] >= begin_date) &
                                        (all_portfolio_stock_turn_volume['BCRQ'] <= end_date)]
    portfolio_id_input = list(set(all_portfolio_stock_turn_volume['PORTFOLIOID']))

    # 初始化一个空的DataFrame来存储结果
    results = pd.DataFrame()
    for portfolio_id in portfolio_id_input:
        portfolio_stock_turn_volume = all_portfolio_stock_turn_volume[all_portfolio_stock_turn_volume['PORTFOLIOID'] == portfolio_id]

        df_merged = pd.merge(portfolio_stock_turn_volume, all_stock_ma_price, left_on=['STOCK_CODE', 'BCRQ'],
                             right_on=['stock_code', 'trade_date'], how='inner')

        # 遍历四个均线信号
        for signal_col in ['ma_5_days_signal', 'ma_10_days_signal', 'ma_20_days_signal', 'ma_30_days_signal']:
            # 分别计算买入和卖出的信号和没信号的交易次数和交易规模
            signal_present_buy = df_merged[(df_merged[signal_col] == 1) & (df_merged['BS'] == 1)]
            signal_absent_buy = df_merged[(df_merged[signal_col] == 0) & (df_merged['BS'] == 1)]
            signal_present_sell = df_merged[(df_merged[signal_col] == 1) & (df_merged['BS'] == -1)]
            signal_absent_sell = df_merged[(df_merged[signal_col] == 0) & (df_merged['BS'] == -1)]

            # 计算总的买入和卖出交易次数和交易规模
            # 计算买入和卖出的交易次数
            total_buy_trades = signal_present_buy['BS'].count() + signal_absent_buy['BS'].count()
            total_sell_trades = signal_present_sell['BS'].count() + signal_absent_sell['BS'].count()
            # 计算买入和卖出的交易金额
            total_buy_amount = signal_present_buy['CJJE'].sum() + signal_absent_buy['CJJE'].sum()
            total_sell_amount = signal_present_sell['CJJE'].sum() + signal_absent_sell['CJJE'].sum()

            # 计算有信号和没信号的买入和卖出的交易次数和交易金额
            signal_present_buy_trades = signal_present_buy['BS'].count()
            signal_absent_buy_trades = signal_absent_buy['BS'].count()
            signal_present_sell_trades = signal_present_sell['BS'].count()
            signal_absent_sell_trades = signal_absent_sell['BS'].count()

            signal_present_buy_amount = signal_present_buy['CJJE'].sum()
            signal_absent_buy_amount = signal_absent_buy['CJJE'].sum()
            signal_present_sell_amount = signal_present_sell['CJJE'].sum()
            signal_absent_sell_amount = signal_absent_sell['CJJE'].sum()

            # 计算买入和卖出的信号占比
            trade_ratio_present_buy = signal_present_buy_trades / total_buy_trades
            trade_ratio_absent_buy = signal_absent_buy_trades / total_buy_trades
            amount_ratio_present_buy = signal_present_buy_amount / total_buy_amount
            amount_ratio_absent_buy = signal_absent_buy_amount / total_buy_amount
            trade_ratio_present_sell = signal_present_sell_trades / total_sell_trades
            trade_ratio_absent_sell = signal_absent_sell_trades / total_sell_trades
            amount_ratio_present_sell = signal_present_sell_amount / total_sell_amount
            amount_ratio_absent_sell = signal_absent_sell_amount / total_sell_amount

            # 步骤7：结果汇总
            result = {
                'portfolio_id': portfolio_id,
                'begin_date': begin_date,
                'end_date': end_date,
                'ma_signal_type': signal_col,
                'buy_count': total_buy_trades,
                'sell_count': total_sell_trades,
                'buy_amount': total_buy_amount,
                'sell_amount': total_sell_amount,
                'signal_present_buy_count_ratio': trade_ratio_present_buy,
                'signal_absent_buy_count_ratio': trade_ratio_absent_buy,
                'signal_present_sell_count_ratio': trade_ratio_present_sell,
                'signal_absent_sell_count_ratio': trade_ratio_absent_sell,
                'signal_present_buy_amount_ratio': amount_ratio_present_buy,
                'signal_absent_buy_amount_ratio': amount_ratio_absent_buy,
                'signal_present_sell_amount_ratio': amount_ratio_present_sell,
                'signal_absent_sell_amount_ratio': amount_ratio_absent_sell
            }
            results = results.append(result, ignore_index=True)

    results = results[['portfolio_id', 'begin_date', 'end_date', 'ma_signal_type', 'buy_count', 'sell_count', 'buy_amount',
                       'sell_amount', 'signal_present_buy_count_ratio', 'signal_absent_buy_count_ratio', 'signal_present_sell_count_ratio',
                       'signal_absent_sell_count_ratio', 'signal_present_buy_amount_ratio', 'signal_absent_buy_amount_ratio',
                       'signal_present_sell_amount_ratio', 'signal_absent_sell_amount_ratio']]
    # 步骤8：输出结果
    results.to_csv('investment_manager_signalsV4.csv', index=False)


if __name__ == '__main__':
    all_stock_ma_price = pd.read_csv('财汇股票行情数据_240603_移动平均线_V2.csv')  # 如果A表是CSV文件
    all_portfolio_stock_turn_volume = pd.read_csv('../石化投资组合股票交易数据_240603_部分测试数据.csv')  # 如果B表是CSV文件

    all_portfolio_stock_turn_volume.drop_duplicates(subset=['PORTFOLIOID', 'STOCK_CODE', 'BCRQ', 'BS', 'CJSL', 'CJJE'],
                                                    inplace=True)

    begin_date, end_date = 20200218, 20240618
    get_trade_mode(all_stock_ma_price, all_portfolio_stock_turn_volume, begin_date, end_date)
