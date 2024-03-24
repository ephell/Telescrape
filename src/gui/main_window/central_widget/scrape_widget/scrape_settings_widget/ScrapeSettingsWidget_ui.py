# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScrapeSettingsWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_ScrapeSettingsWidget(object):
    def setupUi(self, ScrapeSettingsWidget):
        if not ScrapeSettingsWidget.objectName():
            ScrapeSettingsWidget.setObjectName(u"ScrapeSettingsWidget")
        ScrapeSettingsWidget.setWindowModality(Qt.ApplicationModal)
        ScrapeSettingsWidget.resize(453, 205)
        self.verticalLayout_2 = QVBoxLayout(ScrapeSettingsWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.past_active_days_label = QLabel(ScrapeSettingsWidget)
        self.past_active_days_label.setObjectName(u"past_active_days_label")
        font = QFont()
        font.setPointSize(11)
        self.past_active_days_label.setFont(font)

        self.horizontalLayout.addWidget(self.past_active_days_label)

        self.past_active_days_spin_box = QSpinBox(ScrapeSettingsWidget)
        self.past_active_days_spin_box.setObjectName(u"past_active_days_spin_box")
        self.past_active_days_spin_box.setMaximum(9999)

        self.horizontalLayout.addWidget(self.past_active_days_spin_box)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.exclude_label = QLabel(ScrapeSettingsWidget)
        self.exclude_label.setObjectName(u"exclude_label")
        self.exclude_label.setFont(font)

        self.verticalLayout.addWidget(self.exclude_label)

        self.bots_check_box = QCheckBox(ScrapeSettingsWidget)
        self.bots_check_box.setObjectName(u"bots_check_box")
        font1 = QFont()
        font1.setPointSize(10)
        self.bots_check_box.setFont(font1)
        self.bots_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.bots_check_box)

        self.deleted_users_check_box = QCheckBox(ScrapeSettingsWidget)
        self.deleted_users_check_box.setObjectName(u"deleted_users_check_box")
        self.deleted_users_check_box.setFont(font1)
        self.deleted_users_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.deleted_users_check_box)

        self.restricted_users_check_box = QCheckBox(ScrapeSettingsWidget)
        self.restricted_users_check_box.setObjectName(u"restricted_users_check_box")
        self.restricted_users_check_box.setFont(font1)
        self.restricted_users_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.restricted_users_check_box)

        self.scam_flagged_users_check_box = QCheckBox(ScrapeSettingsWidget)
        self.scam_flagged_users_check_box.setObjectName(u"scam_flagged_users_check_box")
        self.scam_flagged_users_check_box.setFont(font1)
        self.scam_flagged_users_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.scam_flagged_users_check_box)

        self.spam_flagged_users_check_box = QCheckBox(ScrapeSettingsWidget)
        self.spam_flagged_users_check_box.setObjectName(u"spam_flagged_users_check_box")
        self.spam_flagged_users_check_box.setFont(font1)
        self.spam_flagged_users_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.spam_flagged_users_check_box)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(ScrapeSettingsWidget)

        QMetaObject.connectSlotsByName(ScrapeSettingsWidget)
    # setupUi

    def retranslateUi(self, ScrapeSettingsWidget):
        ScrapeSettingsWidget.setWindowTitle(QCoreApplication.translate("ScrapeSettingsWidget", u"Form", None))
        self.past_active_days_label.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Get users active in past days (0 = activity doesn't matter):", None))
        self.exclude_label.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Exclude:", None))
        self.bots_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Bots", None))
        self.deleted_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Deleted users", None))
        self.restricted_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Restricted users", None))
        self.scam_flagged_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users flagged as scam", None))
        self.spam_flagged_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users flagged as fake", None))
    # retranslateUi

