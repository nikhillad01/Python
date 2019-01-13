"""******************************************************************************
* Purpose: Leap Year
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 21-12-2018
*
******************************************************************************
"""

from Utility import utilities
u=utilities.util()
def leap():

    try:
        year=int(input("Enter Year to check leap Year"))
    except ValueError:
        print("Enter integer value")

    u.leap_year(year)



if __name__=="__main__":
    leap()