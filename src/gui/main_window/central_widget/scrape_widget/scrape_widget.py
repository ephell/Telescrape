import os
from typing import TYPE_CHECKING, Dict, Optional, Union

if TYPE_CHECKING:
    from telethon.tl.types import Channel, Chat

    from src.client import Client
    from src.gui.main_window.central_widget.central_widget import CentralWidget
    Entity = Union[Channel, Chat]

from PySide6.QtCore import QByteArray, QSize, Qt, Signal, Slot
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QCheckBox, QLabel, QLayout, QWidget
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
        self._all_check_boxes: Dict[QCheckBox, Entity] = {}
        self._scraper: Scraper = None
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
        self.logout_button.clicked.connect(self.logout_signal.emit)
        self.get_groups_button.clicked.connect(self._on_get_groups_button_clicked)
        self.scrape_button.clicked.connect(self._on_scrape_button_clicked)
        self.select_all_button.clicked.connect(self._on_select_all_button_clicked)
        self.unselect_all_button.clicked.connect(self._on_unselect_all_button_clicked)

    def set_hidden(self, value: bool):
        if self.central_widget is not None:
            self.central_widget.set_scrape_widget_hidden(value)
        else:
            self.setHidden(value)

    def _start_loading_gif(self):
        self.scroll_area_layout.setSizeConstraint(QLayout.SetMaximumSize)
        self.scroll_area_layout.addWidget(self._loading_gif_container_label, 0, Qt.AlignCenter)
        self._loading_gif_container_label.setHidden(False)
        self._loading_gif.start()

    def _stop_loading_gif(self):
        self.scroll_area_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.scroll_area_layout.removeWidget(self._loading_gif_container_label)
        self._loading_gif_container_label.setHidden(True)
        self._loading_gif.stop()

    def _clear_scroll_area(self, layout: QLayout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        # Shrink (redo) the layout after widgets have been deleted.
        self.scroll_area_layout.invalidate()
        self.scroll_area_layout.activate()

    def _add_check_box(self, entity: Union["Entity", str] = "Test"): # 'str' is for testing.
        check_box = QCheckBox(self)
        if isinstance(entity, str):
            check_box.setText(entity)
        else:
            check_box.setText(entity.title)
        self._all_check_boxes.update({check_box: entity})
        check_box.stateChanged.connect(self._on_checkbox_stateChanged)
        self.scroll_area_layout.addWidget(check_box)
        self._update_check_boxes_checked_label()

    def _update_check_boxes_checked_label(self):
        self.check_boxes_checked_label.setText(
            f"({self.checked_check_boxes_counter}/{len(self._all_check_boxes)}) Selected."
        )

    @Slot()
    def _on_checkbox_stateChanged(self, check_state):
        if check_state == 2: # Checked
            self.checked_check_boxes_counter += 1
        elif check_state == 0: # Unchecked
            self.checked_check_boxes_counter -= 1
        self._update_check_boxes_checked_label()

    # Space in between 'o' and 'n' to prevent 'QMetaObject::connectSlotsByName: No matching signal'.
    @Slot()
    def o_n_client_login_finished_signal(self, client: Optional["Client"]):
        if client is not None:
            self._scraper = Scraper(client)

    @asyncSlot()
    async def _on_get_groups_button_clicked(self):
        self._clear_scroll_area(self.scroll_area_layout)
        self._all_check_boxes = {}
        self._start_loading_gif()
        if self._scraper is not None:
            for entity in await self._scraper.get_scrapable_entities():
                self._add_check_box(entity)
        self._update_check_boxes_checked_label()
        self._stop_loading_gif()

    @asyncSlot()
    async def _on_scrape_button_clicked(self):
        for check_box, entity in self._all_check_boxes.items():
            if check_box.isChecked():
                if isinstance(entity, str):
                    # Happens only when adding check boxes manually via _add_check_box()
                    # while developing.
                    print(f"No 'entity' set for '{check_box.text()}'. Skipping ... ")
                else:
                    await self._scraper.scrape_entity(entity)

    @Slot()
    def _on_select_all_button_clicked(self):
        for check_box, _ in self._all_check_boxes.items():
            check_box.setChecked(True)

    @Slot()
    def _on_unselect_all_button_clicked(self):
        for check_box, _ in self._all_check_boxes.items():
            check_box.setChecked(False)


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
    for i in range(10):
        sw._add_check_box(f"Checkbox {i}")
    sw._stop_loading_gif()
    sw.show()

    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())
