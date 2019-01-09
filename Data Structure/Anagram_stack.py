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
        for num in range(0, 1000 + 1):
                                     # prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
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
        for i in range(0, len(self.prime_list)):
            for j in range(i + 1, len(self.prime_list)):
                if sorted(self.prime_list[i]) == sorted(self.prime_list[j]):
                    st.push(self.prime_list[i])
                    st.push(self.prime_list[j])

        for i in range(0, st.size()):
            print(st.pop())             # stack removes element from back end, so it will print numbers in reverse order.
try:
    o = Stack()
    o.get_prime()
    o.anagram_stack()
except Exception as e:
    print(e)