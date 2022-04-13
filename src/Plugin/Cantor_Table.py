import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': '1',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)（必须）
    'id': 'Cantor_Table',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "Cantor表_fixV1.0.1 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'V1.0.1',  # 版本号（必须）

    'save_name': "Cantor表前",  # 文件保存项目名-在输出（必须）
    'quantifier': "项",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "Cantor表",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """
    这里引用一下洛谷OJ对Cantor表的介绍
    https://www.luogu.com.cn/problem/P1014
    
    现代数学的著名证明之一是 Georg Cantor 证明了有理数是可枚举的。他是用下面这一张表来证明这一命题的：

    1/1, 1/2, 1/3,1/4,1/5, …
    2/1, 2/2, 2/3,2/4, …
    3/1, 3/2, 3/3, …
    4/1, 4/2, …
    5/1, …
    …

    我们以 Z 字形给上表的每一项编号。第一项是 1/1，然后是 1/2，2/1，3/1，2/2，…

输入格式
    整数N（1≤N)

输出格式
    表中的前 N 项
    
    哈哈，把自己的题解拿来用了""",  # 帮助和说明(可选)
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
    "fullwidth_symbol": '1'  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}

def main(n,self,do_what):
    if do_what == "output":
        a = 1
        b = 1
        if n >= 1:
            hpyc.output(self,"1/1")
        for i in range(1, n):
            if a == 1:
                if b % 2 == 0:
                    b -= 1
                    a += 1
                    hpyc.output(self, str(a) + "/" + str(b))
                    continue
                else:
                    b += 1
                    hpyc.output(self, str(a) + "/" + str(b))
                    continue
            if b == 1:
                if a % 2 == 0:
                    a += 1
                    hpyc.output(self, str(a) + "/" + str(b))
                    continue
                else:
                    a -= 1
                    b += 1
                    hpyc.output(self, str(a) + "/" + str(b))
                    continue
            if a % 2 == 0:
                if b % 2 == 0:
                    a -= 1
                    b += 1
                    hpyc.output(self, str(a) + "/" + str(b))
                    continue
                else:
                    a += 1
                    b -= 1
                    hpyc.output(self, str(a) + "/" + str(b))
                    continue
            else:
                if b % 2 == 0:  # 向xia
                    a += 1
                    b -= 1
                    hpyc.output(self, str(a) + "/" + str(b))
                    continue
                else:
                    a -= 1
                    b += 1
                    hpyc.output(self, str(a) + "/" + str(b))
                    continue

    else:
        a = 1
        b = 1
        len = 0
        if n >= 1:
            hpyc.write_without_flush(self,"1/1")
        for i in range(1, n):
            if len >= 5000000:
                hpyc.flush()
            if a == 1:
                if b % 2 == 0:
                    b -= 1
                    a += 1
                    hpyc.write_without_flush(self, str(a) + "/" + str(b))
                    len+=1
                    continue
                else:
                    b += 1
                    hpyc.write_without_flush(self, str(a) + "/" + str(b))
                    len += 1
                    continue
            if b == 1:
                if a % 2 == 0:
                    a += 1
                    hpyc.write_without_flush(self, str(a) + "/" + str(b))
                    len += 1
                    continue
                else:
                    a -= 1
                    b += 1
                    hpyc.write_without_flush(self, str(a) + "/" + str(b))
                    len += 1
                    continue
            if a % 2 == 0:
                if b % 2 == 0:
                    a -= 1
                    b += 1
                    hpyc.write_without_flush(self, str(a) + "/" + str(b))
                    len += 1
                    continue
                else:
                    a += 1
                    b -= 1
                    hpyc.write_without_flush(self, str(a) + "/" + str(b))
                    len += 1
                    continue
            else:
                if b % 2 == 0:  # 向xia
                    a += 1
                    b -= 1
                    hpyc.write_without_flush(self, str(a) + "/" + str(b))
                    len += 1
                    continue
                else:
                    a -= 1
                    b += 1
                    hpyc.write_without_flush(self, str(a) + "/" + str(b))
                    len += 1
                    continue