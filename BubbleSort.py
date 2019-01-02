from Utility import utilities

try:
    l=list(input("Enter elements without space or comma"))
    utilities.bubble_sort(l)
except ValueError:
    print("Enter valid values")