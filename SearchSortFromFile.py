"""******************************************************************************
* Purpose: Search and sort from Txt files.
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************
"""

from  Utility import utilities


try:
    print("*********** Binary search from file************************")

    a=input("Enter element to search")
    utilities.binary_from_file(a)
    print()


    print("********************* String Insertion Sort***************")

    data=[]
    a=int(input("Enter total numbers in list"))
    for i in range(0,a):
        x=input("Enter element ")
        data.append(x)
    print("unsorted list : ",data)
    utilities.file_insertion_sort(data)



    print("********************* Integer Bubble Sort***************")

    intdata=[]
    b=int(input("Enter total numbers in list"))
    for j in range(0,b):
        y=int(input("Enter element "))
        intdata.append(y)
    print("unsorted list : ",intdata)
    utilities.file_bubble_sort()



except ValueError:
    print("Enter valid values")