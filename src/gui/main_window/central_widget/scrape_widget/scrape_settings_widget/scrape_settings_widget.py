from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from src.gui.main_window.central_widget.scrape_widget.scrape_settings_widget.ScrapeSettingsWidget_ui import (
    Ui_ScrapeSettingsWidget
)


class ScrapeSettingsWidget(Ui_ScrapeSettingsWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Telescrape - Scrape Settings")
        self.setFocus()
        self.setWindowFlags(Qt.Dialog)
        self.setFixedSize(self.size())

    def show(self):
        super().show()
        self.setFocus()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    ssw = ScrapeSettingsWidget(None)
    ssw.show()
    app.exec()
