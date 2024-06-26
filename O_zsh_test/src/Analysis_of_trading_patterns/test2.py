total_market_trade_counts = {
    'signal_day_5': {'buy': 0, 'sell': 0},
    'signal_day_10': {'buy': 0, 'sell': 0},
    'signal_day_20': {'buy': 0, 'sell': 0},
    'signal_day_30': {'buy': 0, 'sell': 0}
}

total_market_trade_volumes = {
    'signal_day_5': {'buy': 0, 'sell': 0},
    'signal_day_10': {'buy': 0, 'sell': 0},
    'signal_day_20': {'buy': 0, 'sell': 0},
    'signal_day_30': {'buy': 0, 'sell': 0}
}

# 初始化用于存储每个均线信号的加权交易次数和交易规模的字典
weighted_sums = {
    'signal_day_5': {'present_buy_trades': 0, 'absent_buy_trades': 0, 'present_sell_trades': 0, 'absent_sell_trades': 0,
                     'present_buy_volume': 0, 'absent_buy_volume': 0, 'present_sell_volume': 0,
                     'absent_sell_volume': 0},
    'signal_day_10': {'present_buy_trades': 0, 'absent_buy_trades': 0, 'present_sell_trades': 0,
                      'absent_sell_trades': 0,
                      'present_buy_volume': 0, 'absent_buy_volume': 0, 'present_sell_volume': 0,
                      'absent_sell_volume': 0},
    'signal_day_20': {'present_buy_trades': 0, 'absent_buy_trades': 0, 'present_sell_trades': 0,
                      'absent_sell_trades': 0,
                      'present_buy_volume': 0, 'absent_buy_volume': 0, 'present_sell_volume': 0,
                      'absent_sell_volume': 0},
    'signal_day_30': {'present_buy_trades': 0, 'absent_buy_trades': 0, 'present_sell_trades': 0,
                      'absent_sell_trades': 0,
                      'present_buy_volume': 0, 'absent_buy_volume': 0, 'present_sell_volume': 0,
                      'absent_sell_volume': 0}
}

# 遍历每个投资组合的结果
for index, result in results.iterrows():
    for signal_col in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
        # 累加每个均线信号的总买入和卖出次数
        total_market_trade_counts[signal_col]['buy'] += result['Total_Buy_Trades']
        total_market_trade_counts[signal_col]['sell'] += result['Total_Sell_Trades']

        # 累加每个均线信号的买入和卖出交易规模
        total_market_trade_volumes[signal_col]['buy'] += abs(result['Total_Buy_Amount'])
        total_market_trade_volumes[signal_col]['sell'] += abs(result['Total_Sell_Amount'])

        # 累加每个均线信号的加权交易次数和交易规模
        weighted_sums[signal_col]['present_buy_trades'] += result['Signal_Present_Buy_Trades'] * result[
            'Trade_Ratio_Signal_Present_Buy']
        weighted_sums[signal_col]['absent_buy_trades'] += result['Signal_Absent_Buy_Trades'] * result[
            'Trade_Ratio_Signal_Absent_Buy']
        weighted_sums[signal_col]['present_sell_trades'] += result['Signal_Present_Sell_Trades'] * result[
            'Trade_Ratio_Signal_Present_Sell']
        weighted_sums[signal_col]['absent_sell_trades'] += result['Signal_Absent_Sell_Trades'] * result[
            'Trade_Ratio_Signal_Absent_Sell']

        weighted_sums[signal_col]['present_buy_volume'] += abs(result['Signal_Present_Buy_Amount']) * result[
            'Amount_Ratio_Signal_Present_Buy']
        weighted_sums[signal_col]['absent_buy_volume'] += abs(result['Signal_Absent_Buy_Amount']) * result[
            'Amount_Ratio_Signal_Absent_Buy']
        weighted_sums[signal_col]['present_sell_volume'] += abs(result['Signal_Present_Sell_Amount']) * result[
            'Amount_Ratio_Signal_Present_Sell']
        weighted_sums[signal_col]['absent_sell_volume'] += abs(result['Signal_Absent_Sell_Amount']) * result[
            'Amount_Ratio_Signal_Absent_Sell']

# 计算每个均线信号的加权平均买入和卖出比例
weighted_averages = {}
for signal_col in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
    weighted_averages[signal_col] = {
        'Weighted_Avg_Trade_Present_Buy': weighted_sums[signal_col]['present_buy_trades'] /
                                          total_market_trade_counts[signal_col]['buy'],
        'Weighted_Avg_Trade_Absent_Buy': weighted_sums[signal_col]['absent_buy_trades'] /
                                         total_market_trade_counts[signal_col]['buy'],
        'Weighted_Avg_Trade_Present_Sell': weighted_sums[signal_col]['present_sell_trades'] /
                                           total_market_trade_counts[signal_col]['sell'],
        'Weighted_Avg_Avg_Trade_Absent_Sell': weighted_sums[signal_col]['absent_sell_trades'] /
                                              total_market_trade_counts[signal_col]['sell'],
        'Weighted_Avg_Volume_Present_Buy': weighted_sums[signal_col]['present_buy_volume'] /
                                           total_market_trade_volumes[signal_col]['buy'],
        'Weighted_Avg_Volume_Absent_Buy': weighted_sums[signal_col]['absent_buy_volume'] /
                                          total_market_trade_volumes[signal_col]['buy'],
        'Weighted_Avg_Volume_Present_Sell': weighted_sums[signal_col]['present_sell_volume'] /
                                            total_market_trade_volumes[signal_col]['sell'],
        'Weighted_Avg_Volume_Absent_Sell': weighted_sums[signal_col]['absent_sell_volume'] /
                                           total_market_trade_volumes[signal_col]['sell']
    }

# 打印每个均线信号的全市场整体交易偏好
for signal_col, averages in weighted_averages.items():
    print(f"\n均线信号 {signal_col} 的全市场整体交易偏好：")
    for key, value in averages.items():
        print(f"{key}: {value:.4f}")