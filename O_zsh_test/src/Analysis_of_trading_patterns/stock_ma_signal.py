import pandas as pd

# #显示所有的列
# pd.set_option('display.max_columns', None)

# #显示所有的行
# pd.set_option('display.max_rows', 10000)


def calculate_moving_average(df):
    df['average_price_5'] = df['TCLOSE'].rolling(window=5).mean()
    df['average_price_10'] = df['TCLOSE'].rolling(window=10).mean()
    df['average_price_20'] = df['TCLOSE'].rolling(window=20).mean()
    df['average_price_30'] = df['TCLOSE'].rolling(window=30).mean()
    return df

def detect_signal_day(df):
    df['ma_5_days_signal'] = (df['average_price_5'] > df['average_price_5'].shift(1)).astype(int)
    df['ma_10_days_signal'] = (df['average_price_10'] > df['average_price_10'].shift(1)).astype(int)
    df['ma_20_days_signal'] = (df['average_price_20'] > df['average_price_20'].shift(1)).astype(int)
    df['ma_30_days_signal'] = (df['average_price_30'] > df['average_price_30'].shift(1)).astype(int)
    return df

def process_data(df, stocks):
    df = df[df['SYMBOL'].isin(stocks)]

    df['SYMBOL'] = df['SYMBOL'].astype(str)
    # 删除异常值
    df = df.dropna(subset=['TCLOSE', 'SYMBOL'])
    # 按照证券代码和交易时间排序
    df = df.sort_values(by=['SYMBOL', 'TRADEDATE'])
    df['TCLOSE'] = df.groupby('SYMBOL')['TCLOSE'].fillna(method='ffill')

    # 计算移动平均线
    df['average_price_5'] = df.groupby('SYMBOL')['TCLOSE'].transform(lambda x: x.rolling(window=5).mean())
    df['average_price_10'] = df.groupby('SYMBOL')['TCLOSE'].transform(lambda x: x.rolling(window=10).mean())
    df['average_price_20'] = df.groupby('SYMBOL')['TCLOSE'].transform(lambda x: x.rolling(window=20).mean())
    df['average_price_30'] = df.groupby('SYMBOL')['TCLOSE'].transform(lambda x: x.rolling(window=30).mean())
    # 判断信号日
    df = detect_signal_day(df)
    df.loc[df['average_price_5'].isna(), 'ma_5_days_signal'] = None
    df.loc[df['average_price_10'].isna(), 'ma_10_days_signal'] = None
    df.loc[df['average_price_20'].isna(), 'ma_20_days_signal'] = None
    df.loc[df['average_price_30'].isna(), 'ma_30_days_signal'] = None
    return df

data_path = '../财汇股票行情数据_240603.csv'
df = pd.read_csv(data_path, encoding="utf-8", error_bad_lines=False)

all_stock_turn_volume = pd.read_csv('../石化投资组合股票交易数据_240603_部分测试数据.csv')
stocks = list(set(all_stock_turn_volume['STOCK_CODE']))

# 处理数据
result_df = process_data(df, stocks)

result_df.rename(columns={'TRADEDATE': 'trade_date', 'SYMBOL': 'stock_code', 'TCLOSE': 'stock_adjclose'}, inplace=True)
result_df = result_df[['stock_code', 'trade_date', 'stock_adjclose', 'ma_5_days_signal', 'ma_10_days_signal', 'ma_20_days_signal',
                       'ma_30_days_signal']]
result_df.to_csv('财汇股票行情数据_240603_移动平均线_V2.csv', index=False, encoding='utf-8')





