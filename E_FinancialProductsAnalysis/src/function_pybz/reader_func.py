



def get_raw_files(statistics_date):
    if statistics_date == '2022-09-30':
        all_data_file = '../../data_pybz/pyjy_bank_wealth_product_0930.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_22年三季报_230314.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_22年三季报_230314.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_22年三季报_230314.csv'
        series_name_file = '../../data_pybz/out5.xlsx'
    elif statistics_date == '2022-12-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0424.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_22年四季报_230503.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_22年四季报_230503.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_22年四季报_230503.csv'
        series_name_file = '../../data_pybz/out5-22q4.xlsx'
    elif statistics_date == '2023-03-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_23年Q1_230515.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_23年Q1_230515.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_23年Q1_230515.csv'
        series_name_file = '../../data_pybz/out5-23q1.xlsx'
    else:
        raise ValueError

    return all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file

