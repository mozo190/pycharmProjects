import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
if year == 2024:
    print("This is it.")