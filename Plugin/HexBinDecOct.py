import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': '0',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)
    'id': 'HexBinDecOct',  # ID，插件标识符，需要和文件名一致
    'option_name': "进制转换v1.0.0 by HowieHz",  # 选项名-在选择算法列表中
    'version': 'v1.0.0',  # 版本号

    'save_name': "进制转换",  # 文件保存项目名-在输出
    'quantifier': "",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "进制转换",  # 选择此项后输出的名字
    'author': "HowieHz",  # 作者(可选)
    'help': """
输入格式:
    需要转换的数字,输入的进制

    (输入的进制 -> 默认值10)
    (半角逗号分隔)
    
输入例:
    8,10
    8
    10,2
                    """,  # 帮助和说明(可选)
    'output_end': "",  # 输出小尾巴(可选)

    'output_mode': '3',
    # 具体说明和区别请看“output_mode参数讲解”一节
    # 调用类main的return形式，
    # 0为返回一次（适用于return字符串等情况），
    # 1为返回多次（适用于return列表等情况），
    # 2为返回多次（适用于return列表等情况，和1相似，但是每次输出不换行）,
    # （推荐）3无return返回值，要求插件作者放置保存和输出（性能最好，推荐使用，默认值）（要求插件作者自己写好保存和返回，计算调用main函数，保存调用main_save函数），
    # 4和三类似，但是只会调用main，且会传入第三个参数，第三个参数为'save'时表示为要输出到内屏，第三个参数为'output'时表示要保存
    'save_mode': '1',  # 保存名的形式，0为 时间+算法名+输入+量词  1为 时间+输入+“的”+算法名
    # 如果是1，则self.quantifier无效化
    "fullwidth_symbol": '0'  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def main(input:str, self):  # 输出到框体内
    try:
        num,b=input.split(',')
    except Exception:
        num=input
        b="10"
    if b == "2":
        num=int(num,2)
    elif b == "8":
        num=int(num,8)
    elif b == "10":
        num=int(num)
    elif b == "16":
        num=int(num,16)
    else:
        hpyc.output(self,"目前不支持该进制的输入\n\n*做信息题是吧，自己算")
        return

    hpyc.output(self,"二进制："+str(bin(num))[2:])
    hpyc.output(self,"八进制：" + str(oct(num))[2:])
    hpyc.output(self,"十进制：" + str(num))
    hpyc.output(self,"十六进制：" + str(hex(num))[2:].upper())
    return




def main_save(input, file):  # 保存到文件
    return