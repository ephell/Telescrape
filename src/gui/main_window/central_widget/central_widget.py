from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget

from src.gui.main_window.central_widget.base_widget.base_widget import BaseWidget
from src.gui.main_window.central_widget.overlay_widget.overlay_widget import OverlayWidget


class CentralWidget(QWidget):

    def __init__(self, main_window=None):
        super().__init__(main_window)
        self.base_widget = self._set_base_widget(BaseWidget(self))
        self.overlay_widget = self._set_overlay_widget(OverlayWidget(self))
        self.resize(self.base_widget.size())
        if main_window is not None:
            main_window.resize(self.size())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._base_widget_container.resize(self.size())
        self._overlay_widget_container.resize(self.size())

    def set_base_widget_hidden(self, value: bool):
        self._set_widget_container_hidden(self._base_widget_container, value)

    def set_overlay_widget_hidden(self, value: bool):
        self._set_widget_container_hidden(self._overlay_widget_container, value)

    def _set_base_widget(self, base_widget):
        self._base_widget_container = QWidget(self)
        self._base_widget_container.resize(base_widget.size())
        self._base_widget_container.setLayout(QVBoxLayout())
        self._base_widget_container.layout().addWidget(base_widget)
        return base_widget

    def _set_overlay_widget(self, overlay_widget):
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

    def _set_widget_container_hidden(self, widget_container: QWidget, value: bool):
        widget_container.setHidden(value)
        if value:
            widget_container.raise_()


if __name__ == "__main__":
    app = QApplication([])
    container = CentralWidget(None)
    container.show()
    app.exec()
