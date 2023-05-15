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
import mitosheet as mito
import numpy as np
import pandas as pd
import pandas_bokeh
import plotly_express as px
import quantstats as qs
import scipy.signal as signal
import scipy.stats as stats
import seaborn as sns
import statsmodels as st
import statsmodels.api as sm
from cvxopt import matrix, solvers
from scipy.stats.mstats import gmean
from WindPy import *


# In[2]:


# 参数设置
warnings.filterwarnings("ignore")

# %matplotlib ipympl
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
pandas_bokeh.output_notebook()  # notebook 展示

# os.getcwd()  # 获取当前工作目录
root = os.path.abspath(".")[:1]
os.chdir("{}:/工作同步目录/2 公募基金评价/B 公募基金分析框架/Python代码/量化资产择时".format(root))  # 改变当前工作目录
w.start()
start_day = "20050101"  # 2005年1月开始有PMI指标
end_day = "20221130"


# # 1. 宏观指标、资产选择以及趋势判断方法

# ## 1.1 宏观指标数据处理

# In[3]:


#

# Wind API读取宏观指标
"""
增长与景气：
M0000545-工业增加值当月同比-月-滞后1月
M0017126-PMI-月-不滞后
S5808575-LME三个月期铜价格-日-不滞后
S0031550-波罗的海干散货指数-日-不滞后
通胀：
M0000612-CPI当月同比-月-滞后1月
M0001227-PPI当月同比-月-滞后1月
S5111903-WTI原油现货价-日-不滞后
货币：
M0001385-M2同比-月-滞后1月
利率：
S0059749-国债到期收益率10年期-日-不滞后
构造-国债利差10年期与3个月-日-不滞后
外汇：
M0000271-美元指数-日-不滞后
"""
# macro_data_raw = w.edb(
#     "M0000545,M0017126,S5808575,S0031550,M0000612,M0001227,S5111903,M0001385,S0059749,S0059741,M0000271",
#     start_day,
#     end_day,
#     usedf=True,
# )[1]
# macro_data_raw.rename(
#     columns={
#         "M0000545": "工业增加值当月同比",
#         "M0017126": "PMI",
#         "S5808575": "LME三个月期铜价格",
#         "S0031550": "波罗的海干散货指数",
#         "M0000612": "CPI当月同比",
#         "M0001227": "PPI当月同比",
#         "S5111903": "WTI原油现货价",
#         "M0001385": "M2同比",
#         "S0059749": "国债到期收益率10年期",
#         "S0059741": "国债到期收益率3个月",
#         "M0000271": "美元指数",
#     },
#     inplace=True,
# )
# macro_data_raw.index = pd.to_datetime(macro_data_raw.index)
# macro_data_raw.to_csv("MacroData.csv")

# 宏观指标的处理
macro_data0 = pd.read_csv("MacroData.csv", index_col=0)
macro_data0.index = pd.to_datetime(macro_data0.index)

macro_data0["国债利差10年期与3个月"] = macro_data0["国债到期收益率10年期"] - macro_data0["国债到期收益率3个月"]
macro_data0 = macro_data0.resample("m").last()  # 读取每个月最后一个取值

# 对滞后指标进行滞后操作，向后平移一个月
macro_data0[["工业增加值当月同比_滞后", "CPI当月同比_滞后", "PPI当月同比_滞后", "M2同比_滞后"]] = macro_data0[
    ["工业增加值当月同比", "CPI当月同比", "PPI当月同比", "M2同比"]
].shift(1)
# mito.sheet(macro_data0, analysis_to_replay="id-ldngvpyvnp")
# 仅保留滞后宏观指标
macro_data = macro_data0.drop(
    ["工业增加值当月同比", "CPI当月同比", "PPI当月同比", "M2同比", "国债到期收益率3个月"], axis=1
)


# In[4]:


macro_data_rebase = qs.utils.rebase(macro_data, 100)
fig = px.line(
    macro_data_rebase,
    x=macro_data_rebase.index,
    y=macro_data_rebase.columns,
    width=1000,
    height=500,
)
# Add range slider
fig.update_xaxes(rangeslider_visible=True)


# ## 1.2 大类资产收益率数据处理

# In[5]:


# Wind API读取大类资产指标
# index_data_raw=w.wsd("000300.SH,000905.SH,H11006.CSI,H11008.CSI,AU9999.SGE,NH0300.NHF,NH0400.NHF,"
#                      "NH0500.NHF,H11025.CSI","close", start_day, end_day, usedf=True)[1]

# index_data_raw.rename(columns={'000300.SH': '沪深300', '000905.SH': '中证500', 'H11006.CSI': '中证国债',
#                            'H11008.CSI': '中证企业债', 'AU9999.SGE': '黄金', 'NH0300.NHF': '农产品',
#                            'NH0400.NHF': '基本金属', 'NH0500.NHF': '能源化工', 'H11025.CSI': '货币'}, inplace=True)

# index_data_raw.index = pd.to_datetime(index_data_raw.index)
# index_data_raw.to_csv('IndexData.csv')

# 资产指数的处理
index_data = pd.read_csv("IndexData.csv", index_col=0, infer_datetime_format=True)
index_data.index = pd.to_datetime(index_data.index)
index_data = index_data.resample("m").last()  # 读取每个月最后一个取值


# 2.3 合并数据
index_return_data = qs.utils.to_returns(index_data)  # 转成相对收益数据
total_data = pd.merge(index_return_data, macro_data, left_index=True, right_index=True, how="inner")


# In[6]:


index_data_rebase = qs.utils.rebase(index_data, 100)
px.line(
    index_data_rebase,
    x=index_data_rebase.index,
    y=index_data_rebase.columns,
    width=1000,
    height=500,
)
# mito.sheet(index_data_rebase, analysis_to_replay="id-moeicosxri")


# ##  1.3 判断宏观指标趋势

# In[7]:


#
# 我们通过观察最新值来判断当前的趋势。具体来看，如果T期的指标值大于T-1期的指标值，则我们认为指标是处于上行趋势，反之则认为指标是处于下行趋势。

data = macro_data.copy()
for factor in macro_data.columns:
    data[factor + "3M移动平均"] = data[factor].rolling(3).mean()
    data[factor + "9M移动平均"] = data[factor].rolling(9).mean()
    data[factor + "12M移动平均"] = data[factor].rolling(12).mean()
    data[factor + "HP滤波"] = sm.tsa.filters.hpfilter(data[factor].dropna(axis=0), 100)[
        1
    ]  # HP滤波平滑参数选160,参数λ越大,趋势项越平滑。根据Ravn and Uhlig(2002)的建议，对于年度数据lambda参数取值6.25(1600/4^4)，对于季度数据取值1600，对于月度数据取值129600(1600*3^4)。
    # plt.rcParams["figure.figsize"] = (8, 5)
    data[
        [
            factor,
            factor + "3M移动平均",
            factor + "9M移动平均",
            factor + "12M移动平均",
            factor + "HP滤波",
        ]
    ].plot_bokeh.line(
        panning=False,
        # rangetool=True,
        zooming=False,
        title=factor + "历史走势",
        figsize=(800, 450),
    )

# 经过移动平均或者hp滤波处理后，经济指标将会剔除很多噪音，变得平滑。从移动平均和hp滤波对比来看，hp滤波效果会更及时，趋势更平滑，而移动平均会有滞后现象。


# # 2. 宏观指标趋势对于大类资产收益率的影响

# ## 2.1 宏观指标趋势对于大类资产收益率的影响【历史均线法】

# In[15]:


# 例如：9月份的滞后指标，在10月份发布，指导11月份的资产配置；9月份的当期指标，在9月底已知，指导10月份的资产配置
# 绘制三个曲线，原始资产收益曲线，策略曲线（position1真实），策略曲线（position2理想）
for factor in macro_data.columns:
    for index in index_return_data.columns:
        n = 3  # 移动平均的月数n
        data1 = total_data[[factor, index]]  # 提取出宏观因子与指数数据
        data1.dropna(axis=0, inplace=True)
        # 生成移动平均宏观指标
        data1[factor + str(n) + "M移动平均"] = data1[factor].rolling(n).mean()
        # mito.sheet(data1)
        # flag字段用于记录月末宏观指标变动方向，position1模拟真实情况，下月初调仓，position2模拟理想情况，假设能预测到当月指标变化，并于当月初调仓
        data1["flag"] = data1["position1"] = data1["position2"] = 0
        # 第一个月数据因为滞后1月缺失，2-4月数据开始计算MA，5月底开始比较宏观趋势，由于是下月调仓，因此业绩从6月开始统计，理想情形业绩可以从5月开始统计，但为了可比，也从6月开始展示业绩
        for i in range(data1.shape[0] - 1):
            if (
                data1[factor + str(n) + "M移动平均"][i]
                > data1[factor + str(n) + "M移动平均"].shift(1)[i]
            ):
                data1["flag"][i] = 1  # 宏观指标上涨flag=1
                data1["position1"][i + 1] = 1
                data1["position2"][i] = 1

            elif (
                data1[factor + str(n) + "M移动平均"][i]
                < data1[factor + str(n) + "M移动平均"].shift(1)[i]
            ):
                data1["flag"][i] = -1  # 宏观指标下跌flag=-1
                data1["position1"][i + 1] = -1
                data1["position2"][i] = -1
            else:
                data1["flag"][i] = 0  # 宏观指标与上期一致flag=0
                data1["position1"][i + 1] = data1["position1"][i]  # 等于上期头寸
                data1["position2"][i] = data1["position1"][i - 1]  # 等于上期头寸

        # 真实情景收益
        up_return_series_real = data1[data1["position1"] == 1][index]
        up_df_real = pd.DataFrame()
        up_df_real["return"] = up_return_series_real.sort_values(ascending=False)
        up_df_real["position"] = 1

        down_return_series_real = data1[data1["position1"] == -1][index]
        down_df_real = pd.DataFrame()
        down_df_real["return"] = down_return_series_real.sort_values(ascending=False)
        down_df_real["position"] = -1

        up_meanreturn_real = up_return_series_real.mean()
        down_meanreturn_real = down_return_series_real.mean()

        n1_real = len(up_return_series_real)
        n2_real = len(down_return_series_real)

        t_result_real = stats.ttest_ind(
            a=up_return_series_real, b=down_return_series_real, equal_var=True
        )
        t_value_real = t_result_real[0]
        p_value_real = t_result_real[1]

        # 理想情景收益
        up_return_series_theory = data1[data1["position2"] == 1][index]
        up_df_theory = pd.DataFrame()
        up_df_theory["return"] = up_return_series_theory.sort_values(ascending=False)
        up_df_theory["position"] = 1

        down_return_series_theory = data1[data1["position2"] == -1][index]
        down_df_theory = pd.DataFrame()
        down_df_theory["return"] = down_return_series_theory.sort_values(
            ascending=False
        )
        down_df_theory["position"] = -1

        up_meanreturn_theory = up_return_series_theory.mean()
        down_meanreturn_theory = down_return_series_theory.mean()

        n1_theory = len(up_return_series_theory)
        n2_theory = len(down_return_series_theory)

        t_result_theory = stats.ttest_ind(
            a=up_return_series_theory, b=down_return_series_theory, equal_var=True
        )
        t_value_theory = t_result_theory[0]
        p_value_theory = t_result_theory[1]
        
        # 文字表述
        print('%s对%s的影响 \n->真实情景下: 指标上行月度:%d 指标下行月度: %d 上行平均涨跌幅:%f 下行平均涨跌幅:%f 差异:%f t值:%f p值:%f               \n->理想情景下: 指标上行月度:%d 指标下行月度: %d 上行平均涨跌幅:%f 下行平均涨跌幅:%f 差异:%f t值:%f p值:%f'
              % (factor, index, n1_real, n2_real, up_meanreturn_real, down_meanreturn_real,up_meanreturn_real-down_meanreturn_real,t_value_real, p_value_real,
                 n1_theory, n2_theory,up_meanreturn_theory, down_meanreturn_theory,up_meanreturn_theory-down_meanreturn_theory ,t_value_theory, p_value_theory))

        # 作图
        fig = plt.figure(figsize=(16,3))  # 设置图片大小
        # 各个子图的设置
        ax1 = fig.add_subplot(1,4, 1)  
        ax1.set_title("%s上行对%s的影响-真实" % (factor, index),fontsize=10)
        ax1.tick_params(labelsize=8)
        plt.fill_between(x=range(n1_real), y1=up_df_real["return"])
        ax2 = fig.add_subplot(1,4, 2)      
        ax2.set_title("%s下行对%s的影响-真实" % (factor, index),fontsize=10)
        ax2.tick_params(labelsize=8)
        plt.fill_between(x=range(n2_real), y1=down_df_real["return"])
        ax3 = fig.add_subplot(1,4, 3)  
        ax3.set_title("%s上行对%s的影响-理想" % (factor, index),fontsize=10)
        ax3.tick_params(labelsize=8)
        plt.fill_between(x=range(n1_theory), y1=up_df_theory["return"], color="green")  
        ax4 = fig.add_subplot(1,4, 4)  
        ax4.set_title("%s下行对%s的影响-理想" % (factor, index),fontsize=10)
        ax4.tick_params(labelsize=8)
        plt.fill_between(x=range(n2_theory), y1=down_df_theory["return"], color="green")
        plt.show()


# In[16]:


px.scatter(macro_data, x="LME三个月期铜价格", y="波罗的海干散货指数", trendline="ols")
px.scatter(macro_data, x="CPI当月同比_滞后", y="PPI当月同比_滞后", trendline="ols")


# ## 2.2 宏观指标趋势对于大类资产收益率的影响【HP滤波法】

# In[17]:


# 例如：9月份的滞后指标，在10月份发布，指导11月份的资产配置；9月份的当期指标，在9月底已知，指导10月份的资产配置
# 绘制三个曲线，原始资产收益曲线，策略曲线（position1真实），策略曲线（position2理想）
for factor in macro_data.columns:
    for index in index_return_data.columns:
        
        # factor='PMI'
        # index='沪深300'
        
        data1 = total_data[[factor, index]]  # 提取出宏观因子与指数数据
        data1.dropna(axis=0, inplace=True)
        # 生成移动平均宏观指标
        data1[factor + "_HP滤波"] = sm.tsa.filters.hpfilter(data1[factor].dropna(axis=0), 100)[1]    
        # mito.sheet(data1)
        # flag字段用于记录月末宏观指标变动方向，position1模拟真实情况，下月初调仓，position2模拟理想情况，假设能预测到当月指标变化，并于当月初调仓
        data1["flag"] = data1["position1"] = data1["position2"] = 0
        # 第一个月数据因为滞后1月缺失，2-4月数据开始计算MA，5月底开始比较宏观趋势，由于是下月调仓，因此业绩从6月开始统计，理想情形业绩可以从5月开始统计，但为了可比，也从6月开始展示业绩
        for i in range(data1.shape[0] - 1):
            if (
                data1[factor + "_HP滤波"][i]
                > data1[factor + "_HP滤波"].shift(1)[i]
            ):
                data1["flag"][i] = 1  # 宏观指标上涨flag=1
                data1["position1"][i + 1] = 1
                data1["position2"][i] = 1

            elif (
                data1[factor + "_HP滤波"][i]
                < data1[factor + "_HP滤波"].shift(1)[i]
            ):
                data1["flag"][i] = -1  # 宏观指标下跌flag=-1
                data1["position1"][i + 1] = -1
                data1["position2"][i] = -1
            else:
                data1["flag"][i] = 0  # 宏观指标与上期一致flag=0
                data1["position1"][i + 1] = data1["position1"][i]  # 等于上期头寸
                data1["position2"][i] = data1["position1"][i - 1]  # 等于上期头寸

        # 真实情景收益
        up_return_series_real = data1[data1["position1"] == 1][index]
        up_df_real = pd.DataFrame()
        up_df_real["return"] = up_return_series_real.sort_values(ascending=False)
        up_df_real["position"] = 1

        down_return_series_real = data1[data1["position1"] == -1][index]
        down_df_real = pd.DataFrame()
        down_df_real["return"] = down_return_series_real.sort_values(ascending=False)
        down_df_real["position"] = -1

        up_meanreturn_real = up_return_series_real.mean()
        down_meanreturn_real = down_return_series_real.mean()

        n1_real = len(up_return_series_real)
        n2_real = len(down_return_series_real)

        t_result_real = stats.ttest_ind(
            a=up_return_series_real, b=down_return_series_real, equal_var=True
        )
        t_value_real = t_result_real[0]
        p_value_real = t_result_real[1]

        # 理想情景收益
        up_return_series_theory = data1[data1["position2"] == 1][index]
        up_df_theory = pd.DataFrame()
        up_df_theory["return"] = up_return_series_theory.sort_values(ascending=False)
        up_df_theory["position"] = 1

        down_return_series_theory = data1[data1["position2"] == -1][index]
        down_df_theory = pd.DataFrame()
        down_df_theory["return"] = down_return_series_theory.sort_values(
            ascending=False
        )
        down_df_theory["position"] = -1

        up_meanreturn_theory = up_return_series_theory.mean()
        down_meanreturn_theory = down_return_series_theory.mean()

        n1_theory = len(up_return_series_theory)
        n2_theory = len(down_return_series_theory)

        t_result_theory = stats.ttest_ind(
            a=up_return_series_theory, b=down_return_series_theory, equal_var=True
        )
        t_value_theory = t_result_theory[0]
        p_value_theory = t_result_theory[1]
        
        # 文字表述
        print('%s对%s的影响 \n->真实情景下: 指标上行月度:%d 指标下行月度: %d 上行平均涨跌幅:%f 下行平均涨跌幅:%f 差异:%f t值:%f p值:%f               \n->理想情景下: 指标上行月度:%d 指标下行月度: %d 上行平均涨跌幅:%f 下行平均涨跌幅:%f 差异:%f t值:%f p值:%f'
              % (factor, index, n1_real, n2_real, up_meanreturn_real, down_meanreturn_real,up_meanreturn_real-down_meanreturn_real,t_value_real, p_value_real,
                 n1_theory, n2_theory,up_meanreturn_theory, down_meanreturn_theory,up_meanreturn_theory-down_meanreturn_theory ,t_value_theory, p_value_theory))

        # 作图
        fig = plt.figure(figsize=(16,3))  # 设置图片大小
        # 各个子图的设置
        ax1 = fig.add_subplot(1,4, 1)  
        ax1.set_title("%s上行对%s的影响-真实" % (factor, index),fontsize=10)
        ax1.tick_params(labelsize=8)
        plt.fill_between(x=range(n1_real), y1=up_df_real["return"])
        ax2 = fig.add_subplot(1,4, 2)      
        ax2.set_title("%s下行对%s的影响-真实" % (factor, index),fontsize=10)
        ax2.tick_params(labelsize=8)
        plt.fill_between(x=range(n2_real), y1=down_df_real["return"])
        ax3 = fig.add_subplot(1,4, 3)  
        ax3.set_title("%s上行对%s的影响-理想" % (factor, index),fontsize=10)
        ax3.tick_params(labelsize=8)
        plt.fill_between(x=range(n1_theory), y1=up_df_theory["return"], color="green")  
        ax4 = fig.add_subplot(1,4, 4)  
        ax4.set_title("%s下行对%s的影响-理想" % (factor, index),fontsize=10)
        ax4.tick_params(labelsize=8)
        plt.fill_between(x=range(n2_theory), y1=down_df_theory["return"], color="green")
        plt.show()


# # 3. 基于单个宏观指标变化趋势的资产配置策略

# ## 3.1 资产配置规则

# 1. 采用1个月作为调仓的周期。在每一个换仓时点，首先我们将考察各个宏观指标的最新变化趋势，并统计历史上该指标的变化趋势是否会对某一个大类资产的下期收益产生显著的影响。如果存在显著影响，则根据影响的方向在基准权重的基础上调整下一个月对应资产的配置权重
# 2. 对于同一个资产，在某一个月末的换仓时点可能存在多个宏观指标趋势对其未来收益存在较为显著的影响。在这种情况下，我们将根据宏观指标变化趋势对于资产的正面影响的数量与负面影响的数量，在基准权重的基础上来决定下一期对应资产的权重
# 
# 
# **资产配比原则：** 每类资产占比的最大浮动区间范围为+/-20%，在大类资产类别内部，根据宏观指标的变动趋势赋予得分，每多一个有利指标加5%/子资产数量（如沪深300就是2.5%，商品就是1.25%）的权重，每多一个有不利指标减5%/子资产数量的权重。如大类资产整体没有达到封顶权重，则最后按照四类大类资产的占比进行归一化。如大类资产整体达到封顶权重，则现在大类资产内部先按照封顶权重进行比例分摊，最后再大类资产之间进行归一化。
# 
# 设定资产类别及影响因素的映射关系表
# * 权益（30%）：
#     * 沪深300（12.5%）: 工业增加值当月同比（正向）；PMI（正向）；LME三个月期铜价格（正向）；波罗的海干散货指数（正向）；国债到期收益率10年期（正向）；美元指数（负向）
#     * 中证500（12.5%）：工业增加值当月同比（正向）；PMI（正向）；LME三个月期铜价格（正向）；波罗的海干散货指数（正向）；国债到期收益率10年期（正向）；美元指数（负向）
# * 债券（30%）：
#     * 中证国债（12.5%）：工业增加值当月同比（负向）；PMI（负向）；LME三个月期铜价格（负向）；波罗的海干散货指数（负向）；CPI当月同比（负向）；PPI当月同比（负向）；国债到期收益率10年期（负向）；美元指数（正向）
#     * 中证企业债（12.5%）：工业增加值当月同比（负向）；PMI（负向）；LME三个月期铜价格（负向）；波罗的海干散货指数（负向）；CPI当月同比（负向）；PPI当月同比（负向）；国债到期收益率10年期（负向）；美元指数（正向）
# * 商品（20%）：
#     * 黄金（5%）：美元指数（负向）
#     * 农产品（5%）：LME三个月期铜价格（正向）；波罗的海干散货指数（正向）；PPI当月同比（正向）；WTI原油现货价（正向）
#     * 基本金属（5%）：工业增加值当月同比（正向）；PMI（正向）；LME三个月期铜价格（正向）；波罗的海干散货指数（正向）；WTI原油现货价（正向）；美元指数（弱）
#     * 能源化工(5%)：工业增加值当月同比（正向）；PMI（正向）；LME三个月期铜价格（正向）；波罗的海干散货指数（正向）；WTI原油现货价（正向）
# * 货币（20%）：
# 工业增加值当月同比（负向）；PMI（负向）；LME三个月期铜价格（负向）；波罗的海干散货指数（负向）；PPI当月同比（负向）；WTI原油现货价（负向）；M2同比（负向）

# ## 3.2 资产回测过程 - 基于HP滤波法判定趋势

# In[44]:


# 采用HP滤波方法判断宏观指标趋势，并构建策略
# 基准权重
weight_stock = [0.15, 0.15]
weight_bond = [0.15, 0.15]
weight_comm = [0.05, 0.05, 0.05, 0.05]
weight_curr = [0.2]
weight = weight_stock + weight_bond + weight_comm + weight_curr

# 基准是几类资产按照固定配比，日度再平衡
# 先计算日度收益，再乘以权重，最后累乘
bench_return = index_return_data.dot(weight)
bench_cumreturn = pd.DataFrame(qs.utils.to_prices(bench_return, 1)).rename(
    columns={0: "基准收益"}
)

bench_cumreturn.plot_bokeh.line(
    panning=False,
    # rangetool=True,
    zooming=False,
    title="基准收益",
    figsize=(800, 450),
)

data2 = macro_data.copy()
for factor in macro_data.columns:
    data2[factor].dropna(axis=0, inplace=True)
    # 生成移动平均宏观指标
    data2[factor + "_HP滤波"] = sm.tsa.filters.hpfilter(
        macro_data[factor].dropna(axis=0), 100
    )[1]
    data2[factor + "_flag"] = 0

for i in range(macro_data.shape[0] - 1):
    # 先判定每类宏观指标的变动方向
    for factor in macro_data.columns:
        if data2[factor + "_HP滤波"][i] > data2[factor + "_HP滤波"].shift(1)[i]:
            data2[factor + "_flag"][i] = 1  # 宏观指标上涨flag=1
        elif data2[factor + "_HP滤波"][i] < data2[factor + "_HP滤波"].shift(1)[i]:
            data2[factor + "_flag"][i] = -1  # 宏观指标下跌flag=-1
        else:
            data2[factor + "_flag"][i] = 0  # 宏观指标与上期一致flag=0

        # flag字段用于记录月末宏观指标变动方向，position1模拟真实情况，下月初调仓，position2模拟理想情况，假设能预测到当月指标变化，并于当月初调仓
        data1["flag"] = data1["position1"] = data1["position2"] = 0





