# pyside6 ui signal导入
from PySide6.QtCore import Qt, QObject, QEvent, QSize, QRect
from PySide6.QtGui import QIcon, QPixmap, QPalette, QBrush
from PySide6.QtWidgets import *
from requests import get
from os.path import exists
import logging


import logging
from ..ui import Ui_TestWin
from requests import get
from os.path import exists


class testWinApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TestWin()  # UI类的实例化()
        self.ui.setupUi(self)  # ui初始化
        self.setWindowTitle("hpyculator test")  # 设置标题

        op = QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        self.ui.plainTextEdit.setGraphicsEffect(op)
        self.ui.plainTextEdit.setAutoFillBackground(True)
        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        # op.setEnabled(True)
        # self.ui.output_box.setAutoFillBackground(True)
        #
        # op2 = QGraphicsBlurEffect()
        # op2.setBlurRadius(12)
        # self.setGraphicsEffect(op2)
        # 2.窗口及其上面的控件都半透明：
        # self.setWindowOpacity(0.7)
        self.show()
