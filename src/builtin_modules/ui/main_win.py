# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from . import main_window_resource_rc

class Ui_MainWin(object):
    def setupUi(self, MainWin):
        if not MainWin.objectName():
            MainWin.setObjectName(u"MainWin")
        MainWin.resize(1392, 994)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWin.sizePolicy().hasHeightForWidth())
        MainWin.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/ico/icons/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWin.setWindowIcon(icon)
        MainWin.setAutoFillBackground(False)
        MainWin.setStyleSheet(u"/*QMainWindow{\n"
"background-image: url(:/background/images/background3.png);\n"
"border-radius: 20px;\n"
"}*/\n"
"\n"
"#central_widget{\n"
"background-image: url(:/background/images/background3.png);\n"
"/*background-image: url(:/background/images/background1_gaussian_blur.png);*/\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QTextEdut{\n"
"padding-top: 5px;\n"
"background-color: rgba(229, 229, 229, 170);\n"
"border-radius: 10px;\n"
"}\n"
"QPlainTextEdit{\n"
"padding-top: 5px;\n"
"background-color: rgba(229, 229, 229, 170);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"QListWidget{\n"
"padding-top: 5px;\n"
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
"}\n"
"\n"
"\n"
"QCheckBox {\n"
"	background-color: rgba(229, 229, 229, 150);\n"
"	border-radius: 6px;\n"
"	height: 5px;\n"
"	border-style:so"
                        "lid;\n"
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
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 200), stop:1 rgba(34, 142, 255, 200));\n"
"	border-radi"
                        "us: 10px;\n"
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
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-w"
                        "idth: 1px;\n"
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
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
""
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
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   heigh"
                        "t: 20px;\n"
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
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white"
                        ";\n"
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
"}")
        MainWin.setUnifiedTitleAndToolBarOnMac(False)
        self.central_widget = QWidget(MainWin)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.central_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.central_widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label_3)

        self.button_about = QPushButton(self.central_widget)
        self.button_about.setObjectName(u"button_about")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.button_about.sizePolicy().hasHeightForWidth())
        self.button_about.setSizePolicy(sizePolicy2)
        self.button_about.setMinimumSize(QSize(35, 25))
        self.button_about.setMaximumSize(QSize(25, 35))
        self.button_about.setStyleSheet(u"QPushButton{\n"
"background:rgb(213, 213, 213);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/ico/icons/ico.ico", QSize(), QIcon.Normal, QIcon.On)
        self.button_about.setIcon(icon1)

        self.horizontalLayout.addWidget(self.button_about)

        self.button_setting = QPushButton(self.central_widget)
        self.button_setting.setObjectName(u"button_setting")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.button_setting.sizePolicy().hasHeightForWidth())
        self.button_setting.setSizePolicy(sizePolicy3)
        self.button_setting.setMaximumSize(QSize(35, 35))
        self.button_setting.setStyleSheet(u"QPushButton{\n"
"background:rgb(213, 213, 213);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/ico/icons/setting_icon.png", QSize(), QIcon.Normal, QIcon.On)
        self.button_setting.setIcon(icon2)

        self.horizontalLayout.addWidget(self.button_setting)

        self.button_minimize = QPushButton(self.central_widget)
        self.button_minimize.setObjectName(u"button_minimize")
        sizePolicy3.setHeightForWidth(self.button_minimize.sizePolicy().hasHeightForWidth())
        self.button_minimize.setSizePolicy(sizePolicy3)
        self.button_minimize.setMaximumSize(QSize(35, 35))
        self.button_minimize.setStyleSheet(u"QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}")

        self.horizontalLayout.addWidget(self.button_minimize)

        self.button_maximum = QPushButton(self.central_widget)
        self.button_maximum.setObjectName(u"button_maximum")
        sizePolicy3.setHeightForWidth(self.button_maximum.sizePolicy().hasHeightForWidth())
        self.button_maximum.setSizePolicy(sizePolicy3)
        self.button_maximum.setMaximumSize(QSize(35, 35))
        self.button_maximum.setStyleSheet(u"QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}")

        self.horizontalLayout.addWidget(self.button_maximum)

        self.button_close = QPushButton(self.central_widget)
        self.button_close.setObjectName(u"button_close")
        sizePolicy3.setHeightForWidth(self.button_close.sizePolicy().hasHeightForWidth())
        self.button_close.setSizePolicy(sizePolicy3)
        self.button_close.setMaximumSize(QSize(35, 35))
        self.button_close.setStyleSheet(u"QPushButton{\n"
"background:#F76677;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"background:red;\n"
"}")

        self.horizontalLayout.addWidget(self.button_close)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_9 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.search_box = QPlainTextEdit(self.central_widget)
        self.search_box.setObjectName(u"search_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy4)
        self.search_box.setMinimumSize(QSize(270, 0))
        self.search_box.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(12)
        self.search_box.setFont(font)
        self.search_box.setLayoutDirection(Qt.LeftToRight)
        self.search_box.setStyleSheet(u"")
        self.search_box.setFrameShape(QFrame.StyledPanel)
        self.search_box.setLineWidth(1)

        self.verticalLayout_3.addWidget(self.search_box)

        self.verticalSpacer_3 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.choices_list_box = QListWidget(self.central_widget)
        QListWidgetItem(self.choices_list_box)
        QListWidgetItem(self.choices_list_box)
        QListWidgetItem(self.choices_list_box)
        QListWidgetItem(self.choices_list_box)
        QListWidgetItem(self.choices_list_box)
        QListWidgetItem(self.choices_list_box)
        QListWidgetItem(self.choices_list_box)
        QListWidgetItem(self.choices_list_box)
        self.choices_list_box.setObjectName(u"choices_list_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(7)
        sizePolicy5.setHeightForWidth(self.choices_list_box.sizePolicy().hasHeightForWidth())
        self.choices_list_box.setSizePolicy(sizePolicy5)
        self.choices_list_box.setMinimumSize(QSize(270, 0))
        self.choices_list_box.setMaximumSize(QSize(16777215, 16777215))
        self.choices_list_box.setFont(font)
        self.choices_list_box.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.choices_list_box)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.input_box = QPlainTextEdit(self.central_widget)
        self.input_box.setObjectName(u"input_box")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(3)
        sizePolicy6.setVerticalStretch(2)
        sizePolicy6.setHeightForWidth(self.input_box.sizePolicy().hasHeightForWidth())
        self.input_box.setSizePolicy(sizePolicy6)
        self.input_box.setFont(font)
        self.input_box.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.input_box)

        self.verticalSpacer = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_8 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.save_check = QCheckBox(self.central_widget)
        self.save_check.setObjectName(u"save_check")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(3)
        sizePolicy7.setVerticalStretch(1)
        sizePolicy7.setHeightForWidth(self.save_check.sizePolicy().hasHeightForWidth())
        self.save_check.setSizePolicy(sizePolicy7)
        self.save_check.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"\u66f4\u7eb1\u9ed1\u4f53 UI SC"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.save_check.setFont(font1)
        self.save_check.setLayoutDirection(Qt.LeftToRight)
        self.save_check.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.save_check)

        self.verticalSpacer_7 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.output_lock_maximums_check = QCheckBox(self.central_widget)
        self.output_lock_maximums_check.setObjectName(u"output_lock_maximums_check")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.output_lock_maximums_check.sizePolicy().hasHeightForWidth())
        self.output_lock_maximums_check.setSizePolicy(sizePolicy8)
        self.output_lock_maximums_check.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"\u66f4\u7eb1\u9ed1\u4f53 UI SC"])
        font2.setPointSize(12)
        self.output_lock_maximums_check.setFont(font2)
        self.output_lock_maximums_check.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.output_lock_maximums_check)

        self.verticalSpacer_6 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.output_optimization_check = QCheckBox(self.central_widget)
        self.output_optimization_check.setObjectName(u"output_optimization_check")
        sizePolicy8.setHeightForWidth(self.output_optimization_check.sizePolicy().hasHeightForWidth())
        self.output_optimization_check.setSizePolicy(sizePolicy8)
        self.output_optimization_check.setMinimumSize(QSize(0, 30))
        self.output_optimization_check.setFont(font2)
        self.output_optimization_check.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.output_optimization_check)

        self.verticalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.start_button = QPushButton(self.central_widget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(3)
        sizePolicy9.setVerticalStretch(1)
        sizePolicy9.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy9)
        self.start_button.setMinimumSize(QSize(100, 30))
        font3 = QFont()
        font3.setFamilies([u"\u66f4\u7eb1\u9ed1\u4f53 SC Light"])
        font3.setPointSize(18)
        font3.setBold(False)
        self.start_button.setFont(font3)
        self.start_button.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.start_button)

        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.output_box = QPlainTextEdit(self.central_widget)
        self.output_box.setObjectName(u"output_box")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(3)
        sizePolicy10.setVerticalStretch(5)
        sizePolicy10.setHeightForWidth(self.output_box.sizePolicy().hasHeightForWidth())
        self.output_box.setSizePolicy(sizePolicy10)
        self.output_box.setFont(font)
        self.output_box.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.output_box)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        MainWin.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWin)
        self.start_button.clicked.connect(MainWin.startEvent)
        self.save_check.clicked.connect(MainWin.saveCheckEvent)
        self.output_optimization_check.clicked.connect(MainWin.outputOptimizationCheckEvent)
        self.output_lock_maximums_check.clicked.connect(MainWin.outputLockMaximumsCheckEvent)
        self.search_box.textChanged.connect(MainWin.searchText)
        self.choices_list_box.itemClicked.connect(MainWin.chooseOptionEvent)
        self.button_setting.clicked.connect(MainWin.openSettingWin)
        self.button_close.clicked.connect(MainWin.quitEvent)
        self.button_about.clicked.connect(MainWin.openAboutWin)

        QMetaObject.connectSlotsByName(MainWin)
    # setupUi

    def retranslateUi(self, MainWin):
        MainWin.setWindowTitle(QCoreApplication.translate("MainWin", u"hpycacular", None))
        self.label_3.setText("")
        self.button_about.setText("")
        self.button_setting.setText("")
        self.button_minimize.setText("")
        self.button_maximum.setText("")
        self.button_close.setText("")
        self.search_box.setPlainText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None))

        __sortingEnabled = self.choices_list_box.isSortingEnabled()
        self.choices_list_box.setSortingEnabled(False)
        ___qlistwidgetitem = self.choices_list_box.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None));
        ___qlistwidgetitem1 = self.choices_list_box.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None));
        ___qlistwidgetitem2 = self.choices_list_box.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None));
        ___qlistwidgetitem3 = self.choices_list_box.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None));
        ___qlistwidgetitem4 = self.choices_list_box.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None));
        ___qlistwidgetitem5 = self.choices_list_box.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None));
        ___qlistwidgetitem6 = self.choices_list_box.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None));
        ___qlistwidgetitem7 = self.choices_list_box.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None));
        self.choices_list_box.setSortingEnabled(__sortingEnabled)

        self.input_box.setPlainText("")
        self.save_check.setText(QCoreApplication.translate("MainWin", u"\u4fdd\u5b58\u8f93\u51fa\u5230\u6587\u4ef6", None))
        self.output_lock_maximums_check.setText(QCoreApplication.translate("MainWin", u"\u5185\u6846\u8f93\u51fa\u4e0a\u9650", None))
        self.output_optimization_check.setText(QCoreApplication.translate("MainWin", u"\u5185\u6846\u8f93\u51fa\u6027\u80fd\u4f18\u5316", None))
        self.start_button.setText(QCoreApplication.translate("MainWin", u"\u5f00\u59cb\u8ba1\u7b97", None))
        self.output_box.setPlainText(QCoreApplication.translate("MainWin", u"\u8fd9\u662f\u4e00\u6bb5\u6d4b\u8bd5\u6587\u5b57\n"
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
"\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee\u8fd9\u662f\u4e00\u4e2a\u6d4b\u8bd5\u9879\u76ee", None))
    # retranslateUi

