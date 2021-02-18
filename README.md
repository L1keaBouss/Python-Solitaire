# Solitaire Game - based graphical user interface with animation and no sound
## Solitaire Game written in Python using graphics.py

## Overview
This is a graphical-based, Python implementation of the popular Standard card game solitaire uses one 52-card pack.
To play, simply run the **py guisolitaire.py** file using Python 3.

## 1. Dealing with cards
- This game uses a deck of 52 cards.
- There are a total of 4 sets of decks (Suit Stacks), which are empty at first.
- There are seven rows of vertical cards, all face down except for the top one. From left to right: the first vertical card column has 1 card, the second vertical card column has 2 cards, the third vertical card column has 3 cards, and so on to the rightmost vertical card column has 7 Cards.
- The remaining cards are left face down in the dealer group in the upper left corner.
- The deck in the upper left corner will issue an opened card and stay on the right side of the deck.
- The four sets of cards in the upper right corner are spades♠(Spades), hearts♥(Hearts), clubs♣(Club), and diamonds(Diamonds).

## 2. Pile of cards on four sets of cards
- The four sets of cards must start from Ace and increase in order (for example, A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K), from bottom to top.
- The seven vertical rows of cards must be spaced red and black, and from high to low. You can put a 4♥ or 4♦ on a 5♠, but you cannot put a 4♠ or 4♣.
- The game cards are taken out from the deck and opened, (press the first card of the deck to open). The game cards will gradually decrease because you must place the top card in a vertical row or four sets of cards in the upper right corner (Press the left button and drag to the desired position).
- Open the face-down cards by moving the cards in the vertical row of cards to place them in the upper right corner of the four sets of cards.

## 3. Moving cards and vertical row of cards
- Any opened cards can be used to play.
- To move a card from a vertical row, all or part of a card to another vertical row, just press the top card and move to the destination.
- Only King cards or decks starting with King can be moved to an empty vertical row of cards.
- To move the first card of the game deck, just press and move it.
- To move the first card of the game deck or vertical card row to the four sets of cards in the upper right corner, you only need to press and move - or press once to automatically put it on.
- To open the face-down cards in the vertical deck, you must first move the opened cards to another deck or empty slot.
- When you can't move any top card or deck, click on the deal set to put the new card into the game set to the right.

## 4. Game objectives
- Move the cards to the four sets of cards in the upper right corner according to the rules of the game.

## 5. Buttons
- New: Game- A New Game set
- Quit: Game Exited
- Flush All: The cards are automatically added to the four sets of cards in the upper right corner.
