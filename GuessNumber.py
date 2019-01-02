from Utility import utilities
import  math
try:
    a=int(input("Enter Number of Questions"))
    n=int(2**a)

    print("Think of Number Between 0 and ",n-1)
    secretNumber=utilities.guessNumber(0,n)
    print("Your Number is ",secretNumber)
except (ValueError,ZeroDivisionError):
    print("Enter valid integer")