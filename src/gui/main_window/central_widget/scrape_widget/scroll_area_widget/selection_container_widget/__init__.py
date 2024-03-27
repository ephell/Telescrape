import os

if __name__ == "__main__":
    __package__ = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace(os.path.sep, ".")

from typing import TYPE_CHECKING, List, Union

if TYPE_CHECKING:
    from telethon.tl.types import Channel, Chat

    from ..scroll_area_widget import ScrollAreaWidget
    Entity = Union[Channel, Chat]

from PySide6.QtCore import QByteArray, QSize, Qt, Signal, Slot
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QLabel, QLayout, QWidget

from .selection_widget import SelectionWidget
from .SelectionContainerWidget_ui import Ui_SelectionContainerWidget


class SelectionContainerWidget(Ui_SelectionContainerWidget, QWidget):

    finished_adding_check_boxes_signal = Signal()
    is_selection_made_signal = Signal(bool)

    def __init__(self, scroll_area_widget: "ScrollAreaWidget"):
        super().__init__(scroll_area_widget)
        self.setupUi(self)
        self._scroll_area_widget = scroll_area_widget
        self._setup_loading_gif()
        # General.
        self._all_selection_widgets: List[SelectionWidget] = []
        self._total_checked_check_boxes = 0
        self._update_counter_label()

    async def on_get_groups_button_clicked(self) -> None:
        self._delete_all_widgets_from_container_frame_layout()
        self._all_selection_widgets = []
        self._total_checked_check_boxes = 0
        self._update_counter_label() # Reset.

        self._start_loading_gif()
        for i, entity in enumerate(await self._scroll_area_widget.get_scraper().get_scrapable_entities()):
            self._add_selection_widget(i, entity) 
        self._stop_loading_gif()

        self.finished_adding_check_boxes_signal.emit()

    def on_logout_signal(self) -> None:
        self._delete_all_widgets_from_container_frame_layout()
        self._all_selection_widgets = []
        self._total_checked_check_boxes = 0
        self._update_counter_label()

    def get_all_selection_widgets(self):
        return self._all_selection_widgets

    def _delete_all_widgets_from_container_frame_layout(self) -> None:
        while self.selection_widget_container_frame.layout().count():
            child = self.selection_widget_container_frame.layout().takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        # Shrink (redo) the layout after widgets have been deleted.
        self.selection_widget_container_frame.layout().invalidate()
        self.selection_widget_container_frame.layout().activate()

    def _add_selection_widget(self, number: int, entity: "Entity") -> None:
        selection = SelectionWidget(number, entity, self)
        selection.check_box.stateChanged.connect(self._on_check_box_state_changed)
        self._all_selection_widgets.append(selection)
        self.selection_widget_container_frame.layout().addWidget(selection)
        self._update_counter_label()

    @Slot()
    def _on_check_box_state_changed(self, state) -> None:
        if state == 2: # Checked
            self._total_checked_check_boxes += 1
        elif state == 0: # Unchecked
            self._total_checked_check_boxes -= 1
        self._update_counter_label()

        if self._total_checked_check_boxes > 0:
            self.is_selection_made_signal.emit(True)
        else:
            self.is_selection_made_signal.emit(False)

    def _update_counter_label(self):
        self.counter_label.setText(
            f"Selected: {self._total_checked_check_boxes}/{len(self._all_selection_widgets)}"
        )

    def _setup_loading_gif(self) -> None:
        self._loading_gif = QMovie(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "loading.gif"), 
            QByteArray(), 
            self
        )
        self._loading_gif_container_label = QLabel(self)
        self._loading_gif_container_label.setMovie(self._loading_gif)
        self._loading_gif_container_label.setMaximumSize(QSize(40, 40))
        self._loading_gif_container_label.setScaledContents(True)

    def _start_loading_gif(self) -> None:
        self.selection_widget_container_frame.layout().setSizeConstraint(QLayout.SetMaximumSize)
        self.selection_widget_container_frame.layout().addWidget(self._loading_gif_container_label, 0, Qt.AlignCenter)
        self._loading_gif_container_label.setHidden(False)
        self._loading_gif.start()

    def _stop_loading_gif(self) -> None:
        self.selection_widget_container_frame.layout().setSizeConstraint(QLayout.SetFixedSize)
        self.selection_widget_container_frame.layout().removeWidget(self._loading_gif_container_label)
        self._loading_gif_container_label.setHidden(True)
        self._loading_gif.stop()


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
    
    sw = SelectionContainerWidget(None)
    for i in range(15):
        sw._add_selection_widget(i, "Test CheckBox")
    sw.show()

    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())
