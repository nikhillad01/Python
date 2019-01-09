import json
from DSA.Linked_list import linked_list
l=linked_list()
class stock_linked_list:

    def linked_list_stock(self):
        with open('/home/admin1/PycharmProjects/BridgeLabzDemo/JSON/stock.json', "r") as f:
            f = json.load(f)
        print(type(f))

        for i in f["Stock Report"]:
            #print(i)
            #print(type(i))
            l.add(i)
            #{'Stock Name': 'Google', 'Number of Share': 26, 'Share Price': 1000}
        #how_many_companies=int(input("How many companies"))
        l.display()
        comp_name=input("Stock/comp name")
        no_of_share=int(input("No of shares "))
        price_per_share=int(input("price per share : "))

        new_comp={'Stock Name':comp_name,
                  'Number of Share':no_of_share,
                  'Share Price':price_per_share}
        l.add(new_comp)
        #l.delete("{'Stock Name': 'Google', 'Number of Share': 26, 'Share Price': 1000}",l)
        e=l.display()
        print(e)
        d={"Stock Reoport":[]}
        for j in e:

            #d["Stock Report"].append(j)
            print("aaaa",j)
            d["Stock Reoport"].append(j)
        #print("Dicttt",d)
        print("Dict : ",d)
        json_dict=json.dumps(d,indent=2)
        print(json_dict)
s=stock_linked_list()
s.linked_list_stock()