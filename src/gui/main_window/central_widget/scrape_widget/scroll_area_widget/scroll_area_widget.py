if __name__ == "__main__":
    import os
    __package__ = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace(os.path.sep, ".")

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.scrape_widget.scrape_widget import ScrapeWidget
    from src.scraper import Scraper

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout, QWidget
from qasync import asyncSlot

from .progress_container_widget import ProgressContainerWidget
from .selection_container_widget import SelectionContainerWidget


class ScrollAreaWidget(QStackedWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._selection_container_widget = SelectionContainerWidget(self)
        self._progress_container_widget = ProgressContainerWidget(self)
        self.addWidget(self._selection_container_widget)
        self.addWidget(self._progress_container_widget)
        # General
        self._scraper: "Scraper" = None
        self._scrape_widget: "ScrapeWidget" = None
        # Signals and slots.
        self._selection_container_widget.finished_adding_check_boxes_signal.connect(
            self._on_finished_adding_check_boxes_signal
        )
        self._selection_container_widget.is_selection_made_signal.connect(
            self._on_is_selection_made_signal
        )
        self._progress_container_widget.finished_all_scraping_tasks_signal.connect(
            self._on_finished_all_scraping_tasks_signal
        )
    
    def set_scraper(self, scraper: "Scraper"):
        self._scraper = scraper

    def get_scraper(self) -> "Scraper":
        return self._scraper

    def set_scrape_widget(self, scrape_widget: "ScrapeWidget"):
        self._scrape_widget = scrape_widget

    def get_scrape_settings(self):
        return self._scrape_widget.get_scrape_settings_widget().get_settings()

    def get_all_selection_widgets(self):
        return self._selection_container_widget.get_all_selection_widgets()

    def show_selection_widget(self) -> None:
        self.setCurrentWidget(self._selection_container_widget)

    def show_progress_widget(self) -> None:
        self.setCurrentWidget(self._progress_container_widget)

    @asyncSlot()
    async def on_get_groups_button_clicked(self) -> None:
        self._scrape_widget.get_groups_button.setEnabled(False)
        self._scrape_widget.select_all_button.setEnabled(False)
        self._scrape_widget.unselect_all_button.setEnabled(False)
        self._scrape_widget.scrape_button.setEnabled(False)
        self._scrape_widget.logout_button.setEnabled(False)
        await self._selection_container_widget.on_get_groups_button_clicked()
        self._scrape_widget.get_groups_button.setEnabled(True)
        self._scrape_widget.select_all_button.setEnabled(True)
        self._scrape_widget.unselect_all_button.setEnabled(True)
        self._scrape_widget.logout_button.setEnabled(True)

    @asyncSlot()
    async def on_scrape_button_clicked(self) -> None:
        self._scrape_widget.get_groups_button.setEnabled(False)
        self._scrape_widget.select_all_button.setEnabled(False)
        self._scrape_widget.unselect_all_button.setEnabled(False)
        self._scrape_widget.scrape_button.setEnabled(False)
        self._scrape_widget.logout_button.setEnabled(False)
        await self._progress_container_widget.on_scrape_button_clicked()

    @Slot()
    def on_select_all_button_clicked(self):
        for selection in self._selection_container_widget.get_all_selection_widgets():
            selection.check_box.setChecked(True)

    @Slot()
    def on_unselect_all_button_clicked(self):
        for selection in self._selection_container_widget.get_all_selection_widgets():
            selection.check_box.setChecked(False)

    @Slot()
    def on_logout_signal(self):
        self._scrape_widget.scrape_button.setEnabled(False)
        self._scrape_widget.select_all_button.setEnabled(False)
        self._scrape_widget.unselect_all_button.setEnabled(False)
        self._selection_container_widget.delete_all_widgets_from_container_frame_layout()
        self._progress_container_widget.delete_all_widgets_from_container_frame_layout()

    @Slot()
    def _on_finished_adding_check_boxes_signal(self) -> None:
        self.setCurrentWidget(self._selection_container_widget)

    @Slot()
    def _on_finished_all_scraping_tasks_signal(self):
        self._scrape_widget.get_groups_button.setEnabled(True)
        self._scrape_widget.scrape_button.setEnabled(True)
        self._scrape_widget.logout_button.setEnabled(True)

    @Slot()
    def _on_is_selection_made_signal(self, is_made: bool):
        if is_made:
            self._scrape_widget.scrape_button.setEnabled(True)
        else:
            self._scrape_widget.scrape_button.setEnabled(False)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication, QPushButton

    app = QApplication(sys.argv)
    container = QWidget()
    container_layout = QVBoxLayout(container)

    saw = ScrollAreaWidget(None)
    saw._progress_container_widget.layout().addWidget(QPushButton("Dummy"))
    container_layout.addWidget(saw)

    def change_widget():
        current_index = saw.currentIndex()
        next_index = (current_index + 1) % saw.count()
        saw.setCurrentIndex(next_index)

    button = QPushButton("Change Widget")
    button.clicked.connect(change_widget)
    container_layout.addWidget(button)
    container.show()
    app.exec() 
