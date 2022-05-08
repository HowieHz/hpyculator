import shelve
import os

from PySide6.QtWidgets import QMessageBox, QDialog

from ui.setting_window import Ui_SettingWindow

from hpyculator import setting_window_signal

from Doc import VERSION  # 版本号导入


class SettingApplication(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingWindow()  # 实例化ui
        self.ui.setupUi(self)  # 初始化ui，不初始化不显示
        self.band()  # 自定义槽

        self.setting_signal = setting_window_signal  # 方便调用自定义信号

        self.setWindowTitle(f"设置  Hpyculator版本{VERSION}")  # 设置标题

        # 初始化设置目录
        self.SETTING_DIR_PATH = str(os.path.join(os.getcwd(), 'Setting'))
        self.SETTING_FILE_PATH = str(os.path.join(self.SETTING_DIR_PATH, 'hpyculator_setting'))

        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
            # 读取目录设置
            self.OUTPUT_DIR_PATH = setting_file['save_location']
            self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)

            # 读取保存选项状态设置
            self.ui.save_setting_check.setChecked(setting_file['save_settings'])

            # 读取保存日志文件设置
            self.ui.save_log_check.setChecked(setting_file['save_log'])

    def band(self):
        pass

    def saveSetting(self):
        # 保存目录设置
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
            # 读取目录设置
            setting_file['save_location'] = self.ui.output_save_location.toPlainText()
            setting_file['save_settings'] = self.ui.save_setting_check.isChecked()
            setting_file['save_log'] = self.ui.save_log_check.isChecked()

        QMessageBox.information(self, "保存完成", "保存完成\n部分设置将在重新启动后生效", QMessageBox.Ok)
        self.close()
        return

    def cancelSetting(self):
        self.close()
        return

    def saveSettingCheckEvent(self):
        return

    def saveLogCheckEvent(self):
        return
