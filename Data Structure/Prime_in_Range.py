from DSA import  DSA_Utilities
o=DSA_Utilities.Stack()
import numpy as np
class prime_two_d:
    def __init__(self):
        self.prime_list = []
    def get_prime(self):
        for num in range(0, 1000 + 1):
            # prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    #print(num)
                    self.prime_list.append(num)
                   # o.push(num)
        #return num

       # print(self.prime_list)

    def two_d_Array(self):
        row = 10
        column = 25
        limit = 100
        two_d_array = [[0 for j in range(column)] for i in range(row)]
       # print(two_d_array)
        k = 0

        for i in range(row):

            for j in range(column):

                if k < len(self.prime_list):
                    if self.prime_list[k] <= limit:
                        #for l in self.prime_list:
                            two_d_array[i][j] =self.prime_list[k]
                            k += 1


            limit += 100

        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")

            print()


    def anagram(self):


        self.prime_list=[str(i) for i in self.prime_list]
        #print(self.prime_list)
        sort_words = {}
        for word in self.prime_list:
            sort_words[word] = ''.join(sorted(word))

        #print(sort_words)

        anagrams = []
        for i in range(len(self.prime_list)):
            ana = [self.prime_list[i]]
            for j in range(i + 1, len(self.prime_list)):
                if sort_words[self.prime_list[i]] == sort_words[self.prime_list[j]]:
                    ana.append(self.prime_list[j])

            if len(ana) != 1:
                anagrams.append(ana)

        print(anagrams)
        anagrams2 = [val for sublist in anagrams for val in sublist]
        anagrams2=[int(x) for x in anagrams2]
        print('flattend',anagrams2)
        f=np.array(anagrams2)
        print()
        print("Anagrams in 2D array")
        print(f)
        not_anagrams=[]
        for i in range(0,1000):

            if i not in anagrams2:
                not_anagrams.append(i)
        not_anagrams=np.array(not_anagrams)
        print()
        print("Not Anagrams and Not Prime : ")
        print(not_anagrams)

try:
    p=prime_two_d()
    p.get_prime()
    p.two_d_Array()
    p.anagram()
except Exception as e:
    print(e)
