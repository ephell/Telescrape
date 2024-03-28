import os
from typing import Dict, Union

if __name__ == "__main__":
    __package__ = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace(os.path.sep, ".")

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QCheckBox, QFileDialog, QLineEdit, QSpinBox, QWidget

from src.config import Config

from .ScrapeSettingsWidget_ui import Ui_ScrapeSettingsWidget


class ScrapeSettingsWidget(Ui_ScrapeSettingsWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Telescrape - Scrape Settings")
        self.setFocusPolicy(Qt.ClickFocus)
        self.setFocus()
        self.setWindowFlags(Qt.Dialog)
        self.setFixedSize(self.size())
        self._initialize_settings()
        # Signals and slots.
        self.close_button.clicked.connect(self._on_close_button_clicked)
        self.reset_to_default_button.clicked.connect(self._on_reset_to_default_button_clicked)
        self.browse_button.clicked.connect(self._on_browse_button_clicked)

    def show(self):
        super().show()
        self.setFocus()

    def get_current_settings(self) -> Dict[str, Union[int, str, bool]]:
        return self._get_setting_name_to_setting_property_map("current_value")

    def _initialize_settings(self):
        self._connect_setting_widget_update_signals()

        scrape_settings_section_options = Config.get_all_options_from_section(Config.Section.SCRAPE_SETTINGS)
        default_settings = self._get_default_settings()

        if (
            len(scrape_settings_section_options) == 0
            or set(scrape_settings_section_options.keys()) != set(default_settings.keys())
        ):
            self._set_settings(self._get_default_settings())
            return

        self._set_settings(scrape_settings_section_options)

    def _connect_setting_widget_update_signals(self):
        for _, signal in self._get_setting_name_to_setting_property_map("update_signal").items():
            signal.connect(self._on_setting_widget_updated)
                
    def _set_settings(self, settings_names_and_values: Dict[str, Union[int, str, bool]]):
        try:
            setting_name_to_widget_map = self._get_setting_name_to_widget_map()
            for name, value in settings_names_and_values.items():
                widget = setting_name_to_widget_map.get(name)
                if widget is not None:
                    self._set_widget_value(widget, value)
                else:
                    raise KeyError(f"Key '{name}' doesn't exist in 'setting_name_to_widget_map' dictionary.")

            self._write_settings_to_config(self.get_current_settings())
        except _SetWidgetValueException:
            self._set_settings(self._get_default_settings())
            self._write_settings_to_config(self._get_default_settings())

    def _set_widget_value(self, widget: Union[QSpinBox, QCheckBox, QLineEdit], value):
        if isinstance(widget, QSpinBox):
            if isinstance(value, int):
                self.last_active_days_spin_box.setValue(value)
            elif isinstance(value, str) and value.isdigit():
                self.last_active_days_spin_box.setValue(int(value))
            else:
                raise _SetWidgetValueException(
                    f"Invalid type of value for '{widget}'. " 
                    f"Expected: 'int' or 'str'. Received: '{type(value)}'."
                )
        elif isinstance(widget, QCheckBox):
            if isinstance(value, bool):
                widget.setChecked(value)
            elif isinstance(value, str):
                if value.lower() in ["true", "false"]:
                    widget.setChecked(value.lower() == "true")
                else:
                    raise _SetWidgetValueException(
                        f"Invalid 'str' value for '{widget}'. " 
                        f"Expected: 'True' or 'False'. Received: '{value}'."
                    )
            else:
                raise _SetWidgetValueException(
                    f"Invalid type of value for '{widget}'. " 
                    f"Expected: 'bool' or 'str'. Received: '{type(value)}'."
                )
        elif isinstance(widget, QLineEdit):
            if isinstance(value, str):
                widget.setText(value)
                widget.setCursorPosition(0)
        else:
            raise TypeError(f"Widget of type '{widget}' not supported!")

    def _write_settings_to_config(self, settings: Dict):
        Config.delete_all_options_from_section(Config.Section.SCRAPE_SETTINGS)
        for setting, value in settings.items():
            Config.write_option_to_section(Config.Section.SCRAPE_SETTINGS, setting, str(value))

    def _get_settings_info_map(self) -> Dict[str, Dict[str, Union[int, str, bool, QWidget, Signal]]]:
        return {
            "user_active_in_last_days": {
                "default_value": 0, 
                "current_value": self.last_active_days_spin_box.value(),
                "widget": self.last_active_days_spin_box,
                "update_signal": self.last_active_days_spin_box.valueChanged
            },
            "exclude_yourself": {
                "default_value": False, 
                "current_value": self.yourself_check_box.isChecked(),
                "widget": self.yourself_check_box,
                "update_signal": self.yourself_check_box.stateChanged
            },
            "exclude_admins": {
                "default_value": False, 
                "current_value": self.admins_check_box.isChecked(),
                "widget": self.admins_check_box,
                "update_signal": self.admins_check_box.stateChanged
            },
            "exclude_bots": {
                "default_value": True, 
                "current_value": self.bots_check_box.isChecked(),
                "widget": self.bots_check_box,
                "update_signal": self.bots_check_box.stateChanged
            },
            "exclude_deleted_users": {
                "default_value": True, 
                "current_value": self.deleted_users_check_box.isChecked(),
                "widget": self.deleted_users_check_box,
                "update_signal": self.deleted_users_check_box.stateChanged
            },
            "exclude_restricted_users": {
                "default_value": True, 
                "current_value": self.restricted_users_check_box.isChecked(),
                "widget": self.restricted_users_check_box,
                "update_signal": self.restricted_users_check_box.stateChanged
            },
            "exclude_scam_flagged_users": {
                "default_value": True, 
                "current_value": self.scam_flagged_users_check_box.isChecked(),
                "widget": self.scam_flagged_users_check_box,
                "update_signal": self.scam_flagged_users_check_box.stateChanged
            },
            "exclude_fake_flagged_users": {
                "default_value": True, 
                "current_value": self.fake_flagged_users_check_box.isChecked(),
                "widget": self.fake_flagged_users_check_box,
                "update_signal": self.fake_flagged_users_check_box.stateChanged
            },
            "exclude_users_in_contacts": {
                "default_value": False, 
                "current_value": self.users_in_contacts_check_box.isChecked(),
                "widget": self.users_in_contacts_check_box,
                "update_signal": self.users_in_contacts_check_box.stateChanged
            },
            "exclude_users_with_hidden_last_seen_online": {
                "default_value": False, 
                "current_value": self.users_with_hidden_last_seen_online_check_box.isChecked(),
                "widget": self.users_with_hidden_last_seen_online_check_box,
                "update_signal": self.users_with_hidden_last_seen_online_check_box.stateChanged
            },
            "data_dir_path": {
                "default_value": os.path.join(os.getcwd(), "scraped_data_dir"), 
                "current_value": self.data_dir_path_line_edit.text(),
                "widget": self.data_dir_path_line_edit,
                "update_signal": self.data_dir_path_line_edit.textChanged 
            }
        }

    def _get_default_settings(self) -> Dict[str, Union[int, str, bool]]:
        return self._get_setting_name_to_setting_property_map("default_value")

    def _get_setting_name_to_widget_map(self) -> Dict[str, QWidget]:
        return self._get_setting_name_to_setting_property_map("widget")

    def _get_setting_name_to_setting_property_map(
            self, 
            setting_property: str
        ) -> Dict[str, Union[int, str, bool, Signal]]:
        settings = {}
        for setting_name, setting_properties in self._get_settings_info_map().items():
            for property_name, property_value in setting_properties.items():
                if property_name == setting_property:
                    settings.update({setting_name: property_value})
        return settings

    @Slot()
    def _on_close_button_clicked(self):
        self.close()

    @Slot()
    def _on_reset_to_default_button_clicked(self):
        self._set_settings(self._get_default_settings())

    @Slot()
    def _on_browse_button_clicked(self):
        dir_path = QFileDialog.getExistingDirectory(self, "Select Directory", "", QFileDialog.ShowDirsOnly)
        if dir_path:
            self.data_dir_path_line_edit.setText(dir_path)
            self.data_dir_path_line_edit.setCursorPosition(0)

    @Slot()
    def _on_setting_widget_updated(self):
        for setting_name, setting_value in self.get_current_settings().items():
            Config.write_option_to_section(Config.Section.SCRAPE_SETTINGS, setting_name, str(setting_value))


class _SetWidgetValueException(Exception):

    def __init__(self, message: str):
        super().__init__(message)


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    ssw = ScrapeSettingsWidget(None)
    ssw.show()
    app.exec()
