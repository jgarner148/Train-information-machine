import requests
import json
import time
from datetime import date

def clear(): #Clears the screen
  print("\n"*99)

def jprint(obj):
    text = json.dumps(obj,sort_keys=True, indent=4)
    print(text)

username = "rttapi_jgarner148"
password = "bdb0d0827ecc3c019db7d44d028166017e995c21"

def info_origin():
  looping = True
  while looping == True:
    train_code = input("What is the trains UID code?: ")
    if len(train_code) == 6:
      get_info = requests.get("http://api.rtt.io/api/v1/json/service/" + train_code + date.today().strftime("%Y %m %d"), auth=(username,password))
      jprint(get_info.json())


info_origin()
#get_info = requests.get("http://api.rtt.io/api/v1/json/service/C19440/2021/01/11", auth=(username,password))
#answer = jprint(response.json()["destination"])
