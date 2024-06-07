import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "mozo190"
TOKEN = "dfg123dsfg15fgdfg5dfg"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
response = requests.post(url=graph_endpoint, json=graph_config, headers={"X-USER-TOKEN": TOKEN})
print(response.text)
#https://pixe.la/v1/users/mozo190/graphs/graph1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": "20210701",
    "quantity": "10.5"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers={"X-USER-TOKEN": TOKEN})
