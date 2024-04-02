if __name__ == "__main__":
    import os
    __package__ = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace(os.path.sep, ".")

from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from PySide6.QtWidgets import QLineEdit
    from src.gui.main_window.central_widget import CentralWidget

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from src.config import Config

from .LoginWidget_ui import Ui_LoginWidget


class LoginWidget(Ui_LoginWidget, QWidget):

    def __init__(self, central_widget: Optional["CentralWidget"] = None):
        super().__init__(central_widget)
        self._central_widget = central_widget
        self.setupUi(self)
        self._initialize_login_details()

    def set_hidden(self, value: bool):
        if self._central_widget is not None:
            self._central_widget.set_login_widget_hidden(value)

    def get_current_login_details(self) -> Dict[str, str]:
        return {
            name: line_edit.text()
            for name, line_edit in self._get_login_details_names_and_line_edits().items()
        }

    def _initialize_login_details(self):
        login_details_names_and_line_edits = self._get_login_details_names_and_line_edits()
        login_details_section_options = Config.get_all_options_from_section(Config.Section.LOGIN_DETAILS)
        if (
            len(login_details_section_options) == 0
            or set(login_details_section_options.keys()) != set(login_details_names_and_line_edits.keys())
        ):
            self._reset_config_login_details()
            self._reset_login_line_edits()
        else:
            self._set_login_details_from_config()
        self._connect_line_edits_update_signals()

    def _get_login_details_names_and_line_edits(self) -> Dict[str, "QLineEdit"]:
        return {
            "phone_number": self.line_edit_phone_number,
            "api_id": self.line_edit_api_id,
            "api_hash": self.line_edit_api_hash
        }

    def _reset_config_login_details(self):
        Config.delete_all_options_from_section(Config.Section.LOGIN_DETAILS)
        for detail, _ in self.get_current_login_details().items():
            Config.write_option_to_section(Config.Section.LOGIN_DETAILS, detail, "")
    
    def _reset_login_line_edits(self):
        for _, line_edit in self._get_login_details_names_and_line_edits().items():
            line_edit.setText("")

    def _set_login_details_from_config(self):
        for config_n, config_v in Config.get_all_options_from_section(Config.Section.LOGIN_DETAILS).items():
            for login_n, line_edit in self._get_login_details_names_and_line_edits().items():
                if config_n == login_n:
                    line_edit.setText(config_v)
                    line_edit.setCursorPosition(0)

    def _connect_line_edits_update_signals(self):
        for _, line_edit in self._get_login_details_names_and_line_edits().items():
            line_edit.textChanged.connect(self._on_line_edit_editing_finished)

    @Slot()
    def _on_line_edit_editing_finished(self):
        """Write current login details to config."""
        Config.delete_all_options_from_section(Config.Section.LOGIN_DETAILS)
        for detail, value in self.get_current_login_details().items():
            Config.write_option_to_section(Config.Section.LOGIN_DETAILS, detail, str(value))


if __name__ == "__main__":
    import sys

    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    mw = QMainWindow()
    cw = LoginWidget(mw)
    mw.setCentralWidget(cw)
    mw.show()
    app.exec()
