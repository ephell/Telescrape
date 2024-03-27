# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgressContainerWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ProgressContainerWidget(object):
    def setupUi(self, ProgressContainerWidget):
        if not ProgressContainerWidget.objectName():
            ProgressContainerWidget.setObjectName(u"ProgressContainerWidget")
        ProgressContainerWidget.resize(467, 253)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressContainerWidget.sizePolicy().hasHeightForWidth())
        ProgressContainerWidget.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(ProgressContainerWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.counter_label = QLabel(ProgressContainerWidget)
        self.counter_label.setObjectName(u"counter_label")
        font = QFont()
        font.setPointSize(11)
        self.counter_label.setFont(font)

        self.verticalLayout_3.addWidget(self.counter_label, 0, Qt.AlignHCenter)

        self.progress_widget_container_frame = QFrame(ProgressContainerWidget)
        self.progress_widget_container_frame.setObjectName(u"progress_widget_container_frame")
        self.progress_widget_container_frame.setFrameShape(QFrame.NoFrame)
        self.progress_widget_container_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.progress_widget_container_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.progress_widget_container_frame)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_3.setStretch(1, 1)

        self.retranslateUi(ProgressContainerWidget)

        QMetaObject.connectSlotsByName(ProgressContainerWidget)
    # setupUi

    def retranslateUi(self, ProgressContainerWidget):
        ProgressContainerWidget.setWindowTitle(QCoreApplication.translate("ProgressContainerWidget", u"Form", None))
        self.counter_label.setText(QCoreApplication.translate("ProgressContainerWidget", u"CounterLabel", None))
    # retranslateUi

