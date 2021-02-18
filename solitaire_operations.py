# ***** ***** ***** ***** ***** 
# Solitaire Game Basic Rules Operations
# ***** ***** ***** ***** *****
from basic_configuration import TransactionStatus, Stack

class cardPile:
    def __init__(self):
        self.type = "Generic"
        self.cards = []
        self.movingcards = 1
        self.button = None
        self.label = None

    def getTopCard(self):
        return None if len(self.cards) == 0 else self.cards[-1]

    def isSameSuit(self):
        return (self.cards[0].suit == self.travelTo.suit)

    def isOppositeColor(self):
        return (self.getTopCard().color != self.travelTo.getTopCard().color)

    def isNextFoundationCard(self):
        return (self.cards[0].value == (self.travelTo.getTopCard().value + 1))

    def isNextTableauCard(self):
        return (self.getTopCard().value == (self.travelTo.getTopCard().value - 1))

    def isEmptyTargetStack(self):
        return (len(self.travelTo.cards) == 0)

    def isAce(self):
        return (self.cards[0].value == 1)

    def isKing(self):
        return (self.getTopCard().value == 13)
        
class transaction(cardPile):
    def __init__(self, travelFrom):
        cardPile.__init__(self)
        self.type = Stack.Transaction
        self.travelFrom = travelFrom
        self.travelTo = None
        self.status = TransactionStatus.Closed

    def validate(self, inTarget):
        return self.validateFoundation() if inTarget == Stack.Foundation else self.validateTableau()

    def validateFoundation(self):
        if self.isSameSuit():
            if self.isEmptyTargetStack():
                return True if self.isAce() else False
            else:
                return True if self.isNextFoundationCard() else False
        else:
            return False

    def validateTableau(self):
        if self.isEmptyTargetStack():
            return True if self.isKing() else False
        else:
            return True if self.isNextTableauCard() and self.isOppositeColor() else False

    def makeTransaction(self, pickupCount):
        if self.status == TransactionStatus.Closed and len(self.travelFrom.cards) > 0:
            self.status = TransactionStatus.Open
            tempSet = self.travelFrom.cards[::]
            for i in range(pickupCount):
                self.cards.append(tempSet.pop())
        
    def performTransaction(self, stackType):
        return self.performToFoundation() if stackType == Stack.Foundation else self.performToTableau()

    def performToFoundation(self):
        self.travelTo.cards.append(self.travelFrom.cards.pop())
        self.travelFrom.movingcards = self.travelFrom.movingcards - 1

        # Adjust Numbers
        if self.travelFrom.movingcards <= 0:
            self.travelFrom.movingcards = 0

        if len(self.travelFrom.cards) > 0 and self.travelFrom.movingcards == 0:
            self.travelFrom.movingcards = 1
            
        self.travelTo.movingcards = self.travelTo.movingcards + 1

    def performToTableau(self):
        cardCount = len(self.cards)
        for i in range(cardCount):
            self.travelTo.cards.append(self.cards.pop())
            self.travelFrom.cards.pop()
            
        # Adjust Numbers
        self.travelFrom.movingcards = self.travelFrom.movingcards - cardCount
        
        if self.travelFrom.movingcards < 0:
            self.travelFrom.movingcards = 0

        if len(self.travelFrom.cards) > 0:
            self.travelFrom.movingcards = 1
            
        self.travelTo.movingcards = self.travelTo.movingcards + cardCount

        if len(self.travelTo.cards) == 1:
            self.travelTo.movingcards = 1
    
    def closeTransaction(self):
        self.travelTo = None
        self.travelFrom = None
        self.cards = []
        self.status = TransactionStatus.Closed

class goalPile(cardPile):
    def __init__(self, suit):
        cardPile.__init__(self)
        self.type = Stack.Foundation
        self.suit = suit

class DISCARDPILE(cardPile):
    def __init__(self):
        cardPile.__init__(self)
        self.type = Stack.Discard

class DRAWPILE(cardPile):
    def __init__(self):
        cardPile.__init__(self)
        self.type = Stack.Draw

class TABLE(cardPile):
    def __init__(self):
        cardPile.__init__(self)
        self.type = Stack.Tableau
        self.labelStack = None