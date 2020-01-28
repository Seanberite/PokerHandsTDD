class PokerHand(object):
    def __init__(self, card_list=[]):
        self.card_list = card_list
        return

    def isEmpty(self):
        if self.card_list == []:
            return True
        else:
            return False

    def getHand(self):
        return self.card_list