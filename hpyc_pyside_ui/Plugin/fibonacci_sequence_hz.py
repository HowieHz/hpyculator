import hpyculator as hpyc

VERSION = "V1.1.0"
PLUGIN_METADATA = {
    "input_mode": hpyc.NUM,
    "id": "fibonacci_sequence_hz",
    "option": f"斐波那契数列{VERSION} by HowieHz",
    "version": VERSION,
    "tag": ["category:Mathematical-calculations"],
    "save_name": "斐波那契数列前",
    "quantifier": "项",
    "output_start": "",
    "output_name": "斐波那契数列计算",
    "author": "HowieHz",
    "help": """
    输入数字n，输出斐波那契数列的前n项
""",
    "output_end": "",
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.ON,
}


def on_calculate(num, do_what):
    """计算函数"""
    output = hpyc.output if do_what == "output" else hpyc.write

    if num == 0:
        output("")
    if num == 1:
        output("1")
    if num >= 2:
        output("1")
        output("1")
    fs1 = 1
    fs2 = 1
    for _ in range(num - 2):
        fs3 = fs1
        fs1 += fs2
        fs2 = fs3
        output(fs1)
