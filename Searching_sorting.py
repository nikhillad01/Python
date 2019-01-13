"""******************************************************************************
* Purpose: Searching and Sorting
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************
"""

"""This file has all searching and sorting programs  for Integer and strings."""

from Utility import utilities
u=utilities.util()
def search_sort():
    l = [9, 4, 6, 7, 1, 0, 6, 2]
    string_list = list(map(str, l))
    print()
    print(l)
    print("String List : ", string_list)
    print()
    print("***************Binary String Search***********************")
    try:
        x=input("Enter String to find Binary Search ")
    except ValueError:
        print("Enter valid values.")
    u.binary_search(string_list,x)
    print()


    print("***********************Binary Integer Search***************")
    try:
        x2 = int(input("Enter Integer Binary Search"))
    except ValueError:
        print("Enter valid values .")

    u.binary_search(l, x2)
    print()

    print("***************************Insertion Sort***********************************")
    u.insertion_sort(l)
    print()


    print("***************************Insertion String Sort***********************************")
    u.insertion_sort(string_list)
    print()


    print("************************** Bubble Sort Integer**************************************")
    u.bubble_sort(l)
    print()


    print("************************** Bubble Sort String**************************************")
    u.bubble_sort(string_list)


    print()
    print("Time For all Dict ",u.timeDict)


if __name__=="__main__":
    search_sort()