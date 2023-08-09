
# -*- coding: utf-8 -*-
"""
    由于22年Q4数据披露不全，使用22年Q3数据进行补充
"""
import copy

import pandas as pd
import numpy as np
import argparse
from enum import Enum


if __name__ == '__main__':

    file1 = '分类结果2.xlsx'
    file2 = '23年Q1/固收增强分类结果_final.xlsx'

    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)[['FinProCode', '权益类', '资产明细是否有含权基金', 'final_enhance_type_asset']]

    df = df1.merge(df2, how='left', on='FinProCode')

    df.to_excel("分类结果_补充.xlsx")
