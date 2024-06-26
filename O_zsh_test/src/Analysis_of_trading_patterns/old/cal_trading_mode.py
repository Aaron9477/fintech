import pandas as pd

# 假设你已经有了两个数据表 A 和 B

import pandas as pd


def get_trade_mode(all_stock_ma_price, all_portfolio_stock_turn_volume, begin_date, end_date):
    # todo:begin_date是否有为空的情况？
    # todo:end_date是否有投资经理不在任，还为空的情况
    current_date = int(pd.to_datetime('today').date().strftime('%Y%m%d'))
    all_portfolio_stock_turn_volume['BEG_DATE'] = pd.to_datetime(all_portfolio_stock_turn_volume['BEG_DATE'].astype(str))\
        .dt.strftime('%Y%m%d').fillna(-1).astype(int)
    all_portfolio_stock_turn_volume['END_DATE'] = pd.to_datetime(all_portfolio_stock_turn_volume['END_DATE'].astype(str))\
        .dt.strftime('%Y%m%d').fillna(current_date).astype(int)

    # 交易日期在begin_date和end_date之间的交易
    all_portfolio_stock_turn_volume = all_portfolio_stock_turn_volume[(all_portfolio_stock_turn_volume['BCRQ'] >= begin_date) &
    (all_portfolio_stock_turn_volume['BCRQ'] <= end_date)]
    portfolio_id_input = list(set(all_portfolio_stock_turn_volume['PORTFOLIOID']))

    # 初始化一个空的DataFrame来存储结果
    results = pd.DataFrame()
    for portfolio_id in portfolio_id_input:
        portfolio_stock_turn_volume = all_portfolio_stock_turn_volume[all_portfolio_stock_turn_volume['PORTFOLIOID'] == portfolio_id]

        df_merged = pd.merge(portfolio_stock_turn_volume, all_stock_ma_price, left_on=['STOCK_CODE', 'BCRQ'],
                             right_on=['SYMBOL', 'TRADEDATE'], how='inner')
        df_merged.to_csv("test.csv")

        # 遍历四个均线信号
        for signal_col in ['signal_day_5', 'signal_day_10', 'signal_day_20', 'signal_day_30']:
            # 计算有信号和没信号的交易次数和交易规模
            signal_present = df_merged[df_merged[signal_col] == 1]
            signal_absent = df_merged[df_merged[signal_col] == 0]

            total_trades = df_merged['BS'].count()
            total_amount = df_merged['CJJE'].sum()

            signal_present_trades = signal_present['BS'].count()
            signal_absent_trades = signal_absent['BS'].count()

            signal_present_amount = signal_present['CJJE'].sum()
            signal_absent_amount = signal_absent['CJJE'].sum()

            # 步骤6：计算占比
            trade_ratio_present = signal_present_trades / total_trades
            trade_ratio_absent = signal_absent_trades / total_trades
            amount_ratio_present = signal_present_amount / total_amount
            amount_ratio_absent = signal_absent_amount / total_amount

            # 步骤7：结果汇总
            result = {
                'Portfolio_Id': portfolio_id,
                'Signal_Column': signal_col,
                'begin_date': begin_date,
                'end_date': end_date,
                'Trades_Signal_Present': signal_present_trades,
                'Trades_Signal_Absent': signal_absent_trades,
                'Trade_Ratio_Signal_Present': trade_ratio_present,
                'Trade_Ratio_Signal_Absent': trade_ratio_absent,
                'Amount_Signal_Present': signal_present_amount,
                'Amount_Signal_Absent': signal_absent_amount,
                'Amount_Ratio_Signal_Present': amount_ratio_present,
                'Amount_Ratio_Signal_Absent': amount_ratio_absent
            }
            results = results.append(result, ignore_index=True)

    # 步骤8：输出结果
    results.to_csv('investment_manager_signalsV2.csv', index=False)


if __name__ == '__main__':
    all_stock_ma_price = pd.read_csv('../财汇股票行情数据_240603_移动平均线_部分测试数据.csv')  # 如果A表是CSV文件
    all_portfolio_stock_turn_volume = pd.read_csv('../石化投资组合股票交易数据_240603_部分测试数据_更少的数据.csv')  # 如果B表是CSV文件

    all_portfolio_stock_turn_volume.drop_duplicates(subset=['PORTFOLIOID', 'STOCK_CODE', 'BCRQ', 'BS', 'CJSL', 'CJJE'],
                                                    inplace=True)

    begin_date, end_date = 20200218, 20240618
    get_trade_mode(all_stock_ma_price, all_portfolio_stock_turn_volume, begin_date, end_date)
