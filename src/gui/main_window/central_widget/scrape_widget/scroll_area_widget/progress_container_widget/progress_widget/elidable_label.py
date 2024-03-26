from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFontMetrics, QPainter
from PySide6.QtWidgets import QLabel, QToolTip


class ElidableLabel(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self._tooltip = QToolTip()

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        metrics = QFontMetrics(self.font())
        elided_text = metrics.elidedText(self.text(), Qt.ElideRight, self.width())
        if elided_text != self.text():
            trigger_area = QRect(self.width() - 20, 0, 20, self.height())
            if trigger_area.contains(event.pos()):
                self._tooltip.showText(self.mapToGlobal(event.pos()), self.text())

    def paintEvent(self, _):
        painter = QPainter(self)
        metrics = QFontMetrics(self.font())
        elided_text = metrics.elidedText(self.text(), Qt.ElideRight, self.width())
        painter.drawText(self.rect(), self.alignment(), elided_text)
