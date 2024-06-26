import ccxt
from Function import *

print(ccxt.__version__)  # 检查ccxt版本，需要最新版本，1.44.21以上

# ===参数设定
coins = ['ada', 'bch', 'bnb', 'btc', 'dot', 'eth', 'link', 'ltc', 'xrp']
future_date = '240329'  # 要套利的合约到期时间
r_threshold = 0.1  # 高于利差就开始入金，0.05代表5%

# ===创建交易所
exchange = ccxt.binance()
exchange.apiKey = ''
exchange.secret = ''
exchange.proxies = {
        'http': '127.0.0.1:7890',
        'https': '127.0.0.1:7890',
    }
# 加载币本位合约数据。币种的合约面值，价格精度信息
symbol_list, contact_size, price_precision = load_market(exchange)
for coin in coins:
    coin = coin.upper()
    spot_symbol_name = {'type1': coin + 'USDT', 'type2': coin + '/USDT'}
    future_symbol_name = {'type1': coin + 'USD_' + future_date}
    # ===计算价差
    # 获取现货卖一数据。因为现货是买入，取卖一。
    # noinspection PyUnresolvedReferences
    spot_sell1_price = exchange.publicGetTickerBookTicker(params={'symbol': spot_symbol_name['type1']})['askPrice']
    # 获取期货买一数据。因为期货是卖出，取买一。
    # noinspection PyUnresolvedReferences
    future_buy1_price = exchange.dapiPublicGetTickerBookTicker(params={'symbol': future_symbol_name['type1']})[0][
        'bidPrice']

    # 计算价差
    r = float(future_buy1_price) / float(spot_sell1_price) - 1
    print(
        'coin: %s, 现货价格：%.4f，期货价格：%.4f，价差：%.4f%%' % (coin, float(spot_sell1_price), float(future_buy1_price), r * 100))
    # ===判断价差是否满足要求
    if r < r_threshold:
        print('利差小于目标阀值，不入金')
    else:
        print('========== 利差大于目标阀值: %.4f vs %.4f  ==========' % (r, r_threshold))

    # ===循环结束
    print('*' * 20, '本次循环结束，暂停', '*' * 20, '\n')
    time.sleep(2)