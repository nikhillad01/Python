"""******************************************************************************
* Purpose: Simulate Banking Cash Counter Using Queue .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 02-01-2019
*
******************************************************************************"""


class Queue:
    def __init__(self):             # Creating list of items
        self.items = ['Nikhil','Pushkar','Sagar','Shahazad','Jahnvi']
        self.Total_cash=1000

    def push(self, data):           # Method to append the data in queue.
        self.items.append(data)

    def pop(self):              # Method to delete the data from beginning.
        return self.items.pop(0)

    def show(self):                 # Method to print the data .
        print(self.items)
        return self.items

    def isEmpty(self):              # returns true if queue is empty
        return self.items == []

    def peek(self):                 # Returns the top item form queue but does not removes it.
        if not self.isEmpty():
            return self.items[-1]

    def __sizeof__(self):           # Calculate size of queue.
        # return self.items
        print(len(self.items))


    def deposit(self,depo_amt):                 # Method to add deposit amount.
        self.Total_cash=self.Total_cash+depo_amt
        q.pop()
        print(self.Total_cash)
        q.show()

    def withdraw(self,withdraw_amt):            # Method to withdraw amount.
        if self.Total_cash - withdraw_amt>0:            # if withdraw balance is greater than total cash in bank the users request if refused .
            self.Total_cash=self.Total_cash - withdraw_amt
            q.pop()
            print(self.Total_cash)
            q.show()
        else:
            print("Not enough balance")
            q.pop()


q=Queue()

q.show()                # prints whole queue.
try:
    for i in range(0,len(q.items)):
        print('Welcome : ',q.items[0])
        c = int(input("please select choice 1: Deposit 2: Withdraw money "))
        if c==1:
            depo_amt=int(input("Enter amount to deposit "))
            q.deposit(depo_amt)
        else:
            withdraw_amt=int(input("Enter amount to withdraw "))
            q.withdraw(withdraw_amt)
except Exception as e:
    print(e)


