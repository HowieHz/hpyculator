import toml
import os
import pathlib

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

        self.setWindowTitle(_("设置") + "  Hpyculator" + _("版本") + f"{VERSION}")  # 设置标题

        # 初始化设置目录
        self.SETTING_DIR_PATH = str(os.path.join(os.getcwd(), "Setting"))
        self.SETTING_FILE_PATH = str(
            os.path.join(self.SETTING_DIR_PATH, "hpyculator_setting.toml")
        )

        # 从设置文件读取插件目录
        dict_setting = toml.load(self.SETTING_FILE_PATH)
        if "output_dir_path" in dict_setting:
            # 读取目录设置
            self.OUTPUT_DIR_PATH = dict_setting["output_dir_path"]
            self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)

        # 读取保存选项状态设置
        if "is_save_check_box_status" in dict_setting:
            self.ui.check_is_save_check_box.setChecked(
                dict_setting["is_save_check_box_status"]
            )

        # 背景图片选择框初始化
        self.background_dir_path = os.path.join(".", "background_img")
        self.ui.combo_background.clear()  # 清空选框
        self.ui.combo_background.addItems(
            os.listdir(self.background_dir_path)
        )  # 相对入口文件位置
        if "background_img" in dict_setting:
            self.ui.combo_background.setCurrentText(dict_setting["background_img"])

    def event_save_setting(self):
        """
        按下保存按钮之后的事件

        :return:
        """
        dict_setting = toml.load(self.SETTING_FILE_PATH)
        dict_setting["output_dir_path"] = self.ui.output_save_location.toPlainText()
        dict_setting[
            "is_save_check_box_status"
        ] = self.ui.check_is_save_check_box.isChecked()
        with open(self.SETTING_FILE_PATH, "w+", encoding="utf-8") as setting_file:
            toml.dump(dict_setting, setting_file)

        QMessageBox.information(
            self, _("保存完成"), _("保存完成\n部分设置将在重新启动后生效"), QMessageBox.Ok
        )
        self.close()

    def event_cancel_setting(self):
        self.close()

    def event_save_setting_check(self):
        """
        占位用，因为都是最后统一读取写入设置文件的
        """

    def event_reset_save_location(self):
        """重置保存路径"""
        dict_setting = toml.load(self.SETTING_FILE_PATH)
        dict_setting["output_dir_path"] = self.OUTPUT_DIR_PATH = os.path.join(
            os.getcwd(), "Output"
        )
        self.ui.output_save_location.setPlainText(self.OUTPUT_DIR_PATH)
        with open(
            self.SETTING_FILE_PATH, "w+", encoding="utf-8"
        ) as setting_file:  # 写入配置文件
            toml.dump(dict_setting, setting_file)

    def event_choose_background_img(self, qstring):
        """选择背景图片"""
        dict_setting = toml.load(self.SETTING_FILE_PATH)
        dict_setting["background_img"] = qstring
        with open(
            self.SETTING_FILE_PATH, "w+", encoding="utf-8"
        ) as setting_file:  # 写入配置文件
            toml.dump(dict_setting, setting_file)
        # background_img_path = pathlib.Path(self.background_dir_path).joinpath(qstring)
        # if background_img_path.is_file():
        #     self.bg_img = QPixmap(background_img_path)
        return

    def event_open_background_dir(self):
        """
        打开存储背景图片的文件夹

        :return:
        """
        dict_setting = toml.load(self.SETTING_FILE_PATH)
        os.system(f'explorer {dict_setting["background_img_dir_path"]}')

    def event_open_plugin_dir(self):
        """
        打开储存插件的文件架

        :return:
        """
        dict_setting = toml.load(self.SETTING_FILE_PATH)
        os.system(f'explorer {dict_setting["plugin_dir_path"]}')
