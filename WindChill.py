"""******************************************************************************
* Purpose: Wind Chill
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 26-12-2018
*
******************************************************************************
"""
from Utility import utilities
u=utilities.util()
def wind_chill():

    try :
        temperature=int(input("Enter temperature  : "))
        windspeed=int(input("Enter wind speed  : "))
    except ValueError:
        print("Temperature and wind should be Integer or float not Strings")

    u.windChill(temperature, windspeed)
if __name__=="__main__":
    wind_chill()