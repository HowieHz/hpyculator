开始
================

目录
-----------------
`零.检查依赖 <..\quick_start.html#id4>`_

`一.从0创建单文件插件`_

`二.从0创建文件夹插件`_

`三.从示例开始 <Start.html#id8>`_ (推荐)

一.从0创建单文件插件
----------------------------

1.创建一个.py文件（文件名要求符合python变量名要求）

2.在文件开头键入 `元数据 <Metadata.html>`_

3.根据 ``return_mode``\，进行不同的开发（这几种模式的不同，详情请见 `return_mode参数讲解 <Metadata.html#return-mode>`_\）

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
