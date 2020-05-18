import mainClasses
def numberOfTuples(mydeck = mainClasses.Deck,numberOf = int):
    pairTest = {}
    for card in mydeck:
        if card.rank in pairTest:
            pairTest[card.rank] +=1
        else:
            pairTest[card.rank] = 1
    pairNum = 0
    for item in pairTest:
        if pairTest[item] == numberOf:
            pairNum +=1
        #returns the number of pairs found
        return pairNum

def isPair(mydeck = mainClasses.Deck):
    return numberOfTuples(mydeck, 2) == 1
def isTwoPair(mydeck = mainClasses.Deck):
    return numberOfTuples(mydeck,2) == 2
def isThreeOfAKind(myhand = mainClasses.Deck):
    return numberOfTuples(mymyhand,3) == 1
def isFourOfAKind(myhand = mainClasses.Deck):
    return numberOfTuples(myhand,4) == 1