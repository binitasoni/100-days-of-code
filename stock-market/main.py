STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"



import requests
from twilio.rest import Client
response = requests.get(url="https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TSLA&apikey=[YOUR API KEY]")
data = response.json()
print(data)
percent=float(data['Global Quote']['10. change percent'][:-1])

response = requests.get(url="https://newsapi.org/v2/top-headlines?q=Tesla&apiKey=[YOUR API KEY]")
data = response.json()
Headline=data['articles'][0]['title']
brief=data['articles'][0]['content']
message=(f"TSLA: 🔺 {percent} \nHeadline:{Headline}\nBrief:{brief}")
print(message)

account_sid = "[YOUR SID]"
auth_token = "[YOUR AUTH TOKEN]"


if percent>=5 or percent<=5:
   client = Client(account_sid, auth_token)
   message = client.messages \
                .create(
                     body=message,
                     from_='+15153293408',
                     to='[TO NUMBER]'
                 )
   print(message.status)



