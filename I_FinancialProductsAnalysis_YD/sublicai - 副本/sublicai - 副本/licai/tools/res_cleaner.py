import numpy as np


def clean_res(value):
    """
    清洗值
    (1) numpy类型转换为python原生类型
    (2) Nan转换为None
    (3) Inf转换为999999
    (4) -Inf转换为-999999

    Args:
        value: 原始值

    Returns:
        清洗后的值

    """
    # 转换Numpy
    if isinstance(value, np.generic):
        value = value.item()
    # 处理Nan
    if isinstance(value, float) and np.isnan(value):
        value = None
    # 处理Inf
    if isinstance(value, float) and np.isinf(value):
        if value > 0:
            value = 999999
        else:
            value = -999999
    return value


if __name__ == '__main__':
    a = np.float64(2.3)
    b = np.int32(12)
    c = np.nan
    d = np.inf
    e = np.array([123])[0]
    f = np.array([23.7])[0]
    g = np.array([np.nan])[0]
    h = np.array([-np.inf])[0]

    clean_res(a)
    clean_res(b)
    clean_res(c)
    clean_res(d)
    clean_res(e)
    clean_res(f)
    clean_res(g)
    clean_res(h)
    clean_res('123')
    clean_res(None)
