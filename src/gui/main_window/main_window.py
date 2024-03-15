from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from qasync import asyncClose

from src.gui.main_window.MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app
        self.client = None
        self.setupUi(self)
        self.setWindowTitle("Telescrape")
        self.setFocus()
        self.setFocusPolicy(Qt.ClickFocus) # Make all widgets lose focus when clicking on the main window.
        self.setWindowFlags(Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint) # Set non resizable.
        self.login_button.client_login_finished.connect(self._on_client_login_finished)
        self.login_button.client_login_finished.connect(self.logout_button.on_client_login_finished)


    @asyncClose
    async def closeEvent(self, event):
        super().closeEvent(event)
        for window in QApplication.topLevelWidgets():
            window.close()
        if self.client is not None:
            await self.client.logout()

    def _on_client_login_finished(self, client):
        self.client = client
