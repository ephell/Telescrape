import os

if __name__ == "__main__":
    __package__ = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace(os.path.sep, ".")

import asyncio
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.gui.main_window.central_widget import CentralWidget

from PySide6.QtCore import QByteArray, QSize, Signal
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QMessageBox, QWidget

from .input_dialog import InputDialog
from .LoginOverlayWidget_ui import Ui_LoginOverlayWidget


class LoginOverlayWidget(Ui_LoginOverlayWidget, QWidget):
    """Displayed during sign-in by overlaying the `login_widget` in `CentralWidget`."""

    login_successful_signal = Signal()

    def __init__(self, central_widget: Optional["CentralWidget"] = None):
        super().__init__(central_widget)
        self._central_widget = central_widget
        self.setupUi(self)
        self.continue_button.setHidden(True)
        self.status_image_label.setMaximumSize(QSize(30, 30))
        self.status_image_label.setScaledContents(True)
        
        module_dir_path = os.path.dirname(os.path.abspath(__file__))
        self._SUCCESS_IMAGE = QPixmap(os.path.join(module_dir_path, "status_success.png"))
        self._FAIL_IMAGE = QPixmap(os.path.join(module_dir_path, "status_fail.png"))
        self._LOADING_GIF = QMovie(os.path.join(module_dir_path, "loader.gif"), QByteArray(), self)

    def set_hidden(self, value: bool):
        if self._central_widget is not None:
            self._central_widget.set_login_overlay_widget_hidden(value)

    def set_status_loading(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setMovie(self._LOADING_GIF)
        self.continue_button.setHidden(True)
        self._LOADING_GIF.start()

    def set_status_success(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setPixmap(self._SUCCESS_IMAGE)
        try:
            self.continue_button.clicked.disconnect(self._continue_button_on_click_login_fail)
        except RuntimeError: 
            # Raised when there's no such slot connected. Only happens 
            # until the first time 'set_status_fail' is called.
            pass
        self.continue_button.clicked.connect(self._continue_button_on_click_login_success)
        self.continue_button.setHidden(False)

    def set_status_fail(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setPixmap(self._FAIL_IMAGE)
        try:
            self.continue_button.clicked.disconnect(self._continue_button_on_click_login_success)
        except RuntimeError:
            # Raised when there's no such slot connected. Only happens 
            # until the first time 'set_status_success' is called.
            pass
        self.continue_button.clicked.connect(self._continue_button_on_click_login_fail)
        self.continue_button.setHidden(False)

    def _continue_button_on_click_login_success(self):
        self.set_hidden(True)
        self.login_successful_signal.emit()

    def _continue_button_on_click_login_fail(self):
        self.set_hidden(True)
    
    async def open_error_message_box(self, text: str):
        QMessageBox(QMessageBox.Critical, "Error", text, parent=self).show()

    async def open_login_code_input_dialog(self):
        future = asyncio.Future()
        self.login_code_dialog = InputDialog(self)
        self.login_code_dialog.setWindowTitle("Login Code")
        self.login_code_dialog.label.setText(
            "A login code has been sent to you by Telegram via the app. "
            "Please enter the code below:"
        )
        self.login_code_dialog.buttonBox.accepted.connect(
            lambda: future.set_result(self.login_code_dialog.lineEdit.text())
        )
        self.login_code_dialog.buttonBox.rejected.connect(lambda: future.set_result(None))
        self.login_code_dialog.show()
        await future
        return future.result()

    async def open_password_input_dialog(self):
        future = asyncio.Future()
        self.two_step_dialog = InputDialog(self)
        self.two_step_dialog.setWindowTitle("2FA Password")
        self.two_step_dialog.label.setText(
            "Two-step verification is enabled on this account. "
            "Please enter the password below:"
        )
        self.two_step_dialog.buttonBox.accepted.connect(
            lambda: future.set_result(self.two_step_dialog.lineEdit.text())
        )
        self.two_step_dialog.buttonBox.rejected.connect(lambda: future.set_result(None))
        self.two_step_dialog.show()
        await future
        return future.result()


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    mw = QMainWindow()
    cw = LoginOverlayWidget(mw)
    cw.set_status_loading("Loading ... ")
    mw.setCentralWidget(cw)
    mw.show()
    app.exec()
