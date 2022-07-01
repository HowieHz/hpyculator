import hpyculator as hpyc

VERSION = "V1.0.3"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "HexBinDecOct_hz",  # ID，插件标识符，需要和文件名一致
    "option": f"进制转换{VERSION} by HowieHz",  # 选项名-在选择算法列表中
    "version": VERSION,  # 版本号
    "tag": ["category:Mathematical-calculations"],
    "save_name": "",  # 文件保存项目名-在输出
    "quantifier": "的进制转换结果",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": "进制转换",  # 选择此项后输出的名字
    "author": "HowieHz",  # 作者(可选)
    "help": """
输入格式:
    需要转换的数字,输入的进制

    (输入的进制 -> 默认值10)
    (逗号 或 空格分隔)

输入例:
    8,10
    8
    10，2
    10 2
    """,
    "output_end": "",
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.OFF,
}


def on_calculate(data: str, todo):
    """计算函数"""
    for pattern in [",", "，", " "]:
        if pattern in data:
            num, base, *_ = data.split(pattern)
            break
    else:
        hpyc.output("请按格式输入！！！")
        return
    base = base or "10"  # 初始化

    if base == "2":
        num = int(num, 2)
    elif base == "8":
        num = int(num, 8)
    elif base == "10":
        num = int(num)
    elif base == "16":
        num = int(num, 16)
    else:
        hpyc.output("目前不支持该进制的输入\n\n*做信息题是吧，自己算")
        return
    if todo == "output":
        hpyc.output("二进制：" + str(bin(num))[2:])
        hpyc.output("八进制：" + str(oct(num))[2:])
        hpyc.output("十进制：" + str(num))
        hpyc.output("十六进制：" + str(hex(num))[2:].upper())
    elif todo == "save":
        hpyc.write_without_flush("二进制：" + str(bin(num))[2:])
        hpyc.write_without_flush("八进制：" + str(oct(num))[2:])
        hpyc.write_without_flush("十进制：" + str(num))
        hpyc.write_without_flush("十六进制：" + str(hex(num))[2:].upper())
    else:
        pass
    return
