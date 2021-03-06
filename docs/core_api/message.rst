消息
===============

消息输出队列
-----------------------
获取消息输出队列

.. code-block:: python

    from hpyc_core import Core
    instance_core = Core()
    message_queue = instance_core.getMessageQueue()

在以上示例中使用 ``message_queue.get()`` 可获取消息，消息类型是元组

出现的消息有以下几种

("ERROR", "TypeConversionError", str("详细信息"))
--------------------------------------------------------------------------------

    类型转换出现错误，详细信息在第三项， 类型是 `str`

    此时运算线程停止

("ERROR", "CalculationError", str("详细信息"))
----------------------------------------------------------------------------

    运算出现错误，详细信息在第三项， 类型是 `str`

    此时运算线程停止

("OUTPUT", str(result))
----------------------------------------------------------------------------

    插件运算结果，第二项是运算结果

("MESSAGE", "OutputReachedLimit")
----------------------------------------------------------------------------

    达到输出上限，仅选择 ”从缓冲区中返回，但是有返回上限“ 模式才会触发的消息

    此时运算线程停止，但此时不能推出消息监听

    因为接下来还有一条 ``CalculationProgramIsFinished`` 消息

("MESSAGE", "CalculationProgramIsRunning")
----------------------------------------------------------------------------

    运算线程开始

("MESSAGE", "CalculationProgramIsFinished", time_spent)
--------------------------------------------------------------------------------------------

    运算顺利完毕，第三项是运算所用时间，单位是 `ns` ，类型是 `int`

    此时运算线程停止