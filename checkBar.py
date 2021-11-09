from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtWidgets import *
from stylesheets import *
import datetime

class CheckBar(QtWidgets.QWidget):

    checked = 0
    def __init__(self, day_id, task_id, window, color):
        super().__init__()
        width = 22
        self.setFixedWidth(width)
        self.setFixedHeight(width)
        self.day_id = day_id
        self.task_id = task_id
        self.window = window 
        self.color = color
        
        self.widget = QWidget(self)
        self.widget.setFixedWidth(width)
        self.widget.setFixedHeight(width)

        # get data from database
        self.read_color()
        self.get_start_date()

    def paintEvent(self, e: QPaintEvent):
        if self.checked == 0:
            self.widget.setStyleSheet(check_bar_unclicked)
        if self.checked == 1:
            self.widget.setStyleSheet(check_bar_first(self.color))
        if self.checked == 2:
            self.widget.setStyleSheet(check_bar_second(self.color))

        # change border_color for todays button
        if self.day_id == (datetime.datetime.today() - self.start_date).days and self.checked == 0:
            self.widget.setStyleSheet(check_bar_today(self.color))

        if self.day_id < 0:
            self.widget.setStyleSheet(check_bar_unclickable)

    def get_start_date(self):
        startDate = self.window.db_task.sql_query("SELECT startDate FROM tasks WHERE id = {}".format(self.task_id))[0][0]
        self.start_date = datetime.datetime.strptime(startDate,  "%Y-%m-%d")

    def _trigger_refresh(self):
        self.update()

    def update_database(self):
        date = self.start_date + datetime.timedelta(days=self.day_id)
        self.window.db_joint.insert_or_update(self.task_id, self.day_id, self.checked, date.date())

    def mousePressEvent(self, e):
        # ignore filler buttons
        if self.day_id < 0:
            return
        # ignore future days
        if self.day_id > (datetime.datetime.today() - self.start_date).days:
            return 

        # only act for left click
        if e.button() == QtCore.Qt.LeftButton:
            # return for future buttons
            self.checked = (self.checked + 1) % 3
            self.update_database()
            # update unfinished tasks if day_id is today
            if self.checked != 2 and self.day_id == (datetime.datetime.today() - self.start_date).days:
                self.window.update_tasks_todo(self.task_id, self.checked)
            self.update()

        # use middle button to set to 2 instantly
        if e.button() == QtCore.Qt.MiddleButton:
            old_checked = self.checked
            self.checked = 2
            self.update_database()
            if old_checked == 0 and self.day_id == (datetime.datetime.today() - self.start_date).days:
                self.window.update_tasks_todo(self.task_id, self.checked)
            self.update()

    def read_color(self):
        result = self.window.db_joint.sql_query("SELECT check_number FROM data_joint WHERE task_id = {} and day_id = {}".format(self.task_id, self.day_id))
        if result:
            self.checked = result[0][0]
            self.update()

