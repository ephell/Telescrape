import asyncio
import os
import platform
import subprocess
from typing import TYPE_CHECKING, Dict, Optional, Union

if TYPE_CHECKING:
    from telethon.tl.types import Channel, Chat

    from src.client import Client
    from src.gui.main_window.central_widget.central_widget import CentralWidget
    Entity = Union[Channel, Chat]

from PySide6.QtCore import QByteArray, QSize, Qt, Signal, Slot
from PySide6.QtGui import QFont, QMovie
from PySide6.QtWidgets import QCheckBox, QLabel, QLayout, QWidget
from qasync import asyncSlot

from src.gui.main_window.central_widget.scrape_widget.entity_status_widget.entity_status_widget import EntityStatusWidget
from src.gui.main_window.central_widget.scrape_widget.scrape_settings_widget.scrape_settings_widget import ScrapeSettingsWidget
from src.gui.main_window.central_widget.scrape_widget.ScrapeWidget_ui import Ui_ScrapeWidget
from src.scraper import Scraper


class ScrapeWidget(Ui_ScrapeWidget, QWidget):

    logout_signal = Signal()

    def __init__(self, central_widget: Optional["CentralWidget"] = None):
        super().__init__(central_widget)
        self._central_widget = central_widget
        self.setupUi(self)
        self.counter_label.setText(f"Selected: 0/0")
        self.scrape_button.setEnabled(False)
        self.select_all_button.setEnabled(False)
        self.unselect_all_button.setEnabled(False)
        self._scroll_area_layout = self.scroll_area_widget_contents.layout()
        self._scrape_settings_widget = ScrapeSettingsWidget(self)
        # setSizeContraint() to force items inside the scroll area to stack from top to bottom, equally.
        self._scroll_area_layout.setSizeConstraint(QLayout.SetFixedSize)
        self._scroll_area_layout.setSpacing(0)
        # General.
        self._total_checked_check_boxes = 0
        self._all_check_boxes: Dict[QCheckBox, Entity] = {}
        self._scraper: Scraper = None
        self._total_scraping_tasks = 0
        self._total_completed_scraping_tasks = 0
        self._total_successful_scraping_tasks = 0
        self._total_failed_scraping_tasks = 0
        # Loading gif.
        self._loading_gif = QMovie(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "loading.gif"), 
            QByteArray(), 
            self
        )
        self._loading_gif_container_label = QLabel(self)
        self._loading_gif_container_label.setMovie(self._loading_gif)
        self._loading_gif_container_label.setMaximumSize(QSize(40, 40))
        self._loading_gif_container_label.setScaledContents(True)
        # Signals and slots.
        self.logout_button.clicked.connect(self._on_logout_button_clicked)
        self.get_groups_button.clicked.connect(self._on_get_groups_button_clicked)
        self.scrape_button.clicked.connect(self._on_scrape_button_clicked)
        self.select_all_button.clicked.connect(self._on_select_all_button_clicked)
        self.unselect_all_button.clicked.connect(self._on_unselect_all_button_clicked)
        self.open_data_dir_button.clicked.connect(self._on_open_data_dir_button_clicked)
        self.open_scrape_settings_button.clicked.connect(self._on_open_scrape_settings_button_clicked)

    def set_hidden(self, value: bool):
        if self._central_widget is not None:
            self._central_widget.set_scrape_widget_hidden(value)
        else:
            self.setHidden(value)

    def _start_loading_gif(self):
        self._scroll_area_layout.setSizeConstraint(QLayout.SetMaximumSize)
        self._scroll_area_layout.addWidget(self._loading_gif_container_label, 0, Qt.AlignCenter)
        self._loading_gif_container_label.setHidden(False)
        self._loading_gif.start()

    def _stop_loading_gif(self):
        self._scroll_area_layout.setSizeConstraint(QLayout.SetFixedSize)
        self._scroll_area_layout.removeWidget(self._loading_gif_container_label)
        self._loading_gif_container_label.setHidden(True)
        self._loading_gif.stop()

    def _remove_all_widgets_from_scroll_area(self):
        while self._scroll_area_layout.count():
            child = self._scroll_area_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        # Shrink (redo) the layout after widgets have been deleted.
        self._scroll_area_layout.invalidate()
        self._scroll_area_layout.activate()

    def _add_check_box(self, entity: Union["Entity", str] = "Test"): # 'str' is for testing.
        check_box = QCheckBox(self)
        font = QFont()
        font.setPointSize(10)
        check_box.setFont(font)
        if isinstance(entity, str):
            check_box.setText(entity)
        else:
            check_box.setText(entity.title)
        self._all_check_boxes.update({check_box: entity})
        check_box.stateChanged.connect(self._on_checkbox_stateChanged)
        self._scroll_area_layout.addWidget(check_box)
        self._update_counter_label("checked_check_boxes")

    def _update_counter_label(self, format: str):
        if format == "checked_check_boxes":
            self.counter_label.setText(
                f"Selected: {self._total_checked_check_boxes}/{len(self._all_check_boxes)}"
            )
        elif format == "scraping_tasks":
            self.counter_label.setText(
                f"Completed: {self._total_completed_scraping_tasks}/{self._total_scraping_tasks} | "
                f"Successful: {self._total_successful_scraping_tasks} | "
                f"Failed: {self._total_failed_scraping_tasks}"
            )

    # Space in between 'o' and 'n' to prevent 'QMetaObject::connectSlotsByName: No matching signal'.
    @Slot()
    def o_n_client_login_finished_signal(self, client: Optional["Client"]):
        if client is not None:
            self._scraper = Scraper(client)

    @Slot()
    def _on_checkbox_stateChanged(self, check_state):
        if check_state == 2: # Checked
            self._total_checked_check_boxes += 1
        elif check_state == 0: # Unchecked
            self._total_checked_check_boxes -= 1
        self._update_counter_label("checked_check_boxes")

        if self._total_checked_check_boxes > 0:
            self.scrape_button.setEnabled(True)
        else:
            self.scrape_button.setEnabled(False)

    @Slot()
    def _on_logout_button_clicked(self):
        self.scrape_button.setEnabled(False)
        self.select_all_button.setEnabled(False)
        self.unselect_all_button.setEnabled(False)
        self._remove_all_widgets_from_scroll_area()
        self._total_checked_check_boxes = 0
        self._all_check_boxes = {}
        self._update_counter_label("checked_check_boxes")
        self.logout_signal.emit()
        
    @asyncSlot()
    async def _on_get_groups_button_clicked(self):
        self.get_groups_button.setEnabled(False)
        self.select_all_button.setEnabled(False)
        self.unselect_all_button.setEnabled(False)
        self.scrape_button.setEnabled(False)
        self.logout_button.setEnabled(False)

        self._remove_all_widgets_from_scroll_area()
        self._total_checked_check_boxes = 0
        self._all_check_boxes = {}
        self._update_counter_label("checked_check_boxes") # Reset to default.
        self._start_loading_gif()
        if self._scraper is not None:
            for entity in await self._scraper.get_scrapable_entities():
                self._add_check_box(entity)
        self._update_counter_label("checked_check_boxes")
        self._stop_loading_gif()

        self.get_groups_button.setEnabled(True)
        self.select_all_button.setEnabled(True)
        self.unselect_all_button.setEnabled(True)
        self.logout_button.setEnabled(True)

    @asyncSlot()
    async def _on_scrape_button_clicked(self):
        self.get_groups_button.setEnabled(False)
        self.select_all_button.setEnabled(False)
        self.unselect_all_button.setEnabled(False)
        self.scrape_button.setEnabled(False)
        self.logout_button.setEnabled(False)
        self.open_scrape_settings_button.setEnabled(False)
        self._remove_all_widgets_from_scroll_area()
        self._total_completed_scraping_tasks = 0
        self._total_successful_scraping_tasks = 0
        self._total_failed_scraping_tasks = 0

        tasks = []
        for check_box, entity in self._all_check_boxes.items():
            if check_box.isChecked():
                if isinstance(entity, str):
                    # Happens only when adding check boxes manually via _add_check_box()
                    # while developing.
                    print(f"No 'entity' set for '{check_box.text()}'. Skipping ... ")
                else:
                    esw = EntityStatusWidget(entity.title)
                    esw.finished_signal.connect(self._on_entity_status_widget_finished_signal)
                    esw.set_status_loading("In progress ... ")
                    self._scroll_area_layout.addWidget(esw)
                    scraping_settings = self._scrape_settings_widget.get_settings()
                    tasks.append(
                        self._scraper.scrape_entity(
                            entity, 
                            esw,
                            user_active_in_last_days=scraping_settings["user_active_in_last_days"],
                            exclude_admins=scraping_settings["exclude_admins"],
                            exclude_bots=scraping_settings["exclude_bots"],
                            exclude_deleted_users=scraping_settings["exclude_deleted_users"],
                            exclude_restricted_users=scraping_settings["exclude_restricted_users"],
                            exclude_scam_flagged_users=scraping_settings["exclude_scam_flagged_users"],
                            exclude_fake_flagged_users=scraping_settings["exclude_fake_flagged_users"]
                        )
                    )

        self._total_scraping_tasks = len(tasks)
        self._update_counter_label("scraping_tasks")
        await asyncio.gather(*tasks)
        self.get_groups_button.setEnabled(True)
        self.logout_button.setEnabled(True)
        self.open_scrape_settings_button.setEnabled(True)

    @Slot()
    def _on_entity_status_widget_finished_signal(self, is_success):
        self._total_completed_scraping_tasks += 1
        if is_success:
            self._total_successful_scraping_tasks += 1
        else:
            self._total_failed_scraping_tasks += 1
        self._update_counter_label("scraping_tasks")

    @Slot()
    def _on_select_all_button_clicked(self):
        for check_box, _ in self._all_check_boxes.items():
            check_box.setChecked(True)

    @Slot()
    def _on_unselect_all_button_clicked(self):
        for check_box, _ in self._all_check_boxes.items():
            check_box.setChecked(False)

    @Slot()    
    def _on_open_data_dir_button_clicked(self):
        if self._scraper is not None:
            system = platform.system()
            if system == "Windows":
                os.startfile(self._scraper.scraped_data_dir_path)
            elif system == "Darwin":
                subprocess.Popen(["open", self._scraper.scraped_data_dir_path])
            else:
                subprocess.Popen(["xdg-open", self._scraper.scraped_data_dir_path])

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
    sw._start_loading_gif()
    # for i in range(10):
    #     sw._add_check_box(f"Checkbox {i}")
    for i in range(10):
        esw = EntityStatusWidget("Test EntityStatusWidgetTest EntityStatusWidgeTest EntityStatusWidgeTest EntityStatusWidgettt")
        esw.set_status_loading("Scraping ... ")
        esw.set_status_loading("Finished scraping. Total users scraped: 100000.")
        sw._scroll_area_layout.addWidget(esw)
    sw._stop_loading_gif()
    sw.show()

    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())
