"""******************************************************************************
* Purpose: Find Days of week
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************"""
from Utility import utilities
u=utilities.util()
def days_of_week():
    try:
        day=int(input("Enter day"))
        month=int(input("Enter month"))
        year=int(input("Enter year"))
        u.daysofweek(day,month,year)
    except ValueError:
        print("error")



if __name__ == "__main__":
    days_of_week()