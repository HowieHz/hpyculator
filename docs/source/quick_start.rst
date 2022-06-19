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

目前__main__.py是项目入口

src文件夹下
    Plugin里面存放的是内置插件

    background_img文件夹里面是内置的背景图

    test内是单元测试

    use_for_packing内存放的是用于打包，启动的工具

    utils内是主要代码

src/utils文件夹下
    calculate -> 调用插件计算

    document -> 常量存放

    locale -> i18n

    plugin -> 插件管理，插件加载

    pyside_frameless_win -> 无边框ui

    settings -> 管理设置文件

    ui -> ui

    ui_manager -> 管理ui，大部分程序逻辑

