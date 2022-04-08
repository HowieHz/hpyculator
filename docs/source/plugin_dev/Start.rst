开始
================

零.读完文档
-----------------
读完文档后有三种选择

`一.从0创建单文件插件`_

`二.从0创建文件夹插件`_

`三.从示例开始 <Start.html#id6>`_

一.从0创建单文件插件
----------------------------

1.创建一个.py文件（文件名要求符合python变量名要求）

2.文件开头写 `元数据 <Metadata.html>`_

3.根据 ``output_mode``\，进行不同的开发（这几种模式的不同，详情请见 `output_mode参数讲解 <Metadata.html#output-mode>`_\）

    a.当 ``output_mode``\为0-2时，写一个 ``main``\函数，这个函数的 ``return``\值会作为输出值和保存值，详情请见 `插件事件 当output_mode为0,1,2 <Events.html#output-mode0-1-2>`_

    b.当 ``output_mode``\为3时，

        将以下代码，复制到你的插件文件里(以下函数的用法 详情请见 `函数 <API/contents.html#id1>`__ 一节)

                .. code-block:: python

                    def write(file,anything,end="\n"):
                        file.write(str(anything)+end)
                        file.flush()

                    def write_without_flush(file,anything,end="\n"):
                        file.write(str(anything)+end)

                    def flush(file):
                        file.flush()

                    def output(self,anything,end="\n"):
                        self.output.AppendText(str(anything)+end)


        然后写 ``main``\函数用于计算并且输入到内框， ``main_save``\函数用于计算并保存

        详情请见 `插件事件 当 output_mode为3 <Events.html#output-mode3>`_

    c.当 ``output_mode``\为4时，

        和数值为3的时候的步骤一样，但是会多传入一个参数说明是否保存，详情请见 `插件事件 当 output_mode为4 <Events.html#output-mode4>`_


二.从0创建文件夹插件
---------------------------------------

1.创建一个文件夹（文件夹要求符合python变量名要求）

2.在里面放置__init__.py文件作为插件入口

3.对__init__.py进行 和 创建单文件插件 的 相同的操作

三.从 `示例 <Example.html>`__ 开始
-------------------------------------------------------------------------------------------------------------------

1.从 `插件参考（写法参考） <Example.html>`__\页面获取示例

2.根据插件类型进行不同的操作

    a.如要创建一个单文件插件

        首先创建一个.py文件（文件名要求符合python变量名要求）

        然后将从 `插件参考（写法参考） <Example.html>`__\页面获取的示例复制进去

        最后进行修改

    b.如要创建一个文件夹插件

        创建一个文件夹（文件夹要求符合python变量名要求）

        然后在这个文件夹根目录创建一个__init__.py文件

        之后将从 `插件参考（写法参考） <Example.html>`__\页面获取的示例复制进去

        最后进行修改