'''
使用方法：稳普益要从平台拉取的，各理财子的半年报数据，筛选存续产品&理财子公司，作为本代码的输入
目前所有的金额都少乘10000，需要修改

图鉴更新也需要用这个
'''
import pandas as pd

# 假设你的Excel表格名为"input_data.xlsx"，并且Sheet名为"Sheet1"
input_path = "理财子半年报数据_from普益.xlsx"
df = pd.read_excel(input_path, sheet_name="Sheet1")

# 创建一个空的DataFrame，用于存放转换后的数据
output_data = pd.DataFrame(columns=['公司', '说明', '产品类型', '发行数量', '金额', '金额占比(%)', '排名'])

# 定义产品类型与说明的映射关系
product_mapping = {
    '公募': '按募集方式',
    '私募': '按募集方式',
    '固定收益类': '按投资性质',
    '混合类': '按投资性质',
    '权益类': '按投资性质',
    '商品及金融衍生品类': '按投资性质'
}

# 循环处理每个公司数据
for _, row in df.iterrows():
    company = row['公司']
    total_amount = row['合计金额'] if not pd.isna(row['合计金额']) else 0

    # 处理不同类型的产品数据
    for product_type in ['公募', '私募', '固定收益类', '混合类', '权益类', '商品及金融衍生品类']:
        quantity_col = product_type + '数量'
        amount_col = product_type + '金额'

        quantity = row[quantity_col] if not pd.isna(row[quantity_col]) else 0
        amount = row[amount_col] if not pd.isna(row[amount_col]) else 0

        # 计算金额占比
        percentage = (amount / total_amount) * 100 if total_amount > 0 else 0

        # 添加记录到输出表
        output_data = output_data.append({
            '公司': company,
            '说明': product_mapping[product_type],
            '产品类型': product_type,
            '发行数量': quantity,
            '金额': amount,
            '金额占比(%)': percentage,
            '排名': None  # 排名后续计算
        }, ignore_index=True)

    # 添加"合计"的行
    total_quantity = row['合计数量'] if not pd.isna(row['合计数量']) else 0
    output_data = output_data.append({
        '公司': company,
        '说明': '按募集方式',
        '产品类型': '合计',
        '发行数量': total_quantity,
        '金额': total_amount,
        '金额占比(%)': 100.0,
        '排名': None  # 排名后续计算
    }, ignore_index=True)

    output_data = output_data.append({
        '公司': company,
        '说明': '按投资性质',
        '产品类型': '合计',
        '发行数量': total_quantity,
        '金额': total_amount,
        '金额占比(%)': 100.0,
        '排名': None  # 排名后续计算
    }, ignore_index=True)

# 计算排名
output_data['排名'] = output_data.groupby(['说明', '产品类型'])['金额'].rank(ascending=False, method='min').astype(int)
output_data['金额'] = output_data['金额'] * 10000

# 保存为新的Excel文件
output_path = "底层数据-公告披露信息.xlsx"
output_data.to_excel(output_path, index=False)