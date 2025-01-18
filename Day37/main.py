import requests
from datetime import datetime


pixela_endpoint = 'https://pixe.la/v1/users'
TOKEN = "your token of pixela"
USERNAME = "your username"
GRAPH_ID = "graph1"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfSerivce": "yes",
    "notMinor" : "yes",
}

# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name": "Cycling Graphs",
    "unit" : "km",
    "type" : "float",
    "color" : "ichou",
}

headers = {
    "X-USER-TOKEN" : TOKEN,

}

# response = requests.post(url = graph_endpoint, json = graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "9.74",

}

# response = requests.post(url = pixel_creation_endpoint, json = pixel_data, headers = headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_data = {
    "quantity" : "4.5",
}

# response = requests.put(url = update_endpoint, json = pixel_data, headers= headers)
# print(response.text)



delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url = delete_endpoint, headers= headers)
print(response.text)