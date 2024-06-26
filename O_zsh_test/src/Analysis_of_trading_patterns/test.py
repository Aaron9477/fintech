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

# 初始化用于存储加权比例的字典，每个均线信号分别计算
weighted_trade_counts = {
    'signal_day_5': {'buy': 0, 'sell': 0},
    'signal_day_10': {'buy': 0, 'sell': 0},
    'signal_day_20': {'buy': 0, 'sell': 0},
    'signal_day_30': {'buy': 0, 'sell': 0}}

weighted_trade_volumes = {
    'signal_day_5': {'buy': 0, 'sell': 0},
    'signal_day_10': {'buy': 0, 'sell': 0},
    'signal_day_20': {'buy': 0, 'sell': 0},
    'signal_day_30': {'buy': 0, 'sell': 0}}

# 遍历每个投资组合的结果
for result in results:
    for signal_col in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
        # 累加每个均线信号的总买入和卖出次数
        total_market_trade_counts[signal_col]['buy'] += result['Total_Buy_Trades']
        total_market_trade_counts[signal_col]['sell'] += result['Total_Sell_Trades']

        # 累加每个均线信号的买入和卖出交易规模
        total_market_trade_volumes[signal_col]['buy'] += abs(result['Total_Buy_Amount'])
        total_market_trade_volumes[signal_col]['sell'] += abs(result['Total_Sell_Amount'])

        # 累加每个均线信号的买入和卖出的信号交易次数、规模以及相应的加权比例
        # ... 同上 ...

# 计算每个均线信号的加权平均买入和卖出比例
weighted_averages_trade_counts = {
    # ... 计算交易次数的加权平均 ...
}

weighted_averages_trade_volumes = {
    # ... 计算交易规模的加权平均 ...
}

# 遍历每个均线信号
for signal_col in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
    # 计算交易次数的加权平均
    weighted_averages_trade_counts[signal_col] = {
        'Weighted_Avg_Signal_Present_Buy': weighted_ratios[signal_col]['present_buy'] /
                                           total_market_trade_counts[signal_col]['buy'],
        'Weighted_Avg_Signal_Absent_Buy': weighted_ratios[signal_col]['absent_buy'] /
                                          total_market_trade_counts[signal_col]['buy'],
        'Weighted_Avg_Signal_Present_Sell': weighted_ratios[signal_col]['present_sell'] /
                                            total_market_trade_counts[signal_col]['sell'],
        'Weighted_Avg_Signal_Absent_Sell': weighted_ratios[signal_col]['absent_sell'] /
                                           total_market_trade_counts[signal_col]['sell']
    }

    # 计算交易规模的加权平均
    weighted_averages_trade_volumes[signal_col] = {
        'Weighted_Avg_Signal_Present_Buy': weighted_trade_volumes[signal_col]['present_buy'] /
                                           total_market_trade_volumes[signal_col]['buy'],
        'Weighted_Avg_Signal_Absent_Buy': weighted_trade_volumes[signal_col]['absent_buy'] /
                                          total_market_trade_volumes[signal_col]['buy'],
        'Weighted_Avg_Signal_Present_Sell': weighted_trade_volumes[signal_col]['present_sell'] /
                                            total_market_trade_volumes[signal_col]['sell'],
        'Weighted_Avg_Signal_Absent_Sell': weighted_trade_volumes[signal_col]['absent_sell'] /
                                           total_market_trade_volumes[signal_col]['sell']
    }

# 输出每个均线信号的全市场整体交易偏好
for signal_col in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
    print(f"均线信号 {signal_col} 的全市场整体交易偏好：")
    print("交易次数加权平均：")
    for key, value in weighted_averages_trade_counts[signal_col].items():
        print(f"{key}: {value:.2%}")
    print("交易规模加权平均：")
    for key, value in weighted_averages_trade_volumes[signal_col].items():
        print(f"{key}: {value:.2%}")