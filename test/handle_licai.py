

import pandas as pd

reflact_dict = {'日开': '日开', '2-14天 周开为主': '周开/半月开', '15-32天 月开为主': '月开', '33-186天 半年开为主': '季开/半年开',
                '187-370天 年开为主': '年开', '371-800天 两年开为主': '一年半开/两年开', '>800天': '两年开以上'}
company_list = []

all_guimo = pd.read_csv('理财公司总规模清单.csv')

all_guimo_dict = {}

for index, row in all_guimo.iterrows():
    all_guimo_dict[row['AgentName']] = int(row['Unnamed: 1'])
    company_list.append(row['AgentName'])


output_col = ['日开', '周开/半月开', '月开', '季开/半年开', '年开', '一年半开/两年开', '两年开以上', '和']
res = pd.DataFrame(data=0.0,index=company_list,columns=output_col)

type_guimo = pd.read_csv('理财公司分公司分类型规模清单.csv')
for index, row in type_guimo.iterrows():
    if row['MinInvestTimeType'] != '数据缺失':
        res[reflact_dict[row['MinInvestTimeType']]][row['AgentName']] = float(row['Unnamed: 2'])

for index, row in res.iterrows():
    row['和'] = row.sum()

res = res.apply(lambda x:x/x['和'], axis=1)

print(res)
res.to_excel('res_ratio2.xlsx')


#     print(row)
#     all_guimo_dict[row['AgentName']] = int(row['Unnamed: 2'])
# print(all_guimo_dictt)




# print(res)
