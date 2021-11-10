from random import shuffle
from Card import Card

class Deck(object):

    def __init__(self):
        self.cards = []
        suits = ("Club","Spade","Heart","Diamond")
        faceValues = [("Ace", 1), ("Two",2), ("Three",3), \
                      ("Four",4), ("Five",5), ("Six",6), ("Seven",7), \
                      ("Eight" , 8), ("Nine",9), ("Ten",10), ("Jack", 10), \
                      ("Queen",10), ("King", 10)]
        for suit in suits:
            for face in faceValues:
                card = Card(face[0],suit,face[1])
                self.cards.append(card)
        shuffle(self.cards)

    def takeCard(self):
        return self.cards.pop()

    def printDeck(self):
        for c in enumerate(self.cards):
            print(c[0],c[1].face,c[1].suit,c[1].value)

