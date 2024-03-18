from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from qasync import asyncClose

from src.gui.main_window.central_widget.central_widget import CentralWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.client = None
        self.setWindowTitle("Telescrape")
        self.setFocus()
        self.setFocusPolicy(Qt.ClickFocus) # Make all widgets lose focus when clicking on the main window.
        self.setWindowFlags(Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint) # Set non resizable.
        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)

        # self.login_button.client_login_finished_signal.connect(self._on_client_login_finished_signal)
        # self.login_button.client_login_finished_signal.connect(self.logout_button.on_client_login_finished_signal)
        # self.logout_button.client_logout_finished_signal.connect(self.login_button.on_client_logout_finished_signal)

        self.central_widget.base_widget.line_edit_username.setText("Raska Goo")
        self.central_widget.base_widget.line_edit_phone_number.setText("37060751782")
        self.central_widget.base_widget.line_edit_api_id.setText("14112344")
        self.central_widget.base_widget.line_edit_api_hash.setText("90d2a30e6a391fee8c99f38476d4bf46")

        # self.line_edit_username.setText("Saulius One")
        # self.line_edit_phone_number.setText("37067210952")
        # self.line_edit_api_id.setText("21366188")
        # self.line_edit_api_hash.setText("b78754703b1780a3db1087c371ed3bc7")

    def get_base_widget(self):
        return self.central_widget.base_widget

    def get_overlay_widget(self):
        return self.central_widget.overlay_widget

    @asyncClose
    async def closeEvent(self, event):
        super().closeEvent(event)
        for window in QApplication.topLevelWidgets():
            window.close()
        if self.client is not None:
            await self.client.logout()

    def _on_client_login_finished_signal(self, client):
        self.client = client
