# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'setting_win.ui'
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
    QCheckBox,
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QTextEdit,
    QWidget,
)


class Ui_SettingWin(object):
    def setupUi(self, SettingWin):
        if not SettingWin.objectName():
            SettingWin.setObjectName("SettingWin")
        SettingWin.resize(640, 480)
        SettingWin.setMinimumSize(QSize(640, 480))
        SettingWin.setMaximumSize(QSize(640, 480))
        SettingWin.setStyleSheet(
            "/*\n"
            "Aqua Style Sheet for QT Applications\n"
            "Author: Jaime A. Quiroga P.\n"
            "Company: GTRONICK\n"
            "Last updated: 22/01/2019, 07:55.\n"
            "Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
            "*/\n"
            "QMainWindow {\n"
            "	background-color:#ececec;\n"
            "}\n"
            "QTextEdit {\n"
            "	border-width: 1px;\n"
            "	border-style: solid;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QPlainTextEdit {\n"
            "	border-width: 1px;\n"
            "	border-style: solid;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QToolButton {\n"
            "	border-style: solid;\n"
            "	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
            "	border-left"
            "-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
            "	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-width: 1px;\n"
            "	border-radius: 5px;\n"
            "	color: rgb(0,0,0);\n"
            "	padding: 2px;\n"
            "	background-color: rgb(255,255,255);\n"
            "}\n"
            "QToolButton:hover{\n"
            "	border-style: solid;\n"
            "	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
            "	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
            "	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
            "	border-width: 1px;\n"
            "	border-rad"
            "ius: 5px;\n"
            "	color: rgb(0,0,0);\n"
            "	padding: 2px;\n"
            "	background-color: rgb(255,255,255);\n"
            "}\n"
            "QToolButton:pressed{\n"
            "	border-style: solid;\n"
            "	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
            "	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-width: 1px;\n"
            "	border-radius: 5px;\n"
            "	color: rgb(0,0,0);\n"
            "	padding: 2px;\n"
            "	background-color: rgb(142,142,142);\n"
            "}\n"
            "QPushButton{\n"
            "	border-style: solid;\n"
            "	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-righ"
            "t-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
            "	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-width: 1px;\n"
            "	border-radius: 5px;\n"
            "	color: rgb(0,0,0);\n"
            '	font: 16pt "Microsoft YaHei UI";\n'
            "	padding: 10px;\n"
            "	background-color: rgb(255,255,255);\n"
            "}\n"
            "QPushButton::default{\n"
            "	border-style: solid;\n"
            "	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217"
            "));\n"
            "	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-width: 1px;\n"
            "	border-radius: 5px;\n"
            "	color: rgb(0,0,0);\n"
            '	font: 16pt "Microsoft YaHei UI";\n'
            "	padding: 10px;\n"
            "	background-color: rgb(255,255,255);\n"
            "}\n"
            "QPushButton:hover{\n"
            "	border-style: solid;\n"
            "	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
            "	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
            "	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
            "	border-width: 1px;\n"
            "	border-radius: 5px;\n"
            "	color: rgb(0,0,0);\n"
            "	padding: 2px;\n"
            "	background-color"
            ": rgb(255,255,255);\n"
            "}\n"
            "QPushButton:pressed{\n"
            "	border-style: solid;\n"
            "	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
            "	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-width: 1px;\n"
            "	border-radius: 5px;\n"
            "	color: rgb(0,0,0);\n"
            "	padding: 2px;\n"
            "	background-color: rgb(142,142,142);\n"
            "}\n"
            "QPushButton:disabled{\n"
            "	border-style: solid;\n"
            "	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, "
            "stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
            "	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
            "	border-width: 1px;\n"
            "	border-radius: 5px;\n"
            "	color: #808086;\n"
            "	padding: 2px;\n"
            "	background-color: rgb(142,142,142);\n"
            "}\n"
            "QLineEdit {\n"
            "	border-width: 1px; border-radius: 4px;\n"
            "	border-style: solid;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QLabel {\n"
            "	color: #000000;\n"
            "}\n"
            "QLCDNumber {\n"
            "	color: rgb(0, 113, 255, 255);\n"
            "}\n"
            "QProgressBar {\n"
            "	text-align: center;\n"
            "	color: rgb(240, 240, 240);\n"
            "	border-width: 1px; \n"
            "	border-radius: 10px;\n"
            "	border-color: rgb(230, 230, 230);\n"
            "	border-style: solid;\n"
            "	background-color:rgb(207,207,207);\n"
            ""
            "}\n"
            "QProgressBar::chunk {\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
            "	border-radius: 10px;\n"
            "}\n"
            "QMenuBar {\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
            "}\n"
            "QMenuBar::item {\n"
            "	color: #000000;\n"
            "  	spacing: 3px;\n"
            "  	padding: 1px 4px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
            "}\n"
            "\n"
            "QMenuBar::item:selected {\n"
            "  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #FFFFFF;\n"
            "}\n"
            "QMenu::item:selected {\n"
            "	border-style: solid;\n"
            "	border-top-color: transparent;\n"
            "	border-right-color: transparent;\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, "
            "stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	border-bottom-color: transparent;\n"
            "	border-left-width: 2px;\n"
            "	color: #000000;\n"
            "	padding-left:15px;\n"
            "	padding-top:4px;\n"
            "	padding-bottom:4px;\n"
            "	padding-right:7px;\n"
            "}\n"
            "QMenu::item {\n"
            "	border-style: solid;\n"
            "	border-top-color: transparent;\n"
            "	border-right-color: transparent;\n"
            "	border-left-color: transparent;\n"
            "	border-bottom-color: transparent;\n"
            "	border-bottom-width: 1px;\n"
            "	color: #000000;\n"
            "	padding-left:17px;\n"
            "	padding-top:4px;\n"
            "	padding-bottom:4px;\n"
            "	padding-right:7px;\n"
            "}\n"
            "QTabWidget {\n"
            "	color:rgb(0,0,0);\n"
            "	background-color:#000000;\n"
            "}\n"
            "QTabWidget::pane {\n"
            "		border-color: rgb(223,223,223);\n"
            "		background-color:rgb(226,226,226);\n"
            "		border-style: solid;\n"
            "		border-width: 2px;\n"
            "    	border-radius: 6px;\n"
            "}\n"
            "QTabBar::tab:first {\n"
            "	border-style: solid;\n"
            "	border-left-width:1px;\n"
            "	border-right-width:0px;\n"
            "	border-top-width:1px;\n"
            "	border-bottom-widt"
            "h:1px;\n"
            "	border-top-color: rgb(209,209,209);\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
            "	border-bottom-color: rgb(229,229,229);\n"
            "	border-top-left-radius: 4px;\n"
            "	border-bottom-left-radius: 4px;\n"
            "	color: #000000;\n"
            "	padding: 3px;\n"
            "	margin-left:0px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QTabBar::tab:last {\n"
            "	border-style: solid;\n"
            "	border-width:1px;\n"
            "	border-top-color: rgb(209,209,209);\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
            "	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
            "	border-bottom-color: rgb(229,229,229);\n"
            "	border-top-right-radius: 4px;\n"
            "	border-b"
            "ottom-right-radius: 4px;\n"
            "	color: #000000;\n"
            "	padding: 3px;\n"
            "	margin-left:0px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QTabBar::tab {\n"
            "	border-style: solid;\n"
            "	border-top-width:1px;\n"
            "	border-bottom-width:1px;\n"
            "	border-left-width:1px;\n"
            "	border-top-color: rgb(209,209,209);\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
            "	border-bottom-color: rgb(229,229,229);\n"
            "	color: #000000;\n"
            "	padding: 3px;\n"
            "	margin-left:0px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
            "  	border-style: solid;\n"
            "  	border-left-width:1px;\n"
            "	border-right-color: transparent;\n"
            "	border-top-color: rgb(209,209,209"
            ");\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
            "	border-bottom-color: rgb(229,229,229);\n"
            "	color: #FFFFFF;\n"
            "	padding: 3px;\n"
            "	margin-left:0px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "\n"
            "QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
            "  	border-style: solid;\n"
            "  	border-left-width:1px;\n"
            "  	border-bottom-width:1px;\n"
            "  	border-top-width:1px;\n"
            "	border-right-color: transparent;\n"
            "	border-top-color: rgb(209,209,209);\n"
            "	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
            "	border-bottom-color: rgb(229,229,229);\n"
            "	color: #FFFFFF;\n"
            "	padding: 3px;\n"
            "	margin-left:0px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 r"
            "gba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "\n"
            "QCheckBox {\n"
            "	color: #000000;\n"
            "	padding: 2px;\n"
            "}\n"
            "QCheckBox:disabled {\n"
            "	color: #808086;\n"
            "	padding: 2px;\n"
            "}\n"
            "\n"
            "QCheckBox:hover {\n"
            "	border-radius:4px;\n"
            "	border-style:solid;\n"
            "	padding-left: 1px;\n"
            "	padding-right: 1px;\n"
            "	padding-bottom: 1px;\n"
            "	padding-top: 1px;\n"
            "	border-width:1px;\n"
            "	border-color: transparent;\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "\n"
            "	height: 10px;\n"
            "	width: 10px;\n"
            "	border-style:solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #000000;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QCheckBox::indicator:unchecked {\n"
            "\n"
            "	height: 10px;\n"
            "	width: 10px;\n"
            "	border-style:solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlinearg"
            "radient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #000000;\n"
            "}\n"
            "QRadioButton {\n"
            "	color: 000000;\n"
            "	padding: 1px;\n"
            "}\n"
            "QRadioButton::indicator:checked {\n"
            "	height: 10px;\n"
            "	width: 10px;\n"
            "	border-style:solid;\n"
            "	border-radius:5px;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #a9b7c6;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QRadioButton::indicator:!checked {\n"
            "	height: 10px;\n"
            "	width: 10px;\n"
            "	border-style:solid;\n"
            "	border-radius:5px;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #a9b7c6;\n"
            "	background-color: transparent;\n"
            "}\n"
            "QStatusBar"
            " {\n"
            "	color:#027f7f;\n"
            "}\n"
            "QSpinBox {\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QDoubleSpinBox {\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QTimeEdit {\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QDateTimeEdit {\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QDateEdit {\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, sto"
            "p:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "\n"
            "QToolBox {\n"
            "	color: #a9b7c6;\n"
            "	background-color:#000000;\n"
            "}\n"
            "QToolBox::tab {\n"
            "	color: #a9b7c6;\n"
            "	background-color:#000000;\n"
            "}\n"
            "QToolBox::tab:selected {\n"
            "	color: #FFFFFF;\n"
            "	background-color:#000000;\n"
            "}\n"
            "QScrollArea {\n"
            "	color: #FFFFFF;\n"
            "	background-color:#000000;\n"
            "}\n"
            "QSlider::groove:horizontal {\n"
            "	height: 5px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
            "}\n"
            "QSlider::groove:vertical {\n"
            "	width: 5px;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
            "}\n"
            "QSlider::handle:horizontal {\n"
            "	background: rgb(253,253,253);\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: rgb(207,207,207);\n"
            "	width: 12px;\n"
            "	margin: -5px 0;\n"
            "	border-radius: 7px;\n"
            "}\n"
            "QSlider::ha"
            "ndle:vertical {\n"
            "	background: rgb(253,253,253);\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: rgb(207,207,207);\n"
            "	height: 12px;\n"
            "	margin: 0 -5px;\n"
            "	border-radius: 7px;\n"
            "}\n"
            "QSlider::add-page:horizontal {\n"
            "    background: rgb(181,181,181);\n"
            "}\n"
            "QSlider::add-page:vertical {\n"
            "    background: rgb(181,181,181);\n"
            "}\n"
            "QSlider::sub-page:horizontal {\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
            "}\n"
            "QSlider::sub-page:vertical {\n"
            "    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
            "}\n"
            "QScrollBar:horizontal {\n"
            "	max-height: 20px;\n"
            "	border: 1px transparent grey;\n"
            "	margin: 0px 20px 0px 20px;\n"
            "}\n"
            "QScrollBar:vertical {\n"
            "	max-width: 20px;\n"
            "	border: 1px transparent grey;\n"
            "	margin: 20px 0px 20px 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "	"
            "background: rgb(253,253,253);\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: rgb(207,207,207);\n"
            "	border-radius: 7px;\n"
            "	min-width: 25px;\n"
            "}\n"
            "QScrollBar::handle:horizontal:hover {\n"
            "	background: rgb(253,253,253);\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: rgb(147, 200, 200);\n"
            "	border-radius: 7px;\n"
            "	min-width: 25px;\n"
            "}\n"
            "QScrollBar::handle:vertical {\n"
            "	background: rgb(253,253,253);\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: rgb(207,207,207);\n"
            "	border-radius: 7px;\n"
            "	min-height: 25px;\n"
            "}\n"
            "QScrollBar::handle:vertical:hover {\n"
            "	background: rgb(253,253,253);\n"
            "	border-style: solid;\n"
            "	border-width: 1px;\n"
            "	border-color: rgb(147, 200, 200);\n"
            "	border-radius: 7px;\n"
            "	min-height: 25px;\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "   border: 2px transparent grey;\n"
            "   border-top-right-radius: 7px;\n"
            "   border-bottom-right-radius: 7px;\n"
            "   background: rgba(34, 142, 255, 255);\n"
            "   width"
            ": 20px;\n"
            "   subcontrol-position: right;\n"
            "   subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::add-line:horizontal:pressed {\n"
            "   border: 2px transparent grey;\n"
            "   border-top-right-radius: 7px;\n"
            "   border-bottom-right-radius: 7px;\n"
            "   background: rgb(181,181,181);\n"
            "   width: 20px;\n"
            "   subcontrol-position: right;\n"
            "   subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::add-line:vertical {\n"
            "   border: 2px transparent grey;\n"
            "   border-bottom-left-radius: 7px;\n"
            "   border-bottom-right-radius: 7px;\n"
            "   background: rgba(34, 142, 255, 255);\n"
            "   height: 20px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::add-line:vertical:pressed {\n"
            "   border: 2px transparent grey;\n"
            "   border-bottom-left-radius: 7px;\n"
            "   border-bottom-right-radius: 7px;\n"
            "   background: rgb(181,181,181);\n"
            "   height: 20px;\n"
            "   subcontrol-position: bottom;\n"
            "   subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "   border: 2px transp"
            "arent grey;\n"
            "   border-top-left-radius: 7px;\n"
            "   border-bottom-left-radius: 7px;\n"
            "   background: rgba(34, 142, 255, 255);\n"
            "   width: 20px;\n"
            "   subcontrol-position: left;\n"
            "   subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal:pressed {\n"
            "   border: 2px transparent grey;\n"
            "   border-top-left-radius: 7px;\n"
            "   border-bottom-left-radius: 7px;\n"
            "   background: rgb(181,181,181);\n"
            "   width: 20px;\n"
            "   subcontrol-position: left;\n"
            "   subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:vertical {\n"
            "   border: 2px transparent grey;\n"
            "   border-top-left-radius: 7px;\n"
            "   border-top-right-radius: 7px;\n"
            "   background: rgba(34, 142, 255, 255);\n"
            "   height: 20px;\n"
            "   subcontrol-position: top;\n"
            "   subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:vertical:pressed {\n"
            "   border: 2px transparent grey;\n"
            "   border-top-left-radius: 7px;\n"
            "   border-top-right-radius: 7px;\n"
            "   background: rgb(181,181,181);\n"
            "   height: 20px;\n"
            "   subcontr"
            "ol-position: top;\n"
            "   subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::left-arrow:horizontal {\n"
            "   border: 1px transparent grey;\n"
            "   border-top-left-radius: 3px;\n"
            "   border-bottom-left-radius: 3px;\n"
            "   width: 6px;\n"
            "   height: 6px;\n"
            "   background: white;\n"
            "}\n"
            "QScrollBar::right-arrow:horizontal {\n"
            "   border: 1px transparent grey;\n"
            "   border-top-right-radius: 3px;\n"
            "   border-bottom-right-radius: 3px;\n"
            "   width: 6px;\n"
            "   height: 6px;\n"
            "   background: white;\n"
            "}\n"
            "QScrollBar::up-arrow:vertical {\n"
            "   border: 1px transparent grey;\n"
            "   border-top-left-radius: 3px;\n"
            "   border-top-right-radius: 3px;\n"
            "   width: 6px;\n"
            "   height: 6px;\n"
            "   background: white;\n"
            "}\n"
            "QScrollBar::down-arrow:vertical {\n"
            "   border: 1px transparent grey;\n"
            "   border-bottom-left-radius: 3px;\n"
            "   border-bottom-right-radius: 3px;\n"
            "   width: 6px;\n"
            "   height: 6px;\n"
            "   background: white;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
            " "
            "  background: none;\n"
            "}\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "   background: none;\n"
            "}"
        )
        self.button_cancel = QPushButton(SettingWin)
        self.button_cancel.setObjectName("button_cancel")
        self.button_cancel.setGeometry(QRect(500, 420, 111, 41))
        font = QFont()
        font.setFamilies(["Microsoft YaHei UI"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.button_cancel.setFont(font)
        self.button_save_setting = QPushButton(SettingWin)
        self.button_save_setting.setObjectName("button_save_setting")
        self.button_save_setting.setGeometry(QRect(280, 420, 201, 41))
        self.button_save_setting.setFont(font)
        self.layoutWidget = QWidget(SettingWin)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 102, 35))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        font1 = QFont()
        font1.setFamilies(["\u66f4\u7eb1\u9ed1\u4f53 UI SC"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.label_6 = QLabel(SettingWin)
        self.label_6.setObjectName("label_6")
        self.label_6.setGeometry(QRect(50, 160, 147, 39))
        font2 = QFont()
        font2.setFamilies(["\u7b49\u8ddd\u66f4\u7eb1\u9ed1\u4f53 Slab SC"])
        font2.setPointSize(12)
        self.label_6.setFont(font2)
        self.combo_background = QComboBox(SettingWin)
        self.combo_background.setObjectName("combo_background")
        self.combo_background.setGeometry(QRect(210, 160, 311, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.combo_background.setFont(font3)
        self.label_4 = QLabel(SettingWin)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(50, 370, 128, 21))
        self.label_4.setFont(font2)
        self.check_is_save_log = QCheckBox(SettingWin)
        self.check_is_save_log.setObjectName("check_is_save_log")
        self.check_is_save_log.setGeometry(QRect(210, 370, 161, 21))
        font4 = QFont()
        font4.setFamilies(["\u66f4\u7eb1\u9ed1\u4f53 SC"])
        font4.setPointSize(12)
        self.check_is_save_log.setFont(font4)
        self.check_is_save_log.setStyleSheet(
            "QCheckBox {\n"
            "	color: #000000;\n"
            "	padding: 2px;\n"
            "}\n"
            "QCheckBox:disabled {\n"
            "	color: #808086;\n"
            "	padding: 2px;\n"
            "}\n"
            "\n"
            "QCheckBox:hover {\n"
            "	border-radius:4px;\n"
            "	border-style:solid;\n"
            "	padding-left: 1px;\n"
            "	padding-right: 1px;\n"
            "	padding-bottom: 1px;\n"
            "	padding-top: 1px;\n"
            "	border-width:1px;\n"
            "	border-color: transparent;\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "\n"
            "	height: 15px;\n"
            "	width: 15px;\n"
            "	border-style:solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #000000;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QCheckBox::indicator:unchecked {\n"
            "\n"
            "	height: 15px;\n"
            "	width: 15px;\n"
            "	border-style:solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255"
            ", 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #000000;\n"
            "}"
        )
        self.label_3 = QLabel(SettingWin)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(50, 330, 144, 21))
        self.label_3.setFont(font2)
        self.check_is_save_check_box = QCheckBox(SettingWin)
        self.check_is_save_check_box.setObjectName("check_is_save_check_box")
        self.check_is_save_check_box.setGeometry(QRect(210, 330, 177, 21))
        self.check_is_save_check_box.setFont(font4)
        self.check_is_save_check_box.setStyleSheet(
            "QCheckBox {\n"
            "	color: #000000;\n"
            "	padding: 2px;\n"
            "}\n"
            "QCheckBox:disabled {\n"
            "	color: #808086;\n"
            "	padding: 2px;\n"
            "}\n"
            "\n"
            "QCheckBox:hover {\n"
            "	border-radius:4px;\n"
            "	border-style:solid;\n"
            "	padding-left: 1px;\n"
            "	padding-right: 1px;\n"
            "	padding-bottom: 1px;\n"
            "	padding-top: 1px;\n"
            "	border-width:1px;\n"
            "	border-color: transparent;\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "\n"
            "	height: 15px;\n"
            "	width: 15px;\n"
            "	border-style:solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #000000;\n"
            "	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
            "}\n"
            "QCheckBox::indicator:unchecked {\n"
            "\n"
            "	height: 15px;\n"
            "	width: 15px;\n"
            "	border-style:solid;\n"
            "	border-width: 1px;\n"
            "	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255"
            ", 255), stop:1 rgba(91, 171, 252, 255));\n"
            "	color: #000000;\n"
            "}"
        )
        self.button_open_background_dir = QPushButton(SettingWin)
        self.button_open_background_dir.setObjectName("button_open_background_dir")
        self.button_open_background_dir.setGeometry(QRect(540, 160, 81, 41))
        self.button_open_background_dir.setFont(font)
        self.label_7 = QLabel(SettingWin)
        self.label_7.setObjectName("label_7")
        self.label_7.setGeometry(QRect(50, 210, 147, 39))
        self.label_7.setFont(font2)
        self.button_open_plugin_dir = QPushButton(SettingWin)
        self.button_open_plugin_dir.setObjectName("button_open_plugin_dir")
        self.button_open_plugin_dir.setGeometry(QRect(210, 210, 211, 41))
        self.button_open_plugin_dir.setFont(font)
        self.output_save_location = QTextEdit(SettingWin)
        self.output_save_location.setObjectName("output_save_location")
        self.output_save_location.setGeometry(QRect(210, 70, 401, 71))
        self.label_2 = QLabel(SettingWin)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(50, 90, 161, 49))
        self.label_2.setFont(font2)
        self.button_reset_save_location = QPushButton(SettingWin)
        self.button_reset_save_location.setObjectName("button_reset_save_location")
        self.button_reset_save_location.setGeometry(QRect(210, 270, 148, 39))
        self.button_reset_save_location.setFont(font)
        self.label_5 = QLabel(SettingWin)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(50, 270, 111, 39))
        self.label_5.setFont(font2)

        self.retranslateUi(SettingWin)
        self.button_save_setting.clicked.connect(SettingWin.saveSetting)
        self.button_cancel.clicked.connect(SettingWin.cancelSetting)
        self.check_is_save_check_box.clicked.connect(SettingWin.saveSettingCheckEvent)
        self.check_is_save_log.clicked.connect(SettingWin.saveLogCheckEvent)
        self.button_reset_save_location.clicked.connect(
            SettingWin.resetSaveLocationEvnet
        )
        self.combo_background.currentTextChanged.connect(SettingWin.chooseBackgroundImg)
        self.button_open_background_dir.clicked.connect(
            SettingWin.openBackgroundDirEvent
        )
        self.button_open_plugin_dir.clicked.connect(SettingWin.openPluginDirEvent)

        QMetaObject.connectSlotsByName(SettingWin)

    # setupUi

    def retranslateUi(self, SettingWin):
        SettingWin.setWindowTitle(
            QCoreApplication.translate("SettingWin", "Dialog", None)
        )
        self.button_cancel.setText(
            QCoreApplication.translate("SettingWin", "\u53d6\u6d88\u4fee\u6539", None)
        )
        self.button_save_setting.setText(
            QCoreApplication.translate("SettingWin", "\u4fdd\u5b58", None)
        )
        self.label.setText(
            QCoreApplication.translate("SettingWin", "\u8bbe\u7f6e", None)
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "SettingWin", "\u80cc\u666f\u56fe\u7247\u9009\u62e9", None
            )
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "SettingWin", "\u662f\u5426\u5f00\u542f\u65e5\u5fd7\u6587\u4ef6", None
            )
        )
        self.check_is_save_log.setText("")
        self.label_3.setText(
            QCoreApplication.translate(
                "SettingWin",
                "\u662f\u5426\u4fdd\u5b58\u9009\u62e9\u6846\u72b6\u6001",
                None,
            )
        )
        self.check_is_save_check_box.setText("")
        self.button_open_background_dir.setText(
            QCoreApplication.translate("SettingWin", "\u76ee\u5f55", None)
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "SettingWin", "\u63d2\u4ef6\u5b58\u653e\u76ee\u5f55", None
            )
        )
        self.button_open_plugin_dir.setText(
            QCoreApplication.translate(
                "SettingWin", "\u6253\u5f00\u63d2\u4ef6\u5b58\u653e\u76ee\u5f55", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "SettingWin",
                "\u4fdd\u5b58\u8f93\u51fa\u6587\u4ef6\u7684\u4f4d\u7f6e",
                None,
            )
        )
        self.button_reset_save_location.setText(
            QCoreApplication.translate(
                "SettingWin", "\u91cd\u7f6e\u4fdd\u5b58\u4f4d\u7f6e", None
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "SettingWin", "\u91cd\u7f6e\u4fdd\u5b58\u4f4d\u7f6e", None
            )
        )

    # retranslateUi
