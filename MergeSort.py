"""******************************************************************************
* Purpose: Merge Sort
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************
"""

from Utility import utilities
#data=[]
def merge():
    try:
        data = []
        d=int(input("Enter total elements in list "))
        for i in range(d):
            x=input("Enter string")
            data.append(x)
        print("unsorted list : ",data)
        end=len(data)
        utilities.mergesort(data)
        while True:
            # main program
            while True:
                answer = input('Run again? (y/n): ')
                if answer in ('y', 'n'):
                    break
                print('Invalid input.')
            if answer == 'y' or 'Y':
                merge()
            elif answer=='n' or 'N':
                print('Goodbye')
                break
    except ValueError:
        print("Value error")

merge()