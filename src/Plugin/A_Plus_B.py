import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': hpyc.STRING,  # 输入模式
    'id': 'A_Plus_B',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "高精度整数加法 V1.1.0 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'V1.1.0',  # 版本号（必须）

    'save_name': "",  # 文件保存项目名-在输出（必须）
    'quantifier': "的答案",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "A+B Problem",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """
输入格式
    整数A,整数B

    例：1,2

输出格式
    N
    （N是A+B的和）

    """,  # 帮助和说明(可选)
    'output_end': "",  # 输出小尾巴(可选)

    'return_mode': hpyc.NO_RETURN,
    'use_quantifier': hpyc.OFF,
    "fullwidth_symbol": hpyc.OFF
}

def main(input:str,self) -> None:
    a,b=input.split(",")
    a = int(a)
    b = int(b)
    hpyc.output(self,a+b)

def main_save(input:str,filename) -> None:
    a, b = input.split(",")
    a=int(a)
    b=int(b)
    hpyc.write(filename,a+b)

def main_test(input:str,self) -> int:
    a, b = input.split(",")
    a=int(a)
    b=int(b)
    return a+b
