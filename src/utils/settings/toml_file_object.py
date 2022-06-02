from .settings_file_object import SettingsFileObject
import toml
from typing import Any


class TomlSettingsFileObject(SettingsFileObject):
    def __init__(self,
                 settings_dir_path: str,
                 settings_file_name: str = "settings",
                 settings_file_format: str = "toml"):
        """
        读取一个文件laod

        :param settings_dir_path: 设置文件目录
        :param settings_file_name: 设置文件名
        :param settings_file_format: 设置文件猴嘴
        """
        super().__init__(settings_dir_path, settings_file_name, settings_file_format)

    def add(self, key: str, value: Any = None):
        """
        添加一项配置

        :param key:
        :param value:
        :return:
        """
        settings_dict = toml.loads(self._settings_file_stream.read())
        self._settings_file_stream.seek(0)
        settings_dict[key] = value
        self._settings_file_stream.write(toml.dumps(settings_dict))
        self._settings_file_stream.seek(0)
        self._settings_file_stream.flush()
        return

    def read(self, key: str) -> Any:
        """
        读取一项配置

        :param key:
        :return:
        """
        # 等价return toml.load(self._settings_file_path)[key]
        settings_dict = toml.loads(self._settings_file_stream.read())
        self._settings_file_stream.seek(0)
        return settings_dict[key]

    def readAll(self) -> dict:
        """
        读取全部的

        :return:
        """
        # 等价return toml.load(self._settings_file_path)[key]
        settings_dict = toml.loads(self._settings_file_stream.read())
        self._settings_file_stream.seek(0)
        return settings_dict

    def delete(self, key: str) -> None:
        """
        删除一项配置

        :param key:
        :return:
        """
        settings_dict = toml.loads(self._settings_file_stream.read())
        self._settings_file_stream.seek(0)
        settings_dict.pop(key)
        self._settings_file_stream.write(toml.dumps(settings_dict))
        self._settings_file_stream.seek(0)
        self._settings_file_stream.flush()
        return

    def modify(self, key: str, value: Any) -> None:
        """
        修改一项配置

        :param key:
        :param value:
        :return:
        """
        settings_dict = toml.loads(self._settings_file_stream.read())
        self._settings_file_stream.seek(0)
        settings_dict[key] = value
        self._settings_file_stream.write(toml.dumps(settings_dict))
        self._settings_file_stream.seek(0)
        self._settings_file_stream.flush()
        return

    def exists(self, key: str) -> bool:
        """
        检查一个键是否存在

        :param key:
        :return:
        """
        settings_dict = toml.loads(self._settings_file_stream.read())
        self._settings_file_stream.seek(0)
        is_exists = key in settings_dict
        self._settings_file_stream.seek(0)
        return is_exists

    @property
    def setting_file_path(self) -> str:
        """
        设置文件的路径

        :return:
        """
        return self._settings_file_path
