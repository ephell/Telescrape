# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgressWidget.ui'
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

from src.gui.main_window.central_widget.scrape_widget.scroll_area_widget.progress_container_widget.progress_widget.elidable_label import ElidableLabel

class Ui_ProgressWidget(object):
    def setupUi(self, ProgressWidget):
        if not ProgressWidget.objectName():
            ProgressWidget.setObjectName(u"ProgressWidget")
        ProgressWidget.resize(780, 17)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressWidget.sizePolicy().hasHeightForWidth())
        ProgressWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(ProgressWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.status_image_label = QLabel(ProgressWidget)
        self.status_image_label.setObjectName(u"status_image_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.status_image_label.sizePolicy().hasHeightForWidth())
        self.status_image_label.setSizePolicy(sizePolicy1)
        self.status_image_label.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.status_image_label)

        self.line = QFrame(ProgressWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.selection_title_label = ElidableLabel(ProgressWidget)
        self.selection_title_label.setObjectName(u"selection_title_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.selection_title_label.sizePolicy().hasHeightForWidth())
        self.selection_title_label.setSizePolicy(sizePolicy2)
        self.selection_title_label.setMinimumSize(QSize(300, 0))
        self.selection_title_label.setMaximumSize(QSize(250, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.selection_title_label.setFont(font)

        self.horizontalLayout.addWidget(self.selection_title_label)

        self.line_2 = QFrame(ProgressWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.status_message_label = ElidableLabel(ProgressWidget)
        self.status_message_label.setObjectName(u"status_message_label")
        sizePolicy2.setHeightForWidth(self.status_message_label.sizePolicy().hasHeightForWidth())
        self.status_message_label.setSizePolicy(sizePolicy2)
        self.status_message_label.setMinimumSize(QSize(400, 0))
        self.status_message_label.setMaximumSize(QSize(250, 16777215))
        self.status_message_label.setFont(font)

        self.horizontalLayout.addWidget(self.status_message_label)


        self.retranslateUi(ProgressWidget)

        QMetaObject.connectSlotsByName(ProgressWidget)
    # setupUi

    def retranslateUi(self, ProgressWidget):
        ProgressWidget.setWindowTitle(QCoreApplication.translate("ProgressWidget", u"Form", None))
        self.status_image_label.setText(QCoreApplication.translate("ProgressWidget", u"Status Image", None))
        self.selection_title_label.setText(QCoreApplication.translate("ProgressWidget", u"Selection Title Label", None))
        self.status_message_label.setText(QCoreApplication.translate("ProgressWidget", u"Status Message Label", None))
    # retranslateUi

