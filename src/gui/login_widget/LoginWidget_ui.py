# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWidget.ui'
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

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(407, 103)
        self.verticalLayout = QVBoxLayout(LoginWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.status_message_label = QLabel(LoginWidget)
        self.status_message_label.setObjectName(u"status_message_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_message_label.sizePolicy().hasHeightForWidth())
        self.status_message_label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.status_message_label.setFont(font)
        self.status_message_label.setAlignment(Qt.AlignCenter)
        self.status_message_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.status_message_label, 0, Qt.AlignHCenter)

        self.status_image_placeholder_label = QLabel(LoginWidget)
        self.status_image_placeholder_label.setObjectName(u"status_image_placeholder_label")

        self.verticalLayout.addWidget(self.status_image_placeholder_label, 0, Qt.AlignHCenter)


        self.retranslateUi(LoginWidget)

        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Login Widget", None))
        self.status_message_label.setText(QCoreApplication.translate("LoginWidget", u"STATUS MESSAGE", None))
        self.status_image_placeholder_label.setText(QCoreApplication.translate("LoginWidget", u".GIF PLACEHOLDER", None))
    # retranslateUi

