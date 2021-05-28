import singer
import urllib.request
import json
import requests
import os.path
from os import path
from getHist import getHistData
from getCurr import currentData


schema={
    "properties": {
            "sunriseStart": {
              "type": "string",'format': 'date-time'
            },
            "sunriseEnd": {
              "type": "string",'format': 'date-time'
            },
            "sunsetStart": {
              "type": "string",'format': 'date-time'
            },
            "sunsetEnd": {
              "type": "string",'format': 'date-time'
            }
          }
}

datt=[]

#gethistorical
datt=getHistData()
singer.write_schema('pune', schema, 'sunriseStart')
singer.write_records('pune', records=datt)

