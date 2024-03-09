# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CodeRequestDialog.ui'
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
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CodeRequestDialog(object):
    def setupUi(self, CodeRequestDialog):
        if not CodeRequestDialog.objectName():
            CodeRequestDialog.setObjectName(u"CodeRequestDialog")
        CodeRequestDialog.resize(444, 83)
        self.verticalLayout = QVBoxLayout(CodeRequestDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(CodeRequestDialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.buttonBox = QDialogButtonBox(CodeRequestDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CodeRequestDialog)
        self.buttonBox.accepted.connect(CodeRequestDialog.accept)
        self.buttonBox.rejected.connect(CodeRequestDialog.reject)

        QMetaObject.connectSlotsByName(CodeRequestDialog)
    # setupUi

    def retranslateUi(self, CodeRequestDialog):
        CodeRequestDialog.setWindowTitle(QCoreApplication.translate("CodeRequestDialog", u"Dialog", None))
    # retranslateUi

