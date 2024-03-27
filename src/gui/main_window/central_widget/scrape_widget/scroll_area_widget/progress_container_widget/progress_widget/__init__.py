import os

if __name__ == "__main__":
    __package__ = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace(os.path.sep, ".")

from PySide6.QtCore import QByteArray, QSize, Signal
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QWidget

from .ProgressWidget_ui import Ui_ProgressWidget


class ProgressWidget(Ui_ProgressWidget, QWidget):
    """Used to display the status of entity that is being scraped."""

    finished_signal = Signal(bool) # bool = is_success

    def __init__(self, selection_title: str, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.selection_title_label.setText(selection_title)
        self.status_image_label.setMaximumSize(QSize(17, 17))
        self.status_image_label.setScaledContents(True)
        module_dir_path = os.path.dirname(os.path.abspath(__file__))
        self._success_image = QPixmap(os.path.join(module_dir_path, "status_success.png"))
        self._fail_image = QPixmap(os.path.join(module_dir_path, "status_fail.png"))
        self._loading_gif = QMovie(os.path.join(module_dir_path, "loading.gif"), QByteArray(), self)

    def set_status_loading(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setMovie(self._loading_gif)
        self._loading_gif.start()

    def set_status_success(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setPixmap(self._success_image)
        self.finished_signal.emit(True)

    def set_status_fail(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setPixmap(self._fail_image)
        self.finished_signal.emit(False)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    esw = ProgressWidget("Test Group Title")

    esw.set_status_loading("Scraping ... ")

    esw.show()
    app.exec()
