import os
import jpype
import hpyculator as hpyc

PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "A_Plus_B_import_Java",  # ID,插件标识符,需要和文件名一致（必须）
    "option_name": "A+B_Problem_with_Java V1.0.1 by shacha086,HowieHz",  # 选项名-在选择算法列表中（必须）
    "version": "V1.0.1",  # 版本号（必须）
    "save_name": "",  # 文件保存项目名-在输出（必须）
    "quantifier": "的答案",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": "A+B Problem",  # 选择此项后输出的名字（必须）
    "author": "shacha086,HowieHz",  # 作者(可选)
    "help": """
输入格式
    整数A,整数B

    例：1,2

输出格式
    N
    （N是A+B的和）

注：
    本项目基于java8构建

shacha086构建了计算核心
HowieHz构建了插件化的部分
    """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "use_quantifier": hpyc.OFF,
    "fullwidth_symbol": hpyc.OFF,
}

r"""
改成jdk8构建了，这个懒得再打一遍了，先放在这
    注：
    本插件基于jdk17构建
    C:\Program Files\Java\jdk-17.0.2\bin\server\jvm.dll为默认地址
    如此地址无jdk17，请传入第三个参数（用逗号分隔），第三个参数为\jdk-17.0.2\bin\server\jvm.dll的绝对地址
    """


def on_calculate(data, todo):
    """计算函数"""
    a, b = data.split(",")
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
    try:
        jpype.shutdownJVM()
    except:
        pass
