from Utility import utilities
u=utilities.util()

def guess_number():

    try:
        a=int(input("Enter Number of Questions"))

    except (ValueError, ZeroDivisionError):
        print("Enter valid integer")

    n=int(2**a)

    print("Think of Number Between 0 and ",n-1)
    secretNumber=u.guessNumber(0,n)
    print("Your Number is ",secretNumber)


if __name__=="__main__":
    guess_number()