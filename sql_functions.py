import datetime
import sqlite3

class SQLConnection():
    def __init__(self, db_name):
        self.db_name = db_name
        return
    
    def sql_query_commit(self, query):
        connection = sqlite3.connect("{}.db".format(self.db_name))
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        connection.commit()
        c.close()
        connection.close()
        return result

    def sql_query(self, query):
        """Performs query on database db_name"""
        connection = sqlite3.connect("{}.db".format(self.db_name))
        c = connection.cursor()
        c.execute(query)
        result = c.fetchall()
        c.close()
        connection.close()
        return result

class SQLTaskConnection(SQLConnection):
    def __init__(self, db_name):
        super().__init__(db_name)
        connection = sqlite3.connect("{}.db".format(self.db_name))
        c = connection.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            taskName TEXT NOT NULL,
            days INTEGER,
            duration TEXT,
            startDate timestamp,
            endDate timestamp,
            color TEXT
        )""")
        c.close()
        connection.commit()
        connection.close()

        self.current_id = self.get_current_id()

    def get_current_id(self):
        # has to be called while initializing
        connection = sqlite3.connect("{}.db".format(self.db_name))
        c = connection.cursor()
        c.execute("SELECT id FROM tasks")
        result = c.fetchall()
        result.sort(reverse=True)
        current_id = result[0][0] if result else 0
        c.close()
        connection.close()

        return current_id

    def insert_task(self, name, days, duration, start, color):
        """Inserts task into task_data and returns the task id"""
        connection = sqlite3.connect("{}.db".format(self.db_name))
        c = connection.cursor()
        endDate = start + datetime.timedelta(days=days)
        # works only with sqlite 3.5 or higher
        # id = c.execute("INSERT INTO tasks VALUES (null, ?, ?, ?, ?, ?) RETURNING id", (name, days, duration, start, endDate))
        self.current_id += 1
        c.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?)", (self.current_id, name, days, duration, start, endDate, color))
        connection.commit()
        connection.close()

        return self.current_id
    
    def update_row(self, task_id, taskName, days, duration, startDate, endDate, color):
        """Updates a task in task_data"""
        connection = sqlite3.connect("{}.db".format(self.db_name))
        c = connection.cursor()
        values = {"task_id": task_id, "taskName": taskName, "days": days, "duration": duration, "startDate": startDate, "endDate": endDate, "color": color}
        c.execute("UPDATE tasks SET taskName=:taskName, days=:days, duration=:duration, startDate=:startDate, endDate=:endDate, color=:color WHERE id=:task_id", values)
        connection.commit()
        connection.close()

class SQLJointConnection(SQLConnection):
    def __init__(self, db_name):
        super().__init__(db_name)
        connection = sqlite3.connect("{}.db".format(self.db_name))
        c = connection.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS data_joint (
            task_id INTEGER,
            day_id INTEGER,
            check_number INTEGER,
            date timestamp,
            PRIMARY KEY (task_id, day_id)
        )""")
        c.close()
        connection.commit()
        connection.close()

    def insert_or_update(self, task_id, day_id, checked, date):
        connection = sqlite3.connect("{}.db".format(self.db_name))
        c = connection.cursor()
        c.execute("INSERT OR IGNORE INTO data_joint (task_id, day_id, check_number, date) VALUES (?, ?, ?, ?)", (task_id, day_id, checked, date))
        c.execute("UPDATE data_joint SET check_number = {} WHERE task_id = {} and day_id = {}".format(checked, task_id, day_id))
        c.close()
        connection.commit()
        connection.close()
        connection.close()
