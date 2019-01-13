"""This is utility for oops programs"""
import json

class Person:
    try:
        def __init__(self):

            """This is constructor of  class initialise variables."""
            try:
                with open("../JSON/stock.json", "r") as stock_jf:           # reads stock file.
                    stock_jf = json.load(stock_jf)  # load() convert file into python from json
            except FileNotFoundError:
                print("File not found")

            self.stock_jf = stock_jf

            try:
                with open("../JSON/customers.json", "r") as person_json_value:      # reads customers file.
                    person_json_value = json.load(person_json_value)
            except FileNotFoundError:
                print("File not found ")

            self.person_json_value=person_json_value

        def view_shares(self):

            """This method is used to display all the available ."""

            for i in range(len(self.stock_jf['Stock Report'])):  # ["Stock Report "] is main key under that all company values are stored as key and value pair.
                print(i,self.stock_jf['Stock Report'][i])

        def check_validity(self):

            """This method is used to check if user is valid or not . """

            print("*************** Welcome ******************")
            i=0                         # variable used for iteration
            name=input("Enter Username")
            while i<len(self.person_json_value["Person"]):              # i is incrementing and loop will continue till i reaches the len of ["Person"]
                if self.person_json_value["Person"][i]["Name"]==name.title():   # i.e ["person"][0]["Name"] here [0] is index
                    index=i
                    print(self.person_json_value["Person"][i])
                    print("....Login successful....")
                    c = int(input("1:Buy shares\n2:Sell shares:"))
                    if c == 1:
                        p.buy_share(index)
                    elif c == 2:
                        p.sell_share(index)

                    else:
                        print("wrong Input")


                i+=1




        def add_new_company(self):
            name =input("Enter company name")
            number=int(input("Enter Your Number of share"))
            price=int(input('Enter Your Price per share'))
            new_stock_dict = {"Stock Name": name,           # creates new entry as dictionary.

                              "Number of Share": number,

                              "Share Price": price}

            with open('../Utility/stock.json', 'w') as stock_jf:
                self.stock_jf['Stock Report'].append(new_stock_dict)   # appends new company entry to the [Stack Report] Key

            stock_jf.write(json.dumps(self.stock_jf,indent=2))  # first dumps converts data to Json string  and then writes to file.


        def buy_share(self,index):
            for i in range(len(self.stock_jf['Stock Report'])):  # prints all the data with index
                print(i,self.stock_jf['Stock Report'][i])

            print('Enter Which Company Share you want to buy')
            choice =int(input("Enter choice in int(index)"))        # choice should be the index of company name.

            buy_share =int(input("Enter Number of Share You want to buy"))
            each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']    # calculates amount for shares.
            amount_pay = buy_share * each_share_price

            if self.person_json_value['Person'][index]["Total Balance"]> amount_pay:   # if person has more money than total amount of shares to by:

                    print("Total amount you have to pay for ",buy_share," stocks : ",amount_pay )
                    updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share

                    with open("../Utility/stock.json", "w") as jf:
                        self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                        jf.write(json.dumps(self.stock_jf,indent=2))


                    person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                    print('Your Updated Balance is ', person_updated_balance)
                    person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                    print('Your Updated No. of share is ', person_updated_share)

                    with open("../JSON/customers.json", "w") as jf:
                        self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                        self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                        jf.write(json.dumps(self.person_json_value))
            else:print("Sorry , You Don't have enough money ")



        def sell_share(self,index):
            print('Enter choice to sell your share to particular company')
            for i in range(len(self.stock_jf['Stock Report'])):    # prints all shares
                print(i, self.stock_jf['Stock Report'][i])

            choice = int(input("Enter choice in Int"))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company')
            sell_share =int(input("Number of shares to sell "))             # index of company to sell share of that .
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share  # updates the number of stock in total company stocks.


            with open("../JSON/stock.json", "w") as jf:
                    self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf,indent=2))

            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company"))        # asks user for price he wants to sell his shares
            person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] + person_share_price * sell_share  # add money to  user after selling .


            print(' --', person_share_price * sell_share, '----will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance)

            print('Now Your Updated Number of share is ', updated_person_share)

            with open("../JSON/customers.json", "w") as jf:
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                    jf.write(json.dumps(self.person_json_value,indent=2))




    except KeyboardInterrupt:
        print("keyboard Interrupt")
p=Person()



class CliniqueManagement:

    def __init__(self):
        pass

    def getUserInput(self):
        """
         This method is to take the input from user
        """
        print()
        print("------Welcome to Clinique------")
        print()
        ch = input("Press : y/n to continue or exit:")
        while ch == 'y':
            print(" \n 1.Doctor Options  \n 2.For Patient options ? \n 3.Exit")
            choice = int(input("Enter your choice:"))
            if choice == 1:
                print("\n 1.Add Doctor \n 2.View Doctors \n 3.Exit")
                ch1 = int(input("Enter your choice:"))
                if ch1 == 1:
                    self.add_doctors()
                elif ch1 == 2:
                    self.view_doctors()
                elif ch1 == 3:
                    break
                else:
                    print("!!..Invalid choice..!!")
                    break
            elif choice == 2:
                print("\n 1.Add Appointment \n 2.Search Doctor \n 3.Exit")
                ch2 = int(input("Enter your choice:"))
                if ch2 == 1:
                    self.addAppointment()
                elif ch2 == 2:
                    print("\n 1.Search Doctor by Name \n 2.Search Doctor Id \n 3.Search Doctor Specialization \n 4.Exit")
                    ch3=int(input("Enter your choice:"))
                    if ch3 == 1:
                        self.searchDoctorbyName()
                    elif ch3 == 2:
                        self.searchDoctorbyId()
                    elif ch3 == 3:
                        self.search_doctor_by_Specialization()


                elif ch2 == 3:
                    break
                else:
                    print("!!..Invalid choice..!!")
                    break
            elif choice == 3:
                break
            else:
                print("!!!..Invalid choice..!!!")
                break

    def readJsonfileofDoctor(self):
        """
         This method is to create the json file which contain information about doctors
        :return: it return doctor file in the form of dictionary
        """

        with open('Doctors_info.json', 'r') as file_obj:
            json_str = file_obj.read()
            # loads the data and convert it into dictionary format

            json_value = json.loads(json_str)

            file_obj.close()

        return json_value

    def read_Json_file_of_Patient(self):
        """
         This method is to create the json file which contain information about patient
        :return: it returns file of patient in form of dictionary
        """
        patient_information = {
            "patient":[{
                    "Name": "sahil sharma",
                    "Id": 12,
                    "Age": 24,
                    "mobile number": "7865232419"
                     },
                    {
                    "Name": "pratik Patil",
                    "Id": 12,
                    "Age": 34,
                    "mobile number": "8956345213"
                     },
                    {
                    "Name": "sampada dagwar",
                    "Id": 14,
                    "Age": 21,
                    "mobile number": "9420036520"

                    },

                   {
                    "Name": "nidhi kamath",
                    "Id": 15,
                    "Age": 22,
                    "mobile number": "8976348562"

                   }]
         }
        # convert python dictionary to json format string
        s = json.dumps(patient_information)
        # open json file to write
        with open('Patient_info.json', 'w') as file_obj:
            file_obj.write(s)

        # open json file to read
        with open('Patient_info.json', 'r') as file_obj:
            json_str = file_obj.read()
            # loads the data and convert it into dictionary format
            json_value = json.loads(json_str)

        file_obj.close()

        return json_value



    def readJsonfileofAppoinment(self):
        """
         This method is to create the json file which contain all information about patients appointment
        :return: it returns appointment file in the form of dictionary
        """
        appoinment_information = {
            "Dr.Arman Singh":[{"patient Name": "Nikhil lad","Id": 12,"Age": 24,"mobile number": "7865232419", "time":"AM"},
                              {"patient Name": "pushkar ishware","Id": 12,"Age": 34,"mobile number": "8956345213", "time":"AM"}],
            "Dr.Shital Patil":[{"patient Name": "jhanvi mhatre","Id": 14,"Age": 21,"mobile number": "9420036520", "time":"PM"}],
            "Dr.Varun Shaha":[{"patient Name": "shazad shaikh", "Id": 15,"Age": 22,"mobile number": "8976348562" ,"time":"AM"}],
            "Dr. Amit Joshi": [{"patient Name": "sagar kadam","Id": 12,"Age": 34,"mobile number": "8956345213", "time":"AM"}]}

        # convert python dictionary to json format string
        s = json.dumps(appoinment_information)
        # open json file to write
        with open('appoinment_info.json', 'w') as file_obj:
            file_obj.write(s)

        # open json file to read
        with open('appoinment_info.json', 'r') as file_obj:
            json_str = file_obj.read()
            # loads the data and convert it into dictionary format
            json_value = json.loads(json_str)

        file_obj.close()

        return json_value


    def add_doctors(self):
        """
         This method is to add new entery doctor
        """
        doctor_name=input("Enter Name:")
        doctor_id=int(input("Enter Id:"))
        specilization=input("Enter Specialization:")
        availability=input("Enter Availability(AM/PM/Both):")

        with open('Doctors_info.json', 'r') as file_obj:
            # open json file to read
            json_str = file_obj.read()
            # loads the data and convert it into dictionary format
            new_json_value = json.loads(json_str)

        # add new entry
        new_dict={"Name": doctor_name , "Id": doctor_id, "specialization": specilization, "Availability": availability}

        # open json file to write
        with open('Doctors_info.json', 'w') as file_obj:
            new_json_value["doctor"].append(new_dict)
            # convert python dictionary to json format string
            file_obj.write(json.dumps(new_json_value,indent=2))


    def view_doctors(self):
        """
         This method is to display all available doctors
        """
        # call function to read file which returns dictionary
        doctor_dict=self.readJsonfileofDoctor()
        # store list of json file in new list doctor_list
        doctor_list=doctor_dict["doctor"]


        print("Available Doctors are:")
        print("----------------------------------------")
        print("Name                    specialization ")
        print("----------------------------------------")

        # traverse doctor file
        for i in range(len(doctor_list)):
            name = doctor_list[i]["Name"]
            specialization = doctor_list[i]["specialization"]

            print(name, "          ",specialization)

    def addAppointment(self):
        """
         This method is to take appointment by patient
        """
        print("Name of doctors")
        print("---------------")
        # call function to read file which returns dictionary
        doctor_dict = self.readJsonfileofDoctor()
        # store list of json file in new list doctor_list
        doctor_list = doctor_dict["doctor"]


        for i in range(len(doctor_list)):
            name = doctor_list[i]["Name"]
            specialization=doctor_list[i]["specialization"]
            Availability=doctor_list[i]['Availability']
            print(name," ",specialization,' ',Availability)     # using index i prints name of doctor from doctor_list['Name']


        doctor_name=input("Name of Doctor to take appointment(i.e Dr. Drake Ramory )??")       # doctor name as input
        time=input("please Enter appointment time..(AM/PM/Both) :")

        """Logic : Take doctor name as input to take appointment and check only for that doctor if he has more than 5 patients """

        appointment_dict = self.readJsonfileofAppoinment()      # read appointment json.
        appointment_list = appointment_dict[doctor_name]        # store all patients of 1 doctor in list.

        print("this is appointment list ",appointment_list)
                                                                # check each doctor has maximum 5 patient
        if len(appointment_list) < 5:
            for i in range(len(doctor_list)):
                if doctor_name == doctor_list[i]["Name"]:
                    if time.upper() == doctor_list[i]["Availability"]:
                        print("Doctor is available..!! Please Enter the patient details:")
                        name = input("Enter patient name:")
                        id = int(input("Enter patient Id:"))
                        age = int(input("Enter patient age:"))
                        mob_no = input("Enter patient's mobile number:")


                        with open('appoinment_info.json', 'r') as file_obj:
                            json_str = file_obj.read()
                                                                # loads the data and convert it into dictionary format
                            new_json_value = json.loads(json_str)

                                                                # add new entry
                        new_dict = {"patient Name": name ,"Id": id,"Age": age,"mobile number": mob_no, "time":time}

                                                                # open json file to write
                        with open('appoinment_info.json', 'w') as file_obj:
                            new_json_value[doctor_name].append(new_dict)
                            # convert python dictionary to json format string
                            file_obj.write(json.dumps(new_json_value,indent=2))

                        print("Your appointment is fixed. Thank You !")

                    else:
                         print("Sorry. Doctor is not available..!! ")


    def searchDoctorbyName(self):
        """
         This method is to search the doctor by name to check the availability of doctor
        """
        doctor_dict = self.readJsonfileofDoctor()
        doctor_list = doctor_dict["doctor"]
        name=input("Enter doctor name you want to search (i.e Dr.Drake Ramoray ):")
        for i in range(len(doctor_list)):
                                                 # check entered name is equal to name in file
            if name == doctor_list[i]["Name"]:
                print(name, " works for this Clinique..!!")
                break
            else:
                print("We dont have any doctor named :",name)
                break


    def searchDoctorbyId(self):
        """
         This method is to search the doctor by Id to check the availability of doctor
        """
        doctor_dict = self.readJsonfileofDoctor()
        doctor_list = doctor_dict["doctor"]
        # check entered id is equal to id in file
        id = int(input("Enter doctor Id you want to search:"))
        for i in range(len(doctor_list)):
            if id == doctor_list[i]["Id"]:
                print("Doctor is available..!!")
                break
            else:
                print("Doctor is not available..!!")
                break


    def search_doctor_by_Specialization(self):
        """
        This method is to search the doctor by specialization to check the availability of doctor
        """
        doctor_dict = self.readJsonfileofDoctor()
        doctor_list = doctor_dict["doctor"]
        specialization = input("Enter doctor specialization you want to search:")
        for i in range(len(doctor_list)):
            # check entered specialization is equal to specialization in file
            if specialization == doctor_list[i]["specialization"]:
                print("Doctor is available..!!")
                break
            else:
                print("Doctor is not available..!!")
                break



CliniqueManagement_obj = CliniqueManagement()
CliniqueManagement_obj.readJsonfileofDoctor()




import random
import numpy as np
from DSA import DSA_Utilities

class DeckOfCards:

    """This class is used to write logic for deck of cards"""

    def shuffle(self):

        """Method to distribute 9 cards to 4 users"""

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11 Jack", "12 Queen", "13 King", "14 Ace"]

        list_cards = []         # list to hold cards.

        while len(list_cards) < 36:  # loop will run till 36 because we want to distribute 36 cards to 4 players.
            for i in range(0, 9):       # used to get only  9 numbers

                random_no = random.randint(1, 13)  # generate random number within 1 and 13

                cards_rank = Rank[random_no - 1]

                random_no_suits = random.randint(0, 3)  # generates random number for suits.
                cards_rank = cards_rank + ' ' + suits[random_no_suits]  # adds suit and Rank together.

                if list_cards.__contains__(cards_rank) is False:  # if list of cards does not contains cards_rank already:

                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)  # append cards_rank to list of cards

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # list comprehensions for matrix.
        index = 0
        for i in range(row):  # row iteration

            for j in range(column):  # column iteration .
                two_d_array[i][j] = list_cards[index]
                index += 1
        #print(two_d_array)
        a=np.array(two_d_array)
        print(a)
        #print("list of cards , : ",list_cards)
        limit=9
        l1 = []         # four lists are used  for slicing of 36  elements in 4 parts(9 each).
        l2=[]
        l3=[]
        l4=[]
        #print("listttttt",list_cards)
        #print(list_cards[:9])
        for i in list_cards[0:9]:
            i = tuple((int(i[:2]), i[2:]))  # because we are getting data like ['12 Queen Spades']. all in string format so we split first two chars converts it to int and  add in tuple which makes to separate elements in one small tuple.
                                            # also it makes the sorting easy  with Int.

            l1.append(i)        # appends data to list.

        #l1.sort()
        l1.sort()               # sorts the data.
        print()
        print("Queue data")
        print()
        print("Player 1 Cards")

        for j in l1:
            q1.push(j)           # adds data of player 1 to queue 1.

        #utilities.bubble_sort(l1)

        q1.show()
        #print("List data")
        #print(l1)
        print()

        for i in list_cards[9:18]:
            i = tuple((int(i[:2]), i[2:]))
            l2.append(i)
        l2.sort()
        print("Player 2 Cards")
        for l in l2:
            q2.push(l)       # adds data of player 2 to queue 2.
        q2.show()
        print()

        for i in list_cards[18:27]:
            i = tuple((int(i[:2]), i[2:]))
            l3.append(i)
        l3.sort()
        print("Player 3 Cards")
        for m in l3:
            q3.push(m)       # adds data of player 3 to queue 3.
        q3.show()
        print()

        for i in list_cards[27:]:
             i=tuple((int(i[:2]),i[2:]))
             l4.append(i)

        l4.sort()
        print("Player 4 Cards")
        for n in l4:
            q4.push(n)       # adds data of player 4 to queue 4.
        q4.show()
        #print("First two chars : ",l1[8][:2])
        #s ="13 King Diamonds"
        #s2=tuple((int(s[:2]),s[2:]))
        #print(s2)
        return list_cards, two_d_array
q1=DSA_Utilities.Queue()            # Queue class objects.
q2=DSA_Utilities.Queue()
q3=DSA_Utilities.Queue()
q4=DSA_Utilities.Queue()



import random
import numpy as np
class Deck_Of_Cards_1:



    def shuffle(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        list_cards = []

        while len(list_cards) < 36:   # loop will run till 36 because we want to distribute 36 cards to 4 players.
            for i in range(0, 9):      # used to get only 9 numbers

                random_no = random.randint(1, 13)       # generate random number within 1 and 13

                cards_rank = Rank[random_no - 1]

                random_no_suits = random.randint(0, 3)      # generates random number for suits.
                cards_rank = cards_rank + ' ' + suits[random_no_suits]  # adds suit and Rank together.

                if list_cards.__contains__(cards_rank) is False:  # if list of cards does not contains cards_rank already:

                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)   # append cards_rank to list of cards

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # list comprehensions for matrix.
        index = 0
        for i in range(row):            # row iteration

            for j in range(column):     # column iteration .
                two_d_array[i][j] = list_cards[index]
                index += 1
        #print(two_d_array)
        a=np.array(two_d_array)     # numpy to print in good structure .
        print(a)
        return list_cards, two_d_array



class inventory:
    def inventory_method(self):
        try:
            with open("../JSON/inventory.json") as f:
                data=json.load(f)
        except FileNotFoundError:
            print("File not found")




        print("File not found")     # json.load() loads data from file to Python Dict.
        print("Data in Python dict format : ")
        print(data)
        print("All in one")
        new_rice={}
        new_wheat={}
        new_pulses={}
        for r,w,p in zip(data['Rice'],data['Wheat'],data["Pulses"]):   # using zip we can iterate over two or more lists at a time.
            r_name=r['name']
            r_price=r['Price']
            new_rice[r_name]=r_price        # updates the new_rice dictionary with only rice values.

            w_name = w["name"]
            w_price = w["Price"]
            new_wheat[w_name] = w_price   # updates the new_wheat dictionary with only wheat values.

            p_name=p['name']
            p_price=p['Price']
            new_pulses[p_name]=p_price    # updates the new_pulses dictionary with only pulses values.

        print()
        print("Rice detail ", new_rice)
        print("Total Rice items : ", len(new_rice))     # calculates total rice items
        print("Total cost of Rice Items : ", sum(new_rice.values()))    # calculates total price of rice items.
        print()
        print("Wheat detail ", new_wheat)
        print("Total Wheat items : ", len(new_wheat))   # calculates total Wheat items
        print("Total cost of Wheat Items : ", sum(new_wheat.values()))    # calculates total price of Wheat items.
        print()
        print("Pulses detail ", new_pulses)
        print("Total Pulse items : ", len(new_pulses))   # calculates total Pulses items
        print("Total cost of Pulse Items : ", sum(new_pulses.values()))    # calculates total price of Pulse items.



import json
class inventory2:

    def inventory(self):
        try:
            with open("../JSON/inv2.json") as f:
                data=json.load(f)
            print(data)
        except FileNotFoundError:
            print("File Not Found")

        print("Available items in our grocery store:")

        print("rice :")
        for r in data["Rice"]:
            print(r['name'], " Per kg", r['Price'], "Available Kg's", r['quantity'],"kg")   # prints rice data

            print("Pulses :")
        for p in data['Pulses']:
            print(p['name'], " Per kg", p['Price'], "Available kgs  ", p['quantity'],"kg")  # prints pulse data

            print("Wheat :")
        for w in data['Wheat']:
            print(w['name'], " Per kg", w['Price'], "Available kgs   ", w['quantity'],"kg")  # prints wheat data.


        ch = int(input('You want to add item ??'))


        if ch == 1:

           item = input("What item you want to add Rice , Pulses , Wheat  write name")
           user_requirement=input("Enter name of item ")
           price_per_kg=int(input("enter price per KG"))
           quantity=int(input("Enter total Quantity "))

        try:
            with open("../JSON/inv2.json", 'r') as jf:
                    json_str = jf.read()
                    jf.close()
                    json_value = json.loads(json_str)  # loads python object to json string
        except FileNotFoundError:
            print("File not found")

        try:
            with open("../JSON/inv2.json", 'w') as jf:
                    json_value[item.title()].append({"name": user_requirement,
                                         "Weight": 1,
                                         "Price": price_per_kg,
                                         "quantity":quantity})
                    jf.write(json.dumps(json_value,indent=2))
                    jf.close()
        except FileNotFoundError:
            print("Files not found")



import re
import datetime
class regex:
    def regular_exp(self):
        str1='Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is +91­xxxxxxxxxx.Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.'
        try:
            full_name=input("Enter Your Full name")
            first_name, last_name = full_name.split(" ")
            phonenumber = input("Enter phone number with standard format eg : 987-654-3210")
            regex ="\w{3}-\w{3}-\w{4}"          # pattern to match mobile number.

            #\w for characters

            date=datetime.datetime.today().strftime('%d-%m-%Y')
            if re.search(regex, phonenumber):
                print("Valid phone number")
                str2 = re.sub("<<name>>", first_name.title(), re.sub("<<full name>>", full_name.title(),
                                                                     re.sub("xxxxxxxxxx", phonenumber,
                                                                            re.sub("01/01/2016", date, str1))))
                print(str2)

            else:
                print("Invalid phone number")

        except ValueError:
            print("Name should be str")




class StockReport:
    def __init__(self):
        try:
            with open("../JSON/stock3.json") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("File Not found")
        self.data = data

    def stock_report(self):
        total_stock_google = 0
        total_stock_apple = 0

        for g in self.data["Google"]:
            print("total shares values of", g['name'], "is", g['shares'] * g['price'])
            total_stock_google += g['shares'] * g['price']

        print()
        for a in self.data["Apple"]:
            print("total shares values of", a['name'], "is", a['shares'] * a['price'])
            total_stock_apple += a['shares'] * a['price']

        print()
        print("Total stock of Google is: ", total_stock_google)
        print()
        print("Total stock of Apple is: ", total_stock_apple)




from DSA.Linked_list import linked_list
l=linked_list()
class stock_linked_list:

    def linked_list_stock(self):
        with open('../JSON/stock.json', "r") as f:
            f = json.load(f)
        print(type(f))

        for i in f["Stock Report"]:
            #print(i)
            #print(type(i))
            l.add(i)
            #{'Stock Name': 'Google', 'Number of Share': 26, 'Share Price': 1000}
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



