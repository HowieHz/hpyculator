事件
=============================================

eventReloadPlugins
-----------------------
重新加载插件

.. code-block:: python

    def eventReloadPlugins(self) -> None:

eventStartCalculate
-----------------------
启动计算
    - plugin_id: 插件id
    - input_data: 未处理的原始输入数据
    - mode: 计算模式
    - None
    - ValueError: 当输入了不存在的mode

modes别名
    - 仅返回到消息队列
                "ReturnAfterComputing",
                "ComputingAndReturn",
                "RAC",
                "Return",
                "ReturnAfterCalculating",

    - 仅保存到文件中
                "SaveAfterComputing",
                "ComputingAndSave",
                "SAC",
                "Save",
                "SaveAfterCalculating",

    - 从缓冲区中返回
                "ReturnAfterComputingFromBuffer",
                "ComputingAndReturnFromBuffer",
                "RACFB",
                "ReturnFromBuffer",
                "ReturnAfterCalculatingFromBuffer",

    - 从缓冲区中返回，但是有返回上限
                "ReturnAfterComputingFromLimitedBuffer",
                "ComputingAndReturnFromLimitedBuffer",
                "RACFLB",
                "ReturnFromLimitedBuffer",
                "ReturnAfterCalculatingFromLimitedBuffer",

.. code-block:: python

    eventStartCalculate(self, plugin_id: str, input_data: Any, mode="Return") -> None:

eventExit
-----------------------
退出流程，防止进程残留

默认使用atexit模块注册到退出事件

所以一般来说不需要手动触发

.. code-block:: python

    def eventExit() -> None:

