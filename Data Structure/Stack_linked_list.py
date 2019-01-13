"""******************************************************************************
* Purpose: Stack Calender.
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 24-12-2018
*
******************************************************************************"""
from DSA import DSA_Utilities
stack=DSA_Utilities.Stack()    # two instances of same class will never be the same.
stack1=DSA_Utilities.Stack()


class Node:
    def __init__(self, data, next=None):
        """
        This is the constructor of Node class .
        data:user given value will be stored in this variable
        next: this variable keeps the address of next node
        """
        self.data = data
        self.next = next

class Stack_n:
    top = 0
    head = None



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

            m = month               # gregorian calender method.
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

            for i in range(row):            # iterate for rows.

                for j in range(column):     # iterate for columns.

                    if values <= days[m - 1]:
                        if i == 0 and j < d0:
                            stack.push(' ')             # add values using stack.
                            continue

                        stack.push(values)
                        values += 1

            for i in range(stack.size()):
                stack_element = stack.pop()  # take last element and push it using another stack. because elements pushed in stack are in reversed order.
                                             # so put that using another object to make it in sequence.
                stack1.push(stack_element)   # copy stack into stack1 push

            for i in range(row):

                for j in range(column):
                    if stack1.size() > 0:
                        x = stack1.pop()        # pop last element
                        x1 = str(x).ljust(2)
                        print(x1, end=" ")

                print()




# stack = Stack()
s1 = Stack_n()

if __name__=="__main__":
    try:
        year=int(input("Enter year: "))
        month=int(input("Enter month "))
    except (ValueError,KeyboardInterrupt):
        print("not valid value ")
    if month>0 and month<12:
        s1.calender_stack(month, year)
    else:print("Month should be month > 0 and month < 12")





