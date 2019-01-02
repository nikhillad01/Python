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

try:
    a=int(input("Enter value to find SQRT"))
    utilities.sqrtnewton(a)
except ValueError:
    print("Enter Correct value")