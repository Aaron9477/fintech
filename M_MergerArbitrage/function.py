import pandas as pd
import time
import math

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option("display.max_rows", 500)


# 在币币账户下单
def binance_spot_place_order(exchange, symbol, long_or_short, price, amount):
    """
    :param exchange:  ccxt交易所
    :param symbol: 币币交易对代码，例如'BTC/USDT'
    :param long_or_short:  两种类型：买入、卖出
    :param price:  下单价格
    :param amount:  下单数量
    :return:
    """

    for i in range(5):
        try:
            # 买
            if long_or_short == '买入':
                order_info = exchange.create_limit_buy_order(symbol, amount, price)  # 买单
            # 卖
            elif long_or_short == '卖出':
                order_info = exchange.create_limit_sell_order(symbol, amount, price)  # 卖单
            else:
                raise ValueError('long_or_short只能是：`买入`或者`卖出`')

            print('binance币币交易下单成功：', symbol, long_or_short, price, amount)
            print('下单信息：', order_info, '\n')
            return order_info

        except Exception as e:
            print('binance币币交易下单报错，1s后重试', e)
            time.sleep(1)

    print('binance币币交易下单报错次数过多，程序终止')
    exit()


# 在期货合约账户下限价单
def binance_future_place_order(exchange, symbol, long_or_short, price, amount):
    """
    :param exchange:  ccxt交易所
    :param symbol: 合约代码，例如'BTCUSD_210625'
    :param long_or_short:  四种类型：开多、开空、平多、平空
    :param price: 开仓价格
    :param amount: 开仓数量，这里的amount是合约张数
    :return:

    timeInForce参数的几种类型
    GTC - Good Till Cancel 成交为止
    IOC - Immediate or Cancel 无法立即成交(吃单)的部分就撤销
    FOK - Fill or Kill 无法全部立即成交就撤销
    GTX - Good Till Crossing 无法成为挂单方就撤销

    """

    if long_or_short == '开空':
        side = 'SELL'
    elif long_or_short == '平空':
        side = 'BUY'
    else:
        raise NotImplemented('long_or_short目前只支持 `开空`、`平空`，请参考官方文档添加其他的情况')

    # 确定下单参数
    # 开空
    params = {
        'side': side,
        'positionSide': 'SHORT',
        'symbol': symbol,
        'type': 'LIMIT',
        'price': price,  # 下单价格
        'quantity': amount,  # 下单数量，注意此处是合约张数,
        'timeInForce': 'GTC',  # 含义见本函数注释部分
    }
    # 尝试下单
    for i in range(5):
        try:
            params['timestamp'] = int(time.time() * 1000)
            order_info = exchange.dapiPrivatePostOrder(params)
            print('币安合约交易下单成功：', symbol, long_or_short, price, amount)
            print('下单信息：', order_info, '\n')
            return order_info
        except Exception as e:
            print('币安合约交易下单报错，1s后重试...', e)
            time.sleep(1)

    print('币安合约交易下单报错次数过多，程序终止')
    exit()


# binance各个账户间转钱
def binance_account_transfer(exchange, currency, amount, from_account='币币', to_account='合约'):
    """
    """

    if from_account == '币币' and to_account == '合约':
        transfer_type = 'MAIN_CMFUTURE'
    elif from_account == '合约' and to_account == '币币':
        transfer_type = 'CMFUTURE_MAIN'
    else:
        raise ValueError('未能识别`from_account`和`to_account`的组合，请参考官方文档')

    # 构建参数
    params = {
        'type': transfer_type,
        'asset': currency,
        'amount': amount,
    }

    # 开始转账
    for i in range(5):
        try:
            params['timestamp'] = int(time.time() * 1000)
            transfer_info = exchange.sapiPostAssetTransfer(params=params)
            print('转账成功：', from_account, 'to', to_account, amount)
            print('转账信息：', transfer_info, '\n')
            return transfer_info
        except Exception as e:
            print('转账报错，1s后重试', e)
            time.sleep(1)

    print('转账报错次数过多，程序终止')
    exit()


def load_market(exchange):
    """
    加载市场数据

    :param exchange:    交易所对象，用于获取数据
    :return:

        price_precision 币种价格精     例： 2 代表 0.01
            {'BTCUSD_PERP': 1, 'BTCUSD_231229': 1, 'BTCUSD_240329': 1, 'BTCUSD_240628': 1, ...}
        contact_size    合约面值       例： 100.0 代表 一张合约价值100U
            {'BTC': 100, 'EOS': 10, 'DOT': 10, 'ETH': 10}
    """
    # ===获取交易对的信息
    exchange_info = exchange.dapiPublicGetExchangeinfo()

    # ===挑选出所有符合条件的交易对
    symbol_list = [x['symbol'] for x in exchange_info['symbols']]  # 获取所有的交易对名称

    # ===获取各个交易对的精度、下单量等信息
    contact_size = {}  # 币种合约面值，例如bnb，买一张合约价值多少U
    price_precision = {}  # 币种价格精，例如bnb，价格是158.887，不能是158.8869
    # 遍历获得想要的数据
    for info in exchange_info['symbols']:
        symbol = info['symbol']
        contact_size[symbol] = int(info['contractSize'])
        for _filter in info['filters']:
            if _filter['filterType'] == 'PRICE_FILTER':
                price_precision[symbol] = int(math.log(float(_filter['tickSize']), 0.1))

    return symbol_list, contact_size, price_precision
