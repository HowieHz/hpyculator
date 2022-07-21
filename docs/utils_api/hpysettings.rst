hpysettings
====================

用于快捷管理json，yaml，toml设置文件

设置文件对象的add，delete，modify方法支持链式调用

hpysettings.load
------------------------------------

load函数用于创建一个设置文件对象（返回一个创建好的设置文件对象）

.. code-block:: python

    def load(
        settings_dir_path: str = str(os.path.join(os.getcwd(), "Setting")),  # 默认设置目录
        settings_file_name: str = "settings",
        settings_file_format: str = "toml",
    ) -> hpysettings.SettingsFileObject:
        """加载一个设置文件对象
        工厂函数

        :param settings_dir_path: 设置文件所在目录, 默认是 str(os.path.join(os.getcwd(), "Setting"))
        :param settings_file_name: 设置文件的文件名, 默认是"settings"
        :param settings_file_format: 设置文件的类型(后缀), 默认是"toml"
        :return: 设置文件实例
        """

hpysettings.SettingsFileObject
-----------------------------------------------------------------

hpysettings.JsonSettingsFileObject, hpysettings.YamlSettingsFileObject, hpysettings.TomlSettingsFileObject 均继承自 hpysettings.SettingsFileObject

.. code-block:: python

    hpysettings.SettingsFileObject = Union[
        hpysettings.JsonSettingsFileObject, hpysettings.YamlSettingsFileObject, hpysettings.TomlSettingsFileObject
    ]

hpysettings.SettingsFileObject.add
-----------------------------------------

.. code-block:: python

    def add(self, key: str, value: Any) -> SettingsFileObject:
        """添加一项配置

        :param key: 键
        :param value: 值
        :return: 链式调用, 返回本身
        """

hpysettings.SettingsFileObject.read
-----------------------------------------

.. code-block:: python

    def read(self, key: str) -> Any:
        """读取一项配置

        :param key: 键
        :return: 值
        :raises KeyError: 没有这个键
        """

hpysettings.SettingsFileObject.readAll
------------------------------------------

.. code-block:: python

    def readAll(self) -> dict:
        """读取全部的

        :return: 键值对
        """

hpysettings.SettingsFileObject.delete
-----------------------------------------

.. code-block:: python

    def delete(self, key: str) -> SettingsFileObject:
        """删除一项配置

        :param key: 键
        :return: 链式调用, 返回本身
        :raises KeyError: 没有这个键
        """
hpysettings.SettingsFileObject.modify
-----------------------------------------

.. code-block:: python

    def modify(self, key: str, value: Any) -> SettingsFileObject:  # type: ignore
        """修改一项配置

        :param key: 键
        :param value: 值
        :return: 链式调用, 返回本身
        :raises keyError: 没有这个键
        """

hpysettings.SettingsFileObject.exists
------------------------------------------

.. code-block:: python

    def exists(self, key: str) -> bool:
        """检查一个键是否存在

        :param key: 键
        :return: 存在为True, 不存在为False
        """
hpysettings.SettingsFileObject.setting_file_path
-------------------------------------------------------

.. code-block:: python

    @property
    def setting_file_path(self) -> str:
        """获取设置文件的路径

        :return: 设置文件的路径
        """