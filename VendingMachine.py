"""******************************************************************************
* Purpose: Find the Fewest Notes to be returned for Vending Machine
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************
"""
from  Utility import  utilities
u=utilities.util()
def vending_machine():
    try:
        a=int(input("enter money"))
    except ValueError:
        print("Enter only integer values.")

    u.vendingMachine(a)


if __name__=="__main__":
    vending_machine()