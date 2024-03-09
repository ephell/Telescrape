import asyncio

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox, QPushButton
from qasync import asyncSlot

from client import Client
from src.gui.main_window.dialog_code_request.dialog_code_request import CodeRequestDialog


class LoginButton(QPushButton):

    logged_in_successfully = Signal(Client)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicked.connect(self.on_clicked)

    @asyncSlot()
    async def on_clicked(self):
        login_info = self._get_login_info()
        if login_info is None:
            return

        self.client = Client(*login_info, self.open_code_input_dialog_and_get_input) 
        await self.client.login()

    async def open_code_input_dialog_and_get_input(self):
        future = asyncio.Future()
        self.dialog = CodeRequestDialog()
        self.dialog.buttonBox.accepted.connect(lambda: future.set_result(self.dialog.lineEdit.text()))
        self.dialog.buttonBox.rejected.connect(lambda: future.set_result(None))
        self.dialog.show()
        await future
        return future.result()

    def _get_login_info(self):
        mw = self.window()
        phone_number = mw.line_edit_phone_number.text()
        try:
            phone_number = int(phone_number)
        except ValueError:
            message_box = QMessageBox()
            message_box.setWindowTitle("Invalid Phone Number Format")
            message_box.setText("Phone number field must contain digits only.")
            message_box.setIcon(QMessageBox.Icon.Critical)
            message_box.exec()
            return None
        else:
            return (
                mw.line_edit_username.text(),
                phone_number,
                mw.line_edit_api_id.text(),
                mw.line_edit_api_hash.text()
            )
