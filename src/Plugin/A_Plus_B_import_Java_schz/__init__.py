"""太好了，pj共荣"""
import os

import hpyculator as hpyc
import jpype

NAME = "高精度浮点数加法(基于Java)"
VERSION = "V1.0.4"
AUTHOR = ["shacha086", "HowieHz"]
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "A_Plus_B_import_Java_schz",  # ID,插件标识符,需要和文件名一致（必须）
    # 选项名-在选择算法列表中（必须）
    "option": f"{NAME}{VERSION} by {', '.join(AUTHOR) if isinstance(AUTHOR,list) else AUTHOR}",
    "version": VERSION,  # 版本号（必须）
    "tag": [
        "category:Mathematical-calculations",
        "computer_language:java",
        "depend:jpype",
    ],
    "save_name": "",  # 文件保存项目名-在输出（必须）
    "quantifier": "相加所得",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": NAME,  # 选择此项后输出的名字（必须）
    "author": AUTHOR,  # 作者(可选)
    "help": """
输入格式
    A,B

输出格式
    N
    （N是A+B的和）

输入样例
    例1：1,2
    例2：-1，2.2
    例3：12345678 -2.123123

注：
    本插件基于java8构建

shacha086构建了计算核心
HowieHz构建了插件化的部分
    """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.OFF,
}

r"""
改成jdk8构建了，这个懒得再打一遍了，先放在这
    注：
    本插件基于jdk17构建
    C:\Program Files\Java\jdk-17.0.2\bin\server\jvm.dll为默认地址
    如此地址无jdk17，请传入第三个参数（用逗号分隔），第三个参数为\jdk-17.0.2\bin\server\jvm.dll的绝对地址
    """


def on_calculate(data: str, todo: str):
    """计算函数"""
    for pattern in [",", "，", " "]:
        if pattern in data:
            a, b, *_ = data.split(pattern)
            break
    else:
        hpyc.output("请按格式输入！！！")
        return
    jar_path = str(os.path.abspath(__file__))[:-11] + "A+Bproj.jar"
    jvm_path = jpype.getDefaultJVMPath()
    if not jpype.isJVMStarted():
        jpype.startJVM(
            jvm_path, "-ea", "-Djava.class.path=%s" % jar_path, convertStrings=False
        )
    if todo == "output":
        hpyc.output(jpype.JClass("com.shacha.Main").main(a, b))
    else:
        hpyc.write(jpype.JClass("com.shacha.Main").main(a, b))
