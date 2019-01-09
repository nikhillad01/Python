import  json
try:
    with open("stock.json","r") as f:
        data=json.load(f)
    print(data)


    def google(s):
        google={}
        for g in data[s.title()]:
            g_name=g["number of shares"]
            g_price=g["share price"]
            google[g_name]=g_price
            print("Name of share: ",g['name of share'],"Total number of shares: ",g["number of shares"],"Price per share: ",g["share price"])

        print("Value For", s.title(),"Class A, Class B, Class C shares  : ", [k*v for k,v in google.items()])
        print("Total Value of",s.title()," Stock : ",sum([k*v for k,v in google.items()]))


    if __name__ == "__main__":
        print(" Google , Microsoft , Facebook , Honor, Apple , Amazon ")
        l=['google','microsoft','facebook','honor','apple','amazon']
        s = input("Enter company name")
        if s.lower() in l:
            google(s)
        else:print("We don't have records for this company or check spelling")

except Exception as e:
    print(e)