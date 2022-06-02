"""管理设置文件"""
# todo xml
# todo ini
# todo json
# todo yaml

from .toml_file_object import TomlSettingsFileObject
from .json_file_object import JsonSettingsFileObject

import os

dict_settings_file_object = {
    "toml": TomlSettingsFileObject,
    "json": JsonSettingsFileObject,
}


class SettingsManager:
    """设置文件管理类"""

    def __init__(self):
        """初始化设置文件管理"""
        self._settings_dir_path = str(os.path.join(os.getcwd(), "Setting"))  # 初始化设置目录

        # if not os.path.isfile(self._settings_file_path):
        #     open(self._settings_file_path, "w", encoding="utf-8")  # 初始化文件

        # 检查对应文件是否存在
        # 每次操作完不关闭文件流，就flush一次

    def load(
        self,
        settings_dir_path: str = "",
        settings_file_name: str = "hpyculator_setting",
        settings_file_format: str = "toml",
    ):
        """
        加载一个设置文件对象

        :param settings_dir_path: 设置文件所在目录
        :param settings_file_name: 设置文件的文件名
        :param settings_file_format: 设置文件的类型（后缀）
        :return:
        """
        if not settings_dir_path:
            settings_dir_path = self._settings_dir_path
        return dict_settings_file_object[settings_file_format](
            settings_dir_path, settings_file_name, settings_file_format
        )
        # settings_dir_path = self._settings_dir_path
        # return TomlSettingsFileObject(settings_dir_path,
        #                               settings_file_name,
        #                               settings_file_format)
