# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
from . import main_window_resource_rc


class Ui_MainWin(object):
    def setupUi(self, MainWin):
        if not MainWin.objectName():
            MainWin.setObjectName("MainWin")
        MainWin.resize(1145, 926)
        MainWin.setStyleSheet(
            "/*QMainWindow{\n"
            "background-image: url(:/background/images/background3.png);\n"
            "border-radius: 20px;\n"
            "}*/\n"
            "\n"
            "#central_widget{\n"
            "margin-top: 0px;\n"
            "margin-right: 0px;\n"
            "margin-bottom: 0px;\n"
            "margin-left: 0px;\n"
            "/*background-image: url(:/background/images/background3.png);\n"
            "background-size: cover;\n"
            "background-repeat: no-repeat;\n"
            "border-radius: 10px;*/\n"
            "}\n"
            "\n"
            "QTextEdit{\n"
            "padding-top: 5px;\n"
            "padding-left: 2px;\n"
            "background-color: rgba(229, 229, 229, 170);\n"
            "border-radius: 10px;\n"
            "}\n"
            "QPlainTextEdit{\n"
            "padding-top: 5px;\n"
            "padding-left: 2px;\n"
            "background-color: rgba(229, 229, 229, 170);\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "\n"
            "QListWidget{\n"
            "padding-top: 5px;\n"
            "padding-left: 2px;\n"
            "background-color: rgba(229, 229, 229, 150);\n"
            "border-radius: 10px;\n"
            "}\n"
            "\n"
            "\n"
            "QPushButton{\n"
            "background-color: rgba(229, 229, 229, 120);\n"
            "border-radius: 10px;\n"
            "padding: 7px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "	background-color: rgba(190, 190, 190, 130);\n"
            ""
            "}\n"
            "\n"
            "\n"
            "QCheckBox {\n"
            "	background-color: rgba(229, 229, 229, 150);\n"
            "	border-radius: 6px;\n"
            "	height: 5px;\n"
            "	border-style:solid;\n"
            "	border-width: 1px;\n"
            "	border-color: transparent;\n"
            "\n"
            "	color: #000000;\n"
            "	padding: 10px;\n"
            "}\n"
            "QCheckBox:disabled {\n"
            "	color: #808086;\n"
            "	padding: 2px;\n"
            "}\n"
            "QCheckBox:hover {\n"
            "	/*padding-left: 1px;\n"
            "	padding-right: 1px;\n"
            "	padding-bottom: 1px;\n"
            "	padding-top: 1px;\n"
            "	border-width:1px;*/\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "	image: url(:/checked/images/checked.png);\n"
            "	height: 20px;\n"
            "	width: 20px;\n"
            "}\n"
            "QCheckBox::indicator:unchecked {\n"
            "	image: url(:/checked/images/unchecked.png);\n"
            "	height: 20px;\n"
            "	width: 20px;\n"
            "}\n"
            "\n"
            "\n"
            "QProgressBar {\n"
            "	text-align: center;\n"
            "	color: rgb(240, 240, 240);\n"
            "	border-width: 1px; \n"
            "	border-radius: 10px;\n"
            "	border-color: rgb(230, 230, 230);\n"
            "	border-style: solid;\n"
            "	background-color:rgb(207,207,207);\n"
            "}\n"
            "QProgressBar::chunk {\n"
            "	background-colo"
            "r: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 200), stop:1 rgba(34, 142, 255, 200));\n"
            "	border-radius: 10px;\n"
            "}\n"
            "\n"
            "\n"
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
            "	background: rgb(253,253,253);\n"
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
            ""
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
            "   width: 20px;\n"
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
            ""
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
            "   border: 2px transparent grey;\n"
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
            "   border: 2px transp"
            "arent grey;\n"
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
            "   subcontrol-position: top;\n"
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
            "   border: 1px transparent g"
            "rey;\n"
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
            "   background: none;\n"
            "}\n"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "   background: none;\n"
            "}"
        )
        self.gridLayout = QGridLayout(MainWin)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QLabel(MainWin)
        self.label_3.setObjectName("label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_3)

        self.button_about = QPushButton(MainWin)
        self.button_about.setObjectName("button_about")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(
            self.button_about.sizePolicy().hasHeightForWidth()
        )
        self.button_about.setSizePolicy(sizePolicy1)
        self.button_about.setMinimumSize(QSize(35, 25))
        self.button_about.setMaximumSize(QSize(25, 35))
        self.button_about.setStyleSheet(
            "QPushButton{\n"
            "background:rgb(213, 213, 213);\n"
            "border-radius:5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(170, 255, 255);\n"
            "}"
        )
        icon = QIcon()
        icon.addFile(":/ico/icons/ico.ico", QSize(), QIcon.Normal, QIcon.On)
        self.button_about.setIcon(icon)

        self.horizontalLayout.addWidget(self.button_about)

        self.button_setting = QPushButton(MainWin)
        self.button_setting.setObjectName("button_setting")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(
            self.button_setting.sizePolicy().hasHeightForWidth()
        )
        self.button_setting.setSizePolicy(sizePolicy2)
        self.button_setting.setMaximumSize(QSize(35, 35))
        self.button_setting.setStyleSheet(
            "QPushButton{\n"
            "background:rgb(213, 213, 213);\n"
            "border-radius:5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color: rgb(170, 255, 255);\n"
            "}"
        )
        icon1 = QIcon()
        icon1.addFile(":/ico/icons/setting_icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_setting.setIcon(icon1)

        self.horizontalLayout.addWidget(self.button_setting)

        self.button_minimize = QPushButton(MainWin)
        self.button_minimize.setObjectName("button_minimize")
        sizePolicy2.setHeightForWidth(
            self.button_minimize.sizePolicy().hasHeightForWidth()
        )
        self.button_minimize.setSizePolicy(sizePolicy2)
        self.button_minimize.setMaximumSize(QSize(35, 35))
        self.button_minimize.setStyleSheet(
            "QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}"
        )

        self.horizontalLayout.addWidget(self.button_minimize)

        self.button_maximum = QPushButton(MainWin)
        self.button_maximum.setObjectName("button_maximum")
        sizePolicy2.setHeightForWidth(
            self.button_maximum.sizePolicy().hasHeightForWidth()
        )
        self.button_maximum.setSizePolicy(sizePolicy2)
        self.button_maximum.setMaximumSize(QSize(35, 35))
        self.button_maximum.setStyleSheet(
            "QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}"
        )

        self.horizontalLayout.addWidget(self.button_maximum)

        self.button_close = QPushButton(MainWin)
        self.button_close.setObjectName("button_close")
        sizePolicy2.setHeightForWidth(
            self.button_close.sizePolicy().hasHeightForWidth()
        )
        self.button_close.setSizePolicy(sizePolicy2)
        self.button_close.setMaximumSize(QSize(35, 35))
        self.button_close.setStyleSheet(
            "QPushButton{\n"
            "background:#F76677;\n"
            "border-radius:5px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background:red;\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.button_close)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_9 = QSpacerItem(
            20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.search_plugin = QPlainTextEdit(MainWin)
        self.search_plugin.setObjectName("search_plugin")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(
            self.search_plugin.sizePolicy().hasHeightForWidth()
        )
        self.search_plugin.setSizePolicy(sizePolicy3)
        self.search_plugin.setMinimumSize(QSize(320, 0))
        self.search_plugin.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(12)
        self.search_plugin.setFont(font)
        self.search_plugin.setLayoutDirection(Qt.LeftToRight)
        self.search_plugin.setStyleSheet("")
        self.search_plugin.setFrameShape(QFrame.StyledPanel)
        self.search_plugin.setLineWidth(1)

        self.verticalLayout_3.addWidget(self.search_plugin)

        self.verticalSpacer_3 = QSpacerItem(
            20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.list_choices_plugin = QListWidget(MainWin)
        QListWidgetItem(self.list_choices_plugin)
        QListWidgetItem(self.list_choices_plugin)
        QListWidgetItem(self.list_choices_plugin)
        QListWidgetItem(self.list_choices_plugin)
        QListWidgetItem(self.list_choices_plugin)
        QListWidgetItem(self.list_choices_plugin)
        QListWidgetItem(self.list_choices_plugin)
        QListWidgetItem(self.list_choices_plugin)
        self.list_choices_plugin.setObjectName("list_choices_plugin")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(7)
        sizePolicy4.setHeightForWidth(
            self.list_choices_plugin.sizePolicy().hasHeightForWidth()
        )
        self.list_choices_plugin.setSizePolicy(sizePolicy4)
        self.list_choices_plugin.setMinimumSize(QSize(320, 0))
        self.list_choices_plugin.setMaximumSize(QSize(16777215, 16777215))
        self.list_choices_plugin.setFont(font)
        self.list_choices_plugin.setStyleSheet("")

        self.verticalLayout_3.addWidget(self.list_choices_plugin)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(
            13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.input_box = QPlainTextEdit(MainWin)
        self.input_box.setObjectName("input_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.input_box.sizePolicy().hasHeightForWidth())
        self.input_box.setSizePolicy(sizePolicy5)
        self.input_box.setFont(font)
        self.input_box.setStyleSheet("")

        self.verticalLayout_5.addWidget(self.input_box)

        self.verticalSpacer = QSpacerItem(
            20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer = QSpacerItem(
            13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalSpacer_8 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.check_save = QCheckBox(MainWin)
        self.check_save.setObjectName("check_save")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(3)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.check_save.sizePolicy().hasHeightForWidth())
        self.check_save.setSizePolicy(sizePolicy6)
        self.check_save.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies(["\u66f4\u7eb1\u9ed1\u4f53 UI SC"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.check_save.setFont(font1)
        self.check_save.setLayoutDirection(Qt.LeftToRight)
        self.check_save.setStyleSheet("")

        self.verticalLayout_2.addWidget(self.check_save)

        self.verticalSpacer_7 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.check_output_lock_maximums = QCheckBox(MainWin)
        self.check_output_lock_maximums.setObjectName("check_output_lock_maximums")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(
            self.check_output_lock_maximums.sizePolicy().hasHeightForWidth()
        )
        self.check_output_lock_maximums.setSizePolicy(sizePolicy7)
        self.check_output_lock_maximums.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies(["\u66f4\u7eb1\u9ed1\u4f53 UI SC"])
        font2.setPointSize(12)
        self.check_output_lock_maximums.setFont(font2)
        self.check_output_lock_maximums.setStyleSheet("")

        self.verticalLayout_2.addWidget(self.check_output_lock_maximums)

        self.verticalSpacer_6 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.check_output_optimization = QCheckBox(MainWin)
        self.check_output_optimization.setObjectName("check_output_optimization")
        sizePolicy7.setHeightForWidth(
            self.check_output_optimization.sizePolicy().hasHeightForWidth()
        )
        self.check_output_optimization.setSizePolicy(sizePolicy7)
        self.check_output_optimization.setMinimumSize(QSize(0, 30))
        self.check_output_optimization.setFont(font2)
        self.check_output_optimization.setStyleSheet("")

        self.verticalLayout_2.addWidget(self.check_output_optimization)

        self.verticalSpacer_10 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_10)

        self.check_auto_wrap = QCheckBox(MainWin)
        self.check_auto_wrap.setObjectName("check_auto_wrap")
        sizePolicy7.setHeightForWidth(
            self.check_auto_wrap.sizePolicy().hasHeightForWidth()
        )
        self.check_auto_wrap.setSizePolicy(sizePolicy7)
        self.check_auto_wrap.setMinimumSize(QSize(0, 30))
        self.check_auto_wrap.setFont(font2)
        self.check_auto_wrap.setStyleSheet("")

        self.verticalLayout_2.addWidget(self.check_auto_wrap)

        self.verticalSpacer_5 = QSpacerItem(
            13, 5, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.check_make_container = QCheckBox(MainWin)
        self.check_make_container.setObjectName("check_make_container")
        sizePolicy7.setHeightForWidth(
            self.check_make_container.sizePolicy().hasHeightForWidth()
        )
        self.check_make_container.setSizePolicy(sizePolicy7)
        self.check_make_container.setMinimumSize(QSize(0, 30))
        self.check_make_container.setFont(font2)
        self.check_make_container.setStyleSheet("")

        self.verticalLayout_2.addWidget(self.check_make_container)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.button_start = QPushButton(MainWin)
        self.button_start.setObjectName("button_start")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(3)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(
            self.button_start.sizePolicy().hasHeightForWidth()
        )
        self.button_start.setSizePolicy(sizePolicy8)
        self.button_start.setMinimumSize(QSize(100, 30))
        font3 = QFont()
        font3.setFamilies(["\u66f4\u7eb1\u9ed1\u4f53 SC Light"])
        font3.setPointSize(18)
        font3.setBold(False)
        self.button_start.setFont(font3)
        self.button_start.setStyleSheet("")

        self.verticalLayout.addWidget(self.button_start)

        self.verticalSpacer_2 = QSpacerItem(
            20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.output_box = QPlainTextEdit(MainWin)
        self.output_box.setObjectName("output_box")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(3)
        sizePolicy9.setVerticalStretch(5)
        sizePolicy9.setHeightForWidth(self.output_box.sizePolicy().hasHeightForWidth())
        self.output_box.setSizePolicy(sizePolicy9)
        self.output_box.setFont(font)
        self.output_box.setStyleSheet("")

        self.verticalLayout.addWidget(self.output_box)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(
            20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(MainWin)

        QMetaObject.connectSlotsByName(MainWin)

    # setupUi

    def retranslateUi(self, MainWin):
        MainWin.setWindowTitle(QCoreApplication.translate("MainWin", "Form", None))
        self.label_3.setText("")
        self.button_about.setText("")
        self.button_setting.setText("")
        self.button_minimize.setText("")
        self.button_maximum.setText("")
        self.button_close.setText("")
        self.search_plugin.setPlainText(
            QCoreApplication.translate(
                "MainWin",
                "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee",
                None,
            )
        )

        __sortingEnabled = self.list_choices_plugin.isSortingEnabled()
        self.list_choices_plugin.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_choices_plugin.item(0)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate(
                "MainWin", "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None
            )
        )
        ___qlistwidgetitem1 = self.list_choices_plugin.item(1)
        ___qlistwidgetitem1.setText(
            QCoreApplication.translate(
                "MainWin", "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None
            )
        )
        ___qlistwidgetitem2 = self.list_choices_plugin.item(2)
        ___qlistwidgetitem2.setText(
            QCoreApplication.translate(
                "MainWin", "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None
            )
        )
        ___qlistwidgetitem3 = self.list_choices_plugin.item(3)
        ___qlistwidgetitem3.setText(
            QCoreApplication.translate(
                "MainWin", "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None
            )
        )
        ___qlistwidgetitem4 = self.list_choices_plugin.item(4)
        ___qlistwidgetitem4.setText(
            QCoreApplication.translate(
                "MainWin", "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None
            )
        )
        ___qlistwidgetitem5 = self.list_choices_plugin.item(5)
        ___qlistwidgetitem5.setText(
            QCoreApplication.translate(
                "MainWin",
                "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee",
                None,
            )
        )
        ___qlistwidgetitem6 = self.list_choices_plugin.item(6)
        ___qlistwidgetitem6.setText(
            QCoreApplication.translate(
                "MainWin",
                "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee",
                None,
            )
        )
        ___qlistwidgetitem7 = self.list_choices_plugin.item(7)
        ___qlistwidgetitem7.setText(
            QCoreApplication.translate(
                "MainWin",
                "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee",
                None,
            )
        )
        self.list_choices_plugin.setSortingEnabled(__sortingEnabled)

        self.input_box.setPlainText("")
        self.check_save.setText(
            QCoreApplication.translate(
                "MainWin", "\u4fdd\u5b58\u8f93\u51fa\u5230\u6587\u4ef6", None
            )
        )
        self.check_output_lock_maximums.setText(
            QCoreApplication.translate(
                "MainWin", "\u5185\u6846\u8f93\u51fa\u4e0a\u9650", None
            )
        )
        self.check_output_optimization.setText(
            QCoreApplication.translate(
                "MainWin",
                "\u8f93\u51fa\u524d\u5148\u4fdd\u5b58\u5728\u4e34\u65f6\u6587\u4ef6\u4e2d",
                None,
            )
        )
        self.check_auto_wrap.setText(
            QCoreApplication.translate("MainWin", "\u81ea\u52a8\u6362\u884c", None)
        )
        self.check_make_container.setText(
            QCoreApplication.translate("MainWin", "\u6253\u8868\u6a21\u5f0f", None)
        )
        self.button_start.setText(
            QCoreApplication.translate("MainWin", "\u5f00\u59cb\u8ba1\u7b97", None)
        )
        self.output_box.setPlainText(
            QCoreApplication.translate(
                "MainWin",
                "\u8fd9\u662f\u4e00\u6bb5\u6d4b\u8bd5\u6587\u5b57\n"
                "	\u6d4b\u8bd5\n"
                "Abo\n"
                "	robot\n"
                "	electry\n"
                "1/2\n"
                "2/3/23/\n"
                "/12\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5"
                "\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\n"
                "\n"
                "12.331.23/123\n"
                "12\n"
                "1233333333333333333333333333333333333333333333333333333333333\n"
                "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee"
                "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u6bb5\u6d4b\u8bd5\u6587\u5b57\n"
                "	\u6d4b\u8bd5\n"
                "Abo\n"
                "	robot\n"
                "	electry\n"
                "1/2\n"
                "2/3/23/\n"
                "/12\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5"
                "\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\n"
                "\n"
                "12.331.23/123\n"
                "12\n"
                "1233333333333333333333333333333333333333333333333333333333333\n"
                ""
                "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u6bb5\u6d4b\u8bd5\u6587\u5b57\n"
                "	\u6d4b\u8bd5\n"
                "Abo\n"
                "	robot\n"
                "	electry\n"
                "1/2\n"
                "2/3/23/\n"
                "/12\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5"
                "\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9"
                "\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\n"
                "\n"
                "12.331.23/123\n"
                "12\n"
                "1233333333333333333333333333333333333333333333333333333333333\n"
                "\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee",
                None,
            )
        )

    # retranslateUi
