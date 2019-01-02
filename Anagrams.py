"""******************************************************************************
* Purpose: To find if two strings are Anagram or not
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************"""
from  Utility import utilities

try:
    a=input("Enter str1")
    b=input("Enter str2")
    utilities.anagrams(a,b)
except ValueError:
    print("enter strings")
