"""******************************************************************************
* Purpose: Prime Numbers in range .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 22-12-2018
*
******************************************************************************"""
from Utility import utilities
u=utilities.util()
def prime_in_range():
    """this method is used to take lower and higher ranges to find the prime numbers from that range ."""
    try :
        n1=int(input("Enter  lower end  "))
        n2=int(input("Enter higher range  "))
    except ValueError:
        print("Something went wrong")

    u.primeNumbers(n1, n2)

if __name__=="__main__":
    prime_in_range()