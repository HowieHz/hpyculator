import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': '0',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)
    # self.input_box_amount=1 #输入框数量
    'id': 'test9_n',  # ID,插件标识符
    'option_name': "tset⑨_nV1.0.1 by HowieHz",  # 选项名-在选择算法列表中
    'version': 'V1.0.1',  # 版本号
    'save_name': "tset⑨",  # 文件保存项目名-在输出
    'quantifier': "",  # 文件保存量词-在输入后面
    'output_start': "",  # 输出头
    'output_name': "test⑨",
    'author': "HowieHz",  # 作者
    'help': """
    输入n，输出n个⑨
    
    不满一个的⑨就会被uuz吃掉
""",  # 帮助和说明
    # self.output_init=""#选择后默认输出
    'output_end': "",  # 输出小尾巴
    'output_mode': '3',
    # 调用类main的return形式，
    # 0为返回一次（适用于return字符串等情况），
    # 1为返回多次（适用于return列表等情况），
    # 2为返回多次（适用于return列表等情况，和1相似，但是每次输出不换行）,
    # （推荐）3无return返回值，要求插件作者放置保存和输出（性能最好，推荐使用，默认值）（要求模块自己写好保存和返回，计算调用main函数，保存调用main_save函数），
    # 4和三类似，但是只会调用main，且会传入第三个参数，第三个参数为'save'时表示为要输出到内屏，第三个参数为'output'时表示要保存
    'save_mode': '1'  # 保存名的形式，0为 时间+算法名+输入+量词  1为 时间+输入+“的”+算法名
    # 回文质数第5项(第1-5项)   51,12,31,45的方差
    # 如果是1，则self.quantifier无效化
    # save_mode,output_mode,input_mode的值为int
}

def main(input,self):#调用时传入两个参数，第一个参数是输入，第二个参数是程序的主类，要作为输出函数的的第一个参数\
    num=input
    num=int(num)
    for i in range(num):
        hpyc.output(self,"⑨")
    return

def main_save(input,file):#返回一个字符串，第一个参数是输入，第二个参数是需要被保存的文件流，要作为保存函数的第一个参数
    num =input
    num = int(num)
    for i in range(num):
        hpyc.write(file,"⑨")
    return