# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/8/2 19:55 
# @Author    : Wangyd5 
# @File      : test_set
# @Project   : licai
# @Function  ： 计算系列
# --------------------------------


from process.util_cal.set_identify import *
from config.basic_confi import project_path
import os

path = os.path.join(os.path.join(project_path,'docs'),'银行理财子公司调研材料.xlsx')
set_exist=pd.read_excel(path)
set_exist=pd.Series(set_exist['产品系列名单'].values,index=set_exist['公司名称'])

set_exist_dict={}
for ind in set_exist.index:
    set_exist_dict[ind]=set_exist_proc(set_exist[ind])


from database.read.read_py_base import PyReader
from process.module.preprocess_bank_table import select_product_info_cache
reader = PyReader()

data = select_product_info_cache()

company_products = get_set(data,set_exist_dict)



