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
    refList = ["A" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",]
    testLst = []
    for card in myDeck:
        testLst.append(refList.index(card.rank))
    testLst.sort()
    for i in range (len(testLst)-2):
        if testLst[i] + 1 != testLst[i + 1]: 
            return False
    if testLst[len(testLst) -1] != testLst[len(testLst) -2] +1:
        return False
    return True

def isRoyalFlush(myDeck):
    if(not isFlush(myDeck)):
        return False
    royaltest = {}
    for card in myDeck:
        if card.rank in royaltest:
            royaltest[card.rank] +=1
        else:
            royaltest[card.rank] = 1
    if len(royaltest) != 5:
        return False
    for item in royaltest:
        if royaltest[item] != 1:
            return False
    if all(k in royaltest for k in ("K","10","J","Q","A")):
        return True
    return False

