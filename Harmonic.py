"""******************************************************************************
* Purpose: Harmonic Number
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 21-12-2018
*
******************************************************************************
"""
from Utility import utilities
u=utilities.util()
def harmonic():
    try:
        a=int(input("Enter number to find nth harmonic "))
    except(ZeroDivisionError, ValueError):
        print("Enter valid number")
    u.harmonic(a)


if __name__=="__main__":
    harmonic()