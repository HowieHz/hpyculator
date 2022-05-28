import hpyculator as hpyc

VERSION = "V1.0.2"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "test9_hz",  # ID,插件标识符
    "option": f"tset⑨{VERSION} by HowieHz",  # 选项名-在选择算法列表中
    "version": VERSION,  # 版本号
    "tag": ["category:Other"],
    "save_name": "tset⑨",  # 文件保存项目名-在输出
    "quantifier": "",  # 文件保存量词-在输入后面
    "output_start": "",  # 输出头
    "output_name": "test⑨",
    "author": "HowieHz",
    "help": """\
    输入n，输出n个⑨

    不满一个的⑨就会被幽幽子吃掉
""",
    "output_end": "",
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
}


def on_calculate(
        data: str, do_what: str
):  # 调用时传入两个参数，第一个参数是输入，第二个参数是程序的主类，要作为输出函数的的第一个参数
    """计算函数"""
    # print(hpyc.getIoInstance())
    num = data
    num = int(num)
    need_write = ""
    need_write_len = 0
    for _ in range(num):
        need_write += "⑨\n"
        need_write_len += 1
        if need_write_len >= 100000000:
            hpyc.write_without_flush(need_write)
            hpyc.flush()
            need_write = ""
            need_write_len = 0
    if do_what == "output":
        hpyc.output(need_write)
    else:
        hpyc.write(need_write)
