import datetime
import math
from datetime import datetime

def convert_time(time): 
    if type(time) == str:
        time = datetime.strptime(time, "%H:%M")
    if time.hour == 0:
        return "{} min".format(time.minute)
    if time.minute == 0:
        if time.hour == 1:
            return "{} hour".format(time.hour)
        return "{} hours".format(time.hour)
    return "{} h, {} min".format(time.hour, time.minute) 

def format_list_sql_query(query, list):
    if len(list) == 1:
        return "{} = {}".format(query, next(iter(list)))
    return "{} in {}".format(query, tuple(list))

def interpret_accomplished_tasks_month_difference(dif):
    if abs(dif) <= 0.05:
        return "This month you complete as many assigned tasks as last month."
    else:
        comparison = "less" if dif < 0 else "more"
        percentage = round(abs(dif) * 100)
        return "This month you complete <b>{}%</b> {} assigned tasks than last month.".format(percentage, comparison)

def interpret_accomplished_tasks_percentage(accomplished, total):
    if total == 0:
        return "You have not assigned any tasks this month."

    percentage = round(accomplished / total * 100)
    return "You complete <b>{}%</b> of your assigned tasks this month.".format(percentage)

def add_delta_month(year, month, delta_months):
    new_month = (month + delta_months) % 12
    new_month = 12 if new_month == 0 else new_month
    new_year = year
    if delta_months > 0 and new_month < month:
        new_year += 1
    if delta_months < 0 and new_month > month:
        new_year -= 1
    
    if delta_months > 0:
        new_year += abs(delta_months)//12
    if delta_months < 0:
        new_year -= abs(delta_months)//12
    
    return new_year, new_month

def add_delta_month_datetime(year, month, day, delta_months):
    year, month = add_delta_month(year, month, delta_months)
    return datetime(year, month, day)
