import mainClasses
def numberOfTuples(mydeck,numberOf = int):
    pairTest = {}
    for card in mydeck.deckorder:
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

def isPair(mydeck : mainClasses.Deck):
    return numberOfTuples(mydeck, 2) == 1
def isTwoPair(mydeck : mainClasses.Deck):
    return numberOfTuples(mydeck,2) == 2
def isThreeOfAKind(myhand : mainClasses.Deck):
    return numberOfTuples(myhand,3) == 1
def isFourOfAKind(myhand : mainClasses.Deck):
    return numberOfTuples(myhand,4) == 1

def isFlush(mydeck):
    flushTest ={}
    for card in mydeck:
        if card.suit in flushTest:
            flushTest[card.suit] +=1
        else:
            flushTest[card.suit] = 1
    return len(flushTest) == 1

#straight can also return a royal flush so be careful later on
def isStraight(myDeck):
    if isRoyalFlush(myDeck):
        return False
    refList = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    refList2 = ["A" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]
    testLst = []
    for card in myDeck:
        testLst.append(refList.index(card.rank))
    testLst.sort()
    if testLst[len(testLst) -1] - testLst[0] == len(myDeck.deckorder) -1 :
        return True
    testLst = []
    for card in myDeck:
        testLst.append(refList2.index(card.rank))
    testLst.sort()
    if testLst[len(testLst) -1] - testLst[0] == len(myDeck.deckorder) -1:
        return True
    return False

def isRoyalFlush(myDeck):
    if(not isFlush(myDeck)):
        return False
    royaltest = {}
    for card in myDeck:
        if card.suit in royaltest:
            royaltest[card.suit] +=1
        else:
            royaltest[card.suit] = 1
    if len(royaltest) != 5:
        return False
    for items in royaltest:
        if royaltest[item] > 1:
            return False
    return royaltest.keys >= {"K","Q","J","10","A"}

