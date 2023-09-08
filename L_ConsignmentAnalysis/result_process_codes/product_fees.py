# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023年7月21日09:11:10
# @Author    : Noah Zhan
# @File      : product_fees
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_产品费率】依赖表
# --------------------------------


import dateutil
import numpy as np
import pandas as pd

from data_process_codes.preprocess import exclude_mother_child_relation, preprocess
from sectorize import sectorize

def print_1():
    print('2')

def product_fees(start_date,end_date,df1,df2,if_sector = False):
    '''
    function:生成【底层数据_产品费率】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - end_date:datetime64，数据更新的截止时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - if_sector:是否计算板块数据。
    return:
        - 底层数据_产品费率:【底层数据_产品费率】依赖表，用于更新理财图鉴。
    '''
    print(" *生成【底层数据_产品费率】依赖表, ",start_date,"到",end_date,"...")
    
    底层数据_产品费率 = pd.DataFrame()
    date = end_date
    i = 1

    def func4(x):#关于管理费要综合采用两列数据，进行这个函数这样的操作,how='left'
        if x[0] is not np.nan:
            return x[0]
        else:
            return x[1]

    while date >= start_date:
        print(" -Processing date ",date)
        month_begin_date = date - dateutil.relativedelta.relativedelta(months=1) + dateutil.relativedelta.relativedelta(days=1)#月初
        df1_temp = preprocess(df1,end_date)
        df1_temp['manage_fee'] = df1_temp[['manage_fee_y','manage_fee_x']].apply(func4,axis=1)#新生成一列管理费，综合使用之前的两列数据
        df1_temp['sale_fee'] = df1_temp[['sale_fee_y','sale_fee_x']].apply(func4,axis=1)#新生成一列销售费，综合使用之前的两列数据
        df2_temp = df2[(df2['代销开始日']<date)&(df2['代销结束日']>month_begin_date)]
        df3_temp = pd.merge(df1_temp,df2_temp,how='inner',left_on=['RegistrationCode','FinProCode'],right_on=['产品登记编码','普益代码'])#合并匹配基础数据和代销数据
        df4_temp = exclude_mother_child_relation(df3_temp)#剔除母子公司之间建立的代销关系

        if if_sector:
            df3_temp_licai_sector = sectorize(df3_temp,type='licai_sector')
            df4_temp_licai_sector = sectorize(df4_temp,type='licai_sector')
            df3_temp_daixiao_sector = sectorize(df3_temp,type='daixiao_sector')
            df4_temp_daixiao_sector = sectorize(df4_temp,type='daixiao_sector')
        else:
            df3_temp_licai_sector = df3_temp
            df4_temp_licai_sector = df4_temp
            df3_temp_daixiao_sector = df3_temp
            df4_temp_daixiao_sector = df4_temp
            
        #先计算理财机构的数据(对于理财公司)
        底层数据_产品费率_temp = pd.DataFrame(columns = ['日期','固定管理费-未剔除母子关系','固定管理费水平-未剔除母子关系','销售费-未剔除母子关系','销售费水平-未剔除母子关系','固定管理费-剔除母子关系','固定管理费水平-剔除母子关系','销售费-剔除母子关系','销售费水平-剔除母子关系'])
        固定管理费_未剔除母子关系 = df3_temp_licai_sector.groupby(['理财公司简称','InvestmentType'])['manage_fee'].agg('mean')
        底层数据_产品费率_temp['固定管理费-未剔除母子关系'] = 固定管理费_未剔除母子关系
        底层数据_产品费率_temp.index = 固定管理费_未剔除母子关系.index
        底层数据_产品费率_temp['日期'] = date
        底层数据_产品费率_temp['销售费-未剔除母子关系'] = df3_temp_licai_sector.groupby(['理财公司简称','InvestmentType'])['sale_fee'].agg('mean')
        底层数据_产品费率_temp['固定管理费-剔除母子关系'] = df4_temp_licai_sector.groupby(['理财公司简称','InvestmentType'])['manage_fee'].agg('mean')
        底层数据_产品费率_temp['销售费-剔除母子关系'] = df4_temp_licai_sector.groupby(['理财公司简称','InvestmentType'])['sale_fee'].agg('mean')
        
        #固定管理费水平-未剔除母子关系(对每一类产品进行类别内的排名，后面的代码也是一样)
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类','固定管理费水平-未剔除母子关系'
                        ] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类'
                                            ]['固定管理费-未剔除母子关系'].rank(method='min',ascending=False
                                                                ).apply(lambda x:str(round(x,0)
                                                                                    )+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '权益类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '权益类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '权益类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '混合类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '混合类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '混合类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类']['固定管理费-未剔除母子关系'])))
        #固定管理费水平-剔除母子关系
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '权益类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '权益类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '权益类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '混合类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '混合类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '混合类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类']['固定管理费-未剔除母子关系'])))
        #销售费水平-未剔除母子关系
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '权益类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '权益类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '权益类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '混合类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '混合类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '混合类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类']['销售费水平-未剔除母子关系'])))
        #销售费水平-剔除母子关系
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '固定收益类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '权益类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '权益类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '权益类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '混合类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '混合类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '混合类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '现金管理类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp.loc[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp[底层数据_产品费率_temp.index.get_level_values(1) == '商品及金融衍生品类']['销售费水平-未剔除母子关系'])))
        
        
        #计算代销机构的数据(对于代销机构)
        底层数据_产品费率_temp2 = pd.DataFrame(columns = ['日期','固定管理费-未剔除母子关系','固定管理费水平-未剔除母子关系','销售费-未剔除母子关系','销售费水平-未剔除母子关系','固定管理费-剔除母子关系','固定管理费水平-剔除母子关系','销售费-剔除母子关系','销售费水平-剔除母子关系'])
        固定管理费_未剔除母子关系 = df3_temp_daixiao_sector.groupby(['代销机构','InvestmentType'])['manage_fee'].agg('mean')
        底层数据_产品费率_temp2['固定管理费-未剔除母子关系'] = 固定管理费_未剔除母子关系
        底层数据_产品费率_temp2.index = 固定管理费_未剔除母子关系.index
        底层数据_产品费率_temp2['日期'] = date
        底层数据_产品费率_temp2['销售费-未剔除母子关系'] = df3_temp_daixiao_sector.groupby(['代销机构','InvestmentType'])['sale_fee'].agg('mean')
        底层数据_产品费率_temp2['固定管理费-剔除母子关系'] = df4_temp_daixiao_sector.groupby(['代销机构','InvestmentType'])['manage_fee'].agg('mean')
        底层数据_产品费率_temp2['销售费-剔除母子关系'] = df4_temp_daixiao_sector.groupby(['代销机构','InvestmentType'])['sale_fee'].agg('mean')
        
        #固定管理费水平-未剔除母子关系
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类','固定管理费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类']['固定管理费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类']['固定管理费-未剔除母子关系'])))
        #固定管理费水平-剔除母子关系
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类']['固定管理费-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类','固定管理费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类']['固定管理费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类']['固定管理费-未剔除母子关系'])))
        #销售费水平-未剔除母子关系
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类','销售费水平-未剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类']['销售费-未剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类']['销售费水平-未剔除母子关系'])))
        #销售费水平-剔除母子关系
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '固定收益类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '权益类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '混合类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '现金管理类']['销售费水平-未剔除母子关系'])))
        底层数据_产品费率_temp2.loc[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类','销售费水平-剔除母子关系'] = 底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类']['销售费-剔除母子关系'].rank(method='min',ascending=False).apply(lambda x:str(round(x,0))+'/'+str(len(底层数据_产品费率_temp2[底层数据_产品费率_temp2.index.get_level_values(1) == '商品及金融衍生品类']['销售费水平-未剔除母子关系'])))
        
        #合并数据
        底层数据_产品费率 = pd.concat([ 底层数据_产品费率,底层数据_产品费率_temp,底层数据_产品费率_temp2],axis=0)#合并不同时期的数据
        date = end_date - dateutil.relativedelta.relativedelta(months=i)#date减一个月
        i= i+1

    # 底层数据_产品费率.reset_index().to_excel(path_outputdir+r'\底层数据_产品费率.xlsx')
    return 底层数据_产品费率.reset_index()