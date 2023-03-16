# -*- coding: utf-8 -*-
"""
    连接一年的基金规模数据
"""
import pandas as pd
import numpy as np
import argparse
import datetime
import copy


if __name__ == '__main__':
    # df1 = pd.read_excel("../../基金信息_2022-09-30.xlsx")
    df1 = pd.read_excel("基金信息_2022-12-31.xlsx")
    df2 = pd.read_csv("中信建投公募基金自有分类20230306.csv", encoding='gb18030')
    df_res = df1.merge(df2, how="left", left_on="SecuCode", right_on="fund_code", )

    # df_res = df_res.fillna(0)

    df_res.to_excel("基金信息_2.xlsx")











