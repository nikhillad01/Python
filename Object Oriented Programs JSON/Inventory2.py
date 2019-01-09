
import json

with open("/home/admin1/PycharmProjects/BridgeLabzDemo/JSON/inv2.json") as f:
    data=json.load(f)
print(data)
rice={}
wheat={}
pulses={}

print("Available items in our grocery store:")

print("rice :")
for r in data["Rice"]:
    print(r['name'], " Per kg", r['Price'], "Available Kg's", r['quantity'],"kg")
print()
print("Pulses :")
for p in data['Pulses']:
    print(p['name'], " Per kg", p['Price'], "Available kgs  ", p['quantity'],"kg")
print()
print("Wheats :")
for w in data['Wheat']:
    print(w['name'], " Per kg", w['Price'], "Available kgs   ", w['quantity'],"kg")
print()

ch = int(input('You want to add item ??'))


if ch == 1:

    item = input("What item you want to add Rice , Pulses , Wheat ")
    user_requirement=input("Enter name of item ")
    price_per_kg=int(input("enter price per KG"))
    quantity=int(input("Enter total Quantity "))


with open("/home/admin1/PycharmProjects/BridgeLabzDemo/JSON/inv2.json", 'r') as jf:
    json_str = jf.read()
    jf.close()
    json_value = json.loads(json_str)
with open("/home/admin1/PycharmProjects/BridgeLabzDemo/JSON/inv2.json", 'w') as jf:
    json_value[item.title()].append({"name": user_requirement,
                         "Weight": 1,
                         "Price": price_per_kg,
                         "quantity":quantity})
    jf.write(json.dumps(json_value,indent=2))
    jf.close()
