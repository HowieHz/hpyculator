元数据
=================

这是元数据字典各键值的类型要求

具体说明请看 `参数会影响什么`_ 一节

**数据类型要求**

.. code-block:: python

    from typing import TypedDict, Literal
    import hpyculator as hpyc


    class MetadataDict(TypedDict, total=False):
        """插件元数据数据类型"""

        input_mode: Literal[hpyc.STRING, hpyc.NUM, hpyc.FLOAT]
        id: str
        option: str
        version: str
        tag: list | str
        save_name: str
        quantifier: str
        output_start: str
        output_name: str
        author: str | list
        help: str
        output_end: str
        return_mode: Literal[
            hpyc.RETURN_ONCE,
            hpyc.RETURN_ITERABLE,
            hpyc.NO_RETURN,
            hpyc.NO_RETURN_SINGLE_FUNCTION,
        ]
        fullwidth_symbol: Literal[hpyc.ON, hpyc.OFF]

以下是一段示例元数据

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

数据类型要求和说明

    .. code-block:: python

        import hpyculator as hpyc

    - 输入数据类型 ``input_mode`` , 会将原始输入转换成对应类型, 要求在以下常量中选择一个
        - `hpyc.STRING` -> 对应 `str` 类型
        - `hpyc.NUM` -> 对应 `int` 类型
        - `hpyc.FLOAT` -> 对应 `float` 类型
    - 插件 ``id``
        - `str` 类型, 要求于文件名(单文件插件)/文件夹名(文件夹插件)一致, 否则无法正常加载插件
    - 选项名 `option`
        - `str` 类型, 给用户展示选项所用
    - 版本号 `version`
        - `str` 类型, 建议使用语义化版本
    - 标签 ``tag`` 支持的形式
        - 列表，如：["标签1","标签2"] ["标签1"]
        - 字符串，如："标签"
    - 保存所用名称 ``save_name``
        - `str` 类型
    - 量词, 保存用 ``quantifier``
        - `str` 类型
    - 输出头 ``output_start``
        - `str` 类型, 一般与 ``help `` 同时输出
    - 输出名 ``output_name``
        - `str` 类型, 一般与 ``help `` 同时输出
    - 作者名 ``author`` 支持的形式
        - 字符串类型，如："作者名"
        - 列表，如：["作者名1", "作者名2"]
    - 详细介绍, 帮助, 介绍正文 ``help``
        - `str` 类型
    - 输出尾 ``output_end``
        - `str` 类型, 一般与 ``help `` 同时输出
    - 返回模式 ``return_mode`` 要求在以下常量中选择一个
        - `hpyc.RETURN_ONCE`
        - `hpyc.RETURN_ITERABLE`
        - `hpyc.NO_RETURN`
        - `hpyc.NO_RETURN_SINGLE_FUNCTION`
    - 全角模式 ``fullwidth_symbol``
        - 会将 ``help`` 字段值中的半角符号转换为全角符号

参数会影响什么
----------------------------------------------------------------------------

**以下内容是描述hpyc_pyside_ui的解析系统**

    - 内置文本框框在选择后的输出

    .. code-block:: python

            """
            output_start
            output_name version
            by author

            使用提示：

            help

            output_end
            """


    - 保存文件名
        - 时间 + save_name + 输入 + quantifier .txt
    - 添加的选项
        - option
    - `会被特殊识别的标签 <https://github.com/HowieHz/hpyculator/blob/main/hpyc_pyside_ui/README.md#%E4%BC%9A%E8%A2%AB%E7%89%B9%E6%AE%8A%E8%AF%86%E5%88%AB%E7%9A%84tag>`_
        - category:开头的标签，会被作为插件类别识别，如"category:math"
        - computer_language:开头的标签，会作为所用编程语言识别，如"computer_language:java"
        - depend:开头的标签，会作为依赖识别，如"depend:numpy"


``return_mode`` 参数讲解
----------------------------------------------------------------------------

.. code-block:: python

    import hpyculator as hpyc


`hpyc.RETURN_ONCE` : on_calculate函数返回的结果会经过一次str转换之后输出

`hpyc.RETURN_ITERABLE` : on_calculate函数返回的结果会经过迭代，每一项都会经过str转换之后输出


**hpyc_pyside_ui对hpyc.RETURN_ITERABLE的处理方式**

    .. code-block:: python

        #return的值是[1,2,3,4]
        #输出和保存则是
        """
        1
        2
        3
        4
        """


为了提供更高的自由度， `hpyc.NO_RETURN` 和 `hpyc.NO_RETURN_SINGLE_FUNCTION` 孕育而生

`hpyc.NO_RETURN` 和 `hpyc.NO_RETURN_SINGLE_FUNCTION` 给与了插件作者调整输出时机和保存时机

`hpyc.NO_RETURN` 中，核心(hpyc_core)仅仅是把参数传给 ``on_calculate`` 函数和 ``on_calculate_with_save`` 函数 ，然后需要使用 `output <API.html#output>`_\， `write <API.html#write>`_\， `flush <API.html#flush>`_\等函数自己调节输出到文本框，写入内存，写入硬盘的时机

`hpyc.NO_RETURN` 分成两个函数不够高效，于是出现了 `hpyc.NO_RETURN_SINGLE_FUNCTION` ，会多传入一个参数(请看插件事件一节)，来告知插件究竟是保存还是输出，来决定是使用 `output <API.html#output>`_\还是 `write <API.html#write>`_\ 函数
