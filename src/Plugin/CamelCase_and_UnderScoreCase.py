import hpyculator as hpyc

PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "CamelCase_and_UnderScoreCase",  # ID,插件标识符,需要和文件名一致（必须）
    "option_name": "下划线驼峰转换器 V1.0.1 by HowieHz",  # 选项名-在选择算法列表中（必须）
    "version": "V1.0.1",  # 版本号（必须）
    "save_name": "转换结果",  # 文件保存项目名-在输出（必须）
    "quantifier": "",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": "下划线驼峰转换器",  # 选择此项后输出的名字（必须）
    "author": "HowieHz",  # 作者(可选)
    "help": """
数据模式表：
0 -> 下划线 例hello_world
1 -> 小驼峰 例helloWorld
2 -> 大驼峰 帕斯卡命名法 例HelloWorld
3 -> 全大写+下划线 例NEVER_GIVE_UP

输入格式
    要转换的字符串,输入数据模式,输出数据模式
    （半角逗号分隔）

输出格式
    转换后的字符串

    """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "use_quantifier": hpyc.ON,
    "fullwidth_symbol": hpyc.OFF,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def on_calculate(data, todo):
    """计算函数"""
    text, input_mode, output_mode = data.split(",")
    text_list = []  # 存放单词组
    if input_mode == "0":
        text_list = str(text).split("_")
        # print(text_list)
    elif input_mode == "1":
        text_list_single = []
        text_uppercase_index = []
        text_list = []
        for i in text:
            text_list_single.append(i)
        for index, text_list_single_data in enumerate(text_list_single):
            if "A" <= text_list_single_data <= "Z":
                text_uppercase_index.append(index)
        text_uppercase_index.append(len(text_list_single))
        before_uppercase_index = 0
        for uppercase_index in text_uppercase_index:
            word = "".join(text_list_single[before_uppercase_index:uppercase_index])
            text_list.append(word)
            before_uppercase_index = uppercase_index
    elif input_mode == "2":
        text_list_single = []
        text_uppercase_index = []
        text_list = []
        for i in text:
            text_list_single.append(i)
        for index, text_list_single_data in enumerate(text_list_single):
            if "A" <= text_list_single_data <= "Z":
                text_uppercase_index.append(index)
        text_uppercase_index.append(len(text_list_single))
        before_uppercase_index = 0
        for uppercase_index in text_uppercase_index:
            word = "".join(text_list_single[before_uppercase_index:uppercase_index])
            text_list.append(word)
            before_uppercase_index = uppercase_index
        if text_list[0] == "":
            text_list = text_list[1:]
    elif input_mode == "3":
        text_list = str(text).split("_")
    else:
        pass
    text = ""
    if output_mode == "0":
        for i in text_list:
            text += i.lower() + "_"
        text = text[:-1]
    elif output_mode == "1":
        text += text_list[0].lower()
        for i in text_list[1:]:
            text += i.capitalize()
    elif output_mode == "2":
        for i in text_list:
            text += i.capitalize()
    elif output_mode == "3":
        for i in text_list:
            text += i.upper() + "_"
        text = text[:-1]
    else:
        pass
    if todo == "output":
        hpyc.output(text)
    else:
        hpyc.write(text)
