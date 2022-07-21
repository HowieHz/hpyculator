hpydecorator
===================================

hpydecorator.getRuntime
--------------------------------

.. code-block:: python

    def getRunTime(times: int = 1, output: bool = False) -> Callable:
        """一个装饰器, 用来计算函数运行时长, 第一个装饰器参数是运行次数

        装饰后的函数将返回一个元组:(原函数返回值, 运行时长)
        运行时长: 类型int, 单位ns

        :param times: 运行次数, 默认为1
        :param output: 是否输出到流, 默认为False
        :return: 装饰后的函数
        """

例子
~~~~~~~~~~~

.. code-block:: python

    @getRunTime(5)
    def fun_():
        print("text")
        return 1

    num, time = fun_()
    # num = 1
    # time = 五次运行该函数的总时间，单位ns

    @getRunTime(times = 5, output = True)
    def fun2_():
        print("text")
        return 1

    num, time = fun2_()
    # num = 1
    # time = 五次运行该函数的总时间，单位ns
    # 在此基础上会自动执行print(time)

hpydecorator.getFunName
----------------------------

.. code-block:: python

    def getFunName(fun: Callable) -> Callable:
        """函数形参增加__fun_name__用于获得函数名

        :param fun: 原函数
        :return: 装饰后的函数
        """

例子
~~~~~~~~~~~

.. code-block:: python

    @getFunName(__fun_name__: str)
    def fun_():
        return __fun_name__

    name = fun_()
    # name = "fun_"

hpydecorator.isChange
-------------------------------

如何使用
    1. @isChange(show_hash = True) 添加到你要装饰的函数上
    2. 从输出获取函数的hash
    3. @isChange(hash="获取的hash值", show_hash = True) 添加到你要装饰的函数上
    4. 如hash值太长导致装饰器需要占多行
        如：
    .. code-block:: python
        @hpydecorator.isChange(
            hash="5b0ad0d14da3144eb78b73c950320b145d3939d3ef60aa4d52616989",
            ignore_line=2,
            show_hash=False,
        )

        请填写ignore_line, 忽略前几行不计入函数hash值计算

.. code-block:: python

    def isChange(
        hash: str = "0", ignore_line: int = 1, show_hash: bool = False
    ) -> Callable:
        """一个装饰器, 用来计算函数是否被修改

        返回一个元组, 第一项为原返回值, 第二项是是否被修改, 被修改为True, 反之为False

        :param hash: 预先计算的hash值, 默认为"0"
        :param ignore_line: 忽略函数的前几行不进行hash计算, 默认为1
        :param show_hash: 是否输出本次计算的hash值, 默认为False
        :return: 装饰后的函数
        """

例子
~~~~~~~~~~~

.. code-block:: python

    @hpydecorator.isChange(
        hash="5b0ad0d14da3144eb78b73c950320b145d3939d3ef60aa4d52616989",
        ignore_line=4,
        show_hash=False,
        )
    def _fun4() -> None:
    """func

    :return: None
    """
    print("hello")

    assert _fun4()[1] is False  # 代码未被修改