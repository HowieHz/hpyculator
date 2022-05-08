import hpyculator as hpyc

PLUGIN_METADATA = {
    'input_mode': hpyc.NUM,
    'id': 'Yang_Hui_s_Triangle_fix',  # ID,插件标识符,需要和文件名一致（必须）
    'option_name': "杨辉三角_fixV1.0.1 by HowieHz",  # 选项名-在选择算法列表中（必须）
    'version': 'V1.0.1',  # 版本号（必须）

    'save_name': "杨辉三角前",  # 文件保存项目名-在输出（必须）
    'quantifier': "行",  # 文件保存量词-在输入后面(可选)

    'output_start': "",  # 输出头(可选)
    'output_name': "杨辉三角",  # 选择此项后输出的名字（必须）
    'author': "HowieHz",  # 作者(可选)
    'help': """
    输入数字n ，输出前n行杨辉三角
            """,  # 帮助和说明(可选)
    'output_end': "",  # 输出小尾巴(可选)

    'return_mode': hpyc.NO_RETURN,
    'use_quantifier': hpyc.OFF,
    "fullwidth_symbol": hpyc.ON  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
}


def on_calculate(num):  # 返回一个列表
    if num == 0:
        return []
    l1 = [[1]]
    for _ in range(0, num - 1):
        l1.append(list(map(lambda x, y: x + y, [0] + l1[-1], l1[-1] + [0])))
    for i in l1:
        hpyc.output(i)


def on_calculate_with_save(num, file):  # 返回一个列表
    if num == 0:
        hpyc.write(file, [])
    l1 = [[1]]
    for _ in range(0, num - 1):
        l1.append(list(map(lambda x, y: x + y, [0] + l1[-1], l1[-1] + [0])))
    for i in l1:
        hpyc.write_without_flush(file, i)
    hpyc.flush(file)
    l1 = None
    return
