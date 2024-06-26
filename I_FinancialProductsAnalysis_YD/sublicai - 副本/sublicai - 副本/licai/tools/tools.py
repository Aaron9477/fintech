# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/9/19 18:42 
# @Author    : Wangyd5 
# @File      : tools
# @Project   : sublicai
# @Function  ：
# --------------------------------

import pandas as pd
import numpy as np
import os
import sys
# from openpyxl.utils import get_column_letter
from time import *
import datetime
from config.basic_config import project_path

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = clock()
        return self

    def __exit__(self, *args):
        self.end = clock()
        self.secs = self.end - self.start
        self.min = self.secs/60
        self.millisecond = self.secs * 1000  # millisecond
        if self.verbose:
            if self.secs <0.1:
                print('elapsed time: %f ms' % self.millisecond)

            elif self.secs<10:
                print('elapsed time: %f s' % self.secs)
            else:
                print('elapsed time: %f min' % self.min)


class tool_set(object):

    @staticmethod
    def download_auto_save(path=None):
        """ 作为一个装饰器，如果未下载 就下载保存到本地，下载了就加载出来，节省时间
        @:param fname:  存储路径  eg: 'mkt.pkl'
        """
        if path is None:
            path = os.path.join(os.path.join(project_path, 'docs'))
        def outer(func):
            #  外层
            def inner(*args, **kwargs):
                if 'fname' in kwargs:
                    fname = os.path.join(path,kwargs['fname'])
                # 内层
                if not os.path.exists(fname):
                    print(f'下载数据-{fname}')

                    # print(os.environ)
                    df = func(*args, **kwargs)
                    df.to_pickle(fname)
                else:
                    print(f'--获取数据-{fname}')
                    df = pd.read_pickle(fname)
                return df
            return inner
        return outer


    @staticmethod
    def project_root_path(project_name=None, print_log=True):
        """
        获取当前项目根路径
        :param project_name: 项目名称
                                1、可在调用时指定
                                2、[推荐]也可在此方法中直接指定 将'XmindUitl-master'替换为当前项目名称即可（调用时即可直接调用 不用给参数）
        :param print_log: 是否打印日志信息
        :return: 指定项目的根路径
        """
        p_name = 'XmindUitl-master' if project_name is None else project_name
        project_path = os.path.abspath(os.path.dirname(__file__))
        # Windows
        if project_path.find('\\') != -1: separator = '\\'
        # Mac、Linux、Unix
        if project_path.find('/') != -1: separator = '/'

        root_path = project_path[:project_path.find(f'{p_name}{separator}') + len(f'{p_name}{separator}')]
        if print_log:
            print(f'当前项目名称：{p_name}\r\n当前项目根路径：{root_path}')
        return root_path

    now_date = datetime.datetime.now().strftime('%Y%m%d')


if __name__ == '__main__':
    project_name = 'gene_stock_factor'
    path = tool_set.project_root_path(project_name)

