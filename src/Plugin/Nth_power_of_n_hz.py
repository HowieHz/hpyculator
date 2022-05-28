import hpyculator as hpyc

VERSION = "V1.0.0"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "Nth_power_of_n_hz",
    "option": f"x的n次方(幂运算) {VERSION} by HowieHz",
    "version": VERSION,
    "tag": ["category:Mathematical calculations"],
    "save_name": "",
    "quantifier": "次幂",
    "output_start": "",
    "output_name": "2的n次方",
    "author": "HowieHz",
    "help": """\
    计算x的n次方

输入格式:
    x,n
    (数字间用逗号或者空格分隔)

输入样例:
    9 9
    9,9
    9，9
""",
    "output_end": "",
    "return_mode": hpyc.RETURN_ONCE,
    "fullwidth_symbol": hpyc.OFF,
}


def on_calculate(inp):
    """计算函数"""
    try:
        if "," in inp:
            x, n = inp.split(",")
        elif "，" in inp:
            x, n = inp.split("，")
        else:
            x, n = inp.split()
        n = float(n) if "." in n else int(n)
        x = float(x) if "." in x else int(x)
    except ValueError:
        return "请按照格式输入"
    return x**n
