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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_ScrapeSettingsWidget(object):
    def setupUi(self, ScrapeSettingsWidget):
        if not ScrapeSettingsWidget.objectName():
            ScrapeSettingsWidget.setObjectName(u"ScrapeSettingsWidget")
        ScrapeSettingsWidget.setWindowModality(Qt.ApplicationModal)
        ScrapeSettingsWidget.resize(474, 367)
        self.verticalLayout_3 = QVBoxLayout(ScrapeSettingsWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.exclude_frame = QFrame(ScrapeSettingsWidget)
        self.exclude_frame.setObjectName(u"exclude_frame")
        self.exclude_frame.setFrameShape(QFrame.StyledPanel)
        self.exclude_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.exclude_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.last_active_days_label = QLabel(self.exclude_frame)
        self.last_active_days_label.setObjectName(u"last_active_days_label")
        font = QFont()
        font.setPointSize(11)
        self.last_active_days_label.setFont(font)

        self.horizontalLayout.addWidget(self.last_active_days_label)

        self.last_active_days_spin_box = QSpinBox(self.exclude_frame)
        self.last_active_days_spin_box.setObjectName(u"last_active_days_spin_box")
        font1 = QFont()
        font1.setPointSize(10)
        self.last_active_days_spin_box.setFont(font1)
        self.last_active_days_spin_box.setMaximum(9999)

        self.horizontalLayout.addWidget(self.last_active_days_spin_box)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.exclude_label = QLabel(self.exclude_frame)
        self.exclude_label.setObjectName(u"exclude_label")
        self.exclude_label.setFont(font)

        self.verticalLayout.addWidget(self.exclude_label)

        self.yourself_check_box = QCheckBox(self.exclude_frame)
        self.yourself_check_box.setObjectName(u"yourself_check_box")
        self.yourself_check_box.setFont(font1)
        self.yourself_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.yourself_check_box)

        self.admins_check_box = QCheckBox(self.exclude_frame)
        self.admins_check_box.setObjectName(u"admins_check_box")
        self.admins_check_box.setFont(font1)
        self.admins_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.admins_check_box)

        self.bots_check_box = QCheckBox(self.exclude_frame)
        self.bots_check_box.setObjectName(u"bots_check_box")
        self.bots_check_box.setFont(font1)
        self.bots_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.bots_check_box)

        self.deleted_users_check_box = QCheckBox(self.exclude_frame)
        self.deleted_users_check_box.setObjectName(u"deleted_users_check_box")
        self.deleted_users_check_box.setFont(font1)
        self.deleted_users_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.deleted_users_check_box)

        self.restricted_users_check_box = QCheckBox(self.exclude_frame)
        self.restricted_users_check_box.setObjectName(u"restricted_users_check_box")
        self.restricted_users_check_box.setFont(font1)
        self.restricted_users_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.restricted_users_check_box)

        self.scam_flagged_users_check_box = QCheckBox(self.exclude_frame)
        self.scam_flagged_users_check_box.setObjectName(u"scam_flagged_users_check_box")
        self.scam_flagged_users_check_box.setFont(font1)
        self.scam_flagged_users_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.scam_flagged_users_check_box)

        self.fake_flagged_users_check_box = QCheckBox(self.exclude_frame)
        self.fake_flagged_users_check_box.setObjectName(u"fake_flagged_users_check_box")
        self.fake_flagged_users_check_box.setFont(font1)
        self.fake_flagged_users_check_box.setChecked(True)

        self.verticalLayout.addWidget(self.fake_flagged_users_check_box)

        self.users_in_contacts_check_box = QCheckBox(self.exclude_frame)
        self.users_in_contacts_check_box.setObjectName(u"users_in_contacts_check_box")
        self.users_in_contacts_check_box.setFont(font1)
        self.users_in_contacts_check_box.setChecked(False)

        self.verticalLayout.addWidget(self.users_in_contacts_check_box)

        self.users_with_hidden_last_seen_online_check_box = QCheckBox(self.exclude_frame)
        self.users_with_hidden_last_seen_online_check_box.setObjectName(u"users_with_hidden_last_seen_online_check_box")
        self.users_with_hidden_last_seen_online_check_box.setFont(font1)
        self.users_with_hidden_last_seen_online_check_box.setChecked(False)

        self.verticalLayout.addWidget(self.users_with_hidden_last_seen_online_check_box)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.exclude_frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_button = QPushButton(ScrapeSettingsWidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.close_button)

        self.reset_to_default_button = QPushButton(ScrapeSettingsWidget)
        self.reset_to_default_button.setObjectName(u"reset_to_default_button")
        self.reset_to_default_button.setMinimumSize(QSize(115, 0))
        self.reset_to_default_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.reset_to_default_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ScrapeSettingsWidget)

        QMetaObject.connectSlotsByName(ScrapeSettingsWidget)
    # setupUi

    def retranslateUi(self, ScrapeSettingsWidget):
        ScrapeSettingsWidget.setWindowTitle(QCoreApplication.translate("ScrapeSettingsWidget", u"Form", None))
        self.last_active_days_label.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Get users active in last days (0 = activity doesn't matter):", None))
        self.exclude_label.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Exclude:", None))
        self.yourself_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Yourself", None))
        self.admins_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Admins", None))
        self.bots_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Bots", None))
        self.deleted_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Deleted users", None))
        self.restricted_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Restricted users", None))
        self.scam_flagged_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users flagged as scam", None))
        self.fake_flagged_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users flagged as fake", None))
        self.users_in_contacts_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users in your contacts", None))
        self.users_with_hidden_last_seen_online_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users with hidden 'last seen online' status", None))
        self.close_button.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Close", None))
        self.reset_to_default_button.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Reset to Default", None))
    # retranslateUi

