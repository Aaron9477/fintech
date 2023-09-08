# -*- coding: utf-8 -*-
# --------------------------------
# @Time      : 2023年7月31日
# @Author    : WSS
# @Change    :Noah Zhan 2023年8月3日14:13:01
# @File      : main_周度加权平均净值处理
# @Project   : 银行理财代销图鉴
# @Function  ：使用【理财产品净值数据】和【all_nv_data_new】生成【周度净值_均值处理_未筛选存续期】依赖表
# --------------------------------


# 需要用到的库
import pandas as pd
import datetime as dt
from tqdm import tqdm
import numpy as np
import warnings
from WeeklyYield_to_nv import WeeklyYield_to_nv
from fillna_within_n import func_horizontal_fillna, func_vertical_fillna
from get_processed_nv_datas import get_processed_nv_data, get_processed_nv_datas
from preprocess import preprocess

warnings.filterwarnings("default")
from parameter import *


def weekly_average_nav():
    path_new = r".\raw_datas\all_nv_data_new.csv"
    # read
    df1 = pd.read_excel(path_基本数据,index_col=0).infer_objects()
    df1["理财公司简称"] = df1.apply(lambda x: x[0].split("有限")[0], axis=1)
    df9 = pd.read_csv(path_all净值数据, encoding="utf-8")
    df9["EndDate"] = df9["EndDate"].astype("datetime64[ns]")
    df10 = pd.read_csv(path_new, encoding="utf-8")
    df10["EndDate"] = df10["EndDate"].astype("datetime64[ns]")


    现金管理类_七日年化 = pd.DataFrame()
    lc_codes = df1[df1["InvestmentType"] == "现金管理类"]["FinProCode"]
    missing_lc_codes = []

    df_date = pd.read_excel(path_周度日期, header=None)
    df_date = df_date.iloc[1:, 0]
    df_date = df_date[df_date<=end_date]
    周度日期_list = list(df_date)

    for lc_code in tqdm(lc_codes):
        try:
            if 现金管理类_七日年化.empty:
                现金管理类_七日年化 = get_processed_nv_data(
                    df9, lc_code, begin_date=None, end_date=None, is_cash=True
                )
            else:
                现金管理类_七日年化 = pd.concat(
                    [
                        现金管理类_七日年化,
                        get_processed_nv_data(
                            df9,
                            lc_code,
                            begin_date="20210101",
                            end_date="20230731",
                            is_cash=True,
                        ),
                    ],
                    axis=0,
                )
        except ValueError:
            missing_lc_codes.append(lc_code)
        # print(lc_code,"现金管理类产品，净值数据精度不足，不能转化为7日年化收益......")
        except AttributeError:
            continue
    print("以下现金管理类产品，净值数据精度不足，不能转化为7日年化收益", missing_lc_codes)
    warnings.filterwarnings("default")
    # 现金管理类_七日年化

    # #### 填补缺失值-现金管理
    # 填补现金管理类数据缺失值
    现金管理_填补缺失 = 现金管理类_七日年化.groupby("FinProCode").apply(func_vertical_fillna, null_n=8)
    现金管理_矩阵 = 现金管理_填补缺失.set_index(["FinProCode", "EndDate"]).unstack()[
        "LatestWeeklyYield"
    ]
    现金管理_周度矩阵 = 现金管理_矩阵[周度日期_list]
    # 将现金管理类收益率数据转化为净值数据
    现金管理_净值矩阵 = 现金管理_周度矩阵.apply(WeeklyYield_to_nv, axis=1)
    # 现金管理_净值矩阵

    # ### 基础净值数据处理
    日度数据_矩阵 = df10.set_index(["FinProCode", "EndDate"]).unstack()[
        "AccumulatedUnitNV_new"
    ]

    # 填补缺失值（已加进度条）
    print("----------数据缺失值填补开始----------")
    tqdm.pandas(desc="apply")
    日度数据_填补缺失 = 日度数据_矩阵.progress_apply(func_horizontal_fillna, axis=1)
    print("----------数据缺失值填补完毕----------")
    #### 与现金管理数据合并
    现金管理_净值矩阵.replace(0, np.NaN, inplace=True)
    现金管理_净值矩阵 = 现金管理_净值矩阵.dropna(how="all")
    现金管理_净值矩阵_list = list(现金管理_净值矩阵.index)
    周度数据_填补缺失 = 日度数据_填补缺失[周度日期_list]
    # 将现金管理净值数据和非现金管理部分数据合并
    现金管理_净值矩阵_交集 = list(set(现金管理_净值矩阵.index) & set(周度数据_填补缺失.index))
    周度数据_合并 = 周度数据_填补缺失.drop(index=现金管理_净值矩阵_交集)
    周度净值数据_处理 = pd.concat([周度数据_合并, 现金管理_净值矩阵])
    周度净值数据_处理 = 周度净值数据_处理.dropna(how="all")
    # 周度净值数据_处理

    # ### 计算产品加权平均值
    # 计算加权平均净值
    def np_average(values):
        if values.shape[0] == 1:
            # print(values.shape)
            return values
        else:
            if (values["AssetValue"].notna().sum() == 0) | (
                (values["AssetValue"]).sum() < 0.0000001
            ):
                weight_ave = pd.DataFrame()
                weight_ave = values.iloc[:, :-1]
                weight_ave["count"] = values.iloc[:, :-1].count(axis=1)
                # print(weight_ave)
                result = weight_ave.sort_values(
                    by="count", axis=0, ascending=False
                ).iloc[:1, :]
                # print(result.shape)
                # print(weight_ave.sort_values(by='count',axis=0,ascending=False).index[0])
                return result
            else:
                weight_ave = pd.DataFrame()
                weight_ave = values.iloc[:, :-1]
                col = weight_ave.columns
                weight_ave["weight"] = values["AssetValue"].copy()
                result = pd.DataFrame(index=[0], columns=values.columns)
                for i in col:
                    if ((weight_ave[i]).notna() * weight_ave["weight"]).sum() == 0:
                        result.loc[0, i] = np.NaN
                    else:
                        result.loc[0, i] = (
                            weight_ave[i] * weight_ave["weight"]
                        ).sum() / ((weight_ave[i]).notna() * weight_ave["weight"]).sum()
                # print(result.shape)
                return result

    周度净值数据_合并 = pd.merge(
        周度净值数据_处理,
        df1[["FinProCode", "RegistrationCode", "AssetValue"]],
        on="FinProCode",
    )
    # 计算净值的加权平均值（已加进度条）
    print("----------加权平均净值计算开始----------")
    tqdm.pandas(desc="apply")
    周度净值_均值_ = 周度净值数据_合并.groupby(["RegistrationCode"]).progress_apply(np_average)
    print("----------加权平均净值计算完毕----------")
    周度净值_均值 = 周度净值_均值_.drop(["FinProCode", "AssetValue", "count"], axis=1)
    # 周度净值_均值
    df1_temp_ = preprocess(df1, start_date_month, False)
    周度净值_均值处理_未筛选存续期 = pd.merge(
        周度净值_均值, df1_temp_[["RegistrationCode", "FinProCode"]], on="RegistrationCode"
    )
    周度净值_均值处理_未筛选存续期["RegistrationCode"] = 周度净值_均值处理_未筛选存续期["FinProCode"]
    周度净值_均值处理_未筛选存续期.drop("FinProCode", axis=1, inplace=True)
    周度净值_均值处理_未筛选存续期.rename(columns={"RegistrationCode": "FinProCode"}, inplace=True)
    # 周度净值_均值处理_未筛选存续期
    周度净值_均值处理_未筛选存续期.to_excel(r".\raw_datas\周度净值_均值处理_未筛选存续期.xlsx", index=False)

