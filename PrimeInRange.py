from Utility import utilities

try :
    n1=int(input("Enter  lower end  "))
    n2=int(input("Enter higher range  "))
    utilities.primeNumbers(n1,n2)
except ValueError:
    print("Something went wrong")