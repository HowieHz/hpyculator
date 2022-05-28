import hpyculator as hpyc
import numpy as np

NAME = "质数(素数)计算 (埃筛)"
AUTHOR = "HowieHz"
VERSION = "V1.0.0"
PLUGIN_METADATA = {
    # 输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
    "input_mode": hpyc.NUM,
    "id": "prime_hz",  # 插件标识符,需要和文件名一致
    "option": f"{NAME}{VERSION} by {AUTHOR}",  # 选项名-在选择算法列表中
    "version": VERSION,  # 版本号
    "tag": ["category:Mathematical calculations"],
    "save_name": "",  # 文件保存名
    "quantifier": "",  # 文件保存量词
    "output_start": "",  # 输出头
    "output_name": NAME,  # 选择此项后输出的名字
    "author": AUTHOR,  # 作者
    "help": """\
输入格式
    n(n为正整数且n>1)

输入样例
    1
                """,  # 帮助和说明
    "output_end": "",  # 输出小尾巴
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.OFF,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def on_calculate(data, do_what: str):
    output = hpyc.output if do_what == "output" else hpyc.write  # 输出内容只需要用output就好了
    if data < 2:
        output("")
        return
    prime = np.ones((data + 1,), dtype=np.bool_)
    for i in range(2, data + 1):
        if prime[i]:  # 这个数为True，说明是质数
            output(i)  # 输出质数
            new_i = i + i  # 下一个就是2i
            while new_i <= data:  # 没过终值就继续遍历
                prime[new_i] = False  # 扫描到的就是合数
                new_i += i  # 步长，再次遍历
