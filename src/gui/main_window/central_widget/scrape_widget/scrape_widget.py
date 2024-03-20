from PySide6.QtWidgets import QWidget

from src.gui.main_window.central_widget.scrape_widget.ScrapeWidget_ui import Ui_ScrapeWidget


class ScrapeWidget(Ui_ScrapeWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    sw = ScrapeWidget()
    sw.show()
    app.exec()
