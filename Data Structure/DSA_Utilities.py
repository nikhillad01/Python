"""******************************************************************************
* Purpose: Data Structure utilities .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 5-01-2019
*
******************************************************************************"""


"""This file contains  Classes of Stack and Queue"""

"""OOPS concept used Polymorphism : method overriding
i.e. same method name , different class, with same parameters"""

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
           # print(traverse.data)
            return traverse.data

    def pop(self):
        """
                   This method is used to delete last data which is inserted into the stack.
                   actually stack follow the LIFO principle to pop the data from the stack
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
stack=Stack()

class Queue:
    front = None
    rear = None
    def __init__(self):             # Creating list of items
        self.day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']
        self.calender_q=[]

    def push(self,data):           # Method to append the data in queue.

        """
                This method is used to insert data in the Queue .
                data will be given by user which data to be inserted ,
                queue follows First in First Out Principle.
                """

        node = Node(data)           # create node using node class and the data is given by user.

        if self.front == None and self.rear == None:        # if queue is empty.

            self.front = node           # create front node.
            self.rear = node            # create rear node.

        else:

            self.rear.next = node       # if queue is not empty create node after rear node.
            self.rear = self.rear.next  # change the position of rear to next.

    def size(self):
        """
        This method is used to display content of queue.
        """

        size = 1
        traverse = self.front       # starting from first element in queue.
        if self.front == None:      # if there is no elements in queue.
            return 0

        while traverse.next != None:        # traverse till next element is None.(end of queue)
            traverse = traverse.next        # change the position of traverse to next.
            size += 1                       # increment the size.
        return size

    def pop(self):
        """
        This method is used to delete data from the Queue.
        data will deleted according to FIFO principle
        """

        temp = self.front       # temp will store first element.
        self.front = self.front.next    # change the position of front to next.
        return temp.data        # return the data of temp node
    def demo(self):
        a=int(input("enter int"))

    def show(self):

        if self.front == None:
            print("Queue")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

q=Queue()