import os
import smtplib

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
recipient_email = os.environ.get("RECIPIENT_EMAIL")


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg="Subject:Hello\n\nThis is the body of my email.")
