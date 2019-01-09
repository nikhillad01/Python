import json
import numpy as np
from typing import Dict, Any

json_data = '{"name": "nikhil", "city": "Mumbai"}'
python_obj = json.loads(json_data)


inventory="""{
    "Rice":
        [
            {"name":"Basmati","Weight":1,"Price":100},
            {"name":"kolam","Weight":1,"Price":60},
            {"name":"tukda","Weight":1,"Price":40},
            {"name":"Brown","Weight":1,"Price":200}
        ],
    "Pulses":
        [
            {"name":"toor","Weight":1,"Price":100},
            {"name":"masoor","Weight":1,"Price":80},
            {"name":"chana","Weight":1,"Price":70},
            {"name":"moog","Weight":1,"Price":10}
        ]
    
}"""


data=json.loads(inventory)          # loads json data from string
#print(data.values())
to_json=json.dumps(data,indent=2,sort_keys=True)   # converts python object to json.

#print(to_json)

with open("/home/admin1/PycharmProjects/BridgeLabzDemo/JSON/inventory.json") as f:
    data=json.load(f)                   # json.load() loads data from file to
print(data)
print("all in one")
new_rice={}
new_wheat={}
new_pulses={}
for r,w,p in zip(data['Rice'],data['Wheat'],data["Pulses"]):
    r_name=r['name']
    r_price=r['Price']
    new_rice[r_name]=r_price

    w_name = w["name"]
    w_price = w["Price"]
    new_wheat[w_name] = w_price

    p_name=p['name']
    p_price=p['Price']
    new_pulses[p_name]=p_price

print()
print("Rice detail ", new_rice)
print("Total Rice items : ", len(new_rice))
print("Total cost of Rice Items : ", sum(new_rice.values()))
print()
print("Wheat detail ", new_wheat)
print("Total Wheat items : ", len(new_wheat))
print("Total cost of Wheat Items : ", sum(new_wheat.values()))
print()
print("Pulses detail ", new_pulses)
print("Total Pulse items : ", len(new_pulses))
print("Total cost of Pulse Items : ", sum(new_pulses.values()))







# with open("/home/admin1/PycharmProjects/BridgeLabzDemo/JSON/inventory2.json",'w') as f_write:
#     json.dump(data,f_write)