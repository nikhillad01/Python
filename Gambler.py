
"""******************************************************************************
* Purpose: Gambler.py
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************
"""
from Utility import utilities
try:
    stake=int(input("Enter stake"))
    goal=int(input("Enter goal"))
    no=int(input("No of times to play bet"))

    utilities.gambler(stake,goal,no)
except ValueError:
    print("Enter valid entries")