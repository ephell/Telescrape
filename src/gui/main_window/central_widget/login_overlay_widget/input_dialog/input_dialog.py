if __name__ == "__main__":
    import os
    __package__ = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace(os.path.sep, ".")

from PySide6.QtWidgets import QDialog

from .InputDialog_ui import Ui_InputDialog


class InputDialog(QDialog, Ui_InputDialog):
    """Used to retrive login cod and/or 2 FA password during login."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # self.setWindowTitle("Login Code Input")

    def closeEvent(self, event):
        self.buttonBox.rejected.emit()
        super().closeEvent(event)


if __name__ == "__main__":
    import sys

    from src.gui.application import Application
    app = Application(sys.argv)
    cd = InputDialog() 
    cd.show()
    app.exec()
