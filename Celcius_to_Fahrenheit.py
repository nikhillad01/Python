"""******************************************************************************
* Purpose: Celcius to Fahrenheit
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************"""
from  Utility import utilities
def temp():

    try:
        a=int(input("Enter val"))
        utilities.temperaturConversion(a)
        while True:
            # main program

            answer = input('Run again? (y/n): ')
            if answer  in ('y', 'n'):
                  break
            print('Invalid input.')
            if answer == 'y' or 'Y':
                temp()
            elif answer == "n" or answer =='N':
                break
                print('Goodbye')

    except ValueError:
        print("")
temp()