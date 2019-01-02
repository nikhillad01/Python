"""******************************************************************************
* Purpose: Coupoun
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************
"""
from Utility import utilities
try:
    coupounNumber=int(input("Enter coupoun number"))
    utilities.coupoun(coupounNumber)
except ValueError:
    print("Please Enter Valid Integer code")
