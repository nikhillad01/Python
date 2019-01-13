"""******************************************************************************
* Purpose: Binary to Decimal and vice-versa operations
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 27-12-2018
*
******************************************************************************
"""
from Utility import utilities
u=utilities.util()
def to_binary():
    try:
        a=int(input("Enter Decimal number"))
    except ValueError:
        print("enter decimal number only")
    u.toBinary(a)

if __name__=="__main__":
    to_binary()