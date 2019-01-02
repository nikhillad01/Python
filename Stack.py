"""******************************************************************************
* Purpose: Simple Balanced Parentheses Using Stack .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 02-01-2019
*
******************************************************************************"""
# Stack is LIFO (Last In First Out). eg. stack of coins of books .

class Stack:
    def __init__(self):             # Creating list of items
        self.items = []

    def push(self, data):           # Method to append the data in stack.
        self.items.append(data)

    def pop(self):                  # Method to delete the data from end.
        return self.items.pop()

    def show(self):                 # Method to print the data .
        # print(self.items)
        return self.items

    def isEmpty(self):              # returns true if stack is empty
        return self.items == []

    def peek(self):                 # Returns the top item form stack but does not removes it.
        if not self.isEmpty():
            return self.items[-1]

    def __sizeof__(self):           # Calculate size of stack.
        # return self.items
        print(len(self.items))


s = Stack()                         # Stack class object.


exp = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"  # Expression to find Balanced Parentheses.


for i in exp:
    if i == '(':                # if i=='(' then push that into the stack.
        s.push(i)
        print(s.show())

    elif i == ')':    # if i==')' Check if stack is empty , if stack is empty then we have only ')' left so the expression is not correctly  parenthesized.
        if s.isEmpty():
            is_balanced = False
            break
        s.pop()          # else pop the last entered '(' from stack.
        print(s.show())
else:
    if s.isEmpty():                 # if stack is empty : Expression is correctly parenthesized.
        is_balanced = True
        print('Expression is correctly parenthesized.')
    else:
        is_balanced = False
        print('Expression is not correctly parenthesized.')

