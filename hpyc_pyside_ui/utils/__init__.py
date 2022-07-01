"""运行主程序和主程序的一些初始化"""
import os
from .ui_manager import MainWinApp  # 窗口管理类（用于管理设置的窗口）
from .var import instance_core


class CreateApp:
    """运行主程序和主程序的一些初始化"""

    def __init__(self, instance_num: int = 1):
        """创建app

        :param instance_num: 创建几个实例, 默认为1
        :type instance_num: int
        """
        self.instance_num = instance_num

    def run(self) -> list[MainWinApp]:
        """运行主程序

        :return: 一个列表里面有启动的主窗口实例
        :rtype: list[MainWinApp]
        """
        # TODO 路径检查需重构，默认路径改传参
        SETTINGS_DIR_PATH = instance_core.getSettingsDirPath()
        OUTPUT_DIR_PATH = instance_core.getOutputDirPath()
        PLUGINS_DIR_PATH = instance_core.getPluginsDirPath()
        message_queue = instance_core.getMessageQueue()

        self.instance_settings_file = instance_core.getSettingsFileInstance()
        BACKGROUND_IMG_DIR_PATH = self.checkBackgroundImgPath()  # 背景图片路径检查

        list_instance_main_window = []
        for _ in range(self.instance_num):
            list_instance_main_window.append(
                MainWinApp(  # 启动实例
                    setting_file_path=SETTINGS_DIR_PATH,
                    output_dir_path=OUTPUT_DIR_PATH,
                    plugins_dir_path=PLUGINS_DIR_PATH,
                    background_dir_path=BACKGROUND_IMG_DIR_PATH,
                    message_queue=message_queue,
                    instance_settings=self.instance_settings_file,
                )
            )  # 实例化主窗口
            list_instance_main_window[_].show()
        return list_instance_main_window

    def checkBackgroundImgPath(self) -> str:
        """背景图片路径检查

        :return: 存放背景图片的路径
        :rtype: str
        """
        # 从设置文件读取输出目录
        if self.instance_settings_file.exists("background_img_dir_path"):
            background_img_dir_path = self.instance_settings_file.read(
                "background_img_dir_path"
            )
        else:
            background_img_dir_path = str(os.path.join(os.getcwd(), "background_img"))
            self.instance_settings_file.add(
                key="background_img_dir_path", value=background_img_dir_path
            )

        # 检查输出文件夹是否存在
        if not os.path.exists(background_img_dir_path):
            os.makedirs(background_img_dir_path)

        return background_img_dir_path
