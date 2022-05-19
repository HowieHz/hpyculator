# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_win.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QWidget)

class Ui_AboutWin(object):
    def setupUi(self, AboutWin):
        if not AboutWin.objectName():
            AboutWin.setObjectName(u"AboutWin")
        AboutWin.resize(761, 570)
        AboutWin.setMinimumSize(QSize(761, 570))
        AboutWin.setMaximumSize(QSize(761, 570))
        self.gridLayout = QGridLayout(AboutWin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.choices_doc = QComboBox(AboutWin)
        self.choices_doc.setObjectName(u"choices_doc")
        font = QFont()
        font.setPointSize(14)
        self.choices_doc.setFont(font)

        self.horizontalLayout.addWidget(self.choices_doc)

        self.label_2 = QLabel(AboutWin)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u66f4\u7eb1\u9ed1\u4f53 UI SC Light"])
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)

        self.output_doc = QTextEdit(AboutWin)
        self.output_doc.setObjectName(u"output_doc")
        self.output_doc.setFont(font)

        self.gridLayout.addWidget(self.output_doc, 5, 0, 1, 2)

        self.label = QLabel(AboutWin)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"\u66f4\u7eb1\u9ed1\u4f53 UI SC"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(AboutWin)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(200, 35))
        font3 = QFont()
        font3.setFamilies([u"\u66f4\u7eb1\u9ed1\u4f53 UI SC"])
        font3.setPointSize(14)
        self.pushButton.setFont(font3)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)


        self.retranslateUi(AboutWin)
        self.choices_doc.currentTextChanged.connect(AboutWin.chooseShow)
        self.pushButton.clicked.connect(AboutWin.checkUpdate)

        QMetaObject.connectSlotsByName(AboutWin)
    # setupUi

    def retranslateUi(self, AboutWin):
        AboutWin.setWindowTitle(QCoreApplication.translate("AboutWin", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AboutWin", u"\u9009\u62e9\u4f60\u8981\u67e5\u770b\u7684\u5185\u5bb9", None))
        self.label.setText(QCoreApplication.translate("AboutWin", u"\u5173\u4e8ehpycacular", None))
        self.pushButton.setText(QCoreApplication.translate("AboutWin", u"\u68c0\u67e5\u66f4\u65b0", None))
    # retranslateUi

