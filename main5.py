import json
import requests

dict = {}
response = requests.get("https://danepubliczne.imgw.pl/api/data/synop/format/json")
if response.status_code == 200:
    data = json.loads(response.content)
    for i in range(len(data)):
        dict[data[i]['stacja']] = float(data[i]['temperatura'])

print("The lowest temperature in "+str(min(dict, key=dict.get))+", witch is "+str(dict[min(dict, key=dict.get)]))
