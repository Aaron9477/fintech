################ 本项目目的为银行理财代销图鉴相关依赖表生成
（1）data_process_codes下包含数据清洗相关的一些代码，以main开头的可独自运行，其余的会由其他代码调用；
（2）output_dir下的文件为代码输出文件，为各个依赖sheet，生成后后续将复制到图鉴的各个依赖表中，根据文件名和图鉴中的sheet名字可以对应应该如何复制，注意部分表复制时并没有用到所有列；
（3）raw_datas下的文件为原始数据，一部分需要由数据库导出，一部分由data_process_codes下由“main”开头的文件生成，更具体的说明在下面的目录树后面有；
（4）result_process_codes下的文件为各个依赖表生成的代码。
（5）main.ipynb中调用了相关函数生成依赖表并将结果保存至output_dir。
以下为文件夹的目录树：
ROOT
│  .env
│  launch.json
│  main.ipynb
│  main.py
│  readme.txt
│  tree.txt
│  银行理财代销图鉴v1.1.5.xlsx
│  
├─.vscode
│      settings.json
│      
├─data_process_codes
│  │  fillna_within_n.py
│  │  get_processed_nv_datas.py
│  │  main_first_累计净值填充.py
│  │  main_xianjinguanli_df9result.py
│  │  main_周度加权平均净值处理（df7）.py
│  │  merge2cols_ues_col2_if_col1_empty.py
│  │  preprocess.py
│  │  sectorize.py
│  │  sort_by_frequency_return_top_n_join_with_sign.py
│  │  WeeklyYield_to_nv.py
│  │  WeeklyYield_to_rangereturn.py
│  │  WeeklyYield_to_rangereturn_to_annulized.py
│  │  weighted_avg.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          fillna_within_n.cpython-39.pyc
│          merge2cols_ues_col2_if_col1_empty.cpython-39.pyc
│          preprocess.cpython-39.pyc
│          sectorize.cpython-39.pyc
│          sort_by_frequency_return_top_n_join_with_sign.cpython-39.pyc
│          WeeklyYield_to_nv.cpython-39.pyc
│          WeeklyYield_to_rangereturn.cpython-39.pyc
│          WeeklyYield_to_rangereturn_to_annulized.cpython-39.pyc
│          weighted_avg.cpython-39.pyc
│          __init__.cpython-39.pyc
│          
├─output_dir
│      底层数据_产品甄选_代销机构.xlsx
│      底层数据_产品甄选_代销机构_板块.xlsx
│      底层数据_产品甄选_代销机构_近一年.xlsx
│      底层数据_产品甄选_代销机构_近三月.xlsx
│      底层数据_产品甄选_代销机构_近半年.xlsx
│      底层数据_产品甄选_理财公司.xlsx
│      底层数据_产品甄选_理财公司_板块.xlsx
│      底层数据_产品甄选_理财公司_近一年.xlsx
│      底层数据_产品甄选_理财公司_近三月.xlsx
│      底层数据_产品甄选_理财公司_近半年.xlsx
│      底层数据_产品费率.xlsx
│      底层数据_产品费率_板块.xlsx
│      底层数据_代销产品概况_代销机构.xlsx
│      底层数据_代销产品概况_代销机构_板块.xlsx
│      底层数据_代销产品概况_代销机构_绘图.xlsx
│      底层数据_代销产品概况_代销机构_绘图_板块.xlsx
│      底层数据_代销产品概况_理财公司.xlsx
│      底层数据_代销产品概况_理财公司_板块.xlsx
│      底层数据_代销产品概况_理财公司_绘图.xlsx
│      底层数据_代销产品概况_理财公司_绘图_板块.xlsx
│      底层数据_代销产品货架_代销机构.xlsx
│      底层数据_代销产品货架_理财公司.xlsx
│      底层数据_代销产品货架_理财公司_板块.xlsx
│      底层数据_代销机构基本信息.xlsx
│      底层数据_公告分析_代销机构.xlsx
│      底层数据_公告分析_理财公司.xlsx
│      底层数据_净值指标_代销机构.xlsx
│      底层数据_净值指标_理财公司.xlsx
│      底层数据_合作产品.xlsx
│      底层数据_合作产品_板块.xlsx
│      底层数据_固定收益类货架_代销机构.xlsx
│      底层数据_固定收益类货架_代销机构_板块.xlsx
│      底层数据_固定收益类货架_理财公司.xlsx
│      底层数据_固定收益类货架_理财公司_板块.xlsx
│      底层数据_现金管理类产品七日年化收益率作图.xlsx
│      底层数据_现金管理类产品分析.xlsx
│      底层数据_理财公司基本信息.xlsx
│      底底层数据_代销产品货架_代销机构_板块.xlsx
│      
├─raw_datas
│      all_nv_data_new.csv #这个文件是由main_first_累计净值填充.py+py_all_net_value_****.csv生成，对净值数据进行了填充等清洗工作。
│      py_all_net_value_0704.csv #这个文件是数据库导出的净值数据
│      wind_bank_info_230628.csv #这个文件是由万得导出的银行信息数据
│      代销数据0526.xlsx #这个文件是数据库导出的代销关系数据
│      周度净值_均值处理_未筛选存续期.xlsx #这个文件是由main_周度加权平均净值处理（df7）.py生成，对母子产品的净值进行了加权处理
│      周度日期20220101-20230630.xlsx #这个文件中存储了每周最后一个交易日
│      基础数据.xlsx #这个文件是各个产品的数据
│      现金管理类_七日年化.xlsx #这个文件由main_xianjinguanli_df9result.py生成
│      
└─result_process_codes
    │  cash_product_info.py
    │  daixiao_comp_basic_info.py
    │  daixiao_comp_daixiaoproduct_info.py
    │  daixiao_comp_fixed_shalves.py
    │  daixiao_comp_gonggao_analysis.py
    │  daixiao_comp_netvalue_analysis.py
    │  daixiao_comp_product_recommendation.py
    │  daixiao_comp_product_shelves_info.py
    │  hezuoproduct_num.py
    │  licai_comp_basic_info.py
    │  licai_comp_daixiaoproduct_info.py
    │  licai_comp_fixed_shalves.py
    │  licai_comp_gonggao_analysis.py
    │  licai_comp_netvalue_analysis.py
    │  licai_comp_product_recommendation.py
    │  licai_comp_product_shelves_info.py
    │  netvalue_analysis_paint.py
    │  product_fees.py
    │  
    └─__pycache__
            cash_product_info.cpython-39.pyc
            daixiao_comp_basic_info.cpython-39.pyc
            daixiao_comp_daixiaoproduct_info.cpython-39.pyc
            daixiao_comp_fixed_shalves.cpython-39.pyc
            daixiao_comp_gonggao_analysis.cpython-39.pyc
            daixiao_comp_netvalue_analysis.cpython-39.pyc
            daixiao_comp_product_recommendation.cpython-39.pyc
            daixiao_comp_product_shelves_info.cpython-39.pyc
            hezuoproduct_num.cpython-39.pyc
            licai_comp_basic_info.cpython-39.pyc
            licai_comp_daixiaoproduct_info.cpython-39.pyc
            licai_comp_fixed_shalves.cpython-39.pyc
            licai_comp_gonggao_analysis.cpython-39.pyc
            licai_comp_netvalue_analysis.cpython-39.pyc
            licai_comp_product_recommendation.cpython-39.pyc
            licai_comp_product_shelves_info.cpython-39.pyc
            product_fees.cpython-39.pyc
