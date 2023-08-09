# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月21日13:32:33
# @Author    : Noah Zhan
# @File      : merge2cols_ues_col2_if_col1_empty
# @Project   : 银行理财代销图鉴
# @Function  ：综合采用两列数据,首先使用位置1的数据，如果位置1为空则使用位置2.
# --------------------------------

import numpy as np


def merge2cols_ues_col2_if_col1_empty(x):
    '''
    综合采用两列数据,首先使用位置1的数据，如果位置1为空则使用位置2.(用于dataframe.apply()中以快速处理数据)
    '''
    if x[0] is not np.nan:
        return x[0]
    else:
        return x[1]