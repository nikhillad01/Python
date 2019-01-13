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
u=utilities.util()
def powerof_two():
    """This method is used to  get the input to find power of 2."""
    try:
        a=int(input("Enter num to find powers till"))  # Range to find powers till(starting from 0).
    except ValueError:
        print("Enter Int values.")
    utilities.power_of_two(a)

if __name__=="__main__":
    powerof_two()