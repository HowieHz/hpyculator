import hpyculator as hpyc

NAME = "名"
AUTHOR = "作者" or ["作者1", "作者2"]
VERSION = "V1.0.0"
PLUGIN_METADATA = {
    'input_mode' : hpyc.STRING,  # 输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
    'id' : '',  # 插件标识符,需要和文件名一致
    "option": f"{NAME}{VERSION} by {', '.join(AUTHOR) if isinstance(AUTHOR,list) else AUTHOR}",  # 选项名-在选择算法列表中（必须）
    'version' : VERSION,  # 版本号
    'tag' : [""],

    'save_name' : "",  # 文件保存名
    'quantifier' : "",  # 文件保存量词

    'output_start' : "",  # 输出头
    'output_name' : NAME,  # 选择此项后输出的名字
    'author' : AUTHOR,  # 作者
    'help' : """\
输入格式
    n

输入样例
    1
                """,  # 帮助和说明
    'output_end' : "",  # 输出小尾巴

    'return_mode' : hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol" : hpyc.OFF  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
    }


def on_calculate(data, do_what: str):
    output = hpyc.output if do_what == "output" else hpyc.write  # 输出内容只需要用output就好了
