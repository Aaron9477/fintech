# -*- coding: utf-8 -*-
"""
    获取不同公司的assetname集合
"""
import pandas as pd
import numpy as np
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_file', type=str, help='input_file', default='../../data/金融产品资产配置_22年三季报_221222.csv')
    args = parser.parse_args()
    input_file = args.input_file

    df = pd.read_csv(input_file)
    df = df[["AgentName", "AssetName"]]

    grouped = df.groupby('AgentName')
    grouped = grouped['AssetName'].nunique()
    print(grouped)


