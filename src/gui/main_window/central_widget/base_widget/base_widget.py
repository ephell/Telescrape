from PySide6.QtWidgets import QWidget

from src.gui.main_window.central_widget.base_widget.BaseWidget_ui import Ui_BaseWidget


class BaseWidget(Ui_BaseWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    mw = QMainWindow()
    cw = BaseWidget(mw)
    mw.setCentralWidget(cw)
    mw.show()
    app.exec()
