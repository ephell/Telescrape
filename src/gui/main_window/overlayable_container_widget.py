from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget


class OverlayableContainerWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.base_widget = None
        self.overlay_widget = None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._base_widget_container.resize(self.size())
        self._overlay_widget_container.resize(self.size())

    def set_base_widget(self, base_widget):
        self.base_widget = base_widget
        self._base_widget_container = QWidget(self)
        self._base_widget_container.setLayout(QVBoxLayout())
        self._base_widget_container.layout().addWidget(self.base_widget)
        self._base_widget_container.resize(self.size())
        self._base_widget_container.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)

    def set_overlay_widget(self, overlay_widget):
        self.overlay_widget = overlay_widget
        self._overlay_widget_container = QWidget(self)
        self._overlay_widget_container.setWindowFlags(Qt.WindowType.Widget | Qt.WindowType.FramelessWindowHint)
        self._overlay_widget_container.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self._overlay_widget_container.setAutoFillBackground(True)
        self._overlay_widget_container.setContentsMargins(0, 0, 0, 0)
        self._overlay_widget_container.setLayout(QVBoxLayout())
        self._overlay_widget_container.layout().addWidget(overlay_widget)
        self._overlay_widget_container.resize(self.size())
        self._overlay_widget_container.layout().setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Set background color.
        style = QApplication.style()
        palette = style.standardPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(200, 200, 200, 150))
        self._overlay_widget_container.setPalette(palette)

    def set_base_hidden(self, value: bool):
        self._set_widget_container_hidden(self._base_widget_container, value)

    def set_overlay_hidden(self, value: bool):
        self._set_widget_container_hidden(self._overlay_widget_container, value)

    def _set_widget_container_hidden(self, widget_container: QWidget, value: bool):
        widget_container.setHidden(value)
        if value:
            widget_container.raise_()


if __name__ == "__main__":
    from PySide6.QtWidgets import QLabel, QPushButton
    app = QApplication([])

    base = QWidget()
    button_1 = QPushButton("Button 1")
    button_2 = QPushButton("Button 2")
    button_3 = QPushButton("Button 3")
    button_1.setFixedSize(300, 100)
    button_2.setFixedSize(300, 100)
    button_3.setFixedSize(300, 100)
    base.setLayout(QVBoxLayout())
    base.layout().addWidget(button_1)
    base.layout().addWidget(button_2)
    base.layout().addWidget(button_3)

    overlay = QWidget(None)
    overlay.setFixedSize(300, 100)
    overlay.setLayout(QVBoxLayout())
    overlay.layout().addWidget(QLabel("Test overlay label with some text."))
    button_hide_overlay = QPushButton("Click to hide overlay.")
    overlay.layout().addWidget(button_hide_overlay)

    container = OverlayableContainerWidget(None)
    container.set_base_widget(base)
    container.set_overlay_widget(overlay)
    container.set_overlay_hidden(True)

    button_hide_overlay.clicked.connect(lambda: container.set_overlay_hidden(True))
    button_2.clicked.connect(lambda: container.set_overlay_hidden(False))

    container.show()

    app.exec()
