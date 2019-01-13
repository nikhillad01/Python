"""******************************************************************************
* Purpose: To find if two strings are Anagram or not
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************"""

from Utility import utilities
u=utilities.util()
def bubble_sort():
    try:
        l=list(input("Enter elements without space or comma"))      # inputs from user
        u.bubble_sort(l)
    except ValueError:
        print("Enter valid values")

if __name__=="__main__":
    bubble_sort()
