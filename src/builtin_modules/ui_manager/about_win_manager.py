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

        self.ui.combo_doc.addItems([_("开屏介绍"), _("更新日志"), _("使用说明"), _("关于")])

    def event_choose_show(self, qstring):
        def _show_start_show():  # 开屏介绍
            self.ui.output_doc.setText(doc.START_SHOW)

        def _show_todo():  # 更新展望
            self.ui.output_doc.setText(doc.TODO)

        def _show_updata_log():  # 更新日志
            self.ui.output_doc.setText(doc.UPDATE_LOG)

        def _show_about():  # 关于
            # self.ui.output_doc.setText("<img src='..\\ui\\icons\\ico.ico'>")
            self.ui.output_doc.setText(doc.ABOUT)

        dict_jump_map = {
            _("开屏介绍"): _show_start_show,
            _("更新日志"): _show_updata_log,
            _("使用说明"): _show_todo,
            _("关于"): _show_about,
        }
        dict_jump_map[qstring]()

    def event_check_update(self):
        """检查更新"""
        webbrowser.open("https://github.com/HowieHz/hpyculator/releases")
