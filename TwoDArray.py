"""******************************************************************************
* Purpose: 2D Array
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************
"""
from Utility import utilities
try:

    row=int(input("Enter number of rows"))
    column=int(input("Enter num of cols"))
    utilities.two_d_array(row,column)
except ValueError:
    print("enter valid values")