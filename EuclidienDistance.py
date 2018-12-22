from Utility import utilities

try:
    x=int(input("enter X"))
    y=int(input("enter Y"))
    utilities.euclidien(x,y)
except ValueError:
    print("Enter integer value")