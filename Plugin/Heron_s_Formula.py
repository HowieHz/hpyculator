PLUGIN_METADATA = {
    'input_mode': '0',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)（必须）
    'id': 'Heron_s_Formula',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "海伦公式求三角形面积V1.0.0 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'V1.0.0',  # 版本号（必须）

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

    'output_mode': '4',
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

def main(num:str,self,do_what):#返回一个列表
    try:
        a,b,c = num.split(",")
    except:
        output(self, "请按格式输入！！！")
        return
    a=int(a)
    b=int(b)
    c=int(c)
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    if do_what == "output":
        output(self,"以"+str(a) +","+ str(b)+"," +str(c)+"为边长的三角形的面积是:\n"+str(s))
    if do_what == "save":
        write(self,str(s))


def write(file, anything, end="\n"):
    file.write(str(anything) + end)
    file.flush()


def write_without_flush(file, anything, end="\n"):
    file.write(str(anything) + end)


def flush(file):
    file.flush()


def output(self, anything, end="\n"):
    self.output.AppendText(str(anything) + end)