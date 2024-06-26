# -*- coding=utf-8 -*-
# --------------------------------
# @Time      : 2022/11/22 11:03 
# @Author    : Wangyd5 
# @File      : fund_test_field
# @Project   : sublicai
# @Function  ：
# --------------------------------
from sqlalchemy import Column, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import VARCHAR, Numeric,String,Integer,CLOB
from sublicai.tools.date_util import get_cur_time, get_cur_date
from sublicai.tools.generate_id import generate_id

Base = declarative_base()

class FundProductScore(Base):
    """
    基金产品的评价打分,短中长三个周期的六种能力打分
    取数据时,按照manager_id筛选,sign=1取最新数据
    """
    __tablename__ = 'fund_product_score'
    id = Column(String(32), default=generate_id, primary_key=True)
    code = Column(VARCHAR(20), nullable=True, comment="基金代码")
    change_date = Column(VARCHAR(8), nullable=True, comment="变动日期")
    cal_date = Column(VARCHAR(8), default=get_cur_date, nullable=True, comment="计算日期")
    total_score_short_term = Column(Numeric(20, 4), nullable=True, comment="短期评分")
    return_score_short_term = Column(Numeric(20, 4), nullable=True, comment="短期盈利能力")
    return_score_short_rank = Column(VARCHAR(20), nullable=True, comment="短期盈利能力_同类排名")
    selection_score_short_term = Column(Numeric(20, 4), nullable=True, comment="短期选股能力")
    selection_score_short_rank = Column(VARCHAR(20), nullable=True, comment="短期选股能力_同类排名")
    timing_score_short_term = Column(Numeric(20, 4), nullable=True, comment="短期择时能力")
    timing_score_short_rank = Column(VARCHAR(20), nullable=True, comment="短期择时能力_同类排名")
    experience_score_short_term = Column(Numeric(20, 4), nullable=True, comment="短期经验值")
    experience_score_short_rank = Column(VARCHAR(20), nullable=True, comment="短期经验值_同类排名")
    max_drawdown_score_short_term = Column(Numeric(20, 4), nullable=True, comment="短期抗风险力")
    max_drawdown_score_short_rank = Column(VARCHAR(20), nullable=True, comment="短期抗风险力_同类排名")
    sharpe_score_short_term = Column(Numeric(20, 4), nullable=True, comment="短期夏普比率")
    sharpe_score_short_rank = Column(VARCHAR(20), nullable=True, comment="短期夏普比率_同类排名")
    total_score_rank_short_term = Column(Numeric(20, 4), nullable=True, comment="短期评分高于**%的同类基金")
    manager_evaluation_short_term = Column(CLOB, nullable=True, comment="短期点评")
    total_score_medium_term = Column(Numeric(20, 4), nullable=True, comment="中期评分")
    return_score_medium_term = Column(Numeric(20, 4), nullable=True, comment="中期盈利能力")
    return_score_medium_rank = Column(VARCHAR(20), nullable=True, comment="中期盈利能力_同类排名")
    selection_score_medium_term = Column(Numeric(20, 4), nullable=True, comment="中期选股能力")
    selection_score_medium_rank = Column(VARCHAR(20), nullable=True, comment="中期选股能力_同类排名")
    timing_score_medium_term = Column(Numeric(20, 4), nullable=True, comment="中期择时能力")
    timing_score_medium_rank = Column(VARCHAR(20), nullable=True, comment="中期择时能力_同类排名")
    experience_score_medium_term = Column(Numeric(20, 4), nullable=True, comment="中期经验值")
    experience_score_medium_rank = Column(VARCHAR(20), nullable=True, comment="中期经验值_同类排名")
    max_drawdown_score_medium_term = Column(Numeric(20, 4), nullable=True, comment="中期抗风险力")
    max_drawdown_score_medium_rank = Column(VARCHAR(20), nullable=True, comment="中期抗风险力_同类排名")
    sharpe_score_medium_term = Column(Numeric(20, 4), nullable=True, comment="中期夏普比率")
    sharpe_score_medium_rank = Column(VARCHAR(20), nullable=True, comment="中期夏普比率_同类排名")
    total_score_rank_medium_term = Column(Numeric(20, 4), nullable=True, comment="中期高于**%的同类基金")
    manager_evaluation_medium_term = Column(CLOB, nullable=True, comment="中期点评")
    total_score_long_term = Column(Numeric(20, 4), nullable=True, comment="长期评分")
    return_score_long_term = Column(Numeric(20, 4), nullable=True, comment="长期盈利能力")
    return_score_long_rank = Column(VARCHAR(20), nullable=True, comment="长期盈利能力_同类排名")
    selection_score_long_term = Column(Numeric(20, 4), nullable=True, comment="长期选股能力")
    selection_score_long_rank = Column(VARCHAR(20), nullable=True, comment="长期选股能力_同类排名")
    timing_score_long_term = Column(Numeric(20, 4), nullable=True, comment="长期择时能力")
    timing_score_long_rank = Column(VARCHAR(20), nullable=True, comment="长期择时能力_同类排名")
    experience_score_long_term = Column(Numeric(20, 4), nullable=True, comment="长期经验值")
    experience_score_long_rank = Column(VARCHAR(20), nullable=True, comment="长期经验值_同类排名")
    max_drawdown_score_long_term = Column(Numeric(20, 4), nullable=True, comment="长期抗风险力")
    max_drawdown_score_long_rank = Column(VARCHAR(20), nullable=True, comment="长期抗风险力_同类排名")
    sharpe_score_long_term = Column(Numeric(20, 4), nullable=True, comment="长期夏普比率")
    sharpe_score_long_rank = Column(VARCHAR(20), nullable=True, comment="长期夏普比率_同类排名")
    total_score_rank_long_term = Column(Numeric(20, 4), nullable=True, comment="长期高于**%的同类基金")
    manager_evaluation_long_term = Column(CLOB, nullable=True, comment="长期点评")
    sign = Column(Integer, default=2, nullable=True, comment="最新标志,1表示最新,0表示旧")
    __table_args__ = (
        Index('fund_product_score_sign', "sign"), Index('idx_fund_product_score_code_sign', 'code', 'sign'))