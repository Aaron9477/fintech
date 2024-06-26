# import pandas as pd
#
# # 筛选几个投资组合作为样例
# df = pd.read_csv('石化投资组合股票交易数据_240603.csv')
# df = df[(df['PORTFOLIOID'] == 9905000399) | (df['PORTFOLIOID'] == 9905000400)]
# df.to_csv('财汇股票交易数据_240603_测试.csv', index=False, encoding='utf-8')




# import pandas as pd
#
# # 假设df_A和df_B是已经加载好的A表和B表的dataframe
# df_A = pd.read_csv('财汇股票交易数据_240603_部分测试数据.csv')  # 如果A表是CSV文件
# df_B = pd.read_csv('财汇股票行情数据_240603_移动平均线.csv')  # 如果B表是CSV文件
#
# batch_size = 1000000  # 例如，每批处理10000条记录
#
# # 从A表中获取所有唯一的STOCK_CODE
# stock_codes = df_A['STOCK_CODE'].unique()
#
# # 获取df_B的行数
# df_B_rows = df_B.shape[0]
#
# # 使用分批的方式处理数据
# for i in range(0, df_B_rows, batch_size):
#     # 获取当前批次的B表数据
#     batch_df_B = df_B.iloc[i:i + batch_size]
#
#     # 筛选出当前批次中包含A表中STOCK_CODE的股票代码
#     batch_df_B_filtered = batch_df_B[batch_df_B['SYMBOL'].isin(stock_codes)]
#
#     # 将合并后的结果写入到CSV文件中，每次写入时都添加列标题
#     batch_df_B_filtered.to_csv('财汇股票行情数据_240603_移动平均线_部分测试数据.csv', mode='a', header=(i == 0), index=False)
#
#     print(i / df_B_rows)



# # # 筛选格力电器作为分析的股票
# import pandas as pd
# df = pd.read_csv('石化投资组合股票交易数据_240603_部分测试数据.csv')
# df = df[(df['STOCK_NAME'] == '格力电器') & (df['M_NAME'] == '陈华良')]
# # 因为股票净值数据从2015年开始，所以这里做了截断
# df = df[(df['BCRQ'] >= 20160101)]
# df.to_csv('石化投资组合股票交易数据_240603_格力电器测试数据.csv', index=False, encoding='utf-8')

# import pandas as pd
# df = pd.read_csv('财汇股票行情数据_240603.csv')
# df = df[(df['SYMBOL'] == 651)]
# df.to_csv('财汇股票行情数据_240603_格力电器测试数据.csv', index=False, encoding='utf-8')





# # # 筛选璞泰来作为分析的股票
import pandas as pd
df = pd.read_csv('石化投资组合股票交易数据_240603_部分测试数据.csv')
df = df[(df['STOCK_NAME'] == '璞泰来') & (df['M_NAME'] == '刘鲁旦')]
# 因为股票净值数据从2015年开始，所以这里做了截断
df = df[(df['BCRQ'] >= 20160101)]
df.to_csv('石化投资组合股票交易数据_240603_璞泰来测试数据.csv', index=False, encoding='utf-8')


# import pandas as pd
# df = pd.read_csv('财汇股票行情数据_240603.csv')
# df = df[(df['SYMBOL'] == 603659)]
# df.to_csv('财汇股票行情数据_240603_璞泰来测试数据.csv', index=False, encoding='utf-8')