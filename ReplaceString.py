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
u=utilities.util()
def replace_str():
    """This method is used to take inputs to replace string"""
    print("Hello <<UserName>>, How are you?")

    try:
        a=str(input("Enter username"))  #username to replace with <<UserName>>
    except ValueError:
        print("Enter String")

    u.replace_str(a)         #Calling the method from utilities

if __name__=="__main__":
    replace_str()