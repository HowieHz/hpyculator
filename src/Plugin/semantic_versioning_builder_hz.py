import hpyculator as hpyc
from typing import Optional

VERSION = "V1.0.1"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,
    "id": "semantic_versioning_builder_hz",  # ID,插件标识符,需要和文件名一致（必须）
    "option": f"语义化版本生成器 {VERSION} by HowieHz",  # 选项名-在选择算法列表中（必须）
    "version": VERSION,  # 版本号（必须）
    "tag": ["category:Other"],
    "save_name": "语义化版本",  # 文件保存项目名-在输出（必须）
    "quantifier": "",  # 文件保存量词-在输入后面(可选)
    "output_start": "",  # 输出头(可选)
    "output_name": "语义化版本生成器",  # 选择此项后输出的名字（必须）
    "author": "HowieHz",  # 作者(可选)
    "help": """
    关于语义化版本请看https://semver.org/lang/zh-CN/

输入格式
    a.b.c,d.e.f
    （半角逗号 或 全角逗号 或空格 分隔 起始值 和 终值,半角句号分隔主次版本号）
    其中
    a.b.c和d.e.f为语义化版本

    0 <= b,e <= 9
    0 = c,f <= 9
    a<=d

    当a=d，要求b<=e
    当a=d,b=e，要求c<=f

输出格式
    a.b.c到d.e.f（包括a.b.c和d.e.f）的语义化版本

输入样例
    1.0.0,2.0.0
    1.0.0，2.0.0
    1.0.0 2.0.0

吐槽
    用了两个半小时，用生成器写了一遍，和原来的相比(跑了20000次),平均每次快0.0001340595s，
    我突然意识到了 zen of 算法优化，
    空间可以换时间
    我的时间换程序运行时间

    可传入第三个参数 mode2 来使用原本的（非生成器）的函数
    """,  # 帮助和说明(可选)
    "output_end": "",  # 输出小尾巴(可选)
    "output_mode": hpyc.RETURN_ONCE,
    "save_mode": hpyc.OFF,
    "fullwidth_symbol": hpyc.OFF,
}


def on_calculate(inp: str) -> list | str:
    """计算函数"""
    for pattern in [",", "，", " "]:
        if pattern in data:
            a, b, mode, *_ = inp.split(pattern)
            break
    else:
        return "请按格式输入！！！"
    if mode == "mode2":
        list_data = []
        aq, aw, ae = map(str, a.split("."))
        bq, bw, be = map(str, b.split("."))
        a = int(aq + aw + ae)
        b = int(bq + bw + be)
        listc = range(a, b + 1)
        for i in listc:
            list_data.append(i)
        for i in range(0, len(listc)):
            q = int(list_data[i]) // 100  # 百位
            w = int(list_data[i]) // 10 % 10  # 十位
            e = int(list_data[i]) % 10  # 个位
            list_data[i] = str(q) + "." + str(w) + "." + str(e)
        return list_data

    aq, aw, ae = map(int, a.split("."))
    bq, bw, be = map(int, b.split("."))
    if aq == bq:
        if aw == bw:
            if ae == be:  # 1.2.2-1.2.2
                return [".".join((str(aq), str(aw), str(ae)))]
            # 1.2.x-1.2.y
            return [
                ".".join((str(x), str(y), str(z)))
                for x in range(aq, aq + 1)
                for y in range(bw, bw + 1)
                for z in range(ae, be + 1)
            ]
        return (  # 1.2.x-1.6.y 1.2.x-1.2.9 1.3.0-1.5.9 1.6.0-1.6.y
            [
                ".".join((str(x), str(y), str(z)))
                for x in range(aq, aq + 1)
                for y in range(aw, aw + 1)
                for z in range(ae, 10)
            ]
            + [
                ".".join((str(x), str(y), str(z)))
                for x in range(aq, aq + 1)
                for y in range(aw + 1, bw)
                for z in range(0, 10)
            ]
            + [
                ".".join((str(x), str(y), str(z)))
                for x in range(aq, aq + 1)
                for y in range(bw, bw + 1)
                for z in range(0, be + 1)
            ]
        )
        # 1.2.x-1.2.9
        # 1.3.0-1.5.9
        # 1.6.0-1.6.y
    return (  # 1.x.x-3.y.y
        [
            ".".join((str(x), str(y), str(z)))
            for x in range(aq, aq + 1)
            for y in range(aw, aw + 1)
            for z in range(ae, 10)
        ]
        + [
            ".".join((str(x), str(y), str(z)))
            for x in range(aq, aq + 1)
            for y in range(aw + 1, 10)
            for z in range(0, 10)
        ]
        + [
            ".".join((str(x), str(y), str(z)))
            for x in range(aq + 1, bq)
            for y in range(0, 10)
            for z in range(0, 10)
        ]
        + [
            ".".join((str(x), str(y), str(z)))
            for x in range(bq, bq + 1)
            for y in range(0, bw)
            for z in range(0, 10)
        ]
        + [
            ".".join((str(x), str(y), str(z)))
            for x in range(bq, bq + 1)
            for y in range(bw, bw + 1)
            for z in range(0, be + 1)
        ]
    )
    # 1.3.5-1.3.9 a! b! c!
    # 1.4.0-1.9.9 a! b! c!
    # 2.0.0-2.9.9 a! b! c!
    # 3.0.0-3.4.9 a= b! c!
    # 3.5.0-3.5.6 a= b= c!
