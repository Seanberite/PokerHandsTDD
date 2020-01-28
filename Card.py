class Card(object):
    def __init__(self, suit="spades", value=1):
        self.suit = suit
        self.value = value

    def getCard(self):
        return [self.suit, self.value]
