import pandas as pd
from datetime import datetime, timedelta
import os

def analysis_reserves(today_date, macro_file):
    print("银行准备金：")
    # 设定目标日期和相关计算日期
    target_date = today_date - timedelta(days=2)
    one_year_ago_date = target_date - pd.DateOffset(years=1)

    # 读取Excel文件
    data = pd.read_excel(macro_file, sheet_name='存款机构准备金(周)')

    # 数据单位从十亿美元转化为万亿美元
    data['美国-美联储存款机构准备金(周)'] = data['美国-美联储存款机构准备金(周)'] / 1000

    # 转换日期列为datetime类型，便于筛选和计算
    data['日期'] = pd.to_datetime(data['日期'])

    # 排序数据按日期升序
    data = data.sort_values(by='日期').reset_index(drop=True)

    # 获取目标日期余额
    target_balance = data.loc[data['日期'] == target_date, '美国-美联储存款机构准备金(周)'].values[0]

    # 获取近一年最低值及对应日期
    lowest_balance_row = data.loc[(data['日期'] >= one_year_ago_date)]
    lowest_balance = lowest_balance_row['美国-美联储存款机构准备金(周)'].min()
    lowest_balance_date = lowest_balance_row.loc[lowest_balance_row['美国-美联储存款机构准备金(周)'] == lowest_balance, '日期'].values[0]

    # 获取最接近日期的数据
    def get_closest_balance(reference_date, data):
        """找到距离目标日期最近的数据"""
        closest_date = data.iloc[(data['日期'] - reference_date).abs().argsort()[:1]]['日期'].values[0]
        return data.loc[data['日期'] == closest_date, '美国-美联储存款机构准备金(周)'].values[0], closest_date

    # 动态环比计算
    def calculate_dynamic_change(target_date, offset, data):
        """
        动态计算环比：
        1. 先找目标日期的 offset 数据。
        2. 基于 offset 数据，再向前找相同的 offset 数据。
        """
        first_balance, first_date = get_closest_balance(target_date + offset, data)
        first_date_timestamp = pd.Timestamp(first_date)
        second_balance, second_date = get_closest_balance(first_date_timestamp + offset, data)
        second_date_timestamp = pd.Timestamp(second_date)
        return first_balance, second_balance, first_date_timestamp, second_date_timestamp

    # 计算目标日期对应的环比数据
    previous_week_balance, two_weeks_ago_balance, week_date, prev_week_date = calculate_dynamic_change(target_date, pd.Timedelta(weeks=-1), data)
    previous_month_balance, two_months_ago_balance, month_date, prev_month_date = calculate_dynamic_change(target_date, pd.DateOffset(months=-1), data)
    previous_quarter_balance, two_quarters_ago_balance, quarter_date, prev_quarter_date = calculate_dynamic_change(target_date, pd.DateOffset(months=-3), data)

    # 计算环比变化
    def calculate_percentage_change(current, previous):
        return (current - previous) / previous * 100 if previous else None

    week_on_week = calculate_percentage_change(target_balance, previous_week_balance)
    month_on_month = calculate_percentage_change(target_balance, previous_month_balance)
    quarter_on_quarter = calculate_percentage_change(target_balance, previous_quarter_balance)

    week_on_week_prev = calculate_percentage_change(previous_week_balance, two_weeks_ago_balance)
    month_on_month_prev = calculate_percentage_change(previous_month_balance, two_months_ago_balance)
    quarter_on_quarter_prev = calculate_percentage_change(previous_quarter_balance, two_quarters_ago_balance)

    # 格式化输出
    def format_percentage(value):
        return f"+{value:.2f}%" if value > 0 else f"{value:.2f}%" if value is not None else "N/A"

    # 生成统计文本
    report = f"""
{target_date.strftime('%Y-%m-%d')}余额为{target_balance:.2f}万亿美元
周环比{format_percentage(week_on_week)}，上周环比{format_percentage(week_on_week_prev)}
月环比{format_percentage(month_on_month)}，上月环比{format_percentage(month_on_month_prev)}
季环比{format_percentage(quarter_on_quarter)}，上季环比{format_percentage(quarter_on_quarter_prev)}
近一年最低值: {pd.Timestamp(lowest_balance_date).strftime('%Y-%m-%d')}，余额：{lowest_balance:.2f}万亿美元
    """

    # report = f"""
    # {target_date.strftime('%Y-%m-%d')}余额为{target_balance:.2f}万亿美元
    # 周环比{format_percentage(week_on_week)}，上周环比{format_percentage(week_on_week_prev)}（基于{week_date.date()}和{prev_week_date.date()}）
    # 月环比{format_percentage(month_on_month)}，上月环比{format_percentage(month_on_month_prev)}（基于{month_date.date()}和{prev_month_date.date()}）
    # 季环比{format_percentage(quarter_on_quarter)}，上季环比{format_percentage(quarter_on_quarter_prev)}（基于{quarter_date.date()}和{prev_quarter_date.date()}）
    # 近一年最低值: {pd.Timestamp(lowest_balance_date).strftime('%Y-%m-%d')}，余额：{lowest_balance:.2f}万亿美元
    # """

    # 输出统计文本
    print(report)



def analysis_ONRPP(today_date, macro_file):
    print("隔夜逆回购：")

    # 定义一周的时间范围
    end_date = today_date - timedelta(days=1)
    start_date = end_date - timedelta(weeks=1) + timedelta(days=1)

    # 读取Excel文件
    df = pd.read_excel(macro_file, sheet_name='ON RRP')

    df['美国-美联储隔夜逆回购操作(ON RRP)'] = df['美国-美联储隔夜逆回购操作(ON RRP)'] / 100

    # 确保日期列是datetime类型，并且数值列是float类型
    df.columns = ['Date', 'Value']
    df['Date'] = pd.to_datetime(df['Date'])
    df['Value'] = df['Value'].astype(float)

    # 获取本周的数据
    this_week_data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # 计算本周均值
    this_week_mean = this_week_data['Value'].mean()

    # 计算本周单日最低值
    this_week_min = this_week_data['Value'].min()
    this_week_min_date = this_week_data.loc[this_week_data['Value'].idxmin(), 'Date']

    # 获取上一自然周的数据
    last_week_start, last_week_end = start_date - timedelta(weeks=1), end_date - timedelta(weeks=1)
    last_week_data = df[(df['Date'] >= last_week_start) & (df['Date'] <= last_week_end)]

    # 计算上一周均值
    last_week_mean = last_week_data['Value'].mean()

    # 计算周环比
    week_on_week_change = ((this_week_mean / last_week_mean) - 1) * 100 if last_week_mean != 0 else float('inf')

    # 计算近一年最低值
    one_year_ago = end_date - timedelta(days=365)
    one_year_data = df[(df['Date'] >= one_year_ago) & (df['Date'] <= end_date)]
    one_year_min = one_year_data['Value'].min()
    one_year_min_date = one_year_data.loc[one_year_data['Value'].idxmin(), 'Date']

    # 打印结果
    print(f"本周（{start_date.strftime('%Y-%m-%d')}-{end_date.strftime('%Y-%m-%d')}）均值 {this_week_mean:.2f} 万亿美元，周环比 {week_on_week_change:+.2f}%")
    print(f"本周单日最低值为 {this_week_min_date.strftime('%Y-%m-%d')} 的 {this_week_min:.2f} 万亿美元")
    print(f"近一年最低值为 {one_year_min_date.strftime('%Y-%m-%d')} 的 {one_year_min:.2f} 万亿美元")


def add_blank_lines(today_date, file_path):
    print("稳定币市值记录表增加行")

    target_date = today_date - timedelta(days=1)
    today_str = today_date.strftime("%Y%m%d")
    output_file = f"../docs/稳定币市值记录_{today_str}.xlsx"
    if os.path.exists(output_file):
        print(f"文件 {output_file} 已存在，不进行覆盖。")
        return

    # 计算需要插入的日期
    dates_to_insert = [
        target_date,
        target_date - timedelta(weeks=1),
        target_date - timedelta(weeks=2),
        target_date - pd.DateOffset(months=1),
        target_date - pd.DateOffset(months=2),
        target_date - pd.DateOffset(months=3),
        target_date - pd.DateOffset(months=6),
    ]

    # 处理每个 Sheet
    new_data = {}
    sheets = ["USDT", "USDC"]
    for sheet in sheets:
        # 读取数据
        df = pd.read_excel(file_path, sheet_name=sheet)

        # 确保时间列为 datetime 类型
        df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], format="%Y%m%d")

        # 找出数据中已存在的日期
        existing_dates = set(df.iloc[:, 0])

        # 过滤掉已经存在的日期
        missing_dates = [d for d in dates_to_insert if d not in existing_dates]

        # 如果没有需要插入的日期，则跳过处理
        if not missing_dates:
            new_data[sheet] = df
            continue

        # 创建需要插入的空行
        new_rows = pd.DataFrame({df.columns[0]: missing_dates})

        # 其余列填充 NaN
        for col in df.columns[1:]:
            new_rows[col] = None

        # 合并数据并去重排序
        df = pd.concat([df, new_rows]).sort_values(by=df.columns[0]).reset_index(drop=True)

        # 保存处理后的数据
        new_data[sheet] = df

    # 保存到新的 Excel 文件
    with pd.ExcelWriter(output_file) as writer:
        for sheet, df in new_data.items():
            df.to_excel(writer, sheet_name=sheet, index=False)

    print(f"处理完成，文件已保存：{output_file}")



# def analysis_USDT():
#     def load_and_process_data(file_path, sheet_name):
#         # 读取Excel文件
#         data = pd.read_excel(file_path, sheet_name=sheet_name)
#
#         # 确保日期列是datetime类型，并且数值列是float类型
#         data.columns = ['Date', 'MarketCap']
#         data['Date'] = pd.to_datetime(data['Date'])
#         data['MarketCap'] = data['MarketCap'].astype(float) / 1000  # 转换为万亿美元
#
#         return data.sort_values(by='Date').reset_index(drop=True)
#
#     def calculate_changes(target_date, data):
#         target_data = data[data['Date'] <= target_date].iloc[-1]
#         target_market_cap = target_data['MarketCap']
#
#         week_ago_data = data[(data['Date'] > target_date - pd.Timedelta(weeks=1)) & (data['Date'] < target_date)].iloc[
#             0]
#         month_ago_data = \
#         data[(data['Date'] > target_date - pd.DateOffset(months=1)) & (data['Date'] < target_date)].iloc[0]
#         quarter_ago_data = \
#         data[(data['Date'] > target_date - pd.DateOffset(months=3)) & (data['Date'] < target_date)].iloc[0]
#
#         def calc_change(current, previous):
#             return ((current - previous) / previous * 100) if previous != 0 else float('inf')
#
#         week_on_week = calc_change(target_market_cap, week_ago_data['MarketCap'])
#         month_on_month = calc_change(target_market_cap, month_ago_data['MarketCap'])
#         quarter_on_quarter = calc_change(target_market_cap, quarter_ago_data['MarketCap'])
#
#         prev_week_on_week = calc_change(week_ago_data['MarketCap'], data[
#             (data['Date'] > week_ago_data['Date'] - pd.Timedelta(weeks=1)) & (
#                         data['Date'] < week_ago_data['Date'])].iloc[0]['MarketCap'])
#         prev_month_on_month = calc_change(month_ago_data['MarketCap'], data[
#             (data['Date'] > month_ago_data['Date'] - pd.DateOffset(months=1)) & (
#                         data['Date'] < month_ago_data['Date'])].iloc[0]['MarketCap'])
#         prev_quarter_on_quarter = calc_change(quarter_ago_data['MarketCap'], data[
#             (data['Date'] > quarter_ago_data['Date'] - pd.DateOffset(months=3)) & (
#                         data['Date'] < quarter_ago_data['Date'])].iloc[0]['MarketCap'])
#
#         return target_market_cap, week_on_week, prev_week_on_week, month_on_month, prev_month_on_month, quarter_on_quarter, prev_quarter_on_quarter
#
#     def format_report(target_date, market_cap, week_on_week, prev_week_on_week, month_on_month, prev_month_on_month,
#                       quarter_on_quarter, prev_quarter_on_quarter):
#         def format_percentage(value):
#             return f"+{value:.2f}%" if value >= 0 else f"{value:.2f}%"
#
#         report = (
#             f"截至{target_date.strftime('%m月%d日')}，市值达{market_cap:.2f}万亿美元\n"
#             f"周环比{format_percentage(week_on_week)}，上周环比{format_percentage(prev_week_on_week)}\n"
#             f"月环比{format_percentage(month_on_month)}，上月环比{format_percentage(prev_month_on_month)}\n"
#             f"季环比{format_percentage(quarter_on_quarter)}，上季环比{format_percentage(prev_quarter_on_quarter)}"
#         )
#         return report
#
#     # 主程序
#     file_path = '../docs/宏观数据.xlsx'
#     sheet_name = 'USDT_coinmarketcap'
#     target_date = pd.Timestamp('2024-11-29')
#
#     data = load_and_process_data(file_path, sheet_name)
#     market_cap, week_on_week, prev_week_on_week, month_on_month, prev_month_on_month, quarter_on_quarter, prev_quarter_on_quarter = calculate_changes(
#         target_date, data)
#
#     report = format_report(target_date, market_cap, week_on_week, prev_week_on_week, month_on_month,
#                            prev_month_on_month, quarter_on_quarter, prev_quarter_on_quarter)
#     print(report)


if __name__ == '__main__':
    today_date = datetime(2025, 2, 21)
    macro_file = '../docs/宏观数据.xlsx'

    # 准备金、逆回购计算
    analysis_reserves(today_date, macro_file)
    analysis_ONRPP(today_date, macro_file)

    # U需要填充的日期，增加行
    market_cap_file = "../docs/稳定币市值记录_20250214.xlsx"
    # add_blank_lines(today_date, market_cap_file)

    # 暂时无用
    # analysis_USDT()