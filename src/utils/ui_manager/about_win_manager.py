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

        self.setWindowTitle(_("关于 hpyculator"))

        self.ui.combo_doc.addItems([_("开屏介绍"), _("更新日志"), _("关于")])

    def eventChooseShow(self, qstring):
        def _showStartShow():  # 开屏介绍
            self.ui.output_doc.setText(doc.START_SHOW)

        def _showUpdataLog():  # 更新日志
            self.ui.output_doc.setText(doc.CHANGELOG)

        def _showAbout():  # 关于
            # self.ui.output_doc.setText("<img src='..\\ui\\icons\\ico.ico'>")
            self.ui.output_doc.setText(doc.ABOUT)

        dict_jump_map = {
            _("开屏介绍"): _showStartShow,
            _("更新日志"): _showUpdataLog,
            _("关于"): _showAbout,
        }
        dict_jump_map[qstring]()

    @staticmethod
    def eventCheckUpdate():
        """检查更新"""
        webbrowser.open("https://github.com/HowieHz/hpyculator/releases")
