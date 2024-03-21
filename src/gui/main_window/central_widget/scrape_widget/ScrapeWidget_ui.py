# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScrapeWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ScrapeWidget(object):
    def setupUi(self, ScrapeWidget):
        if not ScrapeWidget.objectName():
            ScrapeWidget.setObjectName(u"ScrapeWidget")
        ScrapeWidget.resize(500, 277)
        self.verticalLayout = QVBoxLayout(ScrapeWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.check_boxes_checked_label = QLabel(ScrapeWidget)
        self.check_boxes_checked_label.setObjectName(u"check_boxes_checked_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_boxes_checked_label.sizePolicy().hasHeightForWidth())
        self.check_boxes_checked_label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.check_boxes_checked_label, 0, Qt.AlignHCenter)

        self.scroll_area = QScrollArea(ScrapeWidget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget_contents = QWidget()
        self.scroll_area_widget_contents.setObjectName(u"scroll_area_widget_contents")
        self.scroll_area_widget_contents.setGeometry(QRect(0, 0, 480, 203))
        self.verticalLayout_2 = QVBoxLayout(self.scroll_area_widget_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        self.verticalLayout.addWidget(self.scroll_area)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.get_groups_button = QPushButton(ScrapeWidget)
        self.get_groups_button.setObjectName(u"get_groups_button")

        self.horizontalLayout.addWidget(self.get_groups_button)

        self.select_all_button = QPushButton(ScrapeWidget)
        self.select_all_button.setObjectName(u"select_all_button")

        self.horizontalLayout.addWidget(self.select_all_button)

        self.unselect_all_button = QPushButton(ScrapeWidget)
        self.unselect_all_button.setObjectName(u"unselect_all_button")

        self.horizontalLayout.addWidget(self.unselect_all_button)

        self.scrape_button = QPushButton(ScrapeWidget)
        self.scrape_button.setObjectName(u"scrape_button")

        self.horizontalLayout.addWidget(self.scrape_button)

        self.open_data_dir_button = QPushButton(ScrapeWidget)
        self.open_data_dir_button.setObjectName(u"open_data_dir_button")

        self.horizontalLayout.addWidget(self.open_data_dir_button)

        self.logout_button = QPushButton(ScrapeWidget)
        self.logout_button.setObjectName(u"logout_button")

        self.horizontalLayout.addWidget(self.logout_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(ScrapeWidget)

        QMetaObject.connectSlotsByName(ScrapeWidget)
    # setupUi

    def retranslateUi(self, ScrapeWidget):
        ScrapeWidget.setWindowTitle(QCoreApplication.translate("ScrapeWidget", u"Form", None))
        self.check_boxes_checked_label.setText(QCoreApplication.translate("ScrapeWidget", u"(0/0) Selected.", None))
        self.get_groups_button.setText(QCoreApplication.translate("ScrapeWidget", u"Get Groups", None))
        self.select_all_button.setText(QCoreApplication.translate("ScrapeWidget", u"Select All", None))
        self.unselect_all_button.setText(QCoreApplication.translate("ScrapeWidget", u"Unselect All", None))
        self.scrape_button.setText(QCoreApplication.translate("ScrapeWidget", u"Scrape", None))
        self.open_data_dir_button.setText(QCoreApplication.translate("ScrapeWidget", u"Data Dir", None))
        self.logout_button.setText(QCoreApplication.translate("ScrapeWidget", u"Logout", None))
    # retranslateUi

