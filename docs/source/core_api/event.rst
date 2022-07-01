事件
=============================================
以下均为 ``hpyc_core.Core`` 的方法

eventStartCalculate
-----------------------
开始计算 （启动计算线程）

.. code-block:: python

    eventStartCalculate(self, plugin_id: str, input_data: Any, mode="Return") -> None:

参数说明
    - plugin_id: 插件id, 类型 ``str``
    - input_data: 未处理的原始输入数据, 类型 ``typing.Any``
    - mode: 计算模式, 类型 ``str``

可能引发的异常
    - ValueError: 当输入了不存在的mode

mode参数别名
    - 运算结果仅返回到消息队列
                "ReturnAfterComputing",
                "ComputingAndReturn",
                "RAC",
                "Return",
                "ReturnAfterCalculating",

    - 运算结果仅保存到文件中
                "SaveAfterComputing",
                "ComputingAndSave",
                "SAC",
                "Save",
                "SaveAfterCalculating",

    - 运算结果从缓冲区中返回到消息队列
                "ReturnAfterComputingFromBuffer",
                "ComputingAndReturnFromBuffer",
                "RACFB",
                "ReturnFromBuffer",
                "ReturnAfterCalculatingFromBuffer",

    - 运算结果从缓冲区中返回到消息队列，但是有返回上限
                "ReturnAfterComputingFromLimitedBuffer",
                "ComputingAndReturnFromLimitedBuffer",
                "RACFLB",
                "ReturnFromLimitedBuffer",
                "ReturnAfterCalculatingFromLimitedBuffer",

eventReloadPlugins
-----------------------
重新加载插件

.. code-block:: python

    def eventReloadPlugins(self) -> None:

eventExit
-----------------------
退出流程，进行一些收尾工作防止进程残留

默认使用atexit模块注册到退出事件

所以一般来说不需要手动触发

.. code-block:: python

    def eventExit() -> None:

