import shelve
import os

# pyside6
from PySide6.QtWidgets import QMessageBox, QDialog

from ..ui import Ui_SettingWindow  # 从init导
from ..document import VERSION  # 版本号导入

# 远程包
from hpyculator.hpysignal import setting_window_signal


class SettingWindowApplication(QDialog):
    def __init__(self):
        """设置窗口，是主窗口的子窗口"""
        super().__init__()
        self.ui = Ui_SettingWindow()  # 实例化ui
        self.ui.setupUi(self)  # 初始化ui，不初始化不显示

        self.setting_signal = setting_window_signal  # 方便调用自定义信号

        self.setWindowTitle(f"设置  Hpyculator版本{VERSION}")  # 设置标题

        # 初始化设置目录
        self.SETTING_DIR_PATH = str(os.path.join(os.getcwd(), "Setting"))
        self.SETTING_FILE_PATH = str(
            os.path.join(self.SETTING_DIR_PATH, "hpyculator_setting")
        )

        with shelve.open(
            self.SETTING_FILE_PATH, writeback=True
        ) as setting_file:  # 读取设置文件
            # 读取目录设置
            self.OUTPUT_DIR_PATH = setting_file["save_location"]
            self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)

            # 读取保存选项状态设置
            self.ui.save_setting_check.setChecked(setting_file["is_save_settings"])

            # 读取保存日志文件设置
            self.ui.save_log_check.setChecked(setting_file["save_log"])

    def saveSetting(self):
        """按下保存按钮之后的事件

        :return:
        """
        with shelve.open(
            self.SETTING_FILE_PATH, writeback=True
        ) as setting_file:  # 读取设置文件
            # 读取目录设置
            setting_file["save_location"] = self.ui.output_save_location.toPlainText()
            setting_file["is_save_settings"] = self.ui.save_setting_check.isChecked()
            setting_file["save_log"] = self.ui.save_log_check.isChecked()

        QMessageBox.information(self, "保存完成", "保存完成\n部分设置将在重新启动后生效", QMessageBox.Ok)
        self.close()

    def cancelSetting(self):
        self.close()

    @staticmethod
    def saveSettingCheckEvent():
        """占位用，因为都是最后统一读取写入的

        :return:
        """
        return

    @staticmethod
    def saveLogCheckEvent():
        """占位用，因为都是最后统一读取写入的

        :return:
        """
        return
