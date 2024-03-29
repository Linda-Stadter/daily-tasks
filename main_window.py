import sys
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

from matplotlib.patches import FancyBboxPatch
from mlpcanvas import * 
from datetime import datetime, date, timedelta

class MainWindow(QMainWindow):
    widget_task_ids = {}
    task_overviews_per_month = [None for i in range(12)]

    def __init__(self):
        QMainWindow.__init__(self)
        self.db_task = SQLTaskConnection("task_data")
        self.db_joint = SQLJointConnection("data_joint")
        self.year = datetime.today().year
        self.month = datetime.today().month

        self.resize(QtCore.QSize(850, 600))
        self.setMinimumSize(QtCore.QSize(850, 600))
        self.setStyleSheet(scrollArea_style)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()
        self.init_menu_width = self.ui.frame_left_menu.minimumWidth()
        
        self.show()

    def init_ui(self):
        self.init_flow_layouts()
        self.init_tasks_todo()
        self.init_tasks()
        self.init_month_statistics()
        self.init_effects()
        self.connect_buttons()
        self.compare_accomplished_tasks_statistics()

        self.ui.Pages_Widget.setCurrentWidget(self.ui.page_show_tasks)
        self.ui.day_field.setValidator(QtGui.QIntValidator())

    def init_flow_layouts(self):
        # flow layouts need to be initialized by code
        layout = FlowLayout()
        widget = self.ui.tasks_todo_widget
        widget.setLayout(layout)

    def init_effects(self):
        add_shadow_effect(self.ui.frame_left_menu)
        add_shadow_effect(self.ui.task_overview)
        add_shadow_effect(self.ui.history)
        add_shadow_effect(self.ui.tasks_todo)
        add_shadow_effect(self.ui.add_task_widget)
        add_shadow_effect(self.ui.widget_2)
        add_shadow_effect(self.ui.highlights_widget)
        add_shadow_effect(self.ui.effect_test_2, 5)

    def connect_buttons(self):
        self.ui.Btn_Menu_2.clicked.connect(lambda: self.change_page(self.ui.page_add_task))
        self.ui.Btn_Menu_1.clicked.connect(lambda: self.change_page(self.ui.page_show_tasks))
        self.ui.Btn_Menu_3.clicked.connect(self.show_statistics)
        self.ui.Button_AddTask.clicked.connect(self.insert_new_task)
        self.ui.button_last_year.clicked.connect(lambda: self.change_calendar_year(-1))
        self.ui.button_next_year.clicked.connect(lambda: self.change_calendar_year(+1))
        self.ui.button_last_month.clicked.connect(lambda: self.change_tasks_month(-1))
        self.ui.button_next_month.clicked.connect(lambda: self.change_tasks_month(+1))
        self.ui.button_last_month_2.clicked.connect(lambda: self.change_tasks_month(-1))
        self.ui.button_next_month_2.clicked.connect(lambda: self.change_tasks_month(+1))
    
    def custom_context_menu(self, event):
        contextMenu = QMenu(self)
        delete = contextMenu.addAction("Delete")
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

        # delete label on todo tasks
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

        new_end_date = datetime.now() - timedelta(days=1)
        new_days = (new_end_date - datetime.strptime(task[4],  "%Y-%m-%d")).days
        # convert to date
        new_end_date = new_end_date.date()
        self.db_task.update_row(id, task[1], new_days, task[3], task[4], new_end_date, task[6])

        # delte task from task todo bar
        self.update_tasks_todo(id, 1)
        # delete task from task overview
        sender.deleteLater()
        # insert task with updated parameters
        self.update_task_overview(id, task[1], new_days, task[3], new_end_date, task[6])

    def change_page(self, page):
        self.ui.Pages_Widget.setCurrentWidget(page)

    def toggle_menu(self, max_width):
        current_width = self.ui.frame_left_menu.width()
        end_width = self.init_menu_width
        if current_width == self.init_menu_width:
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
        differences = {task[0]: (datetime.strptime(task[4],  "%Y-%m-%d") - datetime.strptime(oldest_start_date,  "%Y-%m-%d")).days for task in current_tasks}
        # id of check bar for today (with respect to the oldest current task)
        today_day_id = (datetime.today() - datetime.strptime(oldest_start_date,  "%Y-%m-%d")).days
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
            if label:
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

        start_date = date.today()
        rnd_color = get_random_color()
        task_id = self.db_task.insert_task(name_input, days_input, duration_input, start_date, rnd_color)

        # insert new task into ui
        self.update_task_overview(task_id, name_input, days_input, duration_input, start_date, rnd_color)

        self.update_tasks_todo(task_id, 0)
        self.change_page(self.ui.page_show_tasks)

    def update_task_overview(self, task_id, name, days, duration, start, color):
        # get current scrollArea
        scrollArea = self.task_overviews_per_month[self.month-1]

        # add new task to task overview
        task_widget = create_task_widget(self, task_id, name, days, duration, start, color, self.year, self.month)
        self.widget_task_ids[task_widget] = task_id
        scrollArea.widget().layout().addWidget(task_widget)

    def init_tasks(self):
        self.setStyleSheet(scrollArea_style)
        scrollArea = self.task_overviews_per_month[self.month-1]

        # show month name
        month_name = calendar.month_abbr[self.month]
        self.ui.month_label.setText("{} {}".format(month_name, str(self.year)[-2:]))

        if scrollArea:
            scrollArea.setVisible(True)
        else:
            scrollArea = QScrollArea()
            self.ui.task_overview.layout().addWidget(scrollArea)
            new_widget = QWidget()
            scrollArea.setWidget(new_widget)
            scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            scrollArea.setWidgetResizable(True)

            layout = FlowLayout()
            new_widget.setLayout(layout)
            layout.setSpacing(10)

            self.task_overviews_per_month[self.month-1] = scrollArea

            sql_end_date = date(self.year, self.month, 1)
            sql_start_date = add_delta_month_datetime(self.year, self.month, 1, 1).date()
            tasks = self.db_task.sql_query("SELECT * FROM tasks WHERE startDate < strftime('%Y-%m-%d', '{}') and endDate >= strftime('%Y-%m-%d', '{}')".format(sql_start_date, sql_end_date))
            if not tasks:
                return
            tasks.sort(key=lambda x: x[2], reverse=True)

            for task in tasks:
                task_end_date = datetime.strptime(task[4],  "%Y-%m-%d") 
                task_widget = create_task_widget(self, task[0], task[1], task[2], task[3], task_end_date.date(), task[6], self.year, self.month)
                self.widget_task_ids[task_widget] = task[0]
                layout.addWidget(task_widget)
    
    def compute_tasks_count_quantiles(self):
        res = self.db_joint.sql_query("SELECT date, count(task_id) FROM data_joint WHERE check_number != 0 GROUP BY date")
        if not res:
            return [], []
        tasks_per_day = {x[0]: x[1] for x in res}
        quantiles = np.quantile(list(tasks_per_day.values()), [0.25, 0.5, 0.75, 1.0])

        return quantiles, tasks_per_day

    def compare_accomplished_tasks_statistics(self):
        this_month_end = datetime.now()
        last_month_begin = add_delta_month_datetime(this_month_end.year, this_month_end.month, 1, -1)

        accomplished = self.db_joint.sql_query("""SELECT strftime(\"%m-%Y\", date), ifnull(count(*),0) 
                                FROM data_joint 
                                WHERE check_number > 0 AND date >= strftime('%Y-%m-%d', '{}') AND date <= strftime('%Y-%m-%d', '{}') 
                                GROUP BY strftime(\"%m-%Y\", date)""".format(last_month_begin, this_month_end))

        total = self.db_joint.sql_query("""SELECT strftime(\"%m-%Y\", date), ifnull(count(*),0) 
                                FROM data_joint 
                                WHERE check_number != -1 AND day_id >= 0 AND date >= strftime('%Y-%m-%d', '{}') AND date <= strftime('%Y-%m-%d', '{}') 
                                GROUP BY strftime(\"%m-%Y\", date)""".format(last_month_begin, this_month_end))

        accomplished = dict(accomplished)
        total = dict(total)

        last_month_str = datetime.strftime(last_month_begin, "%m-%Y")
        this_month_str = datetime.strftime(this_month_end, "%m-%Y")

        percentage_last_month = accomplished.get(last_month_str, 0) / total.get(last_month_str, 1)
        percentage_this_month = accomplished.get(this_month_str, 0) / total.get(this_month_str, 1)
        highlights_text = []

        if percentage_last_month:
            accomplished_dif = percentage_this_month - percentage_last_month
            month_dif = accomplished_dif / percentage_last_month
            month_dif_text = interpret_accomplished_tasks_month_difference(month_dif)
            highlights_text.append(month_dif_text)
        
        accomplished_tasks_text = interpret_accomplished_tasks_percentage(accomplished.get(this_month_str, 0), total.get(this_month_str, 0))
        highlights_text.append(accomplished_tasks_text)

        self.ui.textBrowser.setText(" ".join(highlights_text))

        y = [percentage_last_month * 100, percentage_this_month * 100]
        x = [calendar.month_abbr[last_month_begin.month], calendar.month_abbr[this_month_end.month]]
        sc = MplCanvas(width=4, height=3, dpi=100)
        sc.axes.barh(x, y, height=0.4, color="#dde6f6")
        sc.axes.xaxis.set_visible(False)

        # new_patches = []
        # for patch in reversed(sc.axes.patches):
        #     bb = patch.get_bbox()
        #     color=patch.get_facecolor()
        #     p_bbox = FancyBboxPatch((bb.xmin, bb.ymin), abs(bb.width), abs(bb.height), 
        #                             boxstyle="round,pad=0.0040,rounding_size=0.10", 
        #                             ec="none", fc=color, mutation_aspect=5)
        #     patch.remove()
        #     if bb.height == 0:
        #         new_patches.append(patch)
        #     else:
        #         new_patches.append(p_bbox)
        # for patch in new_patches:
        #     sc.axes.add_patch(patch)
        # sc.fig.tight_layout()

        sc.setFixedHeight(100)
        self.ui.widget_8.layout().insertWidget(0, sc)


    def init_month_statistics(self):
        month_name = calendar.month_abbr[self.month]
        self.ui.month_label_2.setText("{} {}".format(month_name, str(self.year)[-2:]))

        end_date = add_delta_month_datetime(self.year, self.month, 1, 1)
        start_date = add_delta_month_datetime(self.year, self.month, 1, -5)

        res = self.db_joint.sql_query("""SELECT strftime(\"%m-%Y\", date), ifnull(count(*),0) 
                                        FROM data_joint 
                                        WHERE check_number > 0 AND date >= strftime('%Y-%m-%d', '{}') AND date < strftime('%Y-%m-%d', '{}') 
                                        GROUP BY strftime(\"%m-%Y\", date)""".format(start_date, end_date))

        res = dict(res)
        x =  []
        y = []

        for i in reversed(range(6)):
            current_date = add_delta_month_datetime(self.year, self.month, 1, -i).date()
            x.append(calendar.month_abbr[current_date.month])
            current_date = current_date.strftime('%m-%Y')

            if current_date in res:
                y.append(res[current_date])
            else:
                y.append(0)

        sc = MplCanvas(width=5, height=4, dpi=100)
        sc.axes.bar(x, y, width=0.8, color="#dde6f6")
        max_y_lim = 10 + max(y)//10 * 10
        sc.axes.set_ylim(0, max_y_lim)
        new_patches = []
        for patch in reversed(sc.axes.patches):
            bb = patch.get_bbox()
            color=patch.get_facecolor()
            p_bbox = FancyBboxPatch((bb.xmin, bb.ymin), abs(bb.width), abs(bb.height), 
                                    boxstyle="round,pad=0.0040,rounding_size={}".format(0.002*max_y_lim), 
                                    ec="none", fc=color, mutation_aspect=10)
            patch.remove()
            if bb.height == 0:
                new_patches.append(patch)
            else:
                new_patches.append(p_bbox)
        for patch in new_patches:
            sc.axes.add_patch(patch)
        sc.fig.tight_layout()
        sc.setFixedHeight(300)
        self.ui.monthsplot.layout().itemAt(0).widget().deleteLater()
        self.ui.monthsplot.layout().insertWidget(0, sc)

    def show_statistics(self):
        if self.ui.calendar.count() < 1:
            # create new calendar
            self.create_calendar_statistics()
        else:
            # update calendar if there already exists one
            self.update_calendar_statistics()

        # show statistics page
        self.change_page(self.ui.page_statistics)

    def change_tasks_month(self, i):
        widget = self.task_overviews_per_month[self.month-1]
        widget.setVisible(False)

        self.year, self.month = add_delta_month(self.year, self.month, i)

        self.init_tasks()
        self.init_month_statistics()

    def change_calendar_year(self, i):
        # change year if updated year is not in the future
        current_year = datetime.today().year
        year = self.year + i
        self.year = year if year <= current_year else current_year
        self.ui.year_label.setText("{}".format(self.year))
        # update shown calendar using the updated year
        self.update_calendar_statistics()

    def update_calendar_statistics(self):
        # delete old calendar
        for i in range(self.ui.calendar.count()):
            self.ui.calendar.itemAt(i).widget().deleteLater()
        # create new one
        self.create_calendar_statistics()

    def create_calendar_statistics(self):
        quantiles, tasks_per_day = self.compute_tasks_count_quantiles()

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
                    current_date = date(self.year, month, day)
                    color = 0
                    try: 
                        count = tasks_per_day[str(current_date)]
                        color = 1
                        for i in range(len(quantiles)-1, 0, -1):
                            if count >= quantiles[i]:
                                color = i+1
                                break
                    except:
                        color = 0

                    current_date = date(self.year, month, day)
                    day_widget = create_calendar_day_widget(self, current_date, count, color)
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
