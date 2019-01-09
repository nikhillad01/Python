import json

from JSON.Inventory2 import  Inventory


def inventory_runner():
    with open('/home/admin1/PycharmProjects/BridgeLabzDemo/JSON/inv2.json', 'r') as jf:
        json_str = jf.read()
        jf.close()
        json_value = json.loads(json_str)

    i_obj = Inventory(json_value)

    i_obj.inventory_materials()
    i_obj.see_category()


if __name__ == "__main__":
    inventory_runner()