# ccardview.py
#   Implementation of a CardView with changeable forground color
#   Illustrates inheritance

from cardview import CardView

class ColorCardView(CardView):

    def setColor(self):
        CardView.setColorCard(self)

    def setSymbol(self):
        CardView.setSymbolCard(self)