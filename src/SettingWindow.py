#import json
#import time
#import webbrowser
#import os
import shelve
import os
#import importlib
#import pyperclip

from PySide6.QtWidgets import QMainWindow,QMessageBox

from ui.SettingWindow import Ui_SettingWindow

from ui.Signal import setting_window_signal

from Version import VERSION

class SettingApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SettingWindow()#实例化ui
        self.ui.setupUi(self)#初始化ui，不初始化不显示
        self.band()  # 自定义槽

        self.setting_signal = setting_window_signal#方便调用自定义信号

        self.setWindowTitle(f"设置  Hpyculator版本{VERSION}")#设置标题

        # 初始化设置目录
        self.SETTING_DIR_PATH = str(os.path.join(os.getcwd(), 'Setting'))
        print(f'SETTING_DIR:{self.SETTING_DIR_PATH}')
        self.SETTING_FILE_PATH = str(os.path.join(self.SETTING_DIR_PATH, 'hpyculator_setting'))

        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
            # 读取目录设置
            self.OUTPUT_DIR_PATH = setting_file['save_location']
            self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)

    def band(self):
        pass

    def save_setting(self):
        #保存目录设置
        with shelve.open(self.SETTING_FILE_PATH, writeback=True) as setting_file:  # 读取设置文件
            # 读取目录设置
            setting_file['save_location']=self.ui.output_save_location.toPlainText()

        QMessageBox.information(self,"保存完成","保存完成",QMessageBox.Ok)
        self.close()

    def cancel_setting(self):
        self.close()