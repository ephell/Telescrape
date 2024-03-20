# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScrapeWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ScrapeWidget(object):
    def setupUi(self, ScrapeWidget):
        if not ScrapeWidget.objectName():
            ScrapeWidget.setObjectName(u"ScrapeWidget")
        ScrapeWidget.resize(281, 138)
        self.verticalLayout = QVBoxLayout(ScrapeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(ScrapeWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.scrollArea = QScrollArea(ScrapeWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QSize(16777215, 90))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 261, 88))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(ScrapeWidget)

        QMetaObject.connectSlotsByName(ScrapeWidget)
    # setupUi

    def retranslateUi(self, ScrapeWidget):
        ScrapeWidget.setWindowTitle(QCoreApplication.translate("ScrapeWidget", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("ScrapeWidget", u"Button", None))
    # retranslateUi

