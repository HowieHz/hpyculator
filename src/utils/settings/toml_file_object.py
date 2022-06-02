"""用于创建toml文件对象"""
from .settings_file_object import SettingsFileObject
import toml
from typing import Any


class TomlSettingsFileObject(SettingsFileObject):
    """toml类型的文件对象"""

    def __init__(
        self,
        settings_dir_path: str,
        settings_file_name: str = "settings",
        settings_file_format: str = "toml",
    ):
        """
        读取一个文件，初始化文件对象

        :param settings_dir_path: 设置文件目录
        :param settings_file_name: 设置文件名
        :param settings_file_format: 设置文件后缀
        """
        super().__init__(settings_dir_path, settings_file_name, settings_file_format)

    def add(self, key: str, value: Any = None):
        """
        添加一项配置

        :param key:
        :param value:
        :return:
        """
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict[key] = value
            f.write(toml.dumps(settings_dict))

    def read(self, key: str) -> Any:
        """
        读取一项配置

        :param key:
        :return:
        """
        # 等价return toml.load(self._settings_file_path)[key]
        if not self.exists(key):
            raise KeyError
        settings_dict = self.readAll()
        return settings_dict[key]

    def readAll(self) -> dict:
        """
        读取全部的

        :return:
        """
        # 等价return toml.load(self._settings_file_path)[key]
        with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
            settings_dict = toml.loads(f.read())
        return settings_dict

    def delete(self, key: str) -> None:
        """
        删除一项配置

        :param key:
        :return:
        """
        if not self.exists(key):
            raise KeyError
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict.pop(key)
            f.write(toml.dumps(settings_dict))
        return

    def modify(self, key: str, value: Any) -> None:
        """
        修改一项配置

        :param key:
        :param value:
        :return:
        """
        if not self.exists(key):
            raise KeyError
        settings_dict = self.readAll()
        with open(self._settings_file_path, mode="w+", encoding="utf-8") as f:
            settings_dict[key] = value
            f.write(toml.dumps(settings_dict))
        return

    def exists(self, key: str) -> bool:
        """
        检查一个键是否存在

        :param key:
        :return:
        """
        with open(self._settings_file_path, mode="r", encoding="utf-8") as f:
            is_exists = key in toml.loads(f.read())
        return is_exists

    @property
    def setting_file_path(self) -> str:
        """
        设置文件的路径

        :return:
        """
        return self._settings_file_path
