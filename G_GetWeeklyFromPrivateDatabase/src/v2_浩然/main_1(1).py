# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import pandas as pd
import numpy as np
import sqlite3
import datetime
import time
import sys
import argparse


def get_fund_list(conn, cursor, name):
    sql = f"select fund_name from fund_base_info where category='{name}'"
    fund_list = pd.read_sql(sql, conn)
    conn.commit()
    return fund_list

#新加的，提取基金全部信息
def get_fund_all(conn, cursor, name):
    sql = f"select fund_name, category, administrator, region, manager, establish_time from fund_base_info where category='{name}'"
    fund_all = pd.read_sql(sql, conn)
    conn.commit()
    return fund_all

def get_specific_fund_data(conn, cursor, name):
    sql = f"select nval_date,nval from fund_nval where fund_name ='{name}'"
    fund_data = pd.read_sql(sql, conn)
    conn.commit()
    return fund_data

"""
本周
"""
def this_week(df, date):
    if df.iat[df.index[-1], 0]== date:
        return df['fhjz'].tail(1).iat[0]
    else:
        return float('nan')

"""
成立以来
"""
def since_establish(df, date):
    if df.iat[df.index[-1], 0]== date:
        return df['nval'].tail(1).iat[0] / df['nval'].head(1).iat[0] - 1
    else:
        return float('nan')

"""
年利率
"""
def yield_of_year(group, year):
    try:
       latter = group.get_group(f'{year}').tail(1)
       ht = group.tail(1)
       if latter.values[0] != ht.values[0]:
           former = group.get_group(f'{year-1}').tail(1)
       else:
           former = group.get_group(f'{year}').head(1)

       yearyield=(latter.values[0] / former.values[0]) - 1
       return yearyield

    except KeyError as e:
        return float('nan')

"""
是否创新高
"""
def if_highest(df, date):
    if df.iat[df.index[-1], 0] != date:
        return "nan"
    elif (df['nval'].tail(1).iat[0] == df['nval'].max()):
        return 1
    else:
        return 0


"""
未创新高天数
"""
def days_without_record_high(df, date):
    maxindex = df['nval'].idxmax()
#    curindex= df.index[-1]
    maxday = df.iat[maxindex,0]
#    curday = df.iat[curindex,0]
    return (date-maxday).days

"""
近x月
"""
def recent_months(df, mon, date):
    if df.iat[df.index[-1], 0] != date:
        return float('nan')
    else:
        latest = df.index[-1]
        lagged_theoretical = df.iat[latest, 0] - pd.DateOffset(months=mon)
        td = (abs(df['nval_date'] - lagged_theoretical))
        idx = np.where(td == td.min())[0][0]
        return df.iat[latest, 1]/df.iat[idx, 1]-1

"""
近x年
"""
def recent_years(df, year, date):
    if df.iat[df.index[-1], 0] != date:
        return float('nan')
    else:
        latest = df.index[-1]
        lagged_theoretical = df.iat[latest, 0] - pd.DateOffset(years=year)
        td = (abs(df['nval_date'] - lagged_theoretical))
        idx = np.where(td == td.min())[0][0]
        return df.iat[latest, 1]/df.iat[idx, 1]-1

"""
年化收益率
"""
def annualized_return(df, date):
    if df.iat[df.index[-1], 0] != date:
        return float('nan')
    else:
        latest = df.index[-1]
        first = df.index[0]
        dvalues = (df.iat[latest, 0] - df.iat[first, 0]).days
        x = df.iat[latest, 1] / df.iat[first, 1]
        y = math.pow(x, 365/dvalues)-1
        return y

"""
过去一年最大回撤
"""
def last_year_max_drawdown(df, date):

        #latest = df.index[-1]
        lagged_theoretical = date - pd.DateOffset(years=1)
        td = (abs(df['nval_date'] - lagged_theoretical))
        idx = np.where(td == td.min())[0][0]
        if (date-df['nval_date'][idx]).days<370:
            return df['hc'][idx:].min()
        else:
            return 0

"""
下行标准差
"""
def downside_std(df):
    ss = df['fhjz'][1:]
    ss = ss.where(ss < 0, 0)
    dstd=np.sqrt(((ss**2).sum())/(ss.size-1))
    return dstd

"""
周胜率
"""
def weekly_winning_rate(df):
    total = df['fhjz']
    df_ok = len(total[total > 0])
    return df_ok/(total.size-1)

'''pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 1000)'''

if __name__ == '__main__':

    """
    最新日期
    """
    udate = '2022-9-30'
    update_date = pd.to_datetime(udate)
    print(update_date)

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--db_path', type=str, help='数据库路径', default='test2.db')
    #parser.add_argument('--cet_data_dict_path', type=str, help='CET基金详情文件位置', default='D:/中信建投/7_组内工具/CET/Data/nav_data_dic.csv')
    args = parser.parse_args()
    conn = sqlite3.connect(args.db_path)
    cursor = conn.cursor()

    #str1 = [ '指数增强']
    str1 = ['股票多头-多空', '指数增强', '市场中性', '管理期货', '宏观', '套利', '债券', '混合']
    #catogory=['2016年', '2017年', '2018年', '2019年', '2020年']
    with pd.ExcelWriter('./output_all.xlsx') as writer:
     for cat in str1 :
        res2 = pd.DataFrame(columns=['analysis index'], data=[ '2016年', '2017年', '2018年', '2019年', '2020年', \
                                                         '2021年', '今年以来', '成立以来', '本周', '是否创新高', \
                                                         '未创新高的天数', '近一月', '近三月', '近六月', '近一年', '近两年', \
                                                         '近三年', '年化收益率', '收益标准差', '年化波动率', '历史最大回撤', \
                                                         '过去一年最大回撤', '历史周度回撤', '下行标准差', '下行标准差年化', \
                                                         '周胜率', '风险调整后收益比率', '夏普比率（年化）', 'Sortino比率（年化）', \
                                                         'Calmar比率（历史最大回撤）'])
        res4 = pd.DataFrame()

    # fund_name_list=pd.read_excel(r'E:\中信数据\重点观察私募周报部分内容.xlsx', sheet_name='股票多头-多空', index_col=None)
    # fund_name_list=fund_name_list.iloc[0:1, :]
    # fund_name_list=fund_name_list.dropna(axis=1, how='any')
    # fund_name = fund_name_list.size-1

        category_name = cat
        fund_list = get_fund_list(conn, cursor, category_name)

        fund_num = len(fund_list.index)



        for count in range(fund_num):

          # fund_list.values[count, 0]
          # fund_name_list.values[0, 1 + count]
            fund_data = get_specific_fund_data(conn, cursor, fund_list.values[count, 0])
            if fund_data.empty:
                res2[fund_list.values[count, 0]] = float('nan')
                continue

            """添加 年份标签，方便后续计算"""
            fd_processed = pd.concat([fund_data, pd.DataFrame(columns=['year'])])
            for j in range(len(fd_processed.index)):
                fd_processed.iat[j, 2] = str(fd_processed.iat[j, 0])[:4]

            """统计 周度收益，方便后续计算"""
            fd_processed = pd.concat([fd_processed, pd.DataFrame(columns=['fhjz'])])
            j = 1
            while j < len(fd_processed.index):
                fd_processed.iat[j, 3] = fd_processed.iat[j, 1] / fd_processed.iat[j - 1, 1] - 1
                j += 1

            """统计 最大回撤，方便后续计算"""
            # fd_processed = pd.concat([fd_processed, pd.DataFrame(columns=['hc'])])
            fd_processed['hc'] = fd_processed.expanding(1)['nval'].max()
            fd_processed.iat[0, 4] = float('nan')

            fd_processed['hc'] = fd_processed['nval'] / fd_processed['hc'] - 1
            fd_processed_new = fd_processed
              # # 上一行另一种写法
              # i = 1
              # while i < len(fd_processed.index):
              #     fd_processed.iat[i, 4] = fd_processed.iat[i, 1] / fd_processed.iat[i, 4] - 1
              #     i += 1


            group = fd_processed['nval'].groupby(fd_processed['year'])

            fd_processed['nval_date'] = pd.to_datetime(fd_processed['nval_date'])

            res2[fund_list.values[count, 0]] = float('nan')

            for i in range(7):
                res2.iat[i, count + 1] = yield_of_year(group, 2016 + i)

            res2.iat[7, count + 1] = since_establish(fd_processed, update_date)
            res2.iat[8, count + 1] = this_week(fd_processed, update_date)
            res2.iat[9, count + 1] = if_highest(fd_processed, update_date)
            res2.iat[10, count + 1] = days_without_record_high(fd_processed, update_date)
            res2.iat[11, count + 1] = recent_months(fd_processed, 1, update_date)
            res2.iat[12, count + 1] = recent_months(fd_processed, 3, update_date)
            res2.iat[13, count + 1] = recent_months(fd_processed, 6, update_date)
            res2.iat[14, count + 1] = recent_years(fd_processed, 1, update_date)
            res2.iat[15, count + 1] = recent_years(fd_processed, 2, update_date)
            res2.iat[16, count + 1] = recent_years(fd_processed, 3, update_date)
            res2.iat[17, count + 1] = annualized_return(fd_processed, update_date)
            res2.iat[18, count + 1] = fd_processed['fhjz'].std()
            res2.iat[19, count + 1] = fd_processed['fhjz'].std() * math.sqrt(52)
            res2.iat[20, count + 1] = fd_processed['hc'].min()
            res2.iat[21, count + 1] = last_year_max_drawdown(fd_processed, update_date)
            res2.iat[22, count + 1] = fd_processed['fhjz'].min()
            res2.iat[23, count + 1] = downside_std(fd_processed)
            res2.iat[24, count + 1] = downside_std(fd_processed) * math.sqrt(52)
            res2.iat[25, count + 1] = weekly_winning_rate(fd_processed)
            res2.iat[27, count + 1] = (res2.iat[17, count + 1] - 0.015) / res2.iat[19, count + 1]
            res2.iat[28, count + 1] = (res2.iat[17, count + 1] - 0.015) / res2.iat[24, count + 1]
            res2.iat[29, count + 1] = - res2.iat[17, count + 1] / res2.iat[20, count + 1]

            fd_processed_new['year'] = fd_processed_new['year'].astype(int)
            #fd_processed_new['nval_date'].apply([lambda x: str(x)[:10]])
            fd_processed_new = fd_processed_new[fd_processed_new['year'] > 2016].set_index('nval_date')
            fd_processed_new = fd_processed_new[['nval', 'fhjz', 'hc']]
            fd_processed_new = fd_processed_new.rename(columns={'nval': '复权累计净值', 'fhjz': '周度收益率', 'hc': '最大回撤'})

            res4 = pd.concat([res4, fd_processed_new], axis=1).sort_index()

        fund_all = get_fund_all(conn, cursor, category_name)
        fund_all = fund_all.rename(
            columns={'category': '策略类型', 'administrator': '管理人', 'region': '地区', 'manager': '投资经理',
                     'establish_time': '成立时间'})
        for i in range(len(fund_all.index)):
            fund_all.iat[i, 5] = str(fund_all.iat[i, 5]).replace("-", "/", 2)
        res5 = fund_all.T
        res3 = pd.DataFrame()

        #### 添加了这里
        index_list = list(res4.index)
        res4.index = [x.strftime('%Y/%m/%d') for x in index_list]
        #####################

        #.replace("-", "/", 2)
        for count in range(fund_num):
            res3 = pd.concat([res3, res5.loc[:, count]], axis=1)
            res3 = pd.concat([res3, pd.DataFrame(columns=[count])], axis=1)
            res3 = pd.concat([res3, pd.DataFrame(columns=[count])], axis=1)


       # res4 = res4.reset_index()
       # res4['nval_date'].apply([lambda x:x.to_datetime.strftime('%Y/%m/%d')])
        res4 = res4.T
        res3 = res3.T
        res6 = pd.concat([res3.reset_index(drop=True), res4.reset_index()], axis=1)
        res6 = res6.reset_index(drop=True).T.reset_index()
        res6.iat[0, 0] = float('nan')
        res6.iat[6, 0] = float('nan')



        name = str(cat)
        res2.to_excel(writer, sheet_name=name, index=False)
        name = name+'new'
        ##建立res7单独处理指数增强
        if name == '指数增强new':
            res6 = res6.reset_index()
            res7 = pd.DataFrame()
            res7 = pd.concat([res7, res6.loc[:,'index']], axis = 1)
            for count in range(fund_num):
                count1 =  count*3
                res7 = pd.concat([res7, res6.loc[:, count1]], axis=1)
                res7 = pd.concat([res7, res6.loc[:, count1+1]], axis=1)
                res7 = pd.concat([res7, res6.loc[:, count1+2]], axis=1)
                for k in range(5):
                    res7 = pd.concat([res7, pd.DataFrame(columns=[str(count)+'加'+str(k)])], axis=1)
            for count in range(fund_num):
                res7.loc[6, str(count) + '加0'] = '标准化'
                res7.loc[6, str(count) + '加1'] = '超额收益（复利）'
                res7.loc[6, str(count) + '加2'] = '超额收益（单利）'
                res7.loc[6, str(count) + '加3'] = '周度超额收益率'
                res7.loc[6, str(count) + '加4'] = '超额最大回撤'
                res7.loc[0, str(count) + '加1'] = res7.loc[0, count*3]+'超额收益'
            res6 = res7
        res6.to_excel(writer, sheet_name=name, header=None, index=False, float_format="%.6f")



    cursor.close()
    conn.close()

#print(res2)
####res2.to_excel('output_list3.xlsx', index=False, sheet_name='Data1', float_format="%.6f")
#filepath=r'C:\output.xlsx'(filepath)
#with pd.ExcelWriter('./output_all.xlsx') as writer:
  #  res.to_excel(writer, sheet_name="sheet1" , index=False)
  #  res2.to_excel(writer, sheet_name="sheet2" , index=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
