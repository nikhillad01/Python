# import  json
#
# with open("doctor.json","r") as f:
#     s=json.load(f)
# print(s)
# while True:
#     # for i in s["Doctors"]:
#     #     print(i)
#
#     # print()
#     # for i in s["Patients"]:
#     #     print(i)
#     for i in range(len(s['Doctors'])):
#         print(i,s["Doctors"][i])
#     a=input("You want to take an appointment enter ur name ")
#     doctor=int(input("enter Key of Doctor"))
#
#     def add_new_patient():
#
#             """This method adds new company to stock.json"""
#
#             Date=input("Enter suitable date for appointment ")
#             t=input("AM/PM")
#             new_stock_dict = {"Date": Date,
#
#                               "Name": a,
#                               "Time":t}
#
#             with open('../JSON/doctor.json', 'w') as stock_jf:
#                 s['Doctors'][doctor]["patients"].append(new_stock_dict)
#                 stock_jf.write(json.dumps(s,indent=2))
#
#
#
#
#     if len(s['Doctors'][doctor]["patients"])<5:
#         s['Doctors'][0]["patients"].append(a)
#     else:
#         da=int(input("Sorry Appointments are full you want another date ? ."))
#         if da==1:add_new_patient()
#
#
#
#     # print(s['Doctors'][0]["patients"])
#     # s['Doctors'][0]["patients"].append(a)
#     print(s['Doctors'][0]["patients"])
#     # print(len(s['Doctors'][0]["patients"]))