import requests
import time

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
TOKEN = 'asfgouiuiouBUkkdsgu'
USER = 'zubescu'
GRAPH_ID = 'graph1'

user_params = {
    'token': TOKEN,
    'username': 'zubescu',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# {"message":"This user already exist.","isSuccess":false}
# resp = requests.post(url=pixela_endpoint, json=user_params)
# print(resp.text)

GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER}/graphs'

# graph_config = {
#     'id': GRAPH_ID,
#     'name': 'Walking Graph',
#     'unit': 'km',
#     'type': 'float',
#     'color': 'ajisai',
# }

headers = {
    'X-USER-TOKEN': TOKEN
}

# resp = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(resp.text)

PIXEL_CREATION_ENDPOINT = f'{GRAPH_ENDPOINT}/{GRAPH_ID}'

pixel_data = {
    'date': time.strftime('%Y%m%d'),
    'quantity': '5.1',
}

resp = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
print(resp.text)
