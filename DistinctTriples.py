"""******************************************************************************
* Purpose: Distinct Tripletes
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************
"""

from Utility import utilities



try:
    l = []
    a=int(input("numbers"))
    for i in range(0,a):
        x = int(input("enter no. \n"))
        l.insert(i, x)
    print(l)
    utilities.distinct_triples(l)
except ValueError:
    print("Enter valid number")

