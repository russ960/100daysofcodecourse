import json
import requests
import creds
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token":creds.pixela_token,
    "username":creds.username,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# {"message":"Success. Let's visit https://pixe.la/@russ960 , it is your profile page!","isSuccess":true}
# response = requests.post(pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{creds.username}/graphs"
headers = {
    "X-USER-TOKEN":creds.pixela_token
}
graph_config = {
    "id":"graph1",
    "name":"Coding Graph",
    "unit":"Minutes",
    "type":"int",
    "color":"sora"
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
graph_id = graph_config["id"]
add_pixel_endpoint = f"{pixela_endpoint}/{creds.username}/graphs/{graph_id}"
entry_date = datetime.utcnow().strftime("%Y%m%d")

quantity = 60
pixel_values = {
    "date": entry_date,
    "quantity":str(quantity)
}
# response = requests.post(url=add_pixel_endpoint,json=pixel_values,headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{creds.username}/graphs/{graph_id}/20220404"
pixel_update_values = {
    "quantity":"35"
}
# response = requests.put(url=update_pixel_endpoint,json=pixel_update_values,headers=headers)
response = requests.delete(url=update_pixel_endpoint,headers=headers)
print(response.text)