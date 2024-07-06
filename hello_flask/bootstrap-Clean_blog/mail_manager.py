import os
import smtplib

my_email = os.getenv("MY_EMAIL")
password = os.getenv("MY_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")


def send_email(subject, body):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:{subject}\n\n{body}"
        )
    print("Email sent successfully.")
