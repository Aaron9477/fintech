import pandas as pd

# 假设你已经有了两个数据表 A 和 B

import pandas as pd

# 示例数据加载，实际使用时请替换为实际的数据加载代码
df_A = pd.read_csv('财汇股票行情数据_240603_移动平均线_部分测试数据.csv')  # 如果A表是CSV文件
df_B = pd.read_csv('财汇股票交易数据_240603_部分测试数据_更少的数据.csv')  # 如果B表是CSV文件

# 步骤2：数据连接
# 通过SYMBOL、TRADEDATE和STOCK_CODE、BCRQ连接A表和B表
df_merged = pd.merge(df_A, df_B, left_on=['SYMBOL', 'TRADEDATE'], right_on=['STOCK_CODE', 'BCRQ'])

# 步骤3：筛选交易日期
# 筛选投资经理在任期间的交易记录
df_filtered = df_merged.copy()
df_filtered['BEG_DATE'] = pd.to_datetime(df_filtered['BEG_DATE'].astype(str)).dt.strftime('%Y%m%d').fillna(-1).astype(int)
df_filtered['END_DATE'] = pd.to_datetime(df_filtered['END_DATE'].astype(str)).dt.strftime('%Y%m%d').fillna(99999999).astype(int)

# 只保留在任期间的交易记录
df_filtered = df_filtered[
    (df_filtered['BCRQ'] >= df_filtered['BEG_DATE']) & (df_filtered['BCRQ'] <= df_filtered['END_DATE'])]

# 步骤4和5：计算交易次数和交易规模
# 初始化一个空的DataFrame来存储结果
results = pd.DataFrame()

# 遍历四个均线信号
for signal_col in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
    # 按投资经理名称和信号列进行分组
    grouped = df_filtered.groupby(['M_NAME'])

    for name, group in grouped:
        # 计算有信号和没信号的交易次数和交易规模
        signal_present = group[group[signal_col] == 1]
        signal_absent = group[group[signal_col] == 0]

        total_trades = group['BS'].count()
        total_amount = group['CJJE'].sum()

        signal_present_trades = signal_present['BS'].count()
        signal_absent_trades = signal_absent['BS'].count()

        signal_present_amount = signal_present['CJJE'].sum()
        signal_absent_amount = signal_absent['CJJE'].sum()

        # 步骤6：计算占比
        trade_ratio_present = signal_present_trades / total_trades
        trade_ratio_absent = signal_absent_trades / total_trades
        amount_ratio_present = signal_present_amount / total_amount
        amount_ratio_absent = signal_absent_amount / total_amount

        # 步骤7：结果汇总
        result = {
            'Investment_Manager': name,
            'Signal_Column': signal_col,
            'Signal_Present': 1,
            'Trades_Present': signal_present_trades,
            'Trades_Absent': signal_absent_trades,
            'Trade_Ratio_Present': trade_ratio_present,
            'Trade_Ratio_Absent': trade_ratio_absent,
            'Amount_Present': signal_present_amount,
            'Amount_Absent': signal_absent_amount,
            'Amount_Ratio_Present': amount_ratio_present,
            'Amount_Ratio_Absent': amount_ratio_absent
        }
        results = results.append(result, ignore_index=True)

# 步骤8：输出结果
results.to_csv('investment_manager_signals.csv', index=False)
