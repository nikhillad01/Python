"""******************************************************************************
* Purpose: Calender using Queue and Linked List .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 04-01-2019
*
******************************************************************************"""
from DSA import DSA_Utilities
q=DSA_Utilities.Queue()             # instance of Queue class

class Queue:
    front = None
    rear = None
    def __init__(self):             # Creating list of items
        self.day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']
        self.calender_q=[]


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
                        q.push(" ")
                        continue

                    q.push(values)           # add value in queue one by one .
                    values += 1                 # increment value.

        for i in range(row):

            for j in range(column):
                if q.size() > 0:  # prints in good structure .
                    x = q.pop()
                    x1 = str(x).ljust(2)  # ljust returns left justified string  eg. str(cat).ljust(2,'*')=cat**
                    self.calender_q.append(x1)
                    print(x1, end=" ")  # ends the output with a <space>  .

            print()

q1=Queue()

if __name__=="__main__":
    try:
        year=int(input("Enter year: "))
        month=int(input("Enter month "))
    except (ValueError,KeyboardInterrupt):
        print("not valid value ")
    if month>0 and month<12:
        q1.calender(month, year)
    else:print("Month should be month > 0 and month < 12")

