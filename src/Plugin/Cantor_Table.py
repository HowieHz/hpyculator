import hpyculator as hpyc

PLUGIN_METADATA = {
    "input_mode": hpyc.NUM,
    "id": "Cantor_Table",  # ID,插件标识符,需要和文件名一致（必须）
    "option_name": "Cantor表_fixV1.0.1 by HowieHz",  # 选项名-在选择算法列表中（必须）
    "version": "V1.0.1",  # 版本号（必须）
    "save_name": "Cantor表前",  # 文件保存项目名-在输出（必须）
    "quantifier": "项",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": "Cantor表",  # 选择此项后输出的名字（必须）
    "author": "HowieHz",  # 作者(可选)
    "help": """
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
    "output_end": "",  # 输出小尾巴(可选)
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "use_quantifier": hpyc.ON,
    "fullwidth_symbol": hpyc.ON,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def on_calculate(n, do_what):
    """计算函数"""
    if do_what == "output":
        a = 1
        b = 1
        if n >= 1:
            hpyc.output("1/1")
        for _ in range(n-1):
            if a == 1:
                if b % 2 == 0:
                    b -= 1
                    a += 1
                    hpyc.output(str(a) + "/" + str(b))
                    continue
                b += 1
                hpyc.output(str(a) + "/" + str(b))
                continue
            if b == 1:
                if a % 2 == 0:
                    a += 1
                    hpyc.output(str(a) + "/" + str(b))
                    continue
                a -= 1
                b += 1
                hpyc.output(str(a) + "/" + str(b))
                continue
            if a % 2 == 0:
                if b % 2 == 0:
                    a -= 1
                    b += 1
                    hpyc.output(str(a) + "/" + str(b))
                    continue
                a += 1
                b -= 1
                hpyc.output(str(a) + "/" + str(b))
                continue
            if b % 2 == 0:  # 向xia
                a += 1
                b -= 1
                hpyc.output(str(a) + "/" + str(b))
                continue
            a -= 1
            b += 1
            hpyc.output(str(a) + "/" + str(b))
            continue

    else:
        a = 1
        b = 1
        buffer_len = 0
        if n >= 1:
            hpyc.write_without_flush("1/1")
        for _ in range(n-1):
            if buffer_len >= 5000000:
                hpyc.flush()
            if a == 1:
                if b % 2 == 0:
                    b -= 1
                    a += 1
                    hpyc.write_without_flush(str(a) + "/" + str(b))
                    buffer_len += 1
                    continue
                b += 1
                hpyc.write_without_flush(str(a) + "/" + str(b))
                buffer_len += 1
                continue
            if b == 1:
                if a % 2 == 0:
                    a += 1
                    hpyc.write_without_flush(str(a) + "/" + str(b))
                    buffer_len += 1
                    continue
                a -= 1
                b += 1
                hpyc.write_without_flush(str(a) + "/" + str(b))
                buffer_len += 1
                continue
            if a % 2 == 0:
                if b % 2 == 0:
                    a -= 1
                    b += 1
                    hpyc.write_without_flush(str(a) + "/" + str(b))
                    buffer_len += 1
                    continue
                a += 1
                b -= 1
                hpyc.write_without_flush(str(a) + "/" + str(b))
                buffer_len += 1
                continue
            if b % 2 == 0:  # 向xia
                a += 1
                b -= 1
                hpyc.write_without_flush(str(a) + "/" + str(b))
                buffer_len += 1
                continue
            a -= 1
            b += 1
            hpyc.write_without_flush(str(a) + "/" + str(b))
            buffer_len += 1
            continue
