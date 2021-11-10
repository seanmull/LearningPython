from random import shuffle
from Deck import Deck

class Game(object):

    def __init__(self, chips):
        self.deck = Deck()
        self.playerHand = []
        self.playerHandIndex = 0
        self.playerScore = 0
        self.dealerHand = []
        self.playerChips = chips

    def play(self):
        print("Welcome to blackjack lets two cards each for the player and dealer")
        self.initalDrawPhase()
        self.printCurrentCardsForEachPlayerForInitialDraw()

        

    def initalDrawPhase(self):
        self.playerHand.append(self.deck.takeCard())
        self.playerHand.append(self.deck.takeCard())
        self.dealerHand.append(self.deck.takeCard())
        self.dealerHand.append(self.deck.takeCard())

    def printCurrentCardsForEachPlayerForInitialDraw(self):
        print("The dealer had the following card showing:")
        print(self.dealerHand[0].face, self.dealerHand[0].suit)
        print("The player has the following hand:")
        for card in enumerate(self.playerHand):
            print(card[0],card[1].face,card[1].suit)
        self.calculateHandValueForPlayer(self.playerHand, self.playerHandIndex)
        self.playerHandIndex -= 2
        print("The player hand is currently worth ", self.playerScore)
        self.checkForAceWithPlayer(self.playerHand, self.playerHandIndex)

    
    def playerDrawACard(self):
        self.playerHand.append(self.deck.takeCard())

    def dealerDrawACard(self):
        self.dealerHand.append(self.deck.takeCard())
    
    def checkForAceWithPlayer(self, hand, index):
        for card in hand[index:]:
            self.playerHandIndex += 1
            if card.face == 'Ace':
                add10ToScore = input('You have an Ace do you want to add 10 points?')
                if(add10ToScore == 'Y'):
                    self.playerScore += 10
                    print("The player hand is currently worth ", self.playerScore)

    def decideOnValueOfAce(self, card, isWorthEleven):
        if(card.face == 'Ace' and isWorthEleven):
            card.value = 11

    def hasHandGoneOver21(self,hand):
        return self.calculateHandValue(hand) > 21

    def calculateHandValueForPlayer(self,hand,index):
        value = 0
        for card in hand[index:]:
            value += card.value
            self.playerHandIndex += 1
        self.playerScore += value





class main():
    game = Game(100)
    game.play()


if __name__ == "__main__":
    main()