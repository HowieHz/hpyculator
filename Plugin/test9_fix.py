import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': '0',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)
    # self.input_box_amount=1 #输入框数量
    'id': 'test9_fix',  # ID,插件标识符
    'option_name': "tset⑨_fixV1.0.1 by HowieHz",  # 选项名-在选择算法列表中
    'version': 'V1.0.1',  # 版本号
    'save_name': "tset⑨",  # 文件保存项目名-在输出
    'quantifier': "",  # 文件保存量词-在输入后面
    'output_start': "",  # 输出头
    'output_name': "test⑨",
    'author': "HowieHz",
    'help': """
    test,输出几个⑨
""",
    'output_end': "",
    'output_mode': '3',
    'save_mode': '1'
}

def main(input,self):#调用时传入两个参数，第一个参数是输入，第二个参数是程序的主类，要作为输出函数的的第一个参数\
    num=input
    num=int(num)
    if num<=100000000:
        strings = "⑨\n" * num
        hpyc.output(self, strings)
    else:
        need_write = ""
        need_write_len = 0
        for i in range(num):
            need_write += "⑨\n"
            need_write_len += 1
            if need_write_len >= 100000000:
                hpyc.output(self, need_write)
                need_write=""
                need_write_len = 0
        for i in need_write:
            hpyc.output(self, need_write)
        need_write = None
    return

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
    for i in need_write:
        hpyc.write(file, need_write)
    need_write = None
    return