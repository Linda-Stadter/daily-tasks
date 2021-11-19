import sys
import datetime
import calendar
import numpy as np

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import *

from main_gui import Ui_MainWindow
from formating import *
from calendar_widget import *
from stylesheets import *
from sql_functions import *
from uiFunctions import *
from flowlayout import FlowLayout

class MainWindow(QMainWindow):
    widget_task_ids = {}

    def __init__(self):
        QMainWindow.__init__(self)
        self.db_task = SQLTaskConnection("task_data")
        self.db_joint = SQLJointConnection("data_joint")
        self.year = datetime.datetime.today().year

        self.resize(QtCore.QSize(800, 600))
        self.setMinimumSize(QtCore.QSize(800, 600))
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

        self.show()

    def init_ui(self):
        self.init_flow_layouts()
        self.init_tasks_todo()
        self.init_tasks()
        self.create_calendar_statistics()
        self.init_effects()
        self.connect_buttons()

        self.ui.Pages_Widget.setCurrentWidget(self.ui.page_show_tasks)
        self.ui.day_field.setValidator(QtGui.QIntValidator())

    def init_flow_layouts(self):
        # flow layouts need to be initialized by code
        layout = FlowLayout()
        widget = self.ui.tasks_todo_widget
        widget.setLayout(layout)

        layout = FlowLayout()
        widget = self.ui.tasks_widget
        widget.setLayout(layout)

    def init_effects(self):
        add_shadow_effect(self.ui.scrollArea)
        add_shadow_effect(self.ui.history)
        add_shadow_effect(self.ui.tasks_todo)
        add_shadow_effect(self.ui.add_task_widget)

    def connect_buttons(self):
        self.ui.Btn_Toggle.clicked.connect(lambda: self.toggle_menu(130))
        self.ui.Btn_Menu_2.clicked.connect(lambda: self.change_page(self.ui.page_add_task))
        self.ui.Btn_Menu_1.clicked.connect(lambda: self.change_page(self.ui.page_show_tasks))
        self.ui.Btn_Menu_3.clicked.connect(lambda: self.change_page(self.ui.page_statistics))
        self.ui.Button_AddTask.clicked.connect(self.insert_new_task)
        self.ui.button_last_year.clicked.connect(lambda: self.change_calendar_year(-1))
        self.ui.button_next_year.clicked.connect(lambda: self.change_calendar_year(+1))
    
    def custom_context_menu(self, event):
        contextMenu = QMenu(self)
        delete = contextMenu.addAction("Delete")
        #TODO implement Cancel Task
        cancel_task = contextMenu.addAction("Cancel Task")
        action = contextMenu.exec_(self.mapToGlobal(self.mapFromGlobal(QtGui.QCursor.pos())))
        if action == delete:
            self.show_delete_warning(self.sender())
        elif action == cancel_task:
            self.show_cancel_task_warning(self.sender())
    
    def show_cancel_task_warning(self, sender):
        msg = QMessageBox()
        msg.setWindowTitle("Cancel task")
        msg.setText("Do you really want to stop this task early?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(lambda x: self.cancel_task(x, msg, sender))
        msg.exec()

    def show_delete_warning(self, sender):
        msg = QMessageBox()
        msg.setWindowTitle("Deleting Task")
        msg.setText("Do you really want to delete this task entirely?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(lambda x: self.delete_task(x, msg, sender))
        msg.exec()

    def delete_task(self, button, msg, sender):
        if button == msg.button(QMessageBox.Cancel):
            return
        id = self.widget_task_ids[sender]
        sender.deleteLater()

        # delte label on todo tasks
        name = self.db_task.sql_query("SELECT taskName FROM tasks WHERE id = {}".format(id))
        name = name[0][0]

        label = self.ui.tasks_todo_widget.findChild(QLabel, name)
        if label:
            # label was on the todo list
            label.deleteLater()

        # delete from db
        res = self.db_task.sql_query_commit("DELETE FROM tasks WHERE id={}".format(id))
        res = self.db_joint.sql_query_commit("DELETE FROM data_joint WHERE task_id={}".format(id))

    def cancel_task(self, button, msg, sender):
        if button == msg.button(QMessageBox.Cancel):
            return
        id = self.widget_task_ids[sender]
        task = self.db_task.sql_query("SELECT * FROM tasks WHERE id = {}".format(id))
        task = task[0]
        print(task)
        new_end_date = datetime.date.today()
        new_days = (datetime.datetime.today() - datetime.datetime.strptime(task[4],  "%Y-%m-%d")).days
        self.db_task.update_row(id, task[1], new_days, task[3], task[4], new_end_date, task[6])

        self.update_tasks_todo(id, 1)
        sender.deleteLater()

    def change_page(self, page):
        self.ui.Pages_Widget.setCurrentWidget(page)

    def toggle_menu(self, max_width):
        current_width = self.ui.frame_left_menu.width()
        end_width = 60
        if current_width == 60:
            end_width = max_width
        else:
            self.ui.Btn_Menu_1.setText("")
            self.ui.Btn_Menu_2.setText("")
            self.ui.Btn_Menu_3.setText("")
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(100)
        self.animation.setStartValue(current_width)
        self.animation.setEndValue(end_width)
        #self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        if end_width == max_width:
            self.animation.finished.connect(self.show_button_text)

    def show_button_text(self):
        self.ui.Btn_Menu_1.setText(" TASKS")
        self.ui.Btn_Menu_2.setText(" EDIT")
        self.ui.Btn_Menu_3.setText(" HISTORY")

    def select_tasks_todo(self):
        current_tasks = self.db_task.sql_query("SELECT * FROM tasks WHERE endDate > strftime('%Y-%m-%d', 'now')")
        if not current_tasks:
            return []
        # sort by start date to get oldest start date of a running task
        current_tasks.sort(key=lambda x: x[4])
        oldest_start_date = current_tasks[0][4]
        
        # differences[i] states how many days task i is younger than the oldest relevant task
        differences = {task[0]: (datetime.datetime.strptime(task[4],  "%Y-%m-%d") - datetime.datetime.strptime(oldest_start_date,  "%Y-%m-%d")).days for task in current_tasks}
        # id of check bar for today (with respect to the oldest current task)
        today_day_id = (datetime.datetime.today() - datetime.datetime.strptime(oldest_start_date,  "%Y-%m-%d")).days
        current_task_ids = set([x[0] for x in current_tasks])

        query = format_list_sql_query("SELECT * FROM data_joint WHERE check_number != 0 and task_id", current_task_ids)
        result = self.db_joint.sql_query(query)

        # day_id is different for newer tasks -> subtract number in differences at the respective id
        # task_id starts at 1
        done_task_ids = set([task[0] for task in result if task[1] == today_day_id-differences[task[0]]])
        tasks_todo_ids = current_task_ids - done_task_ids

        return tasks_todo_ids

    def init_tasks_todo(self):
        tasks_todo_ids = self.select_tasks_todo()

        layout = self.ui.tasks_todo_widget.layout()
        layout.setSpacing(8)

        query = format_list_sql_query("SELECT * FROM tasks WHERE id", tasks_todo_ids)
        rows = self.db_task.sql_query(query)
        names = [x[1] for x in rows]

        for i, name in enumerate(names):
            widget = create_tasks_todo_widget(name, rows[i][6])
            layout.addWidget(widget)

    # check 0 means to add
    # check 1 means to delete
    def update_tasks_todo(self, id, checked):
        res = self.db_task.sql_query("SELECT taskName, color FROM tasks WHERE id = {}".format(id))
        name = res[0][0]

        if checked != 0:
            label = self.ui.tasks_todo_widget.findChild(QLabel, name)
            label.deleteLater()
        else:
            layout = self.ui.tasks_todo_widget.layout()
            color = res[0][1]
            widget = create_tasks_todo_widget(name, color)
            layout.addWidget(widget)

    def insert_new_task(self):
        if not self.ui.task_field.text() or not self.ui.day_field.text():
            return

        max_input = 24
        # insert new task into database
        name_input = self.ui.task_field.text()[:max_input]
        days_input = min(31, int(self.ui.day_field.text()))
        duration_input = self.ui.time_field.time().toString("HH:mm")

        # clear inputs
        self.ui.task_field.clear()
        self.ui.day_field.clear()
        self.ui.time_field.clear()

        start_date = datetime.date.today()
        rnd_color = get_random_color()
        task_id = self.db_task.insert_task(name_input, days_input, duration_input, start_date, rnd_color)

        # insert new task into ui
        layout = self.ui.tasks_widget.layout()
        tasks = self.db_task.sql_query( "SELECT * FROM tasks WHERE endDate > strftime('%Y-%m-%d', 'now')")
        tasks.sort(key=lambda x: x[2], reverse=True)

        oldest_start_date = sorted(tasks, key=lambda x: x[4])[0][4] if tasks else start_date
        day_difference = (start_date - datetime.datetime.strptime(oldest_start_date,  "%Y-%m-%d").date()).days

        task_widget = create_task_widget(self, task_id, name_input, days_input, duration_input, day_difference, rnd_color)
        self.widget_task_ids[task_widget] = task_id
        layout.addWidget(task_widget)

        self.update_tasks_todo(task_id, 0)
        self.change_page(self.ui.page_show_tasks)

    def init_tasks(self):
        layout = self.ui.tasks_widget.layout()
        layout.setSpacing(30)

        tasks = self.db_task.sql_query("SELECT * FROM tasks WHERE endDate > strftime('%Y-%m-%d', 'now')")
        if not tasks:
            return
        tasks.sort(key=lambda x: x[2], reverse=True)
        oldest_start_date = sorted(tasks, key=lambda x: x[4])[0][4]

        for task in tasks:
            day_difference = (datetime.datetime.strptime(task[4],  "%Y-%m-%d") - datetime.datetime.strptime(oldest_start_date,  "%Y-%m-%d")).days
            task_widget = create_task_widget(self, task[0], task[1], task[2], task[3], day_difference, task[6])
            self.widget_task_ids[task_widget] = task[0]
            layout.addWidget(task_widget)
    
    def compute_tasks_count_quantiles(self):
        res = self.db_joint.sql_query("SELECT date, count(task_id) FROM data_joint WHERE check_number != 0 GROUP BY date")
        if not res:
            return [], []
        tasks_per_day = {x[0]: x[1] for x in res}
        quantiles = np.quantile(list(tasks_per_day.values()), [0.25, 0.5, 0.75, 1.0])

        return quantiles, tasks_per_day

    def change_calendar_year(self, i):
        current_year = datetime.datetime.today().year
        year = self.year + i
        self.year = year if year <= current_year else current_year
        
        # delete old calendar
        for i in range(self.ui.calendar.count()):
            self.ui.calendar.itemAt(i).widget().deleteLater()

        # create new one with new year
        self.create_calendar_statistics()

    def create_calendar_statistics(self):
        quantiles, tasks_per_day = self.compute_tasks_count_quantiles()

        self.ui.year_label.setText("{}".format(self.year))

        columns = 7
        calendar_grid = self.ui.calendar
        calendar_grid.setSpacing(2)
        d = 0
        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(self.year, month)
            for week in month_calendar:
                for day in week:
                    count = 0
                    # skip first 0 days at the beginning of the year 
                    # count rows in order for monday to begin in row 0
                    if month == 1 and day == 0:
                        d += 1
                        continue
                    # do not count rows for all other 0 days
                    elif day == 0:
                        continue
                    date = datetime.date(self.year, month, day)
                    color = 0
                    try: 
                        count = tasks_per_day[str(date)]
                        color = 1
                        for i in range(len(quantiles)-1, 0, -1):
                            if count >= quantiles[i]:
                                color = i+1
                                break
                    except:
                        color = 0

                    date = datetime.date(self.year, month, day)
                    day_widget = create_calendar_day_widget(self, date, count, color)
                    calendar_grid.addWidget(day_widget, d%columns, d//columns)

                    d += 1
                    # for january skip 0 days at the end of month
                    if day == 31:
                        break
        


app = QApplication(sys.argv)
window = MainWindow()

try:
    sys.exit(app.exec_())
except:
    print("Exit")
