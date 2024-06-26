# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/11/22 11:03 
# @Author    : Wangyd5 
# @File      : fund_field
# @Project   : sublicai
# @Function  ：
# --------------------------------


from sqlalchemy import Column, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import VARCHAR, Numeric,String,Integer,CLOB
from sublicai.tools.date_util import get_cur_time, get_cur_date
from sublicai.tools.generate_id import generate_id

Base = declarative_base()



class FundBasicInfo(Base):
    """
    研究所基金产品指标，根据code取到最新数据
    """
    __tablename__ = 'fund_basic_info'
    __table_args__ = (Index('sim_indicator_sign_fund_type_2', "sign", "fund_type_2", ),
                      Index('sim_indicator_sign_code', "sign", "fund_code", ), {'comment': '基金基本信息原始表'},)
    id = Column(String(32), default=generate_id, primary_key=True)
    fund_code = Column(VARCHAR(20), nullable=True, comment="基金代码")
    fund_name = Column(VARCHAR(40), nullable=True, comment="基金名称")
    setup_date = Column(VARCHAR(8), nullable=True, comment="成立日期")
    setup_trade_date = Column(VARCHAR(8), nullable=True, comment="成立日交易日日期")
    nav_accumulated = Column(Numeric(20, 4), nullable=True, comment="累计净值")
    nav_unit = Column(Numeric(20, 4), nullable=True, comment="单位净值")
    nav_ratio = Column(Numeric(20, 4), nullable=True, comment="增长率")
    change_date = Column(VARCHAR(8), nullable=True, comment="变动日期")
    manager = Column(VARCHAR(40), nullable=True, comment="基金经理")
    manager_id = Column(VARCHAR(40), nullable=True, comment="基金经理id")
    manager_all = Column(VARCHAR(128), nullable=True, comment="基金经理，所有的")
    manager_id_all = Column(VARCHAR(128), nullable=True, comment="基金经理id，所有的")
    company_name = Column(VARCHAR(128), nullable=True, comment="基金公司名称")
    company_id = Column(VARCHAR(128), nullable=True, comment="基金公司id")
    fund_type = Column(VARCHAR(20), nullable=True, comment="产品类型")
    fund_type_name = Column(VARCHAR(40), nullable=True, comment="产品类型名称")
    fund_type_2 = Column(VARCHAR(20), nullable=True, comment="产品类型，二级分类")
    fund_type_2_name = Column(VARCHAR(40), nullable=True, comment="产品类型名称，二级分类")
    fund_asset = Column(Numeric(35, 4), nullable=True, comment="基金规模")
    fund_asset_date = Column(VARCHAR(8), nullable=True, comment="基金规模日期")
    manager_practice_days_average = Column(Numeric(35, 4), nullable=True, comment="基金经理平均从业天数")
    manager_fund_num = Column(Numeric(35, 4), nullable=True, comment="基金经理管理产品总数")
    manager_fund_asset = Column(Numeric(35, 4), nullable=True, comment="基金经理管理总规模")
    institution_ratio = Column(Numeric(20, 4), nullable=True, comment="机构持仓比例")
    personal_ratio = Column(Numeric(20, 4), nullable=True, comment="个人比例")
    manager_ratio = Column(Numeric(20, 4), nullable=True, comment="管理人持仓比例")
    feeder_ratio = Column(Numeric(20, 4), nullable=True, comment="联接基金 持仓比例")
    benchmark_description = Column(VARCHAR(2000), nullable=True, comment="基准描述")
    invest_scope = Column(VARCHAR(2000), comment='投资范围')
    invest_object = Column(VARCHAR(2000), comment='投资目标')
    default_stock_bond_type = Column(VARCHAR(10), comment='基金股票/债券分类')
    default_stock_bond_index = Column(VARCHAR(10), comment='基于基金股票或债券型默认指数, 用于默认表征指数的选择')
    main_manager_id = Column(VARCHAR(100), comment='第一顺位基金经理ID')
    main_manager_name = Column(VARCHAR(10), comment='第一顺位基金经理姓名')
    main_manager_start_date = Column(VARCHAR(10), comment='第一顺位基金经理任职时间')
    is_initial = Column(Integer, comment='是否是主份额基金')
    cal_date = Column(VARCHAR(8), default=get_cur_date, comment="计算日期")
    update_time = Column(VARCHAR(20), default=get_cur_time, comment="更新时间")
    sign = Column(Integer, nullable=True, default=2, comment="最新标志,1表示最新，0表示旧")