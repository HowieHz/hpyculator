函数
===========

write
-------------------

    第一个参数是要写入的东西，

    第二个参数可选参数 为输入后缀，默认为换行符

效果是将指定数据写入硬盘

缺点： `flush <API.html#flush>`__\函数的开销太大了，如果只用 `write <API.html#write>`__\函数内存开销最小，但是时间开销最大

    （n系列内置插件的写法就是只用 `write <API.html#write>`__\）

.. code-block:: python

    def write(anything,end="\n"): -> None


write_without_flush
--------------------------------------

    第一个参数是要写入的东西，

    第二个参数可选参数 为输入后缀，默认为换行符

效果是将指定数据写入内存（要将这些数据写入硬盘需要使用 `flush <API.html#flush>`__\函数）

    和 `write <API.html#write>`__\函数的区别是写入内存后不写入硬盘，

    可以做到多少行写入一次的操作（fix系列内置插件的写法就是这样）

    （找到多少行写入一次是最优的需要插件作者不断调试，反复尝试，才能找到最优点。致敬每一位负责的开发者）

.. code-block:: python

    def write_without_flush(anything,end="\n"): -> None


flush
--------------------------------------

    无形参

搭配 `write_without_flush <API.html#write-without-flush>`__\函数使用

效果是将 内存里的待写入硬盘的数据 写入 硬盘"""

.. code-block:: python

    def flush(): -> None


output
-------------------

    第一个参数是要输出的东西，

    第二个参数是后缀，默认为换行符

效果是将指定数据打印在输出窗口上

.. code-block:: python

    def output(anything,end="\n"): -> None
