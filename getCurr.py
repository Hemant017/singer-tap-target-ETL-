from transform_data import transform_data
import requests
import json
from datetime import datetime
from datetime import timedelta

def currentData():
    response = requests.get(
                'https://api.therainery.com/astronomy/sun',
                params={
                    'latitude': 18.51957,
                    'longitude': 73.85535,
                    'start': datetime.now() ,
                    'end': datetime.now()
                },
                headers={
                    'x-api-key': 'DBOKkxrVSD1y3jWkrTviNa8ExHoCoxYQ1w6BYrkV'
                }
            )
    pune_data = json.loads(response.text)
    return transform_data(json.dumps(pune_data["data"]))

# print(currentData())