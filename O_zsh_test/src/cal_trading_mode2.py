import pandas as pd

# 假设你已经有了两个数据表 A 和 B

# 读取数据表 A 和 B
df_A = pd.read_csv('data_table_A.csv')
df_B = pd.read_csv('data_table_B.csv')

# 连接两个数据表，根据证券代码和交易日期
df_merged = pd.merge(df_A, df_B, left_on='SYMBOL', right_on='STOCK_CODE')

# 只保留投资经理在任的数据
df_merged = df_merged[(df_merged['TRADEDATE'] >= df_merged['BEG_DATE']) & (df_merged['TRADEDATE'] <= df_merged['END_DATE'])]

# 分组计算每个投资经理在每个均线信号下的交易次数和总交易金额
grouped = df_merged.groupby(['M_NAME'])

# 计算各均线信号下投资经理的总投资次数和总投资金额
total_transactions = grouped['BS'].count().reset_index(name='TOTAL_TRANSACTIONS')
total_amount = grouped['CJJE'].sum().reset_index(name='TOTAL_AMOUNT')

# 计算各均线信号下的总交易次数
total_signal_transactions = df_merged.groupby(['M_NAME', 'signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30'])['BS'].count().reset_index(name='TOTAL_SIGNAL_TRANSACTIONS')

# 计算各均线信号下的总交易金额
total_signal_amount = df_merged.groupby(['M_NAME', 'signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30'])['CJJE'].sum().reset_index(name='TOTAL_SIGNAL_AMOUNT')

# 合并总投资次数和总投资金额的数据
merged_data = pd.merge(total_transactions, total_amount, on='M_NAME')

# 计算总投资占比
merged_data['TOTAL_INVESTMENT_RATIO'] = merged_data['TOTAL_AMOUNT'] / merged_data['TOTAL_TRANSACTIONS']

# 合并总交易次数和总交易金额的数据
merged_data = pd.merge(merged_data, total_signal_transactions, on='M_NAME')

# 合并总交易次数和总交易金额的数据
merged_data = pd.merge(merged_data, total_signal_amount, on=['M_NAME', 'signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30'], how='left')

# 填充NaN值为0
merged_data.fillna(0, inplace=True)

# 计算信号下的投资次数占比
for signal in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
    merged_data[f'{signal}_TRANSACTIONS_RATIO'] = merged_data[f'TOTAL_SIGNAL_TRANSACTIONS'] / merged_data['TOTAL_TRANSACTIONS']

# 计算信号下的投资金额占比
for signal in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
    merged_data[f'{signal}_AMOUNT_RATIO'] = merged_data[f'TOTAL_SIGNAL_AMOUNT'] / merged_data['TOTAL_AMOUNT']

# 输出结果
print(merged_data)