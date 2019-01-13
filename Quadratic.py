"""******************************************************************************
* Purpose: Quadratic.py
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 22-12-2018
*
******************************************************************************"""
from Utility import utilities
u=utilities.util()
def quadratic():

    """This method is used to take inputs  to find quadratic equation ."""

    try:
        a=int(input("Enter A"))
        b=int(input("Enter B"))
        c=int(input("Enter C"))
    except ValueError:
        print("Not valid Values ")

    utilities.quadratic(a, b, c)

if __name__=="__main__":
    quadratic()