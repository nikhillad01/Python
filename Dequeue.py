"""******************************************************************************
* Purpose: Palindrome­Checker Using Dqueue .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 02-01-2019
*
******************************************************************************"""



class Deque:

    def __init__(self):
        self.items = []

    def add_rear(self, item):
          self.items.append()

    def add_front(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    def show(self):                 # Method to print the data .
        print(self.items)
        return self.items

    def pal_check(self,str1):
        for char in str1:
            dq.add_front(char)
        print(dq.items)
        match = True
        while dq.size()>1 and match:
            front = dq.remove_front()
            print('front',front)
            rear =dq.remove_rear()
            print('rear', rear)
            if front != rear:
                match = False
            else:
                match=True
        if match==True:
            print("palindrome")
        else:
            print('Not Palindrome')




dq=Deque()


str1=input("Enter string to check palindrome")
dq.pal_check(str1)
