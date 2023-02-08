# -*- coding: utf-8 -*-
"""
    基金分析第一步：拉取前十大资产中基金类型
"""

from WindPy import w
import pandas as pd
import numpy as np
import argparse
import datetime

w.start()
wind_return = w.wsd("000015.OF,000037.OF,000217.OF,000218.OF", "prt_stocktonav", "2022-09-30", "2022-09-30", "")

print(wind_return)