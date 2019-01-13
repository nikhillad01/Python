"""******************************************************************************
* Purpose: Commercial Data Processing
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 9-1-2018

******************************************************************************
"""

from JSON import OOPS_Utility
p=OOPS_Utility.Person()

if __name__ == "__main__":

    p.view_shares()
    try:
        i = int(input("1: Admin Login or 2: User "))
        if i == 1:
            print("welcome Admin")
            j = int(input("1 to add Company :"))
            if j == 1:
                p.add_new_company()
        elif i == 2:
            print("Welcome User")
            p.check_validity()

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid Value")
