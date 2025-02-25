


def get_raw_files_jy(statistics_date):
    if statistics_date == '2023-03-31':
        all_data_file = '../../data_pybz/jy_理财产品要素数据-聚源.csv'
        jy_raw_asset_file = '../../data_pybz/jy_金融产品资产配置_23年一季报_230626.csv'
        jy_top10_file = '../../data_pybz/jy_前十大持仓_23年一季报_230626.csv'
    elif statistics_date == '2023-06-30':
        all_data_file = '../../data_pybz/jy_理财产品要素数据-聚源_0630_230906.csv'
        jy_raw_asset_file = '../../data_pybz/jy_金融产品资产配置_23年二季报_230906.csv'
        jy_top10_file = '../../data_pybz/jy_前十大持仓_23年二季报_230906.csv'
    else:
        raise ValueError

    return all_data_file, jy_raw_asset_file, jy_top10_file


def get_raw_files(statistics_date):
    if statistics_date == '2022-06-30':
        # 此处bank表用最新的，只有规模是不正确的
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_22年二季报_230515.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_22年二季报_230515.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_22年二季报_230515.csv'
        series_name_file = '../../data_pybz/out5-23q2.xlsx'
    elif statistics_date == '2022-09-30':
        all_data_file = '../../data_pybz/pyjy_bank_wealth_product_0930.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_22年三季报_230515.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_22年三季报_230515.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_22年三季报_230515.csv'
        series_name_file = '../../data_pybz/out5.xlsx'
    elif statistics_date == '2022-12-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_1231.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_22年四季报_230529.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_22年四季报_230529.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_22年四季报_230529.csv'
        series_name_file = '../../data_pybz/out5-22q4.xlsx'
    elif statistics_date == '2023-03-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0331.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_23年Q1_230620.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_23年Q1_230620.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_23年Q1_230620.csv'
        series_name_file = '../../data_pybz/out5-23q1.xlsx'
    elif statistics_date == '2023-06-30':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0630.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_23年Q2_230928.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_23年Q2_230928.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_23年Q2_230928.csv'
        series_name_file = '../../data_pybz/out5-23q1.xlsx'
    elif statistics_date == '2023-09-30':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_0930.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_23年Q3_231110.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_23年Q3_231110.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_23年Q3_231110.csv'
        series_name_file = '../../data_pybz/out5-23q1.xlsx'
    elif statistics_date == '2023-12-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_23Q4_240516.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_24年Q4_240516.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_24年Q4_240516.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_24年Q4_240516.csv'
        series_name_file = '../../data_pybz/out5-23q1.xlsx'
    elif statistics_date == '2024-03-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_240331_240514.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_24年Q1_240513.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_24年Q1_240513.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_24年Q1_240513.csv'
        series_name_file = '../../data_pybz/out5-24q1.xlsx'
    elif statistics_date == '2024-06-30':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_24Q2_240923.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_24年Q2_240923.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_24年Q2_240923.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_24年Q2_240923.csv'
        series_name_file = '../../data_pybz/out5-24q1.xlsx'
    elif statistics_date == '2024-09-30':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_24Q3_241108.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_24年Q3_241107.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_24年Q3_241107.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_24年Q3_241107.csv'
        series_name_file = '../../data_pybz/out5-24q3.xlsx'
    elif statistics_date == '2024-12-31':
        all_data_file = '../../data_pybz/bank_wealth_product_base_pyjy_24Q4_250212.csv'
        raw_asset_file = '../../data_pybz/pybz_金融产品资产配置_24年Q4_250219.csv'
        top10_file = '../../data_pybz/pybz_金融产品前十名持仓_24年Q4_250219.csv'
        non_standard_file = '../../data_pybz/pybz_非标准化债权及股权类资产表_24年Q4_250219.csv'
        # todo: 此处未更新
        series_name_file = '../../data_pybz/out5-24q3.xlsx'
    else:
        raise ValueError

    return all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file


def get_raw_filesV2(statistics_date):
    if statistics_date == '2024-06-30':
        all_data_file = '../../../data_pybz/bank_wealth_product_base_pyjy_24Q2_240923.csv'
        raw_asset_file = '../../../data_pybz/pybz_金融产品资产配置_24年Q2_240923.csv'
        top10_file = '../../../data_pybz/pybz_金融产品前十名持仓_24年Q2_240923.csv'
        non_standard_file = '../../../data_pybz/pybz_非标准化债权及股权类资产表_24年Q2_240923.csv'
        series_name_file = '../../../data_pybz/out5-24q1.xlsx'
    else:
        raise ValueError

    return all_data_file, raw_asset_file, top10_file, non_standard_file, series_name_file


def get_intermediate_files(statistics_date):
    if statistics_date == '2022-09-30':
        fixed_income_file = '../../22年Q3/固收增强分类结果.xlsx'
    elif statistics_date == '2022-12-31':
        fixed_income_file = '../../22年Q4/固收增强分类结果.xlsx'
    elif statistics_date == '2023-03-31':
        fixed_income_file = '../../23年Q1/固收增强分类结果.xlsx'
    elif statistics_date == '2023-06-30':
        fixed_income_file = '../../23年Q1/固收增强分类结果.xlsx'
    elif statistics_date == '2023-09-30':
        fixed_income_file = '../../23年Q1/固收增强分类结果.xlsx'
    else:
        raise ValueError

    b = None

    return fixed_income_file, b