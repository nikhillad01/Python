"""******************************************************************************
* Purpose: Coupoun
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
******************************************************************************
"""
from Utility import utilities
u=utilities.util()
def coupoun_number():
    try:
        coupounNumber=int(input("Enter coupoun number"))
        u.coupoun(coupounNumber)
    except ValueError:
        print("Please Enter Valid Integer code")

if __name__ == "__main__":
    coupoun_number()