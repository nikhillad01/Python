"""******************************************************************************
* Purpose: Linked list ordered.
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************"""
class node:
    def __init__(self, data=None, next=None):
        self.data = data                # data node
        self.next = None                # last element of list will always has none .
        self.next_node = next

    def get_data(self):                  # gets the data of node
        return self.data

    def get_next(self):                  # gets next node
        return self.next

    def set_next(self, new_next):        # used while deleting: sets the next element to other next node.
        self.next = new_next


class linked_list:                      # wrapper class for node class. user will never interface with node
    def __init__(self):
        self.head = node()              # never gonna contain any actual data and not indexable.  simply used as placeholder to allow us to point to first node.

    def add(self, data):                # appends  element to list
        new_node = node(data)           # creates a new node using class node .
        current = self.head             # point to start iteration from ... first node
        while current.next != None:     # while next element  is not Null
            current = current.next      # sets the current node to next node
        current.next = new_node         # create  the new node after current node

    def length(self):                   # calculates length of list
        current = self.head             # at start nodes starts from Head
        total = 0                       # variable to count the nodes.

        while current:                  # while current = True
            total += 1                  # incrementing total.
            current = current.get_next()  # current element = next element until loop finishes
        return total

    def display(self):                   # to display list

        elemenst = []                    # list to
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elemenst.append(current_node.data)
        print('data in linked list ', elemenst)
        findword = int(input("Enter the element to search "))
        my_list.search(findword, elemenst)
        ans = int(input("want to write data in file "))
        if ans == 1:
            my_list.write(elemenst)
        else: exit()

    def search(self, data, elemenst):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
                print("Element found ")
                my_list.delete(data, elemenst)
                print("Element deleted: ")
                my_list.write(elemenst)
            else:
                current = current.get_next()
        if current is None:
            print("Data was not in list and added to list")
            my_list.add(data)
        return current

    def delete(self, data, elemenst):
        current = self.head             # starts from head node.
        previous = None
        found = False
        while current and found is False:       # iterate till current and found is false.
            if current.get_data() == data:
                found = True

            else:
                previous = current
                current = current.get_next()
        if current is None:
            print("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())       # sets the previous element address to currents next element .

    def write(self, elemenst):
        f1 = open('../Utility/test.txt', 'w')
        f1.close()
        with open('../Utility/test.txt', 'a') as f:
            elemenst.sort()
            f.write(','.join(str(word) for word in elemenst))
            #exit()


# elemenst=[]
my_list = linked_list()

file = open("../Utility/test.txt",
            'r')  # Open the file in Read mode into variable file
d = file.read().split(",")  # Read the file seperate by ,
d[-1] = d[-1].strip()

word_list = []
newd = str(d).strip('[]')
for word in d:
    word_list.append(word)

print('elements from  file : ', word_list)

for i in word_list:
    my_list.add(int(i))
print("data in linked list")
my_list.display()


my_list.display()



