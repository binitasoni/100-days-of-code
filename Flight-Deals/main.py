import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from twilio.rest import Client
sheety_endpoint = "https://api.sheety.co/[Endpoint]"
scope = ['https://www.googleapis.com/auth/spreadsheets', 
  'https://www.googleapis.com/auth/drive.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
GS=client.open("Flight Deals")
GoogleSheet=GS.get_worksheet(0)
cityCell = GoogleSheet.find("City")
cities = GoogleSheet.col_values(cityCell.col)
IATACell = GoogleSheet.find("IATA Code")
IATA_codes = GoogleSheet.col_values(IATACell.col)
price=GoogleSheet.find("Lowest Price")
sheet_price = GoogleSheet.col_values(price.col)
# <---Get the cities----->
def DataManager():
       # This function is responsible for talking to the Google Sheet.
    response = requests.get(url=sheety_endpoint)
    prices = response.json()
    return prices
# <---Get the IATA Code----->
def get_iata(city):
     twillo_endpoint=f"https://tequila-api.kiwi.com/locations/query?term={city}&locale=en-US&location_types=airport&limit=10&active_only=true"
     header={
       "apikey":"[YOUR API KEY]"
     } 
     response=requests.get(url=twillo_endpoint,headers=header)
     iata=response.text
     iata_code=(iata[21:24])
     return iata_code

sheet_data=DataManager()
# <---Change the values----->
# for x in range(1, len(cities)):
#     GoogleSheet.update_cell((IATACell.row + x), 
#     IATACell.col, 
#     get_iata(cities[x]))

#<---Search for Flights----->

def get_Flight(city):
     header={
       "apikey":"[YOUR API KEY]"
     } 
     nights_in_dst_from=7
     nights_in_dst_to=28
     e=f"https://tequila-api.kiwi.com/v2/search?fly_from={city}&dateFrom={date_from}&dateTo={date_to}&flight_type=round&nights_in_dst_from={nights_in_dst_from}&nights_in_dst_to={nights_in_dst_to}&curr=GBP"
     response=requests.get(url=e,headers=header)
     flight=response.json()["data"][0]
     return flight
from datetime import timedelta,datetime    
date_from=str(datetime.now().strftime("%d/%m/%Y")).split()[0]
print(date_from)
date_to=str((datetime.now() +timedelta(days=6*30)).strftime("%d/%m/%Y"))
print(date_to.split()[0])

def send_message(message):
   account_sid = "[YOUR KEY]"
   auth_token = "[YOUR KEY]"
   client = Client(account_sid, auth_token)
   message = client.messages \
                .create(
                     body=message,
                     from_="[YOUR KEY]",
                     to="[YOUR KEY]"
                 )
   print(message.status)
for i in range(1,len(cities)-1):
     data=get_Flight(IATA_codes[i])
     price=data["price"]
     origin_city=data["route"][0]["cityFrom"]
     origin_airport=data["route"][0]["flyFrom"]
     destination_city=data["route"][0]["cityTo"]
     destination_airport=data["route"][0]["flyTo"]
     out_date=data["route"][0]["local_departure"].split("T")[0]
     return_date=data["route"][1]["local_departure"].split("T")[0]
     if price<int(sheet_price[i]):
        message=(f"Low price alert! Only {price}$ from {origin_city}-{origin_airport} to {destination_city}-{destination_airport},from {out_date} to {return_date}")
        send_message(message)

