'''

'''


import pandas as pd

input_path = "权益类理财产品筛选.xlsx"
df = pd.read_excel(input_path, sheet_name="权益类产品权益资产持仓情况")

df = df[df['资产大类'] == '权益类']

penetration_before = df[df['穿透类型'] == '穿透前'].groupby('公司名称').agg({
    '资产规模': 'sum',
    '资产占比': 'sum'
}).rename(columns={'资产规模': '穿透前资产规模', '资产占比': '穿透前资产占比'})

penetration_after = df[df['穿透类型'] == '穿透后'].groupby('公司名称').agg({
    '资产规模': 'sum',
    '资产占比': 'sum'
}).rename(columns={'资产规模': '穿透后资产规模', '资产占比': '穿透后资产占比'})

# 将穿透前和穿透后的数据合并
result = pd.merge(penetration_before, penetration_after, on='公司名称', how='outer').reset_index()

# 输出结果
print(result)

result.to_excel("权益类资产穿透前后的投资情况.xlsx")