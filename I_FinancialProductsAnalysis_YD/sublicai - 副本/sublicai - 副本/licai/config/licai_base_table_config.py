# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/3/24 15:32 
# @Author    : Wangyd5 
# @File      : delete_update_product_info_config
# @Project   : sublicai
# @Function  ：修改基础信息表的配置
# --------------------------------

import os


class LicaiBaseTable:
    # 基础表命名
    table_product_info_py = 'py_bank_wealth_product_1231_0518' + '.csv'
    table_product_info_jy = 'jy_bank_wealth_product_1231_0518' + '.csv'
    table_net_value_py = 'py_all_net_value_0704' + '.csv'
    table_net_value_jy = 'all_net_value_05_18' + '.csv'

    # 衍生表命名
    sub_table_product_info_base_merge = 'bank_wealth_product_base_pyjy_0529'+'.csv'

    # 生成表命名
    sub_table_product_info_py = 'bank_wealth_product_py'+'.csv'
    sub_table_product_info_jy = 'bank_wealth_product_jy'+'.csv'


def delete_upate_sub_table():
    base_path = 'D:\\institution\\sublicai\\docs\\'
    path_1 = os.path.join(base_path,LicaiBaseTable.sub_table_product_info_py)
    path_2 = os.path.join(base_path,LicaiBaseTable.sub_table_product_info_jy)
    path_3 = os.path.join(base_path,LicaiBaseTable.sub_table_product_info_base_merge)


    for path in [path_1,path_2,path_3]:
        if os.path.exists(path):
            os.remove(path)
            print(f'{path}已经删除...')
        else:
            print('已经删除完毕......')


if __name__ == '__main__':
    delete_upate_sub_table()