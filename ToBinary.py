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
try:
    a=int(input("Enter Decimal number"))
    utilities.toBinary(a)
except ValueError:
    print("enter decimal number only")