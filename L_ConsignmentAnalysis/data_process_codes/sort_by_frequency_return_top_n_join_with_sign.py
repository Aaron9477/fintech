# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月21日13:44:15
# @Author    : Noah Zhan
# @File      : sort_by_frequency_return_top_n_join_with_sign
# @Project   : 银行理财代销图鉴
# @Function  ：根据元素出现的次数排名，再用符号连接前n个，返回字符串。
# --------------------------------

def sort_by_frequency_return_top_n_join_with_sign(x,ascending=False,n=2,sign=','):
    '''
    function:根据元素出现的次数排名，再用符号连接前n个，返回字符串。
    params:
        - x:pd.Series/pd.DataFrame,包含待元素的序列;
        - ascending:bool,是否升序;
        - n：需连接返回前n个元素;
        - sign:用于连接元素的中间间隔符号，例如','。
    return:
        - 
    '''
    return sign.join(list(x.value_counts().sort_values(ascending=ascending).index[:n]))