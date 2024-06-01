import datetime as dt
import random
import smtplib
import pandas

my_email = "zoltan@yahoo.com"
password = "123456789"

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = 1
# start_day = "2024-06-01 00:00:00"
# day_of_birthday = dt.datetime(year=1972, month=11, day=1)
#
# if day_of_week == 1:
#     with open("quotes.txt", "r") as file:
#         all_quote = file.readlines()
#         quote = random.choice(all_quote)
#     print(quote)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="info@aloewebshop.hu",
#             msg=f"Subject:Monday motivation\n\n {quote}"
#         )

##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

now = dt.datetime.now()
today_month = now.month
today_day = now.day

birthday_dict = pandas.read_csv("birthdays.csv")

# print(birthday_dict)
for index, row in birthday_dict.iterrows():
    if row["month"] == today_month and row["day"] == today_day:
        randrange_letter = random.randrange(1, 3)
        with open(f"letter_templates/letter_{randrange_letter}.txt", "r") as file_read:
            letter = file_read.read()
            letter = letter.replace("[NAME]", row["name"])
        print(letter)
        server = row["email"].split("@")[1].split(".")[0]
        country = row["email"].split("@")[1].split(".")[1]
        if server == "gmail":
            server = "gmail"
        elif server == "yahoo":
            server = "mail.yahoo"
        elif server == "hotmail":
            server = "live"
        elif server == "outlook":
            server = "mail.outlook"
        else:
            server = "mail"
        with smtplib.SMTP(f"smtp.{server}.{country}") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday\n\n {letter}"
            )

    # for line in data:
    #     if int(line.split(",")[3]) == today_month and int(line.split(",")[4]) == today_day:
    #         randrange_letter = random.randrange(1, 3)
    #         with open(f"letter_templates/letter_{randrange_letter}.txt", "r") as file_read:
    #             letter = file_read.read()
    #             letter = letter.replace("[NAME]", line.split(",")[0])
    #         print(letter)
    #         with smtplib.SMTP("smtp.gmail.com") as connection:
    #             connection.starttls()
    #             connection.login(user=my_email, password=password)
    #             connection.sendmail(
    #                 from_addr=my_email,
    #                 to_addrs=line.split(",")[2],
    #                 msg=f"Subject:Happy Birthday\n\n {letter}"
    #             )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

