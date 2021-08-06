# <----------Sending Email---------->
import smtplib


def send_email(message):
  my_email="[YOUR KEY]"
  password="[YOUR KEY]"
  receiver_email="[YOUR KEY]"
  print("Sending mail rn!")
  connection=smtplib.SMTP("smtp.gmail.com")
  connection = smtplib.SMTP("smtp.gmail.com")
  connection.starttls()
  connection.login(user=my_email, password=password)
  connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=message)
  print("mail sent!")
  connection.close()
# <----------Web scraping---------->
import requests
from bs4 import BeautifulSoup
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
url="https://www.amazon.com/dp/B00FLYWNYQ/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B00FLYWNYQ&pd_rd_w=MiHMW&pf_rd_p=085568d9-3b13-4ac1-8ae4-24a26c00cb0c&pd_rd_wg=axZCX&pf_rd_r=2385RCDCGS7WFS2ANXYW&pd_rd_r=1fb24595-1e69-42e7-b706-ec311e4e0203&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFVMUFNVjZFR1lVVjMmZW5jcnlwdGVkSWQ9QTA1ODcyNzAyU1Q0RDVVNFFBQUxUJmVuY3J5cHRlZEFkSWQ9QTAwNjA1NjIzMERRVFRTU0c2WVBWJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
response=requests.get(url=url,headers=headers)
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage,"html.parser")
texts=soup.find(class_="a-size-medium a-color-price priceBlockBuyingPriceString")
print(soup.title.string)
price=float(texts.getText()[1:])
print(price)
title=soup.find(class_="a-size-large product-title-word-break").getText()
check_price=88.00
if price<check_price:
   message=f"Alert Price is low for this item:\nProduct Name: {soup.title.string}\nPrice: {price}"
   send_email(message.encode('utf-8'))
