# -*- coding: utf-8 -*-
"""
Created on Tue JUL 21 17:20:45 2022
通用函数文件
@author: 王永镇
"""

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

