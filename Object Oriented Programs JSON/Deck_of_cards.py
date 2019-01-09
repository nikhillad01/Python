import random
import numpy as np
class DeckOfCards:



    def shuffle(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

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
        return list_cards, two_d_array


card = DeckOfCards()
card.shuffle()
