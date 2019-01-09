import json

from JSON.Commercial_data_processing import commercial_data


def inventory_runner():
    with open('stock.json', 'r') as jf:
        json_str = jf.read()
        jf.close()
        json_value = json.loads(json_str)

    i_obj = commercial_data(json_value)

    i_obj.stock_materials()
    i_obj.see_category()


if __name__ == "__main__":
    inventory_runner()