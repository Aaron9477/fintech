'''
代码待修改
'''


import pandas as pd

input_path = "权益类理财产品筛选.xlsx"
df = pd.read_excel(input_path, sheet_name="权益类产品权益资产持仓情况")

# 过滤穿透后的数据
df_after_penetration = df[df['穿透类型'] == '穿透后']

# 分别处理“权益类”和“资管产品”
equity_df = df_after_penetration[df_after_penetration['资产大类'] == '权益类']
asset_management_df = df_after_penetration[df_after_penetration['资产大类'] == '资管产品']

# 汇总权益类数据
equity_summary = equity_df.groupby('公司名称').agg({
    '资产规模': 'sum',
    '资产占比': 'sum'
}).rename(columns={'资产规模': '穿透后权益类资产规模', '资产占比': '穿透后权益类资产占比'})

# 汇总资管产品数据
asset_management_summary = asset_management_df.groupby('公司名称').agg({
    '资产规模': 'sum',
    '资产占比': 'sum'
}).rename(columns={'资产规模': '穿透后公募基金规模', '资产占比': '穿透后公募基金占比'})

print(asset_management_summary)

# 将权益类和资管产品的数据合并
result = pd.merge(equity_summary, asset_management_summary, on='公司名称', how='outer').fillna(0)
result = result.reset_index()
# 输出结果
print(result)

result.to_excel("统计穿透后权益类资产和公募基金投资情况分析.xlsx")