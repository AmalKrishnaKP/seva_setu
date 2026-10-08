import os
from twilio.rest import Client


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
api_key = os.environ["TWILIO_API_KEY"]
api_secret = os.environ["TWILIO_API_SECRET"]


client = Client(api_key, api_secret, account_sid)
def setup():
    service = client.verify.v2.services.create(
        friendly_name="My First Verify Service"
    )
    return  service.sid

# print(service.sid)

def otp_send(phone):
    verification = client.verify.v2.services(
        "VA00e091649a83bfd056858a8d346cee4f"
    ).verifications.create(to=phone, channel="sms")

    return verification.status
def verifi(phone,otp):
    verification_check = client.verify.v2.services(
        "VA00e091649a83bfd056858a8d346cee4f"
    ).verification_checks.create(to=phone, code=otp)

    return  verification_check.status



