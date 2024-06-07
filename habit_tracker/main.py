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
