元数据
=================

这是一段示例元数据，

如果要开发，可以复制这一段，放在插件文件开头，然后进行修改

请替换掉{}的部分

具体说明和区别请看 `参数会影响什么`_ 一节

.. code-block:: python

    import hpyculator as hpyc

    PLUGIN_METADATA = {
    'input_mode' : hpyc.STRING,#输入模式，STRING为传入字符串,NUM为传入int,FLOAT为传入float(传入的作为on_calculate函数的开始计算值)
    'id' : '[文件名]',#ID，插件标识符，需要和文件名一致
    'option_name' : "[算法名][版本号(推荐语义化版本)] by [作者名]",#选项名-在选择算法列表中
    'version' : '[版本号(推荐语义化版本)]',#版本号

    'save_name' : "{}",#文件保存项目名-在输出
    'quantifier' : "{}",#文件保存量词-在输入后面(可选)

    'output_start' : "",#输出头(可选)
    'output_name' : "{算法名}", #选择此项后输出的名字
    'author' : "{作者名}",#作者(可选)
    'help' : """
        {帮助内容}
                """,#帮助和说明(可选)
    'output_end' : "",#输出小尾巴(可选)

    'return_mode' : hpyc.NO_RETURN,
    # 具体说明和区别请看“return_mode参数讲解”一节
    # hpyc.RETURN_ONCE为返回一次（适用于return字符串等情况），
    # hpyc.RETURN_LIST为将返回的数据迭代输出（适用于return列表等情况），
    # hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE为将返回的数据迭代输出（适用于return列表等情况，和hpyc.RETURN_LIST相似，但是每次输出不换行）,
    # （推荐）hpyc.NO_RETURN无return返回值，要求插件作者放置保存和输出（性能最好，推荐使用，默认值）（要求插件作者自己写好保存和返回，计算调用on_calculate函数，
    #         保存调用mon_calculate_with_save函数），
    # （推荐）hpyc.NO_RETURN_SINGLE_FUNCTION和三类似，但是只会调用on_calculate，且会传入第三个参数，第三个参数为'save'时表示为要输出到内屏，第三个参数为'output'时表示要保存
    'use_quantifier' : hpyc.OFF ,#保存名的形式，OFF为 时间+算法名+输入+量词  ON为 时间+输入+“的”+算法名
                                    #如果是ON，则quantifier无效化
    "fullwidth_symbol" : hpyc.OFF #懒人专用，默认是0，开1之后help段符号全部转换成全角(可选)
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
        use_quantifier为ON
            时间 + save_name + 输入 + quantifier .txt
        use_quantifier为OFF
            时间 + 输入 + "的" +save_name .txt

        """

    """添加的选项
        option_name

        """


``return_mode`` 参数讲解
----------------------------------------------------------------------------
    ``import hpyculator as hpyc``

    方案0  -> hpyc.RETURN_ONCE

    方案1  -> hpyc.RETURN_LIST

    方案2  -> hpyc.RETURN_LIST_OUTPUT_IN_ONE_LINE

    方案3  -> hpyc.NO_RETURN

    方案4  -> hpyc.NO_RETURN_SINGLE_FUNCTION

    关于这几个mode的来源----一个小故事

        (1) 方案0和方案1是最初的方案

            由主程序控制读写和内屏输出，这两个方案的区别是，

            方案0是on_calculate函数return的值 直接输出，比如输出一个字符串

            方案1是on_calculate函数return的值 放在一个迭代器里面依次输出，比如把一个列表的每一项依次输出

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

        (2) 方案3和方案4给与了插件作者调整输出时机和保存时机

            方案3中，程序仅仅是把参数传给 ``on_calculate`` 函数和 ``on_calculate_with_save``函数 ，然后需要使用 `output <API.html#output>`_\， `write <API.html#write>`_\， `flush <API.html#flush>`_\等函数自己调节输出到文本框，写入内存，写入硬盘的时机

            有人觉得方案3分成两个函数太麻烦了，于是出现了方案4，会多传入一个参数，来告知插件究竟是保存还是输出到内屏
