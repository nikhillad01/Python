#
# import json
#
#
# class CliniqueManagement:
#
#     def __init__(self):
#         pass
#
#     def getUserInput(self):
#         """
#          This method is to take the input from user
#         """
#         print()
#         print("------Welcome to Clinique------")
#         print()
#         ch = input("Press : y/n to continue or exit:")
#         while ch == 'y':
#             print(" \n 1.Doctor Options  \n 2.For Patient options ? \n 3.Exit")
#             choice = int(input("Enter your choice:"))
#             if choice == 1:
#                 print("\n 1.Add Doctor \n 2.View Doctors \n 3.Exit")
#                 ch1 = int(input("Enter your choice:"))
#                 if ch1 == 1:
#                     self.add_doctors()
#                 elif ch1 == 2:
#                     self.view_doctors()
#                 elif ch1 == 3:
#                     break
#                 else:
#                     print("!!..Invalid choice..!!")
#                     break
#             elif choice == 2:
#                 print("\n 1.Add Appointment \n 2.Search Doctor \n 3.Exit")
#                 ch2 = int(input("Enter your choice:"))
#                 if ch2 == 1:
#                     self.addAppointment()
#                 elif ch2 == 2:
#                     print("\n 1.Search Doctor by Name \n 2.Search Doctor Id \n 3.Search Doctor Specialization \n 4.Exit")
#                     ch3=int(input("Enter your choice:"))
#                     if ch3 == 1:
#                         self.searchDoctorbyName()
#                     elif ch3 == 2:
#                         self.searchDoctorbyId()
#                     elif ch3 == 3:
#                         self.search_doctor_by_Specialization()
#
#
#                 elif ch2 == 3:
#                     break
#                 else:
#                     print("!!..Invalid choice..!!")
#                     break
#             elif choice == 3:
#                 break
#             else:
#                 print("!!!..Invalid choice..!!!")
#                 break
#
#     def readJsonfileofDoctor(self):
#         """
#          This method is to create the json file which contain information about doctors
#         :return: it return doctor file in the form of dictionary
#         """
#         # doctors_information = {
#         #             "doctor": [{
#         #                             "Name": "Dr.Arman Singh",
#         #                             "Id": 101,
#         #                             "specialization": "Cardiologist",
#         #                             "Availability": "AM"
#         #                         },
#         #                         {
#         #                             "Name": "Dr.Shital Patil",
#         #                             "Id": 102,
#         #                             "specialization":"Neurologist",
#         #                             "Availability": "PM"
#         #                         },
#         #                         {
#         #                             "Name": "Dr.Varun Shaha",
#         #                             "Id": 103,
#         #                             "specialization": "Addiction psychiatrist",
#         #                             "Availability": "AM"
#         #
#         #                         }]
#         #                        }
#
#         with open('Doctors_info.json', 'r') as file_obj:
#             json_str = file_obj.read()
#             # loads the data and convert it into dictionary format
#
#             json_value = json.loads(json_str)
#
#             file_obj.close()
#
#         return json_value
#
#     def read_Json_file_of_Patient(self):
#         """
#          This method is to create the json file which contain information about patient
#         :return: it returns file of patient in form of dictionary
#         """
#         patient_information = {
#             "patient":[{
#                     "Name": "sahil sharma",
#                     "Id": 12,
#                     "Age": 24,
#                     "mobile number": "7865232419"
#                      },
#                     {
#                     "Name": "pratik Patil",
#                     "Id": 12,
#                     "Age": 34,
#                     "mobile number": "8956345213"
#                      },
#                     {
#                     "Name": "sampada dagwar",
#                     "Id": 14,
#                     "Age": 21,
#                     "mobile number": "9420036520"
#
#                     },
#
#                    {
#                     "Name": "nidhi kamath",
#                     "Id": 15,
#                     "Age": 22,
#                     "mobile number": "8976348562"
#
#                    }]
#          }
#         # convert python dictionary to json format string
#         s = json.dumps(patient_information)
#         # open json file to write
#         with open('Patient_info.json', 'w') as file_obj:
#             file_obj.write(s)
#
#         # open json file to read
#         with open('Patient_info.json', 'r') as file_obj:
#             json_str = file_obj.read()
#             # loads the data and convert it into dictionary format
#             json_value = json.loads(json_str)
#
#         file_obj.close()
#
#         return json_value
#
#
#
#     def readJsonfileofAppoinment(self):
#         """
#          This method is to create the json file which contain all information about patients appointment
#         :return: it returns appointment file in the form of dictionary
#         """
#         appoinment_information = {
#             "Dr.Arman Singh":[{"patient Name": "Nikhil lad","Id": 12,"Age": 24,"mobile number": "7865232419", "time":"AM"},
#                               {"patient Name": "pushkar ishware","Id": 12,"Age": 34,"mobile number": "8956345213", "time":"AM"}],
#             "Dr.Shital Patil":[{"patient Name": "jhanvi mhatre","Id": 14,"Age": 21,"mobile number": "9420036520", "time":"PM"}],
#             "Dr.Varun Shaha":[{"patient Name": "shazad shaikh", "Id": 15,"Age": 22,"mobile number": "8976348562" ,"time":"AM"}],
#             "Dr. Amit Joshi": [{"patient Name": "sagar kadam","Id": 12,"Age": 34,"mobile number": "8956345213", "time":"AM"}]}
#
#         # convert python dictionary to json format string
#         s = json.dumps(appoinment_information)
#         # open json file to write
#         with open('appoinment_info.json', 'w') as file_obj:
#             file_obj.write(s)
#
#         # open json file to read
#         with open('appoinment_info.json', 'r') as file_obj:
#             json_str = file_obj.read()
#             # loads the data and convert it into dictionary format
#             json_value = json.loads(json_str)
#
#         file_obj.close()
#
#         return json_value
#
#
#     def add_doctors(self):
#         """
#          This method is to add new entery doctor
#         """
#         doctor_name=input("Enter Name:")
#         doctor_id=int(input("Enter Id:"))
#         specilization=input("Enter Specialization:")
#         availability=input("Enter Availability(AM/PM/Both):")
#
#         with open('Doctors_info.json', 'r') as file_obj:
#             # open json file to read
#             json_str = file_obj.read()
#             # loads the data and convert it into dictionary format
#             new_json_value = json.loads(json_str)
#
#         # add new entry
#         new_dict={"Name": doctor_name , "Id": doctor_id, "specialization": specilization, "Availability": availability}
#
#         # open json file to write
#         with open('Doctors_info.json', 'w') as file_obj:
#             new_json_value["doctor"].append(new_dict)
#             # convert python dictionary to json format string
#             file_obj.write(json.dumps(new_json_value,indent=2))
#
#
#     def view_doctors(self):
#         """
#          This method is to display all available doctors
#         """
#         # call function to read file which returns dictionary
#         doctor_dict=self.readJsonfileofDoctor()
#         # store list of json file in new list doctor_list
#         doctor_list=doctor_dict["doctor"]
#
#
#         print("Available Doctors are:")
#         print("----------------------------------------")
#         print("Name                    specialization ")
#         print("----------------------------------------")
#
#         # traverse doctor file
#         for i in range(len(doctor_list)):
#             name = doctor_list[i]["Name"]
#             specialization = doctor_list[i]["specialization"]
#
#             print(name, "          ",specialization)
#
#     def addAppointment(self):
#         """
#          This method is to take appointment by patient
#         """
#         print("Name of doctors")
#         print("---------------")
#         # call function to read file which returns dictionary
#         doctor_dict = self.readJsonfileofDoctor()
#         # store list of json file in new list doctor_list
#         doctor_list = doctor_dict["doctor"]
#
#
#         for i in range(len(doctor_list)):
#             name = doctor_list[i]["Name"]
#             specialization=doctor_list[i]["specialization"]
#             Availability=doctor_list[i]['Availability']
#             print(name," ",specialization,' ',Availability)     # using index i prints name of doctor from doctor_list['Name']
#
#
#         doctor_name=input("Name of Doctor to take appointment(i.e Dr. Drake Ramory )??")       # doctor name as input
#         time=input("please Enter appointment time..(AM/PM/Both) :")
#
#         """Logic : Take doctor name as input to take appointment and check only for that doctor if he has more than 5 patients """
#
#         appointment_dict = self.readJsonfileofAppoinment()      # read appointment json.
#         appointment_list = appointment_dict[doctor_name]        # store all patients of 1 doctor in list.
#
#         print("this is appointment list ",appointment_list)
#                                                                 # check each doctor has maximum 5 patient
#         if len(appointment_list) < 5:
#             for i in range(len(doctor_list)):
#                 if doctor_name == doctor_list[i]["Name"]:
#                     if time.upper() == doctor_list[i]["Availability"]:
#                         print("Doctor is available..!! Please Enter the patient details:")
#                         name = input("Enter patient name:")
#                         id = int(input("Enter patient Id:"))
#                         age = int(input("Enter patient age:"))
#                         mob_no = input("Enter patient's mobile number:")
#
#
#                         with open('appoinment_info.json', 'r') as file_obj:
#                             json_str = file_obj.read()
#                                                                 # loads the data and convert it into dictionary format
#                             new_json_value = json.loads(json_str)
#
#                                                                 # add new entry
#                         new_dict = {"patient Name": name ,"Id": id,"Age": age,"mobile number": mob_no, "time":time}
#
#                                                                 # open json file to write
#                         with open('appoinment_info.json', 'w') as file_obj:
#                             new_json_value[doctor_name].append(new_dict)
#                             # convert python dictionary to json format string
#                             file_obj.write(json.dumps(new_json_value,indent=2))
#
#                         print("Your appointment is fixed. Thank You !")
#
#                     else:
#                          print("Sorry. Doctor is not available..!! ")
#
#
#     def searchDoctorbyName(self):
#         """
#          This method is to search the doctor by name to check the availability of doctor
#         """
#         doctor_dict = self.readJsonfileofDoctor()
#         doctor_list = doctor_dict["doctor"]
#         name=input("Enter doctor name you want to search (i.e Dr.Drake Ramoray ):")
#         for i in range(len(doctor_list)):
#                                                  # check entered name is equal to name in file
#             if name == doctor_list[i]["Name"]:
#                 print(name, " works for this Clinique..!!")
#                 break
#             else:
#                 print("We dont have any doctor named :",name)
#                 break
#
#
#     def searchDoctorbyId(self):
#         """
#          This method is to search the doctor by Id to check the availability of doctor
#         """
#         doctor_dict = self.readJsonfileofDoctor()
#         doctor_list = doctor_dict["doctor"]
#         # check entered id is equal to id in file
#         id = int(input("Enter doctor Id you want to search:"))
#         for i in range(len(doctor_list)):
#             if id == doctor_list[i]["Id"]:
#                 print("Doctor is available..!!")
#                 break
#             else:
#                 print("Doctor is not available..!!")
#                 break
#
#
#     def search_doctor_by_Specialization(self):
#         """
#         This method is to search the doctor by specialization to check the availability of doctor
#         """
#         doctor_dict = self.readJsonfileofDoctor()
#         doctor_list = doctor_dict["doctor"]
#         specialization = input("Enter doctor specialization you want to search:")
#         for i in range(len(doctor_list)):
#             # check entered specialization is equal to specialization in file
#             if specialization == doctor_list[i]["specialization"]:
#                 print("Doctor is available..!!")
#                 break
#             else:
#                 print("Doctor is not available..!!")
#                 break
#
#
#
# CliniqueManagement_obj = CliniqueManagement()
# CliniqueManagement_obj.readJsonfileofDoctor()