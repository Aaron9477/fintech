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
wind_return = w.wsd("019014.SH", "maturitydate,bduration,sduration,modidura_cnbd,sprdura_cnbd,interestduration_cnbd,weight_modidura,weight_sprdura,weight_interestduration", "2022-09-30", "2022-09-30", "credibility=1")
print(wind_return)
wind_return = w.wsd("2201011S.IB", "maturitydate,bduration,sduration,modidura_cnbd,sprdura_cnbd,interestduration_cnbd,weight_modidura,weight_sprdura,weight_interestduration", "2022-09-30", "2022-09-30", "credibility=1")
print(wind_return)
wind_return = w.wsd("101003.SH", "maturitydate,bduration,sduration,modidura_cnbd,sprdura_cnbd,interestduration_cnbd,weight_modidura,weight_sprdura,weight_interestduration", "2022-09-30", "2022-09-30", "credibility=1")

wind_return = w.wsd(fund_str, "NAV_adj", statistics_date, statistics_date, "PriceAdj=F")

print(wind_return)