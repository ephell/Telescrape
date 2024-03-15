from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox, QPushButton
from qasync import asyncSlot

from client import Client
from src.gui.login_widget.login_widget import LoginWidget


class LoginButton(QPushButton):

    client_login_finished = Signal(Client)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicked.connect(self._on_clicked)

    @asyncSlot()
    async def _on_clicked(self):
        login_info = self._get_login_info()
        if login_info is None:
            return

        self.login_widget = LoginWidget()
        self.client = Client(*login_info, self.login_widget) 
        self.client_login_finished.emit(await self.client.login())

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
