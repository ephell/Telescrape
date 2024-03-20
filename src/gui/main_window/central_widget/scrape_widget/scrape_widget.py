from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.central_widget import CentralWidget

from PySide6.QtWidgets import QCheckBox, QLayout, QWidget

from src.gui.main_window.central_widget.scrape_widget.ScrapeWidget_ui import Ui_ScrapeWidget


class ScrapeWidget(Ui_ScrapeWidget, QWidget):

    def __init__(self, central_widget: Optional["CentralWidget"] = None):
        super().__init__(central_widget)
        self.central_widget = central_widget
        self.setupUi(self)
        self.scroll_area_layout = self.scroll_area_widget_contents.layout()
        # Force items inside the scroll area to stack from top to bottom, equally.
        self.scroll_area_layout.setSizeConstraint(QLayout.SetFixedSize)
        self.checked_check_boxes_counter = 0
        self.all_check_boxes = []

    def set_hidden(self, value: bool):
        if self.central_widget is not None:
            self.central_widget.set_scrape_widget_hidden(value)
        else:
            self.setHidden(value)

    def _add_check_box(self, text: str = "Test") -> QCheckBox:
        check_box = QCheckBox(self)
        check_box.setText(text)
        check_box.stateChanged.connect(self.on_checkbox_stateChanged)
        self.all_check_boxes.append(check_box)
        self.scroll_area_layout.addWidget(check_box)
        return check_box

    def on_checkbox_stateChanged(self, check_state):
        if check_state == 2: # Checked
            self.checked_check_boxes_counter += 1
        elif check_state == 0: # Unchecked
            self.checked_check_boxes_counter -= 1
        self.check_boxes_checked_label.setText(
            f"({self.checked_check_boxes_counter}/{len(self.all_check_boxes)}) Selected."
        )


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    sw = ScrapeWidget()

    for i in range(5):
        sw._add_check_box(f"Checkbox {i}")

    sw.show()
    app.exec()
