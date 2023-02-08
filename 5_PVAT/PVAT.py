# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 14:41:52 2022

@author: hongwc
"""
import sys
import pandas as pd
import numpy as np
import sys
import os
import unicodedata
import re
import warnings
from datetime import datetime

warnings.filterwarnings('ignore')
from WindPy import w
import matplotlib.pyplot as plt
from PyQt5.Qt import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *


class FileDialog_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("中兵投资———文件路径选择")
        self.setFixedSize(800, 800)
        # UI设计
        self.setupUI()
        self.valuation_table_ts = []
        self.date_ls = []

    def setupUI(self):
        # 交互界面
        self.btn_choose = QPushButton("文件选择", self)
        self.btn = QPushButton("确 定", self)
        self.btn_choose.move(560, 40)
        self.btn.move(660, 40)

        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(30, 150, 740, 600))
        self.filepath_solt = QLineEdit(self)
        self.filepath_solt.setEnabled(False)
        self.block_stock_line = QLineEdit(self)
        self.block_stock_line.resize(350, 30)
        self.block_stock_line.move(30, 100)
        self.block_stock_line.setPlaceholderText("请输入大宗股票代码,多支股票以,隔开")

        self.filepath_solt.resize(500, self.btn.height())
        self.filepath_solt.move(30, 40)

        # 按键功能关联
        self.btn_choose.clicked.connect(self.folder_choose)     # 文件路径选择
        self.btn.clicked.connect(self.import_port)              # 触发文件分析

        self.combobox = QComboBox(self)
        self.combobox.move(400, 100)
        self.combobox.resize(self.btn.width() - 25, self.btn.height() )
        infomation = ["广发", "嘉实", "银华"]
        self.combobox.addItems(infomation)

        # 读取部分输入信息
        self.start_dt_label = QLabel("开始日期", self)
        self.start_dt_label.move(540, 80)
        self.start_dt = QDateEdit(self)
        self.start_dt.setDisplayFormat("yyyy-MM-dd")
        self.start_dt.setCalendarPopup(True)
        self.start_dt.resize(120, 30)
        self.start_dt.move(540, 100)
        self.start_dt.setDate(QDate.currentDate())

        self.end_dt_label = QLabel("结束日期", self)
        self.end_dt_label.move(660, 80)
        self.end_dt = QDateEdit(self)
        self.end_dt.setDisplayFormat("yyyy-MM-dd")
        self.end_dt.setCalendarPopup(True)
        self.end_dt.resize(120, 30)
        self.end_dt.move(660, 100)
        self.end_dt.setDate(QDate.currentDate())

    def folder_choose(self):
        self.dir_pth = QFileDialog.getExistingDirectory(None, "估值表文件路径", os.getcwd())
        self.filepath_solt.setText(self.dir_pth)

    # 分析入口
    def import_port(self):
        start_date_str=self.start_dt.dateTime().toString("yyyyMMdd")
        end_date_str=self.end_dt.dateTime().toString("yyyyMMdd")
        file_ls = os.listdir(self.dir_pth)
        block_stock_ls = self.block_stock_line.text().split(",")
        self.block_stock_ls = [code.strip() for code in block_stock_ls if code.strip() != ""]   # 要过滤掉的大宗股票，不参与计算
        # 存储读取到的估值表内容
        self.valuation_table_ts = []
        self.date_ls = []   # 存储估值表文件对应的时间点
        if self.combobox.currentText() == "广发":
            if len(file_ls) > 0:
                for i, file_i in enumerate(file_ls):
                    try:
                        date_i=file_i[16:24]    # 取估值表文件名称里的时间，时间在名称里的文本位置需要确定
                        # 判断估值表日期是否在分析区间内:
                        if date_i>=start_date_str and date_i<=end_date_str:
                            self.textBrowser.append("读取估值表..." + file_i)
                            QApplication.processEvents()
                            self.date_ls.append(file_i[16:24])
                            self.valuation_table_ts.append(pd.read_excel(self.dir_pth + "/" + file_i, header=4))

                    except:
                        self.textBrowser.append("文件类型错误，非Excel文件")
                        file_ls = []
                        self.date_ls = []
                        self.valuation_table_ts = []
                        return
            else:
                self.textBrowser.append("文件夹内容为空")
                return

            if len(self.valuation_table_ts) <= 1:
                QApplication.processEvents()
                self.textBrowser.append("时间区间选择有误......")
            else:
                # 进行数据分析
                self.data_export()
                QApplication.processEvents()
                self.textBrowser.append("统计结果导出.......")

        if self.combobox.currentText() == "嘉实":
            if len(file_ls) > 0:
                for i, file_i in enumerate(file_ls):
                    try:
                        date_i=file_i[26:30] + file_i[31:33] + file_i[34:36]
                        if date_i>=start_date_str and date_i<=end_date_str:
                            self.textBrowser.append("读取估值表..." + file_i)
                            QApplication.processEvents()
                            self.date_ls.append(file_i[26:30] + file_i[31:33] + file_i[34:36])
                            self.valuation_table_ts.append(pd.read_excel(self.dir_pth + "/" + file_i, header=4))

                    except:
                        self.textBrowser.append("文件类型错误，非Excel文件")
                        file_ls = []
                        self.date_ls = []
                        self.valuation_table_ts = []
                        return
            else:
                self.textBrowser.append("文件夹内容为空")
                return

            if len(self.valuation_table_ts)<=1:
                QApplication.processEvents()
                self.textBrowser.append("时间区间选择有误......")
            else:
                self.data_export()
                QApplication.processEvents()
                self.textBrowser.append("统计结果导出.......")

        if self.combobox.currentText() == "银华":
            if len(file_ls) > 0:
                for i, file_i in enumerate(file_ls):
                    try:
                        date_i=file_i[10:14] + file_i[15:17] + file_i[18:20]
                        if date_i>=start_date_str and date_i<=end_date_str:
                            self.textBrowser.append("读取估值表..." + file_i)
                            QApplication.processEvents()
                            self.date_ls.append(file_i[10:14] + file_i[15:17] + file_i[18:20])
                            self.valuation_table_ts.append(pd.read_excel(self.dir_pth + "/" + file_i, header=4))

                    except:
                        self.textBrowser.append("文件类型错误，非Excel文件")
                        file_ls = []
                        self.date_ls = []
                        self.valuation_table_ts = []
                        return
            else:
                self.textBrowser.append("文件夹内容为空")
                return

            if len(self.valuation_table_ts)<=1:
                QApplication.processEvents()
                self.textBrowser.append("时间区间选择有误......")
            else:
                self.data_export()
                QApplication.processEvents()
                self.textBrowser.append("统计结果导出.......")

    def get_stock_code(self, code):
        if code[0] in ['0', '3']:
            return code + '.SZ'
        elif code[0] in ['4', '8']:
            return code + '.BJ'
        elif code[0] in ['6']:
            return code + '.SH'

    # 绩效归因分析
    def data_export(self):
        w.start()

        self.daily_data_ls = self.valuation_table_ts
        self.date_list = self.date_ls
        self.daily_nav_list = []
        for i, data_i in enumerate(self.daily_data_ls):
            nav_i = data_i.loc[data_i['科目代码'] == '累计单位净值', '科目名称'].values[0]    # 提取该日估值表里的净值
            self.daily_nav_list.append(nav_i)

        # 定制投后绩效分析

        self.original_port = pd.DataFrame()  # 大宗原组合
        self.reduce_block_dic = {}  # 大宗交易减持时点图
        self.get_stock_port()  # 统计持仓   # TODO:看到此处！！！！！！
        writer = pd.ExcelWriter(os.getcwd() + '\\' + self.combobox.currentText() + '专户.xlsx', engine='xlsxwriter')

        self.performance_compare()  # 计算组合收益及基准收益表现
        self.merge_data.to_excel(writer, sheet_name='产品净值走势')

        if len(self.block_stock_ls) > 0 and self.block_stock_ls[0] != "":
            self.reduce_block_analysis()  # 统计大宗减持时点
            for i, code_i in enumerate(self.reduce_block_dic.keys()):
                self.reduce_block_dic[code_i].to_excel(writer, sheet_name=code_i + '减持时点')

        writer.save()
        QApplication.processEvents()

    # 产品 基准 原组合收益对比
    def performance_compare(self):
        QApplication.processEvents()
        self.textBrowser.append("计算 {:}......".format("产品 基准 原组合业绩表现"))

        nav = pd.DataFrame(self.daily_nav_list, index=self.date_list)
        nav.columns = ['产品']
        start_date = self.date_list[0]
        end_date = self.date_list[-1]
        # 基准指数选取为中证800
        bench = w.wsd("000906.SH", "close", start_date, end_date, "Fill=Previous")
        bench_index = pd.DataFrame({'日期': bench.Times, '中证800': bench.Data[0]})
        bench_index['日期'] = bench_index['日期'].apply(lambda x: datetime.strftime(x, '%Y%m%d'))
        bench_index.set_index(['日期'], inplace=True)

        # 日期以交易日为准
        nav_bench_data = pd.merge(nav, bench_index, left_index=True, right_index=True, how='inner')
        nav_bench_data['产品'] = nav_bench_data['产品'].apply(lambda x: eval(x) if isinstance(x, str) == True else x)   # TODO:此处不懂，待看
        # 计算原组合收益
        if len(self.block_stock_ls) > 0 or len(self.original_port) > 0:
            try:

                original_port_ret = self.port_ret_calc(self.original_port, "原组合")
                original_port_ret.set_index(['日期'], inplace=True)

                # 合并数据
                merge_data = pd.merge(nav_bench_data, original_port_ret, left_index=True, right_index=True, how='left')
                merge_data.fillna(0, inplace=True)
                merge_data['原组合'] = (merge_data['原组合'] + 1).cumprod()

                # 业绩标准化
                self.merge_data = merge_data / merge_data.iloc[0, :]
                self.max_drawdown_calc()
            except:
                nav_bench_data = nav_bench_data / nav_bench_data.iloc[0, :]
                self.merge_data = nav_bench_data
                self.max_drawdown_calc()
        else:
            nav_bench_data = nav_bench_data / nav_bench_data.iloc[0, :]
            self.merge_data = nav_bench_data
            self.max_drawdown_calc()

    # 统计组合收益情况
    def port_ret_calc(self, port, port_name):
        def get_stock_close(stock_port):
            stock_code = list(stock_port['股票代码'])
            date_now = list(stock_port['日期'])[0]
            date_next = list(stock_port['下一日'])[0]
            QApplication.processEvents()
            self.textBrowser.append("统计组合收益{:}......".format(date_now))

            close = w.wsd(stock_code, "close", date_now, date_now, "Days=Alldays;Fill=Previous").Data[0]
            stock_port['收盘价'] = close
            close = w.wsd(stock_code, "close", date_next, date_next, "Days=Alldays;Fill=Previous").Data[0]
            stock_port['下一日收盘价'] = close
            return stock_port

        port_ret_ls = [0]
        date_list = sorted(list(set(port['日期'])))
        for i, date_i in enumerate(date_list):
            if i == len(date_list) - 1:
                break
            else:
                start_date = date_list[i]
                end_date = date_list[i + 1]
                price_st = port.loc[port['日期'] == start_date, :]
                price_st['下一日'] = end_date
                # 获取收盘价
                price = price_st.groupby(['日期']).apply(get_stock_close)
                ret_i = np.sum((price['下一日收盘价'] / price['收盘价'] - 1) * price['市值占比'])
                # 计算组合收益
                port_ret_ls.append(ret_i)

        port_ret = pd.DataFrame({'日期': date_list, port_name: port_ret_ls})
        return port_ret

    # 计算动态回撤
    def max_drawdown_calc(self):
        drawdown_ls = [0]
        nav_ls = list(self.merge_data['产品'])
        for i in range(len(nav_ls)):
            if i == 0:
                continue
            else:
                drawdown = nav_ls[i] / max(nav_ls[:i + 1]) - 1
                drawdown_ls.append(drawdown)
        self.merge_data['产品动态回撤'] = drawdown_ls

    # 统计全部持仓股票 不包括新股
    def get_stock_port(self):
        stock_list = []
        date_list = []
        stock_num_list = []
        percent_list = []
        unit_cost = []

        if self.combobox.currentText() in ["广发", "嘉实"]:
            for i, data_i in enumerate(self.daily_data_ls):
                for j, sbj_j in enumerate(data_i['科目代码']):
                    if (str(sbj_j)[:4] == "1102" and len(str(sbj_j)) > 12 and data_i['停牌信息'][j] == "正常交易") or (
                            str(sbj_j)[11:17] + '.' + str(sbj_j)[-2:] in self.block_stock_ls):
                        # 1102.03 上交所网上新股
                        # 1102.04 上交所网下新股
                        # 1102.34 深交所网下新股
                        stock_code = sbj_j[11:17] + '.' + sbj_j[-2:]
                        stock_list.append(stock_code)
                        date_list.append(self.date_list[i])
                        stock_num_list.append(data_i['数量'][j])
                        percent_i = data_i['市值占比'][j]
                        if isinstance(percent_i, str) == True and percent_i[-1] == "%":
                            percent_i = eval(percent_i[:-1]) / 100
                        percent_list.append(percent_i)
                        unit_cost.append(data_i['单位成本'][j])

        if self.combobox.currentText() in ['银华']:
            for i, data_i in enumerate(self.daily_data_ls):
                for j, sbj_j in enumerate(data_i['科目代码']):
                    if (str(sbj_j)[:4] == "1102" and len(str(sbj_j)) > 12 and data_i['停牌信息'][j] == "正常交易") or (
                            self.get_stock_code(str(sbj_j)[-6:]) in self.block_stock_ls):
                        # 1102.03 上交所网上新股
                        # 1102.04 上交所网下新股
                        # 1102.34 深交所网下新股
                        stock_code = self.get_stock_code(str(sbj_j)[-6:])
                        stock_list.append(stock_code)
                        date_list.append(self.date_list[i])
                        stock_num_list.append(data_i['数量'][j])
                        percent_i = data_i['市值占比'][j]
                        if isinstance(percent_i, str) == True and percent_i[-1] == "%":
                            percent_i = eval(percent_i[:-1]) / 100
                        percent_list.append(percent_i)
                        unit_cost.append(data_i['单位成本'][j])

        # 返回全部股票持仓
        stock_port = pd.DataFrame(
            {'日期': date_list, '股票代码': stock_list, '股票数目': stock_num_list, '市值占比': percent_list, '单位成本': unit_cost})
        stock_port = stock_port.groupby(['日期', '股票代码']).sum()
        self.stock_port = stock_port.reset_index()
        self.original_port = self.stock_port[self.stock_port['股票代码'].isin(self.block_stock_ls)]

    # 大宗减持时点
    def reduce_block_analysis(self):
        def get_stock_close(stock_port):
            stock_code = list(stock_port['股票代码'])
            date = list(stock_port['日期'])[0]
            QApplication.processEvents()
            self.textBrowser.append("计算 {:}.......".format("产品 基准 原组合业绩表现"))
            close = w.wsd(stock_code, "close", date, date, "Days=Alldays;Fill=Previous").Data[0]
            stock_port['收盘价'] = close
            return stock_port

        self.original_port = self.original_port.groupby(['日期']).apply(get_stock_close)

        for i, stock_code_i in enumerate(self.block_stock_ls):
            try:
                num_price_block_i = self.original_port[self.original_port['股票代码'].isin([stock_code_i])]
                # 统计减持收益
                num_price_block_i['卖出数量'] = num_price_block_i['股票数目'].diff().fillna(0)
                num_price_block_i['卖出数量'] = - num_price_block_i['卖出数量']
                num_price_block_i['累计收益'] = (num_price_block_i['收盘价'] - num_price_block_i['单位成本']) * num_price_block_i[
                    '卖出数量']
                num_price_block_i['累计收益'] = num_price_block_i['累计收益'].cumsum()
                self.reduce_block_dic[stock_code_i] = num_price_block_i
            except:
                continue

    # 统计组合收益情况
    def port_ret_calc(self, port, port_name):
        def get_stock_close(stock_port):
            stock_code = list(stock_port['股票代码'])
            date_now = list(stock_port['日期'])[0]
            date_next = list(stock_port['下一日'])[0]
            QApplication.processEvents()
            self.textBrowser.append("统计组合收益{:}......".format(date_now))
            close = w.wsd(stock_code, "close", date_now, date_now, "Days=Alldays;Fill=Previous").Data[0]
            stock_port['收盘价'] = close
            close = w.wsd(stock_code, "close", date_next, date_next, "Days=Alldays;Fill=Previous").Data[0]
            stock_port['下一日收盘价'] = close
            return stock_port

        port_ret_ls = [0]
        date_list = sorted(list(set(port['日期'])))
        for i, date_i in enumerate(date_list):
            if i == len(date_list) - 1:
                break
            else:
                start_date = date_list[i]
                end_date = date_list[i + 1]
                price_st = port.loc[port['日期'] == start_date, :]
                price_st['下一日'] = end_date
                # 获取收盘价
                price = price_st.groupby(['日期']).apply(get_stock_close)
                ret_i = np.sum((price['下一日收盘价'] / price['收盘价'] - 1) * price['市值占比'])
                # 计算组合收益
                port_ret_ls.append(ret_i)

        port_ret = pd.DataFrame({'日期': date_list, port_name: port_ret_ls})
        return port_ret

    # 计算动态回撤
    def max_drawdown_calc(self):
        drawdown_ls = [0]
        nav_ls = list(self.merge_data['产品'])
        for i in range(len(nav_ls)):
            if i == 0:
                continue
            else:
                drawdown = nav_ls[i] / max(nav_ls[:i + 1]) - 1
                drawdown_ls.append(drawdown)
        self.merge_data['产品动态回撤'] = drawdown_ls


    # 大宗减持时点
    def reduce_block_analysis(self):
        def get_stock_close(stock_port):
            stock_code = list(stock_port['股票代码'])
            date = list(stock_port['日期'])[0]
            QApplication.processEvents()
            self.textBrowser.append("统计大宗股票减持收益{:}.......".format(date))
            close = w.wsd(stock_code, "close", date, date, "Days=Alldays;Fill=Previous").Data[0]
            stock_port['收盘价'] = close
            return stock_port

        self.original_port = self.original_port.groupby(['日期']).apply(get_stock_close)
        QApplication.processEvents()
        self.textBrowser.append("统计 {:}......".format("大宗股票减持时点"))
        for i, stock_code_i in enumerate(self.block_stock_ls):
            try:
                num_price_block_i = self.original_port[self.original_port['股票代码'].isin([stock_code_i])]
                # 统计减持收益
                num_price_block_i['卖出数量'] = num_price_block_i['股票数目'].diff().fillna(0)
                num_price_block_i['卖出数量'] = - num_price_block_i['卖出数量']
                num_price_block_i['累计收益'] = (num_price_block_i['收盘价'] - num_price_block_i['单位成本']) * num_price_block_i[
                    '卖出数量']
                num_price_block_i['累计收益'] = num_price_block_i['累计收益'].cumsum()
                self.reduce_block_dic[stock_code_i] = num_price_block_i
            except:
                continue
        QApplication.processEvents()
        self.textBrowser.append("统计完成......")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_window = FileDialog_Window()
    file_window.show()
    sys.exit(app.exec())
