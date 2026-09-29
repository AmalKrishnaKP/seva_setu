from twilio.rest import Client
import os


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

def opt_send():
    verification = client.verify.v2.services(
        "VA00e091649a83bfd056858a8d346cee4f"
    ).verifications.create(to="+919539040358", channel="sms")

    return verification.status
def verifi(code):
    verification_check = client.verify.v2.services(
        "VA00e091649a83bfd056858a8d346cee4f"
    ).verification_checks.create(to="+919539040358", code=code)

    return  verification_check.status



