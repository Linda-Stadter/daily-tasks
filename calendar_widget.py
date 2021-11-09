from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QEvent, QObject
from PyQt5.QtWidgets import *
from stylesheets import *


class CalendarWidget(QtWidgets.QWidget):

    tooltip = None
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, window, date, task_count):
        super().__init__()
        self.window = window
        self.date = date
        self.task_count = task_count
        width = 10
        self.setFixedWidth(width)
        self.setFixedHeight(width)
        
        self.widget = QWidget(self)
        self.widget.setFixedWidth(width)
        self.widget.setFixedHeight(width)

        self.installEventFilter(self)

    def eventFilter(self, a0: 'QObject', a1: 'QEvent') -> bool:
        if a1.type() == QEvent.Enter:
            self.create_tooltip(a0, a1)
        return super().eventFilter(a0, a1)

    def leaveEvent(self, a0: QtCore.QEvent) -> None:
        self.tooltip.deleteLater()
        return super().leaveEvent(a0)

    def create_tooltip(self, a0, a1):
        weekday = self.weekdays[self.date.weekday()]
        text = "{}, {} \n{} Tasks".format(weekday, self.date, self.task_count)
        tooltip = QLabel(text, self.window.ui.centralwidget)
        tooltip.move(self.pos()+QtCore.QPoint(100, 60))
        tooltip.setStyleSheet(calendar_tooltip_style)
        tooltip.adjustSize()
        tooltip.show()

        self.tooltip = tooltip

