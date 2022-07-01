from math import *

import hpyculator as hpyc

NAME = "计算器(基于eval)"
AUTHOR = "HowieHz" or ["作者1", "作者2"]
VERSION = "V1.0.2"
PLUGIN_METADATA = {
    # 输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
    "input_mode": hpyc.STRING,
    "id": "calculator_eval_hz",  # 插件标识符,需要和文件名一致
    # 选项名-在选择算法列表中（必须）
    "option": f"{NAME}{VERSION} by {', '.join(AUTHOR) if isinstance(AUTHOR, list) else AUTHOR}",
    "version": VERSION,  # 版本号
    "tag": ["category:Mathematical-calculations"],
    "save_name": "",  # 文件保存名
    "quantifier": "的计算结果",  # 文件保存量词
    "output_start": "",  # 输出头
    "output_name": NAME,  # 选择此项后输出的名字
    "author": AUTHOR,  # 作者
    "help": """\
输入格式
    若干数学符号和数字的组合

(注：eval已做危险关键字过滤)

支持列表(refer to https://www.runoob.com/python3/python3-basic-operators.html):

算术运算符
    +	加 - 两个对象相加
    -	减 - 得到负数或是一个数减去另一个数
    *	乘 - 两个数相乘或是返回一个被重复若干次的字符串
    /	除 - x 除以 y
    %	取模 - 返回除法的余数
    **	幂 - 返回x的y次幂
    //	取整除 - 向下取接近商的整数

特殊表示
    0b开头	-> 2进制数
    0o开头	-> 8进制数
    0x开头	-> 16进制数
    复数	    -> a+bj
    pi	    -> 圆周率
    e	    -> 自然常数
    1e18	-> 科学计数法

数学函数
    函数	            返回值 ( 描述 )
    abs(x)	        返回数字的绝对值，如abs(-10) 返回 10
    ceil(x)	        返回数字的上入整数，如math.ceil(4.1) 返回 5
    exp(x)	        返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
    fabs(x)	        返回数字的绝对值，如math.fabs(-10) 返回10.0
    floor(x)	    返回数字的下舍整数，如math.floor(4.9)返回 4
    log(x)	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0
    log10(x)	    返回以10为基数的x的对数，如math.log10(100)返回 2.0
    max(x1, x2,...)	返回给定参数的最大值，参数可以为序列
    min(x1, x2,...)	返回给定参数的最小值，参数可以为序列
    modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
    pow(x, y)	    x**y 运算后的值
    round(x [,n])	返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数
    sqrt(x)	        返回数字x的平方根

    acos(x)	        返回x的反余弦弧度值
    asin(x)	        返回x的反正弦弧度值
    atan(x)	        返回x的反正切弧度值
    atan2(y, x)	    返回给定的 X 及 Y 坐标值的反正切值。
    cos(x)	        返回x的弧度的余弦值
    hypot(x, y)	    返回欧几里德范数 sqrt(x*x + y*y)。
    sin(x)	        返回的x弧度的正弦值
    tan(x)	        返回x弧度的正切值
    degrees(x)	    将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
    radians(x)	    将角度转换为弧度

比较（关系）运算符
    ==	等于 - 比较对象是否相等
    !=	不等于 - 比较两个对象是否不相等
    >	大于 - 返回x是否大于y
    <	小于 - 返回x是否小于y
    >=	大于等于 - 返回x是否大于等于y
    <=	小于等于 - 返回x是否小于等于y

位运算符
    &	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
    |	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1
    ^	按位异或运算符：当两对应的二进位相异时
    ~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
    <<	左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0
    >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数

逻辑运算符
    and	    x and y	布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值
    or	    x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值
    not	    not x	布尔"非" - 如果 x 为 True，返回 False;如果 x 为 False，它返回 True

                """,  # 帮助和说明
    "output_end": "",  # 输出小尾巴
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.OFF,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def on_calculate(data: str, do_what: str):
    output = hpyc.output if do_what == "output" else hpyc.write  # 输出内容只需要用output就好了
    _list_char_check = [
        "import",
        "system",
        "rf",
        "rm",
        "str",
        "exec",
        "eval",
        ";",
        "'",
        '"',
        "lambda",
        "__import__",
        "os",
        "，",
        "{",
        "}",
    ]
    for _char in _list_char_check:
        if _char in data:
            output("检测到非法字符")
            return
    try:
        output(eval(data))
    except SyntaxError:
        output("检测到不支持的字符")
        return
