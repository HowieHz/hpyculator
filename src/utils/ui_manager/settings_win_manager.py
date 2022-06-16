import os

# pyside6
from PySide6.QtWidgets import QDialog, QMessageBox

from .. import document as doc
from ..document import VERSION  # 版本号导入
from ..settings import instance_settings_file  # 导入实例
from ..ui import Ui_SettingsWin  # 从init导


class SettingsWinApp(QDialog):
    """设置窗口的操作"""

    def __init__(self):
        """设置窗口，是主窗口的子窗口"""
        super().__init__()
        self.ui = Ui_SettingsWin()  # 实例化ui
        self.ui.setupUi(self)  # 初始化ui，不初始化不显示

        self.setWindowTitle(
            f"{doc.SETTINGS_LITERAL} Hpyculator {doc.VERSION_LITERAL}{VERSION}"
        )  # 设置标题

        if instance_settings_file.exists("output_dir_path"):
            # 读取目录设置
            self.OUTPUT_DIR_PATH = instance_settings_file.read("output_dir_path")
            self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)

        # 读取保存选项状态设置
        if instance_settings_file.exists("is_save_check_box_status"):
            self.ui.check_is_save_check_box_status.setChecked(
                instance_settings_file.read("is_save_check_box_status")
            )

        # 背景图片选择框初始化
        self.background_dir_path = os.path.join(".", "background_img")
        self.ui.combo_background.clear()  # 清空选框
        self.ui.combo_background.addItems(
            os.listdir(self.background_dir_path)
        )  # 相对入口文件位置
        if instance_settings_file.exists("background_img"):
            self.ui.combo_background.setCurrentText(
                instance_settings_file.read("background_img")
            )

    def eventSaveSettings(self):
        """
        按下保存按钮之后的事件

        :return:
        """
        (
            instance_settings_file.modify(
                key="output_dir_path", value=self.ui.output_save_location.toPlainText()
            ).modify(
                key="is_save_check_box_status",
                value=self.ui.check_is_save_check_box_status.isChecked(),
            )
        )
        QMessageBox.information(self, doc.SAVED_LITERAL, doc.SAVED_TIPS, QMessageBox.Ok)
        self.close()

    def eventCancelSettings(self):
        self.close()

    def eventSaveCheckBoxStatus(self):
        """
        占位用，因为都是最后统一读取写入设置文件的
        """

    def eventResetSaveLocation(self):
        """重置保存路径"""
        self.OUTPUT_DIR_PATH = os.path.join(os.getcwd(), "Output")
        instance_settings_file.modify(key="output_dir_path", value=self.OUTPUT_DIR_PATH)
        self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)

    def eventChooseBackgroundImg(self, int_):
        """选择背景图片"""
        instance_settings_file.modify(
            key="background_img", value=self.ui.combo_background.currentText()
        )

    @staticmethod
    def eventOpenBackgroundDir():
        """
        打开存储背景图片的文件夹

        :return:
        """
        os.system(f'explorer {instance_settings_file.read("background_img_dir_path")}')

    @staticmethod
    def eventOpenPluginDir():
        """
        打开储存插件的文件架

        :return:
        """
        os.system(f'explorer {instance_settings_file.read("plugin_dir_path")}')
