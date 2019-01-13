"""******************************************************************************
* Purpose: Linked list Utility.
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 02-01-2019
*
******************************************************************************"""
class node:
    def __init__(self, data=None, next=None):
        """
               This is constructor of class"""
        self.data = data                # data node
        self.next = None                # last element of list will always has none .
        self.next_node = next

    def get_data(self):                 # gets the data of node
        return self.data

    def get_next(self):                 # gets next node
        return self.next

    def set_next(self, new_next):       # used while deleting: sets the next element to other next node.
        self.next = new_next


class linked_list:                      # wrapper class for node class. user will never interface with node
    def __init__(self):
        self.head = node()              # never gonna contain any actual data and not indexable.  simply used as placeholder to allow us to point to first node.

    def add(self, data):                # appends  element to list
        """
        This method is used to insert data in linked list.
               """
        new_node = node(data)           # creates a new node using class node .
        current = self.head             # point to start iteration from ... first node
        while current.next != None:     # while next element  is not Null
            current = current.next      # sets the current node to next node
        current.next = new_node         # create  the new node after current node


    def display(self):                  # to display list
        """
                This method is used to display data from linked list.
        """

        elemenst = []                   # list to store list members.
        current_node = self.head            # starts from head node.
        while current_node.next != None:    # iterates till end of list .
            current_node = current_node.next    # sets current node = next node
            elemenst.append(current_node.data)  # appends data of current node to list.
        print('data in linked list ', elemenst)
        return elemenst


    def delete(self, data, elemenst):
        current = self.head         # starts from head node.
        previous = None             # set previous element as none
        found = False
        while current and found is False:       # iterate till while current and found is false
            if current.get_data() == data:      # if data found then make Found element True.
                found = True

            else:
                previous = current          # else make current element as previous and next element as current .
                current = current.get_next()
        if current is None:         # if data not found till end .
            print("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())  # setting the next element of currents previous element to the currents next element.



my_list = linked_list()