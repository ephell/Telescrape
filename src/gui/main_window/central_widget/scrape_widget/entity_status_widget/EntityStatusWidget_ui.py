# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EntityStatusWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_EntityStatusWidget(object):
    def setupUi(self, EntityStatusWidget):
        if not EntityStatusWidget.objectName():
            EntityStatusWidget.setObjectName(u"EntityStatusWidget")
        EntityStatusWidget.resize(385, 36)
        self.horizontalLayout_2 = QHBoxLayout(EntityStatusWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.status_image_label = QLabel(EntityStatusWidget)
        self.status_image_label.setObjectName(u"status_image_label")

        self.horizontalLayout.addWidget(self.status_image_label)

        self.entity_title_label = QLabel(EntityStatusWidget)
        self.entity_title_label.setObjectName(u"entity_title_label")

        self.horizontalLayout.addWidget(self.entity_title_label)

        self.status_message_label = QLabel(EntityStatusWidget)
        self.status_message_label.setObjectName(u"status_message_label")

        self.horizontalLayout.addWidget(self.status_message_label)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(EntityStatusWidget)

        QMetaObject.connectSlotsByName(EntityStatusWidget)
    # setupUi

    def retranslateUi(self, EntityStatusWidget):
        EntityStatusWidget.setWindowTitle(QCoreApplication.translate("EntityStatusWidget", u"Form", None))
        self.status_image_label.setText(QCoreApplication.translate("EntityStatusWidget", u"Status Image", None))
        self.entity_title_label.setText(QCoreApplication.translate("EntityStatusWidget", u"Entity Title", None))
        self.status_message_label.setText(QCoreApplication.translate("EntityStatusWidget", u"Status Message", None))
    # retranslateUi

