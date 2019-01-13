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
u=utilities.util()
def two_d_arraY():

    try:
        row=int(input("Enter number of rows"))
        column=int(input("Enter num of cols"))
    except ValueError:
        print("enter valid values")

    u.two_d_array(row, column)

if __name__=="__main__":
    two_d_arraY()