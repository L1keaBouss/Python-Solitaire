# solitaireapp.py
import random, sys
from graphics import *
from deckofcards import DeckOfCards
from solitaire_operations import cardPile, transaction, goalPile, DISCARDPILE, DRAWPILE, TABLE
from ccardview import ColorCardView
from basic_configuration import Suit, Color, TransactionStatus, Stack

# Defining backgroundcolor
FELT_GREEN = color_rgb(36,115,69)

class SolitaireApp:
    def __init__(self, interface):
        self.gameDeck = DeckOfCards()
        self.o_A = TABLE()
        self.o_B = TABLE()
        self.o_C = TABLE()
        self.o_D = TABLE()
        self.o_E = TABLE()
        self.o_F = TABLE()
        self.o_G = TABLE()
        self.tableau = [self.o_A, self.o_B, self.o_C, self.o_D, self.o_E, self.o_F, self.o_G]
        self.o_heartGoal = goalPile(Suit.Heart)
        self.o_diamondGoal = goalPile(Suit.Diamond)
        self.o_spadeGoal = goalPile(Suit.Spade)
        self.o_clubGoal = goalPile(Suit.Club)
        self.o_draw = DRAWPILE()
        self.o_discard = DISCARDPILE()
        self.o_temp = transaction(None)
        self.dealCards()
        self.backCard = ColorCardView("Card_Back", Suit.Blank, 0, "__")
        self.buttonBackCard = ColorCardView("Card_Back", Suit.Blank, 0, "SolitaireGAME..")
        self.milkCard = ColorCardView("Milk", Suit.Milk, 0, ".")

        self.gameTopRow = 2 # for Grid Layout

        self.win = Frame(interface, height=500, width=640, bg=FELT_GREEN)
        self.win.pack()

        # Obligatory Game Label
        Label(self.win, text="SOLITAIRE GAME", bg="White").grid(row=0, column=0, columnspan=15)
        self.returnCardLabel(self.buttonBackCard, self.win).grid(row=1, column=0)
        for x in range(1, 14):
            self.returnCardLabel(self.backCard, self.win).grid(row=1, column=x)
        for x in range(14, 16):
            self.returnCardLabel(self.buttonBackCard, self.win).grid(row=1, column=x)

        # ***** ***** ***** ***** ***** 
        # Set up Tableau Buttons
        self.gB_A = Button(self.win, text="Select", name="_A", command=self.changeButtonA)
        self.gB_B = Button(self.win, text="Select", name="_B", command=self.changeButtonB)
        self.gB_C = Button(self.win, text="Select", name="_C", command=self.changeButtonC)
        self.gB_D = Button(self.win, text="Select", name="_D", command=self.changeButtonD)
        self.gB_E = Button(self.win, text="Select", name="_E", command=self.changeButtonE)
        self.gB_F = Button(self.win, text="Select", name="_F", command=self.changeButtonF)
        self.gB_G = Button(self.win, text="Select", name="_G", command=self.changeButtonG)
        self.tableauButtons = [self.gB_A, self.gB_B, self.gB_C, self.gB_D, self.gB_E, self.gB_F, self.gB_G]

        # Set up Tableau Cards
        self.gL_A = self.returnCardLabel(self.o_A.getTopCard(), self.win)
        self.gL_B = self.returnCardLabel(self.o_B.getTopCard(), self.win)
        self.gL_C = self.returnCardLabel(self.o_C.getTopCard(), self.win)
        self.gL_D = self.returnCardLabel(self.o_D.getTopCard(), self.win)
        self.gL_E = self.returnCardLabel(self.o_E.getTopCard(), self.win)
        self.gL_F = self.returnCardLabel(self.o_F.getTopCard(), self.win)
        self.gL_G = self.returnCardLabel(self.o_G.getTopCard(), self.win)
        self.tableauCards = [self.gL_A, self.gL_B, self.gL_C, self.gL_D, self.gL_E, self.gL_F, self.gL_G]

        # Tableau Other
        self.gL_AStack = [self.gL_A]
        self.gL_BStack = [self.gL_B]
        self.gL_CStack = [self.gL_C]
        self.gL_DStack = [self.gL_D]
        self.gL_EStack = [self.gL_E]
        self.gL_FStack = [self.gL_F]
        self.gL_GStack = [self.gL_G]
        for xcol in range(2, 14):
            aLabel = self.returnCardLabel(self.milkCard, self.win)
            aLabel.grid(row=2, column=xcol)
            self.gL_AStack.append(aLabel)
            bLabel = self.returnCardLabel(self.milkCard, self.win)
            bLabel.grid(row=3, column=xcol)
            self.gL_BStack.append(bLabel)
            cLabel = self.returnCardLabel(self.milkCard, self.win)
            cLabel.grid(row=4, column=xcol)
            self.gL_CStack.append(cLabel)
            dLabel = self.returnCardLabel(self.milkCard, self.win)
            dLabel.grid(row=5, column=xcol)
            self.gL_DStack.append(dLabel)
            eLabel = self.returnCardLabel(self.milkCard, self.win)
            eLabel.grid(row=6, column=xcol)
            self.gL_EStack.append(eLabel)
            fLabel = self.returnCardLabel(self.milkCard, self.win)
            fLabel.grid(row=7, column=xcol)
            self.gL_FStack.append(fLabel)
            gLabel = self.returnCardLabel(self.milkCard, self.win)
            gLabel.grid(row=8, column=xcol)
            self.gL_GStack.append(gLabel)

        # Set up Goal Buttons
        self.gB_Spades = Button(self.win, text="Place", command=self.placeSpade)
        self.gB_Hearts = Button(self.win, text="Place", command=self.placeHeart)
        self.gB_Clubs = Button(self.win, text="Place", command=self.placeClub)
        self.gB_Diamonds = Button(self.win, text="Place", command=self.placeDiamond)
        self.goalButtons = [self.gB_Spades, self.gB_Hearts, self.gB_Clubs, self.gB_Diamonds]

        # Set up Goal Spots
        self.gL_Spades = self.returnGoalLabel(self.o_spadeGoal.getTopCard(), Suit.Spade, self.win)
        self.gL_Hearts = self.returnGoalLabel(self.o_heartGoal.getTopCard(), Suit.Heart, self.win)
        self.gL_Clubs = self.returnGoalLabel(self.o_clubGoal.getTopCard(), Suit.Club, self.win)
        self.gL_Diamonds = self.returnGoalLabel(self.o_diamondGoal.getTopCard(), Suit.Diamond, self.win)
        self.goalCards = [self.gL_Spades, self.gL_Hearts, self.gL_Clubs, self.gL_Diamonds]

        # Set up Discard Spot
        Label(self.win, text="Discard", bg="White").grid(row=self.gameTopRow, column=14)
        self.gB_Discard = Button(self.win, text="Select", command=self.onClick_gB_Discard)
        self.gL_Discard = self.returnGoalLabel(self.o_discard.getTopCard(), Suit.Blank, self.win)

        # Set up Draw Spot
        Label(self.win, text="Draw Pile", bg="White").grid(row=self.gameTopRow, column=15)
        self.gB_Draw = Button(self.win, text="Draw", command=self.onClick_gB_Draw)


        # ***** ***** ***** ***** ***** 
        # Place Tableau Buttons
        bCount = self.gameTopRow
        for b in self.tableauButtons:
            b.grid(row=bCount, column=0)
            bCount = bCount+1

        # Place Tableau Cards
        cCount = self.gameTopRow
        for c in self.tableauCards:
            c.grid(row=cCount, column=1)
            cCount = cCount+1

        # Place Goal Buttons
        gCount = self.gameTopRow + 3
        for g in self.goalButtons:
            g.grid(row=gCount, column=15)
            gCount = gCount+1

        # Place Goal Spots
        gcCount = self.gameTopRow + 3
        for gc in self.goalCards:
            gc.grid(row=gcCount, column=14)
            gcCount = gcCount+1

        # Place Discard Spot
        self.gB_Discard.grid(row=(self.gameTopRow + 1), column=14)
        self.gL_Discard.grid(row=(self.gameTopRow + 2), column=14)

        # Place Draw Spot
        self.gB_Draw.grid(row=(self.gameTopRow + 1), column=15)


        # ***** ***** ***** ***** ***** 
        # Assign Discard Buttons to Object
        self.o_discard.button = self.gB_Discard
        self.o_discard.label = self.gL_Discard
        
        # Assign Draw Buttons to Object
        self.o_draw.button = self.gB_Draw

        # Assign Tableau Cards
        self.o_A.button = self.gB_A
        self.o_B.button = self.gB_B
        self.o_C.button = self.gB_C
        self.o_D.button = self.gB_D
        self.o_E.button = self.gB_E
        self.o_F.button = self.gB_F
        self.o_G.button = self.gB_G
        self.o_A.label = self.gL_A
        self.o_B.label = self.gL_B
        self.o_C.label = self.gL_C
        self.o_D.label = self.gL_D
        self.o_E.label = self.gL_E
        self.o_F.label = self.gL_F
        self.o_G.label = self.gL_G
        self.o_A.labelStack = self.gL_AStack
        self.o_B.labelStack = self.gL_BStack
        self.o_C.labelStack = self.gL_CStack
        self.o_D.labelStack = self.gL_DStack
        self.o_E.labelStack = self.gL_EStack
        self.o_F.labelStack = self.gL_FStack
        self.o_G.labelStack = self.gL_GStack

        # Assign Goal Spots
        self.o_spadeGoal.button = self.gB_Spades
        self.o_heartGoal.button = self.gB_Hearts
        self.o_clubGoal.button = self.gB_Clubs
        self.o_diamondGoal.button = self.gB_Diamonds
        self.o_spadeGoal.label = self.gL_Spades
        self.o_heartGoal.label = self.gL_Hearts
        self.o_clubGoal.label = self.gL_Clubs
        self.o_diamondGoal.label = self.gL_Diamonds
        
        # Do I Need a Transaction Space For Player to See Cards or just figure out how to higlight cells.
        #Label(self.win, text="Current Transaction").grid(row=self.gameTopRow+7, column=0, columnspan=5)
        #self.gL_TransactionLabel = Label(self.win, text="AB")
        #self.gL_TransactionLabel.grid(row=self.gameTopRow+7, column=6, columnspan=10)

    # ACTIONS
    def returnCardLabel(self, card, frame):
        return Label(frame, text=u"{0}{1} ".format(card.letter, card.symbol), fg=card.color, bg="White")
        
    def returnGoalLabel(self, card, suit, frame):
        if card is not None:
            return Label(frame, text=u"{0}{1} ".format(card.letter, card.symbol), fg=card.color, bg="White")
        else:
            suitCard = ColorCardView("Blank", suit, 0, ".")
            #ColorCardView(suitCard)
            return Label(frame, text=u"{0} ".format(suitCard.symbol), fg=suitCard.color, bg="White")

    # ***** ***** ***** ***** ***** 
    # Populate Goals
    # ***** ***** ***** ***** *****
    def placeSpade(self):
        self.goalTransaction(self.o_spadeGoal)

    def placeHeart(self):
        self.goalTransaction(self.o_heartGoal)

    def placeClub(self):
        self.goalTransaction(self.o_clubGoal)

    def placeDiamond(self):
        self.goalTransaction(self.o_diamondGoal)

    def goalTransaction(self, o_suitGoal):
        # Did we just hit a Place Button for no reason?
        if self.o_temp.status == TransactionStatus.Closed:
            return False
        
        # Set the Destination
        self.o_temp.travelTo = o_suitGoal
        
        # Can the Transaction Happen
        if self.o_temp.validate(Stack.Foundation):
            # Perform the Transaction
            self.o_temp.performTransaction(Stack.Foundation)
            self.o_temp.closeTransaction()
            self.gui_closeTransaction()
            self.gui_Refresh()

    def updateFoundationLabel(self, aCardStack):
        aCard = ColorCardView("Blank", aCardStack.suit, 0, ".") if len(aCardStack.cards) == 0 else aCardStack.cards[len(aCardStack.cards)-1]
        if len(aCardStack.cards) == 0:
            labelPrep = u"{0} ".format(aCard.symbol)
        else:
            labelPrep = u"{0}{1} ".format(aCard.letter, aCard.symbol)
        aCardStack.label["text"] = labelPrep
        aCardStack.label["fg"] = aCard.color
        aCardStack.label["bg"] = Color.White

    # ***** ***** ***** ***** ***** 
    # Draw a New Card Click
    # ***** ***** ***** ***** *****
    def onClick_gB_Draw(self):
        """
        Move from drawStack to discardStack
        Version 1 is 1 at a time.
        """
        # If attempting a Transaction, disable
        if self.o_temp.status == TransactionStatus.Open:
            return False

        # If Draw Stack is empty, replenish from the Discard Pile
        countDrawStack = len(self.o_draw.cards)
        if countDrawStack == 0:
            self.o_draw.cards = self.o_discard.cards[::-1]
            self.o_discard.cards = []

        # Move top of Draw Pile to Discard
        if len(self.o_draw.cards) > 0:
            self.o_discard.cards.append(self.o_draw.cards.pop())

        # UPDATE GUI
        self.gui_Refresh()
        
    # ***** ***** ***** ***** ***** 
    # Discard Button Click
    # ***** ***** ***** ***** *****
    def onClick_gB_Discard(self):
        if self.o_discard.button["text"] == "Select":
            self.select_gB_Discard()
        elif self.o_discard.button["text"] == "Cancel":
            self.o_temp.closeTransaction()
            self.gui_closeTransaction()

    def select_gB_Discard(self):
        # Ignore if there are no cards
        if len(self.o_discard.cards) == 0:
            return False

        # make a Transaction
        self.o_temp = transaction(self.o_discard)
        self.o_temp.makeTransaction(1)

        # Alter GUI Buttons
        self.gui_openTransaction(self.gB_Discard)
        self.o_discard.label["bg"] = "Yellow"

    # ***** ***** ***** ***** ***** 
    # Select Tableau Card
    # ***** ***** ***** ***** *****
    def changeButtonA(self):
        self.onClick_Button(self.o_A)
    def changeButtonB(self):
        self.onClick_Button(self.o_B)
    def changeButtonC(self):
        self.onClick_Button(self.o_C)
    def changeButtonD(self):
        self.onClick_Button(self.o_D)
    def changeButtonE(self):
        self.onClick_Button(self.o_E)
    def changeButtonF(self):
        self.onClick_Button(self.o_F)
    def changeButtonG(self):
        self.onClick_Button(self.o_G)

    def onClick_Button(self, o_Stack):
        if o_Stack.button["text"] == "Select":
            self.select_gB_ButtonX(o_Stack)
        elif o_Stack.button["text"] == "Place":
            self.place_gB_ButtonX(o_Stack)
        else: # Cancel
            self.o_temp.closeTransaction()
            self.gui_closeTransaction()

    def select_gB_ButtonX(self, o_Stack):
        # Ignore if there are no cards
        if len(o_Stack.cards) == 0:
            return False

        # make a Transaction
        self.o_temp = transaction(o_Stack)
        self.o_temp.makeTransaction(o_Stack.movingcards)

        # Alter GUI Buttons
        self.gui_openTransaction(o_Stack.button)
        o_Stack.label["bg"] = "Yellow"
        pass

    def place_gB_ButtonX(self, o_Stack):
        # Set the Destination
        self.o_temp.travelTo = o_Stack
        
        # Can the Transaction Happen
        if self.o_temp.validate(Stack.Tableau):
            # Perform the Transaction
            self.o_temp.performTransaction(Stack.Tableau)
            self.o_temp.closeTransaction()
            self.gui_closeTransaction()
            self.gui_Refresh()
        
    def changeButton(self, aButton):
        if aButton["text"]=="Place":
            aButton.config(text="Select")
        else:
            aButton.config(text="Place")
            
    def gui_openTransaction(self, fromButton):
        self.gB_A["text"] = "Cancel" if fromButton is self.gB_A else "Place"
        self.gB_B["text"] = "Cancel" if fromButton is self.gB_B else "Place"
        self.gB_C["text"] = "Cancel" if fromButton is self.gB_C else "Place"
        self.gB_D["text"] = "Cancel" if fromButton is self.gB_D else "Place"
        self.gB_E["text"] = "Cancel" if fromButton is self.gB_E else "Place"
        self.gB_F["text"] = "Cancel" if fromButton is self.gB_F else "Place"
        self.gB_G["text"] = "Cancel" if fromButton is self.gB_G else "Place"
        self.gB_Discard["text"] = "Cancel" if fromButton is self.gB_Discard else "Select"

    def gui_closeTransaction(self):
        self.gB_A["text"] = "Select"
        self.gB_B["text"] = "Select"
        self.gB_C["text"] = "Select"
        self.gB_D["text"] = "Select"
        self.gB_E["text"] = "Select"
        self.gB_F["text"] = "Select"
        self.gB_G["text"] = "Select"
        self.gB_Discard["text"] = "Select"

    def gui_Refresh(self):
        # Automove a card to Foundation Then call Gui Refresh to do it again
        # Check Discard
        if True:
            if len(self.o_discard.cards) > 0:
                    self.autoMoveToFoundation(self.o_discard)
        # Check Tableau
        if True:
            for stack in self.tableau:
                if len(stack.cards) > 0:
                    self.autoMoveToFoundation(stack)

        # update Discard Pile
        aDiscardCard = self.backCard if len(self.o_discard.cards) == 0 else self.o_discard.getTopCard()
        self.o_discard.label["text"] = u"{0}{1} ".format(aDiscardCard.letter, aDiscardCard.symbol)
        self.o_discard.label["fg"] = aDiscardCard.color
        self.o_discard.label["bg"] = "White"

        # update Foundations
        self.updateFoundationLabel(self.o_spadeGoal)
        self.updateFoundationLabel(self.o_clubGoal)
        self.updateFoundationLabel(self.o_heartGoal)
        self.updateFoundationLabel(self.o_diamondGoal)

        # update Tableau
        for stack in self.tableau:
            self.updateTableauStack(stack)

        # Update Form Number of Cards in Draw Pile
        self.gL_Draw = Label(self.win, text=str(len(self.o_draw.cards))).grid(row=(self.gameTopRow + 2), column=15)

    def autoMoveToFoundation(self, inStack):
        checkSuit = inStack.getTopCard().suit
        inStack.button.invoke()

        lowestLevel = 13
        if self.o_heartGoal.getTopCard() is not None and self.o_heartGoal.getTopCard().value < lowestLevel: lowestLevel = self.o_heartGoal.getTopCard().value
        if self.o_spadeGoal.getTopCard() is not None and self.o_spadeGoal.getTopCard().value < lowestLevel: lowestLevel = self.o_spadeGoal.getTopCard().value
        if self.o_clubGoal.getTopCard() is not None and self.o_clubGoal.getTopCard().value < lowestLevel: lowestLevel = self.o_clubGoal.getTopCard().value
        if self.o_diamondGoal.getTopCard() is not None and self.o_diamondGoal.getTopCard().value < lowestLevel: lowestLevel = self.o_diamondGoal.getTopCard().value
        if (self.o_heartGoal.getTopCard() is None) or (self.o_spadeGoal.getTopCard() is None) or (self.o_clubGoal.getTopCard() is None) or (self.o_diamondGoal.getTopCard() is None): lowestLevel = 0

        if checkSuit == Suit.Heart:
            self.o_temp.travelTo = self.o_heartGoal
        if checkSuit == Suit.Spade:
            self.o_temp.travelTo = self.o_spadeGoal
        if checkSuit == Suit.Club:
            self.o_temp.travelTo = self.o_clubGoal
        if checkSuit == Suit.Diamond:
            self.o_temp.travelTo = self.o_diamondGoal

        if self.o_temp.validate(Stack.Foundation) and self.o_temp.cards[0].value <= (lowestLevel + 2):
            self.o_temp.travelTo.button.invoke()
        if self.o_temp.status == TransactionStatus.Open: inStack.button.invoke()
        
    def updateTableauStack(self, aCardStack):
        shownCards = [self.backCard] if len(aCardStack.cards) == 0 else aCardStack.cards[-aCardStack.movingcards:]
        #print(" -- cards in Stack: {0}".format(aCardStack.movingcards))
        for pos in range(aCardStack.movingcards):
            #print(" -- {0} of {1} cards".format(pos, aCardStack.movingcards))
            aCard = shownCards[pos]
            labelPrep = u"{0}{1} ".format(aCard.letter, aCard.symbol)
            aCardStack.labelStack[pos]["text"] = labelPrep
            aCardStack.labelStack[pos]["fg"] = aCard.color
            aCardStack.labelStack[pos]["bg"] = Color.White
        for pos in range(aCardStack.movingcards,13):
            aCard = self.milkCard
            labelPrep = u"{0}{1} ".format(aCard.letter, aCard.symbol)
            aCardStack.labelStack[pos]["text"] = labelPrep
            aCardStack.labelStack[pos]["fg"] = aCard.color
            aCardStack.labelStack[pos]["bg"] = Color.White
            
    def updateTableauLabel(self, aCardStack):
        aCard = self.backCard if len(aCardStack.cards) == 0 else aCardStack.cards[len(aCardStack.cards)-1]
        labelPrep = u"{0}{1} ".format(aCard.letter, aCard.symbol)
        aCardStack.label["text"] = labelPrep
        aCardStack.label["fg"] = aCard.color
        aCardStack.label["bg"] = Color.White
    
    def dealCards(self):
        for i in range(len(self.tableau)):
            for j in range(i+1):
                self.fillStack(self.tableau[i])
        self.o_draw.cards = self.gameDeck.cards

    def fillStack(self, stack):
        stack.cards.append(self.gameDeck.cards.pop())

    def displayStack(self, stack):
        stackline = ""
        for i in stack.cards:
            stackline += u"{0}{1} ".format(i.letter, i.symbol)
        return stackline

    def __str__(self):
        layout = "SOLITAIRE GAME"
        layout += "\n---------\n"
        for i in range(len(self.tableau)):
            layout += self.displayStack(self.tableau[i])
            layout += "\n"
        return layout