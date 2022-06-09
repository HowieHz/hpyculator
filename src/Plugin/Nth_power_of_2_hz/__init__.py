from typing import Optional

import hpyculator as hpyc

VERSION = "V1.0.1"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "Nth_power_of_2_hz",
    "option": f"2的n次方{VERSION} by HowieHz",
    "version": VERSION,
    "tag": ["category:Mathematical calculations", "cache"],
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
    
此插件使用了文本文件来储存缓存
如计算过一遍，将会读取上次运算的缓存直接输出
如修改缓存，会导致不可预知的后果
""",
    "output_end": "",
    "return_mode": hpyc.RETURN_ONCE,
    "fullwidth_symbol": hpyc.OFF,
}


def on_calculate(inp: str):
    """计算函数"""
    try:
        inp = float(inp) if "." in inp else int(inp)
    except ValueError:
        return "请按照格式输入"
    # if inp in table:
    #     return table[inp]
    return 2**inp
    # make_table(inp)


# def make_table(how):
#     """打表专用"""
#     import tqdm
#     import os
#     ans = 2
#     with open(os.path.join(__file__, "..", "table.py"), mode="a+", encoding="utf-8") as f:
#         for num in tqdm.tqdm(range(1, how + 1)):
#             f.write(f"{num}: {ans},\n")
#             ans *= 2
