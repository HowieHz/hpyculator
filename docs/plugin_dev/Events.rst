插件事件
=============================================

    开始计算之后，会创建一个新线程分给插件

    单文件插件调用 ``文件名.py``\内的 ``on_calculate``\函数和 ``on_calculate_with_save``\函数

    文件夹插件调用 ``文件夹名\__init_.py``\内的 ``on_calculate``\函数和 `on_calculate_with_save``\函数

    （注：当 ``return_mode``\为RETURN_……或NO_RETURN_SINGLE_FUNCTION，只调用 ``on_calculate``\函数）

当 ``return_mode``\为RETURN_……
-----------------------------------

根据 ``input_mode``\参数，将用户输入处理后传入on_calculate函数

    调用插件的 ``on_calculate``\函数，

        第一个实参是转换后的输入值

    .. code-block:: python

        def on_calculate(inputdata)
            #插件主体
            return 你要输出的东西

当 ``return_mode``\为NO_RETURN
-----------------------------------------------------------------

根据 ``input_mode``\参数，将输入处理成目标形式

当用户选择不保存（内屏输出）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

调用插件的 ``on_calculate``\函数，

    第一个实参是转换后的输入值

.. code-block:: python

    def on_calculate(inputdata)
        #插件主体，需要输出到内屏的时候使用下面的语句
        output("你要输出的东西")

当用户选择保存
~~~~~~~~~~~~~~~~~~~~~~~~~

调用插件的 ``on_calculate_with_save``\函数，

    第一个实参是转换后的输入值

.. code-block:: python

    def on_calculate_with_save(inputdata)
        #插件主体，需要保存的时候使用下面的语句
        write("你要保存的东西")
        #或者
        write_without_flush("你要保存的东西")
        #记得配合flush(file)使用

当 ``return_mode``\为NO_RETURN_SINGLE_FUNCTION
-----------------------------------------------------------------

根据 ``input_mode``\参数，将用户输入处理成目标形式

当用户选择不保存（内屏输出）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

调用插件的 ``on_calculate``\函数，

    第一个实参是转换后的输入值，

    第二个实参是 ``'output'``

当用户选择保存
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

调用插件的 ``on_calculate``\函数，

    第一个实参是转换后的输入值，

    第二个实参是 ``'save'``
