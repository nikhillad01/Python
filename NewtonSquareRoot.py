"""******************************************************************************
* Purpose: Newtons method for Square root
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************
"""
from  Utility import  utilities
u=utilities.util()
def newton_sqrt():
    """This method is used to take the inputs to find square
     root according newtons method."""

    try:
        a=int(input("Enter value to find SQRT"))
    except ValueError:
        print("Enter Correct value")
    u.sqrtnewton(a)


if __name__=="__main__":
    newton_sqrt()