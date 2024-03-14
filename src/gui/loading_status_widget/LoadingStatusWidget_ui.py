# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadingStatusWidget.ui'
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

class Ui_LoadingStatusWidget(object):
    def setupUi(self, LoadingStatusWidget):
        if not LoadingStatusWidget.objectName():
            LoadingStatusWidget.setObjectName(u"LoadingStatusWidget")
        LoadingStatusWidget.resize(407, 103)
        self.verticalLayout = QVBoxLayout(LoadingStatusWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.status_message_label = QLabel(LoadingStatusWidget)
        self.status_message_label.setObjectName(u"status_message_label")
        font = QFont()
        font.setPointSize(11)
        self.status_message_label.setFont(font)

        self.verticalLayout.addWidget(self.status_message_label, 0, Qt.AlignHCenter)

        self.status_image_placeholder_label = QLabel(LoadingStatusWidget)
        self.status_image_placeholder_label.setObjectName(u"status_image_placeholder_label")

        self.verticalLayout.addWidget(self.status_image_placeholder_label, 0, Qt.AlignHCenter)


        self.retranslateUi(LoadingStatusWidget)

        QMetaObject.connectSlotsByName(LoadingStatusWidget)
    # setupUi

    def retranslateUi(self, LoadingStatusWidget):
        LoadingStatusWidget.setWindowTitle(QCoreApplication.translate("LoadingStatusWidget", u"Loading Status Dialog", None))
        self.status_message_label.setText(QCoreApplication.translate("LoadingStatusWidget", u"STATUS MESSAGE", None))
        self.status_image_placeholder_label.setText(QCoreApplication.translate("LoadingStatusWidget", u".GIF PLACEHOLDER", None))
    # retranslateUi

