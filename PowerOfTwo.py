"""******************************************************************************
* Purpose: Power of Two
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 21-12-2018
*
******************************************************************************
"""
from Utility import  utilities
try:

    a=int(input("Enter num to find powers till"))  # Range to find powers till(starting from 0).
    utilities.power_of_two(a)
except ValueError:
    print("Enter Int values.")