import datetime

def convert_time(time): 
    if type(time) == str:
        time = datetime.datetime.strptime(time, "%H:%M")
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

def interpret_accomplished_tasks_difference(dif):
    if abs(dif) <= 0.05:
        return "This month you complete as many assigned tasks as last month."
    else:
        comparison = "less" if dif < 0 else "more"
        return "This month you complete {}% {} assigned tasks than last month.".format(round(abs(dif)*100), comparison)