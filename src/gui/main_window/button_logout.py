from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton


class LogoutButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.client = None
        # self.clicked.connect(self.on_clicked)

    @Slot()
    def on_logged_in_successfully(self, client):
        print("\nza")
        self.client = client

    # @Slot()
    # def on_clicked(self):
        
    