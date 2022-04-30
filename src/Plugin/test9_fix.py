import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': hpyc.STRING,  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)
    # self.input_box_amount=1 #输入框数量
    'id': 'test9_fix',  # ID,插件标识符
    'option_name': "tset⑨_fixV1.0.2 by HowieHz",  # 选项名-在选择算法列表中
    'version': 'V1.0.2',  # 版本号
    'save_name': "tset⑨",  # 文件保存项目名-在输出
    'quantifier': "",  # 文件保存量词-在输入后面
    'output_start': "",  # 输出头
    'output_name': "test⑨",
    'author': "HowieHz",
    'help': """
    输入n，输出n个⑨
    
    不满一个的⑨就会被uuz吃掉
""",
    'output_end': "",
    'return_mode': hpyc.NO_RETURN,
    'use_quantifier' : hpyc.ON
}

def main(input,self):#调用时传入两个参数，第一个参数是输入，第二个参数是程序的主类，要作为输出函数的的第一个参数\
    hpyc.output(self, "勾个输出优化吧，谢谢")
    return
    """num = input
    num = int(num)
    need_write = ""
    need_write_len = 0
    for i in range(num):
        need_write += "⑨\n"
        need_write_len += 1
        if need_write_len >= 100000000:
            hpyc.output(self, need_write)
            need_write = ""
            need_write_len = 0
    hpyc.output(self, need_write)
    return"""

def main_save(input,file):#返回一个字符串，第一个参数是输入，第二个参数是需要被保存的文件流，要作为保存函数的第一个参数
    num =input
    num = int(num)
    need_write=""
    need_write_len=0
    for i in range(num):
        need_write+="⑨\n"
        need_write_len+=1
        if need_write_len >= 100000000:
            hpyc.write_without_flush(file, need_write)
            hpyc.flush(file)
            need_write=""
            need_write_len=0
    hpyc.write(file, need_write)
    return