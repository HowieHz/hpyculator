"""运行主程序和主程序的一些初始化"""
import os
from typing import Optional

# from .log import LogManager  # 日志管理 初始化
from .plugin import instance_plugin_manager  # 插件管理
from .settings import instance_settings_file
from .ui_manager import MainWinApp  # 窗口管理类（用于管理设置的窗口）


class CreateApp:
    """运行主程序和主程序的一些初始化"""

    def __init__(self, instance_num: Optional[int] = 1):
        """
        创建app

        :param instance_num: 创建几个实例
        """
        self.instance_num = instance_num

    def run(self):
        """运行主程序"""
        # TODO 路径检查需重构，默认路径改传参
        SETTING_FILE_PATH = instance_settings_file.setting_file_path
        OUTPUT_DIR_PATH = checkOutputPath()  # 输出路径检查
        BACKGROUND_IMG_DIR_PATH = checkBackgroundImgPath()  # 背景图片路径检查
        PLUGIN_DIR_PATH = pluginCheck()  # 插件加载

        list_instance_main_window = []
        for _ in range(self.instance_num):
            list_instance_main_window.append(
                MainWinApp(  # 启动实例
                    SETTING_FILE_PATH,
                    OUTPUT_DIR_PATH,
                    PLUGIN_DIR_PATH,
                    BACKGROUND_IMG_DIR_PATH,
                )
            )  # 实例化主窗口
            list_instance_main_window[_].show()
        return list_instance_main_window


def checkOutputPath():
    """
    检查输出目录

    :return: output_dir_path
    """
    if instance_settings_file.exists("output_dir_path"):
        output_dir_path = instance_settings_file.read("output_dir_path")
    else:
        output_dir_path = str(os.path.join(os.getcwd(), "Output"))
        instance_settings_file.add(key="output_dir_path", value=output_dir_path)
        # print(f"输出文件保存位置:{output_dir_path}")

    # 检查输出文件夹是否存在
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    return output_dir_path


def checkBackgroundImgPath():
    """
    背景图片路径检查

    :return: background_img_dir_path
    """
    # 从设置文件读取输出目录
    if instance_settings_file.exists("background_img_dir_path"):
        background_img_dir_path = instance_settings_file.read("background_img_dir_path")
    else:
        background_img_dir_path = str(os.path.join(os.getcwd(), "background_img"))
        instance_settings_file.add(
            key="background_img_dir_path", value=background_img_dir_path
        )

    # 检查输出文件夹是否存在
    if not os.path.exists(background_img_dir_path):
        os.makedirs(background_img_dir_path)

    return background_img_dir_path


def pluginCheck():
    """
    加载插件

    :return: 存放插件的文件夹路径
    """
    # 从设置文件读取插件目录
    if instance_settings_file.exists("plugin_dir_path"):
        plugin_dir_path = instance_settings_file.read("plugin_dir_path")
    else:
        plugin_dir_path = str(os.path.join(os.getcwd(), "Plugin"))
        instance_settings_file.add(key="plugin_dir_path", value=plugin_dir_path)

    # 检查模块文件夹是否存在
    if not os.path.exists(plugin_dir_path):
        os.makedirs(plugin_dir_path)

    instance_plugin_manager.initPlugin(plugin_dir_path)  # 加载插件

    return plugin_dir_path
