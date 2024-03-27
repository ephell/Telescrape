from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QWidget

from src.gui.main_window.central_widget.scrape_widget.scrape_settings_widget.ScrapeSettingsWidget_ui import (
    Ui_ScrapeSettingsWidget
)


class ScrapeSettingsWidget(Ui_ScrapeSettingsWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Telescrape - Scrape Settings")
        self.setFocusPolicy(Qt.ClickFocus)
        self.setFocus()
        self.setWindowFlags(Qt.Dialog)
        self.setFixedSize(self.size())
        self._default_settings = self.get_settings()
        # Signals and slots.
        self.close_button.clicked.connect(self._on_close_button_clicked)
        self.reset_to_default_button.clicked.connect(self._on_reset_to_default_button_clicked)

    def show(self):
        super().show()
        self.setFocus()

    def get_settings(self):
        return {
            "user_active_in_last_days": self.last_active_days_spin_box.value(),
            "exclude_yourself": self.yourself_check_box.isChecked(),
            "exclude_admins": self.admins_check_box.isChecked(),
            "exclude_bots": self.bots_check_box.isChecked(),
            "exclude_deleted_users": self.deleted_users_check_box.isChecked(),
            "exclude_restricted_users": self.restricted_users_check_box.isChecked(),
            "exclude_scam_flagged_users": self.scam_flagged_users_check_box.isChecked(),
            "exclude_fake_flagged_users": self.fake_flagged_users_check_box.isChecked(),
            "exclude_users_in_contacts": self.users_in_contacts_check_box.isChecked(),
            "exclude_users_with_hidden_last_seen_online": self.users_with_hidden_last_seen_online_check_box.isChecked()
        }

    @Slot()
    def _on_close_button_clicked(self):
        self.close()

    @Slot()
    def _on_reset_to_default_button_clicked(self):
        self.last_active_days_spin_box.setValue(self._default_settings["user_active_in_last_days"])
        self.yourself_check_box.setChecked(self._default_settings["exclude_yourself"])
        self.admins_check_box.setChecked(self._default_settings["exclude_admins"])
        self.bots_check_box.setChecked(self._default_settings["exclude_bots"])
        self.deleted_users_check_box.setChecked(self._default_settings["exclude_deleted_users"])
        self.restricted_users_check_box.setChecked(self._default_settings["exclude_restricted_users"])
        self.scam_flagged_users_check_box.setChecked(self._default_settings["exclude_scam_flagged_users"])
        self.fake_flagged_users_check_box.setChecked(self._default_settings["exclude_fake_flagged_users"])
        self.users_in_contacts_check_box.setChecked(self._default_settings["exclude_users_in_contacts"])
        self.users_with_hidden_last_seen_online_check_box.setChecked(self._default_settings["exclude_users_with_hidden_last_seen_online"])


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    ssw = ScrapeSettingsWidget(None)
    ssw.show()
    app.exec()
