from .. import document as doc
from ..ui import Ui_AboutWin
import webbrowser

# pyside6
from PySide6.QtWidgets import QDialog


class AboutWinApp(QDialog):
    def __init__(self):
        """设置窗口，是主窗口的子窗口"""
        super().__init__()
        self.ui = Ui_AboutWin()
        self.ui.setupUi(self)

        self.setWindowTitle("关于 hpyculator")

        self.ui.combo_doc.addItems(["开屏介绍", "更新日志", "使用说明", "关于"])

    def chooseShow(self, QString):
        def showStartShow():  # 开屏介绍
            self.ui.output_doc.setText(doc.START_SHOW)

        def showTODO():  # 更新展望
            self.ui.output_doc.setText(doc.TODO)

        def showUpdataLog():  # 更新日志
            self.ui.output_doc.setText(doc.UPDATE_LOG)

        def showAbout():  # 关于
            # self.ui.output_doc.setText("<img src='..\\ui\\icons\\ico.ico'>")
            self.ui.output_doc.setText(doc.ABOUT)

        jump_map = {
            "开屏介绍": showStartShow,
            "更新日志": showUpdataLog,
            "使用说明": showTODO,
            "关于": showAbout,
        }
        jump_map[QString]()

    def checkUpdate(self):
        """检查更新"""
        webbrowser.open("https://github.com/HowieHz/hpyculator/releases")
