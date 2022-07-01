import hpyculator as hpyc

VERSION = "V1.0.1"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "Nth_power_of_n_hz",
    "option": f"x的n次方(幂运算) {VERSION} by HowieHz",
    "version": VERSION,
    "tag": ["category:Mathematical-calculations"],
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


def on_calculate(data: str):
    """计算函数"""
    for pattern in [",", "，", " "]:
        if pattern in data:
            x, n, *_ = map(
                lambda num: float(num) if "." in n else int(num), data.split(pattern)
            )
            break
    else:
        hpyc.output("请按格式输入！！！")
        return None
    return x**n
