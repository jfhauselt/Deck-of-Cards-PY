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
    return pairNum

def isPair(mydeck = mainClasses.Deck):
    return numberOfTuples(mydeck, 2) == 1