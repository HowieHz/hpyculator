import os
import shelve
import sys
# from hpyculator import hpycore as hpyc
# from builtin_modules import document as doc

import logging  # 日志导入
from builtin_modules.log_manager import LogManager  # 日志管理 初始化
from builtin_modules.plugin_manager import instance_plugin_manager  # 插件管理

# pyside6导入
from PySide6.QtWidgets import QApplication

# 窗口管理类（用于管理设置的窗口）
from builtin_modules.ui_manager import MainWindowApplication


class Main:
    def __init__(self):
        GLOBAL_SETTING_FILE_PATH, GLOBAL_OUTPUT_DIR_PATH = self.pathCheck()  # 路径检查
        self.logCheck(GLOBAL_SETTING_FILE_PATH)  # 日志检查
        global_plugin_option_id_dict = self.pluginCheck()  # 插件加载

        main_window = MainWindowApplication(GLOBAL_SETTING_FILE_PATH, GLOBAL_OUTPUT_DIR_PATH, global_plugin_option_id_dict)  # 实例化主窗口
        main_window.show()  # 展示主窗口

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


if __name__ == '__main__':

    app = QApplication(sys.argv)  # 启动一个应用
    instance_main = Main()
    sys.exit(app.exec())  # 避免程序执行到这一行后直接退出
