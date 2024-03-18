from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.central_widget import CentralWidget

from PySide6.QtWidgets import QWidget

from src.gui.main_window.central_widget.base_widget.BaseWidget_ui import Ui_BaseWidget


class BaseWidget(Ui_BaseWidget, QWidget):

    def __init__(self, central_widget: Optional["CentralWidget"] = None):
        super().__init__(central_widget)
        self.central_widget = central_widget
        self.setupUi(self)

    def set_hidden(self, value: bool):
        if self.central_widget is not None:
            self.central_widget.set_base_widget_hidden(value)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    mw = QMainWindow()
    cw = BaseWidget(mw)
    mw.setCentralWidget(cw)
    mw.show()
    app.exec()
