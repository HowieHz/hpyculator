import hpyculator as hpyc

VERSION = "V1.0.0"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "Nth_power_of_2_hz",
    "option": f"2的n次方 {VERSION} by HowieHz",
    "version": VERSION,
    "save_name": "2的",
    "quantifier": "次方",
    "output_start": "",
    "output_name": "2的n次方",
    "author": "HowieHz",
    "help": """\
    计算2的n次方

输入格式:
    n

输入样例:
    9
""",
    "output_end": "",
    "return_mode": hpyc.RETURN_ONCE,
    "fullwidth_symbol": hpyc.OFF,
}


def on_calculate(inp):
    """计算函数"""
    try:
        inp = float(inp) if "." in inp else int(inp)
    except ValueError:
        return "请按照格式输入"
    return 2 ** inp
