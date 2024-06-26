# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/12/11 21:14 
# @Author    : Wangyd5 
# @File      : basic_variable
# @Project   : sublicai
# @Function  ：
# --------------------------------


# 无风险利率
rf = 0.015


# 系列识别
import os
from config.basic_config import project_path
from process.util_cal.set_identify import *

path = os.path.join(os.path.join(project_path,'docs'),'银行理财子公司调研材料.xlsx')
set_exist=pd.read_excel(path)
set_exist=pd.Series(set_exist['产品系列名单'].values,index=set_exist['公司名称'])

set_exist_dict={}
for ind in set_exist.index:
    set_exist_dict[ind]=set_exist_proc(set_exist[ind])
