import shelve
import os

# pyside6
from PySide6.QtWidgets import QMessageBox, QDialog

from ..ui import Ui_SettingWin  # 从init导
from ..document import VERSION  # 版本号导入


class SettingWinApp(QDialog):
    def __init__(self):
        """设置窗口，是主窗口的子窗口"""
        super().__init__()
        self.ui = Ui_SettingWin()  # 实例化ui
        self.ui.setupUi(self)  # 初始化ui，不初始化不显示

        self.setWindowTitle(f"设置  Hpyculator版本{VERSION}")  # 设置标题

        # 初始化设置目录
        self.SETTING_DIR_PATH = str(os.path.join(os.getcwd(), "Setting"))
        self.SETTING_FILE_PATH = str(os.path.join(self.SETTING_DIR_PATH, "hpyculator_setting"))

        with shelve.open(
                self.SETTING_FILE_PATH, writeback=True
        ) as setting_file:  # 读取设置文件
            # 读取目录设置
            self.OUTPUT_DIR_PATH = setting_file["output_dir_path"]
            self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)

            # 读取保存选项状态设置
            self.ui.check_is_save_check_box.setChecked(setting_file["is_save_settings"])

            # 读取保存日志文件设置
            self.ui.check_is_save_log.setChecked(setting_file["is_save_log"])

    def saveSetting(self):
        """
        按下保存按钮之后的事件

        :return:
        """
        with shelve.open(
                self.SETTING_FILE_PATH, writeback=True
        ) as setting_file:  # 读取设置文件
            # 读取目录设置
            setting_file["output_dir_path"] = self.ui.output_save_location.toPlainText()
            setting_file["is_save_settings"] = self.ui.check_is_save_check_box.isChecked()
            setting_file["is_save_log"] = self.ui.check_is_save_log.isChecked()

        QMessageBox.information(self, "保存完成", "保存完成\n部分设置将在重新启动后生效", QMessageBox.Ok)
        self.close()

    def cancelSetting(self):
        self.close()

    def saveSettingCheckEvent(self):
        """
        占位用，因为都是最后统一读取写入设置文件的
        """

    def saveLogCheckEvent(self):
        """
        占位用，因为都是最后统一读取写入设置文件的
        """

    def resetSaveLocationEvnet(self):
        """重置保存路径"""
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:
            self.OUTPUT_DIR_PATH = setting_file["output_dir_path"] = os.path.join(os.getcwd(), "Output")
            self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)

    def chooseBackgroundImg(self, QString):
        """选择背景图片"""
        # TODO Finish
        return

    def openBackgroundDirEvent(self):
        """
        打开存储背景图片的文件夹

        :return:
        """
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:
            os.system(f'explorer {setting_file["background_img_dir_path"]}')

    def openPluginDirEvent(self):
        """
        打开储存插件的文件架

        :return:
        """
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:
            os.system(f'explorer {setting_file["plugin_dir_path"]}')