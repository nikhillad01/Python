import re
import datetime
str1='Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is +91­xxxxxxxxxx.Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.'
try:
    full_name=input("Enter Your Full name")
    first_name, last_name = full_name.split(" ")
    phonenumber = input("Enter phone number with standard format eg : 987-654-3210")
    regex ="\w{3}-\w{3}-\w{4}"
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




