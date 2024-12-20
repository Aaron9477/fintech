import pandas as pd

# 假设这是你的原始DataFrame
data = {
    'PORTFOLIOID': [1, 2, 3, 4],
    'stock_code': ['000001', '000001', '000002', '000002'],
    'stock_name': ['深发展A', '平安银行', '某公司A', '某公司B'],
    'position_start_day': ['20240101', '20240102', '20240104', '20240105']
}

df = pd.DataFrame(data)

df = df.sort_values(by=['stock_code', 'position_start_day'])
# 找到每个股票代码的最新名称
latest_names = df.groupby('stock_code')['stock_name'].apply(lambda x: x.iloc[-1]).reset_index()

# 合并DataFrame来更新股票名称
df = df.merge(latest_names, on='stock_code', suffixes=('', '_latest'))

# 更新stock_name列
df['stock_name'] = df['stock_name_latest']
del df['stock_name_latest']
print(df)