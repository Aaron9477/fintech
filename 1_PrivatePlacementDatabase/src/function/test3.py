# -*- coding: utf-8 -*-

from collections import OrderedDict
import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
import timestamp

#显示所有的列
pd.set_option('display.max_columns', None)

#显示所有的行
pd.set_option('display.max_rows', None)

#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)




if __name__ == '__main__':
    asset_order = OrderedDict()
    asset_order['固定收益类'] = ['a', 'b']
    asset_order['收益类'] = ['a', 'b']
    print(asset_order.index('固定收益类'))


