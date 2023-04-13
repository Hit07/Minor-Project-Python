import requests
from datetime import datetime

TOKEN = "hajabsahakaasaas"
USERNAME = "hiteshn"
GRAPH_ID = "graph1"
pixela_endpoint = 'https://pixe.la/v1/users'

user_parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# r = requests.post(pixela_endpoint,json=user_parameter)
# print(r.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_header = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "id": GRAPH_ID,
    "name": "workout",
    "unit": "calory",
    "type": "float",
    "color": "sora"

}

# r = requests.post(url=graph_endpoint,json=graph_params,headers=graph_header)
# print(r.text)

pixel = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(day=12,month=4,year=2023)


pixel_header = {
    "X-USER-TOKEN": TOKEN
}

params = {
    "date":today.strftime('%Y%m%d'),
    "quantity":"150.07",
}

# r = requests.post(url=pixel,headers=pixel_header,json=params)
# print(r.text)