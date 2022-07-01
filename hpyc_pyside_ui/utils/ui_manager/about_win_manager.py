import webbrowser

# pyside6
from PySide6.QtWidgets import QDialog

from .. import document as doc
from ..ui import Ui_AboutWin


class AboutWinApp(QDialog):
    def __init__(self):
        """设置窗口，是主窗口的子窗口"""
        super().__init__()
        self.ui = Ui_AboutWin()
        self.ui.setupUi(self)

        self.setWindowTitle(doc.ABOUT_HPYCULATOR_LITERAL)

        self.ui.combo_doc.addItems(
            [
                doc.INTRODUCTION_LITERAL,
                doc.CHANGELOG_LITERAL,
                doc.ABOUT_LITERAL,
            ]
        )

        self.ui.button_check_update.setText(doc.CHECK_UPDATE_LITERAL)

    def eventChooseShow(self, qstring) -> None:
        """选择对应文档并显示"""
        match qstring:
            case doc.INTRODUCTION_LITERAL:
                self.ui.output_doc.setText(doc.START_SHOW)
            case doc.CHANGELOG_LITERAL:
                self.ui.output_doc.setText(doc.CHANGELOG)
            case doc.ABOUT_LITERAL:
                # self.ui.output_doc.setText("<img src='..\\ui\\icons\\ico.ico'>")
                self.ui.output_doc.setText(doc.ABOUT)

    @staticmethod
    def eventCheckUpdate() -> None:
        """检查更新"""
        webbrowser.open("https://github.com/HowieHz/hpyculator/releases")
