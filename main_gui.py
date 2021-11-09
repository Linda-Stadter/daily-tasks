# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 554)
        MainWindow.setStyleSheet("background-color: rgb(194, 194, 194);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(60, 40))
        self.frame_toggle.setStyleSheet("background-color: #4b4b4b;")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Toggle.setFont(font)
        self.Btn_Toggle.setStyleSheet("\n"
"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4b4b4b;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #465999;\n"
"}")
        self.Btn_Toggle.setText("")
        self.Btn_Toggle.setIconSize(QtCore.QSize(30, 16))
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.verticalLayout_2.addWidget(self.Btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_2 = QtWidgets.QFrame(self.Top_Bar)
        self.frame_2.setStyleSheet("background: rgb(120, 120, 120);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(60, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_left_menu.setAutoFillBackground(False)
        self.frame_left_menu.setStyleSheet("background-color:#4b4b4b;\n"
"padding: 0 0 0 0px;\n"
"margin: 0 0 0 0px;")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Btn_Menu_1 = QtWidgets.QPushButton(self.frame_top_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Menu_1.sizePolicy().hasHeightForWidth())
        self.Btn_Menu_1.setSizePolicy(sizePolicy)
        self.Btn_Menu_1.setMinimumSize(QtCore.QSize(58, 60))
        self.Btn_Menu_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Btn_Menu_1.setAutoFillBackground(False)
        self.Btn_Menu_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4b4b4b;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #e26457;\n"
"}")
        self.Btn_Menu_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/tasks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_1.setIcon(icon)
        self.Btn_Menu_1.setIconSize(QtCore.QSize(34, 34))
        self.Btn_Menu_1.setShortcut("")
        self.Btn_Menu_1.setCheckable(False)
        self.Btn_Menu_1.setFlat(False)
        self.Btn_Menu_1.setObjectName("Btn_Menu_1")
        self.verticalLayout_4.addWidget(self.Btn_Menu_1, 0, QtCore.Qt.AlignBottom)
        self.Btn_Menu_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setMinimumSize(QtCore.QSize(0, 60))
        self.Btn_Menu_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4b4b4b;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #42ab59;\n"
"}rgb(66, 171, 89)")
        self.Btn_Menu_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_2.setIcon(icon1)
        self.Btn_Menu_2.setIconSize(QtCore.QSize(30, 30))
        self.Btn_Menu_2.setObjectName("Btn_Menu_2")
        self.verticalLayout_4.addWidget(self.Btn_Menu_2)
        self.Btn_Menu_3 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_3.setMinimumSize(QtCore.QSize(0, 60))
        self.Btn_Menu_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: #4b4b4b;\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #e2b757;\n"
"}")
        self.Btn_Menu_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/history_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_3.setIcon(icon2)
        self.Btn_Menu_3.setIconSize(QtCore.QSize(34, 34))
        self.Btn_Menu_3.setObjectName("Btn_Menu_3")
        self.verticalLayout_4.addWidget(self.Btn_Menu_3)
        self.label_6 = QtWidgets.QLabel(self.frame_top_menus)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu, 0, QtCore.Qt.AlignLeft)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_pages.setStyleSheet("background-color: #e0dfdf;")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page_show_tasks = QtWidgets.QWidget()
        self.page_show_tasks.setObjectName("page_show_tasks")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_show_tasks)
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tasks_todo = QtWidgets.QFrame(self.page_show_tasks)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tasks_todo.sizePolicy().hasHeightForWidth())
        self.tasks_todo.setSizePolicy(sizePolicy)
        self.tasks_todo.setMinimumSize(QtCore.QSize(500, 0))
        self.tasks_todo.setStyleSheet("background: #fff;")
        self.tasks_todo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tasks_todo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tasks_todo.setObjectName("tasks_todo")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tasks_todo)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label = QtWidgets.QLabel(self.tasks_todo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_10.addWidget(self.label)
        self.tasks_todo_widget = QtWidgets.QWidget(self.tasks_todo)
        self.tasks_todo_widget.setObjectName("tasks_todo_widget")
        self.verticalLayout_10.addWidget(self.tasks_todo_widget)
        self.frame_tasks_today = QtWidgets.QFrame(self.tasks_todo)
        self.frame_tasks_today.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tasks_today.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tasks_today.setObjectName("frame_tasks_today")
        self.verticalLayout_10.addWidget(self.frame_tasks_today)
        self.verticalLayout_6.addWidget(self.tasks_todo)
        self.tasks_widget_rename = QtWidgets.QWidget(self.page_show_tasks)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tasks_widget_rename.sizePolicy().hasHeightForWidth())
        self.tasks_widget_rename.setSizePolicy(sizePolicy)
        self.tasks_widget_rename.setMinimumSize(QtCore.QSize(600, 0))
        self.tasks_widget_rename.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tasks_widget_rename.setObjectName("tasks_widget_rename")
        self.verticalLayout_6.addWidget(self.tasks_widget_rename)
        self.scrollArea = QtWidgets.QScrollArea(self.page_show_tasks)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("QScrollArea {\n"
"                        background: #ffffff;\n"
"                        border: 0px solid;\n"
"}\n"
"\n"
"QScrollBar::vertical {\n"
"                        width: 8px;\n"
"                        margin: 0px 0 0px 0;\n"
"                        background: transparent;\n"
"                      }\n"
"\n"
"                      QScrollBar::handle:vertical {\n"
"                        min-height: 10px;\n"
"                        background: #4b4b4b;\n"
"                        border-radius: 4px;\n"
"                      }\n"
"\n"
"                      QScrollBar::add-line:vertical {\n"
"                        background: transparent;\n"
"                        height: 0px; \n"
"                        subcontrol-position: bottom;\n"
"                        subcontrol-origin: margin;\n"
"                      }\n"
"\n"
"                      QScrollBar::sub-line:vertical {\n"
"                        background: transparent;\n"
"                        height: 0px; \n"
"                        subcontrol-position: top;\n"
"                        subcontrol-origin: margin;\n"
"                      }\n"
"\n"
"                      QScrollBar::up-arrow:vertical { \n"
"                        background: transparent;\n"
"                        height: 0px; \n"
"                      }\n"
"\n"
"                      QScrollBar::down-arrow:vertical {\n"
"                        background: transparent;                        \n"
"                        height: 0px; \n"
"                        width: 40px;\n"
"                      }")
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.tasks_widget = QtWidgets.QWidget()
        self.tasks_widget.setGeometry(QtCore.QRect(0, 0, 758, 385))
        self.tasks_widget.setObjectName("tasks_widget")
        self.scrollArea.setWidget(self.tasks_widget)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.Pages_Widget.addWidget(self.page_show_tasks)
        self.page_add_task = QtWidgets.QWidget()
        self.page_add_task.setObjectName("page_add_task")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_add_task)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.add_task_widget = QtWidgets.QWidget(self.page_add_task)
        self.add_task_widget.setStyleSheet("background: #fff;")
        self.add_task_widget.setObjectName("add_task_widget")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.add_task_widget)
        self.verticalLayout_18.setSpacing(15)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_5 = QtWidgets.QLabel(self.add_task_widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_18.addWidget(self.label_5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.add_task_widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.task_field = QtWidgets.QLineEdit(self.add_task_widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.task_field.setFont(font)
        self.task_field.setObjectName("task_field")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.task_field)
        self.label_3 = QtWidgets.QLabel(self.add_task_widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.day_field = QtWidgets.QLineEdit(self.add_task_widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.day_field.setFont(font)
        self.day_field.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.day_field.setObjectName("day_field")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.day_field)
        self.label_4 = QtWidgets.QLabel(self.add_task_widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.time_field = QtWidgets.QTimeEdit(self.add_task_widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.time_field.setFont(font)
        self.time_field.setObjectName("time_field")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.time_field)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.Button_AddTask = QtWidgets.QPushButton(self.add_task_widget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.Button_AddTask.setFont(font)
        self.Button_AddTask.setObjectName("Button_AddTask")
        self.horizontalLayout_4.addWidget(self.Button_AddTask)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_4)
        self.verticalLayout_18.addLayout(self.formLayout)
        self.verticalLayout_7.addWidget(self.add_task_widget)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.Pages_Widget.addWidget(self.page_add_task)
        self.page_statistics = QtWidgets.QWidget()
        self.page_statistics.setObjectName("page_statistics")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.page_statistics)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.history = QtWidgets.QWidget(self.page_statistics)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history.sizePolicy().hasHeightForWidth())
        self.history.setSizePolicy(sizePolicy)
        self.history.setStyleSheet("background: #fff;")
        self.history.setObjectName("history")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.history)
        self.verticalLayout_17.setSpacing(15)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.history_label = QtWidgets.QLabel(self.history)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history_label.sizePolicy().hasHeightForWidth())
        self.history_label.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.history_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.history_label.setFont(font)
        self.history_label.setObjectName("history_label")
        self.verticalLayout_17.addWidget(self.history_label)
        self.calendar = QtWidgets.QGridLayout()
        self.calendar.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.calendar.setObjectName("calendar")
        self.verticalLayout_17.addLayout(self.calendar)
        self.verticalLayout_16.addWidget(self.history)
        self.widget_2 = QtWidgets.QWidget(self.page_statistics)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_16.addWidget(self.widget_2)
        self.Pages_Widget.addWidget(self.page_statistics)
        self.verticalLayout_5.addWidget(self.Pages_Widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages_Widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TASKS FOR TODAY"))
        self.label_5.setText(_translate("MainWindow", "ADD A TASK"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Number of days"))
        self.label_4.setText(_translate("MainWindow", "Time per day"))
        self.Button_AddTask.setText(_translate("MainWindow", "Okay"))
        self.history_label.setText(_translate("MainWindow", "HISTORY"))
