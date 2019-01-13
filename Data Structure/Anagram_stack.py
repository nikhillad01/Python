"""******************************************************************************
* Purpose: Anagram Numbers Stack .
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 5-01-2019
*
******************************************************************************"""

from DSA import DSA_Utilities       # import Stack class from DSA_utilities.
st=DSA_Utilities.Stack()            # create instance of DSA_Utilities.Stack() .

class Stack:                        # Stack class
    def __init__(self):
        self.prime_list = []

    def get_prime(self):             # method to find prime numbers in range
        """
        This method is used to print prime  number.
       """
        for num in range(0, 1000 + 1):
                                     # prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):  # check for prime number .
                    if (num % i) == 0:
                        break
                else:
                     self.prime_list.append(num)    # appends prime numbers in prime_list .


    def anagram_stack(self):
        """
        This method is used to print prime anagram in reverse order(Stack).
        """

        anagrams = []
        self.prime_list = [str(i) for i in self.prime_list]
        for i in range(0, len(self.prime_list)):    # loop will start from 0 till end
            for j in range(i + 1, len(self.prime_list)):    # loop from i+1 to end.
                if sorted(self.prime_list[i]) == sorted(self.prime_list[j]):    # i and j elements are sorted and compared with each others .
                    st.push(self.prime_list[i])         # push element in stack.
                    st.push(self.prime_list[j])

        for i in range(0, st.size()):
            print(st.pop())             # stack removes element from back end, so it will print numbers in reverse order.
try:
    o = Stack()
    o.get_prime()
    o.anagram_stack()
except Exception as e:
    print(e)