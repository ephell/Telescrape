if __name__ == "__main__":
    import os
    __package__ = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace(os.path.sep, ".")

import asyncio
from typing import TYPE_CHECKING, Awaitable, List

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.scrape_widget.scroll_area_widget.scroll_area_widget import ScrollAreaWidget

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget

from .progress_widget import ProgressWidget
from .ProgressContainerWidget_ui import Ui_ProgressContainerWidget


class ProgressContainerWidget(Ui_ProgressContainerWidget, QWidget):

    finished_all_scraping_tasks_signal = Signal()

    def __init__(self, scroll_area_widget: "ScrollAreaWidget"):
        super().__init__(scroll_area_widget)
        self.setupUi(self)
        self._scroll_area_widget = scroll_area_widget
        # General.
        self._all_scraping_tasks: List[Awaitable] = []
        self._total_completed_scraping_tasks = 0
        self._total_successful_scraping_tasks = 0
        self._total_failed_scraping_tasks = 0

    async def on_scrape_button_clicked(self) -> None:
        self._scroll_area_widget.show_progress_widget()
        self.delete_all_widgets_from_container_frame_layout()
        self._total_completed_scraping_tasks = 0
        self._total_successful_scraping_tasks = 0
        self._total_failed_scraping_tasks = 0

        self._all_scraping_tasks = []
        for selection in self._scroll_area_widget.get_all_selection_widgets():
            if not selection.check_box.isChecked():
                continue

            progress_widget = ProgressWidget(selection.check_box.text())
            progress_widget.finished_signal.connect(self._on_progress_widget_finished_signal)
            progress_widget.set_status_loading("In progress ... ")
            self.progress_widget_container_frame.layout().addWidget(progress_widget)
            scraping_settings = self._scroll_area_widget.get_scrape_settings()
            self._all_scraping_tasks.append(
                self._scroll_area_widget.get_scraper().scrape_entity(
                    entity=selection.entity,
                    progress_widget=progress_widget,
                    exclude_yourself=scraping_settings["exclude_yourself"],
                    exclude_admins=scraping_settings["exclude_admins"],
                    exclude_bots=scraping_settings["exclude_bots"],
                    exclude_deleted_users=scraping_settings["exclude_deleted_users"],
                    exclude_restricted_users=scraping_settings["exclude_restricted_users"],
                    exclude_scam_flagged_users=scraping_settings["exclude_scam_flagged_users"],
                    exclude_fake_flagged_users=scraping_settings["exclude_fake_flagged_users"],
                    exclude_users_in_contacts=scraping_settings["exclude_users_in_contacts"],
                    exclude_users_with_hidden_last_seen_online=scraping_settings[
                        "exclude_users_with_hidden_last_seen_online"
                    ],
                    user_active_in_last_days=scraping_settings["user_active_in_last_days"]
                )
            )

        self._update_counter_label()
        await asyncio.gather(*self._all_scraping_tasks)
        self.finished_all_scraping_tasks_signal.emit()

    def delete_all_widgets_from_container_frame_layout(self) -> None:
        while self.progress_widget_container_frame.layout().count():
            child = self.progress_widget_container_frame.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        # Shrink (redo) the layout after widgets have been deleted.
        self.progress_widget_container_frame.layout().invalidate()
        self.progress_widget_container_frame.layout().activate()

    @Slot()
    def _on_progress_widget_finished_signal(self, is_success: bool) -> None:
        self._total_completed_scraping_tasks += 1
        if is_success:
            self._total_successful_scraping_tasks += 1
        else:
            self._total_failed_scraping_tasks += 1
        self._update_counter_label()

    def _update_counter_label(self):
        self.counter_label.setText(
            f"Completed: {self._total_completed_scraping_tasks}/{len(self._all_scraping_tasks)} | "
            f"Successful: {self._total_successful_scraping_tasks} | "
            f"Failed: {self._total_failed_scraping_tasks}"
        )


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
    
    pcw = ProgressContainerWidget(None)
    for i in range(15):
        pw = ProgressWidget(f"Test Progress Widget -  {i}")
        pw.set_status_loading("In progress ... ")
        pcw.progress_widget_container_frame.layout().addWidget(pw)
    pcw.show()

    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())
