import os
import smtplib

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
recipient_email = os.environ.get("RECIPIENT_EMAIL")
# sign = "Best regards,\n\nMolnar Zoltan\nPhone: +36 309 776 039"

# subject = "Hello dear Zoltan\n\n"
# customer_name = "Dear Zoltan,"
# message = "This is the body message of the email."
# body = f"{customer_name}\n\n{message}\n\n{sign}"


def send_email(subject, body):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:{subject} {body}"
        )
    print("Email sent successfully.")
