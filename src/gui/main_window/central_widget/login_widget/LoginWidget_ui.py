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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from src.gui.main_window.button_login import LoginButton

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(291, 206)
        LoginWidget.setStyleSheet(u"QLineEdit {\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(LoginWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(LoginWidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(LoginWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_edit_phone_number = QLineEdit(LoginWidget)
        self.line_edit_phone_number.setObjectName(u"line_edit_phone_number")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_edit_phone_number.sizePolicy().hasHeightForWidth())
        self.line_edit_phone_number.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(10)
        self.line_edit_phone_number.setFont(font2)
        self.line_edit_phone_number.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.line_edit_phone_number)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(LoginWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_edit_api_id = QLineEdit(LoginWidget)
        self.line_edit_api_id.setObjectName(u"line_edit_api_id")
        sizePolicy1.setHeightForWidth(self.line_edit_api_id.sizePolicy().hasHeightForWidth())
        self.line_edit_api_id.setSizePolicy(sizePolicy1)
        self.line_edit_api_id.setFont(font2)
        self.line_edit_api_id.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.line_edit_api_id)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(LoginWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_edit_api_hash = QLineEdit(LoginWidget)
        self.line_edit_api_hash.setObjectName(u"line_edit_api_hash")
        sizePolicy1.setHeightForWidth(self.line_edit_api_hash.sizePolicy().hasHeightForWidth())
        self.line_edit_api_hash.setSizePolicy(sizePolicy1)
        self.line_edit_api_hash.setFont(font2)
        self.line_edit_api_hash.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.line_edit_api_hash)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.login_button = LoginButton(LoginWidget)
        self.login_button.setObjectName(u"login_button")
        sizePolicy1.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy1)
        self.login_button.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.login_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.retranslateUi(LoginWidget)

        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("LoginWidget", u"Telescrape", None))
        self.label_2.setText(QCoreApplication.translate("LoginWidget", u"Phone Number", None))
        self.label_3.setText(QCoreApplication.translate("LoginWidget", u"API ID", None))
        self.label_4.setText(QCoreApplication.translate("LoginWidget", u"API HASH", None))
        self.login_button.setText(QCoreApplication.translate("LoginWidget", u"Login", None))
    # retranslateUi

