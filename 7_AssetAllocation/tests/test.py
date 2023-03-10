#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
@author: hao li
"""
import datetime as dt
import os
import time
import warnings

import matplotlib.pyplot as plt
from WindPy import *
import pandas as pd

# In[2]:


# 参数设置
warnings.filterwarnings("ignore")

# # %matplotlib ipympl
# plt.rcParams["font.sans-serif"] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False
#
# # os.getcwd()  # 获取当前工作目录
# root = os.path.abspath(".")[:1]
# os.chdir("{}:/工作同步目录/2 公募基金评价/B 公募基金分析框架/Python代码/量化资产择时".format(root))  # 改变当前工作目录
w.start()
start_day = "20050101"  # 2005年1月开始有PMI指标
end_day = "20221130"

macro_data_raw = w.edb(
    "M0000545,M0017126,S5808575,S0031550,M0000612,M0001227,S5111903,M0001385,S0059749,S0059741,M0000271",
    start_day,
    end_day,
    usedf=True,
)[1]
macro_data_raw.rename(
    columns={
        "M0000545": "工业增加值当月同比",
        "M0017126": "PMI",
        "S5808575": "LME三个月期铜价格",
        "S0031550": "波罗的海干散货指数",
        "M0000612": "CPI当月同比",
        "M0001227": "PPI当月同比",
        "S5111903": "WTI原油现货价",
        "M0001385": "M2同比",
        "S0059749": "国债到期收益率10年期",
        "S0059741": "国债到期收益率3个月",
        "M0000271": "美元指数",
    },
    inplace=True,
)
macro_data_raw.index = pd.to_datetime(macro_data_raw.index)
macro_data_raw.to_csv("MacroData.csv")