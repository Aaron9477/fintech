# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2023/7/11 11:37 
# @Author    : Wangyd5 
# @File      : cal_asset_portfolio_and_top10
# @Project   : licai
# @Function  ：计算资产配置表和前十大持仓 入库
# --------------------------------

from database.read.read_py_base import PyReader
from database.saver.licai_saver import ResDataSaver


if __name__ == '__main__':
    reader = PyReader()
    saver = ResDataSaver()
    data = reader.get_pk_asset_portfolio()

    top_10 = reader.get_pk_top_10()

    # saver.save_asset_portfolio(data)
    # saver.save_top10(top_10)

    data.to_csv(r'M:\Device\C\Users\csc23998\sublicai\licai\docs\pk_asset.csv',index=False)
    top_10.to_csv(r'M:\Device\C\Users\csc23998\sublicai\licai\docs\pk_top10.csv',index=False)

