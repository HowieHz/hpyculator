import hpyculator as hpyc

VERSION = "V1.0.3"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "heron_s_formula_hz",  # ID,插件标识符,需要和文件名一致（必须）
    "option": f"海伦公式求三角形面积{VERSION} by HowieHz",  # 选项名-在选择算法列表中（必须）
    "version": VERSION,  # 版本号（必须）
    "tag": ["category:Mathematical-calculations"],
    "save_name": "",  # 文件保存项目名-在输出（必须）
    "quantifier": "为边长的三角形的面积",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": "海伦公式求三角形面积",  # 选择此项后输出的名字（必须）
    "author": "HowieHz",  # 作者(可选)
    "help": """
输入格式
    实数A,实数B,实数C
    三个数据用逗号或空格隔开

输出格式
    以A,B,C为边长的三角形的面积

输入样例
    12,12,12
    12，12，12
    12 12 12

   """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.OFF,
}


def on_calculate(data: str, do_what):
    """计算函数"""
    for pattern in [",", "，", " "]:
        if pattern in data:
            a, b, c, *_ = map(
                lambda num: int(num) if num.isdigit() else float(num),
                data.split(pattern),
            )
            break
    else:
        hpyc.output("请按格式输入！！！")
        return
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    if do_what == "output":
        hpyc.output(
            "以" + str(a) + "," + str(b) + "," + str(c) + "为边长的三角形的面积是:\n" + str(s)
        )
    if do_what == "save":
        hpyc.write(str(s))
