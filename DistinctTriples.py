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
u=utilities.util()

def distince_triples():
    l = []
    try:

        a=int(input("numbers"))
        for i in range(0,a):
            x = int(input("enter no. \n"))
            l.insert(i, x)
        print(l)
        u.distinct_triples(l)
    except ValueError:
        print("Enter valid number")
distince_triples()
if __name__ == "__main__":
    distince_triples()