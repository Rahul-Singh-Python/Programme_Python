import twilio

from twilio.rest import Client
import random


otp = random.randint(1000,9999)
print("Your OTP is - ",otp)

account_sid = 'twillow id '
auth_token = 'twillow token'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hello Mr. Mayur Your Secure Device OTP is - ' + str(otp) + ' now your mobile is hacked!\n Byby...',
         from_='twillow Number',
         to='send another person Number'
     )

# print(message.sid)


user = int(input("Enter the Number: "))

if otp == user:
	print("User Granted.....")
else:
	print("User Denied......")
