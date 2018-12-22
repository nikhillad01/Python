from Utility import utilities
l=[]

print(l)
try:
    a=int(input("numbers"))
    for i in range(0,a):
        x = int(input("enter no. \n"))
        l.insert(i, x)
    print(l)
    utilities.distinctTriples(l)
except ValueError:
    print("Enter valid number")

