import pandas as pd


# 假设已有一个名为 df 的 DataFrame 包含数据
# df 列名包括：'PORT_CODE', 'I_CODE', 'GYBD', 'TZSY', 'DATE'

# 1. 筛选特定时间范围内的数据
def filter_by_date(df, begin_date, end_date):
    return df[(df['DATE'] >= begin_date) & (df['DATE'] <= end_date)]


# 2. 按投资组合（PORT_CODE）和股票代码（I_CODE）进行分组，并计算求和
def calculate_sum_by_group(df):
    grouped = df.groupby(['PORT_CODE', 'I_CODE']).agg({'GYBD': 'sum', 'TZSY': 'sum'}).reset_index()
    return grouped


# 主程序流程
if __name__ == "__main__":
    # 假设 begin_date 和 end_date 是字符串格式的日期
    begin_date = '2024-01-01'
    end_date = '2024-06-01'

    # 读取数据到 DataFrame df 中，假设已经有了 df

    # 1. 筛选特定时间范围内的数据
    filtered_df = filter_by_date(df, begin_date, end_date)

    # 2. 计算求和
    result = calculate_sum_by_group(filtered_df)

    # 打印结果
    print(result)






import pandas as pd


# 假设已有一个名为 df 的 DataFrame 包含数据
# df 列名包括：'PORT_CODE', 'I_CODE', 'GYBD', 'TZSY', 'DATE'

# 假设 DataFrame C 包含列：'PORT_CODE', 'I_CODE', 其他需要的列

# 1. 筛选特定时间范围内的数据
def filter_by_date(df, begin_date, end_date):
    return df[(df['DATE'] >= begin_date) & (df['DATE'] <= end_date)]


# 2. 按投资组合（PORT_CODE）和股票代码（I_CODE）进行分组，并计算求和
def calculate_sum_by_group(df):
    grouped = df.groupby(['PORT_CODE', 'I_CODE']).agg({'GYBD': 'sum', 'TZSY': 'sum'}).reset_index()
    return grouped


# 3. 将结果与 DataFrame C 进行左连接
def merge_with_c(result_df, c_df):
    merged_df = pd.merge(result_df, c_df, on=['PORT_CODE', 'I_CODE'], how='left')
    return merged_df


# 主程序流程
if __name__ == "__main__":
    # 假设 begin_date 和 end_date 是字符串格式的日期
    begin_date = '2024-01-01'
    end_date = '2024-06-01'

    # 假设 df 是包含原始数据的 DataFrame，C 是包含表 C 数据的 DataFrame
    # 读取数据到 DataFrame df 和 DataFrame C 中

    # 1. 筛选特定时间范围内的数据
    filtered_df = filter_by_date(df, begin_date, end_date)

    # 2. 计算求和
    result = calculate_sum_by_group(filtered_df)