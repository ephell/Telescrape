import os

from PySide6.QtCore import QByteArray, QSize
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QWidget

from src.gui.main_window.central_widget.scrape_widget.entity_status_widget.EntityStatusWidget_ui import Ui_EntityStatusWidget


class EntityStatusWidget(Ui_EntityStatusWidget, QWidget):

    def __init__(self, entity_title: str = "Test", parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.entity_title_label.setText(entity_title)
        self.status_image_label.setMaximumSize(QSize(20, 20))
        self.status_image_label.setScaledContents(True)
        module_dir_path = os.path.dirname(os.path.abspath(__file__))
        self._SUCCESS_IMAGE = QPixmap(os.path.join(module_dir_path, "status_success.png"))
        self._FAIL_IMAGE = QPixmap(os.path.join(module_dir_path, "status_fail.png"))
        self._LOADING_GIF = QMovie(os.path.join(module_dir_path, "loading.gif"), QByteArray(), self)

    def set_status_loading(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setMovie(self._LOADING_GIF)
        self._LOADING_GIF.start()

    def set_status_success(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setPixmap(self._SUCCESS_IMAGE)

    def set_status_fail(self, message: str):
        self.status_message_label.setText(message)
        self.status_image_label.setPixmap(self._FAIL_IMAGE)


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    esw = EntityStatusWidget("Test Group Title")

    esw.set_status_loading("Scraping ... ")

    esw.show()
    app.exec()
