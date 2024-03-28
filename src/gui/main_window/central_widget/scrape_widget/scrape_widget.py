import asyncio
import os
import platform
import subprocess
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.client import Client
    from src.gui.main_window.central_widget import CentralWidget

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from src.gui.main_window.central_widget.scrape_widget.scrape_settings_widget import ScrapeSettingsWidget
from src.gui.main_window.central_widget.scrape_widget.ScrapeWidget_ui import Ui_ScrapeWidget
from src.scraper import Scraper


class ScrapeWidget(Ui_ScrapeWidget, QWidget):

    logout_signal = Signal()

    def __init__(self, central_widget: Optional["CentralWidget"] = None):
        super().__init__(central_widget)
        self._central_widget = central_widget
        self.setupUi(self)
        self.scroll_area_widget.set_scrape_widget(self)
        self._scrape_settings_widget = ScrapeSettingsWidget(self)
        # General.
        self._scraper: Scraper = None
        # Signals and slots.
        self.logout_button.clicked.connect(self.logout_signal.emit)
        self.get_groups_button.clicked.connect(self.scroll_area_widget.on_get_groups_button_clicked)
        self.scrape_button.clicked.connect(self.scroll_area_widget.on_scrape_button_clicked)
        self.select_all_button.clicked.connect(self.scroll_area_widget.on_select_all_button_clicked)
        self.unselect_all_button.clicked.connect(self.scroll_area_widget.on_unselect_all_button_clicked)
        self.open_data_dir_button.clicked.connect(self._on_open_data_dir_button_clicked)
        self.open_scrape_settings_button.clicked.connect(self._on_open_scrape_settings_button_clicked)
        self.logout_signal.connect(self.scroll_area_widget.on_logout_signal)

    def set_hidden(self, value: bool):
        if self._central_widget is not None:
            self._central_widget.set_scrape_widget_hidden(value)
        else:
            self.setHidden(value)

    def get_scrape_settings_widget(self) -> ScrapeSettingsWidget:
        return self._scrape_settings_widget

    """Slot"""
    def on_client_login_finished_signal(self, client: Optional["Client"]):
        if client is not None:
            self.scrape_button.setEnabled(False)
            self.select_all_button.setEnabled(False)
            self.unselect_all_button.setEnabled(False)
            self.scroll_area_widget.set_scraper(Scraper(client))
            self.scroll_area_widget.show_selection_widget()

    @Slot()    
    def _on_open_data_dir_button_clicked(self):
        data_dir_path = self._scrape_settings_widget.get_current_settings()["data_dir_path"]
        print(data_dir_path)
        system = platform.system()
        if system == "Windows":
            os.startfile(data_dir_path)
        elif system == "Darwin":
            subprocess.Popen(["open", data_dir_path])
        else:
            subprocess.Popen(["xdg-open", data_dir_path])

    @Slot()
    def _on_open_scrape_settings_button_clicked(self):
        self._scrape_settings_widget.show()


if __name__ == "__main__":
    import asyncio
    import sys

    from PySide6.QtWidgets import QApplication
    from qasync import QEventLoop

    app = QApplication(sys.argv)
    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    sw = ScrapeWidget()
    sw.show()

    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())
