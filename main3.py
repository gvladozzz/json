import json
import requests
from datetime import datetime
for i in range(4):
    response = requests.get("https://api.opensensemap.org/boxes/63bc1c048d17040007f8a58c?format=json&fbclid=IwAR25OyytoVY2tJzBjfkjxl4AHD6ENihRJKn7Z1o1ptWBcKjUOUqV3uzDpYM")
    if response.status_code == 200:
        data = json.loads(response.content)
        if datetime.now().strftime("%d-%m") in data['sensors'][i]['lastMeasurement']['createdAt']:
            print(data['sensors'][i]['lastMeasurement']['value'])
