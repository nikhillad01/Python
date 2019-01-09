import random
import numpy as np
from  DSA import DSA_Utilities
import re

from Utility import utilities

q1=DSA_Utilities.Queue()
q2=DSA_Utilities.Queue()
q3=DSA_Utilities.Queue()
q4=DSA_Utilities.Queue()
class DeckOfCards:



    def shuffle(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11 Jack", "12 Queen", "13 King", "14 Ace"]

        list_cards = []

        while len(list_cards) < 36:
            for i in range(0, 9):

                random_no = random.randint(1, 13)

                cards_rank = Rank[random_no - 1]

                random_no_suits = random.randint(0, 3)
                cards_rank = cards_rank + ' ' + suits[random_no_suits]

                if list_cards.__contains__(cards_rank) is False:

                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0
        for i in range(row):

            for j in range(column):
                two_d_array[i][j] = list_cards[index]
                index += 1
        #print(two_d_array)
        a=np.array(two_d_array)
        print(a)
        #print("list of cards , : ",list_cards)
        limit=9
        l1 = []
        l2=[]
        l3=[]
        l4=[]
        #print("listttttt",list_cards)
        print(list_cards[:9])
        for i in list_cards[:9]:
            i = tuple((int(i[:2]), i[2:]))
            l1.append(i)
        #l1.sort()
        l1.sort()
        print()
        print("Queue data")
        print()
        print("Player 1 Cards")

        for j in l1:
            q1.enqueue(j)

        #utilities.bubble_sort(l1)

        q1.show()
        #print("List data")
        #print(l1)
        print()
        for i in list_cards[10:19]:
            i = tuple((int(i[:2]), i[2:]))
            l2.append(i)
        l2.sort()
        print("Player 2 Cards")
        for l in l2:
            q2.enqueue(l)
        q2.show()
        print()
        for i in list_cards[19:28]:
            i = tuple((int(i[:2]), i[2:]))
            l3.append(i)
        l3.sort()
        print("Player 3 Cards")
        for m in l3:
            q3.enqueue(m)
        q3.show()
        print()
        for i in list_cards[28:37]:
             i=tuple((int(i[:2]),i[2:]))
             l4.append(i)

        l4.sort()
        print("Player 4 Cards")
        for n in l4:
            q4.enqueue(n)
        q4.show()
        #print("First two chars : ",l1[8][:2])
        #s ="13 King Diamonds"
        #s2=tuple((int(s[:2]),s[2:]))
        #print(s2)
        return list_cards, two_d_array




card = DeckOfCards()
card.shuffle()
