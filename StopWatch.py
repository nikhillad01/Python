"""******************************************************************************
* Purpose: Stopwatch
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 22-12-2018
*
******************************************************************************
"""
from Utility import  utilities
u=utilities.util()
def stop_Watch():
    """this file is used to take input for stop watch"""
    try:
        a=int(input("Enter 1 to start the stop watch"))
    except ValueError:
        print("Not Vald ")
    u.stop_watch(a)

if __name__=="__main__":
    stop_Watch()