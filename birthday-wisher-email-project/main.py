import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

import pandas

my_email = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

now = dt.datetime.now()
today_month = now.month
today_day = now.day

birthday_dict = pandas.read_csv("birthdays.csv")

# print(birthday_dict)
for index, row in birthday_dict.iterrows():
    if row["month"] == today_month and row["day"] == today_day:
        randrange_letter = random.randint(1, 4)
        with open(f"letter_templates/letter_{randrange_letter}.txt", "r") as file_read:
            letter = file_read.read()
            letter = letter.replace("[NAME]", row["name"])
        print(letter)
        server = row["email"].split("@")[1].split(".")[0]
        country = row["email"].split("@")[1].split(".")[1]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday\n\n {letter}"
            )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
