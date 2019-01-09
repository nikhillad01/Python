"""******************************************************************************
* Purpose: Calender .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 03-01-2019
*
******************************************************************************"""

def calender(month, year):



    day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    values = 1              # start date
    d = 1

    m = month
    y = year
    y0 = y - (14 - m) // 12                 # Gregorian Calender method .
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7


    row = 6
    column = 7
    two_d_array = [[0 for j in range(column)] for i in range(row)]      # list comprehension to print matrix

    print('Calender of Month \n')

    for i in range(0, 7):           # Heading of calender
        print(day[i], end=' ')
    print()

    for i in range(row):            # prints matrix rows  and columns .

        for j in range(column):

            if values <= days[m-1]:
                if i == 0 and j < d0:
                    two_d_array[i][j] = ' '         # if the date starts from middle of week  i.e. Thursday , make all days from monday to wed as ' ' .
                    continue

                two_d_array[i][j] = values
                values += 1

    for i in range(row):

        for j in range(column):
            if two_d_array[i][j] != 0:          # prints in good structure .
                x = two_d_array[i][j]
                x1 = str(x).center(2)           # center justified values.
                print(x1, end=" ")              # ends the output with a <space>  .

        print()

if __name__ =="__main__":
    month=int(input("Enter month : "))
    year=int(input("Enter year : "))
    calender(month,year)