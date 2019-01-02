"""******************************************************************************
* Purpose: Monthly loan payment calculator
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************"""
from Utility import utilities

try:
    p=int(input("enter principle amount"))
    y=int(input("enter years"))
    r=float(input("enter rate"))
    utilities.monthlyPayment(p,y,r)
except ValueError:
    print("Enter proper values")

