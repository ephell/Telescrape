from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from src.gui.main_window.dialog_login_code_input.LoginCodeInputDialog_ui import Ui_LoginCodeInputDialog


class LoginCodeInputDialog(QDialog, Ui_LoginCodeInputDialog):

    code_entered = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Login Code")

    def closeEvent(self, event):
        self.buttonBox.rejected.emit()
        super().closeEvent(event)


if __name__ == "__main__":
    import sys

    from src.gui.application.application import Application
    app = Application(sys.argv)
    cd = LoginCodeInputDialog() 
    cd.show()
    app.exec()
