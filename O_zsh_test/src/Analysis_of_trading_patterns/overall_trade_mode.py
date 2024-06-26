import pandas as pd

def summarize_performance(results, begin_date, end_date):
    # 筛选特定的begin_date和end_date
    results_filtered = results[(results['begin_date'] == begin_date) & (results['end_date'] == end_date)]

    summary = results_filtered.groupby('ma_signal_type').agg({
        'buy_count': 'sum',
        'sell_count': 'sum',
        'buy_amount': 'sum',
        'sell_amount': 'sum'
    }).reset_index()

    # 加权平均
    for signal in ['signal_present_buy_count_ratio', 'signal_absent_buy_count_ratio',
                   'signal_present_sell_count_ratio', 'signal_absent_sell_count_ratio',
                   'signal_present_buy_amount_ratio', 'signal_absent_buy_amount_ratio',
                   'signal_present_sell_amount_ratio', 'signal_absent_sell_amount_ratio']:
        if 'buy' in signal:
            total_weight = results_filtered.groupby('ma_signal_type')['buy_count'].sum()
            summary[signal] = results_filtered.groupby('ma_signal_type').apply(
                lambda x: (x[signal] * x['buy_count']).sum() / total_weight[x.name] if total_weight[x.name] > 0 else 0
            ).values
        elif 'sell' in signal:
            total_weight = results_filtered.groupby('ma_signal_type')['sell_count'].sum()
            summary[signal] = results_filtered.groupby('ma_signal_type').apply(
                lambda x: (x[signal] * x['sell_count']).sum() / total_weight[x.name] if total_weight[x.name] > 0 else 0
            ).values
        elif 'buy_amount' in signal:
            total_weight = results_filtered.groupby('ma_signal_type')['buy_amount'].sum()
            summary[signal] = results_filtered.groupby('ma_signal_type').apply(
                lambda x: (x[signal] * x['buy_amount']).sum() / total_weight[x.name] if total_weight[x.name] > 0 else 0
            ).values
        elif 'sell_amount' in signal:
            total_weight = results_filtered.groupby('ma_signal_type')['sell_amount'].sum()
            summary[signal] = results_filtered.groupby('ma_signal_type').apply(
                lambda x: (x[signal] * x['sell_amount']).sum() / total_weight[x.name] if total_weight[x.name] > 0 else 0
            ).values

    # 添加begin_date和end_date字段
    summary['begin_date'] = begin_date
    summary['end_date'] = end_date

    summary.to_csv('investment_manager_signals_summaryV2.csv', index=False)
    print(summary)

if __name__ == '__main__':
    # 假设 'results' 是你之前计算出来的 DataFrame
    results = pd.read_csv('investment_manager_signalsV4.csv')  # 读取之前计算的结果文件

    begin_date, end_date = 20200218, 20240618
    summarize_performance(results, begin_date, end_date)