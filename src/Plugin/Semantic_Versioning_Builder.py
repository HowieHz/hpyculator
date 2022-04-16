import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': '0',  # 输入模式，0为传入字符串 1位传入float(传入的作为main函数的开始计算值)（必须）
    'id': 'Semantic_Versioning_Builder',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "语义化版本生成器 V1.0.0 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'V1.0.0',  # 版本号（必须）

    'save_name': "语义化版本",  # 文件保存项目名-在输出（必须）
    'quantifier': "",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "语义化版本生成器",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """
    关于语义化版本请看https://semver.org/lang/zh-CN/
    
输入格式
    a.b.c,d.e.f
    （半角逗号,半角句号分隔）
    其中
    a.b.c和d.e.f为语义化版本
    
    0 <= b,e <= 9
    0 = c,f <= 9
    a<=d
    
    当a=d，要求b<=e
    当a=d,b=e，要求c<=f

输出格式
    a.b.c到d.e.f（包括a.b.c和d.e.f）的语义化版本

吐槽
    用了两个半小时，用生成器写了一遍，和原来的相比(跑了20000次),平均每次快0.0001340595s，
    我突然意识到了 zen of 算法优化，
    空间可以换时间
    我的时间换程序运行时间
    
    可传入第三个参数 wdnmd 来使用原本的（非生成器）的函数
    """,  # 帮助和说明(可选)
    'output_end': "",  # 输出小尾巴(可选)

    'output_mode': '0',
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


def main(input:str):
    try:
        a, b, c = input.split(",")
    except Exception as e:
        c = ""
        a, b = input.split(",")
    if c == "wdnmd":
        list = []
        aq, aw, ae = map(str, a.split("."))
        bq, bw, be = map(str, b.split("."))
        a = int(aq + aw + ae)
        b = int(bq + bw + be)
        listc = range(a, b + 1)
        for i in listc:
            list.append(i)
        for i in range(0, len(list)):
            q = int(list[i]) // 100  # 百位
            w = int(list[i]) // 10 % 10  # 十位
            e = int(list[i]) % 10  # 个位
            list[i] = str(q) + "." + str(w) + "." + str(e)
        return list

    a,b=input.split(",")
    aq, aw, ae = map(int, a.split("."))
    bq, bw, be = map(int, b.split("."))
    if aq == bq:
        if aw == bw:
            if ae == be:  # 1.2.2-1.2.2
                return ['.'.join((str(aq), str(aw), str(ae)))]
            else:  # 1.2.x-1.2.y
                return ['.'.join((str(x), str(y), str(z))) for x in range(aq, aq + 1) for y in range(bw, bw + 1) for z
                        in
                        range(ae, be + 1)]
        else:  # 1.2.x-1.6.y 1.2.x-1.2.9 1.3.0-1.5.9 1.6.0-1.6.y
            return ['.'.join((str(x), str(y), str(z))) for x in range(aq, aq + 1) for y in range(aw, aw + 1) for z in
                    range(ae, 10)] + \
                   ['.'.join((str(x), str(y), str(z))) for x in range(aq, aq + 1) for y in range(aw + 1, bw) for z in
                    range(0, 10)] + \
                   ['.'.join((str(x), str(y), str(z))) for x in range(aq, aq + 1) for y in range(bw, bw + 1) for z in
                    range(0, be + 1)]
            # 1.2.x-1.2.9
            # 1.3.0-1.5.9
            # 1.6.0-1.6.y
    else:  # 1.x.x-3.y.y
        return ['.'.join((str(x), str(y), str(z))) for x in range(aq, aq + 1) for y in range(aw, aw + 1) for z in
                range(ae, 10)] + \
               ['.'.join((str(x), str(y), str(z))) for x in range(aq, aq + 1) for y in range(aw + 1, 10) for z in
                range(0, 10)] + \
               ['.'.join((str(x), str(y), str(z))) for x in range(aq + 1, bq) for y in range(0, 10) for z in
                range(0, 10)] + \
               ['.'.join((str(x), str(y), str(z))) for x in range(bq, bq + 1) for y in range(0, bw) for z in
                range(0, 10)] + \
               ['.'.join((str(x), str(y), str(z))) for x in range(bq, bq + 1) for y in range(bw, bw + 1) for z in
                range(0, be + 1)]

        # 1.3.5-1.3.9 a! b! c!
        # 1.4.0-1.9.9 a! b! c!
        # 2.0.0-2.9.9 a! b! c!
        # 3.0.0-3.4.9 a= b! c!
        # 3.5.0-3.5.6 a= b= c!