import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': '0',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)（必须）
    'id': 'baseN_plus',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "n进制加法v1.0.0 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'v1.0.0',  # 版本号（必须）

    'save_name': "",  # 文件保存项目名-在输出（必须）
    'quantifier': "",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """

    给定两个 C（2≤C≤10 或 C=16）进制数 A,B（100 位之内）,输出A+B，输出的数是个C进制数

输入格式
    A,B,C

输出格式
    N

输入输出样例
    输入 #1
        10,10,10

    输出 #1
        20
            """,  # 帮助和说明(可选)
    'output_end': "",  # 输出小尾巴(可选)

    'output_mode': '3',
    # 调用类main的return形式，
    # 0为返回一次（适用于return字符串等情况），
    # 1为返回多次（适用于return列表等情况），
    # 2为返回多次（适用于return列表等情况，和1相似，但是每次输出不换行）,
    # （推荐）3无return返回值，要求插件作者放置保存和输出（性能最好，推荐使用，默认值）（要求模块自己写好保存和返回，计算调用main函数，保存调用main_save函数），
    # 4和三类似，但是只会调用main，且会传入第三个参数，第三个参数为'save'时表示为要输出到内屏，第三个参数为'output'时表示要保存
    'save_mode': '0',  # 保存名的形式，0为 时间+算法名+输入+量词  1为 时间+输入+“的”+算法名（必须）
    # 回文质数第5项(第1-5项)   51,12,31,45的方差（未加入特性）
    # 如果是1，则self.quantifier无效化
    "fullwidth_symbol": '0'  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}

def main(input:str, self):  # 输出到框体内
    num_rep = {10: 'a',
               11: 'b',
               12: 'c',
               13: 'd',
               14: 'e',
               15: 'f',
               16: 'g',
               17: 'h',
               18: 'i',
               19: 'j',
               20: 'k',
               21: 'l',
               22: 'm',
               23: 'n',
               24: 'o',
               25: 'p',
               26: 'q',
               27: 'r',
               28: 's',
               29: 't',
               30: 'u',
               31: 'v',
               32: 'w',
               33: 'x',
               34: 'y',
               35: 'z'}
    a,b,c=input.strip().split(",")
    n = int(c.strip())  # n是多少进制
    a_list = list(map(lambda x: int(x, n), list(a.strip())))
    b_list = list(map(lambda x: int(x, n), list(b.strip())))
    a_list.reverse()  # 左边是个位，右边是高位
    b_list.reverse()  # 左边是个位，右边是高位
    if len(a_list)>len(b_list):#a长就交换，a必须短
        a_list,b_list=b_list,a_list
    while True:
        if len(a_list)==len(b_list):
            break
        a_list.append("0")

    for i in range(0, len(b_list)):
        a_list[i] = str(int(a_list[i]) + int(b_list[i]))
        if int(a_list[i]) > (n - 1):
            a_list[i] = str(int(a_list[i]) - n)
            if i != (len(a_list) - 1):
                a_list[i + 1] = str(int(a_list[i + 1]) + 1)
            else:
                a_list.append("1")
    aw_list = a_list[:]
    aw_list.reverse()
    aw=""
    if n>10:
        for i in range(0,len(aw_list)):
            num=int(aw_list[i])
            if num>9:
                aw_list[i]=num_rep[num].upper()
        for i in aw_list:
            aw+=i
    else:
        for i in aw_list:
            aw+=i
    hpyc.output(self,aw)

def baseN(num,b):
  return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"[num % b])

