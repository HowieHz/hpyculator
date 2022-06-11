import hpyculator as hpyc
import numpy as np
from decimal import Decimal

VERSION = "V1.1.0"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "statistics_hz",
    "option": f"数列统计 {VERSION} by HowieHz",
    "version": VERSION,
    "tag": ["category:Mathematical calculations"],
    "save_name": "数列统计",
    "quantifier": "",
    "output_start": "",
    "output_name": "数列统计",
    "author": "HowieHz",
    "help": """\
    输入若干个数字，以此来计算这些数字的统计信息，例如平均数,众数,中位数,方差,标准差……

输入格式:
    A,B,C,...
    （用 半角逗号 或 全角逗号 或 空格 隔开的实数）

输入样例:
    1,2,3
    1 2 3
    1，2，3
""",
    "output_end": "",
    "return_mode": hpyc.RETURN_ONCE,
    "fullwidth_symbol": hpyc.OFF,
}


# def average_num(num_list):
#     """
#     计算一个数列的平均数
#
#     :param num_list:
#     :return:
#     """
#
# def variance(num_list):
#     """
#     计算一个数列的方差
#
#     :param num_list:
#     :return:
#     """
#
# def standard_deviation(num_list):
#     """
#     计算一个数列的标准差
#
#     :param num_list:
#     :return:
#     """


def mode(num_list):
    """
    统计一个数列里面数字的出现次数

    :param num_list:
    :return:
    """
    how = {}
    for _ in num_list:
        if _ in how:
            how[_] += 1
        else:
            how[_] = 1
    return sorted(how.items(), key=lambda key_value: (key_value[1], key_value[0]))


def on_calculate(inp):
    """计算函数"""
    if "," in inp:
        num = inp.split(",")
    elif "，" in inp:
        num = inp.split("，")
    else:
        num = inp.split()

    list_num = np.array(sorted(map(int, num)))

    mode_ret = mode(list_num)

    return f"""\
统计报告
    平均数:{np.average(list_num)}
    众数:{[i[0] for i in mode_ret if i[1] == mode_ret[-1][1]]}，出现了{mode_ret[-1][1]}次
    中位数:{np.median(list_num)}
    最大值:{np.max(list_num)}
    最小值:{np.min(list_num)}
    极差(全距)(最大值-最小值):{np.max(list_num) - np.min(list_num)}

    总体方差:{np.var(list_num)}
    样本方差:{np.var(list_num, ddof=1)}
    标准差(均方差):{np.std(list_num)}
    标准样本差:{np.std(list_num, ddof=1)}
    """


# np.median(a) # 得到数组 a 的中位数
# np.quantile(a, 0.25) # 得到数组 a 的上四分位数
# np.quantile(a, 0.5) # 得到数组 a 的中位数
# np.quantile(a, 0.75) # 得到数组 a 的下四分位数
