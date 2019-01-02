"""******************************************************************************
* Purpose: Replace String from sentence
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 21-12-2018
*
******************************************************************************
"""

from Utility import utilities
try:

    print("Hello <<UserName>>, How are you?")
    a=str(input("Enter username"))  #username to replace with <<UserName>>

    utilities.replace_str(a)         #Calling the method from utilities
except ValueError:
    print("Enter String")