import datetime
from typing import List, Optional, Tuple, Union, Iterable

import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta

__all__ = ['get_end_date', 'align_date_list', 'get_last_report_period', 'date_period_change',
           'get_last_date_in_period', 'TradeDateUtilsTemplate', 'align_time_series',
           'PeriodEndDateRange', 'ReportPeriodUtils', 'align_date', 'date2str', 'str2date', 'NatureDateUtils','get_cur_date','get_cur_time']

from config.basic_config import environment


def get_cur_time(fmt="%Y%m%d%H%M%S"):
    return datetime.datetime.now().strftime(fmt)


def get_cur_date(fmt="%Y%m%d"):
    return datetime.datetime.now().strftime(fmt)


class DateFormatTransfer(object):
    """
    时间日期转换器
    """

    @staticmethod
    def date2str(date: Optional[datetime.date], fmt='%Y%m%d') -> str:
        """
        将时间戳格式转换为字符串

        Args:
            date: 时间格式变量
            fmt: 转换后的字符串格式

        Returns:
            转换后的字符串

        Examples:
            >>> DateFormatTransfer.date2str(datetime.datetime.now().date())
            '20220128'
        """
        res = None
        if date is not None and not (isinstance(date, float) and np.isnan(date)):
            res = date.strftime(fmt)
        return res

    @staticmethod
    def str2date(date_str: Optional[str], fmt='%Y%m%d') -> datetime.date:
        """
        将字符串转换为时间格式

        Args:
            date_str: 时间字符串
            fmt: 时间字符串格式

        Returns:
            date格式

        Examples:
            >>> DateFormatTransfer.str2date("20220128")
            datetime.datetime(2022, 1, 28, 0, 0)
        """
        res = None
        if date_str is not None:
            res = datetime.datetime.strptime(date_str, fmt)
        return res


def date2str(date: Optional[datetime.date]):
    res = None
    if date is not None and not (isinstance(date, float) and np.isnan(date)):
        res = date.strftime('%Y%m%d')
    return res


def str2date(date_str: Optional[str]):
    res = None
    if date_str is not None:
        res = datetime.datetime.strptime(date_str, '%Y%m%d')
    return res


class PeriodEndDateRange(object):
    """
    周期结尾的Range迭代器
    """

    def __init__(self, start, end, step="d", is_trade_date=False, trade_date_list=None, is_include_end=True):
        """
        Args:
            start: 起始时间
            end: 结束时间
            step: 步长, 是d, w, m, q, h, y的形式
            is_trade_date: 是否交易日
            trade_date_list: 交易日列表
            is_include_end: 是否包含结束日期
        """
        if is_trade_date:  # 若取交易日, 则需要向下找到最近的交易日. 例如start=20211001, 不加该判断的话, 会取20210930
            start = TradeDateUtilsTemplate(trade_date_list).get_next_nearest_trading_date(start)
        self.start = get_cur_period_end(start, step, is_trade_date, trade_date_list)
        self.end = end
        self.step = step
        self.is_include_end = is_include_end
        self.is_trade_date = is_trade_date
        self.trade_date_list = trade_date_list

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_include_end:
            flag = self.start <= self.end
        else:
            flag = self.start < self.end

        if flag:
            ret = self.start
            nxt_period_end = get_nxt_period_end(self.start, self.step, self.is_trade_date, self.trade_date_list)
            if self.is_trade_date:
                nxt_period_end = nxt_period_end
                nxt_period_nature_end = nxt_period_end
                while nxt_period_end == self.start:
                    # 若出现一个周期内(如周)都没有交易日, 若is_trade_date设置为周, 会造成死循环
                    nxt_period_nature_end = get_nxt_period_end(nxt_period_nature_end, self.step)  # 该周期的自然结尾日，该周期内无交易日
                    nxt_period_end = get_nxt_period_end(nxt_period_nature_end, self.step, self.is_trade_date,
                                                        self.trade_date_list)

            self.start = nxt_period_end
            return ret
        else:
            raise StopIteration


class NatureDateUtils(object):
    @classmethod
    def date_period_change(cls, date: str, period: str):
        """
        对某一日期加减周期

        Args:
            date: 日期
            period: 周期，{数字}{d, w, m, q, h, y}形式, 分别代表日、周、月、季、半年、年. 如1y, 3m等
        Examples:
            >>> NatureDateUtils.date_period_change("20210810", "-3q")
            '20201110'
        """
        num = int(period[:-1])
        date_type = period[-1]
        if date_type == "y":
            new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(years=num)
        elif date_type == "h":
            new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(months=6 * num)
        elif date_type == "q":
            new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(months=3 * num)
        elif date_type == "m":
            new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(months=num)
        elif date_type == "w":
            new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(weeks=num)
        elif date_type == "d":
            new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(days=num)
        else:
            return None
        res = datetime.datetime.strftime(new_date, "%Y%m%d")
        return res

    @staticmethod
    def align_to_benchmark(benchmark_date_list: Iterable, time_series: pd.Series) -> pd.Series:
        """
        时间序列对齐到基准日期, 在每个基准日期按照**当日最近一次公布的值(含当日)**填充

        例如基金净值对齐到交易日中
        输出的时间列表为基准的时间, 值列表的规则如下：
        ①若日期在基准中, 则取该日期对应的值
        ②若日期不在基准中, 则将该值向后填充到下一个最近的基准中
        ③若有多个值向后填充到下一个最近基准, 则取下个最近基准前最近的一个日期对应的值
        例如交易日为20211202, 20211203, 20211206, 20211207
        基金在20211202公布净值为1.1, 则20211202得到的净值为1.1, 符合①条件
        基金在20211204公布净值为1.2, 则将该净值向后推移到20211206, 符合②条件
        基金在20211205公布净值为1.3, 则将该净值向后推移到20211206, 基金在20211206没有公布净值, 则使用20211205的净值而非20211204的净值, 符合③条件
        基金在20211203、20211207没有公布净值, 分别按照20211202、20211205公布的净值填充

        Args:
            benchmark_date_list: 基准日期
            time_series: 被对齐的时间序列, 是Series的形式, index为日期

        Returns:
            对齐后的时间序列

        Examples:
            >>> benchmark_list = [20211202, 20211203, 20211206, 20211207]
            >>> nav_series = pd.Series([1.1, 1.2, 1.3], index=[20211202, 20211204, 20211205])
            >>> NatureDateUtils.align_to_benchmark(benchmark_list, nav_series)
            20211202    1.1
            20211203    1.1
            20211206    1.3
            20211207    1.3
            dtype: float64
        """
        benchmark_date_list = np.array(benchmark_date_list)
        benchmark_date_list = benchmark_date_list[benchmark_date_list >= time_series.index[0]]
        return time_series.asof(benchmark_date_list)

    @classmethod
    def get_period_order(cls, date: str, period: str = "w") -> str:
        """
        对日期计算其周期次序，如第几周，第几月等

        Parameters
        ----------
        date: 日期
        period: 周期, ["w", "m", "q", "h", "y"]

        Returns
        -------
        返回周期序, 若周期不为年, 则格式为"年份+周期符号+周期序", 如2021W2; 若周期为年, 则格式为年份, 如2013

        Examples
        -------
        >>> NatureDateUtils.get_period_order("20210106", "w") # 20210101为周五, 则20201228-20210103为第53周, 20210106为第1周
        '2021W1'
        >>> NatureDateUtils.get_period_order("20201107", "m")
        '2020M11'
        >>> NatureDateUtils.get_period_order("20201107", "y")
        '2020'
        """
        year = date[:4]
        if period == "w":
            year, week_order, week_num = datetime.datetime.strptime(date, '%Y%m%d').isocalendar()
            return f"{year}W{str(week_order).zfill(2)}"
        if period == "m":
            return f"{year}M{date[4:6]}"
        if period == "q":
            month = int(date[4:6])
            return f"{year}Q{(month - 1) // 3 + 1}"
        if period == "h":
            month = int(date[4:6])
            return f"{year}H{(month - 1) // 6 + 1}"
        if period == "y":
            return year

    @classmethod
    def get_next_period_end(cls, date: str, period: str, is_trade_date=False, trade_date_list=None):
        """
        获取下一周期的最后自然日
        """
        cur_period_begin = get_cur_period_begin(date, period)  # 获取当前周期第一个自然日
        nxt_period_begin = NatureDateUtils.date_period_change(cur_period_begin, f'2{period}')  # 获取下2个周期第一个自然日
        res = get_last_period_end(nxt_period_begin, period)  # 获取下2个周期第一个自然日前一日, 即下1个周期最后一个自然日
        if is_trade_date:
            res = TradeDateUtilsTemplate(trade_date_list).get_pre_nearest_trading_date(res)
        return res

    @classmethod
    def get_next_period_begin(cls, date: str, period: str, is_trade_date=False, trade_date_list=None):
        """
        获取下一周期的期初自然日
        """
        cur_period_end = cls.get_cur_period_end(date, period)
        nxt_period_begin = cls.date_period_change(cur_period_end, "1d")
        cur_period_begin = get_cur_period_begin(date, period)  # 获取当前周期第一个自然日
        nxt_period_begin = NatureDateUtils.date_period_change(cur_period_begin, f'2{period}')  # 获取下2个周期第一个自然日
        res = get_last_period_end(nxt_period_begin, period)  # 获取下2个周期第一个自然日前一日, 即下1个周期最后一个自然日
        if is_trade_date:
            res = TradeDateUtilsTemplate(trade_date_list).get_pre_nearest_trading_date(res)
        return res
    
    @classmethod
    def get_cur_period_begin(cls, date: str, period: str) -> Optional[str]:
        """
        获取本周期开始日
        Args:
            date: 日期
            period: 周期, 是d, w, m, q, h, y格式
        """
        if period == 'y':
            res = date[:4] + '0101'
        elif period == 'h':
            month = (int(date[4:6]) - 1) // 6 * 6 + 1
            res = f"{date[:4]}{str(month).zfill(2)}01"
        elif period == 'q':
            month = 3 * ((int(date[4:6]) - 1) // 3) + 1
            res = f"{date[:4]}{str(month).zfill(2)}01"
        elif period == 'm':
            res = date[:6] + '01'
        elif period == 'w':
            date_time = datetime.datetime.strptime(date, '%Y%m%d')
            date_time = date_time - datetime.timedelta(days=date_time.weekday())
            res = date_time.strftime('%Y%m%d')
        else:
            res = None
        return res

    @classmethod
    def get_cur_period_end(cls, date: str, period: str, is_trade_date=False, trade_date_list=None):
        nxt_period_end = get_nxt_period_end(date, period)
        nxt_period_begin = get_cur_period_begin(nxt_period_end, period)
        res = NatureDateUtils.date_period_change(nxt_period_begin, '-1d')
        if is_trade_date:
            res = TradeDateUtilsTemplate(trade_date_list).get_pre_nearest_trading_date(res)
        return res

    @classmethod
    def get_last_period_end(cls, date: str, period: str, is_trade_date=False, trade_date_list=None):
        """
        获取上一周期的最后自然日
        """
        cur_period_begin = get_cur_period_begin(date, period)
        res = date_period_change(cur_period_begin, '-1d')
        if is_trade_date:
            res = TradeDateUtilsTemplate(trade_date_list).get_pre_nearest_trading_date(res)
        return res

    @classmethod
    def align_date(cls, obj_list: List[Union[pd.Series, pd.DataFrame]]):
        """
        将对象obj_list内元素裁剪为公共时间
        :param obj_list: Series或DataFrame列表, 其中index为需要对齐的时间
        :return: 与obj_list的格式一致, 只是index裁剪为inner join的形式
        """
        date_list = pd.concat(obj_list, axis=1, join="inner").index
        for i in range(len(obj_list)):
            obj_list[i] = obj_list[i].reindex(date_list)
        return obj_list

    @classmethod
    def get_end_date(cls) -> str:
        """
        获取计算时最新的截止日, 如果是当日0点-22点, 则最新截止日为前一日, 如果是当日22点-24点, 则最新截止日为当日
        """
        # if environment == "test":
        #     return "20220620"
        cur_date = datetime.datetime.now().strftime('%Y%m%d')
        if datetime.datetime.now().hour >= 22:
            end_date = cur_date
        else:
            pre_day = date_period_change(cur_date, '-1d')
            end_date = pre_day
        return end_date

    @classmethod
    def align_date_list(cls, benchmark_date_list: List[int], date_list: List[int],
                        value_list: List[float]) -> Tuple[List[int], List[float]]:
        """
        日期对齐到基准交易日, 同时返回相应值列表
        规则为:
        ①若待对齐日期为交易日, 则时间与值取当日
        ②若待对齐日期为非交易日, 则往后顺延到其后的第一个基准交易日
        ③若有多个日期顺延到其后的第一个基准交易日, 则值以最后一个日期

        例如基准交易日是20040101, 20040104, 中间两日为周末, 以下日期的对应关系为:
        20040101 —> 20040101
        20040102 —> 20040104
        20040103 —> 20040104
        20040104 —> 20040104

        Parameters
        ----------
        benchmark_date_list: 基准日期列表
        date_list: 日期列表
        value_list: 值列表

        Returns
        -------
        对齐后的日期列表和值列表

        Examples
        ________
        >>> align_date_list([20040101, 20040104], [20040101, 20040102, 20040103, 20040104], [1, 2, 3, 4])
        (array([20040101, 20040104]), array([1, 4]))
        """
        benchmark_date_list = np.array(benchmark_date_list)
        date_list = np.array(date_list)
        value_list = np.array(value_list)
        date_list_aligned = benchmark_date_list[benchmark_date_list >= date_list[0]]
        idx = date_list.searchsorted(date_list_aligned, side="right") - 1
        value_list_aligned = value_list[idx]
        return date_list_aligned, value_list_aligned

    @classmethod
    def align_time_series(cls, benchmark_date_list, time_series: pd.Series):
        benchmark_date_list = np.array(benchmark_date_list)
        date_list = np.array(time_series.index)
        value_list = np.array(time_series.values)
        if len(date_list) == 0:
            return pd.Series([])
        date_list_aligned = benchmark_date_list[benchmark_date_list >= date_list[0]]
        idx = date_list.searchsorted(date_list_aligned, side="right") - 1
        value_list_aligned = value_list[idx]
        return pd.Series(value_list_aligned, index=date_list_aligned)

    @classmethod
    def get_dates(cls, start, end, step='1d', is_include_end=True):
        if not step[0].isdigit():
            step = f'1{step}'
        res = []
        cur = start
        while 1:
            res.append(cur)
            cur = cls.date_period_change(cur, step)

            if is_include_end:
                flag = cur > end
            else:
                flag = cur >= end
            if flag:
                break
        return res


class ReportPeriodUtils(object):
    @staticmethod
    def get_last_report_period(date: str, report_period_type: Optional[str] = None) -> str:
        """
        获取当前日期以前最近的报告期

        Args:
            date: 当前日期
            report_period_type: 报告期类型,若为None, 则取前一个季度报告期, 若不为None, 则为单季度形式"0331", "0630", "0930", "1231"

        Returns:
            报告期列表

        Examples:
            >>> ReportPeriodUtils.get_last_report_period("20210810", "0930")
            '20200930'
        """
        if report_period_type is None:
            return NatureDateUtils().get_last_period_end(date, 'q')
        else:
            year = date[:4]
            if date > year + report_period_type:
                return f"{year}{report_period_type}"
            else:
                return f"{int(year) - 1}{report_period_type}"

    @staticmethod
    def get_dates(begin_date: str, end_date: str) -> List[str]:
        """
        获取起止时间内的报告期, 包括起止时间

        Args:
            begin_date: 开始时间
            end_date: 结束时间

        Returns:
            报告期列表

        Examples:
            >>> ReportPeriodUtils.get_dates("20190101", "20210101")
            ['20190331', '20190630', '20190930', '20191231', '20200331', '20200630', '20200930', '20201231']
        """
        date_list = []
        cur_quarter_end = NatureDateUtils().get_cur_period_end(begin_date, 'q')
        while cur_quarter_end <= end_date:
            date_list.append(cur_quarter_end)
            new_year = cur_quarter_end[:4]
            month_day = cur_quarter_end[4:]
            if month_day == '1231':
                new_year = str(int(new_year) + 1)
            new_month_day = {'0331': '0630', '0630': '0930', '0930': '1231', '1231': '0331'}[month_day]
            cur_quarter_end = f'{new_year}{new_month_day}'
        return date_list


"""
以下函数未来将被替代
"""


def align_date(obj_list: List[Union[pd.Series, pd.DataFrame]]):
    """
    将对象obj_list内元素裁剪为公共时间
    :param obj_list: Series或DataFrame列表, 其中index为需要对齐的时间
    :return: 与obj_list的格式一致, 只是index裁剪为inner join的形式
    """
    date_list = pd.concat(obj_list, axis=1, join="inner").index
    for i in range(len(obj_list)):
        obj_list[i] = obj_list[i].reindex(date_list)
    return obj_list


def get_end_date() -> str:
    """
    获取计算时最新的截止日, 如果是当日0点-22点, 则最新截止日为前一日, 如果是当日22点-24点, 则最新截止日为当日
    """
    if environment == "test":
        return "20220620"
    cur_date = datetime.datetime.now().strftime('%Y%m%d')
    if datetime.datetime.now().hour >= 22:
        end_date = cur_date
    else:
        pre_day = date_period_change(cur_date, '-1d')
        end_date = pre_day
    return end_date


def align_date_list(benchmark_date_list: List[int], date_list: List[int],
                    value_list: List[float]) -> Tuple[List[int], List[float]]:
    """
    日期对齐到基准交易日, 同时返回相应值列表
    规则为:
    ①若待对齐日期为交易日, 则时间与值取当日
    ②若待对齐日期为非交易日, 则往后顺延到其后的第一个基准交易日
    ③若有多个日期顺延到其后的第一个基准交易日, 则值以最后一个日期

    例如基准交易日是20040101, 20040104, 中间两日为周末, 以下日期的对应关系为:
    20040101 —> 20040101
    20040102 —> 20040104
    20040103 —> 20040104
    20040104 —> 20040104

    Parameters
    ----------
    benchmark_date_list: 基准日期列表
    date_list: 日期列表
    value_list: 值列表

    Returns
    -------
    对齐后的日期列表和值列表

    Examples
    ________
    >>> align_date_list([20040101, 20040104], [20040101, 20040102, 20040103, 20040104], [1, 2, 3, 4])
    (array([20040101, 20040104]), array([1, 4]))
    """
    benchmark_date_list = np.array(benchmark_date_list)
    date_list = np.array(date_list)
    value_list = np.array(value_list)
    date_list_aligned = benchmark_date_list[benchmark_date_list >= date_list[0]]
    idx = date_list.searchsorted(date_list_aligned, side="right") - 1
    value_list_aligned = value_list[idx]
    return date_list_aligned, value_list_aligned


def align_time_series(benchmark_date_list, time_series: pd.Series):
    benchmark_date_list = np.array(benchmark_date_list)
    date_list = np.array(time_series.index)
    value_list = np.array(time_series.values)
    if len(date_list) == 0:
        return pd.Series([])
    date_list_aligned = benchmark_date_list[benchmark_date_list >= date_list[0]]
    idx = date_list.searchsorted(date_list_aligned, side="right") - 1
    value_list_aligned = value_list[idx]
    return pd.Series(value_list_aligned, index=date_list_aligned)


def align_time_series_by_trade_date_template(time_series: pd.Series, period: str, end_date: str,
                                             trade_date_calendar: list = None, w=None):
    """
    将时间序列对齐到交易日, 并转化周期

    Args:
        time_series: 时间序列
        period: 周期, 是d, w, m, q, h, y格式
        begin_date: 最后对齐到的开始时间
        end_date: 最后对齐到的结束时间
        trade_date_calendar: Optional, 交易日列表, 与w二选一
        w: Optional, 获取交易日数据对象, 与trade_date_list二选一

    Returns:
        对齐并转化周期后的时间序列

    Examples:
        >>> time_series = pd.Series([1.0, 1.1, 1.2, 1.3], index=['20211008', '20211011', '20211013', '20211015'])
        >>> trade_date_list = ['20210930', '20211008', '20211011', '20211012', '20211013', '20211014', '20211015', '20211018',
                               '20211019', '20211020', '20211021', '20211022', '20211025', '20211026', '20211027', '20211028',
                               '20211029', '20211101']
        >>> print(align_time_series_by_trade_date_template(time_series, 'w', '20210930', '20211102', trade_date_list))
            20211008    1.0
            20211015    1.3
            20211022    1.3
            20211029    1.3
            dtype: float64

    """
    # 1. 找到所有交易日的周期末
    if trade_date_calendar is None:
        trade_date_calendar = w.get_trade_date_list_cache()
    begin_date = time_series.index.min()
    period_date_list = TradeDateUtilsTemplate(trade_date_calendar).get_period_last_trade_date_list(begin_date, end_date,
                                                                                                   period)
    # 2. 将时间序列对齐到周期末时间
    res = align_time_series(period_date_list, time_series)
    return res


def get_last_report_period(date: str, report_period_type: str) -> str:
    """
    获取当前日期以前最近的报告期

    Parameters
    ----------
    date: 当前日期
    report_period_type: 报告期类型, "0331", "0630", "0930", "1231"

    Examples
    --------
    >>> get_last_report_period("20210810", "0930")
    '20200930'
    """
    year = date[:4]
    if date > year + report_period_type:
        return f"{year}{report_period_type}"
    else:
        return f"{int(year) - 1}{report_period_type}"


def get_last_date_in_period(all_trade_date_list, date_list, period: str = 'w', cut_last: bool = True):
    """
    未来版本将被TradeDateUtilsTemplate.get_trade_date代替
    取日期列表内每个周期末尾日期

    Parameters
    ----------
    all_trade_date_list: 所有交易日列表
    date_list: 日期列表
    period: 周期
    cut_last: 若结果中最后一个日期并非当周期最后一个交易日, 则删除结果最后一个日期

    Returns
    -------
    周期转换后的日期列表

    Examples
    --------
    >>> get_last_date_in_period(np.arange(20210801, 20210817).astype(str), "w")
    ['20210801', '20210808', '20210815']
    """
    df = pd.DataFrame({"date": date_list})
    df["period"] = df["date"].apply(lambda x: NatureDateUtils.get_period_order(x, period))
    df = df.groupby("period").apply(lambda x: x.sort_values(by='date', ascending=False).iloc[0]).sort_values(
        by='date')
    if cut_last:
        if not TradeDateUtilsTemplate(all_trade_date_list).is_period_last_trade_date(df['date'].max(), period):
            df = df.iloc[:-1]
    return df["date"].tolist()


def get_cur_period_begin(date: str, period: str, is_trade_date=False, trade_date_list=None) -> Optional[str]:
    """
    获取本周期开始日
    Args:
        date: 日期
        period: 周期, 是d, w, m, q, h, y格式
    """
    if period == 'y':
        res = date[:4] + '0101'
    elif period == 'h':
        month = (int(date[4:6]) - 1) // 6 * 6 + 1
        res = f"{date[:4]}{str(month).zfill(2)}01"
    elif period == 'q':
        month = 3 * ((int(date[4:6]) - 1) // 3) + 1
        res = f"{date[:4]}{str(month).zfill(2)}01"
    elif period == 'm':
        res = date[:6] + '01'
    elif period == 'w':
        date_time = datetime.datetime.strptime(date, '%Y%m%d')
        date_time = date_time - datetime.timedelta(days=date_time.weekday())
        res = date_time.strftime('%Y%m%d')
    else:
        res = None
    if res is not None:
        if is_trade_date:
            res = TradeDateUtilsTemplate(trade_date_list).get_next_nearest_trading_date(res)
    return res


def get_cur_period_end(date: str, period: str, is_trade_date=False, trade_date_list=None):
    nxt_period_end = get_nxt_period_end(date, period)
    nxt_period_begin = get_cur_period_begin(nxt_period_end, period)
    res = NatureDateUtils.date_period_change(nxt_period_begin, '-1d')
    if is_trade_date:
        res = TradeDateUtilsTemplate(trade_date_list).get_pre_nearest_trading_date(res)
    return res


def get_last_period_end(date: str, period: str, is_trade_date=False, trade_date_list=None):
    """
    获取上一周期的最后自然日
    """
    cur_period_begin = get_cur_period_begin(date, period)
    res = NatureDateUtils.date_period_change(cur_period_begin, '-1d')
    if is_trade_date:
        res = TradeDateUtilsTemplate(trade_date_list).get_pre_nearest_trading_date(res)
    return res


def get_nxt_period_end(date: str, period: str, is_trade_date=False, trade_date_list=None):
    """
    未来版本将被NatureDateUtils.get_nxt_period_end替代
    获取下一周期的最后自然日
    """
    cur_period_begin = get_cur_period_begin(date, period)  # 获取当前周期第一个自然日
    nxt_period_begin = NatureDateUtils.date_period_change(cur_period_begin, f'2{period}')  # 获取下2个周期第一个自然日
    res = get_last_period_end(nxt_period_begin, period)  # 获取下2个周期第一个自然日前一日, 即下1个周期最后一个自然日
    if is_trade_date:
        res = TradeDateUtilsTemplate(trade_date_list).get_pre_nearest_trading_date(res)
    return res


def date_period_change(date: str, period: str, is_trade_date=False, trade_date_list=None) -> Optional[str]:
    """
    未来版本将被NatureDateUtils.date_period_change替代
    对某一日期加减周期

    Args:
        date: 日期
        period: 周期，{数字}{d, w, m, q, h, y}形式, 分别代表日、周、月、季、半年、年. 如1y, 3m等
    Examples:
        >>> date_period_change("20210810", "-3q")
        '20201110'
    """
    num = int(period[:-1])
    date_type = period[-1]
    if date_type == "y":
        new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(years=num)
    elif date_type == "h":
        new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(months=6 * num)
    elif date_type == "q":
        new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(months=3 * num)
    elif date_type == "m":
        new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(months=num)
    elif date_type == "w":
        new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(weeks=num)
    elif date_type == "d":
        new_date = datetime.datetime.strptime(date, "%Y%m%d") + relativedelta(days=num)
    else:
        return None
    res = datetime.datetime.strftime(new_date, "%Y%m%d")
    if is_trade_date:
        res = TradeDateUtilsTemplate(trade_date_list).get_pre_nearest_trading_date(res)
    return res


def get_period_order(date: str, period: str = "w") -> str:
    year = date[:4]
    if period == "w":
        year, week_order, week_num = datetime.datetime.strptime(date, '%Y%m%d').isocalendar()
        return f"{year}W{str(week_order).zfill(2)}"
    if period == "m":
        return f"{year}M{date[4:6]}"
    if period == "q":
        month = int(date[4:6])
        return f"{year}Q{(month - 1) // 3 + 1}"
    if period == "h":
        month = int(date[4:6])
        return f"{year}H{(month - 1) // 6 + 1}"
    if period == "y":
        return year


class TradeDateUtilsTemplate(object):
    """
    交易日期相关API
    """

    def __init__(self, trade_date_list: Optional[np.ndarray]):
        self.trade_date_list = np.array(trade_date_list)

    def count_trading_dates(self, start_date: str, end_date: str) -> int:
        """
        统计两个日期之间有多少交易日

        Parameters
        ----------
        start_date: 开始日期
        end_date: 结束日期

        Examples
        --------
        >>> TradeDateUtilsTemplate().count_trading_dates("20200808", "20210808")
        243
        """
        return self.trade_date_list.searchsorted(end_date, side='right') - self.trade_date_list.searchsorted(start_date)

    def date_period_change(self, date: str, period: str, is_forward=True) -> Optional[str]:
        """
        对某一日期加减周期

        Args:
            date: 日期
            period: 周期，{数字}{d, w, m, q, h, y}形式, 分别代表日、周、月、季、半年、年. 如1y, 3m等
            is_forward: 如果该时间非交易日, 则向前一个交易日
        Examples:
            >>> date_period_change("20210810", "-3q")
            '20201110'
        """
        res = NatureDateUtils.date_period_change(date, period)
        if is_forward:
            res = self.get_pre_nearest_trading_date(res)
        else:
            res = self.get_next_nearest_trading_date(res)
        return res

    def get_cur_period_begin(self, date: str, period: str) -> str:
        """
        获取本周期第一个交易日

        Args:
            date: 日期
            period: 周期

        Returns:
            交易日期

        """
        res = NatureDateUtils.get_cur_period_begin(date, period)
        res = self.get_next_nearest_trading_date(res)
        return res

    def get_cur_period_end(self, date: str, period: str) -> str:
        """
        获取本周期最后一个交易日

        Args:
            date: 日期
            period: 周期

        Returns:
            交易日期

        """
        res = NatureDateUtils.get_cur_period_end(date, period)
        res = self.get_pre_nearest_trading_date(res)
        return res

    def get_last_period_begin(self, date: str, period: str) -> str:
        """
        获取上周期期初交易日

        Args:
            date: 日期
            period: 周期

        Returns:
            上周期期初交易日

        Examples:
            >>> trade_date_list = ['20210730', '20210802', '20210803', '20210804', '20210805', '20210806', '20210809']
            >>> TradeDateUtils(trade_date_list).get_last_period_begin("20210805", "w")
            '20210730'
        """
        begin_date = NatureDateUtils.get_last_period_begin(date, period)
        begin_trade_date = self.get_next_nearest_trading_date(begin_date)
        return begin_trade_date

    def get_last_period_end(self, date: str, period: str) -> str:
        """
        获取上周期期末交易日

        Args:
            date: 日期
            period: 周期

        Returns:
            上周期期末交易日

        Examples:
            >>> trade_date_list = ['20210730', '20210802', '20210803', '20210804', '20210805', '20210806', '20210809']
            >>> TradeDateUtils(trade_date_list).get_last_period_end("20210805", "w")
            '20210730'
        """
        end_date = NatureDateUtils.get_last_period_end(date, period)
        end_trade_date = self.get_pre_nearest_trading_date(end_date)
        return end_trade_date

    def get_next_nearest_trading_date(self, date: str) -> str:
        """
        获取向后最新一次交易日
        """
        if self.is_trading_date(date):
            return date
        else:
            return self.get_next_trading_date(date)

    def get_next_period_begin(self, date: str, period: str) -> str:
        """
        获取下周期期初交易日

        Args:
            date: 日期
            period: 周期

        Returns:
            下周期期初交易日

        Examples:
            >>> trade_date_list = ['20210730', '20210802', '20210803', '20210804', '20210805', '20210806', '20210809']
            >>> TradeDateUtils(trade_date_list).get_next_period_begin("20210802", "w")
            '20210809'
        """
        begin_date = NatureDateUtils.get_next_period_begin(date, period)
        begin_trade_date = self.get_next_nearest_trading_date(begin_date)
        return begin_trade_date

    def get_next_period_end(self, date: str, period: str) -> str:
        """
        获取下周期期末交易日

        Args:
            date: 日期
            period: 周期

        Returns:
            下周期期末交易日

        Examples:
            >>> trade_date_list = ['20210730', '20210802', '20210803', '20210804', '20210805', '20210806', '20210809']
            >>> TradeDateUtils(trade_date_list).get_next_period_end("20210802", "w")
            '20210809'
        """
        end_date = NatureDateUtils.get_next_period_end(date, period)
        end_trade_date = self.get_pre_nearest_trading_date(end_date)
        return end_trade_date

    def get_pre_nearest_trading_date(self, date: str) -> str:
        """
        获取向前最新一次交易日
        """
        if self.is_trading_date(date):
            return date
        else:
            return self.get_previous_trading_date(date)

    def get_previous_trading_date(self, date: str, n: int = 1) -> str:
        """
        获取前n个交易日

        Parameters
        ----------
        date: 日期
        n: 日期个数

        Examples
        --------
        >>> TradeDateUtilsTemplate().get_previous_trading_date("20210810")
        '20210809'
        """
        pos = self.trade_date_list.searchsorted(date)
        if pos >= n:
            return self.trade_date_list[pos - n]
        else:
            return self.trade_date_list[0]

    def get_next_trading_date(self, date: str, n: int = 1) -> str:
        """
        获取后n个交易日

        Parameters
        ----------
        date: 日期
        n: 日期个数

        Examples
        --------
        >>> TradeDateUtilsTemplate().get_next_trading_date("20210810")
        '20210811'
        """
        pos = self.trade_date_list.searchsorted(date, side='right')
        if pos + n > len(self.trade_date_list):
            return self.trade_date_list[-1]
        else:
            return self.trade_date_list[pos + n - 1]

    def get_trade_dates(self, begin_date: str = None, end_date: str = None, period='d', cut_last=True) -> np.ndarray:
        """
        获取交易日期列表

        Args:
            begin_date: 开始日期
            end_date: 结束日期

        Returns:
            范围在开始和结束日期之间的日期列表

        Examples:
            >>> TradeDateUtilsTemplate().get_trade_dates("20210730", "20210810")
            ['20210730' '20210802' '20210803' '20210804' '20210805' '20210806' '20210809' '20210810']
        """
        if begin_date is None:
            begin_index = 0
        else:
            begin_index = self.trade_date_list.searchsorted(begin_date)
        if end_date is None:
            end_index = len(self.trade_date_list)
        else:
            end_date = self.get_pre_nearest_trading_date(end_date)
            end_index = self.trade_date_list.searchsorted(end_date)  # 结束日期若为交易日, 则取该日, 若非交易日, 取前一个交易日
        res = self.trade_date_list[begin_index:end_index + 1]
        if len(res) == 0:
            return res
        if period != 'd':
            df = pd.DataFrame({"date": res})
            df["period"] = df["date"].apply(lambda x: NatureDateUtils.get_period_order(x, period))
            df = df.groupby("period").apply(lambda x: x.sort_values(by='date', ascending=False).iloc[0]).sort_values(
                by='date')
            if cut_last:
                if not self.is_period_last_trade_date(df['date'].max(), period):
                    df = df.iloc[:-1]
            res = df["date"].values
        return res

    def get_period_last_trade_date_list(self, begin_date, end_date, period):
        """
        获取起止时间内所有周期最后交易日

        Args:
            begin_date: 开始时间
            end_date: 结束时间
            period: 周期

        Returns:
            周期最后交易日列表
        """
        date_list = self.get_trade_dates(begin_date, end_date)
        df = pd.DataFrame({'date': date_list})
        if period == 'd':
            return df['date'].values
        else:
            df['period'] = df['date'].apply(lambda x: NatureDateUtils.get_period_order(x, period))
            df = df.groupby('period').apply(lambda x: x.iloc[-1])
            date_list = df['date'].values
            date_list.sort()
            if not self.is_period_last_trade_date(date_list[-1], period):
                date_list = date_list[:-1]
            return date_list

    def align_time_series(self, time_series: pd.Series, period: str, end_date: str = None):
        """
        将时间序列对齐到交易日, 并转化周期

        Args:
            time_series: 时间序列
            period: 周期, 是d, w, m, q, h, y格式
            end_date: 最后对齐到的结束时间

        Returns:
            对齐并转化周期后的时间序列
        """
        # 1. 找到所有交易日的周期末
        begin_date = time_series.index.min()
        period_date_list = self.get_period_last_trade_date_list(begin_date, end_date, period)
        # 2. 将时间序列对齐到周期末时间
        res = align_time_series(period_date_list, time_series)
        return res

    def transfer_period(self, time_series: pd.Series, end_date: str = None, period: str = "w") -> pd.Series:
        """
        对时间序列转换周期
        例如日频净值转换为周频

        Args:
            time_series: 时间序列
            end_date: 结束时间
                默认为time_series的最后日期. 之所以开放这个参数是因为有时时间序列不全, 希望向后补充
                例如基金净值最后公布时间为2022.1.14, 取period="w", end_date="20220128", 希望将每周的净值填充为2022.1.14的净值
                而不是将净值序列限制到2022.1.14
            period: 周期

        Returns:
            转换后的时间序列

        Examples:
            >>> trade_date_list = ['20210730', '20210802', '20210803', '20210804', '20210805', '20210806', '20210809']
            >>> time_series_ = pd.Series([1,2,3], index=["20210730", "20210803", "20210809"])
            >>> TradeDateUtils(trade_date_list).transfer_period(time_series_)
            20210730    1.0
            20210806    2.0
            dtype: float64
        """
        begin_date = time_series.index.min()
        if end_date is None:
            end_date = time_series.index.max()
        period_date_list = self.get_trade_dates(begin_date, end_date, period, cut_last=False)
        # 将时间序列对齐到交易日期的周期末时间
        res = NatureDateUtils.align_to_benchmark(period_date_list, time_series)
        return res

    def is_trading_date(self, date) -> bool:
        """
        判断是否是交易日

        Parameters
        ----------
        date: 待判断日期

        Examples
        --------
        >>> TradeDateUtilsTemplate().is_trading_date("20210808")
        False
        """
        return date in self.trade_date_list

    def is_period_first_trade_date(self, date: str, period: str = "w") -> bool:
        """
        判断日期是否是周期首个交易日
        Parameters
        ----------
        date: 日期
        period: 周期["w", "m", "q", "h", "y"]

        Examples
        --------
        >>> TradeDateUtilsTemplate().is_period_first_trade_date("20210806", "w") # 当日为周五, 并非当周最后1个交易日
        False
        """
        prev_date = self.get_previous_trading_date(date)
        return self.is_trading_date(date) & (
                NatureDateUtils.get_period_order(prev_date, period) != NatureDateUtils.get_period_order(date, period))

    def is_period_last_trade_date(self, date: str, period: str = "w") -> bool:
        """
        判断日期是否是周期最后交易日
        Parameters
        ----------
        date: 日期
        period: 周期["w", "m", "q", "h", "y"]

        Examples
        --------
        >>> TradeDateUtilsTemplate().is_period_last_trade_date("20210806", "w") # 当日为周五, 是当周最后1个交易日
        True
        """
        next_date = self.get_next_trading_date(date)
        return self.is_trading_date(date) & (
                NatureDateUtils.get_period_order(next_date, period) != NatureDateUtils.get_period_order(date,
                                                                                                        period))

    def get_ready_trade_date(self):
        if environment == "test":
            return "20220914"
        end_date = NatureDateUtils.get_end_date()
        ready_date = self.get_pre_nearest_trading_date(end_date)
        return ready_date

    def get_common_interval_begin_end(self, date: str, interval: str = "1m"):
        """
        获取固定区间的开始结束日期
        Args:
            date: 日期
            interval: ['1m', '1h', '1y', '2y', ..., ’2018(单年度)']

        Returns:
            区间的开始结束日期
        """
        if interval.isdigit():  # 数字型表示单年度
            nature = f"{interval}{date[4:]}"
            interval_begin_date = self.get_last_period_end(nature, period='y')
            interval_end_date = self.get_cur_period_end(nature, period='y')
            interval_end_date = min(self.get_pre_nearest_trading_date(date), interval_end_date)
        else:
            interval_begin_date = self.date_period_change(date, f"-{interval}")
            interval_end_date = self.get_pre_nearest_trading_date(date)
        return interval_begin_date, interval_end_date
