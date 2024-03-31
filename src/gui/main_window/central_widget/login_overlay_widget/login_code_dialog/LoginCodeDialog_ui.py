# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginCodeDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginCodeDialog(object):
    def setupUi(self, LoginCodeDialog):
        if not LoginCodeDialog.objectName():
            LoginCodeDialog.setObjectName(u"LoginCodeDialog")
        LoginCodeDialog.resize(259, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginCodeDialog.sizePolicy().hasHeightForWidth())
        LoginCodeDialog.setSizePolicy(sizePolicy)
        LoginCodeDialog.setMinimumSize(QSize(259, 150))
        LoginCodeDialog.setMaximumSize(QSize(259, 150))
        self.verticalLayout = QVBoxLayout(LoginCodeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(LoginCodeDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(LoginCodeDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEdit, 0, Qt.AlignHCenter)

        self.buttonBox = QDialogButtonBox(LoginCodeDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(LoginCodeDialog)
        self.buttonBox.accepted.connect(LoginCodeDialog.accept)
        self.buttonBox.rejected.connect(LoginCodeDialog.reject)

        QMetaObject.connectSlotsByName(LoginCodeDialog)
    # setupUi

    def retranslateUi(self, LoginCodeDialog):
        LoginCodeDialog.setWindowTitle(QCoreApplication.translate("LoginCodeDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("LoginCodeDialog", u"A login code has been sent to you by Telegram via the app. Please enter the code below:", None))
    # retranslateUi

