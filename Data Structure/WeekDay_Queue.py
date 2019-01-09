"""******************************************************************************
* Purpose: Calender using Queue and Linked List .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 04-01-2019
*
******************************************************************************"""
class Node:
    def __init__(self, data, next=None):
        """
        This is the constructor of Node class .
        data:user given value will be stored in this variable
        next: this variable keeps the address of next node
        """
        self.data = data
        self.next = next

class Queue:
    front = None
    rear = None
    def __init__(self):             # Creating list of items
        self.day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']
        self.calender_q=[]

    def enqueue(self,data):           # Method to append the data in queue.

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

    def dequeue(self):
        """
        This method is used to delete data from the Queue.
        data will deleted according to FIFO principle
        """

        temp = self.front       # temp will store first element.
        self.front = self.front.next    # change the position of front to next.
        return temp.data        # return the data of temp node



    def calender(self,month, year):             # calender method taking month and year as parameter.
        day=self.day
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1  # start date
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12     # Gregorian calendar
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        row = 6
        column = 7
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # list comprehension to print matrix with all zeros .

        print('Calender of : ',month,'/',year)

        for i in range(0, 7):  # Heading of calender
            print(day[i], end=' ')
        print()

        for i in range(row):  # prints matrix rows  and columns .

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:  # if the date starts from middle of week  i.e. Thursday , make all days from monday to wed as ' ' .
                        q.enqueue(" ")
                        continue

                    q.enqueue(values)           # add value in queue one by one .
                    values += 1                 # increment value.

        for i in range(row):

            for j in range(column):
                if q.size() > 0:  # prints in good structure .
                    x = q.dequeue()
                    x1 = str(x).ljust(2)  # ljust returns left justified string  eg. str(cat).ljust(2,'*')=cat**
                    self.calender_q.append(x1)
                    print(x1, end=" ")  # ends the output with a <space>  .

            print()

q=Queue()


q.calender(6,1996)

print()
print()
