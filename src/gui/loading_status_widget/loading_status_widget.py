from PySide6.QtWidgets import QWidget

from src.gui.loading_status_widget.LoadingStatusWidget_ui import Ui_LoadingStatusWidget


class LoadingStatusWidget(Ui_LoadingStatusWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        

if __name__ == "__main__":
    import sys

    from src.gui.application.application import Application
    app = Application(sys.argv)
    widget = LoadingStatusWidget() 
    widget.show()
    app.exec()
