from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication


class Application(QApplication):

    STYLE = "Fusion"

    def __init__(self, argv):
        super().__init__(argv)
        self.setStyle(self.STYLE)
        self.setPalette(self._get_default_palette(self))

    def _get_default_palette(self, application: QApplication):
        palette = application.palette()
        palette.setColorGroup(
            QPalette.Active,     # color group
            Qt.white,            # windowText
            QColor(65, 65, 65),  # button
            QColor(95, 95, 95),  # light
            QColor(40, 40, 40),  # dark
            QColor(60, 60, 60),  # mid
            Qt.white,            # text
            Qt.blue,             # bright_text
            QColor(55, 55, 55),  # base
            QColor(40, 40, 40)   # window
        )
        palette.setColorGroup(
            QPalette.Inactive,   # color group
            Qt.white,            # windowText
            QColor(65, 65, 65),  # button
            QColor(95, 95, 95),  # light
            QColor(40, 40, 40),  # dark
            QColor(60, 60, 60),  # mid
            Qt.white,            # text
            Qt.blue,             # bright_text
            QColor(55, 55, 55),  # base
            QColor(40, 40, 40)   # window
        )
        return palette
