from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.central_widget import CentralWidget
    from src.client import Client

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QCheckBox, QLayout, QWidget
from qasync import asyncSlot

from src.gui.main_window.central_widget.scrape_widget.ScrapeWidget_ui import Ui_ScrapeWidget
from src.scraper import Scraper


class ScrapeWidget(Ui_ScrapeWidget, QWidget):

    logout_signal = Signal()

    def __init__(self, central_widget: Optional["CentralWidget"] = None):
        super().__init__(central_widget)
        self.central_widget = central_widget
        self.setupUi(self)
        self.scroll_area_layout = self.scroll_area_widget_contents.layout()
        # Force items inside the scroll area to stack from top to bottom, equally.
        self.scroll_area_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.checked_check_boxes_counter = 0
        self.all_check_boxes = []
        self._scraper: Scraper = None
        # Signals and slots.
        self.logout_button.clicked.connect(self.logout_signal.emit)
        self.get_groups_button.clicked.connect(self._on_get_groups_button_clicked)

    def set_hidden(self, value: bool):
        if self.central_widget is not None:
            self.central_widget.set_scrape_widget_hidden(value)
        else:
            self.setHidden(value)

    def _add_check_box(self, text: str = "Test") -> QCheckBox:
        check_box = QCheckBox(self)
        check_box.setText(text)
        check_box.stateChanged.connect(self._on_checkbox_stateChanged)
        self.all_check_boxes.append(check_box)
        self.scroll_area_layout.addWidget(check_box)
        return check_box

    @Slot()
    def _on_checkbox_stateChanged(self, check_state):
        if check_state == 2: # Checked
            self.checked_check_boxes_counter += 1
        elif check_state == 0: # Unchecked
            self.checked_check_boxes_counter -= 1
        self.check_boxes_checked_label.setText(
            f"({self.checked_check_boxes_counter}/{len(self.all_check_boxes)}) Selected."
        )

    # Space in between 'o' and 'n' to prevent 'QMetaObject::connectSlotsByName: No matching signal'.
    @Slot()
    def o_n_client_login_finished_signal(self, client: Optional["Client"]):
        if client is not None:
            self._scraper = Scraper(client)

    @asyncSlot()
    async def _on_get_groups_button_clicked(self):
        for i, entity in enumerate(await self._scraper.get_scrapable_entities()):
            self._add_check_box(f"[{i}] {entity.title}")


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    sw = ScrapeWidget()

    for i in range(5):
        sw._add_check_box(f"Checkbox {i}")

    sw.show()
    app.exec()
