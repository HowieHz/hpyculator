import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': hpyc.STRING,
    'id': 'Heron_s_Formula',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "海伦公式求三角形面积V1.0.1 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'V1.0.1',  # 版本号（必须）

    'save_name': "为边长的三角形的面积",  # 文件保存项目名-在输出（必须）
    'quantifier': "",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "海伦公式求三角形面积",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """
输入格式
    实数A,实数B,实数C
    三个数据用半角逗号隔开
    
    例:3,4,5

输出格式
    以A,B,C为边长的三角形的面积。
    
   """,  # 帮助和说明(可选)
    'output_end': "",  # 输出小尾巴(可选)

    'return_mode': hpyc.NO_RETURN_SINGLE_FUNCTION,
    'use_quantifier': hpyc.ON,
    "fullwidth_symbol": hpyc.OFF
}


def on_calculate(num: str, do_what,file ):  # 返回一个列表
    try:
        a, b, c = num.split(",")
    except:
        hpyc.output("请按格式输入！！！")
        return
    a = int(a)
    b = int(b)
    c = int(c)
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    if do_what == "output":
        hpyc.output("以" + str(a) + "," + str(b) + "," + str(c) + "为边长的三角形的面积是:\n" + str(s))
    if do_what == "save":
        hpyc.write(file, str(s))
