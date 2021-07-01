api_key='[YOUR API KEY]'
import requests
MY_LAT=19.225809
MY_LONG=72.845100
phone='[PHONE FROM TWILIO]'
parameters={"lat":MY_LAT,
            "lng":MY_LONG,
            "formatted":0}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=-37.813629&lon=144.963058&exclude=current,minutely,alerts&appid=[YOUR API KEY]")
data = response.json()
li=[]
for i in range(12):
 li.append(data['hourly'][i]['weather'][0]['id'])
will_rain=0
for items in li:
  if items<700:
    will_rain=1

import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "[YOUR ACCOUNT SID]"
auth_token = "[YOUR AUTH TOKEN]"



if will_rain==1:  
   client = Client(account_sid, auth_token)
   message = client.messages \
                .create(
                     body="It's going to rain today,bring an umberallaaa!",
                     from_='[FROM PHONE NO]',
                     to='[TO PHONE NO]'
                 )
   print(message.status)
print(li)
