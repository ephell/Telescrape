from PySide6.QtWidgets import QDialog

from src.gui.main_window.central_widget.login_overlay_widget.login_code_dialog.LoginCodeDialog_ui import Ui_LoginCodeDialog


class LoginCodeInputDialog(QDialog, Ui_LoginCodeDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Login Code Input")

    def closeEvent(self, event):
        self.buttonBox.rejected.emit()
        super().closeEvent(event)


if __name__ == "__main__":
    import sys

    from src.gui.application import Application
    app = Application(sys.argv)
    cd = LoginCodeInputDialog() 
    cd.show()
    app.exec()
