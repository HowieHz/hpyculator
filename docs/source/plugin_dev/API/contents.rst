函数
===========

write
-------------------

    第一个参数是文件流，

    第二个参数是要写入的东西，

    第三个参数是后缀，默认为换行符

效果是将指定数据写入硬盘

缺点：flush函数的开销太大了，如果只用write函数内存开销最小，但是时间开销最大

    （n系列内置插件的写法就是只用write）

.. code-block:: python

    def write(file,anything,end="\n"): -> None


write_without_flush
--------------------------------------

    第一个参数是文件流，

    第二个参数是要写入的东西，

    第三个参数是后缀，默认为换行符

效果是将指定数据写入内存（要将这些数据写入硬盘需要使用flsuh函数）

    和write函数的区别是写入内存后不写入硬盘，

    可以做到多少行写入一次的操作（fix系列内置插件的写法就是这样）

    （找到多少行写入一次是最优的需要插件作者不断调试，反复尝试，才能找到最优点。致敬每一位负责的开发者）

.. code-block:: python

    def write_without_flush(file,anything,end="\n"): -> None


flsuh
--------------------------------------

    第一个参数是文件流

搭配write_without_flush函数使用

效果是将 内存里的待写入硬盘的数据 写入 硬盘"""

.. code-block:: python

    def flush(file): -> None


output
-------------------

    第一个参数是代指主类（确切一点是指输出窗口），

    第二个参数是要输出的东西，

    第三个参数是后缀，默认为换行符

效果是将指定数据打印在输出窗口上

.. code-block:: python

    def output(self,anything,end="\n"): -> None
