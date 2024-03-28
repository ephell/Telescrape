from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.login_widget import LoginWidget

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
        self.client_login_finished_signal.emit(login_result)

    def _get_login_info(self):
        login_widget: "LoginWidget" = self.window().get_login_widget()
        login_details = login_widget.get_current_login_details()
        phone_number = login_details["phone_number"].replace(" ", "")
        try:
            phone_number = int(phone_number)
        except ValueError:
            QMessageBox(
                QMessageBox.Icon.Critical,
                "Invalid Phone Number Format",
                "Phone number field must contain digits only.",
            ).exec()
            return None
        else:
            return (
                login_details["username"],
                phone_number,
                login_details["api_id"],
                login_details["api_hash"]
            )
