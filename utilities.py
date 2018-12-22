from macpath import norm_error
import random
def inputs():
    a=int(input("Enter num"))
    b = int(input("Enter num"))





def replaceStr(uname):
    str=("Hello <<UserName>>, How are you?") # String to replace username with

    if len(uname) < 3 :
        print("Username should be more than 3 chars")#name length should be more than 3
    else:
        modified_str=str.replace("<<UserName>>",uname)#new Modified String
        print(modified_str)


#******************************  FlipCoin  ******************************


def flipCoin(no_flips):
    head=0
    tail=0
    for i in range(no_flips):
        coin=random.uniform(0,1)         #random function  to generate values between 0 - 1 randomly
        if coin>=0.5:
            head+=1                      # increasing  heads count if 1 occurs
        else:
            tail+=1
    print("Total Heads ",head,"total head percentage ",(head/no_flips)*100)
    print("total tails", tail,"Total Tail percentage ",(tail/no_flips)*100)


#******************************  Leap Year  ******************************

def leapYear(year):
    if (year%4 ==0)or(year%4==0)and(year%100!=0):   # Condition to check leap year
        print("Year is leap year")
    else:
        print("Year is not leap")

#******************************  Power of Two  ******************************

def powerOfTwo(n):
    if n<=31:
        for i in range(1,n+1):              # range to find the power from 1 to "n"
            print(i, "Power of two is ", 2**i)
    else:
        print("Out of bound")


#******************************  Harmonic Number  ******************************

def harmonic(nthHarmonic):
    h=0
    for i in range(1,nthHarmonic+1):
        h+=1/i
    print("Harmonic Number ",h)

#******************************  Prime Factors  ******************************

 # Prime number is the number which is  only divisible by 1 and itself so prime-
 # factors would be the factors of that number which are prime number too.

def primefactors(num):
    for i in range(2,num):
        while (num % i == 0):
            print(i)
            num=num/i



#******************************  Gambler  ******************************

def gambler(stake,goal,no):
    wins=0
    loose=0
    #cash=stake
    bets=0
    gamble=0

    for i in range(0,no):
        cash = stake
        #print(" hh",gamble)
        while(cash>0 and cash<goal):
            bets += 1
            gamble = random.uniform(0,1)
            #print(gamble)
            #gamble = random.uniform(0, 1)
            if gamble<0.5:
                cash+=1

            else:
                cash-=1

        if (cash == goal):
            wins+=1
        else:
            loose+=1

    #print(bets)
    print("Wins ",wins ,"in turns ", no)
    print("Total wins ",wins," Winning percentage ",(wins/no)*100)
    print("Avg bets",bets/no)





#******************************  Coupoun  ******************************

def coupoun(coupounNumber):
    count=0
    l=[int(i) for i in str(coupounNumber)]
    print(l)
    while(len(l)>0):                        #Loop will run till list becomes empty
        randomnum=random.randint(0,9)       #generates random numbers
        count += 1
        if randomnum in l:
            l.remove(randomnum)             # if number is found in list then remove number
            #print(l)

    print("Total random numbers to generate coupoun ",count)



#******************************  2D Array  ******************************
import  numpy as np

def twodarray(r,c):

    twolist=[[0 for col in range(c)]for row in range(r)]

            #using MultiList concept it will prints '0' in specified number of columns and rows.
            #if total columns are 3 and total rows are 3... then we will have  a multilist like below.
            #[[0,0,0],[0,0,0],[0,0,0]]
            # List comprehension: [ [ output_expression() for(set of columns to iterate) ]for(set of rows to iterate)]

    for row in range(r):
             for col in range(c):
                 twolist[row][col]=input("Enter ele")

    print(twolist)                     #prints data in multi List
    a=np.array(twolist)                # Converting multilist to numpy array
    print(a)



#****************************** Distince Triples  ******************************

def distinctTriples(l):
    lengthoglist=len(l)
    # we want triplets so the first for loop will start from 0 and end to length -2
    # because elements after length - 2 would be j and k.
    for i in range(0,lengthoglist-2):
        for j in range(1,lengthoglist-1):
            for k in range(2,lengthoglist):
                if l[i]+l[j]+l[k]==0:
                    print(l[i],l[j],l[k])


#****************************** Euclidean distance ******************************

import math                         #library for mathematical functions
def euclidien(x,y):
    edistance=math.sqrt(x*x+y*y)    #calculating square root using Maths square root and  euclidean formula
    print("Euclidean distance :",edistance)


#****************************** String Permutations ******************************


