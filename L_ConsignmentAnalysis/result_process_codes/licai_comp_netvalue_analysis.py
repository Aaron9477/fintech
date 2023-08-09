# -*- coding: utf-8 -*-
# --------------------------------
# @Time      : 2023年7月25日
# @Author    : WSS
# @File      : licai_comp_netvalue_analysis
# @Project   : 银行理财代销图鉴
# @Function  ：生成【底层数据_净值指标_理财公司】依赖表
# --------------------------------
#需要用到的库
import pandas as pd
import empyrical as emp
import numpy as np

from preprocess import exclude_mother_child_relation, preprocess
from sectorize import sectorize


def cal_score(type,AssetValue_rank,interval_ret_annual_rank,
                max_draw_down_rank,sharpe_rank):
    """ 计算每个理财产品的得分"""
    coef_asset = 0
    coef_ret = 0
    coef_mdd = 0
    coef_sharpe = 0
    if type == '现金管理类':
        coef_asset = 0.3
        coef_ret = 0.7
    elif type == '固定收益类（非现金）':
        coef_ret = 0.6
        coef_mdd = 0.2
        coef_sharpe = 0.2
    elif type == '混合类':
        coef_ret = 0.3
        coef_mdd = 0.3
        coef_sharpe = 0.4
    elif type == '权益类':
        coef_ret = 0.3
        coef_mdd = 0.3
        coef_sharpe = 0.4
    elif type == '商品及衍生品类':
        coef_ret = 0.3
        coef_mdd = 0.3
        coef_sharpe = 0.4

    score = AssetValue_rank * coef_asset + interval_ret_annual_rank * coef_ret + \
                      max_draw_down_rank * coef_mdd + sharpe_rank * coef_sharpe
    return score

def func_three(x):#计算近三个月收益率，不满三个月的使用已有数据三月化
    x=x.iloc[-13:]
    if x.notna().sum()==0:
        return np.nan
    else:
        if(not np.isnan(x[-1]))&(not np.isnan(x[0])):
            return x[-1]/x[0]-1
        else:
           if (not np.isnan(x.iloc[-1])):
               x=x.fillna(method='ffill')
               return emp.annual_return((x/x.shift(1)-1).dropna(),annualization=13)
           else:
               k=-1
               for i in range(-1,-52,-1):
                   if (not np.isnan(x.iloc[i])):
                       k=i
                       break
               x=x.iloc[:k+1].fillna(method='ffill')
               return emp.annual_return((x/x.shift(1)-1).dropna(),annualization=13)

def func_halfyear(x):#计算近半年收益率，不满半年的使用已有数据半年化
    x=x.iloc[-26:]
    if x.notna().sum()==0:
        return np.nan
    else:
        if(not np.isnan(x[-1]))&(not np.isnan(x[0])):
            return x[-1]/x[0]-1
        else:
           if (not np.isnan(x.iloc[-1])):
               x=x.fillna(method='ffill')
               return emp.annual_return((x/x.shift(1)-1).dropna(),annualization=26)
           else:
               k=-1
               for i in range(-1,-52,-1):
                   if (not np.isnan(x.iloc[i])):
                       k=i
                       break
               x=x.iloc[:k+1].fillna(method='ffill')
               return emp.annual_return((x/x.shift(1)-1).dropna(),annualization=26)


def func_oneyear(x):#计算近一年收益率，不满一年的使用已有数据年化
    x=x.iloc[-52:]
    if x.notna().sum()==0:
        return np.nan
    else:
        if(not np.isnan(x.iloc[-1]))&(not np.isnan(x.iloc[0])):
            return x.iloc[-1]/x.iloc[0]-1
        else:
            if (not np.isnan(x.iloc[-1])):
                x=x.fillna(method='ffill')
                return emp.annual_return((x/x.shift(1)-1).dropna(),annualization=52)
            else:
                k=-1
                for i in range(-1,-52,-1):
                    if (not np.isnan(x.iloc[i])):
                        k=i
                        break
                x=x.iloc[:k+1].fillna(method='ffill')
                return emp.annual_return((x/x.shift(1)-1).dropna(),annualization=52)


def func_vio(x):#计算近一年波动率，不满一年的计算期间波动率
    x=x.iloc[-52:]
    if x.notna().sum()==0:
        return np.NaN
    else:
        x=x.dropna()
        n=x.count()
        return np.std(x/x.shift(1)-1) * np.sqrt(n)

def np_average (values, weights): 
    weight_ave=pd.DataFrame()
    weight_ave['value']=values
    weight_ave['weight']=weights
    weight_ave=weight_ave.dropna()
    if sum (weight_ave['weight'])<0.001:
        return None
    else:
        return (weight_ave['value'] * weight_ave['weight']).sum() /  (weight_ave['value'].notna() *weight_ave['weight']).sum()
    
def np_average_juzhen (values):
    if values.shape[0]==1:
        #print(values.shape)
        return values
    else:
        if (values['AssetValue'].notna().sum()==0)|((values['AssetValue']).sum()<0.0000001):
            weight_ave=pd.DataFrame()
            weight_ave=values.iloc[:,:-1]
            weight_ave['count']=values.iloc[:,:-1].count(axis=1)
            #print(weight_ave)
            result=weight_ave.sort_values(by='count',axis=0,ascending=False).iloc[:1,:]
            #print(result.shape)
            #print(weight_ave.sort_values(by='count',axis=0,ascending=False).index[0])
            return result
        else:
            weight_ave=pd.DataFrame()
            weight_ave=values.iloc[:,:-1]
            col=weight_ave.columns
            weight_ave['weight']=values['AssetValue'].copy()
            #weight_ave=weight_ave.dropna()
            result=pd.DataFrame(index=[0],columns=values.columns)
            for i in col:
                if ((weight_ave[i]).notna()*weight_ave['weight']).sum()==0:
                    result.loc[0,i]=np.NaN
                else:
                    result.loc[0,i]=(weight_ave[i] * weight_ave['weight']).sum() / ((weight_ave[i]).notna()*weight_ave['weight']).sum()
            #print(result.shape)
            return result

        
#删除数据过少行数
def drop_line(x,n=10):
    y=x.dropna().copy()
    if y.count()<n:
        x[:]=np.NaN
        return x
    else :
        return x
            
def licai_comp_netvalue_analysis(start_date,df1,df2,df7,result_type='single'):
    '''
    function:生成【底层数据_净值指标_理财公司】依赖表
    params:
        - start_date:datetime64，数据更新的开始时间;
        - df1:dataframe，银行理财产品的基础数据表;
        - df2:dataframe，银行理财产品的代销表;
        - df7:dataframe，银行理财产品产品的周度净值数据;
        - result_type:str,数据生成的报表类型，取值有'single'(代表单个公司数据)，'licai_sector'(理财公司分版块),'daixiao_sector'(代销公司分版块)，'sector'(理财公司和代销机构都分版块)。
    return:
        - 底层数据_净值指标_理财公司:【底层数据_净值指标_理财公司】依赖表，用于更新理财图鉴。
    '''
    
    df1_temp=preprocess(df1,start_date,False)
    df1_temp = sectorize(df1_temp,type=result_type)
    df1_temp.replace('固定收益类','固定收益类（非现金）', inplace = True)
    df1_temp.replace('商品及金融衍生品类','商品及衍生品类', inplace = True)
    df7_temp=pd.merge(df7,df1_temp,on='FinProCode')
    df3_temp=pd.merge(df1_temp,df2,left_on='FinProCode',right_on='普益代码')
    df4_temp=exclude_mother_child_relation(df3_temp)
    df4_temp_list = df4_temp['FinProCode'].unique()
    
    周度时间_list=list(df7.columns[:])
    周度时间_list=周度时间_list+['理财公司简称','InvestmentType','AssetValue']
    
    for m in ['否','是']:
        if m=='是':
            df7_temp=df7_temp[df7_temp['FinProCode'].isin(df4_temp_list)]
        净值指标_加权平均=df7_temp[周度时间_list].groupby(['理财公司简称','InvestmentType']).apply(np_average_juzhen)
        净值指标_加权平均.drop( 'AssetValue',axis=1,inplace=True)
        净值指标_加权平均=净值指标_加权平均.droplevel(None)
        净值指标_加权平均=净值指标_加权平均.astype(float, errors = 'raise')
        净值指标_加权平均=净值指标_加权平均.apply(drop_line,axis=1)#删除数据缺失很多的行
        净值指标_加权平均=净值指标_加权平均.dropna(how='all')
        #print(1)
        
        净值指标_理财公司=pd.DataFrame(columns=['threemon_ret','sixmon_ret','oneyear_return'],index=净值指标_加权平均.index)
        #净值指标_理财公司_否.index=净值指标_加权平均.index
        净值指标_理财公司['threemon_ret']=净值指标_加权平均.apply(func_three,axis=1)
        净值指标_理财公司['sixmon_ret']=净值指标_加权平均.apply(func_halfyear,axis=1)
        净值指标_理财公司['oneyear_return']=净值指标_加权平均.apply(func_oneyear,axis=1)
        #计算最大回撤
        净值指标_理财公司['max_markdown']= 净值指标_加权平均.apply(lambda x : emp.max_drawdown((x[-53:]/x.shift(1)[-53:]-1).dropna()),axis=1)
        #计算夏普比率    
        净值指标_理财公司['sharpo'] = 净值指标_理财公司['oneyear_return']/abs(净值指标_理财公司['max_markdown'])
        #净值指标_理财公司['sharpo']= 净值指标_加权平均.apply(lambda x : emp.sharpe_ratio((x[-53:]/x.shift(1)[-53:]-1).dropna(), risk_free=0, annualization=52),axis=1)
        #计算波动率
        净值指标_理财公司['violia']=净值指标_加权平均.apply(lambda x : func_vio(x),axis=1)
        #计算资产规模
        净值指标_理财公司['Asset'] = df7_temp[周度时间_list].groupby(['理财公司简称','InvestmentType'])['AssetValue'].sum()
        
        净值指标_理财公司=净值指标_理财公司.swaplevel('理财公司简称','InvestmentType')
    
        #计算排名
        for j in 净值指标_理财公司.index.get_level_values('InvestmentType').unique():
            count_ret=净值指标_理财公司.loc[j,'oneyear_return'].count()
            count_maxdraw=净值指标_理财公司.loc[j,'max_markdown'].count()
            count_sharpo=净值指标_理财公司.loc[j,'sharpo'].count()
            count_asset=净值指标_理财公司.loc[j,'Asset'].count()
            for i in 净值指标_理财公司.loc[j].index:
                净值指标_理财公司.loc[(j,i),'ret_rank']=净值指标_理财公司.loc[j,'oneyear_return'].rank(method='min',ascending=True)[i]/count_ret
                净值指标_理财公司.loc[(j,i),'oneyear_rank']=净值指标_理财公司.loc[j,'oneyear_return'].rank(method='min',ascending=False)[i]
                净值指标_理财公司.loc[(j,i),'oneyear_count']=count_ret
                净值指标_理财公司.loc[(j,i),'maxdraw_rank']=净值指标_理财公司.loc[j,'max_markdown'].rank(method='min',ascending=True)[i]/count_maxdraw
                净值指标_理财公司.loc[(j,i),'sharpo_rank']=净值指标_理财公司.loc[j,'sharpo'].rank(method='min',ascending=True)[i]/count_sharpo
                净值指标_理财公司.loc[(j,i),'asset_rank']=净值指标_理财公司.loc[j,'Asset'].rank(method='min',ascending=True)[i]/count_asset
        净值指标_理财公司[['ret_rank','maxdraw_rank','sharpo_rank','asset_rank']]=净值指标_理财公司[['ret_rank','maxdraw_rank','sharpo_rank','asset_rank']].fillna(0)
        #计算得分
        for j in 净值指标_理财公司.index.get_level_values('InvestmentType').unique():
            for i in 净值指标_理财公司.loc[j].index:
                净值指标_理财公司.loc[(j,i),'score']=cal_score(j,净值指标_理财公司.loc[(j,i),'asset_rank'],净值指标_理财公司.loc[(j,i),'ret_rank'],净值指标_理财公司.loc[(j,i),'maxdraw_rank'],净值指标_理财公司.loc[(j,i),'sharpo_rank'])
        #对得分进行排名     
        for j in 净值指标_理财公司.index.get_level_values('InvestmentType').unique():
            count_score=净值指标_理财公司.loc[j,'score'].count()
            for i in 净值指标_理财公司.loc[j].index:
                净值指标_理财公司.loc[(j,i),'score_rank']=净值指标_理财公司.loc[j,'score'].rank(method='min',ascending=False)[i]
                净值指标_理财公司.loc[(j,i),'score_sum']=count_score
    
        if m=='是':
            净值指标_理财公司['是否剔除母子关系']='是'
            净值指标_理财公司.sort_index(inplace=True)
            底层数据_净值指标_理财公司_是=净值指标_理财公司.copy()
        if m=='否':
            净值指标_理财公司['是否剔除母子关系']='否'
            净值指标_理财公司.sort_index(inplace=True)
            底层数据_净值指标_理财公司_否=净值指标_理财公司.copy()

    底层数据_净值指标_理财公司=pd.concat([底层数据_净值指标_理财公司_否,底层数据_净值指标_理财公司_是]) 
    底层数据_净值指标_理财公司=底层数据_净值指标_理财公司.drop(['ret_rank','maxdraw_rank','sharpo_rank','asset_rank'], axis=1)
    底层数据_净值指标_理财公司.replace(np.inf,'-', inplace = True)
    底层数据_净值指标_理财公司 = 底层数据_净值指标_理财公司.fillna(value="-")
    底层数据_净值指标_理财公司 = 底层数据_净值指标_理财公司.swaplevel('理财公司简称','InvestmentType')
    
    return 底层数据_净值指标_理财公司
