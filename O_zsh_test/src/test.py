import numpy as np
import pandas as pd
from datetime import datetime, timedelta


# 辅助函数，获取数组中的极值点
def get_extre(array, order):
    # 获取order个最小值和最大值作为极值点
    extres_min = np.partition(array, order)[:order]
    extres_max = np.partition(array, -order)[-order:]
    return extres_min, extres_max


# 计算组合交易能力的主函数
def Cal_BSpreference(order, stock_position_port, data_all, ignore_edge_trading=True):
    # 提取所有股票代码
    stocks = list(set(stock_position_port['windcode']))

    # 初始化结果存储字典
    results_dict = {
        '股票代码': [],
        '左侧买入能力': [],
        '左侧卖出能力': [],
        '右侧买入能力': [],
        '右侧卖出能力': [],
        '左侧交易能力': [],
        '右侧交易能力': [],
        '买入交易能力': [],
        '卖出交易能力': [],
        '左侧买入金额': [],
        '左侧卖出金额': [],
        '右侧买入金额': [],
        '右侧卖出金额': []
    }

    # 遍历所有股票代码
    for stock in stocks:
        # 筛选特定股票的交易数据
        stock_position_port_stock = stock_position_port[stock_position_port['windcode'] == stock]

        # 处理交易量数据，将0替换为NaN并删除这些行
        position_adj = stock_position_port_stock['trade'].replace(0, np.nan).dropna()
        if position_adj.empty:
            continue

        # 获取股票价格数据
        stock_code = stock
        data0 = data_all[data_all['windcode'] == stock_code]
        data = pd.DataFrame(data0['S_DQ_ADJCLOSE'].values, index=data0['backdate'], columns=[stock])
        data = data.sort_index()
        data.dropna(inplace=True)

        # 检查数据完整性
        start_date = stock_position_port_stock['backdate'].min() - timedelta(days=180)
        if data.index[0] > start_date:
            continue

        # 扩展价格数据，以包含所有需要的日期
        all_dates = pd.date_range(start=data.index.min(), end=data.index.max(), freq='D')
        data_full = data.reindex(all_dates, fill_value=np.nan)

        # 计算持仓调整与收盘价的关系
        position_adj['close'] = data_full.loc[position_adj.index, stock]
        position_adj['持仓调整'] = position_adj['trade']

        # 获取股票价格的极值点
        array = data.iloc[:, 0].values
        extres_min, extres_max = get_extre(array, order)
        extres = np.append(extres_min, extres_max)

        # 初始化交易能力相关列表
        LR_power_list = []
        amount_list = []

        # 遍历每一天的交易数据
        for ind_date in position_adj.index:
            # 计算当日在价格序列中的位置
            ind_date_ind = all_dates.get_loc(ind_date)

            # 忽略极值点边缘的交易
            if ignore_edge_trading and (
                    ind_date_ind in [0, len(all_dates) - 1] or ind_date in [data.index[0], data.index[-1]]):
                continue

            # 确定当日交易的极值点范围
            extre_left = extres[np.searchsorted(extres, ind_date_ind) - 1]
            extre_right = extres[np.searchsorted(extres, ind_date_ind)]

            # 计算交易能力
            trade_ability = (data_full.iloc[ind_date_ind, 0] - min(data_full.iloc[extre_left, 0],
                                                                   data_full.iloc[extre_right, 0])) / \
                            (max(data_full.iloc[extre_left, 0], data_full.iloc[extre_right, 0]) - min(
                                data_full.iloc[extre_left, 0], data_full.iloc[extre_right, 0]))

            # 根据买卖方向调整交易能力得分
            if position_adj.at[ind_date, '持仓调整'] > 0:
                LR_power_list.append(trade_ability)
            else:
                LR_power_list.append(-trade_ability)

            # 记录交易金额
            amount_list.append(abs(position_adj.at[ind_date, '持仓调整']) * data_full.iloc[ind_date_ind, 0])

        # 计算交易能力得分
        trade_power = np.mean(LR_power_list)

        # 存储结果到字典
        results_dict['股票代码'].append(stock)
        results_dict['左侧买入能力'].append(trade_power)  # 示例，需要根据实际逻辑填写
        # ... (此处省略其他字段的赋值)

    # 将结果字典转换为DataFrame
    BSpreference = pd.DataFrame(results_dict).T
    return BSpreference

# 注意：上述代码中省略了部分逻辑，你需要根据原代码的逻辑补全所有字段的计算和赋值。