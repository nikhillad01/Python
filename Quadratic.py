from Utility import utilities
try:
    a=int(input("Enter A"))
    b=int(input("Enter B"))
    c=int(input("Enter C"))

    utilities.quadratic(a,b,c)
except ValueError:
    print("Not valid Values ")

