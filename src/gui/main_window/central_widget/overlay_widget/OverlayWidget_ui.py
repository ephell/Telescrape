# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OverlayWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OverlayWidget(object):
    def setupUi(self, OverlayWidget):
        if not OverlayWidget.objectName():
            OverlayWidget.setObjectName(u"OverlayWidget")
        OverlayWidget.resize(253, 218)
        self.verticalLayout_4 = QVBoxLayout(OverlayWidget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.status_message_label = QLabel(OverlayWidget)
        self.status_message_label.setObjectName(u"status_message_label")

        self.verticalLayout_2.addWidget(self.status_message_label, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.continue_button = QPushButton(OverlayWidget)
        self.continue_button.setObjectName(u"continue_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_button.sizePolicy().hasHeightForWidth())
        self.continue_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.continue_button, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.status_image_label = QLabel(OverlayWidget)
        self.status_image_label.setObjectName(u"status_image_label")

        self.verticalLayout.addWidget(self.status_image_label, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 2)
        self.verticalLayout_4.setStretch(2, 1)

        self.retranslateUi(OverlayWidget)

        QMetaObject.connectSlotsByName(OverlayWidget)
    # setupUi

    def retranslateUi(self, OverlayWidget):
        OverlayWidget.setWindowTitle(QCoreApplication.translate("OverlayWidget", u"Form", None))
        self.status_message_label.setText(QCoreApplication.translate("OverlayWidget", u"Message label", None))
        self.continue_button.setText(QCoreApplication.translate("OverlayWidget", u"Continue", None))
        self.status_image_label.setText(QCoreApplication.translate("OverlayWidget", u"Image label", None))
    # retranslateUi

