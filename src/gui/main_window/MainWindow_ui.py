# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
    QMainWindow, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from src.gui.main_window.button_login import LoginButton
from src.gui.main_window.button_logout import LogoutButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(285, 220)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(23)
        font.setBold(True)
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(13)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.line_edit_username = QLineEdit(self.centralwidget)
        self.line_edit_username.setObjectName(u"line_edit_username")

        self.horizontalLayout.addWidget(self.line_edit_username)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.line_edit_phone_number = QLineEdit(self.centralwidget)
        self.line_edit_phone_number.setObjectName(u"line_edit_phone_number")

        self.horizontalLayout_2.addWidget(self.line_edit_phone_number)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.line_edit_api_id = QLineEdit(self.centralwidget)
        self.line_edit_api_id.setObjectName(u"line_edit_api_id")

        self.horizontalLayout_3.addWidget(self.line_edit_api_id)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.line_edit_api_hash = QLineEdit(self.centralwidget)
        self.line_edit_api_hash.setObjectName(u"line_edit_api_hash")

        self.horizontalLayout_4.addWidget(self.line_edit_api_hash)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.login_button = LoginButton(self.centralwidget)
        self.login_button.setObjectName(u"login_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.login_button, 0, Qt.AlignHCenter)

        self.logout_button = LogoutButton(self.centralwidget)
        self.logout_button.setObjectName(u"logout_button")
        sizePolicy1.setHeightForWidth(self.logout_button.sizePolicy().hasHeightForWidth())
        self.logout_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.logout_button, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Telescrape", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"API ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"API HASH", None))
        self.login_button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.logout_button.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
    # retranslateUi

