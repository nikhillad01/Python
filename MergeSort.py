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
u=utilities.util()
def merge():
    try:
        data = []
        d=int(input("Enter total elements in list "))
        for i in range(d):          # getting data in list.
            x=input("Enter string")
            data.append(x)
        print("unsorted list : ",data)
        end=len(data)
        u.mergesort(data)       # calling merge sort method from utilities .
        while True:
            # main program
            while True:
                answer = input('Run again? (y/n): ')
                if answer in ('y', 'n'):        # if answer is not y or n then invalid input.
                    break
                print('Invalid input.')
            if answer == 'y' or 'Y':        # if answer is Y or y the re run the merge method.
                merge()
            elif answer=='n' or 'N':        # if answer is n or N then break .
                exit()
                #print('Goodbye')
                break
    except ValueError:
        print("Value error")


if __name__=="__main__":
    merge()