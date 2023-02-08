# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import pandas as pd
import numpy as np
import datetime
import time
import os
import fnmatch
path = os.getcwd()

def choose_report(input_df):
    # 按 2022中报、2022二季报 的顺序，选取一份报告做后续处理
    if len(input_df[(input_df['InfoSource'] == '2022中报')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '2022中报')]
    elif len(input_df[(input_df['InfoSource'] == '2022二季报')]) > 0:
        input_df = input_df[(input_df['InfoSource'] == '2022二季报')]

    return input_df


bank_wealth_product = pd.read_csv(os.path.join(path, '../../data/bank_wealth_product_12_11.csv'))
bank_wealth_product = bank_wealth_product[pd.notnull(bank_wealth_product['FinProCode'])]

bank_wealth_product =bank_wealth_product [pd.notnull(bank_wealth_product ['InvestmentType'])]
top10 = pd.read_csv(os.path.join(path, '../../data/资产明细_221216.csv'))
top10['Secu_new']=top10['SecuName'].apply(lambda x:'现金及存款' if fnmatch.fnmatch(str(x),'*存款*') else str(x))
top10['Secu_new']=top10['Secu_new'].apply(lambda x:'现金及存款' if fnmatch.fnmatch(str(x),'*现金*') else str(x))
top10['Secu_new']=top10['Secu_new'].apply(lambda x:'现金及存款' if fnmatch.fnmatch(str(x),'*存放同业*') else str(x))
top10['Secu_new']=top10['Secu_new'].apply(lambda x:'逆回购' if fnmatch.fnmatch(str(x),'*逆回购*') else str(x))
top10=top10[pd.notnull(top10['FinProCode'])]
top10=top10[pd.notnull(top10['AgentName'])]

bank_wealth_product['FinProCode']=bank_wealth_product['FinProCode'].astype(str)
top10['FinProCode']=top10['FinProCode'].astype(str)
del top10['InvestmentType']
data_all=pd.merge(bank_wealth_product,top10,how='right',on='FinProCode')
data_all=choose_report(data_all)

data_all=data_all.loc[:,['CompanyName','InvestmentType','MarketValue','Secu_new']]
res1=data_all.groupby(['CompanyName','InvestmentType','Secu_new']).sum()
res1['rank']=  res1.groupby(['CompanyName','InvestmentType']).rank(ascending=False)
res1=res1.reset_index()
res1=res1.sort_values(['rank'],ascending=False).sort_values(['CompanyName','InvestmentType'])
res1=res1.loc[res1['rank'] <= 10]

data_all=data_all.loc[:,['CompanyName','MarketValue','Secu_new']]
res2=data_all.groupby(['CompanyName','Secu_new']).sum()
res2['rank']=  res2.groupby(['CompanyName']).rank(ascending=False)
res2=res2.reset_index()
res2=res2.sort_values(['rank'],ascending=False).sort_values(['CompanyName'])
res2=res2.loc[res2['rank'] <= 10]

with pd.ExcelWriter('./output_all.xlsx') as writer:
    res1.to_excel(writer, sheet_name="sheet1" , index=False)
    res2.to_excel(writer, sheet_name="sheet2" , index=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
