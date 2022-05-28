import numba
import hpyculator as hpyc
from decimal import Decimal

NAME = "是质数吗？(是素数吗？)"
AUTHOR = "HowieHz"
VERSION = "V1.0.0"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "is_prime_hz",
    "option": f"{NAME}{VERSION} by {AUTHOR}",
    "version": VERSION,
    "tag": ["category:Mathematical calculations"],
    "save_name": "",
    "quantifier": "的质数鉴定结果",
    "output_start": "",
    "output_name": "是质数吗？",
    "author": "HowieHz",
    "help": """\
    输入一个大于1的正整数，判断是否是质数

输入格式:
    n(n为正整数且n>1)
    
使用了jit技术，第一次运行稍慢
""",
    "output_end": "",
    "return_mode": hpyc.RETURN_ONCE,
    "fullwidth_symbol": hpyc.OFF,
}


@numba.jit(nopython=True)
def is_prime_jit(num):
    """
    判断是否是质数 小范围的话要2，3特判

    :param num:
    :return:
    """
    if (num == 2) or (num == 3):
        return True, 0
    if (num % 6 != 1) and (num % 6 != 5):
        if num % 2 == 0:
            return False, 2
        else:
            return False, 3
    for i in range(5, int(num ** 0.5) + 1, 6):
        if (num % i == 0) or (num % (i + 2) == 0):
            return False, i
    return True, 0


def is_prime(num):
    """
    判断是否是质数 小范围的话要2，3特判

    :param num:
    :return:
    """
    if (num % 6 != 1) and (num % 6 != 5):
        if num % 2 == 0:
            return False, 2
        else:
            return False, 3
    for i in range(5, int(num ** 0.5) + 1, 6):
        if (num % i == 0) or (num % (i + 2) == 0):
            return False, i
    return True, 0


def is_prime_big_int(num):
    """
    判断是否是质数 小范围的话要2，3特判
    为了准确性 做除法的时候转换成Decimal

    :param num:
    :return:
    """
    if (int(num) % 6 != 1) and (num % 6 != 5):
        if num % 2 == 0:
            return False, 2
        else:
            return False, 3
    for i in range(5, int(Decimal(num) / 2) + 1, 6):
        if (num % i == 0) or (num % (i + 2) == 0):
            return False, i
    return True, 0


def on_calculate(num: str):
    if not num.isdigit() or int(num) <= 1:
        return f"{num}不是大于1的正整数，无法鉴定"
    num = int(num)
    if num > int(float("17" + 307 * "0")):  # 1.7E+308
        print("nmsl")
        answer = is_prime_big_int(num)
        if answer[0]:
            return f"{num}是质数"
        else:
            return f"{num}不是质数，有一个因数是{answer[1]}"
    if num > 9223372036854775807:
        answer = is_prime(num)
        if answer[0]:
            return f"{num}是质数"
        else:
            return f"{num}不是质数，有一个因数是{answer[1]}"
    answer = is_prime_jit(num)
    if answer[0]:
        return f"{num}是质数"
    else:
        return f"{num}不是质数，有一个因数是{answer[1]}"
