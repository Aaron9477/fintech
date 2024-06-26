import pandas as pd

# #显示所有的列
# pd.set_option('display.max_columns', None)

# #显示所有的行
# pd.set_option('display.max_rows', 10000)


def process_data(df):
    stocks = list(set(df['STOCK_CODE']))

    df = df[df['STOCK_CODE'].isin(stocks)]

    df['STOCK_CODE'] = df['STOCK_CODE'].astype(str)
    # 删除异常值
    df = df.dropna(subset=['STOCK_CODE', 'CJJE', 'BS'])
    # 按照证券代码和交易时间排序
    df = df.sort_values(by=['STOCK_CODE', 'BCRQ'])

    df.rename(columns={'PORTFOLIOID': 'portfolio_id', 'BCRQ': 'trade_date', 'STOCK_CODE': 'stock_code',
                              'CJJE': 'trade_volume', 'BS': 'trade_type'}, inplace=True)
    df = df[['portfolio_id', 'stock_code', 'trade_date', 'trade_volume', 'trade_type']]

    # 对同一投资组合的不同投资经理的数据做去重处理
    df.drop_duplicates(subset=['portfolio_id', 'stock_code', 'trade_date', 'trade_volume', 'trade_type'], inplace=True)

    return df


all_stock_turn_volume = pd.read_csv('../石化投资组合股票交易数据_240603_部分测试数据.csv')

# 处理数据
result_df = process_data(all_stock_turn_volume)


result_df.to_csv('股票交易详情表.csv', index=False, encoding='utf-8')





