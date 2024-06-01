import smtplib
import datetime as dt
import random

my_email = "zoltan@yahoo.com"
password = "123456789"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
start_day = "2024-06-01 00:00:00"
day_of_birthday = dt.datetime(year=1972, month=11, day=1)

#minden nap menjen ki egy levél


if day_of_week == 1:
    with open("quotes.txt", "r") as file:
        all_quote = file.readlines()
        quote = random.choice(all_quote)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="info@aloewebshop.hu",
            msg=f"Something happening this week. {quote}"
        )
