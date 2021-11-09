import datetime

def convert_time(time): 
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
        return "{} = {}".format(query, list.pop())
    return "{} in {}".format(query, tuple(list))