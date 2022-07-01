import hpyculator as hpyc

NAME = "公因数(公质数，公素数)"
AUTHOR = "HowieHz" or ["作者1", "作者2"]
VERSION = "V1.0.0"
ID = "common_factor_hz"
PLUGIN_METADATA = {
    "input_mode": hpyc.STRING,  # 输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
    "id": ID,  # 插件标识符,需要和文件名一致
    "option": f"{NAME}{VERSION} by {', '.join(AUTHOR) if isinstance(AUTHOR, list) else AUTHOR}",  # 选项名-在选择算法列表中（必须）
    "version": VERSION,  # 版本号
    "tag": ["category:Mathematical-calculations"],
    "save_name": "",  # 文件保存名
    "quantifier": "的公因数",  # 文件保存量词
    "output_start": "",  # 输出头
    "output_name": NAME,  # 选择此项后输出的名字
    "author": AUTHOR,  # 作者
    "help": """\
输入若干个大于等于1的整数，求这些数的公因数

输入格式
    a,b,c,...
    a b c
    a，b，c
    a,b
    a

输入样例
    2,3
    2
    2,4,8
    3,9,27,333
                """,  # 帮助和说明
    "output_end": "",  # 输出小尾巴
    "return_mode": hpyc.NO_RETURN_SINGLE_FUNCTION,
    "fullwidth_symbol": hpyc.OFF,  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def on_calculate(data, do_what: str):
    output = hpyc.output if do_what == "output" else hpyc.write  # 输出内容只需要用output就好了
    for pattern in [",", "，", " "]:
        if pattern in data:
            num_list = sorted(list(map(int, data.split(pattern))))
            break
    else:
        hpyc.output("请按格式输入！！！")
        return

    if num_list[0] <= 0:
        hpyc.output("请按格式输入！！！")
        return

    for num in range(1, num_list[0] + 1):
        # 可以直接写lambda _: (_ % num) == 0, num_list)
        # 但是编程指南里面说函数体不要依赖外部变量，这里是局部所以不会出现问题，要是num是全局变量那就寄了
        # Cell variable defined in loop PYL-W0640
        if all(map(lambda _, divisor=num: (_ % divisor) == 0, num_list)):
            output(num)
