from PySide6.QtWidgets import QDialog

from src.gui.login_widget.login_code_input_dialog.LoginCodeInputDialog_ui import Ui_LoginCodeInputDialog


class LoginCodeInputDialog(QDialog, Ui_LoginCodeInputDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Login Code Input")

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
