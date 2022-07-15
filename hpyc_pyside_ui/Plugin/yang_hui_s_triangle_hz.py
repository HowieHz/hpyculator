import hpyculator as hpyc

VERSION = "V1.0.2"
PLUGIN_METADATA = {
    "input_mode": hpyc.NUM,
    "id": "yang_hui_s_triangle_hz",  # ID,插件标识符,需要和文件名一致（必须）
    "option": f"杨辉三角{VERSION} by HowieHz",  # 选项名-在选择算法列表中（必须）
    "version": VERSION,  # 版本号（必须）
    "tag": "category:Mathematical-calculations",
    "save_name": "杨辉三角",  # 文件保存项目名-在输出（必须）
    "quantifier": "行",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": "杨辉三角",  # 选择此项后输出的名字（必须）
    "author": "HowieHz",  # 作者(可选)
    "help": """\
    输入数字n ，输出前n行杨辉三角
            """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.ON,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


# def on_calculate(num: int, do_what: str) -> None:  # 返回一个列表
#     if do_what == "output":
#         output = hpyc.output
#     else:
#         output = hpyc.write
#
#     if not num:  # num = 0
#         output([])
#         return
#
#     all_line = [[1]]
#     output([1])
#     for _ in range(num - 1):
#         # all_line.append([x + y for x, y in zip([0] + all_line[-1], all_line[-1] + [0])])
#         # 等价代码
#         line = []
#         last_line = [0] + all_line[-1]
#         for x, y in zip(last_line, last_line[::-1]):
#             line.append(x + y)
#         all_line.append(line)
#         output(line)


def on_calculate(num: int, do_what: str) -> None:  # 返回一个列表
    if do_what == "output":
        output = hpyc.output
    else:
        output = hpyc.write

    if not num:  # num = 0
        output([])
        return

    all_line = [[1]]
    for _ in range(num - 1):
        all_line.append([x + y for x, y in zip([0] + all_line[-1], all_line[-1] + [0])])
        # 等价代码
        # line = []
        # last_line = [0] + all_line[-1]
        # for x, y in zip(last_line, last_line[::-1]):
        #     line.append(x + y)
        # all_line.append(line)

    for line in all_line:
        output(line)
    return
