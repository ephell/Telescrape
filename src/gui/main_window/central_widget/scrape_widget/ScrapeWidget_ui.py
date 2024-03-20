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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ScrapeWidget(object):
    def setupUi(self, ScrapeWidget):
        if not ScrapeWidget.objectName():
            ScrapeWidget.setObjectName(u"ScrapeWidget")
        ScrapeWidget.resize(419, 277)
        self.verticalLayout = QVBoxLayout(ScrapeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.check_boxes_checked_label = QLabel(ScrapeWidget)
        self.check_boxes_checked_label.setObjectName(u"check_boxes_checked_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_boxes_checked_label.sizePolicy().hasHeightForWidth())
        self.check_boxes_checked_label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.check_boxes_checked_label, 0, Qt.AlignHCenter)

        self.scroll_area = QScrollArea(ScrapeWidget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area_widget_contents.setObjectName(u"scroll_area_widget_contents")
        self.scroll_area_widget_contents.setGeometry(QRect(0, 0, 399, 203))
        self.verticalLayout_2 = QVBoxLayout(self.scroll_area_widget_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        self.verticalLayout.addWidget(self.scroll_area)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(ScrapeWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_3 = QPushButton(ScrapeWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(ScrapeWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(ScrapeWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(ScrapeWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(ScrapeWidget)

        QMetaObject.connectSlotsByName(ScrapeWidget)
    # setupUi

    def retranslateUi(self, ScrapeWidget):
        ScrapeWidget.setWindowTitle(QCoreApplication.translate("ScrapeWidget", u"Form", None))
        self.check_boxes_checked_label.setText(QCoreApplication.translate("ScrapeWidget", u"(0/0) Selected", None))
        self.pushButton.setText(QCoreApplication.translate("ScrapeWidget", u"Get Groups", None))
        self.pushButton_3.setText(QCoreApplication.translate("ScrapeWidget", u"Select All", None))
        self.pushButton_4.setText(QCoreApplication.translate("ScrapeWidget", u"Unselect All", None))
        self.pushButton_5.setText(QCoreApplication.translate("ScrapeWidget", u"Scrape", None))
        self.pushButton_2.setText(QCoreApplication.translate("ScrapeWidget", u"Logout", None))
    # retranslateUi

