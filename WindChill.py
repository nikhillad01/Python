from Utility import utilities
try :
    temperature=int(input("Enter temperature  : "))
    windspeed=int(input("Enter wind speed  : "))
    utilities.windChill(temperature,windspeed)
except ValueError:
    print("Temperature and wind should be Integer or float not Strings")

