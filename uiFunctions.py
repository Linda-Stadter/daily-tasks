import random

from PyQt5 import *
from PyQt5 import QtCore, QtGui
from calendar_widget import CalendarWidget
from PyQt5.QtWidgets import *
from stylesheets import *

from checkBar import CheckBar
from formating import *

POSSIBLE_COLORS = ["red", "blue", "green", "yellow"]

def show_cancel_task_warning():
    msg = QMessageBox()
    msg.setWindowTitle("Cancel task")
    msg.setText("Do you really want to stop this task early?")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setDefaultButton(QMessageBox.Cancel)
    msg.exec()

def show_delete_warning(window, sender):
    msg = QMessageBox()
    msg.setWindowTitle("Deleting Task")
    msg.setText("Do you really want to delete this task entirely?")
    msg.setIcon(QMessageBox.Warning)
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setDefaultButton(QMessageBox.Cancel)
    msg.buttonClicked.connect(lambda x: window.delete_task(x, msg, sender))
    msg.exec()

def add_shadow_effect(widget):
    effect = QGraphicsDropShadowEffect()
    effect.setColor(QtGui.QColor(0, 0, 0, 50))
    effect.setBlurRadius(15)
    effect.setXOffset(0)
    effect.setYOffset(0)
    widget.setGraphicsEffect(effect)

def get_random_color():
    return random.choice(POSSIBLE_COLORS)

# Creating widgets
def create_calendar_day_widget(window, date, count, color):
    colors = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]

    day_widget = CalendarWidget(window, date, count)
    style = calendar_widget_style.format(colors[color])
    day_widget.setStyleSheet(style)
    day_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    day_widget.setFixedWidth(10)
    day_widget.setFixedHeight(10)

    return day_widget

def create_tasks_todo_widget(name, color):
    label = QLabel(name)
    label.setObjectName(name)
    style = add_bgcolor_to_style(color, rounded_box)
    label.setStyleSheet(style)
    return label

def create_task_widget(window, task_id, name, days, duration, day_difference, color):
    task_widget = QWidget()
    task_widget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    task_widget.customContextMenuRequested.connect(window.custom_context_menu)
    task_layout = QVBoxLayout()
    task_layout.setSpacing(0)
    task_layout.setContentsMargins(1, 9, 17, 9)

    #set alignment in your vertical layout
    task_layout.setAlignment(QtCore.Qt.AlignTop)
    task_widget.setLayout(task_layout)
    task_widget.setMinimumWidth(230)
    
    name_banner_widget = QWidget()
    name_banner_widget.setFixedHeight(20)
    name_banner_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    style = add_bgcolor_to_style(color, smaller_rounded_box)
    horizontal_layout = QHBoxLayout()
    
    duration = convert_time(duration)
    duration_label = QLabel(duration)
    style = add_bgcolor_to_style(color, smaller_rounded_box)
    style = add_to_style("margin-left: -5px;", style)
    duration_label.setStyleSheet(style)
    duration_label.setAlignment(QtCore.Qt.AlignRight)

    max_char_length = 30
    name_length = max_char_length - len(duration)
    name_label = QLabel(name[:name_length])
    style = add_bgcolor_to_style(color, smaller_rounded_box)
    style = add_to_style("margin-right: -5px;", style)
    name_label.setStyleSheet(style)

    horizontal_layout.addWidget(name_label)
    horizontal_layout.addWidget(duration_label)
    
    task_layout.addLayout(horizontal_layout)


    checkbox_widget = QWidget()
    checkbox_grid = QGridLayout()
    checkbox_grid.setAlignment(QtCore.Qt.AlignLeft)
    checkbox_widget.setLayout(checkbox_grid)
    checkbox_rows = 7

    checkbar_number = days + day_difference

    for d in range(checkbar_number):
        checkbox_id = d - day_difference
        check_bar = CheckBar(checkbox_id, task_id, window, color)
        checkbox_grid.addWidget(check_bar, d//checkbox_rows, d%checkbox_rows)

    task_layout.addWidget(checkbox_widget)

    return task_widget
    