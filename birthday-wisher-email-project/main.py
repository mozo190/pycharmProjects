import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

day_of_birthday = dt.datetime(year=1972, month=11, day=1)
if year == 2024:
    print(day_of_birthday)
