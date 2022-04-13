快速开始
===================

用户
--------------------

1.从github的 `releases <https://github.com/HowieHz/hpyculator/releases>`__\下载最新版本.zip

2.解压，双击目录下的__main__.exe

3.去插件市场（建设中，先用着内置插件）下点插件就能愉快的使用了


开发者（开发插件）
---------------------

依赖
~~~~~~~~~~~~~~~~

hpyculator 依赖 python3 运行环境。请确保你的 python 版本大于 3.6

安装
~~~~~~~~~~~~~~~~

hpyculator 在 `pypi <https://pypi.org/project/hpyculator>`__ 中可用。它可以通过 ``pip``\命令安装：

.. code-block:: bash

    pip install hpyculator

如果直连速度不畅，你可以使用清华镜像源来加速 hpyculator 的更新：

.. code-block:: bash

    pip install hpyculator -i https://pypi.tuna.tsinghua.edu.cn/simple

更新
~~~~~~~~~~~~~~

在 pypi 的帮助下，``hpyculator`` 可以通过这个命令更新：

.. code-block:: bash

    pip install mcdreforged --upgrade

同样，如果直连速度不畅，你可以使用清华镜像源来加速 hpyculator 的更新：

.. code-block:: bash

    pip install hpyculator --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple

下一步
~~~~~~~~~~
`插件开发 <plugin_dev/index.html>`_

开发者（程序）
---------------------

代码在src文件内，

目前__main__.py是项目入口，Doc.py是一堆常量，Version.py是全局版本号，MainWin.py是基于wxpython所编写的窗口

__main__.py内的Application类继承MainWin的MainWindow类，然后重写对应窗口控件的方法

读取插件的流程
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

主流程在在Application类__init__中

__init__调用readPlugin扫描\Plugin路径下文件

__init__读取\Plugin目录下的.py文件作为单文件插件，然后调用init_plugin_singerfile加载单文件插件

__init__读取\Plugin目录下的文件夹，且文件下有__init__.py文件作为文件夹插件，然后调用init_plugin_folder加载文件夹插件

计算的流程
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

按下计算按钮之后，主程序调用startEvent，

startEvent判断是否有选择计算核心，输入框是否有输入

然后启动新线程，新线程启动startCalculate

startCalculate根据选项，
分别调用

whatNeedCalculateWithTest当用户勾选测试

whatNeedCalculateWithSave当用户选择保存

whatNeedCalculateWithOutputOptimization当用户勾选输出优化，原理是创建临时文件，写入再读取输出

whatNeedCalculate当用户不勾选保存，不勾选测试，不勾选输出优化

优先级：测试>保存>输出优化>优化