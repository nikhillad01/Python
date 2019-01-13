"""******************************************************************************
* Purpose: Palindrome ­ Checker Using Dqueue .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 02-01-2019
*
******************************************************************************"""

"""deque : double ended queue . can add or remove from both ends."""


class Deque:
    try:
        def __init__(self):
            self.items = []

        def add_rear(self, item):           # adds the elements at rear.
              self.items.append()

        def add_front(self, item):          # adds elements at front .
            self.items.insert(0, item)

        def remove_front(self):             # removes element from front .
            return self.items.pop(0)

        def remove_rear(self):              # removes elements from back.
            return self.items.pop()

        def is_empty(self):                 # check if list is empty .
            return self.items == []

        def size(self):                     # returns size of list .
            return len(self.items)
        def show(self):                 # Method to print the data .
            print(self.items)
            return self.items

        def pal_check(self,str1):
            for char in str1:
                dq.add_front(char)
            print(dq.items)
            match = True
            while dq.size()>1 and match:         # loop will run until there is only one element left in list.
                front = dq.remove_front()       # removes front element
                print('front',front)
                rear =dq.remove_rear()          # removes back element .
                print('rear', rear)
                if front != rear:               # if front and back equal match == True else false.
                    match = False
                else:
                    match=True
            if match==True:
                print("palindrome")
            else:
                print('Not Palindrome')
    except Exception as e:
        print(e)




dq=Deque()


str1=input("Enter string to check palindrome")
dq.pal_check(str1)
