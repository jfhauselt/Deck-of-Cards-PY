import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.suit + " " + self.rank

class Deck:
    def __init__(self):
        self.deckorder = []
    def add(self,card):
        self.deckorder.append(card)
    def shuffle(self):
        random.shuffle(self.deckorder)
    def draw(self):
        return self.deckorder.pop()
    def __iter__(self):
        return self.deckorder.__iter__()
    def show(self):
        for item in self.deckorder:
            print(item)
#utilities

#creates standard 52 card deck
def createDeck():
    Suits = ["hearts","clubs","diamonds","spades"]
    Ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    tempDeck = Deck()
    for i in Suits:
        for j in Ranks:
            tempDeck.add(Card(i,j))
    return tempDeck

#takes a standard deck and creates a standard 5 card hand

def createHand(mydeck: Deck):
    tempHand = Deck()
    for i in range(5):
        tempHand.add(mydeck.draw())
    return tempHand
