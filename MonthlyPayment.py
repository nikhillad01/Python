"""******************************************************************************
* Purpose: Monthly loan payment calculator
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************"""
from Utility import utilities
u=utilities.util()

def monthly_payment():

    try:
        p=int(input("enter principle amount"))      # accept user inputs.
        y=int(input("enter years"))
        r=float(input("enter rate"))
    except ValueError:
        print("Enter proper values")
    u.monthlyPayment(p,y,r)




if __name__=="__main__":
    monthly_payment()