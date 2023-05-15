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
    df1 = pd.read_excel("../../理财子基金分析_2021-12-31.xlsx", sheet_name="理财子各基金类型占比")[["理财子公司", "基金类型", "基金资产规模"]]
    df1.rename(columns={'基金资产规模': '2021-12-31基金产品规模'}, inplace=True)

    df2 = pd.read_excel("../../理财子基金分析_2022-03-31.xlsx", sheet_name="理财子各基金类型占比")[["理财子公司", "基金类型", "基金资产规模"]]
    df2.rename(columns={'基金资产规模': '2022-03-31基金产品规模'}, inplace=True)

    df3 = pd.read_excel("../../理财子基金分析_2022-06-30.xlsx", sheet_name="理财子各基金类型占比")[["理财子公司", "基金类型", "基金资产规模"]]
    df3.rename(columns={'基金资产规模': '2022-06-30基金产品规模'}, inplace=True)

    df4 = pd.read_excel("../../理财子基金分析_2022-09-30.xlsx", sheet_name="理财子各基金类型占比")[["理财子公司", "基金类型", "基金资产规模"]]
    df4.rename(columns={'基金资产规模': '2022-09-30基金产品规模'}, inplace=True)

    df_res = df1.merge(df2, how="outer", on=["理财子公司", "基金类型"])
    df_res = df_res.merge(df3, how="outer", on=["理财子公司", "基金类型"])
    df_res = df_res.merge(df4, how="outer", on=["理财子公司", "基金类型"])

    df_res = df_res.fillna(0)

    df_res.to_excel("理财公司投资基金类型规模变化.xlsx")








