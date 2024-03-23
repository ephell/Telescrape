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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

from src.gui.main_window.central_widget.scrape_widget.entity_status_widget.entity_title_label import EntityTitleLabel

class Ui_EntityStatusWidget(object):
    def setupUi(self, EntityStatusWidget):
        if not EntityStatusWidget.objectName():
            EntityStatusWidget.setObjectName(u"EntityStatusWidget")
        EntityStatusWidget.resize(576, 34)
        self.horizontalLayout = QHBoxLayout(EntityStatusWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.status_image_label = QLabel(EntityStatusWidget)
        self.status_image_label.setObjectName(u"status_image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_image_label.sizePolicy().hasHeightForWidth())
        self.status_image_label.setSizePolicy(sizePolicy)
        self.status_image_label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.status_image_label)

        self.line = QFrame(EntityStatusWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.entity_title_label = EntityTitleLabel(EntityStatusWidget)
        self.entity_title_label.setObjectName(u"entity_title_label")
        sizePolicy.setHeightForWidth(self.entity_title_label.sizePolicy().hasHeightForWidth())
        self.entity_title_label.setSizePolicy(sizePolicy)
        self.entity_title_label.setMinimumSize(QSize(150, 0))
        self.entity_title_label.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.entity_title_label)

        self.line_2 = QFrame(EntityStatusWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.status_message_label = QLabel(EntityStatusWidget)
        self.status_message_label.setObjectName(u"status_message_label")

        self.horizontalLayout.addWidget(self.status_message_label)


        self.retranslateUi(EntityStatusWidget)

        QMetaObject.connectSlotsByName(EntityStatusWidget)
    # setupUi

    def retranslateUi(self, EntityStatusWidget):
        EntityStatusWidget.setWindowTitle(QCoreApplication.translate("EntityStatusWidget", u"Form", None))
        self.status_image_label.setText(QCoreApplication.translate("EntityStatusWidget", u"Status Image", None))
        self.entity_title_label.setText(QCoreApplication.translate("EntityStatusWidget", u"Entity Title", None))
        self.status_message_label.setText(QCoreApplication.translate("EntityStatusWidget", u"Status Message", None))
    # retranslateUi

