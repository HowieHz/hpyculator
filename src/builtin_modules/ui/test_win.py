# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'test_win.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPlainTextEdit,
    QSizePolicy,
    QWidget,
)
from . import main_window_resource_rc


class Ui_TestWin(object):
    def setupUi(self, TestWin):
        if not TestWin.objectName():
            TestWin.setObjectName("TestWin")
        TestWin.resize(1037, 743)
        self.centralwidget = QWidget(TestWin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(50, 50, 731, 531))
        self.label.setStyleSheet(
            "background-image: url(:/background/images/background1.png);\n"
            "border-radius: 20px;"
        )
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(160, 180, 401, 281))
        self.plainTextEdit.setStyleSheet("background-color: rgba(229, 229, 229, 50);")
        TestWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(TestWin)

        QMetaObject.connectSlotsByName(TestWin)

    # setupUi

    def retranslateUi(self, TestWin):
        TestWin.setWindowTitle(
            QCoreApplication.translate("TestWin", "MainWindow", None)
        )
        self.label.setText(QCoreApplication.translate("TestWin", "abcdefg", None))
        self.plainTextEdit.setPlainText(
            QCoreApplication.translate("TestWin", "abcdefg", None)
        )

    # retranslateUi
