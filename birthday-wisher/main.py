import smtplib
my_email="binitasonitest@gmail.com"
password="2018Bini!"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email,to_addrs="binitasoni536@gmail.com",msg="Hello imma from pyth0n")
connection.close()
import random
import datetime
list=[]
with open("/Users/anupamsarfare/Downloads/Birthday Wisher (Day 32) start/quotes.txt","r") as f:
    list=[line for line in f.readlines()]
    #print(list)

now=datetime.datetime.now()
day=now.weekday()
print(day)
message=random.choice(list)
print(message)
if day==0:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="binitasoni536@gmail.com", msg=f"Subject:Motivation\n\n{str(message)}")
    connection.close()