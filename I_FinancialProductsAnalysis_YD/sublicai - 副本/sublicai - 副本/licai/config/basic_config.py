# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/9/14 10:54 
# @Author    : Wangyd5 
# @File      : basic_config
# @Project   : sublicai
# @Function  ：
# --------------------------------
import os
import datetime


# 项目绝对路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
today = datetime.datetime.now().strftime('%Y%m%d')


# 定义运行环境
environment = 'test'

# 定义数据库连接信息
class DatabaseInfo:
    # wind
    _wind = {
        "production": {"host": "10.16.233.38",
                       "user": "zhengu",
                       "password": "yurmluxSGscCuqkjlJgLKg==\n",
                       "database": "wande",
                       "charset": "utf8"},
        "test": {"host": "10.101.221.183",
                 "user": "readeronly",
                 "password": "GR3IyVedDoKVhUSJMq1ckA==\n",
                 "database": "wande",
                 "charset": "utf8"},

    }
    wind = _wind[environment]


    #  聚源数据库
    _juyuan = {
        "production": {"host": "",  # fixme 错误
                       "user": "",
                       "password": "",
                       "database": "",
                       "charset": ""},

        "test": {"host": "10.237.122.83",
                 "user": "readeronly",
                 "password": "GR3IyVedDoKVhUSJMq1ckA==\n",
                 "database": "JYDB",
                 "charset": "utf8"},

    }
    juyuan = _juyuan[environment]

    # 理财评估结果表
    _licai = {
        "production": {"host": "10.16.244.110",
                       "port": "1521",
                       "user": "bank_wealth",
                       "password": "shGagCQiFcba5BODD0tC+Q==\n",
                       "database": "licai",
                       },
        # "production": {"host": "10.16.244.110",
        #                "port": "1521",
        #                "user": "jjpg",
        #                "password": "dYme2U97Ju62E151FgJ46w==\n",
        #                "database": "jjpg_bak",
        #                },

        "test": {
            "host": "10.48.92.69",
            "port": "15061",
            "user": "bank_wealth",
            "password": "shGagCQiFcba5BODD0tC+Q==\n",
            "database": "licai",
        },}
    licai = _licai[environment]


    # 基金评估系统test

    _fundtest = {
        "production": {"host": "10.16.244.110",
                       "port": "1521",
                       "user": "jjpg",
                       "password": "dYme2U97Ju62E151FgJ46w==\n",
                       "database": "jjpg",
                       },
        # "production": {"host": "10.16.244.110",
        #                "port": "1521",
        #                "user": "jjpg",
        #                "password": "dYme2U97Ju62E151FgJ46w==\n",
        #                "database": "jjpg_bak",
        #                },

        "test": {
            "host": "10.237.102.44",
            "port": "1521",
            "user": "CELVETEST",
            "password": "FrFQRfOxLoYgEYNWdBFxlw==\n",
            "database": "celve",
        },}
    fundtest = _fundtest[environment]



    # 基金评估系统

    _fund = {
        "production": {"host": "10.16.244.110",
                       "port": "1521",
                       "user": "jjpg",
                       "password": "dYme2U97Ju62E151FgJ46w==\n",
                       "database": "jjpg",
                       },
        # "production": {"host": "10.16.244.110",
        #                "port": "1521",
        #                "user": "jjpg",
        #                "password": "dYme2U97Ju62E151FgJ46w==\n",
        #                "database": "jjpg_bak",
        #                },

        "test": {
            "host": "10.237.102.44",
            "port": "1521",
            "user": "celve",
            "password": "QT1Bzx1w9T6BdfdteY8wAg==\n",
            "database": "celve",
        },}
    fund = _fund[environment]

    # 普益

    _py = {
        "production": {"host": "10.16.244.110",
                       "port": "1521",
                       "user": "jjpg",
                       "password": "dYme2U97Ju62E151FgJ46w==\n",
                       "database": "jjpg",
                       },
        # "production": {"host": "10.16.244.110",
        #                "port": "1521",
        #                "user": "jjpg",
        #                "password": "dYme2U97Ju62E151FgJ46w==\n",
        #                "database": "jjpg_bak",
        #                },

        "test": {
            "host": "10.48.85.24",
            "port": "3307",
            "user": "root",
            "password": "hW8WyQccqURkRUljCDBGGQ==\n",
            "database": "pybz",
        },}
    py = _py[environment]
    # Zxjtzj12!@#$


