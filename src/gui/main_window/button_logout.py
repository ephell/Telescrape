from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QMessageBox, QPushButton
from qasync import asyncSlot


class LogoutButton(QPushButton):

    client_logout_finished_signal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.client = None
        self.clicked.connect(self._on_clicked)
        self.setEnabled(False)

    @Slot()
    def on_client_login_finished_signal(self, client):
        self.client = client
        if self.client is not None:
            self.setEnabled(True)

    @asyncSlot()
    async def _on_clicked(self):
        if self.client is not None:
            await self.client.logout()
            self.msg_box = QMessageBox(
                QMessageBox.Information, 
                "Information", 
                "Logged out successfully!", 
                parent=self
            ).exec()
            self.client = None
            self.setEnabled(False)
            self.client_logout_finished_signal.emit()
