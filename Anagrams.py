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
def anagram_run():

    try:
        a=input("Enter str1")
        b=input("Enter str2")
        u.anagrams(a,b)
    except ValueError:
        print("enter strings")

if __name__=="__main__":
    anagram_run()
    print("we")