from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.base_widget.base_widget import BaseWidget
    from src.gui.main_window.central_widget.overlay_widget.overlay_widget import OverlayWidget
    from src.gui.main_window.central_widget.scrape_widget.scrape_widget import ScrapeWidget
    from src.client import Client

from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from qasync import asyncClose, asyncSlot

from src.gui.main_window.central_widget.central_widget import CentralWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Telescrape")
        self.setFocus()
        self.setFocusPolicy(Qt.ClickFocus) # Make all widgets lose focus when clicking on the main window.
        self.setWindowFlags(Qt.Dialog)
        self._central_widget = CentralWidget(self)
        self._central_widget_initial_size = self._central_widget.size()
        self.setCentralWidget(self._central_widget)
        self._set_resizable(False)
        self._client: "Client" = None
        self._base_widget = self.get_base_widget()
        self._overlay_widget = self.get_overlay_widget()
        self._scrape_widget = self.get_scrape_widget()
        # Signals and slots.
        self._base_widget.login_button.client_login_finished_signal.connect(self._on_client_login_finished_signal)
        self._base_widget.login_button.client_login_finished_signal.connect(
            self._scrape_widget.o_n_client_login_finished_signal
        )
        self._overlay_widget.login_successful_signal.connect(self._on_login_successful_signal)
        self._scrape_widget.logout_signal.connect(self._on_logout_signal)


    def get_base_widget(self) -> "BaseWidget":
        return self._central_widget.base_widget

    def get_overlay_widget(self) -> "OverlayWidget":
        return self._central_widget.overlay_widget

    def get_scrape_widget(self) -> "ScrapeWidget":
        return self._central_widget.scrape_widget

    @asyncClose
    async def closeEvent(self, event):
        super().closeEvent(event)
        for window in QApplication.topLevelWidgets():
            window.close()
        if self._client is not None:
            await self._client.logout()

    def _set_resizable(self, value: bool):
        """MainWindow should only be resizable when ScrapeWidget is visible."""
        if value:
            size = self._central_widget.get_scrape_widget_container_original_size()
            self.setMinimumSize(size)
            self.setMaximumSize(QSize(size.width(), 16777215))
        else:
            self.setMinimumSize(self._central_widget_initial_size)
            self.setMaximumSize(self._central_widget_initial_size)

    @Slot()
    def _on_client_login_finished_signal(self, client: Optional["Client"]):
        self._client = client

    @Slot()
    def _on_login_successful_signal(self):
        self._base_widget.set_hidden(True)
        self._overlay_widget.set_hidden(True)
        self._scrape_widget.set_hidden(False)
        self._set_resizable(True)
        self.resize(self._central_widget.get_scrape_widget_container_original_size())

    @asyncSlot()
    async def _on_logout_signal(self):
        await self._client.logout()
        if not self._client.is_connected():
            print("Logged out successfully!")
        self._scrape_widget.set_hidden(True)
        self._base_widget.set_hidden(False)
        self.resize(self._central_widget.get_base_widget_container_original_size())
        self._set_resizable(False)
