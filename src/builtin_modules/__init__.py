import os
import toml
from typing import Optional

# from .log import LogManager  # 日志管理 初始化
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
        SETTING_FILE_PATH = check_setting_path()
        OUTPUT_DIR_PATH = check_output_path(SETTING_FILE_PATH)  # 输出路径检查
        BACKGROUND_IMG_DIR_PATH = check_background_img_path(SETTING_FILE_PATH)  # 背景图片路径检查
        PLUGIN_DIR_PATH = plugin_check(SETTING_FILE_PATH)  # 插件加载

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


def check_setting_path():
    """
    设置文件路径检查

    :return: setting_file_path
    """
    setting_dir_path = str(os.path.join(os.getcwd(), "Setting"))  # 初始化设置目录
    setting_file_path = str(os.path.join(setting_dir_path, "hpyculator_setting.toml"))
    # 初始化设置文件位置
    # 检查存放设置文件的文件夹是否存在
    if not os.path.exists(setting_dir_path):
        os.makedirs(setting_dir_path)

    if not os.path.isfile(setting_file_path):
        open(setting_file_path,"w",encoding='utf-8')  # 初始化文件

    return setting_file_path


def check_output_path(setting_file_path):
    """
    检查输出目录

    :param setting_file_path: 设置文件存放目录
    :return: output_dir_path
    """
    dict_setting = toml.load(setting_file_path)
    if "output_dir_path" in dict_setting:
        output_dir_path = dict_setting["output_dir_path"]
    else:
        output_dir_path = str(os.path.join(os.getcwd(), "Output"))
        with open(setting_file_path, 'a+', encoding='utf-8') as setting_file:
            toml.dump({"output_dir_path" : output_dir_path},setting_file)
        # print(f"输出文件保存位置:{output_dir_path}")

    # 检查输出文件夹是否存在
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    return output_dir_path


def check_background_img_path(setting_file_path):
    """
    背景图片路径检查

    :return: background_img_dir_path
    """
    # 从设置文件读取输出目录
    dict_setting = toml.load(setting_file_path)
    if "background_img_dir_path" in dict_setting:
        background_img_dir_path = dict_setting["background_img_dir_path"]
    else:
        background_img_dir_path = str(os.path.join(os.getcwd(), "background_img"))
        with open(setting_file_path, 'a+', encoding='utf-8') as setting_file:
            toml.dump({"background_img_dir_path" : background_img_dir_path},setting_file)

    # 检查输出文件夹是否存在
    if not os.path.exists(background_img_dir_path):
        os.makedirs(background_img_dir_path)

    return background_img_dir_path


def plugin_check(setting_file_path):
    """
    加载插件

    :param setting_file_path: 设置文件的文木
    :return: 存放插件的文件夹路径
    """
    # 从设置文件读取插件目录
    dict_setting = toml.load(setting_file_path)
    if "plugin_dir_path" in dict_setting:
        plugin_dir_path = dict_setting["plugin_dir_path"]
    else:
        plugin_dir_path = str(os.path.join(os.getcwd(), "Plugin"))
        with open(setting_file_path, 'a+', encoding='utf-8') as setting_file:
            toml.dump({"plugin_dir_path": plugin_dir_path}, setting_file)

    # 检查模块文件夹是否存在
    if not os.path.exists(plugin_dir_path):
        os.makedirs(plugin_dir_path)

    instance_plugin_manager.init_plugin(plugin_dir_path)  # 加载插件

    return plugin_dir_path
