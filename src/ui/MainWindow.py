# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1015, 877)
        self.cheak_update = QAction(MainWindow)
        self.cheak_update.setObjectName(u"cheak_update")
        self.show_todo = QAction(MainWindow)
        self.show_todo.setObjectName(u"show_todo")
        self.show_about = QAction(MainWindow)
        self.show_about.setObjectName(u"show_about")
        self.show_update_log = QAction(MainWindow)
        self.show_update_log.setObjectName(u"show_update_log")
        self.reset_save_location = QAction(MainWindow)
        self.reset_save_location.setObjectName(u"reset_save_location")
        self.reset_save_location.setCheckable(False)
        self.reset_save_location.setChecked(False)
        self.stop_compute = QAction(MainWindow)
        self.stop_compute.setObjectName(u"stop_compute")
        self.stop_app = QAction(MainWindow)
        self.stop_app.setObjectName(u"stop_app")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.gridLayout_2 = QGridLayout(self.central_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.search_box = QPlainTextEdit(self.central_widget)
        self.search_box.setObjectName(u"search_box")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.search_box.sizePolicy().hasHeightForWidth())
        self.search_box.setSizePolicy(sizePolicy)
        self.search_box.setMinimumSize(QSize(250, 0))
        self.search_box.setMaximumSize(QSize(16777215, 55))
        self.search_box.setLayoutDirection(Qt.LeftToRight)
        self.search_box.setFrameShape(QFrame.StyledPanel)
        self.search_box.setLineWidth(1)

        self.gridLayout.addWidget(self.search_box, 0, 0, 1, 1)

        self.choices_list_box = QListWidget(self.central_widget)
        QListWidgetItem(self.choices_list_box)
        self.choices_list_box.setObjectName(u"choices_list_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(7)
        sizePolicy1.setHeightForWidth(self.choices_list_box.sizePolicy().hasHeightForWidth())
        self.choices_list_box.setSizePolicy(sizePolicy1)
        self.choices_list_box.setMinimumSize(QSize(250, 0))
        self.choices_list_box.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.choices_list_box, 1, 0, 14, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_button = QPushButton(self.central_widget)
        self.start_button.setObjectName(u"start_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy2)
        self.start_button.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.start_button)

        self.save_check = QCheckBox(self.central_widget)
        self.save_check.setObjectName(u"save_check")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.save_check.sizePolicy().hasHeightForWidth())
        self.save_check.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.save_check)

        self.test_check = QCheckBox(self.central_widget)
        self.test_check.setObjectName(u"test_check")
        sizePolicy3.setHeightForWidth(self.test_check.sizePolicy().hasHeightForWidth())
        self.test_check.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.test_check)

        self.output_optimization_check = QCheckBox(self.central_widget)
        self.output_optimization_check.setObjectName(u"output_optimization_check")
        sizePolicy3.setHeightForWidth(self.output_optimization_check.sizePolicy().hasHeightForWidth())
        self.output_optimization_check.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.output_optimization_check)

        self.output_lock_maximums_check = QCheckBox(self.central_widget)
        self.output_lock_maximums_check.setObjectName(u"output_lock_maximums_check")
        sizePolicy3.setHeightForWidth(self.output_lock_maximums_check.sizePolicy().hasHeightForWidth())
        self.output_lock_maximums_check.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.output_lock_maximums_check)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.input_box = QPlainTextEdit(self.central_widget)
        self.input_box.setObjectName(u"input_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(5)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.input_box.sizePolicy().hasHeightForWidth())
        self.input_box.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.input_box, 0, 1, 3, 1)

        self.output_box = QPlainTextEdit(self.central_widget)
        self.output_box.setObjectName(u"output_box")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(5)
        sizePolicy5.setVerticalStretch(5)
        sizePolicy5.setHeightForWidth(self.output_box.sizePolicy().hasHeightForWidth())
        self.output_box.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.output_box, 4, 1, 11, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 1015, 22))
        self.about__menu = QMenu(self.menu_bar)
        self.about__menu.setObjectName(u"about__menu")
        self.reset_menu = QMenu(self.menu_bar)
        self.reset_menu.setObjectName(u"reset_menu")
        self.stop_menu = QMenu(self.menu_bar)
        self.stop_menu.setObjectName(u"stop_menu")
        self.setting_menu = QMenu(self.menu_bar)
        self.setting_menu.setObjectName(u"setting_menu")
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        QWidget.setTabOrder(self.search_box, self.start_button)
        QWidget.setTabOrder(self.start_button, self.test_check)
        QWidget.setTabOrder(self.test_check, self.output_optimization_check)
        QWidget.setTabOrder(self.output_optimization_check, self.output_lock_maximums_check)

        self.menu_bar.addAction(self.reset_menu.menuAction())
        self.menu_bar.addAction(self.setting_menu.menuAction())
        self.menu_bar.addAction(self.stop_menu.menuAction())
        self.menu_bar.addAction(self.about__menu.menuAction())
        self.about__menu.addAction(self.cheak_update)
        self.about__menu.addAction(self.show_todo)
        self.about__menu.addAction(self.show_about)
        self.about__menu.addSeparator()
        self.about__menu.addAction(self.show_update_log)
        self.reset_menu.addAction(self.reset_save_location)
        self.stop_menu.addAction(self.stop_compute)
        self.stop_menu.addAction(self.stop_app)

        self.retranslateUi(MainWindow)
        self.start_button.clicked.connect(MainWindow.startEvent)
        self.save_check.clicked.connect(MainWindow.saveCheckEvent)
        self.test_check.clicked.connect(MainWindow.testCheckEvent)
        self.output_optimization_check.clicked.connect(MainWindow.outputOptimizationCheckEvent)
        self.output_lock_maximums_check.clicked.connect(MainWindow.outputLockMaximumsCheckEvent)
        self.choices_list_box.itemClicked.connect(MainWindow.chooseNumberEvent)
        self.menu_bar.triggered.connect(MainWindow.menuBar)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"hpycacular", None))
        self.cheak_update.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u65e5\u5fd7", None))
        self.show_todo.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u5c55\u671b", None))
        self.show_about.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u5c4f\u4ecb\u7ecd", None))
        self.show_update_log.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.reset_save_location.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u4fdd\u5b58\u8def\u5f84", None))
        self.stop_compute.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u5f53\u524d\u8fd0\u7b97", None))
        self.stop_app.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7a0b\u5e8f", None))
        self.search_box.setPlainText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u540e\u56de\u8f66\u8fdb\u884c\u641c\u7d22", None))

        __sortingEnabled = self.choices_list_box.isSortingEnabled()
        self.choices_list_box.setSortingEnabled(False)
        ___qlistwidgetitem = self.choices_list_box.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u641c\u7d22\u6846\u5c31\u53ef\u4ee5\u663e\u793a\u6240\u6709\u7684\u63d2\u4ef6\u4e86", None));
        self.choices_list_box.setSortingEnabled(__sortingEnabled)

        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.save_check.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8f93\u51fa\u5230\u6587\u4ef6", None))
        self.test_check.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6a21\u5f0f", None))
        self.output_optimization_check.setText(QCoreApplication.translate("MainWindow", u"\u5185\u6846\u8f93\u51fa\u6027\u80fd\u4f18\u5316", None))
        self.output_lock_maximums_check.setText(QCoreApplication.translate("MainWindow", u"\u5185\u6846\u8f93\u51fa\u4e0a\u9650", None))
        self.about__menu.setTitle(QCoreApplication.translate("MainWindow", u"|---\u5173\u4e8e---|", None))
        self.reset_menu.setTitle(QCoreApplication.translate("MainWindow", u"|---\u91cd\u7f6e---|", None))
        self.stop_menu.setTitle(QCoreApplication.translate("MainWindow", u"|---\u7ec8\u6b62---|", None))
        self.setting_menu.setTitle(QCoreApplication.translate("MainWindow", u"|---\u8bbe\u7f6e---|", None))
    # retranslateUi

