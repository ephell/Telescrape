from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from src.gui.main_window.central_widget.scrape_widget.scrape_settings_widget.ScrapeSettingsWidget_ui import (
    Ui_ScrapeSettingsWidget
)


class ScrapeSettingsWidget(Ui_ScrapeSettingsWidget, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Telescrape - Scrape Settings")
        self.setFocus()
        self.setWindowFlags(Qt.Dialog)
        self.setFixedSize(self.size())

    def show(self):
        super().show()
        self.setFocus()

    def get_settings(self):
        return {
            "user_active_in_last_days": self.last_active_days_spin_box.value(),
            "exclude_admins": self.admins_check_box.isChecked(),
            "exclude_bots": self.bots_check_box.isChecked(),
            "exclude_deleted_users": self.deleted_users_check_box.isChecked(),
            "exclude_restricted_users": self.restricted_users_check_box.isChecked(),
            "exclude_scam_flagged_users": self.scam_flagged_users_check_box.isChecked(),
            "exclude_fake_flagged_users": self.fake_flagged_users_check_box.isChecked(),
        }


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication([])
    ssw = ScrapeSettingsWidget(None)
    ssw.show()
    app.exec()
