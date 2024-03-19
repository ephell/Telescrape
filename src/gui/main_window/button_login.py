from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMessageBox, QPushButton
from qasync import asyncSlot

from src.client import Client


class LoginButton(QPushButton):

    client_login_finished_signal = Signal(Client)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicked.connect(self._on_clicked)

    @asyncSlot()
    async def _on_clicked(self):
        login_info = self._get_login_info()
        if login_info is None:
            return

        self.client = Client(*login_info, self.window()) 
        login_result = await self.client.login()
        if login_result is not None:
            self.setEnabled(False)
        self.client_login_finished_signal.emit(login_result)

    def _get_login_info(self):
        bw = self.window().get_base_widget()
        phone_number = bw.line_edit_phone_number.text()
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
                bw.line_edit_username.text(),
                phone_number,
                bw.line_edit_api_id.text(),
                bw.line_edit_api_hash.text()
            )
