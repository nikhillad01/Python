import  numpy as np
class Node:
    def __init__(self, data, next=None):
        """
        This is the constructor of Node class .
        data:user given value will be stored in this variable
        next: this variable keeps the address of next node
        """
        self.data = data
        self.next = next

class Stack:
    top = 0
    head = None

    """
        This is the Stack class to create Stack.
        """


    def push(self, data):
        """
        This method is used to insert data in stack.
        data:data will given by user
         nothing
        """

        node = Node(data)

        if self.head == None:

            self.head = node
        else:

            traverse = self.head

            while traverse.next != None:
                traverse = traverse.next

            traverse.next = node

    def size(self):
            """
            This method is used to find the size of Stack.
            :return:this will return the size of stack
            """
            traverse = self.head

            if self.head == None:
                return 0
            size = 1
            while traverse.next != None:
                traverse = traverse.next
                size += 1
            return size

    def show(self):
            """
            This method is used to display content of stack.
            :return: nothing
            """
            traverse = self.head

            if self.top <= -1:
                print(" Stack Underflow")
                return
            if traverse == None:
                print("Stack is empty")
                return

            while traverse.next != None:
                print(traverse.data)
                traverse = traverse.next
            print(traverse.data)

    def pop(self):
        """
                   This method is used to delete last data which is inserted into the stack.
                   actually stack follow the Last in First Out order Principle to pop the data fromthe stack
                   :return: this will return the data that will be removed
                   """

        traverse = self.head

        if self.head == None:
            return -1

        if self.head.next == None:
            self.head = None

            return traverse.data

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:
                traverse.next = None

                return t1.data
            traverse = traverse.next


    def peek(self):
            """
            This method is used to return the last inserted item in the stack.
            :return: return the last item inserted in the stacck
            """
            traverse = self.head

            if self.head == None:
                return "empty stack"
            self.top = self.size() - 1
            for i in range(0, self.top):
                traverse = traverse.next

            return traverse.data

    def is_empty(self):
            """
            This method is used to know wheter stack is empty or not.
            :return:this will return true if stack is empty else return False
            """

            if self.size() == 0:
                return True
            else:
                return False

    def calender_stack(self, month, year):
            """
           This method is used to print calender of given month and year.
           In this method calender is created using stack
           :param month:month given ser
           :param year: year given by year
           :return: nothing
           """
            day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            values = 1
            d = 1

            m = month
            y = year
            y0 = y - (14 - m) // 12
            x = y0 + y0 // 4 - y0 // 100 + y0 // 400
            m0 = m + 12 * ((14 - m) // 12) - 2
            d0 = (d + x + 31 * m0 // 12) % 7


            row = 6
            column = 7

            print('Your Calender is Ready\n')

            for i in range(0, 7):           # prints heading
                print(day[i], end=' ')
            print()

            for i in range(row):

                for j in range(column):

                    if values <= days[m - 1]:
                        if i == 0 and j < d0:
                            stack.push(' ')             # add values using stack.
                            continue

                        stack.push(values)
                        values += 1

            for i in range(stack.size()):
                stack_element = stack.pop()  # take last element and push it using another stack. beacuse elements pushed in stack are in reversed order. so put that using another object to make it in sequence.
                stack1.push(stack_element)   # copy stack into stack1s push

            for i in range(row):

                for j in range(column):
                    if stack1.size() > 0:
                        x = stack1.pop()        # pop last element
                        x1 = str(x).ljust(2)
                        print(x1, end=" ")

                print()




stack = Stack()                 # two instances of same class will never be the same.
stack1 = Stack()

stack.calender_stack(6,1996)

