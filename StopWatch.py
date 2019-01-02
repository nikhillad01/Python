"""******************************************************************************
* Purpose: Stopwatch
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 22-12-2018
*
******************************************************************************
"""
from Utility import  utilities

try:
    a=int(input("Enter 1 to start the stop watch"))

    utilities.stop_watch(a)
except ValueError:
    print("Not Vald ")