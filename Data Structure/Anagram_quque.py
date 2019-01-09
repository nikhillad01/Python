"""******************************************************************************
* Purpose: Anagram Numbers Queue
*
* @author: Nikhil Lad
* @version: 3.7
* @since: 5-01-2019
*
******************************************************************************"""

from DSA import DSA_Utilities   # import queue class from DSA_utilities.
st=DSA_Utilities.Queue()        # create instance of DSA_Utilities.Queue() .

class Stack:                # Queue class
    def __init__(self):
        self.prime_list = []

    def get_prime(self):            # method to find prime numbers in range
        for num in range(0, 1000 + 1):
            # prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                     self.prime_list.append(num)


    def anagram_queue(self):
        """
        This method is used to print prime anagram number.

        """
        #anagrams = []
        self.prime_list=[str(i) for i in self.prime_list]
        for i in range(0,len(self.prime_list)):
            for j in range (i+1,len(self.prime_list)):
                if sorted(self.prime_list[i])==sorted(self.prime_list[j]):
                    st.enqueue(self.prime_list[i])
                    st.enqueue(self.prime_list[j])
        # for i in self.prime_list:
        #      st.enqueue(i)              # adds the number in queue.

        for i in range(0, st.size()):
            print('Stack: ',st.dequeue())   # queue removes the element from front end .
try:
    o = Stack()
    o.get_prime()
    o.anagram_queue()


except Exception as e:
    print(e)