# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.signal
import datetime
#%matplotlib inline
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置  
plt.rcParams['axes.unicode_minus'] = False  


def get_sign(point,arrmin,arrmax):
    if point in arrmin:
        return -1
    else:
        return 1
def get_min(arr):
    try:
        return min(arr)
    except:
        return 10**10
def get_max(arr):
    try:
        return max(arr)
    except:
        return -10**10
    
def get_extre(array,order=10):
    #step1：将股票价格序列进行随机化，避免同一区间内出现两个相同的最大值
    array=array+np.random.rand(len(array))*0.001
    #step2：滚动计算order区间内的极值点标识
    extres_max=scipy.signal.argrelextrema(array, np.greater, axis=0, order=order, mode='clip')[0]
    extres_min=scipy.signal.argrelextrema(array, np.less, axis=0, order=order, mode='clip')[0]
    #step3：进行不符合条件的极值点清理
    #extre_now赋初始值为最左侧的极值点
    extre_now=min(min(np.append(extres_min,10**10)),min(np.append(extres_max,10**10)))
    #while循环，使用extre_now变量作为指针，在已有的极值点位处从左到右观察，如出现不符合要求的情况，则删除对应的极值点，并将extre_now归为原始值
    while extre_now<max(max(np.append(extres_min,0)),max(np.append(extres_max,0))):
        extre_past=extre_now
        #rolling为extre_now右侧的极值点，将extre_now滚动到下一个极值点
        extres_max_rolling=extres_max[extres_max>extre_past]
        extres_min_rolling=extres_min[extres_min>extre_past]
        extre_now=min(min(np.append(extres_min_rolling,10**10)),min(np.append(extres_max_rolling,10**10)))
        #sign为extre_past、extre_now在极值点的归属，-1为极小值，1为极大值
        extre_past_sign=get_sign(extre_past,extres_min,extres_max)
        extre_now_sign=get_sign(extre_now,extres_min,extres_max)
        #开始分情况讨论，需要删去的极值点情况
        #情况1：extre_past、extre_now均为极小值，则删去对应股价较高的极值点
        if extre_past_sign+extre_now_sign<0:
            if array[extre_past]<=array[extre_now]:
                extres_min=np.delete(extres_min,np.where(extres_min==extre_now))
            elif array[extre_past]>array[extre_now]:
                extres_min=np.delete(extres_min,np.where(extres_min==extre_past))
            extre_now=min(min(np.append(extres_min,10**10)),min(np.append(extres_max,10**10)))
        #情况2：extre_past、extre_now均为极大值，则删去对应股价较低的极值点
        elif extre_past_sign+extre_now_sign>0:
            if array[extre_past]<array[extre_now]:
                extres_max=np.delete(extres_max,np.where(extres_max==extre_past))
            elif array[extre_past]>=array[extre_now]:
                extres_max=np.delete(extres_max,np.where(extres_max==extre_now))
            extre_now=min(min(np.append(extres_min,10**10)),min(np.append(extres_max,10**10)))
        #情况1、2均为出发时：进入后续情况判定
        else:
            #触发以下条件时，删除extre_past、extre_now极值点对
            #（1）extre_past至extre_now区间的最小值小于extre_past、extre_now的极低值点，即反向区间
            #（2）extre_past至extre_now区间的最大值大于extre_past、extre_now的极高值点，即反向区间
            #（3）extre_past和extre_now对应的股价相同
            if (array[extre_past:extre_now].min()<min(array[extre_past],array[extre_now]) 
                or array[extre_past:extre_now].max()>max(array[extre_past],array[extre_now])
                or abs(array[extre_past]-array[extre_now])<0.1):
                extres_max=np.delete(extres_max,np.where(extres_max==extre_past))
                extres_min=np.delete(extres_min,np.where(extres_min==extre_past)) 
                extres_max=np.delete(extres_max,np.where(extres_max==extre_now))
                extres_min=np.delete(extres_min,np.where(extres_min==extre_now))
                extre_now=min(get_min(extres_min),get_min(extres_max))
        #while循环至最后一个极值点后，判断结束
    #左端点值的处理，如果第一个极值点不是最左点，若第一个极值点为极小值，若最左点大于第一个极值点，则将最左点设为极大值点，反之，则删除第一个极值点，将最左点
    #设为极小值点（即将极小值点移动到最左点）；其他情况类似
    if min(min(np.append(extres_min,10**10)),min(np.append(extres_max,10**10)))>0:
        if get_min(extres_min)<get_min(extres_max):
            if array[extres_min[0]]<array[0]-0.001:
                extres_max=np.insert(extres_max, 0, 0)
            else:
                extres_min=np.delete(extres_min,0)
                extres_min=np.insert(extres_min, 0, 0)
        elif get_min(extres_min)>get_min(extres_max):
            if array[extres_max[0]]>array[0]+0.001:
                extres_min=np.insert(extres_min, 0, 0)
            else:
                extres_max=np.delete(extres_max,0)
                extres_max=np.insert(extres_max, 0, 0)
    max_point=len(array)-1
    if max(max(np.append(extres_min,-10**10)),max(np.append(extres_max,-10**10)))<max_point:
        if get_max(extres_min)<get_max(extres_max):
            if array[extres_max[-1]]>array[-1]+0.001:
                extres_min=np.insert(extres_min, -1, max_point)
            else:
                extres_max=np.delete(extres_max,-1)
                extres_max=np.insert(extres_max, -1, max_point)
        elif get_max(extres_min)>get_max(extres_max):
            if array[extres_min[-1]]<array[-1]-0.001:
                extres_max=np.insert(extres_max, -1, max_point)
            else:
                extres_min=np.delete(extres_min,-1)
                extres_min=np.insert(extres_min, -1, max_point)
    return(extres_min,extres_max)



# Cal_BSpreference：计算组合交易能力
# 输入：
# order：计算极致左右比较范围，单边
# stock_position_port：换手情况，包括3列：windcode：股票代码；trade：交易量（股数）；backdate：datetime格式，交易日期
# data_all：股票价格时间序列，建议至少包含stock_position_port日期范围并左右超出至少order个交易日，包括3列：windcode；S_DQ_ADJCLOSE；backdate
# ignore_edge_trading：忽略未被划分在极值点之间边缘位置的交易，建议为True，否则可能出现该处交易能力打分不准确的情况
# 输出：DataFrame，列出每个个股的交易能力和金额统计
def Cal_BSpreference(order,stock_position_port,data_all,ignore_edge_trading=True):
    stocks=list(set(stock_position_port['windcode']))
    stock_names=[]
    buy_left=[]
    sell_left=[]
    buy_right=[]
    sell_right=[]
    power_left=[]
    power_right=[]
    power_buy=[]
    amount_buy=[]
    power_sell=[]
    amount_sell=[]
    amount_left=[]
    amount_right=[]
    amount_buy_left=[]
    amount_sell_left=[]
    amount_buy_right=[]
    amount_sell_right=[]
    for stock in stocks[:]:
        stock_position_port_stock=stock_position_port[stock_position_port['windcode']==stock]        
        position_adj=pd.DataFrame(stock_position_port_stock['trade'].replace(0,np.nan))
        position_adj.columns=['持仓调整']
        position_adj.index=stock_position_port_stock['backdate'].values
        position_adj=position_adj.dropna()
        if len(position_adj.index)==0:
            continue
        stock_code=stock
        data0=data_all[data_all['windcode']==stock_code]#[['S_DQ_ADJCLOSE']]
        data=pd.DataFrame(data0['S_DQ_ADJCLOSE'].values,index=data0['backdate'].values,columns=[stock])
        data=data.sort_index()
        #else:
        #    data=get_close([stock_code],"2020-01-01","2023-08-16")
        data=data.dropna()
        start_date=stock_position_port_stock['backdate'].min()
        if data.index[0]>start_date-datetime.timedelta(days=180):
            continue
        start_date=(data.index).min()
        end_date=(data.index).max()
        data_ind=[]
        for i in range((end_date - start_date).days + 1):
            data_ind.append(start_date + datetime.timedelta(days=i))
        
        data_full=pd.DataFrame(data,index=data_ind).fillna(method='ffill')
        position_adj['close']=data_full.loc[position_adj.index,data_full.columns[0]]
        array=data.iloc[:,0].values
        extres_min,extres_max=get_extre(array,order)
        extres=np.append(extres_min,extres_max)
        LR=[]
        buy_sell_sign=[]
        LR_power=[]
        for ind_date in position_adj.index:
            ind_date_ind=np.where(np.array(data.index)==ind_date)[0][0]
            if ind_date_ind<=get_min(extres):
                position_adj=position_adj.drop(index=ind_date)
                continue
            extre_left=extres[extres<ind_date_ind].max()
            extre_right=extres[extres>=ind_date_ind].min()
            buy_sell_sign=np.sign(position_adj.loc[ind_date,'持仓调整'])
            if ignore_edge_trading and (extre_left==get_min(extres) or extre_right==get_max(extres)):
                buy_sell_sign=0
            if extre_left in extres_min:
                LR.append(buy_sell_sign)
            else:
                LR.append(-buy_sell_sign)
            if buy_sell_sign>0:
                trade_ability=(array[ind_date_ind]-min(array[extre_left],array[extre_right]))/(array[extre_right]-array[extre_left])
            else:
                trade_ability=(array[ind_date_ind]-max(array[extre_left],array[extre_right]))/(array[extre_right]-array[extre_left])
            LR_power.append(trade_ability*abs(buy_sell_sign))
        position_adj['LR']=LR
        position_adj['LR_power']=LR_power

        stock_names.append(stock)
        #细项交易能力
        position_adj_buy_left=position_adj[(position_adj['持仓调整']>0)*(position_adj['LR']<0)]
        position_adj_sell_left=position_adj[(position_adj['持仓调整']<0)*(position_adj['LR']<0)]
        position_adj_buy_right=position_adj[(position_adj['持仓调整']>0)*(position_adj['LR']>0)]
        position_adj_sell_right=position_adj[(position_adj['持仓调整']<0)*(position_adj['LR']>0)]
        # todo:这里用100减，可能因为在计算trade_ability，计算反了。需要修改。
        buy_left.append(100-100*(position_adj_buy_left['close']*np.abs(position_adj_buy_left['持仓调整']*position_adj_buy_left['LR_power'])).sum()/(position_adj_buy_left['close']*np.abs(position_adj_buy_left['持仓调整'])).sum())
        sell_left.append(100-100*(position_adj_sell_left['close']*np.abs(position_adj_sell_left['持仓调整']*position_adj_sell_left['LR_power'])).sum()/(position_adj_sell_left['close']*np.abs(position_adj_sell_left['持仓调整'])).sum())
        buy_right.append(100-100*(position_adj_buy_right['close']*np.abs(position_adj_buy_right['持仓调整']*position_adj_buy_right['LR_power'])).sum()/(position_adj_buy_right['close']*np.abs(position_adj_buy_right['持仓调整'])).sum())
        sell_right.append(100-100*(position_adj_sell_right['close']*np.abs(position_adj_sell_right['持仓调整']*position_adj_sell_right['LR_power'])).sum()/(position_adj_sell_right['close']*np.abs(position_adj_sell_right['持仓调整'])).sum())
        amount_buy_left.append((position_adj_buy_left['close']*np.abs(position_adj_buy_left['持仓调整'])).sum())
        amount_sell_left.append((position_adj_sell_left['close']*np.abs(position_adj_sell_left['持仓调整'])).sum())
        amount_buy_right.append((position_adj_buy_right['close']*np.abs(position_adj_buy_right['持仓调整'])).sum())
        amount_sell_right.append((position_adj_sell_right['close']*np.abs(position_adj_sell_right['持仓调整'])).sum())
        
        #左右交易能力
        position_adj_left=position_adj[position_adj['LR']<0]
        power_left.append(100-100*(position_adj_left['close']*np.abs(position_adj_left['持仓调整']*position_adj_left['LR_power'])).sum()/(position_adj_left['close']*np.abs(position_adj_left['持仓调整'])).sum())
        position_adj_right=position_adj[position_adj['LR']>0]
        power_right.append(100-100*(position_adj_right['close']*np.abs(position_adj_right['持仓调整']*position_adj_right['LR_power'])).sum()/(position_adj_right['close']*np.abs(position_adj_right['持仓调整'])).sum())
        amount_left.append((position_adj_left['close']*np.abs(position_adj_left['持仓调整'])).sum())
        amount_right.append((position_adj_right['close']*np.abs(position_adj_right['持仓调整'])).sum())
        
        #买卖交易能力
        position_adj_buy=position_adj[position_adj['持仓调整']>0]
        position_adj_sell=position_adj[position_adj['持仓调整']<0]
        power_buy.append(100-100*(position_adj_buy['close']*position_adj_buy['持仓调整']*np.abs(position_adj_buy['LR_power'])).sum()/(position_adj_buy['close']*position_adj_buy['持仓调整']).sum())
        power_sell.append(100-100*(position_adj_sell['close']*position_adj_sell['持仓调整']*np.abs(position_adj_sell['LR_power'])).sum()/(position_adj_sell['close']*position_adj_sell['持仓调整']).sum())
        amount_buy.append((position_adj_buy['close']*position_adj_buy['持仓调整']).sum())
        amount_sell.append((-position_adj_sell['close']*position_adj_sell['持仓调整']).sum())
    BSpreference=pd.DataFrame([buy_left,sell_left,buy_right,sell_right,power_left,power_right,power_buy,power_sell,
                               amount_buy_left,amount_sell_left,amount_buy_right,amount_sell_right],
            columns=stock_names,index=['左侧买入能力','左侧卖出能力','右侧买入能力','右侧卖出能力','左侧交易能力','右侧交易能力',
                            '买入交易能力','卖出交易能力','左侧买入金额','左侧卖出金额','右侧买入金额','右侧卖出金额']).T
    return BSpreference


# BSpreference_fig：作图
# stock_sel：list，要作图的股票代码
# plt_start_date：作图的起始日期
# port_name：图片标题前缀
# path_folder：导出文件夹路径
def BSpreference_fig(order,stock_position_port,data_all,stock_sel,plt_start_date,port_name='交易情况',
                     path_folder='D:/working_files/large_file/'):
    stocks=list(set(stock_position_port['windcode']))
    stock_names=[]
    buy_left=[]
    sell_left=[]
    buy_right=[]
    sell_right=[]
    power_left=[]
    power_right=[]
    power_buy=[]
    amount_buy=[]
    power_sell=[]
    amount_sell=[]
    amount_left=[]
    amount_right=[]
    amount_buy_left=[]
    amount_sell_left=[]
    amount_buy_right=[]
    amount_sell_right=[]
    for stock in stock_sel:
        stock_position_port_stock=stock_position_port[stock_position_port['windcode']==stock]        
        position_adj=pd.DataFrame(stock_position_port_stock['trade'].replace(0,np.nan))
        position_adj.columns=['持仓调整']
        position_adj.index=stock_position_port_stock['backdate'].values
        position_adj=position_adj.dropna()
        if len(position_adj.index)==0:
            continue
        stock_code=stock
        data0=data_all[data_all['windcode']==stock_code]#[['S_DQ_ADJCLOSE']]
        data=pd.DataFrame(data0['S_DQ_ADJCLOSE'].values,index=data0['backdate'].values,columns=[stock])
        data=data.sort_index()
        #else:
        #    data=get_close([stock_code],"2020-01-01","2023-08-16")
        data=data.dropna()
        start_date=stock_position_port_stock['backdate'].min()
        if data.index[0]>start_date-datetime.timedelta(days=180):
            continue
        start_date=(data.index).min()
        end_date=(data.index).max()
        data_ind=[]
        for i in range((end_date - start_date).days + 1):
            data_ind.append(start_date + datetime.timedelta(days=i))
        
        data_full=pd.DataFrame(data,index=data_ind).fillna(method='ffill')
        position_adj['close']=data_full.loc[position_adj.index,data_full.columns[0]]
        array=data.iloc[:,0].values
        extres_min,extres_max=get_extre(array,order)
        extres=np.append(extres_min,extres_max)
        position_adj_buy=position_adj[position_adj['持仓调整']>0]
        position_adj_sell=position_adj[position_adj['持仓调整']<0]
        
        skip_num=len(data[data.index<plt_start_date].index)
        extres_min=extres_min-skip_num
        extres_min=extres_min[extres_min>=0]
        extres_max=extres_max-skip_num
        extres_max=extres_max[extres_max>=0]
        data=data[data.index>=plt_start_date]
        
        s=20
        fig = plt.figure()
        fig.set_size_inches(20, 12)
        ax1 = plt.gca()
        ax1.scatter(list(data.iloc[extres_max,0].index),list(data.iloc[extres_max,0].values),s=100,marker='o',c='#FAEBD7',edgecolor='r')
        ax1.scatter(list(data.iloc[extres_min,0].index),list(data.iloc[extres_min,0].values),s=100,marker='o',c='#FAEBD7',edgecolor='g')
        ax1.scatter(list(data.loc[list(position_adj_buy.index),data.columns[0]].index),list(data.loc[list(position_adj_buy.index),data.columns[0]].values),c='r',s=60,marker='^')
        ax1.scatter(list(data.loc[list(position_adj_sell.index),data.columns[0]].index),list(data.loc[list(position_adj_sell.index),data.columns[0]].values),c='g',s=60,marker='v')
        plt.xlabel("时间",fontsize=s)
        plt.ylabel("股价",fontsize=s)
        plt.xticks(fontsize=s)
        plt.yticks(fontsize=s)
        ax11=ax1.twinx()
        ax11.bar(list(data.loc[list(position_adj_buy.index),data.columns[0]].index),list(position_adj_buy['持仓调整']),width=0.5,color='r')
        ax11.bar(list(data.loc[list(position_adj_sell.index),data.columns[0]].index),list(-position_adj_sell['持仓调整']),width=0.5,color='g')
        plt.xticks(fontsize=s)
        plt.yticks(fontsize=s)
        plt.ylabel("买入/卖出数量",fontsize=s)
        plt.title(port_name.split('-')[-1]+'-'+stock,fontsize=s+5)
        ax1.plot(data)
        plt.savefig(path_folder+port_name.split('-')[-1]+'-'+stock+'.png',dpi=600)


if __name__ == '__main__':
    df_A = pd.read_csv('石化投资组合股票交易数据_240603_璞泰来测试数据.csv')  # 如果B表是CSV文件
    df_B = pd.read_csv('财汇股票行情数据_240603_璞泰来测试数据.csv')  # 如果A表是CSV文件

    df_A = df_A[['STOCK_CODE', 'CJSL', 'BCRQ']]

    df_A.rename(columns={'STOCK_CODE': 'windcode', 'CJSL': 'trade', 'BCRQ': 'backdate'}, inplace=True)
    df_B.rename(columns={'SYMBOL': 'windcode', 'TCLOSE': 'S_DQ_ADJCLOSE', 'TRADEDATE': 'backdate'}, inplace=True)

    df_A['backdate'] = pd.to_datetime(df_A['backdate'].astype(str), format='%Y%m%d')
    df_B['backdate'] = pd.to_datetime(df_B['backdate'].astype(str), format='%Y%m%d')

    Cal_BSpreferences = Cal_BSpreference(30, df_A, df_B)

    print(Cal_BSpreferences)

    Cal_BSpreferences.to_csv('璞泰来_result.csv')
    # Cal_BSpreference：计算组合交易能力
    # 输入：
    # order：计算极致左右比较范围，单边
    # stock_position_port：换手情况，包括3列：windcode：股票代码；trade：交易量（股数）；backdate：datetime格式，交易日期
    # data_all：股票价格时间序列，建议至少包含stock_position_port日期范围并左右超出至少order个交易日，包括3列：windcode；S_DQ_ADJCLOSE；backdate
    # ignore_edge_trading：忽略未被划分在极值点之间边缘位置的交易，建议为True，否则可能出现该处交易能力打分不准确的情况
    # 输出：DataFrame，列出每个个股的交易能力和金额统计
    # def Cal_BSpreference(order, stock_position_port, data_all, ignore_edge_trading=True):















