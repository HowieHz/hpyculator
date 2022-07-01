from typing import Optional

import hpyculator as hpyc

NAME = "高精度浮点数加法(基于字符串)"
AUTHOR = "HowieHz"
VERSION = "V1.0.4"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "A_Plus_B_String_hz",  # ID,插件标识符,需要和文件名一致
    "option": f"{NAME} by {AUTHOR}",  # 选项名-在选择算法列表中
    "version": VERSION,  # 版本号
    "tag": ["category:Mathematical-calculations"],
    "save_name": "",  # 文件保存项目名-在输出
    "quantifier": "相加所得",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": NAME,  # 选择此项后输出的名字
    "author": "HowieHz",  # 作者(可选)
    "help": """
输入格式：
    A,B（A>0,B>0）
    （数字间用空格或逗号分隔）

输出结果:
    A+B

输入样例
    1,2
    1 2
    1,2
                """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.RETURN_ONCE,
    "fullwidth_symbol": hpyc.OFF,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def on_calculate(data: str) -> Optional[str]:  # 输出到框体内
    """计算函数"""
    for pattern in [",", "，", " "]:
        if pattern in data:
            a, b, *_ = data.split(pattern)
            break
    else:
        return "请按格式输入！！！"
    point_a = a.find(".")  # 获得a的小数点的索引
    if point_a == -1:
        point_a = len(a)
    point_b = b.find(".")
    if point_b == -1:
        point_b = len(b)
    integer_a = a[:point_a]
    integer_b = b[:point_b]
    fractional_a = a[point_a + 1 :]
    fractional_b = b[point_b + 1 :]

    # 整数补齐
    if len(integer_a) > len(integer_b):  # a的整数部分比较长，所以补b的整数部分
        integer_b = integer_b.rjust(len(integer_a), "0")
    elif len(integer_a) == len(integer_b):
        pass
    else:  # len(integer_a)<len(integer_b):
        integer_a = integer_a.rjust(len(integer_b), "0")

    # 小数补齐
    if len(fractional_a) > len(fractional_b):  # a的整数部分比较长，所以补b的整数部分
        fractional_b = fractional_b.ljust(len(fractional_a), "0")
    elif len(fractional_a) == len(fractional_b):
        pass
    else:  # len(integer_a)<len(integer_b):
        fractional_a = fractional_a.ljust(len(fractional_b), "0")

    carry_num = 0  # 需要进位的数字
    answer = ""
    new_point = len(integer_a)
    a = (integer_a + fractional_a)[::-1]  # 用[::-1]倒转，现在左边低位，右边高位
    b = (integer_b + fractional_b)[::-1]
    for digital_a, digital_b in zip(a, b):
        digital_answer = int(digital_a) + int(digital_b)
        answer += str(digital_answer + carry_num)
        carry_num = 0  # 进位清零
        if digital_answer >= 10:
            carry_num = 1  # 进位
    answer = answer[::-1]
    if len(answer) != new_point:
        answer = answer[:new_point] + "." + answer[new_point:]

    return answer
