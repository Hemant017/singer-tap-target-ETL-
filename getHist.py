# Historical Load : load historical data since 1 Jan 2020

import requests
import json
from datetime import datetime
from datetime import timedelta
from transform_data import transform_data

def getHistData():
# taking input as the date
    Begindatestring = "2020-01-01"
    max_span_days=100
    from datetime import date
    f_date = datetime.strptime(Begindatestring, "%Y-%m-%d")
    l_date = datetime.now()

   #calculated difference
    delta = l_date - f_date
   
    total_days=delta

    # carry out conversion between string to datetime object
    Begindate = datetime.strptime(Begindatestring, "%Y-%m-%d")
    
    # my_data=[]

    my_data={
        "meta":{
        "latitude":"48.8582",
        "longitude":"2.2945",
        "dailyRequestsLimit":50,
        "requestsRemaining":49
    },
        "data":[]
    }


    x=0
    total_days=int(total_days.days)

    #find For multiple of 100 
    if(total_days%max_span_days==0):
        for i in range(0,(total_days//max_span_days)):
            Enddate = Begindate + timedelta(days=max_span_days)
            response = requests.get(
                'https://api.therainery.com/astronomy/sun',
                params={
                    'latitude': 18.51957,
                    'longitude': 73.85535,
                    'start': Begindate,
                    'end': Enddate
                },
                headers={
                    'x-api-key': '7oPjlTt4Nn2NtjrduCIx01UxqIZBShujaHN4OVcc'
                }
            )
            Begindate = Enddate + timedelta(days=1)
            pune_data = json.loads(response.text)
            my_data["data"].extend(pune_data['data'])
            import time
            time.sleep(3)
            x=x+1010
    else:
        # for multiple of 100 and its remainder
        for i in range(0,(total_days//max_span_days)):
            Enddate = Begindate + timedelta(days=max_span_days)
            response = requests.get(
                'https://api.therainery.com/astronomy/sun',
                params={
                    'latitude': 18.51957,
                    'longitude': 73.85535,
                    'start': Begindate,
                    'end': Enddate
                },
                headers={
                    'x-api-key': '7oPjlTt4Nn2NtjrduCIx01UxqIZBShujaHN4OVcc'
                }
            )
            pune_data = json.loads(response.text)
            my_data["data"].extend(pune_data['data'])
            Begindate = Enddate + timedelta(days=1)
            
            
            import time
            time.sleep(3)
            x=x+1
    
        response = requests.get(
            'https://api.therainery.com/astronomy/sun',
            params={
                'latitude': 18.51957,
                'longitude': 73.85535,
                'start': Begindate,
                'end': Begindate+timedelta(days=((total_days%max_span_days)-x-1)  )
            },
            headers={
                'x-api-key': '7oPjlTt4Nn2NtjrduCIx01UxqIZBShujaHN4OVcc'
            }
        )
        pune_data = json.loads(response.text)
        my_data["data"].extend(pune_data['data'])

    return transform_data(json.dumps(my_data["data"]))
#dumps data converted form


