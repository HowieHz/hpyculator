import hpyculator as hpyc

PLUGIN_METADATA = {
    "input_mode": hpyc.FLOAT,
    "id": "fibonacci_Sequence",
    "option_name": "斐波那契数列V1.0.1 by HowieHz",
    "version": "V1.0.1",
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
    "use_quantifier": hpyc.OFF,
    "fullwidth_symbol": hpyc.ON,
}


def on_calculate(num, do_what):
    """计算函数"""
    if do_what == "output":
        if num == 0:
            hpyc.output("")
        if num == 1:
            hpyc.output("1")
        if num >= 2:
            hpyc.output("1")
            hpyc.output("1")
        fs1 = 1
        fs2 = 1
        n = 2
        while n < num:
            fs3 = fs1
            fs1 += fs2
            fs2 = fs3
            hpyc.output(fs1)
            n += 1
    else:
        if num == 0:
            hpyc.write("")
        if num == 1:
            hpyc.write("1")
        if num >= 2:
            hpyc.write("1")
            hpyc.write("1")
        fs1 = 1
        fs2 = 1
        n = 2
        while n < num:
            fs3 = fs1
            fs1 += fs2
            fs2 = fs3
            hpyc.write(fs1)
            n += 1
