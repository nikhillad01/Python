from Utility import utilities
try:
    stake=int(input("Enter stake"))
    goal=int(input("Enter goal"))
    no=int(input("No of times to play bet"))

    utilities.gambler(stake,goal,no)
except ValueError:
    print("Enter valid entries")