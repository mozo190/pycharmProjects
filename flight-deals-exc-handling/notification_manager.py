import os

from twilio.rest import Client

twilio_sid = os.environ.get("TWILIO_SID")
twilio_auth = os.environ.get("TWILIO_AUTH")
twilio_phone_from = os.environ.get("TWILIO_PHONE")
twilio_phone_to = os.environ.get("TWILIO_PHONE_2")


class NotificationManager:

    def __init__(self):
        self.client = Client(twilio_sid, twilio_auth)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=twilio_phone_from,
            to=twilio_phone_to
        )
        print(message.sid)
