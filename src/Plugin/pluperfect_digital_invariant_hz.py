import hpyculator as hpyc
from typing import Generator
import math

NAME = "自幂数计算"
AUTHOR = "HowieHz" or ["HowieHz", ""]
VERSION = "V1.1.0"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,  # 输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
    "id": "pluperfect_digital_invariant_hz",  # 插件标识符,需要和文件名一致
    "option": f"{NAME}{VERSION} by {', '.join(AUTHOR) if isinstance(AUTHOR, list) else AUTHOR} 独身数 水仙花数 四叶玫瑰数 五角星数 六合数 北斗七星数 八仙数 九九重阳数 十全十美数",  # 选项名-在选择算法列表中（必须）
    "version": VERSION,  # 版本号
    "tag": ["category:Mathematical-calculations"],
    "save_name": "",  # 文件保存名
    "quantifier": "范围中的自幂数",  # 文件保存量词
    "output_start": "",  # 输出头
    "output_name": NAME,  # 选择此项后输出的名字
    "author": AUTHOR,  # 作者
    "help": """\
自幂数也被称为超完全数字不变数（pluperfect digital invariant, PPDI）,阿姆斯壮数或阿姆斯特朗数（Armstrong number）
自幂数是指一个 n 位数，它的每个位上的数字的 n 次幂之和等于它本身
Armstrong number is a number that is equal to the sum of cubes of its digits

输入两个数字a,b(a,b均为正整数)，求大于等于a，小于等于b的自幂数

输入格式
    a,b
    a b
    a，b

输入样例
    1,9999
                """,  # 帮助和说明
    "output_end": "",  # 输出小尾巴
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.OFF,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}

answer_list: tuple[int, ...] = (
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    153,
    370,
    371,
    407,
    1634,
    8208,
    9474,
    54748,
    92727,
    93084,
    548834,
    1741725,
    4210818,
    9800817,
    9926315,
    24678050,
    24678051,
    88593477,
    146511208,
)


def on_calculate(data: str, do_what: str) -> None:
    output = hpyc.output if do_what == "output" else hpyc.write  # 输出内容只需要用output就好了
    for pattern in [",", "，", " "]:
        if pattern in data:
            a, b, *_ = map(int, data.split(pattern))
            break
    else:
        hpyc.output("请按格式输入！！！")
        return

    if a < 0 or b < 0:  # 校验数据范围
        hpyc.output("请按格式输入！！！")
        return

    if b <= answer_list[-1]:  # 打表范围以内
        for answer in select_table(a, b):
            output(answer)
    else:  # 打表范围以外
        for answer in select_table(a, b):  # 表输出
            output(answer)

        for num in range(answer_list[-1] + 1, b + 1):
            if (
                sum(
                    map(
                        lambda _: _ ** math.ceil(math.log10(num)),
                        int_to_reverse_list(num),
                    )
                )
                == num
            ):
                output(num)


def select_table(start: int, end: int) -> Generator:
    """读表"""
    for ret in answer_list:
        if start <= ret <= end:
            yield ret


def int_to_reverse_list(r: int) -> Generator:  # 出来是倒序 int转可迭代对象
    while r:  # 商不为0就继续
        r, q = divmod(r, 10)  # quotient and remainder
        yield q


# 测试多种算法

# %%timeit
# math.ceil(math.log10(num))  # 最速取int位数传说
#
# %%timeit
# int(math.log10(num))+1
#
# %%timeit
# len(str(num))

# def int_to_reverse_list(num: int):  # 但是出来是倒序
#     while num:  # 还有数
#         yield num % 10
#         num //= 10
#
#
# def int_to_reverse_list2(r: int):  # 但是出来是倒序  最速int->可迭代对象传说
#     while r:  # 还有数
#         r, q = divmod(r, 10)
#         yield q
#
#
# def int_to_reverse_list3(value: int):  # 但是出来是倒序
#     result = []
#     while value:
#         result.append(value % 10)
#         value //= 10
#     return result
#
# def int_to_reverse_list4(value: int):  # 但是出来是倒序
#     result = ()
#     while value:
#         result+=(value % 10,)
#         value//=10
#     return result
