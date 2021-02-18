import sys
from basic_configuration import Suit, Color

class CardView:
    """ CardView is a widget that displays a graphical representation
    of a standard Card."""
    def __init__(self, name, suit, value, letter):
        self.name = name
        self.suit = suit
        self.value = value
        self.letter = letter
        self.setColorCard()
        self.setSymbolCard()

    def __str__(self):
        return "{0} of {1}s".format(self.name, self.suit)

    def setColorCard(self):
        self.color = Color.Red if self.suit == Suit.Heart or self.suit == Suit.Diamond else Color.Black
        if self.suit == Suit.Blank:
            self.color = Color.Brown
        if self.suit == Suit.Milk:
            self.color = Color.White

    def setSymbolCard(self):
        if self.suit == Suit.Heart: self.symbolNumber = 2665
        if self.suit == Suit.Diamond: self.symbolNumber = 2666
        if self.suit == Suit.Spade: self.symbolNumber = 2660
        if self.suit == Suit.Club: self.symbolNumber = 2663
        if self.suit == Suit.Blank: self.symbolNumber =  '1f0a0'
        if self.suit == Suit.Milk: self.symbolNumber = 2619
        if sys.version_info >= (3, 0):
            self.symbol = chr(int(str(self.symbolNumber), 16))
        else:
            self.symbol = unichr(int(str(self.symbolNumber), 16))