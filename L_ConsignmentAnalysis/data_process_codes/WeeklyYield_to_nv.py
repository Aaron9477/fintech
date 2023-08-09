# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月20日16:16:25
# @Author    : Noah Zhan
# @File      : WeeklyYield_to_nv
# @Project   : 银行理财代销图鉴
# @Function  ：将七日年化序列数据转化为净值数据
# --------------------------------
import numpy as np
import pandas as pd

def WeeklyYield_to_nv(x):
    #将周度七日年化序列数据转化为净值
    nv = ~x.isna()
    x = (x * 7 / 365 * 0.01 + 1).fillna(1).cumprod() * nv
    return x