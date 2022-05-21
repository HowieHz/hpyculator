import os
import shelve
from typing import Optional
import logging

from .log import LogManager  # 日志管理 初始化
from .plugin import instance_plugin_manager  # 插件管理
from .ui_manager import MainWinApp  # 窗口管理类（用于管理设置的窗口）


class CreateApp:
    def __init__(self, instance_num: Optional[int] = 1):
        """
        创建app

        :param instance_num: 创建几个实例
        """
        self.instance_num = instance_num

    def run(self):
        # TODO 路径检查需重构，默认路径改传参
        SETTING_FILE_PATH = checkSettingPath()
        OUTPUT_DIR_PATH = checkOutputPath(SETTING_FILE_PATH)  # 输出路径检查
        BACKGROUND_IMG_DIR_PATH = checkBackgroundImgPath(SETTING_FILE_PATH)  # 背景图片路径检查
        PLUGIN_DIR_PATH = pluginCheck(SETTING_FILE_PATH)  # 插件加载

        logCheck(SETTING_FILE_PATH)  # 日志检查

        list_instance_main_window = []
        for _ in range(self.instance_num):
            list_instance_main_window.append(
                MainWinApp(  # 启动实例
                    SETTING_FILE_PATH,
                    OUTPUT_DIR_PATH,
                    PLUGIN_DIR_PATH,
                    BACKGROUND_IMG_DIR_PATH
                )
            )  # 实例化主窗口
            list_instance_main_window[_].show()
        return list_instance_main_window

def checkSettingPath():
    """
    设置文件路径检查

    :return: setting_file_path
    """
    setting_dir_path = str(os.path.join(os.getcwd(), "Setting"))  # 初始化设置目录
    setting_file_path = str(os.path.join(setting_dir_path, "hpyculator_setting"))
    # 初始化设置文件位置
    # 检查存放设置文件的文件夹是否存在
    if not os.path.exists(setting_dir_path):
        os.makedirs(setting_dir_path)

    return setting_file_path

def checkOutputPath(setting_file_path):
    """
    检查输出目录

    :param setting_file_path: 设置文件存放目录
    :return: output_dir_path
    """

    with shelve.open(setting_file_path, writeback=True) as setting_file:
        # 从设置文件读取输出目录
        if "output_dir_path" in setting_file:
            output_dir_path = setting_file["output_dir_path"]
        else:
            output_dir_path = str(os.path.join(os.getcwd(), "Output"))
            setting_file["output_dir_path"] = output_dir_path
        logging.debug(f"输出文件保存位置:{output_dir_path}")

    # 检查输出文件夹是否存在
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    return output_dir_path

def checkBackgroundImgPath(setting_file_path):
    """
    背景图片路径检查

    :return: background_img_dir_path
    """
    with shelve.open(setting_file_path, writeback=True) as setting_file:
        # 从设置文件读取输出目录
        if "background_img_dir_path" in setting_file:
            background_img_dir_path = setting_file["background_img_dir_path"]
        else:
            background_img_dir_path = str(os.path.join(os.getcwd(), "background_img"))
            setting_file["background_img_dir_path"] = background_img_dir_path

    # 检查输出文件夹是否存在
    if not os.path.exists(background_img_dir_path):
        os.makedirs(background_img_dir_path)

    return background_img_dir_path

def logCheck(setting_file_path):
    """
    日志检查

    :return: None
    """
    # 检查存放日志文件的文件夹是否存在
    LogManager(setting_file_path).checkIsEnableLog()


def pluginCheck(setting_file_path):
    """
    加载插件

    :param setting_file_path: 设置文件的文木
    :return: 存放插件的文件夹路径
    """
    with shelve.open(setting_file_path, writeback=True) as setting_file:
        # 从设置文件读取插件目录
        if "plugin_dir_path" in setting_file:
            plugin_dir_path = setting_file["plugin_dir_path"]
        else:
            plugin_dir_path = str(os.path.join(os.getcwd(), "Plugin"))
            setting_file["plugin_dir_path"] = plugin_dir_path

    # 检查模块文件夹是否存在
    if not os.path.exists(plugin_dir_path):
        os.makedirs(plugin_dir_path)

    instance_plugin_manager.initPlugin(plugin_dir_path)  # 加载插件

    return plugin_dir_path
