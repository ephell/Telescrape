from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from src.gui.main_window.central_widget.login_widget import LoginWidget
from src.gui.main_window.central_widget.overlay_widget.overlay_widget import OverlayWidget
from src.gui.main_window.central_widget.scrape_widget import ScrapeWidget


class CentralWidget(QWidget):

    def __init__(self, main_window: QMainWindow | None = None):
        super().__init__(main_window)
        self.login_widget = self._set_login_widget(LoginWidget(self))
        self.overlay_widget = self._set_overlay_widget(OverlayWidget(self))
        self.set_overlay_widget_hidden(True)
        self.scrape_widget = self._set_scrape_widget(ScrapeWidget(self))
        self.set_scrape_widget_hidden(True)

        self.resize(self.login_widget.size())
        if main_window is not None:
            main_window.resize(self.size())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._login_widget_container.resize(self.size())
        self._overlay_widget_container.resize(self.size())
        self._scrape_widget_container.resize(self.size())

    def set_login_widget_hidden(self, value: bool):
        self._set_widget_container_hidden(self._login_widget_container, value)

    def set_overlay_widget_hidden(self, value: bool):
        self._set_widget_container_hidden(self._overlay_widget_container, value)

    def set_scrape_widget_hidden(self, value: bool):
        self._set_widget_container_hidden(self._scrape_widget_container, value)

    def _set_widget_container_hidden(self, widget_container: QWidget, value: bool):
        widget_container.setHidden(value)
        if value:
            widget_container.raise_()

    def get_login_widget_container_original_size(self):
        return self._login_widget_container_original_size

    def get_scrape_widget_container_original_size(self):
        return self._scrape_widget_container_original_size

    def _set_login_widget(self, login_widget) -> LoginWidget:
        self._login_widget_container = QWidget(self)
        self._login_widget_container.resize(login_widget.size())
        self._login_widget_container_original_size = self._login_widget_container.size()
        self._login_widget_container.setLayout(QVBoxLayout())
        self._login_widget_container.layout().addWidget(login_widget)
        return login_widget

    def _set_overlay_widget(self, overlay_widget) -> OverlayWidget:
        self._overlay_widget_container = QWidget(self)
        self._overlay_widget_container.setWindowFlags(Qt.WindowType.Widget | Qt.WindowType.FramelessWindowHint)
        self._overlay_widget_container.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self._overlay_widget_container.setAutoFillBackground(True)
        self._overlay_widget_container.setContentsMargins(0, 0, 0, 0)
        self._overlay_widget_container.setLayout(QVBoxLayout())
        self._overlay_widget_container.layout().addWidget(overlay_widget)
        # Set background color.
        style = QApplication.style()
        palette = style.standardPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(40, 40, 40, 225))
        self._overlay_widget_container.setPalette(palette)
        return overlay_widget

    def _set_scrape_widget(self, scrape_widget) -> ScrapeWidget:
        self._scrape_widget_container = QWidget(self)
        self._scrape_widget_container.resize(scrape_widget.size())
        self._scrape_widget_container_original_size = self._scrape_widget_container.size()
        self._scrape_widget_container.setLayout(QVBoxLayout())
        self._scrape_widget_container.layout().addWidget(scrape_widget)
        return scrape_widget


if __name__ == "__main__":
    app = QApplication([])
    container = CentralWidget(None)
    container.show()
    app.exec()
