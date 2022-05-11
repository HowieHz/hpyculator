import os
import shelve
import sys
# from hpyculator import hpycore as hpyc
# from builtin_modules import document as doc

import logging  # 日志导入
from .log_manager import LogManager  # 日志管理 初始化
from .plugin_manager import instance_plugin_manager  # 插件管理

# pyside6导入
from PySide6.QtWidgets import QApplication

# 窗口管理类（用于管理设置的窗口）
from .ui_manager import MainWindowApplication

# 类型标注
from typing import Optional


class CreateApp:
    def __init__(self, multiple: Optional[int] = False, test=False):
        """
        创建app

        :param multiple: 创建几个实例
        """
        self.multiple = multiple
        self.test = test
        if not test:
            self.app = QApplication(sys.argv)  # 启动一个应用

    def run(self):
        GLOBAL_SETTING_FILE_PATH, GLOBAL_OUTPUT_DIR_PATH = self.pathCheck()  # 路径检查
        self.logCheck(GLOBAL_SETTING_FILE_PATH)  # 日志检查
        global_plugin_option_id_dict = self.pluginCheck()  # 插件加载
        if self.multiple:
            app_list = []
            for _ in range(self.multiple):
                app_list.append(MainWindowApplication(GLOBAL_SETTING_FILE_PATH,
                                                      GLOBAL_OUTPUT_DIR_PATH,
                                                      global_plugin_option_id_dict))  # 实例化主窗口
                app_list[_].show()
        else:
            main_window = MainWindowApplication(GLOBAL_SETTING_FILE_PATH,
                                                GLOBAL_OUTPUT_DIR_PATH,
                                                global_plugin_option_id_dict)  # 实例化主窗口
            main_window.show()  # 展示主窗口
        if not self.test:
            sys.exit(self.app.exec())  # 避免程序执行到这一行后直接退出
        else:
            return self.app

    @staticmethod
    def pathCheck():
        """
        路径检查

        :return: setting_file_path, output_dir_path
        """

        setting_dir_path = str(os.path.join(os.getcwd(), 'Setting'))  # 初始化设置目录
        setting_file_path = str(os.path.join(setting_dir_path, 'hpyculator_setting'))  # 初始化设置文件位置

        # 检查存放设置文件的文件夹是否存在
        if not os.path.exists(setting_dir_path):
            os.makedirs(setting_dir_path)

        with shelve.open(setting_file_path, writeback=True) as setting_file:
            # 从设置文件读取输出目录
            try:
                output_dir_path = setting_file['save_location']
            except KeyError:
                output_dir_path = str(os.path.join(os.getcwd(), 'Output'))
                setting_file['save_location'] = output_dir_path
            logging.debug(f'输出文件保存位置:{output_dir_path}')

        # 检查输出文件夹是否存在
        if not os.path.exists(output_dir_path):
            os.makedirs(output_dir_path)

        return setting_file_path, output_dir_path

    @staticmethod
    def logCheck(setting_file_path):
        """
        日志检查

        :return: None
        """
        # 检查存放日志文件的文件夹是否存在
        LogManager(setting_file_path).checkIsEnableLog()
        return None

    @staticmethod
    def pluginCheck():
        """
        加载插件

        :return: plugin_option_id_dict, loaded_plugin
        """
        return instance_plugin_manager.initPlugin()  # 加载插件
