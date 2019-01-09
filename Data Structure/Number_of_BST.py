"""******************************************************************************
* Purpose: Number of binary Search tree .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 03-01-2019
*
******************************************************************************"""
import  math
class binary_search_tree():

    def factorial_num(self,n):
       """Function to calculate  the factorial
       of a number using recursion"""
       if n == 1:
           return n
       else:
           return n*b.factorial_num(n-1)

    def count(self,n):

        """Total number of possible Binary Search Trees
            = Catalan number Cn = (2n)!/(n+1)!*n!"""
# Catalan numbers form a sequence of natural numbers that occur in various counting problems,
        n_fact=b.factorial_num(n)
        no=int((b.factorial_num(2*n))/(b.factorial_num(n+1)*n_fact)) # catalan number formula.
        print('Number of Binary Search Tree : ',no)


b=binary_search_tree()
try:
    if __name__ =="__main__":
        a=int(input("Enter number of Nodes : "))
        b.count(a)
except ValueError:
    print("Enter int value")
except KeyboardInterrupt:
    print("KeyBoard Interrupt Error")

