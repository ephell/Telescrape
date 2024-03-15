from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QMessageBox
from qasync import asyncSlot


class LogoutButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.client = None
        self.clicked.connect(self._on_clicked)

    @asyncSlot()
    async def _on_clicked(self):
        if self.client is not None:
            await self.client.logout()
            QMessageBox(
                QMessageBox.Information, 
                "Information", 
                "Logged out successfully!", 
                parent=self
            ).show()
            self.client = None
        else:
            QMessageBox(
                QMessageBox.Information, 
                "Information", 
                "Not logged in.", 
                parent=self
            ).show()

    @Slot()
    def on_client_login_finished(self, client):
        self.client = client
    