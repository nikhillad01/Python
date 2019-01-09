import  json

with open("doctor.json","r") as f:
    s=json.load(f)
print(s)
while True:
    # for i in s["Doctors"]:
    #     print(i)

    # print()
    # for i in s["Patients"]:
    #     print(i)
    for i in range(len(s['Doctors'])):
        print(i,s["Doctors"][i])
    a=input("You want to take an appointment 1/2 enter ur name ")
    doctor=int(input("enter Key of Doctor"))



    # while i<len(s["Doctors"]):
    #        if s["Doctors"][i]["Name"]==name.title():
    #            index = i
    #      i+=1
    if len(s['Doctors'][0]["patients"])<5:
        s['Doctors'][0]["patients"].append(a)
    else:
        print("Sorry Appointments are full .")

    # print(s['Doctors'][0]["patients"])
    # s['Doctors'][0]["patients"].append(a)
    print(s['Doctors'][0]["patients"])
    # print(len(s['Doctors'][0]["patients"]))