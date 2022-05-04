import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': hpyc.STRING,
    'id': 'HexBinDecOct',  # ID，插件标识符，需要和文件名一致
    'option_name': "进制转换v1.0.0 by HowieHz",  # 选项名-在选择算法列表中
    'version': 'v1.0.0',  # 版本号

    'save_name': "进制转换",  # 文件保存项目名-在输出
    'quantifier': "",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "进制转换",  # 选择此项后输出的名字
    'author': "HowieHz",  # 作者(可选)
    'help': """
输入格式:
    需要转换的数字,输入的进制

    (输入的进制 -> 默认值10)
    (半角逗号分隔)
    
输入例:
    8,10
    8
    10,2
                    """,
    'output_end': "",

    'return_mode': hpyc.NO_RETURN_SINGLE_FUNCTION,
    'use_quantifier': hpyc.ON,
    "fullwidth_symbol": hpyc.OFF
}


def main(input: str, self, todo):  # 输出到框体内
    try:
        num, b = input.split(',')
    except Exception:
        num = input
        b = "10"
    if b == "2":
        num = int(num, 2)
    elif b == "8":
        num = int(num, 8)
    elif b == "10":
        num = int(num)
    elif b == "16":
        num = int(num, 16)
    else:
        hpyc.output(self, "目前不支持该进制的输入\n\n*做信息题是吧，自己算")
        return
    if todo == "output":
        hpyc.output(self, "二进制：" + str(bin(num))[2:])
        hpyc.output(self, "八进制：" + str(oct(num))[2:])
        hpyc.output(self, "十进制：" + str(num))
        hpyc.output(self, "十六进制：" + str(hex(num))[2:].upper())
    elif todo == "save":
        hpyc.write_without_flush(self, "二进制：" + str(bin(num))[2:])
        hpyc.write_without_flush(self, "八进制：" + str(oct(num))[2:])
        hpyc.write_without_flush(self, "十进制：" + str(num))
        hpyc.write_without_flush(self, "十六进制：" + str(hex(num))[2:].upper())
    elif todo == "test":
        pass
    else:
        pass
    return
