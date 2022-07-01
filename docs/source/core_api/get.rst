获取
=============================================

getMessageQueue
-----------------------
获取消息输出队列

.. code-block:: python

    def getMessageQueue() -> Queue:

getSettingsFileInstance
-----------------------
获取设置文件实例

.. code-block:: python

    def getSettingsFileInstance() -> SettingsFileObject:

getPluginsDirPath
-----------------------
获取插件存放路径

.. code-block:: python

    def getMessageQueue() -> str:

getOutputDirPath
-----------------------
获取输出路径

.. code-block:: python

    def getOutputDirPath(self) -> str:

getSettingsDirPath
-----------------------
获取设置文件存放路径

.. code-block:: python

    def getSettingsDirPath(self) -> str:

getPluginsTagOption
-----------------------
获取所有插件的tag，tag对应插件选项名
(((plugin1_tag1, plugin1_tag2, ...), plugin1_option), ((plugin2_tag1,), plugin2_option)), ...)

.. code-block:: python

    def getPluginsTagOption() -> tuple[tuple[tuple[str, ...], str], ...]:

getPluginsOptionToId
-----------------------
获取插件选项名和id的映射表

.. code-block:: python

    def getPluginsOptionToId() -> dict[str, str]:

getPluginIdFromOption
-----------------------
通过选项名获得对应插件ID

.. code-block:: python

    getPluginIdFromOption(option: str) -> str:

getPluginInstance
-----------------------
获取对应插件实例

.. code-block:: python

    def getPluginInstance(plugin_id: str) -> ModuleType:

getPluginMetadata
-----------------------
拖过插件ID获取对应插件元数据

.. code-block:: python

    def getPluginMetadata(plugin_id: str) -> MetadataDict:

