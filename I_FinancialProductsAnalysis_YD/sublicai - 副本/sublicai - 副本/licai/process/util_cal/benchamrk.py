# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/8/4 13:18 
# @Author    : Wangyd5 
# @File      : benchamrk
# @Project   : licai
# @Function  ：
# --------------------------------
import numpy as np
import pandas as pd
import re
import datetime

from fuzzywuzzy import fuzz
from difflib import SequenceMatcher

import warnings
warnings.filterwarnings("ignore")

#根据日期信息返回具体的基准指数收益率数值
def get_index_annret(benchmark_code,start_date,end_date):
    if end_date>end_date_default:
        end_date=end_date_default
    if start_date<start_date_default:
        start_date=start_date_default
    time_len=(end_date-start_date).days/365
    cal_tip=benchmark_elements_info.loc['计算说明',benchmark_code]
    value_default=benchmark_elements_info.loc['标准值',benchmark_code]
    if end_date<start_date_default or start_date>end_date_default:
        return value_default
    if cal_tip in ['标准值指数化','无权限','WIND','无数据']:
        return value_default
    #print(benchmark_code)
    benchmark_elements_info_cal=benchmark_elements_info[benchmark_code].loc[start_date:end_date]
    if cal_tip in ['EDB','利率']:
        return benchmark_elements_info_cal.mean()
    ret=benchmark_elements_info_cal.iloc[-1]/benchmark_elements_info_cal.iloc[0]-1
    ret_ann=(1+ret)**(time_len)-1
    return ret_ann


# 根据拆分后的类似于“中债综合全价指数”去匹配最优基准
def get_benchmark(string):
    demo_num = benchmark_elements_code.shape[0]
    elements_demo = benchmark_elements_code.index.values
    sequenceMatcher = SequenceMatcher()
    match_matrix = np.zeros(demo_num)
    for demoi in range(demo_num):
        sequenceMatcher.set_seqs(string, elements_demo[demoi])
        match_matrix[demoi] = fuzz.partial_ratio(string, elements_demo[demoi])

    # 设置阈值，匹配度最高为100分，高于high_limit的直接输出，低于low_limit的报错，两者之间的检查
    high_limit = 90
    low_limit = 70
    type_out = ''
    if match_matrix.max() < high_limit and match_matrix.max() > low_limit:
        type_out = 'Check'
        # print("检查基准《" + string + "》是否为：" + benchmark_elements_code.loc[
        #     elements_demo[match_matrix.argmax()], '输出名称'])
        # judgment_signal = input('判断是否正确')
        judgment_signal = 'y'
        if judgment_signal == 'N' or judgment_signal == 'n':
            bm_output = input('输入基准名称：')
            code_output = input('输入基准代码：')
            value_output = input('输入基准收益率：')
            excel_file = '匹配基准库.xlsx'
            df1 = pd.read_excel(excel_file, sheet_name='Sheet1')
            new_row1 = {'匹配名': str(string), '输出代码': bm_output, '输出名称': code_output, '输出值': value_output}
            df1 = df1.append(new_row1, ignore_index=True)
            df1.to_excel("匹配基准库.xlsx", sheet_name='Sheet1', index=False, header=True)
            return bm_output, code_output, value_output, type_out

    if match_matrix.max() < low_limit:
        type_out = 'Error'

    elements_result = elements_demo[match_matrix.argmax()]
    benchmark_name = benchmark_elements_code.loc[elements_result, '输出名称']
    benchmark_code = benchmark_elements_code.loc[elements_result, '输出代码']
    return_value=get_index_annret(benchmark_code,start_date,end_date)
    #return_value = benchmark_elements_code.loc[elements_result, '输出值']#这个位置可以修改benchmark输出值

    return benchmark_name, benchmark_code, return_value, type_out


# 处理纯数值型的基准，例如【2.64%】、【2.21-3.32】
def judge_num(num_text):
    # 检查是否含有英文字母字符，并且处理"170bp"类型
    if re.search(r"[a-zA-Z]", num_text):
        if 'bp' in num_text:
            bp_pattern = r"(\d+)\s*bp\s*"   # "170bp"
            match0 = re.search(bp_pattern, num_text)
            if match0:
                num1 = str(float(match0.group(1))/100) + '%'
                return 'num', num1, num1
        elif 'BP' in num_text:
            bp_pattern = r"(\d+)\s*BP\s*"  # "170BP"
            match0 = re.search(bp_pattern, num_text)
            if match0:
                num1 = str(float(match0.group(1)) / 100) + '%'
                return 'num', num1, num1
        else:
            return 'NAN', 'num_text', 'num_text'

    # 检查是否有汉字字符，并考虑"0.01或5"以及"浮动基数0.01"
    if re.search(r"[\u4e00-\u9fff]", num_text):
        if re.search(r"(\d+\.\d+|\d+)\s*或\s*(\d+\.\d+|\d+)\s*或\s*(\d+\.\d+|\d+)", num_text):
            huo_pattern = r"(\d+\.\d+|\d+)\s*或\s*(\d+\.\d+|\d+)\s*或\s*(\d+\.\d+|\d+)"  # "0.01或4或6"
            match1 = re.search(huo_pattern, num_text)
            if match1:
                num1 = match1.group(1) + '%'
                num2 = match1.group(2) + '%' + '或' + match1.group(3) + '%'
                return 'huo', num1, num2
        if re.search(r"(\d+\.\d+|\d+)\s*或\s*(\d+\.\d+|\d+)", num_text):
            huo_pattern = r"(\d+\.\d+|\d+)\s*或\s*(\d+\.\d+|\d+)"  # "0.01或5"
            match1 = re.search(huo_pattern, num_text)
            if match1:
                num1 = match1.group(1) + '%'
                num2 = match1.group(2) + '%'
                return 'huo', num1, num2
        if re.search(r"\s*浮动基数\s*(\d+\.\d+|\d+)", num_text):
            num_pattern = r"\s*浮动基数\s*(\d+\.\d+|\d+)"  # "浮动基数0.01"
            match1 = re.search(num_pattern, num_text)
            if match1:
                num1 = match1.group(1) + '%'
                return 'num', num1, num1
        if re.search(r"\s*浮动基数\s*(\d+\.\d+|\d+)%", num_text):
            num_pattern = r"\s*浮动基数\s*(\d+\.\d+|\d+)%"  # "浮动基数0.01%"
            match1 = re.search(num_pattern, num_text)
            if match1:
                num1 = match1.group(1) + '%'
                return 'num', num1, num1
        return 'NAN', 'num_text', 'num_text'

    interval_pattern = [r"\【(\d+.\d+)-(\d+.\d+)\】%",  # "【2.50-3.00】%"
                        r"\【(\d+.\d+)-(\d+.\d+)\】",   # "【3.40-3.90】"
                        r"\【(\d+.\d+)%-(\d+.\d+)%\】",  # "【3.40%-3.90%】"
                        r"(\d+.\d+)-(\d+.\d+)"]        # "0.0100-5.4000"
    for each in interval_pattern:
        match = re.search(each, num_text)
        if match:
            num1 = match.group(1) + '%'
            num2 = match.group(2) + '%'
            return 'interval', num1, num2

    #   num_pattern中正则表达式顺序不能更换，否则匹配会出错
    num_pattern = [r"\【(\d+.\d+)\】%",  # "【2.50】%"
                   r"\【(\d+.\d+)%\】",  # "【2.50%】"
                   r"\【(\d+.\d+)\】",   # "【3.40】"
                   r"(\d+.\d+)%",       # "5.40%"
                   r"(\d+)%",           # "6%"
                   r"(\d+.\d+)",        # "5.40"
                   r"(\d+)"]            # "6"
    for each in num_pattern:
        match = re.search(each, num_text)
        if match:
            num1 = match.group(1) + '%'
            return 'num', num1, num1

    return 'NAN', 'num_text', 'num_text'


# 对初始输入的文本字符串进行处理，删除某些字符、修改符号、修改特殊的某些字符
def delete_char(tt_demo):
    match_1 = re.search(r'(加\d{1,3}个基点)', tt_demo)
    if match_1:
        old_str = match_1.group(1)
        new_str = '+' + str(int(old_str[1:-3]) * 10) + 'bp'
        tt_demo = tt_demo.replace(old_str, new_str)

    if tt_demo.endswith('+浮动基准'):
        tt_demo = tt_demo[:-len('+浮动基准')]

    tt_demo = tt_demo.replace('即', '')
    tt_demo = tt_demo.replace('浮动基数0.00', '浮动基数0.00%')
    tt_demo = tt_demo.replace('40％杭银理财三潭映月', '40％*杭银理财三潭映月')
    tt_demo = tt_demo.replace('60％中国人民银行', '60％*中国人民银行')
    tt_demo = tt_demo.replace('业绩参考区间：', '')
    tt_demo = tt_demo.replace('(CBA03423.CS)', '')
    tt_demo = tt_demo.replace('观察期', '')
    tt_demo = tt_demo.replace('涨跌幅', '')
    tt_demo = tt_demo.replace('开放周期内', '')
    tt_demo = tt_demo.replace('(1.5%)', '')
    tt_demo = tt_demo.replace('(1.50%)', '')
    tt_demo = tt_demo.replace('(1.50)', '')
    tt_demo = tt_demo.replace('×', '*')
    tt_demo = tt_demo.replace('％', '%')
    tt_demo = tt_demo.replace(' ', '')
    tt_demo = tt_demo.replace('＋', '+')
    tt_demo = tt_demo.replace('[', '【')
    tt_demo = tt_demo.replace(']', '】')
    return tt_demo


# 主函数，对初始字符串进行处理，输出匹配处理后结果
def get_lookup(tt_demo):
    if tt_demo[-1] in [',', '.', '，', '。']:
        tt_demo = tt_demo[:-1]
    if ',' in tt_demo or '，' in tt_demo or '。' in tt_demo or '；' in tt_demo:
        # 按照逗号句号拆分，分别处理
        sp_text = re.split('[,，。；]', tt_demo)
        sp_output = ''
        sp_low_output = ''
        sp_high_output = ''
        sp_type = ''
        sp_list = []
        for each in sp_text:
            each = each.replace(' ', '')
            if len(each) < 1:
                continue
            each_formula, each_type, each_list, each_cal_low, each_cal_high = get_lookup(each)
            sp_output += str(each_formula) + ','
            sp_low_output += str(each_cal_low) + ','
            sp_high_output += str(each_cal_high) + ','
            sp_list = sp_list + each_list
            if 'Error' in each_type:
                sp_type = 'Error'
            if 'Check' in each_type:
                sp_type = 'Check'
        # print(sp_output[:-1])
        return sp_output[:-1], sp_type, sp_list, sp_low_output, sp_high_output
    else:
        tt_demo = delete_char(tt_demo)
        bm_input = []
        weight = []

        # 按照加号拆分后逐个进行匹配
        spilt_by_plus = re.split('[+]', tt_demo)

        for each in spilt_by_plus:
            # 处理类似于4.50%*90%的情况
            match_muti = re.match(r'(\d+(\.\d+)?%) *\s*[\*×] *\s*(\d+(\.\d+)?%)', each)
            if match_muti:
                bm_input.append(each)
                weight.append("常数基准值,权重100%")
                continue

            # 判断是否为数值或者区间
            num_type, num1, num2 = judge_num(each)
            # print(num_type)
            if num_type == 'huo':
                huo_temp = num1 + '或' + num2
                return huo_temp, '', [], huo_temp, huo_temp
            if num_type == 'interval':
                bm_input.append('[' + num1 + '-' + num2 + ']')
                weight.append("常数基准值,权重100%")
            if num_type == 'num':
                bm_input.append(num1)
                weight.append("常数基准值,权重100%")

            # 其他情况：带有变动的基准的、乱码的字符串，不具有实际意义的（按照匹配度排除输出Error）
            # 进行拆分过程
            if num_type == 'NAN':
                if '敲入' in each or '敲出' in each:
                    bm_input.append(each)
                    weight.append("常数基准值,权重100%")
                    continue
                if '*' in each and '%' in each:
                    pattern = re.compile(r'([\d\.]+)%')
                    if len(re.findall(pattern, each)) > 0:
                        weight.append(re.findall(pattern, each)[0] + "%")
                    else:
                        continue
                    bm_input.append(each.replace('*', '').strip(re.findall(pattern, each)[0] + "%"))
                if '*' in each and '%' not in each:
                    pattern = r"\b\d{1,2}\b"
                    if len(re.findall(pattern, each)) > 0:
                        weight.append(re.findall(pattern, each)[0] + "%")
                    else:
                        continue
                    bm_input.append(each.replace('*', '').strip(re.findall(pattern, each)[0]))
                if '*' not in each and '%' in each:
                    pattern = re.compile(r'([\d\.]+)%')
                    if len(re.findall(pattern, each)) > 0:
                        bm_input.append(re.findall(pattern, each)[0] + "%")
                    else:
                        if '.' in each and '-' in each:
                            pattern = r"【(\d+\.\d+)%-(\d+\.\d+)%】"
                            if len(re.findall(pattern, each)) > 0:
                                bm_input.append(re.findall(pattern, each)[0])
                            else:
                                pattern = r"【(\d+\.\d+)-(\d+\.\d+)】%"
                                if len(re.findall(pattern, each)) > 0:
                                    bm_input.append(re.findall(pattern, each)[0])
                                    weight.append("常数基准值,权重100%")
                                continue
                            weight.append("常数基准值,权重100%")
                    weight.append("常数基准值,权重100%")

                if '*' not in each and '%' not in each:
                    if '.' in each and '-' in each:
                        pattern = r"【(\d+\.\d+)-(\d+\.\d+)】"
                        if len(re.findall(pattern, each)) > 0:
                            bm_input.append(re.findall(pattern, each)[0])
                        else:
                            continue
                        weight.append("常数基准值,权重100%")
                    else:
                        bm_input.append(each)
                        weight.append("100%")

        # 进行匹配过程
        output = ''
        type_mark = ''
        error_list = []
        check_list = []
        final_cal_low = 0
        final_cal_high = 0
        for each in bm_input:
            if '敲入' in each or '敲出' in each:
                type_mark = 'Error'
                error_list.append(each)
            if weight[bm_input.index(each)] == "常数基准值,权重100%":
                output = output + str(each) + '+'
                if '-' in each:
                    if len(re.findall(r"(\d+.\d+)%", each)) > 1:
                        final_cal_low += float(re.findall(r"(\d+.\d+)%", each)[0]) / 100
                        final_cal_high += float(re.findall(r"(\d+.\d+)%", each)[1]) / 100
                else:
                    match_value = 0
                    if len(re.findall(r"(\d+.\d+)%", each)) > 0:
                        match_value = float(re.findall(r"(\d+.\d+)%", each)[0]) / 100
                    else:
                        if len(re.findall(r"(\d+)%", each)) > 0:
                            match_value = float(re.findall(r"(\d+)%", each)[0]) / 100
                    final_cal_low += match_value
                    final_cal_high += match_value
                continue

            bm_output, code_output, value_output, type_output = get_benchmark(each)

            if 'Check' in type_output:
                type_mark = 'Check'
                check_list.append(each)
            if 'Error' in type_output:
                type_mark = 'Error'
                error_list.append(each)
                output = output + code_output + '*' + str(weight[bm_input.index(each)]) + '+'
                continue

            output = output + code_output + '*' + str(weight[bm_input.index(each)]) + '+'
            each_value = value_output * float(str(weight[bm_input.index(each)]).strip('%')) / 100
            final_cal_low += each_value
            final_cal_high += each_value

        return output[:-1], type_mark, error_list+check_list, final_cal_low, final_cal_high


if __name__ == "__main__":
    from database.read.read_py_base import PyReader
    from process.module.preprocess_bank_table import select_product_info_cache
    reader = PyReader()
    df = select_product_info_cache()
    
    a = 1 / 0 
    
    benchmark_elements_code = pd.read_excel(r'D:\institution\sublicai\licai\docs\匹配基准库.xlsx',sheet_name='标准值', index_col='匹配名')
    benchmark_elements_info = pd.read_excel(r'D:\institution\sublicai\licai\docs\匹配基准库.xlsx',sheet_name='指标指数化' , index_col='标的')
    end_date_default=datetime.datetime(2023, 6, 30, 0, 0)
    start_date_default =datetime.datetime(2022, 1, 1, 0, 0)
    result_df = pd.DataFrame(columns=['RegistrationCode', 'product_name', '基准描述', '基准计算公式', '识别结果类型', '报错位置', '基准下限', '基准上限'])

    for i in range(df.shape[0]):
        text = str(df["Benchmark"][i])
        start_date=df["product_establish_date"][i]
        end_date=df["MaturityDate"][i]
        if text == 'nan':
            new_row = {'RegistrationCode': str(df["RegistrationCode"][i]), 'product_name': str(df["product_name"][i]),
                       '基准描述': ''}
            result_df = result_df.append(new_row, ignore_index=True)
            continue
        formula_result, type_result, error_list, cal_low, cal_high = get_lookup(text)
        if len(error_list) == 0:
            error_list = ''
        new_row = {'RegistrationCode': str(df["RegistrationCode"][i]), 'product_name': str(df["product_name"][i]),
                   '基准描述': text, '基准计算公式': formula_result, '识别结果类型': type_result,
                   '报错位置': str(error_list), '基准下限': cal_low, '基准上限': cal_high}
        result_df = result_df.append(new_row, ignore_index=True)
        if i % 100 == 0:
            print(str(i))
    # result_df.to_excel("benchmark0726_运行结果_0331.xlsx", encoding='ANSI')#替换输出文件路径


