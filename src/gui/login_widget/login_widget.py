import asyncio

from PySide6.QtCore import QByteArray, QSize
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QMessageBox, QWidget

from src.gui.login_widget.login_code_input_dialog.login_code_input_dialog import LoginCodeInputDialog
from src.gui.login_widget.LoginWidget_ui import Ui_LoginWidget


class LoginWidget(Ui_LoginWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.status_image_placeholder_label.setMaximumSize(QSize(30, 30))
        self.status_image_placeholder_label.setScaledContents(True)
        self.set_status_image_loading()

    def set_status_message(self, message: str):
        self.status_message_label.setText(message)

    def set_status_image_loading(self):
        self.loader_gif_player = QMovie(
            "src/gui/login_widget/loader.gif", 
            QByteArray(), 
            self
        )
        self.status_image_placeholder_label.setMovie(self.loader_gif_player)
        self.loader_gif_player.start()

    def set_status_image_success(self):
        self.status_image_placeholder_label.setPixmap(
            QPixmap("src/gui/login_widget/status_success.png")
        )

    def set_status_image_fail(self):
        self.status_image_placeholder_label.setPixmap(
            QPixmap("src/gui/login_widget/status_fail.png")
        )

    async def open_error_message_box(self, text: str):
        QMessageBox(QMessageBox.Critical, "Error", text, parent=self).show()

    async def open_login_code_input_dialog_and_get_input(self):
        future = asyncio.Future()
        self.dialog = LoginCodeInputDialog(self)
        self.dialog.buttonBox.accepted.connect(lambda: future.set_result(self.dialog.lineEdit.text()))
        self.dialog.buttonBox.rejected.connect(lambda: future.set_result(None))
        self.dialog.show()
        await future
        return future.result()


if __name__ == "__main__":
    import sys

    from src.gui.application.application import Application
    app = Application(sys.argv)
    widget = LoginWidget() 
    widget.show()
    widget.open_error_message_box("Duxas")
    app.exec()
