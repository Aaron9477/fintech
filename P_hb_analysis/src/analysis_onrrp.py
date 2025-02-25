import pandas as pd

# 读取Excel文件
file_path = "../docs/宏观数据.xlsx"
sheet_name = "ON RRP和TGA"

# 读取数据
df = pd.read_excel(file_path, sheet_name=sheet_name)

# 确保列名匹配你的数据
df.columns = ["日期", "ON RRP规模", "TGA规模"]

# 确保日期列是 datetime 类型，并按时间排序
df["日期"] = pd.to_datetime(df["日期"])
df = df.sort_values("日期").reset_index(drop=True)

# 计算 ON RRP 和 TGA 之和
df["ON RRP和TGA之和"] = df["ON RRP规模"] + df["TGA规模"]


# 定义计算环比和变化量的函数
def calc_ratios(df, latest_date, column_name, period_days):
    """计算指定列的环比及增减量"""
    ref_date = latest_date - pd.Timedelta(days=period_days)
    prev_df = df[df["日期"] <= ref_date]

    if not prev_df.empty:
        prev_date = prev_df.iloc[-1]["日期"]
        prev_value = prev_df.iloc[-1][column_name]
        latest_value = df.iloc[-1][column_name]
        change = latest_value - prev_value
        ratio = (change / prev_value) * 100 if prev_value != 0 else None
        return prev_date, prev_value, latest_value, change, ratio
    return None, None, None, None, None


# 获取最新日期
latest_date = df.iloc[-1]["日期"]

# 计算日环比、周环比、双周环比
results = {}
for col in ["ON RRP规模", "TGA规模", "ON RRP和TGA之和"]:
    results[col] = {
        "日环比": calc_ratios(df, latest_date, col, 1),
        "周环比": calc_ratios(df, latest_date, col, 7),
        "双周环比": calc_ratios(df, latest_date, col, 14),
    }

# 格式化输出
output = f"{latest_date.strftime('%Y-%m-%d')} 数据：\n"

for col, label in zip(["ON RRP和TGA之和", "TGA规模", "ON RRP规模"], ["ON RRP和TGA之和", "TGA", "ON RRP"]):
    output += f"\n【{label}】\n"
    for period, (prev_date, prev_value, latest_value, change, ratio) in results[col].items():
        if prev_date is not None:
            output += (f"{period}: {ratio:+.2f}%；变化量 {change:+,.2f}；"
                       f"（{prev_date.strftime('%Y-%m-%d')} 规模：{prev_value:.2f}）\n")

print(output)
