from abc import ABC, abstractmethod
from typing import Any
import os


class SettingsFileObject(ABC):
    def __init__(
        self,
        settings_dir_path: str,
        settings_file_name: str = "settings",
        settings_file_format: str = "",
    ):
        """
        读取一个文件laod

        :param settings_dir_path: 设置文件目录
        :param settings_file_name: 设置文件名
        :param settings_file_format: 设置文件猴嘴
        """
        self._setting_dir_path = settings_dir_path

        # 检查存放设置文件的文件夹是否存在
        if not os.path.exists(self._setting_dir_path):
            os.makedirs(self._setting_dir_path)

        # 初始化设置文件位置
        self._settings_file_path = str(
            os.path.join(
                settings_dir_path, f"{settings_file_name}.{settings_file_format}"
            )
        )

        # 初始化文件
        # # self._file_stream = open(self._settings_file_path, mode="w+", buffering=-1, encoding="utf-8")
        self._settings_file_stream = open(
            self._settings_file_path, mode="a+", encoding="utf-8"
        )
        self._settings_file_stream.close()

    @abstractmethod
    def add(self, key: str, value: Any):
        """
        添加一项配置

        :param key:
        :param value:
        :return:
        """

    @abstractmethod
    def read(self, key: str):
        """
        读取一项配置

        :param key:
        :return:
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def readAll(self):
        """
        读取全部的

        :return:
        """

    @abstractmethod
    def delete(self, key: str):
        """
        删除一项配置

        :param key:
        :return:
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def modify(self, key: str, value: Any):
        """
        修改一项配置

        :param key:
        :param value:
        :return:
        """
        if not self.exists(key):
            raise KeyError

    @abstractmethod
    def exists(self, key: str) -> bool:
        """
        检查一个键是否存在

        :param key:
        :return:
        """
        return False

    @property
    def setting_file_path(self) -> str:
        """
        设置文件的路径

        :return:
        """
        return self._settings_file_path
