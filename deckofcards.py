import random
from cardview import CardView
from basic_configuration import Suit

class DeckOfCards:
    def __init__(self):
        self.cards = []
        self.constructDeck()
        self.shuffled = False
        self.shuffleDeck()
        
    def constructDeck(self):
        cardNames = ["Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        cardLetters = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardSuits = [Suit.Heart, Suit.Diamond, Suit.Spade, Suit.Club]
        for j in range(4):
            thisSuit = cardSuits[j]
            for i in range(13):
                newCard = CardView(cardNames[i], thisSuit, cardValues[i], cardLetters[i])
                self.cards.append(newCard)

    def printDeck(self):
        for card in self.cards:
            print(card)

    def shuffleDeck(self):
        for i in range(len(self.cards)):
            rPos = random.randint(0,len(self.cards)-1)
            tempCard = self.cards[rPos]
            self.cards[rPos] = self.cards[i]
            self.cards[i] = tempCard
        self.shuffled = True