from hpyculator import hpycore as hpyc

PLUGIN_METADATA = {
    'input_mode': hpyc.STRING,
    'id': 'P1015_Palindromes',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "P1015 [NOIP1999 普及组] 回文数 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': '？？？',  # 版本号（必须）

    'save_name': "P1015_out",  # 文件保存项目名-在输出（必须）
    'quantifier': "",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "P1015 [NOIP1999 普及组] 回文数",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """
转自洛谷OJ https://www.luogu.com.cn/problem/P1015

题目描述
    若一个数（首位不为零）从左向右读与从右向左读都一样，我们就将其称之为回文数。
    
    例如：给定一个十进制数 56，将 56 加 65（即把 56 从右向左读），得到 121 是一个回文数。
    
    又如：对于十进制数 87：
    
    STEP1：87+78=165
    STEP2：165+561=726
    STEP3：726+627=1353
    STEP4：1353+3531=4884
    
    在这里的一步是指进行了一次 N 进制的加法，上例最少用了 4 步得到回文数 4884。
    
    给定一个 N（2≤N≤10 或 N=16）进制数 M（100 位之内），求最少经过几步可以得到回文数。如果在 30 步以内（包含 30 步）不可能得到回文数，则输出 Impossible!。

输入格式
    N,M

输出格式
    如果能在 30 步以内得到回文数，输出格式形如 STEP=ans，其中 ans 为最少得到回文数的步数。

    否则输出 Impossible!。

输入输出样例
    输入 #1
        10,87
        
    输出 #1
        STEP=4
            """,  # 帮助和说明(可选)
    'output_end': "",  # 输出小尾巴(可选)

    'return_mode': hpyc.NO_RETURN,
    'save_mode': hpyc.OFF,
    "fullwidth_symbol": hpyc.OFF
}


def on_calculate(data: str):  # 输出到框体内
    o, p = data.strip().split(",")
    a = int(o.strip())  # a是多少进制
    b_list = list(map(lambda x: int(x, a), list(p.strip())))
    times = 0
    c_list = b_list[:]
    b_list.reverse()  # 左边是个位，右边是高位
    for _ in range(0, 30):
        if ishw(b_list):
            hpyc.output("STEP=" + str(times))
            return
        times += 1
        for i in range(0, len(b_list)):
            b_list[i] = str(int(c_list[i]) + int(b_list[i]))
            if int(b_list[i]) > (a - 1):
                b_list[i] = str(int(b_list[i]) - a)
                if i != (len(b_list) - 1):
                    b_list[i + 1] = str(int(b_list[i + 1]) + 1)
                else:
                    b_list.append("1")
        c_list = b_list[:]
        c_list.reverse()
    hpyc.output("Impossible!")


def ishw(list_data: list):
    if list_data == list_data[::-1]:
        return True
    else:
        return False


def on_calculate_with_save(data: str):
    o, p = data.strip().split(",")
    a = int(o.strip())  # a是多少进制
    b_list = list(map(lambda x: int(x, a), list(p.strip())))
    times = 0
    c_list = b_list[:]
    b_list.reverse()  # 左边是个位，右边是高位
    for _ in range(0, 30):
        if ishw(b_list):
            hpyc.write("STEP=" + str(times))
            return
        times += 1
        for i in range(0, len(b_list)):
            b_list[i] = str(int(c_list[i]) + int(b_list[i]))
            if int(b_list[i]) > (a - 1):
                b_list[i] = str(int(b_list[i]) - a)
                if i != (len(b_list) - 1):
                    b_list[i + 1] = str(int(b_list[i + 1]) + 1)
                else:
                    b_list.append("1")
        c_list = b_list[:]
        c_list.reverse()
    hpyc.write("Impossible!")
