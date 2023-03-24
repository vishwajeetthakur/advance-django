import requests 
import json 

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    "name" : "vishwa",
    "roll" : 890 , 
    "city" : "new york"
}

json_data = json.dumps(data) # python -- json 
r = requests.post(url=URL, data= json_data) 
response = r.json()
print(response)
