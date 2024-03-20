from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.base_widget.base_widget import BaseWidget
    from src.gui.main_window.central_widget.overlay_widget.overlay_widget import OverlayWidget
    from src.gui.main_window.central_widget.scrape_widget.scrape_widget import ScrapeWidget

from PySide6.QtCore import Qt, Slot
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
        self.base_widget = self.get_base_widget()
        self.overlay_widget = self.get_overlay_widget()
        self.scrape_widget = self.get_scrape_widget()

        self.base_widget.login_button.client_login_finished_signal.connect(
            self._on_client_login_finished_signal
        )
        self.overlay_widget.login_successful_signal.connect(self._on_login_successful_signal)


    def get_base_widget(self) -> "BaseWidget":
        return self.central_widget.base_widget

    def get_overlay_widget(self) -> "OverlayWidget":
        return self.central_widget.overlay_widget

    def get_scrape_widget(self) -> "ScrapeWidget":
        return self.central_widget.scrape_widget

    @asyncClose
    async def closeEvent(self, event):
        super().closeEvent(event)
        for window in QApplication.topLevelWidgets():
            window.close()
        if self.client is not None:
            await self.client.logout()

    @Slot()
    def _on_client_login_finished_signal(self, client):
        self.client = client

    @Slot()
    def _on_login_successful_signal(self):
        self.base_widget.set_hidden(True)
        self.overlay_widget.set_hidden(True)
        self.scrape_widget.set_hidden(False)
        self.resize(self.central_widget.get_scrape_widget_container_size())
