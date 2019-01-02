"""******************************************************************************
* Purpose: Euclidien Distance
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 22-12-2018
*
******************************************************************************
"""
from Utility import utilities

try:
    x=int(input("enter X"))
    y=int(input("enter Y"))
    utilities.euclidien(x,y)
except ValueError:
    print("Enter integer value")