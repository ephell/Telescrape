from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from telethon.tl.types import Channel, Chat
    Entity = Union[Channel, Chat]

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QCheckBox, QHBoxLayout, QLabel, QSizePolicy, QWidget


class SelectionWidget(QWidget):

    def __init__(self, number: int, entity: "Entity", parent=None):
        super().__init__(parent)
        self.entity = entity
        self.number_label = self._setup_number_label(number)
        self.check_box = self._setup_check_box(self.entity)
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self.number_label)
        self._layout.addWidget(self.check_box)
        self.setLayout(self._layout)

    def _setup_number_label(self, number: int) -> QLabel:
        label = QLabel(self)
        label.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred))
        label.setMinimumSize(QSize(30, 0))
        label.setAlignment(Qt.AlignCenter)
        label.setText(f"{str(number + 1)}.")
        font = QFont()
        font.setPointSize(10)
        label.setFont(font)
        return label

    def _setup_check_box(self, entity: Union["Entity", str]) -> QCheckBox: # 'str' is only meant for testing.
        check_box = QCheckBox(self)
        font = QFont()
        font.setPointSize(10)
        check_box.setFont(font)
        if isinstance(entity, str):
            check_box.setText(entity)
        else:
            check_box.setText(entity.title)
        return check_box


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    sw = SelectionWidget(0, "Test CheckBox")
    sw.show()
    app.exec()
