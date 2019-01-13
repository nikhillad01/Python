"""******************************************************************************
* Purpose: Coin Filp
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 21-12-2018
*
******************************************************************************
"""

from Utility import utilities
u=utilities.util()
def coin_flip():
    try:

        a=int(input("Enter number of times to flip coin "))
        u.flip_coin(a)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    coin_flip()
