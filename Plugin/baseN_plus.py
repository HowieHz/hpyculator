import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': '0',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)（必须）
    'id': 'baseN_plus',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "n进制加法v1.2.0 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'v1.2.0',  # 版本号（必须）

    'save_name': "",  # 文件保存项目名-在输出（必须）
    'quantifier': "",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """

    给定两个 C（2≤C≤64）进制数 A,B,输出A+B，输出的数是个C进制数
    
    0到63映射表：0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_
    部分进制数位范围：2(0-1)，8(0-7)，10(0-9)，16(0-9a-f)，32(0-9a-v)，58(0-9a-zA-V)，62(0-9a-zA-Z)，64(0-9a-zA-Z和-_)
    
输入格式
    A,B,C

输出格式
    N

输入输出样例
    输入 #1
        10,10,10

    输出 #1
        20
        
    输入 #2
        63,63,64

    输出 #2
        c6
        
    输入 #3
        89,89ac,16
        
    输出 #3
        8a35
            """,  # 帮助和说明(可选)
    'output_end': "",  # 输出小尾巴(可选)

    'output_mode': '4',
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

def main(input:str, self,todo) -> None:  # 输出到框体内
    num_rep_to = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_"
    num_rep_from={
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'a':10,
        'b':11,
        'c':12,
        'd':13,
        'e':14,
        'f':15,
        'g':16,
        'h':17,
        'i':18,
        'j':19,
        'k':20,
        'l':21,
        'm':22,
        'n':23,
        'o':24,
        'p':25,
        'q':26,
        'r':27,
        's':28,
        't':29,
        'u':30,
        'v':31,
        'w':32,
        'x':33,
        'y':34,
        'z':35,
        'A':36,
        'B':37,
        'C':38,
        'D':39,
        'E':40,
        'F':41,
        'G':42,
        'H':43,
        'I':44,
        'J':45,
        'K':46,
        'L':47,
        'M':48,
        'N':49,
        'O':50,
        'P':51,
        'Q':52,
        'R':53,
        'S':54,
        'T':55,
        'U':56,
        'V':57,
        'W':58,
        'X':59,
        'Y':60,
        'Z':61,
        '-':62,
        '_':63,}
    a,b,c=input.strip().split(",")
    n = int(c.strip())  # n是多少进制

    if n>36:#小于36的直接int，大于36小于64的解析
        a_list = list(map(lambda x: num_rep_from[x], list(a.strip())))
        b_list = list(map(lambda x: num_rep_from[x], list(b.strip())))
    else:
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

    aw_list = a_list[:]#翻转list，左高位右低位
    aw_list.reverse()
    if n>10:#把大于10的位转换为a-zA-Z-_
        for i in range(0,len(aw_list)):
            num=int(aw_list[i])
            if num>9:
                aw_list[i]=num_rep_to[num]
    else:
        pass

    aw = ""
    for i in aw_list:#列表转换为字符串
        aw+=i

    if todo=="output":
        hpyc.output(self,aw)
    else:
        hpyc.write(self,aw)