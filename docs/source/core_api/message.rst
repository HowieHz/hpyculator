消息
===============

getMessageQueue
-----------------------
获取消息输出队列

.. code-block:: python

    def getMessageQueue() -> Queue:


使用.get()方法获取的消息类型是元组
出现的消息有以下几种

("ERROR", "TypeConversionError", str(e))

    类型转换出现错误，详细信息在第三项

    此时运算线程停止

("ERROR", "CalculationError", str(e))

    运算出现错误，详细信息在第三项

    此时运算线程停止

("OUTPUT", str(result))

    插件运算结果，第二项是运算结果

("MESSAGE", "OutputReachedLimit")

    达到输出上限，仅选择 ”从缓冲区中返回，但是有返回上限“ 模式才会触发的消息

    此时运算线程停止

("MESSAGE", "CalculationProgramIsRunning")

    运算线程开始

("MESSAGE", "CalculationProgramIsFinished", time_spent)

    运算顺利完毕，第三项是运算所用时间

    此时运算线程停止