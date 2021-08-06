import requests
endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"
#Sheety APi 
sheety_endpoint="https://api.sheety.co/2d92a5c252204c18a3640a53ff736fc6/myWorkouts/workouts"
sheety_post_endpoint="https://api.sheety.co/2d92a5c252204c18a3640a53ff736fc6/myWorkouts/workouts"
# Nutrition API fetching
header={
  "x-app-id":"[APP_ID]",
  "x-app-key":"[APP KEY]",
 
}
para={
  
"query":input("Enter your exercise?"),

}
response=requests.post(url=endpoint,json=para,headers=header)
print(response.json())
data=response.json()
#getting date and time
from datetime import date,datetime
now=date.today()
date_today=now.strftime("%d/%m/%Y")
now=datetime.now()
time_today=now.strftime("%H:%M:%S")
headers = {
	"Content-Type": "application/json",
}
i=0
for items in data['exercises']:
        i=i+1
        exercise_name=items['name'].title()
        duration=items['duration_min']
        calories=items['nf_calories']
        para2={
         "workout":
           {
            "date":date_today,
            "time":time_today,
            "exercise":exercise_name,
            "duration":duration,
            "calories": calories,

             }
          
         }
        
        print(para2)
       
        response=requests.post(url=sheety_post_endpoint,json=para2)
        print(response.text)


#print(response.text)

# print(time_today)
# {
#   "workouts": [
#     {
#       "date": "21/07/2020",
#       "time": "15:00:00",
#       "exercise": "Running",
#       "duration": 22,
#       "calories": 130,
#       "id": 2
#     }
#   ]
# }
# para2={
#   "workouts":[
#     {
#       data=""
#     }
#   ]
# }
