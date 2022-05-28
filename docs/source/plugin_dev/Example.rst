插件参考（写法参考）
======================

以下是 单文件插件 ， 文件夹插件的__init__.py文件 的示例

使用时请替换掉{}的内容,以下是对三个示例的使用方法

Example1:当``return_mode`` 为
RETURN_ONCE,
RETURN_LIST,
RETURN_LIST_OUTPUT_IN_ONE_LINE,
需要完成 ``on_calculate`` 函数

Example2:当``return_mode`` ,NO_RETURN为完成 ``on_calculate`` 和 ``on_calculate_with_save`` 函数

Example3:当``return_mode`` ,NO_RETURN_SINGLE_FUNCTION,的时候只需要完成 ``on_calculate`` 函数


Example1

.. code-block:: python

    import hpyculator as hpyc

    NAME = "名"
    AUTHOR = "作者" or ["作者1", "作者2"]
    VERSION = "V1.0.0"
    PLUGIN_METADATA = {
        'input_mode': hpyc.STRING,  # 输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
        'id': "prime_hz",  # 插件标识符,需要和文件名一致
        'option': f"{NAME}{VERSION} by {', '.join(AUTHOR) if isinstance(AUTHOR,list) else AUTHOR}",  # 选项名-在选择算法列表中（必须）
        'version': VERSION,  # 版本号
        'tag' : [""],

        'save_name': "",  # 文件保存名
        'quantifier': "",  # 文件保存量词

        'output_start': "",  # 输出头
        'output_name': NAME,  # 选择此项后输出的名字
        'author': AUTHOR,  # 作者
        'help': """\
    输入格式
        n

    输入样例
        1
                    """,  # 帮助和说明
        'output_end': "",  # 输出小尾巴

        'return_mode': hpyc.RETURN_ONCE,
        "fullwidth_symbol": hpyc.OFF  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
    }

    def on_calculate(input_data):
        pass

Example2

.. code-block:: python

    import hpyculator as hpyc

    NAME = "名"
    AUTHOR = "作者" or ["作者1", "作者2"]
    VERSION = "V1.0.0"
    PLUGIN_METADATA = {
        'input_mode': hpyc.STRING,  # 输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
        'id': "prime_hz",  # 插件标识符,需要和文件名一致
        'option': f"{NAME}{VERSION} by {', '.join(AUTHOR) if isinstance(AUTHOR,list) else AUTHOR}",  # 选项名-在选择算法列表中（必须）
        'version': VERSION,  # 版本号
        'tag' : [""],

        'save_name': "",  # 文件保存名
        'quantifier': "",  # 文件保存量词

        'output_start': "",  # 输出头
        'output_name': NAME,  # 选择此项后输出的名字
        'author': AUTHOR,  # 作者
        'help': """\
    输入格式
        n

    输入样例
        1
                    """,  # 帮助和说明
        'output_end': "",  # 输出小尾巴

        'return_mode': hpyc.NO_RETURN,
        "fullwidth_symbol": hpyc.OFF  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
    }
        
    def on_calculate(input_data):#输出到框体内
        pass
        
    def on_calculate_with_save(input_data):#保存到文件
        pass


Example3

.. code-block:: python

    import hpyculator as hpyc

    NAME = "名"
    AUTHOR = "作者" or ["作者1", "作者2"]
    VERSION = "V1.0.0"
    PLUGIN_METADATA = {
        'input_mode': hpyc.STRING,  # 输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为main函数的开始计算值)
        'id': "prime_hz",  # 插件标识符,需要和文件名一致
        'option': f"{NAME}{VERSION} by {', '.join(AUTHOR) if isinstance(AUTHOR,list) else AUTHOR}",  # 选项名-在选择算法列表中（必须）
        'version': VERSION,  # 版本号
        'tag' : [""],

        'save_name': "",  # 文件保存名
        'quantifier': "",  # 文件保存量词

        'output_start': "",  # 输出头
        'output_name': NAME,  # 选择此项后输出的名字
        'author': AUTHOR,  # 作者
        'help': """\
    输入格式
        n

    输入样例
        1
                    """,  # 帮助和说明
        'output_end': "",  # 输出小尾巴

        'return_mode': hpyc.NO_RETURN_SINGLE_FUNCTION,
        "fullwidth_symbol": hpyc.OFF  # 懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
    }


    def on_calculate(data, do_what: str):
        output = hpyc.output if do_what == "output" else hpyc.write  # 输出内容只需要用output就好了


以下.py文件均代指 `内置插件 <https://github.com/HowieHz/hpyculator/tree/main/Plugin>`_
hpyc代指hpyculator模块

test9.py
    是return_mode=hpyc.NO_RETURN的典范，
    在test9系列中内存开销和时间开销中找了一个平衡点，
    使用了write_without_flush和flush函数

Statistics.py
    是return_mode=hpyc.RETURN_ONCE的典范，
    很好的展示了return_mode=hpyc.RETURN_ONC的用处

fibonacci_Sequence.py
    return_mode=hpyc.NO_RETURN_SINGLE_FUNCTION的典范，
    很好的展示了return_mode=hpyc.NO_RETURN_SINGLE_FUNCTION的写法

