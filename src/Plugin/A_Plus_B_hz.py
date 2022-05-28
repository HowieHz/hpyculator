import hpyculator as hpyc

NAME = "整数加法"
AUTHOR = "HowieHz"
VERSION = "V1.2.2"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,  # 输入模式
    "id": "A_Plus_B_hz",  # ID,插件标识符,需要和文件名一致（必须）
    "option": f"{NAME}{VERSION} by {AUTHOR}",  # 选项名-在选择算法列表中（必须）
    "version": VERSION,  # 版本号（必须）
    "save_name": "",  # 文件保存项目名-在输出（必须）
    "quantifier": "相加所得",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": NAME,  # 选择此项后输出的名字（必须）
    "author": AUTHOR,  # 作者(可选)
    "help": """
输入格式
    A,B,C,D……
    （数字间用空格或逗号分隔，ABCD等均为整数）

输入样例
    1,2,3
    1 2 3
    1,2
    2 3 112312 123123
    """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.RETURN_ONCE,
    "fullwidth_symbol": hpyc.OFF,
}


def on_calculate(data: str):
    """计算函数"""
    try:
        if "," in data:
            ret = sum(map(int, data.split(",")))
        elif "，" in data:
            ret = sum(map(int, data.split("，")))
        else:
            ret = sum(map(int, data.split()))
    except ValueError:
        return "请按格式输入！！！"
    return ret
