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
u=utilities.util()
def euclidien():
    try:
        x=int(input("enter X"))
        y=int(input("enter Y"))
        u.euclidien(x,y)
    except ValueError:
        print("Enter integer value")
if __name__=="__main__":
    euclidien()