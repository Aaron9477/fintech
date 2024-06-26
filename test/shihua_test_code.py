import numpy as np

def cal_stock_ma(trade_date_list, nav_list, average_days):
    '''
    计算股票的均线
    Args:
        trade_date_list:交易日期列表
        nav_list:净值列表
        average_days:均线天数
    Returns:
        stock_ma:均线列表
    '''
    stock_ma = []
    for i in range(average_days - 1, len(trade_date_list)):
        stock_ma.append(np.mean(nav_list[i - average_days + 1:i + 1]))



if __name__ == '__main__':
    trade_date_utils = celery_global_value.get_trade_date_utils()
    ready_date = trade_date_utils.get_ready_trade_date()
    date_list = trade_date_utils.get_trade_date_list('20150101', ready_date)

    average_days_list = [5, 10, 20, 30]
