from Utility import utilities
try:
    coupounnumber=int(input("Enter coupoun number"))
    utilities.coupoun(coupounnumber)
except ValueError:
    print("Please Enter Valid Integer code")
