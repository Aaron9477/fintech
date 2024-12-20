import pandas as pd

def get_avg_yield():
    target_file = 'test.xlsx'
    df = pd.read_excel(target_file)
    df = df[['FinProCode', 'actual_yield', 'product_establish_date']]

    # 将 product_establish_date 转换为日期类型
    df['product_establish_date'] = pd.to_datetime(df['product_establish_date'])

    # 提取年份和月份
    df['establish_year'] = df['product_establish_date'].dt.year
    df['establish_month'] = df['product_establish_date'].dt.month

    # 过滤掉 actual_yield 为空的数据
    df = df.dropna(subset=['actual_yield'])

    # 根据年份和月份分组
    grouped = df.groupby(['establish_year', 'establish_month'])

    # 计算实际收益的平均值
    avg_yield = grouped['actual_yield'].mean().reset_index()
    avg_yield.columns = ['establish_year', 'establish_month', 'average_yield']

    # 计算每个年月的产品数量
    product_count = grouped.size().reset_index(name='product_count')

    # 合并两个 DataFrame
    result_df = avg_yield.merge(product_count, on=['establish_year', 'establish_month'], how='outer')

    return result_df


def get_receipt_yield():
    target_file = '同业存单发行利率走势.xlsx'
    new_df = pd.read_excel(target_file)

    # 处理新数据
    new_df['明细数据'] = pd.to_datetime(new_df['明细数据'])
    new_df['coupon_year'] = new_df['明细数据'].dt.year
    new_df['coupon_month'] = new_df['明细数据'].dt.month

    # 从2022年开始计算每年每月的票面利率平均值
    grouped_coupon = new_df[new_df['coupon_year'] >= 2022].groupby(['coupon_year', 'coupon_month'])
    avg_coupon = grouped_coupon['票面利率'].mean().reset_index()
    avg_coupon.columns = ['coupon_year', 'coupon_month', 'average_coupon_rate']

    return avg_coupon


avg_yield = get_avg_yield()
receipt_yield = get_receipt_yield()
final_df = avg_yield.merge(receipt_yield, left_on=['establish_year', 'establish_month'], right_on=['coupon_year', 'coupon_month'], how='left')

del final_df['coupon_year'], final_df['coupon_month']

final_df.rename(columns={'establish_year': '年', 'establish_month': '月', 'average_yield': '理财平均兑付收益',
                         'product_count': '统计理财产品数量', 'average_coupon_rate': '票据平均年化收益率'}, inplace=True)

# 保存到 Excel 文件
output_file_path = 'result.xlsx'
final_df.to_excel(output_file_path, index=False)

print(f"Yearly and monthly average yield and product count have been saved to {output_file_path}")