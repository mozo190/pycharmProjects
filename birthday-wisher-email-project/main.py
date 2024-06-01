import smtplib
import datetime as dt

my_email = "mozo@gamil.com"
password = "123456789"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="info@aloewebshop.hu",
        msg="Something happening this week."
    )

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

day_of_birthday = dt.datetime(year=1972, month=11, day=1)
if year == 2024:
    print(day_of_birthday)
