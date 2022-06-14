元数据
=================

这是一段示例元数据，

请替换掉{}的部分

具体说明和区别请看 `参数会影响什么`_ 一节

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

参数会影响什么
----------------------------------------------------------------------------

.. code-block:: python

    """内置文本框框在选择后的输出

        output_start
        output_name version
        by author

        使用提示：

        help

        output_end

        """

    """内置文本框在选择保存后的输出
        本次计算花费了*秒
        结果输出（用户选择不保存时输出）
        保存计算结果至文件中···（用户选择保存时输出）
        计算结果已保存在 保存文件名的完整路径（用户选择保存时输出）

    """

    """保存文件名
        时间 + save_name + 输入 + quantifier .txt

        """

    """添加的选项
        option

        """

    """作者名author支持的形式
    1. 字符串类型，如："作者名"
    2. 列表，如：["作者名1", "作者名2"]
    """

    """标签tag支持的形式
    1. 列表，如：["标签1","标签2"] ["标签1"]
    """

    """会被特殊识别的标签
    1. category:开头的标签，会被作为插件类别识别，如"category:math"
    2. computer_language:开头的标签，会作为所用编程语言识别，如"computer_language:java"
    3. depend:开头的标签，会作为依赖识别，如"depend:numpy"
    """



``return_mode`` 参数讲解
----------------------------------------------------------------------------
    ``import hpyculator as hpyc``

    方案0  -> hpyc.RETURN_ONCE

    方案1  -> hpyc.RETURN_ITERABLE

    方案2  -> hpyc.RETURN_ITERABLE_OUTPUT_IN_ONE_LINE

    方案3  -> hpyc.NO_RETURN

    方案4  -> hpyc.NO_RETURN_SINGLE_FUNCTION

    由主程序控制读写和内屏输出，这两个方案的区别是，

    方案0是on_calculate函数return的对象 直接输出，比如输出一个字符串

    方案1是on_calculate函数return的对象 迭代输出，比如把一个列表的每一项依次输出

        .. code-block:: python

            #return的值是[1,2,3,4]
            #输出和保存则是
            """
            1
            2
            3
            4
            """

    方案2和方案1的区别是，每次输出之后不换行

        .. code-block:: python

            #return的值是[1,2,3,4]
            #输出和保存则是
            """
            1234
            """

    很显然，当用户输入数值比较大的时候，

    多项数组会迅速占用用户内存，导致死机等后果

    保存的时候所有东西会先写入用户内存，最后再保存到硬盘

    好处是此方案保存是最快的
    （输出也是，但是内存堆积太多再输出容易卡住输出框）

    为了解决内存爆炸的问题，方案3和4孕育而生

    方案3和方案4给与了插件作者调整输出时机和保存时机

    方案3中，程序仅仅是把参数传给 ``on_calculate`` 函数和 ``on_calculate_with_save``函数 ，然后需要使用 `output <API.html#output>`_\， `write <API.html#write>`_\， `flush <API.html#flush>`_\等函数自己调节输出到文本框，写入内存，写入硬盘的时机

    方案3分成两个函数不够高效，于是出现了方案4，会多传入一个参数(请看插件事件一节)，来告知插件究竟是保存还是输出到内屏
