# -*- coding: utf-8 -*-

# ------------------------------
# @Time    : 2020/4/17
# @Author  : gao
# @File    : generate_id.py
# @Project : fund_analysis
# ------------------------------
import uuid


def generate_id():
    return uuid.uuid4().hex

