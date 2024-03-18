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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_OverlayWidget(object):
    def setupUi(self, OverlayWidget):
        if not OverlayWidget.objectName():
            OverlayWidget.setObjectName(u"OverlayWidget")
        OverlayWidget.resize(253, 218)
        self.verticalLayout_3 = QVBoxLayout(OverlayWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.message_label = QLabel(OverlayWidget)
        self.message_label.setObjectName(u"message_label")

        self.verticalLayout_2.addWidget(self.message_label, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image_label = QLabel(OverlayWidget)
        self.image_label.setObjectName(u"image_label")

        self.verticalLayout.addWidget(self.image_label, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(OverlayWidget)

        QMetaObject.connectSlotsByName(OverlayWidget)
    # setupUi

    def retranslateUi(self, OverlayWidget):
        OverlayWidget.setWindowTitle(QCoreApplication.translate("OverlayWidget", u"Form", None))
        self.message_label.setText(QCoreApplication.translate("OverlayWidget", u"Message label", None))
        self.image_label.setText(QCoreApplication.translate("OverlayWidget", u"Image label", None))
    # retranslateUi

