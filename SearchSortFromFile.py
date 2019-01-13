"""******************************************************************************
* Purpose: Search and sort from Txt files.
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************
"""

"""This file contain all the programs for searching and sorting in File ."""

from Utility import utilities
u=utilities.util()
def search_sort_from_file():

    print("*********** Binary search from file************************")

    try:

        a=input("Enter element to search")
    except ValueError:
        print("Not valid value.")

    u.binary_from_file(a)
    print()
    print("********************* String Insertion Sort***************")
    data=[]
    try:
        a=int(input("Enter total numbers in list"))
    except ValueError:
        print("Not valid value. ")

    for i in range(0,a):
        try:
            x=input("Enter element ")
        except ValueError:
            print("Not valid Value")
        data.append(x)
    print("unsorted list : ",data)
    u.file_insertion_sort(data)

    print("********************* Integer Bubble Sort***************")

    intdata=[]
    b=int(input("Enter total numbers in list"))
    for j in range(0,b):
        try:
            y=int(input("Enter element "))
        except ValueError:
            print("not Valid values")

        intdata.append(y)
    print("unsorted list : ",intdata)
    u.file_bubble_sort()





if __name__=="__main__":
    search_sort_from_file()