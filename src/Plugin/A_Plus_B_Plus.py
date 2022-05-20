import hpyculator as hpyc

PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "A_Plus_B_Plus",  # ID,插件标识符,需要和文件名一致
    "option_name": "高精度浮点数加法 基于列表 by HowieHz",  # 选项名-在选择算法列表中
    "version": "V1.0.1",  # 版本号
    "save_name": "加法",  # 文件保存项目名-在输出
    "quantifier": "",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": "高精度浮点数加法 基于列表",  # 选择此项后输出的名字
    "author": "HowieHz",  # 作者(可选)
    "help": """
输入格式：
    A,B（A>0,B>0）

输出结果:
    A+B
                """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.RETURN_ONCE,
    "use_quantifier": hpyc.OFF,
    "fullwidth_symbol": hpyc.OFF,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def on_calculate(data: str):  # 输出到框体内
    """计算函数

    :type data: str
    """
    a, b = data.split(",")
    point_a = a.find(".")  # 获得a的小数点的索引
    if point_a == -1:
        point_a = len(a)
    point_b = b.find(".")
    if point_b == -1:
        point_b = len(b)
    integer_a = a[:point_a]
    integer_b = b[:point_b]
    fractional_a = a[point_a + 1:]
    fractional_b = b[point_b + 1:]

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

    new_point = len(integer_a)
    list_a = list(integer_a + fractional_a)[::-1]  # 用[::-1]倒转，现在左边低位，右边高位
    list_b = list(integer_b + fractional_b)[::-1]

    # 各位相加
    list_answer = []
    for digital_a, digital_b in zip(list_a, list_b):
        list_answer.append(int(digital_a) + int(digital_b))

    # 进位
    for index, digital_answer in enumerate(list_answer):
        if digital_answer >= 10:
            list_answer[index] -= 10
            try:
                list_answer[index + 1] + 1
            except IndexError:
                list_answer.append(1)

    # 倒置加点输出
    list_answer.reverse()  # (用.reverse方法倒转更好读一点)
    if new_point != len(list_answer):
        list_answer.insert(new_point, ".")
    list_answer = map(str, list_answer)  # 把每项的数字转换成字符串
    answer = "".join(list_answer)
    return answer
