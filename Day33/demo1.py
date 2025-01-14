import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")

# if response.status_code == 404:
#     raise Exception("That resource doesn't exist")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access the data")

response.raise_for_status()

data = response.json()

print(data)
print(data["iss_position"])
print(data["iss_position"]["latitude"])
print(data["iss_position"]["longitude"])

iss_position = (data["iss_position"]["longitude"], data["iss_position"]["latitude"])

print(iss_position)