# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACff730b4d1d4b6b7260570b3d54182a37"
auth_token = "17364ac1ce1abe67b545115b1bc670b3"
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+919653603115',
       # //my phone number
                        from_='+12246430461'
                    )

print(call.sid)
