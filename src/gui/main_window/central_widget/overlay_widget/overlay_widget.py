import asyncio
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.gui.main_window.central_widget.central_widget import CentralWidget

from PySide6.QtCore import QByteArray, QSize
from PySide6.QtGui import QMovie, QPixmap
from PySide6.QtWidgets import QMessageBox, QWidget

from src.gui.main_window.central_widget.overlay_widget.login_code_dialog.login_code_dialog import LoginCodeInputDialog
from src.gui.main_window.central_widget.overlay_widget.OverlayWidget_ui import Ui_OverlayWidget


class OverlayWidget(Ui_OverlayWidget, QWidget):
    """Displayed during sign-in by overlaying the `base_widget` in `CentralWidget`."""

    def __init__(self, central_widget: Optional["CentralWidget"] = None):
        super().__init__(central_widget)
        self.central_widget = central_widget
        self.setupUi(self)
        self.image_label.setMaximumSize(QSize(30, 30))
        self.image_label.setScaledContents(True)
        self.set_image_loading()

    def set_hidden(self, value: bool):
        if self.central_widget is not None:
            self.central_widget.set_overlay_widget_hidden(value)

    def set_message(self, message: str):
        self.message_label.setText(message)

    def set_image_loading(self):
        self.loader_gif_player = QMovie("src/gui/main_window/central_widget/overlay_widget/loader.gif", QByteArray(), self)
        self.image_label.setMovie(self.loader_gif_player)
        self.loader_gif_player.start()

    def set_image_success(self):
        self.image_label.setPixmap(QPixmap("src/gui/login_widget/status_success.png"))

    def set_image_fail(self):
        self.image_label.setPixmap(QPixmap("src/gui/login_widget/status_fail.png"))
    
    async def open_error_message_box(self, text: str):
        QMessageBox(QMessageBox.Critical, "Error", text, parent=self).show()

    async def open_login_code_input_dialog_and_get_input(self):
        future = asyncio.Future()
        self.dialog = LoginCodeInputDialog(self)
        self.dialog.buttonBox.accepted.connect(lambda: future.set_result(self.dialog.lineEdit.text()))
        self.dialog.buttonBox.rejected.connect(lambda: future.set_result(None))
        self.dialog.show()
        await future
        return future.result()


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    mw = QMainWindow()
    cw = OverlayWidget(mw)
    mw.setCentralWidget(cw)
    mw.show()
    app.exec()
