import pandas as pd

# 假设 df_A 和 df_B 是您提供的两个 DataFrame
df_A = pd.read_csv('财汇股票行情数据_240603_移动平均线_部分测试数据.csv')  # 如果A表是CSV文件
df_B = pd.read_csv('财汇股票交易数据_240603_部分测试数据.csv')  # 如果B表是CSV文件

# 步骤2: 数据合并
df_merged = pd.merge(df_A, df_B, left_on=['SYMBOL', 'TRADEDATE'], right_on=['STOCK_CODE', 'BCRQ'], how='inner')

# 步骤3: 在任时间过滤
# 假设当前日期为 '2024-06-04'
current_date = '20240604'

# 过滤出投资经理在任期间的记录
df_filtered = df_merged[
    (df_merged['TRADEDATE'] >= df_merged['BEG_DATE']) &
    (df_merged['TRADEDATE'] <= df_merged['END_DATE']) &
    (df_merged['TRADEDATE'] <= current_date)
    ]

# 步骤4: 信号日过滤
# 为每个信号创建一个布尔列，值为 True 表示有信号
signal_columns = ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']
for column in signal_columns:
    df_filtered[f'signal_{column}'] = df_filtered[column] == 1

# 步骤5 & 6: 计算交易次数占比和交易规模占比
results = []
for signal_col in signal_columns:
    signal_name = signal_col.split('_')[1]  # 从列名中提取均线名称
    # 分别计算有信号和无信号的情况
    for signal in [True, False]:
        if signal:
            condition = df_filtered[f'signal_{signal_col}']
        else:
            condition = ~df_filtered[f'signal_{signal_col}']

        # 过滤出符合条件的记录
        df_signal = df_filtered[condition]

        # 计算交易次数占比
        total_trades = df_signal.groupby('M_NAME')['BS'].count()
        total_trades_signal = total_trades.sum()
        total_trades_all = df_signal.groupby('M_NAME')['BS'].count(1).sum()  # 计算总次数

        # 计算交易规模占比
        total_amount = df_signal.groupby('M_NAME')['CJJE'].sum()
        total_amount_signal = total_amount.sum()
        total_amount_all = df_signal.groupby('M_NAME')['CJJE'].sum(1).sum()  # 计算总金额

        # 存储结果
        for manager, count in total_trades.items():
            trade_ratio = (count / total_trades_all) if total_trades_all > 0 else 0
            amount_ratio = (total_amount.loc[manager] / total_amount_all) if total_amount_all > 0 else 0
            results.append({
                'Manager': manager,
                'Signal': f'signal_day_{signal_name}',
                'Signal_Present': signal,
                'Trade_Ratio': trade_ratio,
                'Amount_Ratio': amount_ratio
            })

# 步骤7: 汇总结果到 DataFrame
df_results = pd.DataFrame(results)

# 步骤8: 输出结果
print(df_results)