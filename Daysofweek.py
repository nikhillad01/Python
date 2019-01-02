"""******************************************************************************
* Purpose: Find Days of week
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************"""
from Utility import utilities

try:
    day=int(input("Enter day"))
    month=int(input("Enter month"))
    year=int(input("Enter year"))
    utilities.daysofweek(day,month,year)
except ValueError:
    print("error")