# coding:utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel
from framelesswindow import FramelessWindow


class Window(FramelessWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.label = QLabel(self)
        self.label.setScaledContents(True)
        self.label.setPixmap(QPixmap("resource/images/shoko.png"))
        self.setWindowTitle("PyQt Frameless Window")
        self.setStyleSheet("background:white")
        # self.titleBar.raise_()

    def resizeEvent(self, e):
        # don't forget to call the resizeEvent() of super class
        super().resizeEvent(e)
        length = min(self.width(), self.height())
        self.label.resize(length, length)
        self.label.move(
            self.width() // 2 - length // 2,
            self.height() // 2 - length // 2
        )


if __name__ == "__main__":
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # run app
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec())
