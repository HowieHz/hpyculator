import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': '0',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)（必须）
    'id': 'CamelCase_and_UnderScoreCase',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "下划线驼峰转换器 V1.0.0 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'V1.0.0',  # 版本号（必须）

    'save_name': "转换结果",  # 文件保存项目名-在输出（必须）
    'quantifier': "",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "下划线驼峰转换器",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """
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
    'output_end': "",  # 输出小尾巴(可选)

    'output_mode': '',
    # 调用类main的return形式，
    # 0为返回一次（适用于return字符串等情况），
    # 1为返回多次（适用于return列表等情况），
    # 2为返回多次（适用于return列表等情况，和1相似，但是每次输出不换行）,
    # （推荐）3无return返回值，要求插件作者放置保存和输出（性能最好，推荐使用，默认值）（要求模块自己写好保存和返回，计算调用main函数，保存调用main_save函数），
    # 4和三类似，但是只会调用main，且会传入第三个参数，第三个参数为'save'时表示为要输出到内屏，第三个参数为'output'时表示要保存
    'save_mode': '1',  # 保存名的形式，0为 时间+算法名+输入+量词  1为 时间+输入+“的”+算法名（必须）
    # 回文质数第5项(第1-5项)   51,12,31,45的方差（未加入特性）
    # 如果是1，则self.quantifier无效化
    "fullwidth_symbol": '0'  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}

def main(input,self):
    text,input_mode,output_mode=input.split(",")
    print("text:",text)
    print("input_mode:", input_mode)
    print("output_mode:", output_mode)
    if input_mode == "0":
        text_list=str(text).split('_')
        print(text_list)
    elif input_mode =="1":
        text_list_single=[]
        text_uppercase_index = []
        text_list=[]
        for i in text:
            text_list_single.append(i)
        for index in range(0,len(text_list_single)):
            if "A"<= text_list_single[index] <="Z":
                text_uppercase_index.append(index)
        text_uppercase_index.append(len(text_list_single))
        before_uppercase_index = 0
        for uppercase_index in text_uppercase_index:
            word=""
            for single in text_list_single[before_uppercase_index:uppercase_index]:
                word+=single
            text_list.append(word)
            before_uppercase_index=uppercase_index
    elif input_mode =="2":
        text_list_single = []
        text_uppercase_index = []
        text_list = []
        for i in text:
            text_list_single.append(i)
        for index in range(0, len(text_list_single)):
            if "A" <= text_list_single[index] <= "Z":
                text_uppercase_index.append(index)
        text_uppercase_index.append(len(text_list_single))
        before_uppercase_index = 0
        for uppercase_index in text_uppercase_index:
            word = ""
            for single in text_list_single[before_uppercase_index:uppercase_index]:
                word += single
            text_list.append(word)
            before_uppercase_index = uppercase_index
        if text_list[0]=="":
            text_list=text_list[1:]
    elif input_mode == "3":
        text_list = str(text).split('_')
    else:
        pass
    print(text_list)
    text=""
    if output_mode == "0":
        for i in text_list:
            text+=(i.lower()+"_")
        text=text[:-1]
    elif output_mode == "1":
        text+=text_list[0].lower()
        for i in text_list[1:]:
            text+=i.capitalize()
    elif output_mode == "2":
        for i in text_list:
            text+=i.capitalize()
    elif output_mode == "3":
        for i in text_list:
            text+=(i.upper()+"_")
        text = text[:-1]
    else:
        pass
    hpyc.output(self,text)

def main_save(input,filename):
    return