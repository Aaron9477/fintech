import pandas as pd
from datetime import datetime, timedelta


def calculate_growth(df, date_A):
    df['日期'] = pd.to_datetime(df['日期'], errors='coerce').dt.date  # 仅保留年月日
    df = df.sort_values(by='日期')  # 按日期排序

    # 定义时间间隔
    week_delta = pd.DateOffset(weeks=1)
    month_delta = pd.DateOffset(months=1)
    quarter_delta = pd.DateOffset(months=3)

    # 查找最接近 date_A 的日期
    date_A = df.iloc[(pd.to_datetime(df['日期']) - pd.to_datetime(date_A)).abs().argsort()[:1]]['日期'].values[0]
    index_A = df[df['日期'] == date_A].index[0]

    # 获取 A 的前一周、前一月、前一季度的索引
    date_A_week = date_A - week_delta
    date_A_month = date_A - month_delta
    date_A_quarter = date_A - quarter_delta

    def get_index(date):
        row = df.iloc[(pd.to_datetime(df['日期']) - pd.to_datetime(date)).abs().argsort()[:1]]
        return row.index[0] if not row.empty else None

    index_A_week = get_index(date_A_week)
    index_A_month = get_index(date_A_month)
    index_A_quarter = get_index(date_A_quarter)

    # 计算同比增减
    def compute_change(current, previous):
        return ((current - previous) / previous) if previous else None

    week_change = month_change = quarter_change = None
    prev_week_change = prev_month_change = prev_quarter_change = None

    if index_A_week is not None:
        week_change = compute_change(df.at[index_A, '市值'], df.at[index_A_week, '市值'])
        df.loc[index_A, '周'] = week_change
    if index_A_month is not None:
        month_change = compute_change(df.at[index_A, '市值'], df.at[index_A_month, '市值'])
        df.loc[index_A, '月'] = month_change
    if index_A_quarter is not None:
        quarter_change = compute_change(df.at[index_A, '市值'], df.at[index_A_quarter, '市值'])
        df.loc[index_A, '季'] = quarter_change

    # 计算 A 前一周的同比增减
    if index_A_week is not None:
        prev_week = date_A_week - week_delta
        index_prev_week = get_index(prev_week)
        if index_prev_week is not None:
            prev_week_change = compute_change(df.at[index_A_week, '市值'], df.at[index_prev_week, '市值'])
            df.loc[index_A_week, '周'] = prev_week_change

    # 计算 A 前一月的同比增减
    if index_A_month is not None:
        prev_month = date_A_month - month_delta
        index_prev_month = get_index(prev_month)
        if index_prev_month is not None:
            prev_month_change = compute_change(df.at[index_A_month, '市值'], df.at[index_prev_month, '市值'])
            df.loc[index_A_month, '月'] = prev_month_change

    # 计算 A 前一季度的同比增减
    if index_A_quarter is not None:
        prev_quarter = date_A_quarter - quarter_delta
        index_prev_quarter = get_index(prev_quarter)
        if index_prev_quarter is not None:
            prev_quarter_change = compute_change(df.at[index_A_quarter, '市值'], df.at[index_prev_quarter, '市值'])
            df.loc[index_A_quarter, '季'] = prev_quarter_change

    summary_text = f"截至{date_A}，市值为{df.at[index_A, '市值'] / 100:.3f}万亿美元 \n"
    summary_text += f"周同比{week_change * 100:+.2f}%，上周同比{prev_week_change * 100:+.2f}% \n"
    summary_text += f"月同比{month_change * 100:+.2f}%，上月同比{prev_month_change * 100:+.2f}% \n"
    summary_text += f"季同比{quarter_change * 100:+.2f}%，上季同比{prev_quarter_change * 100:+.2f}% \n"

    # 近两周表现
    recent_data = df[df['日期'] <= date_A].tail(3)
    recent_text = f"{recent_data.iloc[0]['日期']}：{recent_data.iloc[0]['市值']:.2f}B\n"
    for i in range(1, len(recent_data)):
        change_value = (recent_data.iloc[i]['市值'] - recent_data.iloc[i - 1]['市值'])
        recent_text += f"{recent_data.iloc[i]['日期']}：{recent_data.iloc[i]['市值']:.2f}B；"
        recent_text += f"相对上周{change_value:+.2f}B；周同比{recent_data.iloc[i]['周'] * 100:+.2f}%\n"

    return df, summary_text, recent_text


# 需要修改下面的数据！！！！！！！！！！！！！！！！！！！！！！！！！
file_path = "../docs/稳定币市值记录_20250221.xlsx"
date_A = datetime(2025, 2, 20).date()  # 仅保留年月日


xls = pd.ExcelFile(file_path)
df_usdt = pd.read_excel(xls, sheet_name="USDT")
df_usdc = pd.read_excel(xls, sheet_name="USDC")

df_usdt, summary_usdt, recent_usdt = calculate_growth(df_usdt, date_A)
df_usdc, summary_usdc, recent_usdc = calculate_growth(df_usdc, date_A)

# 保存结果到同一个文件的不同 sheet
with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
    df_usdt.to_excel(writer, sheet_name="USDT", index=False)
    df_usdc.to_excel(writer, sheet_name="USDC", index=False)

print("计算完成，结果已保存到原文件。")
print("\nUSDT:")
print(summary_usdt)
print("\nUSDC:")
print(summary_usdc)

print("\nUSDT:")
print(recent_usdt)
print("\nUSDC:")
print(recent_usdc)
