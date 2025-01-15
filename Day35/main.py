import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = "your account sid from twilio"
auth_token = "your auth_token from twilio"
api_key = "your api key from openweathermap.org"


parameters = {
    "lat" : 51.507351,
    "lon" : -0.127758,
    "cnt" : 4,
    "appid" : api_key,
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()["list"][0]["weather"][0]["id"] 

will_rain = False
for hour_data in weather_data["list"]:
    Condition_code = int(hour_data["weather"][0]["id"])
    if Condition_code <= 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid=account_sid, auth_token=auth_token, http_client=proxy_client)
    message = client.messages.create(body = "Its goint to rain today. Bring an Umbrella.",from_="+12057362627", to="+919999999999")
    print(message.status)
