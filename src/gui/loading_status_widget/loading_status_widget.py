from PySide6.QtCore import QByteArray, QTimer, QSize
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget

from src.gui.loading_status_widget.LoadingStatusWidget_ui import Ui_LoadingStatusWidget


class LoadingStatusWidget(Ui_LoadingStatusWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setup_loader_gif()
        self.loader_gif_player.start()

    def setup_loader_gif(self):
        self.loader_gif_player = QMovie(
            "src/gui/loading_status_widget/loader.gif", 
            QByteArray(), 
            self
        )
        self.loader_gif_player.setScaledSize(QSize(30, 30))
        self.gif_placeholder_label.setMovie(self.loader_gif_player)


if __name__ == "__main__":
    import sys

    from src.gui.application.application import Application
    app = Application(sys.argv)
    widget = LoadingStatusWidget() 
    widget.show()
    app.exec()
