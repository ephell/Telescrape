from PySide6.QtCore import QByteArray, QSize
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QWidget

from src.gui.loading_status_widget.LoadingStatusWidget_ui import Ui_LoadingStatusWidget


class LoadingStatusWidget(Ui_LoadingStatusWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.status_image_placeholder_label.setMaximumSize(QSize(30, 30))
        self.status_image_placeholder_label.setScaledContents(True)
        self.set_status_image_loading()

    def set_status_message(self, message: str):
        self.status_message_label.setText(message)

    def set_status_image_loading(self):
        self.loader_gif_player = QMovie(
            "src/gui/loading_status_widget/loader.gif", 
            QByteArray(), 
            self
        )
        self.status_image_placeholder_label.setMovie(self.loader_gif_player)
        self.loader_gif_player.start()

    def set_status_image_success(self):
        self.status_image_placeholder_label.setPixmap(
            QPixmap("src/gui/loading_status_widget/status_success.png")
        )

    def set_status_image_fail(self):
        self.status_image_placeholder_label.setPixmap(
            QPixmap("src/gui/loading_status_widget/status_fail.png")
        )


if __name__ == "__main__":
    import sys

    from src.gui.application.application import Application
    app = Application(sys.argv)
    widget = LoadingStatusWidget() 
    widget.show()
    app.exec()
