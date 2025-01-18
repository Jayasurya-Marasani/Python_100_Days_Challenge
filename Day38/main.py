import requests
import datetime

GENDER = "YOUR GENDER"
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

APP_ID = "Your APP ID"
API_KEY = "YOUR Nutrition x API KEY"
BEARER_TOKEN = "YOUR SHEETY BEARER TOKEN"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "YOUR SHEETY END POINT"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}
bearer_headers = {
        "Authorization" : f"Bearer {BEARER_TOKEN}"
}
parameters = {
    "query" : exercise_text,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
}


response = requests.post(url = exercise_endpoint, json = parameters, headers= headers)
result = response.json()


today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(url = sheet_endpoint, json = sheet_inputs, headers = bearer_headers) 
    print(sheet_response.text)

    