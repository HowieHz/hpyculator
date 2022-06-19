函数
===========

output_without_line_break
-------------------

    第一个参数是要输出的东西

效果是将指定数据打印在输出窗口上，不会换行
分两个函数的原因是调用函数不同，output的性能会优于output_without_line_break

.. code-block:: python

    def output_without_line_break(anything) -> None:

output
-------------------

    第一个参数是要输出的东西

效果是将指定数据打印在输出窗口上，会自动添加换行符

.. code-block:: python

    def output(anything): -> None

write_without_flush
--------------------------------------

    第一个参数是要写入的东西，

    第二个参数可选参数 为输入后缀，默认为换行符

效果是将指定数据写入缓冲区（要将这些数据立即硬盘需要使用 `flush <API.html#flush>`__\函数）

.. code-block:: python

    def write_without_flush(anything,end="\n"): -> None

flush
--------------------------------------

    无形参

搭配 `write_without_flush <API.html#write-without-flush>`__\函数使用

效果是将缓冲区的待写入硬盘的数据写入硬盘
缓冲区最大为1,073,741,824B(1024MB)，缓冲区内数据量超过1024MB程序会自动调用flush
这是为了避免插件作者使用write_without_flush忘记flush导致电脑内存占用极高

.. code-block:: python

    def flush(): -> None

write
-------------------

    第一个参数是要写入的东西，

    第二个参数可选参数 为输入后缀，默认为换行符

效果是将指定数据写入硬盘（等效 write_without_flush + flush）

缺点： `flush <API.html#flush>`__\函数非常耗时，导致这个函数运行较慢

.. code-block:: python

    def write(anything,end="\n"): -> None

