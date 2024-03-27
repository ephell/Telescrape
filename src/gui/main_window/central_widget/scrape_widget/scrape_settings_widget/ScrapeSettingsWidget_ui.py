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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_ScrapeSettingsWidget(object):
    def setupUi(self, ScrapeSettingsWidget):
        if not ScrapeSettingsWidget.objectName():
            ScrapeSettingsWidget.setObjectName(u"ScrapeSettingsWidget")
        ScrapeSettingsWidget.setWindowModality(Qt.ApplicationModal)
        ScrapeSettingsWidget.resize(518, 404)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScrapeSettingsWidget.sizePolicy().hasHeightForWidth())
        ScrapeSettingsWidget.setSizePolicy(sizePolicy)
        ScrapeSettingsWidget.setMinimumSize(QSize(518, 404))
        self.verticalLayout_5 = QVBoxLayout(ScrapeSettingsWidget)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.exclude_frame = QFrame(ScrapeSettingsWidget)
        self.exclude_frame.setObjectName(u"exclude_frame")
        self.exclude_frame.setFrameShape(QFrame.NoFrame)
        self.exclude_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.exclude_frame)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.exclude_label = QLabel(self.exclude_frame)
        self.exclude_label.setObjectName(u"exclude_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.exclude_label.setFont(font)

        self.verticalLayout.addWidget(self.exclude_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.yourself_check_box = QCheckBox(self.exclude_frame)
        self.yourself_check_box.setObjectName(u"yourself_check_box")
        self.yourself_check_box.setMaximumSize(QSize(190, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.yourself_check_box.setFont(font1)
        self.yourself_check_box.setChecked(False)

        self.horizontalLayout_3.addWidget(self.yourself_check_box)

        self.scam_flagged_users_check_box = QCheckBox(self.exclude_frame)
        self.scam_flagged_users_check_box.setObjectName(u"scam_flagged_users_check_box")
        self.scam_flagged_users_check_box.setFont(font1)
        self.scam_flagged_users_check_box.setChecked(True)

        self.horizontalLayout_3.addWidget(self.scam_flagged_users_check_box)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.admins_check_box = QCheckBox(self.exclude_frame)
        self.admins_check_box.setObjectName(u"admins_check_box")
        self.admins_check_box.setMaximumSize(QSize(190, 16777215))
        self.admins_check_box.setFont(font1)
        self.admins_check_box.setChecked(False)

        self.horizontalLayout_4.addWidget(self.admins_check_box)

        self.fake_flagged_users_check_box = QCheckBox(self.exclude_frame)
        self.fake_flagged_users_check_box.setObjectName(u"fake_flagged_users_check_box")
        self.fake_flagged_users_check_box.setFont(font1)
        self.fake_flagged_users_check_box.setChecked(True)

        self.horizontalLayout_4.addWidget(self.fake_flagged_users_check_box)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bots_check_box = QCheckBox(self.exclude_frame)
        self.bots_check_box.setObjectName(u"bots_check_box")
        self.bots_check_box.setMaximumSize(QSize(190, 16777215))
        self.bots_check_box.setFont(font1)
        self.bots_check_box.setChecked(True)

        self.horizontalLayout_5.addWidget(self.bots_check_box)

        self.users_in_contacts_check_box = QCheckBox(self.exclude_frame)
        self.users_in_contacts_check_box.setObjectName(u"users_in_contacts_check_box")
        self.users_in_contacts_check_box.setFont(font1)
        self.users_in_contacts_check_box.setChecked(False)

        self.horizontalLayout_5.addWidget(self.users_in_contacts_check_box)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.deleted_users_check_box = QCheckBox(self.exclude_frame)
        self.deleted_users_check_box.setObjectName(u"deleted_users_check_box")
        self.deleted_users_check_box.setMaximumSize(QSize(190, 16777215))
        self.deleted_users_check_box.setFont(font1)
        self.deleted_users_check_box.setChecked(True)

        self.horizontalLayout_6.addWidget(self.deleted_users_check_box)

        self.users_with_hidden_last_seen_online_check_box = QCheckBox(self.exclude_frame)
        self.users_with_hidden_last_seen_online_check_box.setObjectName(u"users_with_hidden_last_seen_online_check_box")
        self.users_with_hidden_last_seen_online_check_box.setFont(font1)
        self.users_with_hidden_last_seen_online_check_box.setChecked(False)

        self.horizontalLayout_6.addWidget(self.users_with_hidden_last_seen_online_check_box)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.restricted_users_check_box = QCheckBox(self.exclude_frame)
        self.restricted_users_check_box.setObjectName(u"restricted_users_check_box")
        self.restricted_users_check_box.setMaximumSize(QSize(190, 16777215))
        self.restricted_users_check_box.setFont(font1)
        self.restricted_users_check_box.setChecked(True)

        self.horizontalLayout_7.addWidget(self.restricted_users_check_box)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_5.addWidget(self.exclude_frame)

        self.activity_frame = QFrame(ScrapeSettingsWidget)
        self.activity_frame.setObjectName(u"activity_frame")
        self.activity_frame.setFrameShape(QFrame.NoFrame)
        self.activity_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.activity_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.activity_label = QLabel(self.activity_frame)
        self.activity_label.setObjectName(u"activity_label")
        self.activity_label.setFont(font)

        self.verticalLayout_2.addWidget(self.activity_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.last_active_days_label = QLabel(self.activity_frame)
        self.last_active_days_label.setObjectName(u"last_active_days_label")
        sizePolicy.setHeightForWidth(self.last_active_days_label.sizePolicy().hasHeightForWidth())
        self.last_active_days_label.setSizePolicy(sizePolicy)
        self.last_active_days_label.setMinimumSize(QSize(390, 0))
        self.last_active_days_label.setFont(font1)

        self.horizontalLayout.addWidget(self.last_active_days_label)

        self.last_active_days_spin_box = QSpinBox(self.activity_frame)
        self.last_active_days_spin_box.setObjectName(u"last_active_days_spin_box")
        self.last_active_days_spin_box.setFont(font1)
        self.last_active_days_spin_box.setAlignment(Qt.AlignCenter)
        self.last_active_days_spin_box.setMaximum(999999)

        self.horizontalLayout.addWidget(self.last_active_days_spin_box)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.activity_frame)

        self.save_data_to_frame = QFrame(ScrapeSettingsWidget)
        self.save_data_to_frame.setObjectName(u"save_data_to_frame")
        self.save_data_to_frame.setFrameShape(QFrame.NoFrame)
        self.save_data_to_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.save_data_to_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.save_data_to_label = QLabel(self.save_data_to_frame)
        self.save_data_to_label.setObjectName(u"save_data_to_label")
        self.save_data_to_label.setFont(font)

        self.verticalLayout_3.addWidget(self.save_data_to_label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.data_dir_path_line_edit = QLineEdit(self.save_data_to_frame)
        self.data_dir_path_line_edit.setObjectName(u"data_dir_path_line_edit")
        sizePolicy.setHeightForWidth(self.data_dir_path_line_edit.sizePolicy().hasHeightForWidth())
        self.data_dir_path_line_edit.setSizePolicy(sizePolicy)
        self.data_dir_path_line_edit.setMinimumSize(QSize(393, 0))
        self.data_dir_path_line_edit.setFont(font1)
        self.data_dir_path_line_edit.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.data_dir_path_line_edit)

        self.browse_button = QPushButton(self.save_data_to_frame)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setFont(font1)

        self.horizontalLayout_8.addWidget(self.browse_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_5.addWidget(self.save_data_to_frame)

        self.closing_frame = QFrame(ScrapeSettingsWidget)
        self.closing_frame.setObjectName(u"closing_frame")
        self.closing_frame.setFrameShape(QFrame.NoFrame)
        self.closing_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.closing_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 4)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.close_button = QPushButton(self.closing_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.close_button)

        self.horizontalSpacer_4 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.reset_to_default_button = QPushButton(self.closing_frame)
        self.reset_to_default_button.setObjectName(u"reset_to_default_button")
        self.reset_to_default_button.setMinimumSize(QSize(115, 0))
        self.reset_to_default_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.reset_to_default_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.closing_frame)

        QWidget.setTabOrder(self.yourself_check_box, self.admins_check_box)
        QWidget.setTabOrder(self.admins_check_box, self.bots_check_box)
        QWidget.setTabOrder(self.bots_check_box, self.deleted_users_check_box)
        QWidget.setTabOrder(self.deleted_users_check_box, self.restricted_users_check_box)
        QWidget.setTabOrder(self.restricted_users_check_box, self.scam_flagged_users_check_box)
        QWidget.setTabOrder(self.scam_flagged_users_check_box, self.fake_flagged_users_check_box)
        QWidget.setTabOrder(self.fake_flagged_users_check_box, self.users_in_contacts_check_box)
        QWidget.setTabOrder(self.users_in_contacts_check_box, self.users_with_hidden_last_seen_online_check_box)
        QWidget.setTabOrder(self.users_with_hidden_last_seen_online_check_box, self.last_active_days_spin_box)
        QWidget.setTabOrder(self.last_active_days_spin_box, self.data_dir_path_line_edit)
        QWidget.setTabOrder(self.data_dir_path_line_edit, self.browse_button)
        QWidget.setTabOrder(self.browse_button, self.close_button)
        QWidget.setTabOrder(self.close_button, self.reset_to_default_button)

        self.retranslateUi(ScrapeSettingsWidget)

        QMetaObject.connectSlotsByName(ScrapeSettingsWidget)
    # setupUi

    def retranslateUi(self, ScrapeSettingsWidget):
        ScrapeSettingsWidget.setWindowTitle(QCoreApplication.translate("ScrapeSettingsWidget", u"Form", None))
        self.exclude_label.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Exclude", None))
        self.yourself_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Yourself", None))
        self.scam_flagged_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users flagged as scam", None))
        self.admins_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Admins", None))
        self.fake_flagged_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users flagged as fake", None))
        self.bots_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Bots", None))
        self.users_in_contacts_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users in your contacts", None))
        self.deleted_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Deleted users", None))
        self.users_with_hidden_last_seen_online_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Users with hidden 'last seen online' status", None))
        self.restricted_users_check_box.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Restricted users", None))
        self.activity_label.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Activity", None))
        self.last_active_days_label.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Get users that were active in the last number of days (0 = all users):", None))
        self.save_data_to_label.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Save Data To", None))
        self.data_dir_path_line_edit.setText("")
        self.browse_button.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Browse", None))
        self.close_button.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Close", None))
        self.reset_to_default_button.setText(QCoreApplication.translate("ScrapeSettingsWidget", u"Reset to Default", None))
    # retranslateUi

