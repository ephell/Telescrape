from PySide6 import QtWidgets, QtCore, QtGui


class EntityTitleLabel(QtWidgets.QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, _):
        painter = QtGui.QPainter(self)
        metrics = QtGui.QFontMetrics(self.font())
        elided = metrics.elidedText(self.text(), QtCore.Qt.ElideRight, self.width())
        painter.drawText(self.rect(), self.alignment(), elided)
