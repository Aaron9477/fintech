# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import jieba
import re
import datetime
import string
import zhon.hanzi as hanzi

import warnings

warnings.filterwarnings("ignore", category=Warning)


class set_infos(object):
    def __init__(self):
        self.add_list = add_list
        self.tag_remove = tag_remove
        self.tag_pre_selected = tag_pre_selected
        self.symbol = symbol
        self.spec = spec


add_list = [
    '乐享天天', '惠享天天', '净享利', '悦享利', '天天利', '光银', '海融财富', '定开',
    '广银', '邮银财富', '邮银财智', '鑫享利', '皎月', '月月享盈', '悦盈利', '鑫盈利',
    '万利宝', '农银', '乐赢', '尊享', '鑫尊享', '丰裕', '金钻', '半年鑫', '双周鑫', '月月鑫',
    '日日新', '天天利', '惠享天天', '尊享天天', '万利宝', '鑫稳盈', '双周利', '超享象',
    '金雪球', '灵活宝', '理财金葵', '慧赢', '科创'
]

tag_remove = ['心灵', '鑫', '新', '之乐', '之尊享', '半年', '灵活宝现金管理', '两年', '稳健', '成长', '']
tag_pre_selected = ['橙', '红', '青', '紫', '金']

symbol = hanzi.punctuation + string.punctuation
spec = [
    '开放', '款', '人民币', '纯债', '债券', '个人', '法人', '个月定', '天', '固收',
    '增强型', '产品', '宏观', '策略', '可', '转股', '债权', '封闭', '资产', '量化',
    '定', '三年', '封闭型', '竞争力', '主题', '每日', '天持盈', '债转股',
    '增强', '双周', '平衡', '春节', '专享', '沪', '深', '指数', '挂钩', '科技', '创新',
    '最', '短', '持有', '定开', '天持', '盈固收', '个', '月', '市场', '中性',
    '年定', '开', '首个', '第', '年', '号', '测试', '专用', '一年', '日', '申月',
    '赎公募', '最低', '最短', '零售', '灵活', '管理', '全球', '配置', '积极进取', '多资产',
    '之', '多元', '计划', '每月', '每年', '三个', '纯债型', '四个', '月定', '日日', '光银',
    '广银', '邮银财富', '邮银财智', '幸福', '精选', '之一', '定开', '海融财富',
    '中信', '十四个', '周周', '珠联璧合', '私银尊享', '十八'
]


def set_exist_proc(set_string):
    out_sets = []
    if str(set_string) == 'nan':
        return out_sets
    sets = set_string.split('、')
    for set_ in sets:
        set_ = set_.replace('）', '')
        if '（' in set_:
            set_split = set_.split('（')
            set_1 = set_split[0]
            set_2s = set_split[1].split('；')
            for set_2 in set_2s:
                out_sets.append(set_1 + '-' + set_2)
        else:
            out_sets.append(set_)
    return out_sets


def get_str_in_symbol(string, symbol):
    string_split = string.split(symbol)
    if len(string_split) > 2:
        return string_split[1]
    return string


def cut(string):
    if str(string) == 'nan':
        return ([])
    string = re.sub('\(.*?\)', '', string)
    string = re.sub('（.*?）', '', string)
    string = get_str_in_symbol(string, '"')
    string = string.split('系列')[0]
    string = string.split('理财产品')[0]
    string = string.split('理财计划')[0]
    string = string.split('周期')[0]
    string = string.split('期')[0]
    string = string.split('类')[0]
    string = string.split('公募')[0]
    # string=re.sub('".*?"','',string)
    out = jieba.lcut(string)
    return out


def clear(string):
    if str(string) == 'nan':
        return ('')
    string = re.sub('\(.*?\)', '', string)
    string = re.sub('（.*?）', '', string)
    return string


def Identify_special_symbols(string):
    for s in string:
        if not ('a' <= s <= 'z' or 'A' <= s <= 'Z' or s.isdigit() or s in symbol):
            return False
    return True

def remove_company_info(info):
    company_info = cut(info[0]) + cut(info[1])
    product_info = cut(info[5])
    other_info = cut(info['MinInvestTimeType']) + cut(info['RaisingType']) + cut(info['OperationType']) + cut(info['InvestmentType'])
    out = []
    for field in product_info:
        if (field not in company_info + other_info) and not Identify_special_symbols(field) and not field in spec:
            out.append(field)
    return out


def cut_tag(tag):
    cut_ori = cut(tag)
    cut_out = [tag]
    for tag_cut in cut_ori:
        if (len(tag_cut) > 1 or tag_cut in tag_pre_selected) and tag_cut not in tag_remove:
            cut_out.append(tag_cut)
    return cut_out


def get_company_tag_cuts(company_tags):
    company_tag_cuts = []
    for tag in company_tags.values:
        if len(tag) > 0 and tag not in tag_remove:
            company_tag_cuts += cut_tag(tag)
    company_tag_cuts = list(set(company_tag_cuts))
    return company_tag_cuts


def get_tag_abundance(company_tags):
    company_tag_cuts = get_company_tag_cuts(company_tags)
    tag_abundance = []
    for company_tag_cut in company_tag_cuts:
        num = 0
        for company_tag in company_tags:
            if company_tag_cut in company_tag:
                num += 1
        tag_abundance.append(num)
    out = pd.Series(tag_abundance, index=company_tag_cuts)
    return out.sort_values(ascending=False)


def select_tag(tag_abundance):
    max_abundance = tag_abundance.values[0]
    sel_tag_abundance = tag_abundance[tag_abundance >= max_abundance]
    sel_tags = list(sel_tag_abundance.index)
    return (max(sel_tags, key=len, default=''))


def replace_tags(x, tags):
    for tag in tags:
        if tag in x:
            return tag
    return x


def detect_tag(x, tags):
    for tag in tags:
        if x == tag:
            return False
    return True


def replace_others(x, tags):
    for tag in tags:
        if tag in x:
            return tag
    return '其他'


def fill_exist_sets(x, tags):
    for tag in tags:
        tag_splits = tag.split('-')
        replace_tag = 1
        for tag_split in tag_splits:
            if tag_split not in x:
                replace_tag = 0
        if replace_tag == 1:
            return tag
        # if tag_splits[0] in  x:
        #    return tag_splits[0]
    return x


def replace_puyi(x, company_products):
    info = company_products.loc[x]
    product_series = info['product_series']
    set_ = info['set0']
    if not info['CompanyName'] == '华夏理财有限责任公司':
        return set_
    if set_ == '其他':
        if not str(product_series) == 'nan':
            return product_series
    return set_


def get_set(data, set_exist_dict):
    set_info = set_infos()

    add_list = set_info.add_list

    for word in add_list:
        jieba.add_word(word)

    company_list = list(set(data['CompanyName']))

    symbol = set_info.symbol
    spec = set_info.spec

    company_product_infos = []
    for ind in data.index:
        company_product_infos.append(remove_company_info(data.loc[ind]))

    company_product_infos_str = []
    for company_product_info in company_product_infos:
        company_product_info_str = ''
        for string_ in company_product_info:
            company_product_info_str += string_
        company_product_infos_str.append(company_product_info_str)

    data['tag'] = company_product_infos_str

    tag_remove = set_info.tag_remove
    tag_pre_selected = set_info.tag_pre_selected

    company_sets_dict = {}
    company_products = pd.DataFrame()
    for i in range(0, len(company_list)):
        company_product = data[data['CompanyName'] == (company_list[i])]
        company_tags0 = company_product['tag'] + '&&&' + company_product['product_name'].apply(lambda x: clear(str(x)))
        company_tags = company_tags0.copy()
        if company_list[i] in list(set_exist_dict.keys()):
            selected_tags = list(set_exist_dict[company_list[i]])
        else:
            selected_tags = []
        for selected_tag in selected_tags:
            if selected_tag.split('-')[0] not in selected_tags:
                selected_tags.append(selected_tag.split('-')[0])
        company_tags = company_tags.apply(lambda x: fill_exist_sets(x, selected_tags))
        company_tags = company_tags.apply(lambda x: ((' ' + x).split('&&&')[0]).replace(' ', ''))
        # selected_tags=list(set_exist_dict[company_list[i]])
        renew = 1
        while renew:
            company_tags_proc = company_tags[company_tags.apply(lambda x: detect_tag(x, selected_tags))]
            tag_abundance = get_tag_abundance(company_tags_proc)
            if len(tag_abundance) > 0 and tag_abundance.values[0] >= 2:
                selected_tag = select_tag(tag_abundance)
                selected_tags.append(selected_tag)
                company_tags = company_tags.apply(lambda x: replace_tags(x, selected_tags))
            else:
                renew = 0
                company_tags = company_tags.apply(lambda x: replace_others(x, selected_tags))
        company_product['set0'] = list(company_tags)
        company_sets_dict[company_list[i]] = selected_tags
        if len(company_products.index) == 0:
            company_products = company_product.copy()
        else:
            company_products = pd.concat([company_products, company_product], axis=0)

    company_products['set'] = pd.Series(company_products.index, index=company_products.index).apply(
        lambda x: replace_puyi(x, company_products))

    return company_products







