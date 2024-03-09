from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from src.gui.main_window.dialog_code_request.CodeRequestDialog_ui import Ui_CodeRequestDialog


class CodeRequestDialog(QDialog, Ui_CodeRequestDialog):

    code_entered = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Code Request Dialog")

    def closeEvent(self, event):
        self.buttonBox.rejected.emit()
        super().closeEvent(event)


if __name__ == "__main__":
    import sys

    from src.gui.application.application import Application
    app = Application(sys.argv)
    cd = CodeRequestDialog() 
    cd.show()
    app.exec()
