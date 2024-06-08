import os

from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ.get("TWILIO_ACCOUNT_SID"), os.environ.get("TWILIO_AUTH_TOKEN"))

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ.get("TWILIO_PHONE_NUMBER"),
            body=message_body,
            to=os.environ.get("MY_PHONE_NUMBER")
        )
        print(message.sid)


# Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
# https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
def send_whatsapp(self, message_body):
    message = self.client.messages.create(
        from_=f'whatsapp:{os.environ.get("WHATSAPP_PHONE_NUMBER")}',
        body=message_body,
        to=f'whatsapp:{os.environ.get("MY_PHONE_NUMBER")}'
    )
    print(message.sid)
