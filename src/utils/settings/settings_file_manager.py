# read
# modify
# add
# delete
# flush

# todo toml
# todo xml
# todo ini
# todo json
# todo yaml

from typing import Any
from toml_file_object import TomlSettingsFileObject

dict_settings_file_object = {
    "toml": TomlSettingsFileObject
}


class SettingsManager:
    def __init__(self):
        """
        初始化设置文件管理

        :param settings_file_format: 配置文件格式
        """
        self._settings_dir_path = str(os.path.join(os.getcwd(), "Setting"))  # 初始化设置目录

        # if not os.path.isfile(self._settings_file_path):
        #     open(self._settings_file_path, "w", encoding="utf-8")  # 初始化文件

        # 检查对应文件是否存在
        # 每次操作完不关闭文件流，就flush一次

    def load(self,
             settings_dir_path: str = self._settings_dir_path,
             settings_file_name: str = "hpyculator_setting",
             settings_file_format: str = "toml"):
        return dict_settings_file_object[settings_file_format](settings_dir_path,
                                                               settings_file_name,
                                                               settings_file_format)
